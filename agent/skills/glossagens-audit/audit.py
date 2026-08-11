#!/usr/bin/env python3
"""Glossagens Audit — Stufen 0–6 eines Kommentar-Audits.

Prüft ein Artikel-Bundle (content/kommentar/{gesetz}/art-{nr}/) gegen die
opencaselaw-MCP und schreibt einen JSON-Bericht. Die Prüfeinheit ist das
**Paar (Behauptungssatz, Beleg)** — nicht das Zitat allein: ein Entscheid, der
thematisch passt, die konkrete Aussage aber nicht trägt, ist der Fehler, den nur
die Prüfung gegen den tatsächlichen Satz findet.

Stufen:
  0  Inventar      — Bundle parsen: Wortlaut, Paare, Verbatim-Zitate
  1  Wortlaut      — get_law: zitierter Gesetzestext vs. geltende Fassung
  2  Existenz      — cite: existiert die Referenz?
  3  Pinpoint      — get_erwaegung: existiert E. X.Y?
  4  Verbatim      — wörtliche Zitate exakt im Quelltext?
  5  Grounding     — check_claim_support: trägt der Entscheid die Behauptung?
  6  Aktualität    — get_article_history: Belege vor Revision, fehlende Leitentscheide

Die Stufen 2–4 gaten Stufe 5: nur Paare mit existierendem Beleg kosten einen
LLM-Call. Stufe 7 (attest_response auf dem korrigierten Text) liegt beim Agenten.

Der MCP wird per HTTP-JSON-RPC angesprochen, nicht über die MCP-Client-Tools:
batchbar, cachebar, und check_claim_support wird vom Client teils mit
"Invalid request parameters" abgewiesen.

Usage:
  python3 audit.py content/kommentar/bv/art-045
  python3 audit.py content/kommentar/bv/art-045 --report /pfad/report.json
  python3 audit.py content/kommentar/bv --all          # alle Bundles eines Gesetzes
  python3 audit.py ... --no-cache                      # Cache ignorieren
"""
import argparse
import hashlib
import json
import os
import re
import sys
import time
import unicodedata
import urllib.error
import urllib.parse
import urllib.request

MCP_URL = "https://mcp.opencaselaw.ch/mcp"
# Teil des Cache-Keys: bei Änderungen am Antwort-Parsing hochzählen, sonst
# liefert der Cache Ergebnisse der alten Auswertung zurück.
PARSER_VERSION = 3
CACHE_PATH = os.path.expanduser("~/.cache/glossagens-audit/mcp-cache.json")
MIN_QUOTE_LEN = 30

CITE_LINK = re.compile(
    r"\[([^\]]*)\]\(https://mcp\.opencaselaw\.ch/entscheid/([^)#\s]+)(#[^)\s]*)?\)"
)
# Fedlex setzt Änderungsvermerke mitten in den Normsatz — vor dem Textvergleich raus.
FEDLEX_FUSSNOTE = re.compile(
    r"(Fassung gemäss|Eingefügt durch|Aufgehoben durch|Ursprünglich)\b.*?"
    r"\(\s*(AS|RO|FF|BBl)\b.*?\)\s*\.?",
    re.IGNORECASE | re.DOTALL,
)
PINPOINT = re.compile(r"\b(?:E\.|consid\.)\s*(\d+(?:\.\d+)*)")
WORTLAUT_HEAD = re.compile(
    r"^#{2,3}\s*(Gesetzeswortlaut|Gesetzestext|Wortlaut|Art\.\s.*Wortlaut)\s*$",
    re.IGNORECASE,
)
QUOTED = re.compile(r"[«\"„]([^«»\"„“]{%d,})[»\"“]" % MIN_QUOTE_LEN)

# ---------------------------------------------------------------- MCP


class Mcp:
    def __init__(self, use_cache=True):
        self.use_cache = use_cache
        self.cache = {}
        self.calls = 0
        self.hits = 0
        if use_cache and os.path.exists(CACHE_PATH):
            try:
                self.cache = json.load(open(CACHE_PATH))
            except Exception:
                self.cache = {}

    def save(self):
        if not self.use_cache:
            return
        os.makedirs(os.path.dirname(CACHE_PATH), exist_ok=True)
        json.dump(self.cache, open(CACHE_PATH, "w"))

    def call(self, tool, args, retries=2):
        key = f"v{PARSER_VERSION}:{tool}:" + json.dumps(args, sort_keys=True)
        if self.use_cache and key in self.cache:
            self.hits += 1
            return self.cache[key]

        payload = json.dumps(
            {
                "jsonrpc": "2.0",
                "id": 1,
                "method": "tools/call",
                "params": {"name": tool, "arguments": args},
            }
        ).encode()
        req = urllib.request.Request(
            MCP_URL,
            data=payload,
            headers={
                "Content-Type": "application/json",
                "Accept": "application/json, text/event-stream",
            },
        )
        last = None
        for attempt in range(retries + 1):
            try:
                with urllib.request.urlopen(req, timeout=60) as resp:
                    raw = resp.read().decode()
                result = self._parse(raw)
                self.calls += 1
                # Fehlantworten nicht cachen — sonst friert ein transienter
                # Fehler als Dauerbefund ein.
                if self.use_cache and "_error" not in result:
                    self.cache[key] = result
                return result
            except Exception as e:  # Netzfehler / Timeout
                last = e
                if attempt < retries:
                    time.sleep(1.5 * (attempt + 1))
        return {"_error": str(last)}

    @staticmethod
    def _parse(raw):
        """SSE- oder JSON-Antwort auf das innere Tool-Resultat reduzieren."""
        for line in raw.split("\n"):
            if line.startswith("data: "):
                raw = line[6:]
                break
        try:
            outer = json.loads(raw)
        except json.JSONDecodeError:
            return {"_error": "unparsable response", "_raw": raw[:400]}
        if "error" in outer:
            return {"_error": outer["error"].get("message", "mcp error")}
        try:
            text = outer["result"]["content"][0]["text"]
        except (KeyError, IndexError, TypeError):
            return {"_error": "unexpected envelope", "_raw": raw[:400]}
        # Der Server hängt an JSON-Antworten einen Hinweis-Footer an, an dem
        # json.loads scheitert — deshalb raw_decode auf dem führenden Objekt.
        stripped = text.lstrip()
        if stripped.startswith("{"):
            try:
                return json.JSONDecoder().raw_decode(stripped)[0]
            except json.JSONDecodeError:
                pass
        return {"_text": text}


# ---------------------------------------------------------------- Stufe 0


def norm(s):
    """Für Textvergleiche: Unicode, Anführungs-/Gedankenstriche, Whitespace."""
    s = unicodedata.normalize("NFKC", s)
    for a, b in [
        ("«", '"'), ("»", '"'), ("„", '"'), ("“", '"'), ("”", '"'),
        ("‘", "'"), ("’", "'"), ("–", "-"), ("—", "-"), (" ", " "),
    ]:
        s = s.replace(a, b)
    s = re.sub(r"\*+|_+|`+", "", s)          # Markdown-Auszeichnung
    s = re.sub(r"\s+", " ", s)
    return s.strip().lower()


def strip_md(s):
    s = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", s)   # Links → Linktext
    s = re.sub(r"\*+|_+|`+", "", s)
    return re.sub(r"\s+", " ", s).strip()


def ref_from_id(decision_id):
    """decision_id → menschenlesbare Referenz für `cite`."""
    d = urllib.parse.unquote(decision_id) if "%" in decision_id else decision_id
    m = re.match(r"^bge_(?:BGE_)?(\d+)[ _]([IVX]+)[ _](\d+)$", d)
    if m:
        return "BGE {} {} {}".format(*m.groups())
    m = re.match(r"^bger_(\w+)_(\d+)_(\d+)$", d)
    if m:
        return "{}_{}/{}".format(*m.groups())
    return d


def extract_wortlaut(text):
    """Blockquote-Block unter der Wortlaut-Überschrift."""
    lines = text.split("\n")
    out, flag = [], False
    for line in lines:
        if WORTLAUT_HEAD.match(line.strip()):
            flag = True
            continue
        if flag:
            if line.startswith("#") or line.startswith("> **Annotation"):
                break
            if line.startswith(">"):
                out.append(line.lstrip("> ").strip())
    return "\n".join(l for l in out if l)


def sentence_before(text, end):
    """Behauptungssatz, der bei Position `end` in den Beleg mündet."""
    head = text[:end]
    para = head.rsplit("\n\n", 1)[-1]
    parts = re.split(r"(?<=[.!?:])\s+(?=[A-ZÄÖÜ«\"*])", para)
    claim = parts[-1] if parts else para
    if len(strip_md(claim)) < 25 and len(parts) > 1:   # Fragment → Vorsatz dazu
        claim = parts[-2] + " " + claim
    return strip_md(claim).rstrip(" (").strip()


def parse_file(path, rel):
    """Ein Markdown-File → (units, quotes). Deckt beide Zitierlagen ab:
    Fliesstext-Links im Kommentar und OCL-Blöcke in rechtsprechung.md."""
    text = open(path, encoding="utf-8").read()
    body = text.split("---", 2)[2] if text.startswith("---") else text
    offset = len(text) - len(body)

    # Blockgrenzen für rechtsprechung.md. Der Beleg steht je nach Bestand in der
    # Überschrift (### [BGE …](url)) oder in einer - **OCL**-Zeile darunter; die
    # Kernaussage kann vor oder nach dem Link stehen. Deshalb Block als Ganzes.
    heads = [m.start() for m in re.finditer(r"^#{3,4}\s.*$", body, re.M)]

    def block_of(pos):
        start = None
        for h in heads:
            if h <= pos:
                start = h
            else:
                return (start, h) if start is not None else None
        return (start, len(body)) if start is not None else None

    units = []
    for m in CITE_LINK.finditer(body):
        label, decision_id, anchor = m.group(1), m.group(2), m.group(3)
        line_start = body.rfind("\n", 0, m.start()) + 1
        line = body[line_start : body.find("\n", m.end())]

        pin, claim = None, None
        blk = block_of(m.start())
        in_heading = line.lstrip().startswith("#")
        if blk and (in_heading or "**OCL**" in line):
            seg = body[blk[0] : blk[1]]
            km = re.search(r"\*\*Kernaussage\*\*:\s*(.+)", seg)
            if km:
                claim = strip_md(km.group(1).strip())
            pm = PINPOINT.search(seg.split("\n", 1)[0])   # Pinpoint aus der Überschrift
            if pm:
                pin = pm.group(1)
        if claim is None:
            claim = sentence_before(body, m.start())
        if pin is None and anchor:
            # URL-Anker codiert den Pinpoint: #e-2-1-1 → 2.1.1
            am = re.match(r"#e-([\d-]+)$", anchor)
            if am:
                pin = am.group(1).replace("-", ".")
        if pin is None:
            pm = PINPOINT.search(label) or PINPOINT.search(
                body[max(0, m.start() - 160) : m.start()]
            )
            if pm:
                pin = pm.group(1)

        units.append(
            {
                "file": rel,
                "line": body.count("\n", 0, m.start()) + text[:offset].count("\n") + 1,
                "decision_id": decision_id,
                "reference": ref_from_id(decision_id),
                "pinpoint": pin,
                "claim": claim,
                "claim_id": hashlib.sha256(norm(claim).encode()).hexdigest()[:12],
            }
        )

    # Verbatim-Zitate: nächstgelegener Beleg im selben Absatz
    wortlaut = extract_wortlaut(text)
    quotes = []
    for m in QUOTED.finditer(body):
        q = strip_md(m.group(1))
        if len(q) < MIN_QUOTE_LEN or norm(q) in norm(wortlaut):
            continue   # Gesetzeswortlaut prüft Stufe 1
        near = [u for u in units if abs(u["line"] - (body.count("\n", 0, m.start()) + 1)) <= 6]
        quotes.append(
            {
                "file": rel,
                "line": body.count("\n", 0, m.start()) + text[:offset].count("\n") + 1,
                "quote": q,
                "sources": [u["decision_id"] for u in near] or None,
            }
        )
    return units, quotes, wortlaut


def parse_bundle(bundle):
    units, quotes, wortlaut = [], [], ""
    for fname in ("_index.md", "rechtsprechung.md"):
        p = os.path.join(bundle, fname)
        if not os.path.exists(p):
            continue
        u, q, w = parse_file(p, fname)
        units += u
        quotes += q
        wortlaut = wortlaut or w
    return units, quotes, wortlaut


# ---------------------------------------------------------------- Stufen 1–4


def stufe1_wortlaut(mcp, gesetz, article, zitiert):
    if not zitiert:
        return {"status": "kein_wortlaut_block"}
    res = mcp.call("get_law", {"abbreviation": gesetz.upper(), "article": article})
    if "_error" in res:
        return {"status": "nicht_verifizierbar", "grund": res["_error"]}
    stand = res.get("consolidation_date") or res.get("as_of") or res.get("date")
    arts = res.get("articles") or []
    if arts:
        amtlich = "\n".join(a.get("text", "") for a in arts)
    elif res.get("text"):
        amtlich = res["text"]
    elif res.get("_text"):
        # get_law antwortet als Markdown: Artikelblock unter "### Art. N —"
        md = res["_text"]
        sm = re.search(r"Consolidation date:\s*(\S+)", md)
        stand = stand or (sm.group(1) if sm else None)
        block = re.split(r"^### Art\. ", md, maxsplit=1, flags=re.M)
        body = block[1] if len(block) > 1 else md
        body = re.split(r"^---\s*$", body, maxsplit=1, flags=re.M)[0]
        amtlich = "\n".join(body.split("\n")[1:])   # Überschriftszeile weg
    else:
        amtlich = ""
    if not amtlich.strip():
        return {"status": "nicht_verifizierbar", "grund": "kein Text in get_law"}
    amtlich_roh = amtlich
    amtlich = FEDLEX_FUSSNOTE.sub(" ", amtlich)

    nz, na = norm(zitiert), norm(amtlich)
    # Absatzweise: steht jeder zitierte Absatz im amtlichen Text?
    fehlend = []
    for para in [p for p in zitiert.split("\n") if len(strip_md(p)) > 20]:
        # Überschriftszeile des Blockquotes ("Art. 45 BV — Randtitel") ist kein
        # normativer Absatz und steht so nie im Fedlex-Artikeltext.
        if re.match(r"^\*{0,2}Art\.\s*\d+[a-z]*\b", strip_md(para)):
            continue
        core = norm(re.sub(r"^[¹²³⁴⁵⁶⁷⁸⁹\d]+\s*", "", strip_md(para)))
        if core and core not in na:
            fehlend.append(strip_md(para)[:120])
    status = "korrekt" if not fehlend else ("halluziniert_oder_veraltet")
    if not fehlend and len(na) > len(nz) * 1.6:
        status = "unvollstaendig"
    return {
        "status": status,
        "stand": stand,
        "nicht_im_amtlichen_text": fehlend,
        "amtlicher_text": amtlich_roh,
    }


def stufe2_existenz(mcp, units):
    out = {}
    for ref in sorted({u["reference"] for u in units}):
        res = mcp.call("cite", {"reference": ref})
        if "_error" in res:
            out[ref] = {"status": "nicht_verifizierbar", "grund": res["_error"]}
            continue
        if res.get("exists"):
            out[ref] = {
                "status": "existiert",
                "decision_id": res.get("decision_id"),
                "datum": res.get("decision_date"),
                "citation_string": res.get("citation_string_de"),
                "markdown_link": res.get("markdown_link"),
            }
        else:
            cm = res.get("close_matches") or []
            out[ref] = {
                "status": "halluziniert",
                "close_matches": [
                    {
                        "citation_string": c.get("citation_string_de"),
                        "decision_id": c.get("decision_id"),
                        "grund": c.get("match_reason"),
                    }
                    for c in cm[:3]
                ],
            }
    return out


def stufe3_pinpoints(mcp, units, existenz):
    out = {}
    for u in units:
        if not u["pinpoint"]:
            continue
        if existenz.get(u["reference"], {}).get("status") != "existiert":
            continue
        key = f"{u['reference']} E. {u['pinpoint']}"
        if key in out:
            continue
        res = mcp.call(
            "get_erwaegung",
            {"decision_id": u["reference"], "e_number": u["pinpoint"]},
        )
        if "_error" in res:
            out[key] = {"status": "nicht_verifizierbar", "grund": res["_error"]}
        elif res.get("text"):
            out[key] = {"status": "existiert", "text": res["text"]}
        else:
            out[key] = {
                "status": "pinpoint_fehlt",
                "vorhandene": res.get("sibling_erwaegungen") or res.get("siblings"),
            }
    return out


def stufe4_verbatim(mcp, quotes, existenz):
    out = []
    for q in quotes:
        haystack, geprueft = "", []
        for did in q["sources"] or []:
            ref = ref_from_id(did)
            if existenz.get(ref, {}).get("status") != "existiert":
                continue
            geprueft.append(ref)
            for tool, args in (
                ("get_regeste", {"decision_id": ref}),
                ("get_decision_structure", {"decision_id": ref}),
            ):
                res = mcp.call(tool, args)
                if "_error" not in res:
                    haystack += " " + json.dumps(res, ensure_ascii=False)
        if not geprueft:
            status = "keine_pruefbare_quelle"
        elif norm(q["quote"]) in norm(haystack):
            status = "verbatim_ok"
        else:
            status = "nicht_gefunden"
        out.append({**q, "status": status, "geprueft_gegen": geprueft})
    return out


def stufe5_grounding(mcp, units, existenz, pinpoints):
    """Trägt der Beleg die Behauptung? Nur für Paare, die 2–4 überlebt haben."""
    out, seen = [], {}
    for u in units:
        e = existenz.get(u["reference"], {})
        if e.get("status") != "existiert":
            continue
        pin = u["pinpoint"]
        if pin and pinpoints.get(
            f"{u['reference']} E. {pin}", {}
        ).get("status") != "existiert":
            pin = None   # ungültiger Pinpoint → Entscheid als Ganzes prüfen
        # Kein brauchbarer Behauptungssatz extrahierbar → als Befund melden,
        # nicht dem Richter vorwerfen (er antwortet sonst mit einem Fehler).
        if len(re.sub(r"[^\wäöüÄÖÜ]", "", u["claim"])) < 20:
            out.append(
                {
                    "file": u["file"],
                    "line": u["line"],
                    "claim_id": u["claim_id"],
                    "claim": u["claim"],
                    "reference": u["reference"],
                    "pinpoint": pin,
                    "supports": "claim_nicht_extrahierbar",
                    "confidence": None,
                    "begruendung": "Parser fand keinen Behauptungssatz — Zitierlage prüfen",
                }
            )
            continue

        did = e.get("decision_id") or u["decision_id"]
        key = (u["claim_id"], did, pin)
        if key in seen:
            out.append({**seen[key], "file": u["file"], "line": u["line"]})
            continue

        args = {"claim": u["claim"], "decision_id": did}
        if pin:
            args["pinpoint"] = pin
        res = mcp.call("check_claim_support", args)
        rec = {
            "file": u["file"],
            "line": u["line"],
            "claim_id": u["claim_id"],
            "claim": u["claim"],
            "reference": u["reference"],
            "pinpoint": pin,
            "supports": res.get("supports", "nicht_verifizierbar"),
            "confidence": res.get("confidence"),
            "geprueft_gegen": res.get("checked_text_source"),
            "begruendung": res.get("reasoning"),
            "beleg_exzerpt": res.get("supporting_excerpt"),
        }
        if "supports" not in res:
            rec["supports"] = "nicht_verifizierbar"
            rec["begruendung"] = (
                res.get("_error")
                or (res.get("_text") or "")[:200]
                or f"unerwartete Antwort, Felder: {sorted(res)[:8]}"
            )
        seen[key] = rec
        out.append(rec)
    return out


def stufe6_aktualitaet(mcp, sr_number, article, existenz):
    """Sind die Belege zeitlich noch aussagekräftig, und welche Entscheide
    gehören überhaupt zum Artikel?"""
    if not sr_number:
        return {"status": "uebersprungen", "grund": "keine SR-Nummer im Frontmatter"}
    res = mcp.call(
        "get_article_history", {"sr_number": sr_number, "article": article}
    )
    if "_error" in res or "_text" in res:
        return {
            "status": "nicht_verifizierbar",
            "grund": res.get("_error") or res.get("_text", "")[:200],
        }

    timeline = res.get("timeline") or []
    revisionen = sorted(
        t["date"] for t in timeline if t.get("kind") != "court_decision" and t.get("date")
    )
    letzte_revision = revisionen[-1] if revisionen else None

    vor_revision = []
    if letzte_revision:
        for ref, v in existenz.items():
            if v.get("status") == "existiert" and v.get("datum"):
                if v["datum"] < letzte_revision:
                    vor_revision.append(
                        {"referenz": ref, "datum": v["datum"], "revision": letzte_revision}
                    )

    einschlaegig = [
        {"decision_id": t["decision_id"], "datum": t.get("date")}
        for t in timeline
        if t.get("kind") == "court_decision" and t.get("decision_id")
    ]
    zitiert_ids = {v.get("decision_id") for v in existenz.values() if v.get("decision_id")}
    return {
        "status": "geprueft",
        "letzte_revision": letzte_revision,
        "konsolidierung": (res.get("statute") or {}).get("consolidation_date"),
        "belege_vor_revision": vor_revision,
        "einschlaegige_entscheide_gesamt": len(einschlaegig),
        "davon_im_kommentar_zitiert": len(
            [e for e in einschlaegig if e["decision_id"] in zitiert_ids]
        ),
        "nicht_zitierte_einschlaegige": [
            e["decision_id"] for e in einschlaegig if e["decision_id"] not in zitiert_ids
        ][:20],
    }


def sr_from_gesetz(bundle):
    """SR-Nummer aus dem Frontmatter der Gesetzesübersicht."""
    p = os.path.join(os.path.dirname(bundle.rstrip("/")), "_index.md")
    if not os.path.exists(p):
        return None
    m = re.search(r'^sr:\s*"?([\d.]+)"?', open(p, encoding="utf-8").read(), re.M)
    return m.group(1) if m else None


# ---------------------------------------------------------------- Bericht


def audit_bundle(mcp, bundle, gesetz, article):
    units, quotes, wortlaut = parse_bundle(bundle)
    w = stufe1_wortlaut(mcp, gesetz, article, wortlaut)
    ex = stufe2_existenz(mcp, units)
    pp = stufe3_pinpoints(mcp, units, ex)
    vb = stufe4_verbatim(mcp, quotes, ex)
    gr = stufe5_grounding(mcp, units, ex, pp)
    ak = stufe6_aktualitaet(mcp, sr_from_gesetz(bundle), article, ex)

    halluziniert = [r for r, v in ex.items() if v["status"] == "halluziniert"]
    ungestuetzt = [
        g for g in gr if g["supports"] in ("no", "contradicts", "unrelated")
    ]
    # Belegquote: `partial` zählt halb — die Aussage ist tragfähig, aber zu
    # weit gefasst. Nicht beurteilte Paare bleiben aus dem Nenner.
    beurteilt = [
        g for g in gr
        if g["supports"] in ("yes", "partial", "no", "contradicts", "unrelated")
    ]
    ja = len([g for g in beurteilt if g["supports"] == "yes"])
    teils = len([g for g in beurteilt if g["supports"] == "partial"])
    quote = round((ja + 0.5 * teils) / len(beurteilt) * 100) if beurteilt else None
    urteil = None if quote is None else ("A" if quote >= 80 else "B" if quote >= 50 else "C")
    return {
        "bundle": bundle,
        "gesetz": gesetz.upper(),
        "artikel": article,
        "stufe0_inventar": {
            "paare": len(units),
            "unique_referenzen": len(ex),
            "verbatim_zitate": len(quotes),
            "wortlaut_gefunden": bool(wortlaut),
        },
        "stufe1_wortlaut": w,
        "stufe2_existenz": ex,
        "stufe3_pinpoints": pp,
        "stufe4_verbatim": vb,
        "stufe5_grounding": gr,
        "stufe6_aktualitaet": ak,
        "units": units,
        "zusammenfassung": {
            "wortlaut_status": w["status"],
            "referenzen_halluziniert": halluziniert,
            "pinpoints_fehlend": [
                k for k, v in pp.items() if v["status"] == "pinpoint_fehlt"
            ],
            "verbatim_abweichend": [
                f"{q['file']}:{q['line']}" for q in vb if q["status"] == "nicht_gefunden"
            ],
            "belege_ungestuetzt": [
                f"{g['file']}:{g['line']} {g['reference']} → {g['supports']}"
                for g in ungestuetzt
            ],
            "claims_nicht_extrahierbar": [
                f"{g['file']}:{g['line']}"
                for g in gr
                if g["supports"] == "claim_nicht_extrahierbar"
            ],
            "belege_beurteilt": len(beurteilt),
            "belege_gestuetzt": ja,
            "belege_teilweise": teils,
            "belegquote_prozent": quote,
            "urteil": urteil,
        },
    }


def article_from_dir(bundle):
    m = re.match(r"art-0*(\d+)([a-z]*)$", os.path.basename(bundle.rstrip("/")))
    return (m.group(1) + m.group(2)) if m else None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("pfad", help="Bundle (art-045) oder Gesetzesverzeichnis mit --all")
    ap.add_argument("--all", action="store_true", help="alle art-*-Bundles darunter")
    ap.add_argument("--report", default=None)
    ap.add_argument("--no-cache", action="store_true")
    args = ap.parse_args()

    pfad = os.path.abspath(args.pfad)
    if args.all:
        bundles = sorted(
            os.path.join(pfad, d)
            for d in os.listdir(pfad)
            if d.startswith("art-") and os.path.isdir(os.path.join(pfad, d))
        )
        gesetz = os.path.basename(pfad)
    else:
        bundles = [pfad]
        gesetz = os.path.basename(os.path.dirname(pfad))

    mcp = Mcp(use_cache=not args.no_cache)
    reports = []
    for b in bundles:
        art = article_from_dir(b)
        if not art:
            print(f"übersprungen (kein art-Bundle): {b}", file=sys.stderr)
            continue
        print(f"→ {gesetz.upper()} Art. {art}", file=sys.stderr)
        r = audit_bundle(mcp, b, gesetz, art)
        reports.append(r)
        s = r["zusammenfassung"]
        print(
            f"   Paare={r['stufe0_inventar']['paare']} "
            f"Wortlaut={s['wortlaut_status']} "
            f"halluziniert={len(s['referenzen_halluziniert'])} "
            f"Pinpoint-Fehler={len(s['pinpoints_fehlend'])} "
            f"gestützt={s['belege_gestuetzt']}(+{s['belege_teilweise']} teilw.)"
            f"/{s['belege_beurteilt']} "
            f"→ {s['belegquote_prozent']}% Urteil {s['urteil']}",
            file=sys.stderr,
        )
    mcp.save()

    out = args.report or os.path.join(
        bundles[0] if not args.all else pfad, "audit-report.json"
    )
    json.dump(
        {"timestamp": time.strftime("%Y-%m-%d %H:%M:%S"), "reports": reports},
        open(out, "w"),
        indent=2,
        ensure_ascii=False,
    )
    print(
        f"\nMCP-Calls: {mcp.calls} (Cache-Treffer: {mcp.hits})\nBericht: {out}",
        file=sys.stderr,
    )


if __name__ == "__main__":
    main()
