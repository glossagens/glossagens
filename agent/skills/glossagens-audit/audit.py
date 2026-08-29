#!/usr/bin/env python3
"""Glossagens Audit — Stufen 0–6 eines Kommentar-Audits.

Prüft ein Artikel-Bundle (content/kommentar/{gesetz}/art-{nr}/) gegen die
opencaselaw-MCP und schreibt einen JSON-Bericht. Die Prüfeinheit ist das
**Paar (Behauptungssatz, Beleg)** — nicht das Zitat allein: ein Entscheid, der
thematisch passt, die konkrete Aussage aber nicht trägt, ist der Fehler, den nur
die Prüfung gegen den tatsächlichen Satz findet.

Stufen:
  0  Inventar      — Bundle parsen: Wortlaut, Paare, Verbatim-Zitate
  1  Wortlaut      — Fedlex: zitierter Gesetzestext vs. geltende Fassung
  2  Existenz      — cite: existiert die Referenz?
  3  Pinpoint      — get_erwaegung: existiert E. X.Y?
  4  Verbatim      — wörtliche Zitate exakt im Quelltext?
  5  Grounding     — Judge-Verdikt: trägt der Entscheid die Behauptung?
  6  Aktualität    — get_article_history: Belege vor Revision, fehlende Leitentscheide

Dieses Skript ruft **kein** LLM-Tool der opencaselaw-MCP mehr auf. Stufe 5 lief
früher über `check_claim_support`, das serverseitig ein Sonnet-Aufruf ist und
opencaselaw pro Paar Geld kostet (allein aus diesem Repo 16 359 Aufrufe). Das
Urteil fällt jetzt ein Judge-Subagent des jeweiligen Agenten — Claude Code,
Antigravity oder Hermes — gegen den Prüftext, den dieses Skript vorher über die
kostenfreien Lookups holt. Das Skript selbst bleibt LLM-frei: es stellt Jobs,
nimmt Verdikte an, prüft sie mechanisch und rechnet die Belegquote.

Genutzt werden nur Lookup-Tools (`cite`, `get_law`, `get_erwaegung`,
`get_regeste`, `get_decision`, `get_article_history`) — Datenbankabfragen ohne
LLM-Anteil. Die Stufen 2–4 gaten Stufe 5 weiterhin: für ein halluziniertes
Zitat wird kein Judge bemüht. Stufe 7 (Schlussattest) ist kein eigenes Tool
mehr, sondern ein erneuter Lauf über den korrigierten Text.

Der MCP wird per HTTP-JSON-RPC angesprochen, nicht über die MCP-Client-Tools:
batchbar und cachebar.

Usage:
  python3 audit.py content/kommentar/bv/art-045
  python3 audit.py content/kommentar/bv/art-045 --report /pfad/report.json
  python3 audit.py content/kommentar/bv --all          # alle Bundles eines Gesetzes
  python3 audit.py ... --no-cache                      # Cache ignorieren

  # Stufe 5 ohne opencaselaw-Kosten: Jobs ausgeben, urteilen lassen, einlesen
  python3 audit.py content/kommentar/bv/art-045 --emit-jobs
  python3 audit.py --ingest audit-jobs/bv-045
  python3 audit.py --import-cache      # Altbestand aus dem MCP-Cache übernehmen
"""
import argparse
import hashlib
import json
import os
import re
import sys
import threading
import time
import unicodedata
import urllib.error
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed

MCP_URL = "https://mcp.opencaselaw.ch/mcp"
# Gesetzeswortlaute gehören NICHT hierher: Der authentische Normtext kommt aus der
# Fedlex-MCP (mcp__fedlex-connector__get_article / get_law_text). opencaselaws `get_law`
# ist nur Rückfallebene für kantonales Recht und für Normen, die Fedlex nicht führt.
# Seit der IP-Sperre vom 23.08.2026 (HTTP 403) liefert `get_law` hier ohnehin nichts mehr,
# weshalb Stufe 1 stillschweigend ausfällt — siehe stufe1_wortlaut().
# Tools, die serverseitig ein LLM anwerfen und opencaselaw damit Geld kosten.
# Sie werden hier nie aufgerufen — `Mcp.call` blockt sie, damit sie auch nicht
# versehentlich über eine neue Stufe zurückkommen. Der Ersatz für Stufe 5 steht
# im Abschnitt „Judge-Ledger"; `attest_response` und `reflect` haben in diesem
# Skript nie eine Entsprechung gehabt.
BILLED_TOOLS = {"check_claim_support", "attest_response", "reflect"}
# Suchtools kosten serverseitig ebenfalls einen (kleinen) LLM-Anteil
# — Query-Parse, Expansion, Rerank. Dieses Skript braucht keine Suche; die
# Liste steht hier, damit eine künftige Stufe nicht unbemerkt eine aufmacht.
SEARCH_TOOLS = {
    "search", "search_decisions", "search_laws", "search_legislation",
    "search_scholarship", "search_botschaft", "search_practice",
    "search_commentaries", "search_materialien", "find_relevant_erwaegung",
    "find_leading_cases", "find_citations", "find_scholarship_citing_decision",
    "find_scholarship_citing_statute",
}
# Teil des Cache-Keys: bei Änderungen am Antwort-Parsing hochzählen, sonst
# liefert der Cache Ergebnisse der alten Auswertung zurück.
PARSER_VERSION = 10
CACHE_PATH = os.path.expanduser("~/.cache/glossagens-audit/mcp-cache.json")
MIN_QUOTE_LEN = 30
# Stufe 5 ist ~98% der Laufzeit: check_claim_support ist serverseitig ein
# LLM-Aufruf (ø ~5 s), die übrigen Stufen sind Datenbank-Lookups (ø ~0.1 s).
# Die Calls sind voneinander unabhängig, also laufen sie parallel.
MAX_WORKERS = int(os.environ.get("GLOSSAGENS_AUDIT_JOBS", "8"))

SKILL_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.abspath(os.path.join(SKILL_DIR, "..", "..", ".."))
# Der Ledger liegt im Repo, nicht unter ~/.cache: Claude Code, Antigravity und
# Hermes laufen auf verschiedenen Maschinen: ein maschinenlokaler Cache wäre
# für jeden ein anderer, und ein Verdikt soll nachprüfbar festhalten, welches
# Modell es gefällt hat — dieselbe Logik wie beim `revisions`-Vermerk.
LEDGER_PATH = os.environ.get(
    "GLOSSAGENS_JUDGE_LEDGER", os.path.join(SKILL_DIR, "verdicts", "ledger.jsonl")
)
JOBS_ROOT = os.environ.get(
    "GLOSSAGENS_JUDGE_JOBS", os.path.join(REPO_ROOT, "audit-jobs")
)
# Promptfassung des Judge (judge-prompt.md). Teil der job_id: wird der Prompt
# geändert, sind alte Verdikte nicht mehr vergleichbar und müssen neu ergehen.
JUDGE_PROMPT_VERSION = 1
SUPPORTS_ENUM = ("yes", "partial", "no", "contradicts", "unrelated")
# Textbudget für den Volltext-Rückfall — gleicher Wert, den der
# opencaselaw-Server intern verwendete.
VOLLTEXT_BUDGET = 4000

# Höflichkeitsbremse. nginx bei opencaselaw lässt 30 req/s zu; acht parallele
# Lookups ohne Bremse erzeugen kurze Spitzen weit darüber. Am 23.08.2026 hat
# der Betreiber diesen Client per IP gesperrt — Grund laut nginx-Konfiguration:
# «4,229 verify_claim attempts in one day against a 200/day quota, retry loop
# with no backoff». Die Bremse hier ist die Antwort darauf: fester Abstand
# zwischen Requests, exponentieller Backoff, und bei 403/429 wird der Lauf
# abgebrochen statt weitergehämmert.
REQ_PRO_SEK = float(os.environ.get("GLOSSAGENS_AUDIT_RPS", "4"))

CITE_LINK = re.compile(
    r"\[([^\]]*)\]\((https://(?:mcp\.opencaselaw\.ch/entscheid/|entscheidsuche\.ch/docs/)[^)#\s]+)(#[^)\s]*)?\)"
)
# Unverlinkte Zitierungen im Fliesstext. Ein grosser Teil des Bestands zitiert
# ohne Link (BV Art. 5/8/10/13/16/30/31/32/36 überhaupt nur so); würde der Parser
# nur CITE_LINK kennen, meldete er für diese Artikel «0 Paare» — ein Freispruch
# aus Blindheit, nicht aus Belegtheit.
CITE_PLAIN = re.compile(
    r"\b(?:BGE\s+\d+\s+[IVX]+[a-z]?\s+\d+"          # BGE 146 I 49
    r"|\d[A-Z]?_\d+/\d{4}"                          # 1C_123/2020, 6B_1/2019
    r"|[A-Z]{1,3}-\d+/\d{4})"                       # BVGer A-1234/2019
)
ANY_MD_LINK = re.compile(r"\[[^\]]*\]\([^)\s]*\)")
BLOCK_CLAIM = re.compile(
    r"\*\*(Kernaussage|Kernsatz|Regeste|Entscheid|Bedeutung|Aussage)\*?\*?:?\*\*?\s*:?\s*(.+)"
)
# Welches Feld eines Entscheidblocks die Rechtsbehauptung trägt. `Sachverhalt`
# und `Rechtsfrage` fehlen bewusst: Sachverhalt ist Tatsachenschilderung,
# Rechtsfrage eine Frage — beide sind als Behauptungssatz unbrauchbar.
CLAIM_RANG = {
    "Kernaussage": 0, "Kernsatz": 0, "Regeste": 1,
    "Entscheid": 2, "Bedeutung": 3, "Aussage": 3,
}
# «**E. 5.1**: <Aussage>» — Pinpoint und die dazu behauptete Aussage in einer Zeile.
E_CLAIM = re.compile(r"^\s*[-*]?\s*\*\*E\.\s*(\d+(?:\.\d+)*)\*\*\s*:?\s*(.+)$", re.M)
# Führende Normenkette einer Regeste («Art. 5 Abs. 2, Art. 8, Art. 10 BV.») —
# als Behauptungssatz wertlos, verwässert aber die Grounding-Prüfung.
REGESTE_NORMKETTE = re.compile(
    r"^(?:Art\.\s*[\d\w]+[^.;]*?[.;]\s*)+(?=[A-ZÄÖÜ])"
)
FEDLEX_FUSSNOTE = re.compile(
    r"(?:(?:Fassung|Ausdruck)(?:\s+[\w\s]+)?\s+gemäss|"
    r"(?:[A-Za-zÄÖÜäöü]+\s+)?Satz eingefügt durch|"
    r"Eingefügt durch|Aufgehoben durch|Ursprünglich|Berichtigt von)\b.*?"
    r"(?:AS|RO|FF|BBl)\s+\d{4}\s+[^.)]*\)?\.?(?:\s*Diese\s+[^.]*?\.\s*wurde\s+[^.]*\.)?\s*",
    re.IGNORECASE | re.DOTALL,
)
PINPOINT = re.compile(r"\b(?:E\.|consid\.)\s*(\d+(?:\.\d+)*)")
# Urteilsdatum zwischen Referenz und Pinpoint: «v. 22.4.2026», «vom 2. März 2026»,
# gefolgt von optionalen Klammerzusätzen («, 5er-Besetzung»).
DATUM_TAIL = (
    r"(?:\s*,?\s*(?:vom|v\.)\s*\d{1,2}\.\s*(?:\d{1,2}\.|[A-Za-zÄÖÜäöü]+\s*)\s*\d{4})?"
)
WORTLAUT_HEAD = re.compile(
    # Gliederungspräfixe zulassen («## I. Wortlaut», «## 1. Gesetzestext»): ohne
    # sie meldet Stufe 1 `kein_wortlaut_block` und prüft den Normtext stillschweigend
    # nicht — ein blinder Fleck genau dort, wo der Artikel das Gesetz zitiert.
    r"^#{2,3}\s*(?:[IVXLC]+|\d+)?[.)]?\s*"
    r"(Gesetzeswortlaut|Gesetzestext|Wortlaut|Normtext|Art\.\s.*Wortlaut)\s*$",
    re.IGNORECASE,
)
QUOTED = re.compile(r"[«\"„]([^«»\"„“]{%d,})[»\"“]" % MIN_QUOTE_LEN)
# Ein Audit-Protokoll listet die entfernten Falschzitate mit Namen. Ohne diese
# Ausnahme meldet der nächste Lauf genau die Referenzen wieder, die der letzte
# ausgebaut hat — die Transparenz über eine Korrektur würde als Fehler gezählt.
AUSGEBAUT_HEAD = re.compile(
    r"^#{2,4}\s*(Entfernte Entscheide|Entfernte Belege|Nicht übernommen|"
    r"Ausgebaute Zitate|Audit-Protokoll)\b",
    re.IGNORECASE | re.M,
)

# ---------------------------------------------------------------- MCP


class Mcp:
    def __init__(self, use_cache=True):
        self.use_cache = use_cache
        self.cache = {}
        self.calls = 0
        self.hits = 0
        self.lock = threading.Lock()   # call() läuft aus mehreren Threads
        self.takt = threading.Lock()   # serialisiert den Requestabstand
        self.letzter_req = 0.0
        self.blockiert = None          # gesetzt bei 403/429: keine weiteren Requests
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
        # Kostenschutz: LLM-Tools gehen nie ins Netz. Ein bereits bezahltes
        # Ergebnis aus dem Altbestand darf gelesen werden — es kostet nichts
        # mehr —, ein neuer Aufruf nicht.
        if tool in BILLED_TOOLS:
            key = f"v{PARSER_VERSION}:{tool}:" + json.dumps(args, sort_keys=True)
            if self.use_cache and key in self.cache:
                with self.lock:
                    self.hits += 1
                return self.cache[key]
            return {
                "_error": (
                    f"{tool} ist gesperrt: serverseitiger LLM-Aufruf, der "
                    "opencaselaw Kosten verursacht. Stufe 5 urteilt über den "
                    "Judge-Ledger (--emit-jobs / --ingest), siehe SKILL.md."
                )
            }

        key = f"v{PARSER_VERSION}:{tool}:" + json.dumps(args, sort_keys=True)
        if self.use_cache:
            with self.lock:
                if key in self.cache:
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
                "User-Agent": "glossagens-audit/1.0 (https://glossagens.ch)",
            },
        )
        if self.blockiert:
            # Ein einmal abgewiesener Client fragt nicht weiter. Genau die
            # fehlende Bremse hat zur Sperre geführt.
            return {"_error": self.blockiert}

        last = None
        for attempt in range(retries + 1):
            try:
                self._takten()
                with urllib.request.urlopen(req, timeout=60) as resp:
                    raw = resp.read().decode()
                result = self._parse(raw)
                with self.lock:
                    self.calls += 1
                    # Fehlantworten nicht cachen — sonst friert ein transienter
                    # Fehler als Dauerbefund ein.
                    if self.use_cache and "_error" not in result:
                        self.cache[key] = result
                return result
            except urllib.error.HTTPError as e:
                if e.code in (403, 429):
                    grund = (
                        "opencaselaw antwortet mit HTTP {}. Der Lauf bricht ab, "
                        "statt weiterzufragen. 403 = dieser Client ist gesperrt "
                        "(Kontakt: team@jonashertner.com), 429 = Tageskontingent "
                        "erschöpft.".format(e.code)
                    )
                    with self.lock:
                        self.blockiert = grund
                    return {"_error": grund}
                last = e
                if attempt < retries:
                    time.sleep(2.0 ** attempt)
            except Exception as e:  # Netzfehler / Timeout
                last = e
                if attempt < retries:
                    time.sleep(2.0 ** attempt)
        return {"_error": str(last)}

    def _takten(self):
        """Mindestabstand zwischen zwei Requests, über alle Threads hinweg."""
        if REQ_PRO_SEK <= 0:
            return
        abstand = 1.0 / REQ_PRO_SEK
        with self.takt:
            warten = self.letzter_req + abstand - time.monotonic()
            if warten > 0:
                time.sleep(warten)
            self.letzter_req = time.monotonic()

    def call_many(self, tool, args_by_key, workers=None):
        """Unabhängige Calls desselben Tools parallel; Ergebnis je Key.

        Ein Fehlschlag betrifft nur seinen Key — `call` fängt Netzfehler ab und
        liefert `{"_error": ...}`, die Stufen behandeln das bereits als
        `nicht_verifizierbar`."""
        if not args_by_key:
            return {}
        keys = list(args_by_key)
        n = min(workers or MAX_WORKERS, len(keys))
        if n <= 1:
            return {k: self.call(tool, args_by_key[k]) for k in keys}
        with ThreadPoolExecutor(max_workers=n) as ex:
            futs = {ex.submit(self.call, tool, args_by_key[k]): k for k in keys}
            return {futs[f]: f.result() for f in as_completed(futs)}

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


# ---------------------------------------------------------------- Judge-Ledger
#
# Stufe 5 fragt nicht mehr bei opencaselaw nach, ob ein Entscheid eine
# Behauptung trägt — dieser Aufruf war serverseitig ein LLM-Call und damit die
# Kostenstelle des ganzen Audits. Stattdessen:
#
#   1. `--emit-jobs` schreibt für jedes noch unbeurteilte Paar einen Job mit
#      vorgeholtem Prüftext. Ein Job ist selbsttragend: der Judge braucht weder
#      Repo noch Netz noch Werkzeuge — nur Prompt und Text.
#   2. Ein Judge-Subagent des jeweiligen Agenten urteilt (judge-prompt.md).
#   3. `--ingest` prüft die Verdikte mechanisch und schreibt sie in den Ledger.
#
# Der Ledger ist die gemeinsame Wahrheit aller Agenten; ein einmal gefälltes
# Urteil wird nie zweimal bezahlt.


def claim_key(s):
    """Normalform des Behauptungssatzes für die job_id — bewusst schwach:
    nur Whitespace und Gross-/Kleinschreibung. Eine schärfere Normalisierung
    (wie `norm`) würde Sätze zusammenfallen lassen, die ein Judge verschieden
    beurteilen müsste."""
    return re.sub(r"\s+", " ", (s or "")).strip().casefold()


def job_id(claim, decision_id, pinpoint):
    roh = "v{}\x1f{}\x1f{}\x1f{}".format(
        JUDGE_PROMPT_VERSION, claim_key(claim), decision_id or "", pinpoint or ""
    )
    return hashlib.sha1(roh.encode("utf-8")).hexdigest()[:16]


def flat(s):
    """Für den Verbatim-Abgleich der Exzerpte: entfernt, was ein Modell beim
    Abschreiben variiert — Whitespace, typografische Anführungen, Gedankenstriche."""
    s = unicodedata.normalize("NFKC", s or "")
    for a, b in (
        ("«", '"'), ("»", '"'), ("„", '"'), ("“", '"'), ("”", '"'),
        ("’", "'"), ("‘", "'"), ("–", "-"), ("—", "-"), ("\u00a0", " "),
    ):
        s = s.replace(a, b)
    return re.sub(r"\s+", "", s).casefold()


def text_sha(t):
    return hashlib.sha1(flat(t).encode("utf-8")).hexdigest()[:16]


class Ledger:
    """Append-only JSONL im Repo. Späterer Eintrag zur selben job_id gewinnt —
    so lässt sich ein Verdikt durch ein besseres ersetzen, ohne Historie zu
    verlieren."""

    def __init__(self, path=LEDGER_PATH):
        self.path = path
        self.by_id = {}
        self.neu = []
        if os.path.exists(path):
            with open(path, encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    try:
                        v = json.loads(line)
                    except json.JSONDecodeError:
                        continue
                    if v.get("job_id"):
                        self.by_id[v["job_id"]] = v

    def get(self, jid):
        return self.by_id.get(jid)

    def add(self, verdict):
        self.by_id[verdict["job_id"]] = verdict
        self.neu.append(verdict)

    def save(self):
        if not self.neu:
            return 0
        os.makedirs(os.path.dirname(self.path) or ".", exist_ok=True)
        with open(self.path, "a", encoding="utf-8") as f:
            for v in self.neu:
                f.write(json.dumps(v, ensure_ascii=False, sort_keys=True) + "\n")
        n = len(self.neu)
        self.neu = []
        return n


def validate_verdict(raw, job=None):
    """Verdikte kommen von fremden Agenten und werden geprüft, nicht geglaubt.

    Die Verbatim-Bedingung für die Exzerpte ist der Kern: der
    opencaselaw-Server verlangte sie im Prompt und prüfte sie nie nach. Hier
    ist sie erzwingbar, weil der Harness den Prüftext besitzt — ein Modell,
    das Exzerpte erfindet, fällt auf, bevor sein Urteil in die Belegquote
    eingeht. Rückgabe: (Verdikt-Datensatz, None) oder (None, Grund)."""
    if not isinstance(raw, dict):
        return None, "kein JSON-Objekt"
    jid = (raw.get("job_id") or "").strip()
    if not jid:
        return None, "job_id fehlt"
    if job and jid != job["job_id"]:
        return None, "job_id gehört zu keinem ausgegebenen Job"
    sup = raw.get("supports")
    if sup not in SUPPORTS_ENUM:
        return None, "supports ungültig: {!r}".format(sup)
    try:
        conf = float(raw.get("confidence"))
    except (TypeError, ValueError):
        return None, "confidence fehlt oder ist keine Zahl"
    if not 0.0 <= conf <= 1.0:
        return None, "confidence ausserhalb [0,1]"
    model = (raw.get("judge_model") or "").strip()
    if not model:
        return None, "judge_model fehlt — ein Verdikt ohne Urheber ist wertlos"

    exz = {}
    for feld in ("supporting_excerpt", "qualifying_excerpt"):
        val = raw.get(feld)
        if val is None or (isinstance(val, str) and not val.strip()):
            exz[feld] = None
            continue
        if not isinstance(val, str):
            return None, "{} ist kein Text".format(feld)
        if job and job.get("text") and flat(val) not in flat(job["text"]):
            return None, "{} steht nicht wörtlich im Prüftext".format(feld)
        exz[feld] = val.strip()
    # yes/partial ohne Belegstelle ist eine Behauptung über eine Behauptung.
    if job and sup in ("yes", "partial") and not exz["supporting_excerpt"]:
        return None, "{} ohne supporting_excerpt".format(sup)

    rec = {
        "job_id": jid,
        "supports": sup,
        "confidence": round(conf, 3),
        "supporting_excerpt": exz["supporting_excerpt"],
        "qualifying_excerpt": exz["qualifying_excerpt"],
        "reasoning": (raw.get("reasoning") or "").strip()[:400],
        "judge_model": model,
        "judge_agent": (raw.get("judge_agent") or "").strip() or "unbekannt",
        "prompt_version": JUDGE_PROMPT_VERSION,
        "date": time.strftime("%Y-%m-%d"),
        "excerpt_geprueft": bool(job and job.get("text")),
    }
    if job:
        rec.update(
            claim_kurz=job["claim"][:160],
            decision_id=job["decision_id"],
            pinpoint=job.get("pinpoint"),
            text_quelle=job.get("text_quelle"),
            text_sha=job.get("text_sha"),
        )
    return rec, None


def pruef_text(mcp, unit, pinpoint, decision_id, pinpoints):
    """Text, gegen den geurteilt wird — dieselbe Rangfolge, die der
    opencaselaw-Server intern anwandte: Pinpoint-Erwägung, sonst Regeste,
    sonst Volltextkopf. Alle drei sind Lookups ohne LLM-Anteil."""
    if pinpoint:
        t = (pinpoints.get("{} E. {}".format(unit["reference"], pinpoint)) or {}).get("text")
        if t:
            return t, "Erwägung {}".format(pinpoint)
    r = mcp.call("get_regeste", {"decision_id": decision_id})
    if r.get("regeste"):
        return r["regeste"], "Regeste"
    d = mcp.call("get_decision", {"decision_id": decision_id})
    ft = d.get("full_text") or d.get("text") or ""
    if len(ft.strip()) >= 30:
        return ft[:VOLLTEXT_BUDGET], "Volltext (erste {} Zeichen)".format(VOLLTEXT_BUDGET)
    return None, None


# ---------------------------------------------------------------- Stufe 0


def norm(s: str) -> str:
    """Normalisiert Text für den Stufe-1-Abgleich."""
    # Inline-Fussnoten entfernen
    s = re.sub(r"(?:Fassung gemäss|Eingefügt durch|Aufgehoben durch|Berichtigt von|Neugefasst durch|Strafdrohungen neu umschrieben gemäss).*?\((?:\s*AS|\s*RO|\s*FF|\s*BBl)[^)]*\)\.?", "", s, flags=re.S)
    s = FEDLEX_FUSSNOTE.sub("", s)
    # Entferne redaktionelle Zusätze wie "[...]"
    s = re.sub(r"\[.*?\]", "", s)
    # Schweizer Rechtschreibung vereinheitlichen (ß -> ss)
    for a, b in [
        ("ß", "ss"),
        ("ä", "ae"),
        ("ö", "oe"),
        ("ü", "ue"),
        ("Ä", "ae"),
        ("Ö", "oe"),
        ("Ü", "ue"),
    ]:
        s = s.replace(a, b)
    s = re.sub(r"\*+|_+|`+|>+", " ", s)          # Markdown-Auszeichnung
    s = re.sub(r"\[\s*(?:AS|RO|FF|BBl)[^\]]*\]\.?\s*(?:Siehe\s+heute:[^)]*\)\.?)?", " ", s, flags=re.I)
    s = re.sub(r"\bSR\s+[\d.]+\b", "", s)    # Fedlex-interne SR-Einschübe
    s = re.sub(r"\b(?:AS|RO|FF|BBl)\s+\d{4}\s+\d+\b", " ", s) # Fedlex-interne AS/BBl-Einschübe
    s = re.sub(r"[,;.:!?'\"()\[\]{}–—\-]", " ", s) # Interpunktion für Textabgleich neutralisieren
    s = re.sub(r"(\d+)\s+([a-z])\b", r"\1\2", s, flags=re.I) # "329 g" -> "329g", "257 d" -> "257d"
    s = re.sub(r"\b([a-z])\s+(bis|ter|quater|quinquies)\b", r"\1\2", s, flags=re.I) # "a bis" -> "abis"
    s = re.sub(r"(\d+)\s+(bis|ter|quater|quinquies)\b", r"\1\2", s, flags=re.I) # "260 ter" -> "260ter"
    s = re.sub(r"\bschutz\s+beduerftig", "schutzbeduerftig", s, flags=re.I)
    s = re.sub(r"\bwider\s+stand\b", "widerstand", s, flags=re.I)
    s = re.sub(r"\bnicht\s+zu\s+wehr\b", "nicht zur wehr", s, flags=re.I) # Fedlex-Typo-Fix in Art. 67 Abs. 4
    s = re.sub(r"\berforder\s+lichen\b", "erforderlichen", s, flags=re.I) # OCR-Split-Fix
    s = re.sub(r"\bgesamt\s+strafe\b", "gesamtstrafe", s, flags=re.I) # Fedlex-Typo-Fix
    s = re.sub(r"\s+", " ", s)
    return s.strip().lower()


def clean_fedlex(text: str) -> str:
    """Bereinigt amtlichen Fedlex-Text für den Vergleich."""
    t = FEDLEX_FUSSNOTE.sub(" ", text)
    t = re.sub(r"\bGesamt\s+strafe\b", "Gesamtstrafe", t)
    t = re.sub(r"\s+", " ", t).strip()
    return t.strip().lower()


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
    # Listenpunkt oder Tabellenzeile: nicht über die Zeilengrenze zurückgreifen,
    # sonst erbt jeder Beleg einer Liste den Text des ersten Punktes.
    letzte = para.rsplit("\n", 1)[-1]
    if re.match(r"\s*[-*+]\s|\s*\d+[.)]\s|\s*\|", letzte):
        para = letzte
    parts = re.split(r"(?<=[.!?:])\s+(?=[A-ZÄÖÜ«\"*])", para)
    claim = parts[-1] if parts else para
    if len(strip_md(claim)) < 25 and len(parts) > 1:   # Fragment → Vorsatz dazu
        claim = parts[-2] + " " + claim
    return strip_md(claim).rstrip(" (").strip()


def satz_laeuft_weiter(text, pos, claim):
    """Steht der Beleg **mitten** im Satz («Das Bundesgericht hat sich in
    [BGE 137 V 210](…) mit … befasst»), liefert `sentence_before` nur das
    Bruchstück davor. Erkennbar ist das daran, dass das Bruchstück nicht auf ein
    Satzzeichen endet und der Text nach dem Beleg kleingeschrieben weitergeht."""
    if not claim or claim[-1] in ".!?:;":
        return False
    rest = text[pos:pos + 400]
    # über den Beleg hinweg zum Folgetext
    rest = re.sub(r"^\[[^\]]*\]\([^)]*\)|^" + CITE_PLAIN.pattern, "", rest)
    rest = re.sub(r"^[\s,)]*(?:E\.\s*[\d.]+)?[\s,)]*", "", rest)
    return bool(re.match(r"[a-zäöüß]", rest))


def clean_claim(s):
    """Listenmarker, Fussnotenzahlen und ein vorangestellter Beleg gehören nicht
    in den Behauptungssatz, den Stufe 5 dem Entscheid vorhält."""
    s = strip_md(s or "").strip()
    s = re.sub(r"^[-*•>\s]+", "", s)
    s = re.sub(r"^\d{1,3}[.)]?\s+(?=[A-ZÄÖÜ«\"]|In\b|Vgl\b)", "", s)
    s = re.sub(
        r"^(?:In|Vgl\.|Siehe|Gemäss|Nach)?\s*" + CITE_PLAIN.pattern
        + r"[\s,]*(?:E\.\s*[\d.]+)?\s*[—–-]\s*", "", s)
    return s.strip()


def table_claim(line, ref):
    """Übersichtstabellen (`| BGE 126 I 68 | 2000 | Kernsatz … |`) sind im
    Bestand verbreitet. Ohne eigene Behandlung reisst die Satzsegmentierung die
    Zeile nicht auf und der Behauptungssatz wird zur Zeilensuppe aus mehreren
    Entscheiden — Stufe 5 prüft dann Aussagen, die zu anderen Entscheiden gehören."""
    zellen = [strip_md(c.strip()) for c in line.strip().strip("|").split("|")]
    kandidaten = [
        c for c in zellen
        if ref not in c and not re.fullmatch(r"\d{4}|[-–—:\s]*", c) and len(c) >= 20
    ]
    return max(kandidaten, key=len) if kandidaten else None


def blockquote_before(text, pos):
    """Wörtliches Zitat im Blockquote, dessen Beleg allein in der Folgezeile steht:

        > «Der Eingriff darf … nicht einschneidender sein als notwendig»

        ([BGE 126 I 112, E. 5](…)).

    Hier ist das Blockquote der Behauptungssatz. `sentence_before` sieht nur die
    Klammer mit dem Beleg und meldete bisher `claim_nicht_extrahierbar` — ein
    Parserbefund gegen die sauberste Belegform, die es gibt."""
    head = text[:pos]
    zeilen = [l for l in head.split("\n") if l.strip()]
    quote = []
    for l in reversed(zeilen):
        if l.lstrip().startswith(">"):
            quote.insert(0, l.lstrip().lstrip(">").strip())
        elif quote:
            break
        elif len(strip_md(l)) > 40:
            return None      # dazwischen steht Fliesstext, kein Blockquote-Beleg
    return strip_md(" ".join(quote)).strip("«»\"„“ ") or None


def zeile_um(text, pos):
    """Die Zeile, in der `pos` steht."""
    a = text.rfind("\n", 0, pos) + 1
    b = text.find("\n", pos)
    return a, (b if b != -1 else len(text))


def sentence_around(text, pos):
    """Satz, in dem der Beleg selbst steht — für die Zitierlagen, in denen die
    Behauptung dem Beleg **folgt** (`**BGE 148 I 19** — Leitentscheid zu …`,
    `In BGE 148 I 33 entschied das Bundesgericht …`). Ohne das liefert
    `sentence_before` dort «In» oder «🔗»."""
    start = text.rfind("\n\n", 0, pos) + 2
    end = text.find("\n\n", pos)
    # Listen ohne Leerzeile dazwischen: Jeder Punkt ist eine eigene Aussage. Ohne
    # diese Begrenzung erbt jeder Beleg der Liste den Text des ersten Punktes
    # (BV Art. 89: vier Fehlalarme so entstanden).
    za, zb = zeile_um(text, pos)
    if re.match(r"\s*[-*+]\s|\s*\d+[.)]\s|\s*\|", text[za:zb]):
        start, end = za, zb
    para = text[start : end if end != -1 else len(text)]
    rel = pos - start
    parts, acc = re.split(r"(?<=[.!?:])\s+(?=[A-ZÄÖÜ«\"*])", para), 0
    for i, p in enumerate(parts):
        if acc + len(p) >= rel:
            claim = " ".join(parts[i : i + 2])
            break
        acc += len(p) + 1
    else:
        claim = para
    claim = strip_md(claim)
    # Führenden Beleg abschneiden: «BGE 148 I 19 — Leitentscheid …» → «Leitentscheid …»
    claim = re.sub(r"^(?:In|Vgl\.|Siehe|Gemäss|Nach)?\s*" + CITE_PLAIN.pattern
                   + r"[\s,]*(?:E\.\s*[\d.]+)?\s*[—–-]?\s*", "", claim).strip()
    return claim


def parse_file(path, rel):
    """Ein Markdown-File → (units, quotes). Deckt beide Zitierlagen ab:
    Fliesstext-Links im Kommentar und OCL-Blöcke in rechtsprechung.md."""
    text = open(path, encoding="utf-8").read()
    body = text.split("---", 2)[2] if text.startswith("---") else text
    offset = len(text) - len(body)

    # Audit-Protokoll am Dateiende: alles ab dieser Überschrift zählt nicht als
    # Beleg, sondern dokumentiert ausgebaute Belege.
    ab = AUSGEBAUT_HEAD.search(body)
    if ab:
        body = body[: ab.start()]

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

    def block_claim(blk):
        """Behauptungssatz eines Entscheidblocks: Kernaussage/Regeste/Bedeutung."""
        if not blk:
            return None
        seg = body[blk[0] : blk[1]]
        best, best_rang = None, 99
        for bm in BLOCK_CLAIM.finditer(seg):
            rang = CLAIM_RANG[bm.group(1)]
            if rang >= best_rang:
                continue
            txt = strip_md(bm.group(2).strip())
            if bm.group(1) == "Regeste":
                rest = REGESTE_NORMKETTE.sub("", txt)
                if len(rest) >= 40:
                    txt = rest
            best, best_rang = txt, rang
        return best

    def block_fallback(blk):
        """Kein benanntes Feld im Block — erster substanzieller Absatz unter der
        Überschrift. Ohne das liefert `sentence_before` bei einem Beleg in der
        Überschrift die Überschrift selbst («###») und Stufe 5 meldet einen
        Parser-Artefakt als fehlenden Behauptungssatz."""
        if not blk:
            return None
        seg = body[blk[0] : blk[1]].split("\n", 1)
        for para in (seg[1] if len(seg) > 1 else "").split("\n\n"):
            p = strip_md(para.strip())
            p = re.sub(r"^(Sachverhalt|Rechtsfrage|Ausgangslage|Hinweis)\s*:\s*", "", p)
            if len(p) >= 40 and not p.startswith(("|", "-", "*", "#")):
                return p
        return None

    def line_at(pos):
        line_start = body.rfind("\n", 0, pos) + 1
        end = body.find("\n", pos)
        return body[line_start : end if end != -1 else len(body)]

    def lineno(pos):
        return body.count("\n", 0, pos) + text[:offset].count("\n") + 1

    units = []
    for m in CITE_LINK.finditer(body):
        label, url_raw, anchor = m.group(1), m.group(2), m.group(3)
        if "mcp.opencaselaw.ch/entscheid/" in url_raw:
            decision_id = url_raw.split("mcp.opencaselaw.ch/entscheid/")[1]
            ref = ref_from_id(decision_id)
        else:
            decision_id = None
            pm_ref = CITE_PLAIN.search(label)
            ref = pm_ref.group(0) if pm_ref else label
        line = line_at(m.start())

        pin, claim = None, None
        blk = block_of(m.start())
        in_heading = line.lstrip().startswith("#")
        # «🔗 [BGE …](url)» als eigene Zeile: der Beleg steht für den ganzen
        # Block, nicht für den Satz davor — sonst wird «🔗» der Behauptungssatz.
        nur_link = ANY_MD_LINK.sub("", line).strip(" 🔗-*—–>|") == ""
        if blk and (in_heading or nur_link or "**OCL**" in line):
            claim = block_claim(blk) or block_fallback(blk)
            pm = PINPOINT.search(body[blk[0] : blk[1]].split("\n", 1)[0])
            if pm:
                pin = pm.group(1)
        if claim is None and line.lstrip().startswith("|"):
            claim = table_claim(line, ref)
        if claim is None:
            claim = sentence_before(body, m.start())
        if len(claim) < 25 or not re.sub(r"\(?\s*" + CITE_PLAIN.pattern + r".*", "", claim).strip():
            claim = (blockquote_before(body, m.start())
                     or sentence_around(body, m.start()) or claim)
        elif satz_laeuft_weiter(body, m.start(), claim):
            claim = sentence_around(body, m.start()) or claim
        if pin is None and anchor:
            # URL-Anker codiert den Pinpoint: #e-2-1-1 → 2.1.1 oder #consideration_2.1
            am = re.match(r"#(?:e-|consideration_)([\d.-]+)$", anchor)
            if am:
                pin = am.group(1).replace("-", ".")
        if pin is None:
            # Rückwärtssuche nur innerhalb derselben Zeile: In Tabellen steht in
            # der Vorzeile eine fremde Erwägungsspalte, die sonst als Pinpoint
            # dieses Belegs gelesen wird (BV Art. 34: drei Fehlalarme so entstanden).
            vor = body[max(0, m.start() - 160) : m.start()]
            vor = vor[vor.rfind("\n") + 1 :]
            pm = PINPOINT.search(label) or PINPOINT.search(vor)
            if pm:
                pin = pm.group(1)

        claim = clean_claim(claim)
        units.append(
            {
                "file": rel,
                "line": lineno(m.start()),
                "decision_id": decision_id,
                "reference": ref,
                "pinpoint": pin,
                "claim": claim,
                "claim_id": hashlib.sha256(norm(claim).encode()).hexdigest()[:12],
                "zitierlage": "link",
            }
        )

    # ---- Unverlinkte Zitierungen. Spans der Markdown-Links ausnehmen, sonst
    # zählt jede verlinkte Referenz ein zweites Mal (der Linktext nennt sie).
    link_spans = [(m.start(), m.end()) for m in ANY_MD_LINK.finditer(body)]

    def in_link(pos):
        return any(a <= pos < b for a, b in link_spans)

    def add_plain(ref, pos, pin, claim):
        claim = clean_claim(claim)
        units.append(
            {
                "file": rel,
                "line": lineno(pos),
                "decision_id": None,
                "reference": ref,
                "pinpoint": pin,
                "claim": claim,
                "claim_id": hashlib.sha256(norm(claim).encode()).hexdigest()[:12],
                "zitierlage": "plain",
            }
        )

    seen_e_claims = set()
    for m in CITE_PLAIN.finditer(body):
        if in_link(m.start()):
            continue
        ref = re.sub(r"\s+", " ", m.group(0)).strip()
        line = line_at(m.start())
        blk = block_of(m.start())

        if line.lstrip().startswith("#"):
            # Entscheidblock: die Überschrift nennt den Entscheid, die Aussagen
            # stehen darunter. Jede «**E. X.Y**»-Zeile ist ein eigenes Paar —
            # nur so wird der Pinpoint gegen die dort behauptete Aussage geprüft.
            seg = body[blk[0] : blk[1]] if blk else ""
            got_e = False
            for em in E_CLAIM.finditer(seg):
                key = (ref, em.group(1), blk[0] if blk else 0)
                if key in seen_e_claims:
                    continue
                seen_e_claims.add(key)
                got_e = True
                add_plain(ref, blk[0] + em.start(), em.group(1),
                          strip_md(em.group(2).strip()))
            bc = block_claim(blk) or block_fallback(blk)
            if bc or not got_e:
                pm = PINPOINT.search(line)
                pin = pm.group(1) if pm else None
                if pin is None:
                    # Steht der Beleg unverlinkt in der Überschrift und der
                    # Pinpoint nur im OCL-Link darunter, gehört er trotzdem zu
                    # diesem Paar — sonst prüft Stufe 5 gegen die Regeste und
                    # meldet `unrelated` für eine korrekt belegte Erwägung.
                    for lm in CITE_LINK.finditer(seg):
                        if ref_from_id(lm.group(2)) != ref or not lm.group(3):
                            continue
                        am = re.match(r"#e-([\d-]+)$", lm.group(3))
                        if am:
                            pin = am.group(1).replace("-", ".")
                            break
                add_plain(ref, m.start(), pin, bc)
            continue

        # Fliesstext: «… (BGE 146 I 49 E. 4.2).» — Pinpoint direkt dahinter.
        # Bei BGer-Dossiernummern schiebt sich das Urteilsdatum dazwischen
        # («4A_604/2025 v. 22.4.2026, E. 2.2.4»), was der schweizüblichen
        # Zitierform entspricht. Ohne DATUM_TAIL bleibt der Pinpoint ungelesen,
        # Stufe 5 prüft gegen den Sachverhalt und meldet `unrelated` für einen
        # korrekt belegten Satz.
        tail = body[m.end() : m.end() + 60]
        pm = re.match(DATUM_TAIL + r"\s*,?\s*(?:E\.|consid\.)\s*(\d+(?:\.\d+)*)", tail)
        if line.lstrip().startswith("|"):
            claim = table_claim(line, ref) or sentence_before(body, m.start())
        else:
            claim = sentence_before(body, m.start())
            if len(claim) < 25:  # Beleg steht vor der Aussage, nicht dahinter
                claim = (blockquote_before(body, m.start())
                         or sentence_around(body, m.start()) or claim)
            elif satz_laeuft_weiter(body, m.start(), claim):
                claim = sentence_around(body, m.start()) or claim
        add_plain(ref, m.start(), pm.group(1) if pm else None, claim)

    # Verbatim-Zitate: nächstgelegener Beleg im selben Absatz
    wortlaut = extract_wortlaut(text)
    quotes = []
    for m in QUOTED.finditer(body):
        q = strip_md(m.group(1))
        if len(q) < MIN_QUOTE_LEN or norm(q) in norm(wortlaut):
            continue   # Gesetzeswortlaut prüft Stufe 1
        near = [u for u in units if abs(u["line"] - lineno(m.start())) <= 6]
        quotes.append(
            {
                "file": rel,
                "line": lineno(m.start()),
                "quote": q,
                # Unverlinkte Belege tragen keine decision_id — Referenz genügt,
                # stufe4 löst sie ohnehin über `ref_from_id` auf.
                "sources": [u["decision_id"] or u["reference"] for u in near] or None,
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


def stufe1_wortlaut(mcp, gesetz, article, zitiert, sr_number=None):
    """Gleicht den im Bundle zitierten Normtext gegen die geltende Fassung ab.

    SOLL-Quelle ist die **Fedlex-MCP** (`get_article` mit rs_number + article), weil sie
    amtlich und von opencaselaw unabhängig ist. Dieses Skript spricht den MCP per
    HTTP-JSON-RPC an und erreicht damit vorerst nur opencaselaw; solange das so ist,
    ruft die Funktion `get_law` auf und meldet bei der seit 23.08.2026 bestehenden
    IP-Sperre `nicht_verifizierbar`. Ein Lauf mit dieser Meldung hat den Wortlaut
    NICHT geprüft — das Ergebnis nie als bestanden werten, sondern den Wortlaut über
    die Fedlex-MCP von Hand gegenprüfen (oder diese Funktion auf einen Fedlex-Client
    umstellen; die Fedlex-Schnittstelle kennt keine Sperre).
    """
    if not zitiert:
        return {"status": "kein_wortlaut_block"}
    args = {"article": article}
    if sr_number:
        args["sr_number"] = sr_number
    else:
        args["abbreviation"] = gesetz.upper()
    res = mcp.call("get_law", args)
    if "_error" in res:
        return {"status": "nicht_verifizierbar", "grund": res["_error"]}
    md = res.get("_text", "")
    block_offset = 0
    if ("No articles found" in md or not md.strip()) and article.isdigit():
        art_int = int(article)
        for prev in range(art_int - 1, max(1, art_int - 5), -1):
            args_prev = dict(args, article=str(prev))
            res_prev = mcp.call("get_law", args_prev)
            md_prev = res_prev.get("_text", "")
            range_pat = re.compile(r"Art\.\s*(\d+)\s*[-–]\s*(\d+)", re.I)
            for rm in range_pat.finditer(md_prev):
                low, high = int(rm.group(1)), int(rm.group(2))
                if low <= art_int <= high:
                    res = res_prev
                    md = md_prev
                    break
            if res is res_prev:
                break
    elif "No articles found" in md or not md.strip():
        m_suf = re.search(r"(bis|ter|quater|quinquies)$", article)
        if m_suf:
            suffix = m_suf.group(1)
            base = article[:-len(suffix)]
            res_base = mcp.call("get_law", dict(args, article=base))
            md_base = res_base.get("_text", "")
            if md_base and "No articles found" not in md_base:
                res = res_base
                md = md_base
                suffix_map = {"bis": 1, "ter": 2, "quater": 3, "quinquies": 4}
                block_offset = suffix_map.get(suffix, 0)

    stand = res.get("consolidation_date") or res.get("as_of") or res.get("date")
    arts = res.get("articles") or []
    if arts:
        amtlich = "\n".join(a.get("text", "") for a in arts)
    elif res.get("text"):
        amtlich = res["text"]
    elif md:
        # get_law antwortet als Markdown: Artikelblock unter "### Art. N —"
        sm = re.search(r"Consolidation date:\s*(\S+)", md)
        stand = stand or (sm.group(1) if sm else None)
        block = re.split(r"^### Art\. ", md, flags=re.M)
        idx = 1 + block_offset if len(block) > 1 + block_offset else 1
        body = block[idx] if len(block) > idx else md
        body = re.split(r"\n(?=### Art\.)", body)[0]
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


def stufe5_grounding(mcp, units, existenz, pinpoints, ledger,
                     jobs_out=None, workers=None):
    """Trägt der Beleg die Behauptung? Nur für Paare, die 2–4 überlebt haben.

    Das Urteil kommt aus dem Verdikt-Ledger, nicht mehr von `check_claim_support`
    (siehe Abschnitt „Judge-Ledger"). Fehlt eines, gilt das Paar als `offen`:
    ein fehlendes Urteil ist kein Freispruch und geht darum auch nicht in die
    Belegquote ein. Ist `jobs_out` eine Liste, wird für jedes offene Paar der
    Prüftext geholt und ein Job gesammelt.

    Die Reihenfolge von `out` bleibt die der `units` — Platzhalter halten den
    Platz."""
    out, jobs, erster = [], {}, {}
    slots = []          # (Index in out, Key, Unit, geprüfter Pinpoint)
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
        # nicht dem Judge vorwerfen (er urteilte sonst über einen Satzrest).
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
        if key not in jobs:
            jobs[key] = {"claim": u["claim"], "decision_id": did, "pinpoint": pin}
            erster[key] = (u, pin)   # Stammsatz kommt vom ersten Vorkommen
        slots.append((len(out), key, u, pin))
        out.append(None)

    # Offene Paare bestimmen. Der Prüftext wird nur geholt, wenn Jobs
    # ausgegeben werden sollen — für den reinen Berichtslauf wäre er
    # unnötiger Netzverkehr.
    offen_keys = [
        k for k, a in jobs.items()
        if not ledger.get(job_id(a["claim"], a["decision_id"], a["pinpoint"]))
    ]
    texte = {}
    if jobs_out is not None and offen_keys:
        def hole(k):
            u, pin = erster[k]
            return k, pruef_text(mcp, u, pin, jobs[k]["decision_id"], pinpoints)

        n = min(workers or MAX_WORKERS, len(offen_keys))
        if n <= 1:
            texte = dict(hole(k) for k in offen_keys)
        else:
            with ThreadPoolExecutor(max_workers=n) as ex:
                texte = dict(f.result() for f in as_completed(
                    [ex.submit(hole, k) for k in offen_keys]))

    gesehen = set()
    for idx, key, u, _pin in slots:
        quelle, pin = erster[key]
        did = jobs[key]["decision_id"]
        jid = job_id(quelle["claim"], did, pin)
        rec = {
            "file": u["file"],
            "line": u["line"],
            "claim_id": quelle["claim_id"],
            "claim": quelle["claim"],
            "reference": quelle["reference"],
            "pinpoint": pin,
            "job_id": jid,
        }
        v = ledger.get(jid)
        if v:
            rec.update(
                supports=v["supports"],
                confidence=v.get("confidence"),
                geprueft_gegen=v.get("text_quelle"),
                begruendung=v.get("reasoning"),
                beleg_exzerpt=v.get("supporting_excerpt"),
                einschraenkung=v.get("qualifying_excerpt"),
                judge_model=v.get("judge_model"),
                judge_agent=v.get("judge_agent"),
                excerpt_geprueft=v.get("excerpt_geprueft"),
            )
            out[idx] = rec
            continue

        text, quelle_label = texte.get(key, (None, None))
        if jobs_out is not None and not text:
            if mcp.blockiert:
                # Kein Urteil möglich, aber auch kein Befund über den Bestand:
                # das Paar bleibt offen, bis der Zugang wieder besteht.
                rec.update(
                    supports="offen",
                    confidence=None,
                    begruendung="Prüftext nicht beschaffbar — " + mcp.blockiert,
                )
            else:
                # Kein Prüftext beschaffbar (kantonaler Entscheid ohne Regeste
                # und ohne Volltext) — Grenze des Bestands, kein Befund.
                rec.update(
                    supports="nicht_verifizierbar",
                    confidence=None,
                    begruendung="kein Prüftext verfügbar (weder Erwägung noch Regeste noch Volltext)",
                )
            out[idx] = rec
            continue

        rec.update(
            supports="offen",
            confidence=None,
            begruendung="kein Verdikt im Ledger — mit --emit-jobs ausgeben und "
                        "von einem Judge-Subagenten beurteilen lassen",
        )
        if jobs_out is not None and jid not in gesehen:
            gesehen.add(jid)
            jobs_out.append(
                {
                    "job_id": jid,
                    "prompt_version": JUDGE_PROMPT_VERSION,
                    "claim": quelle["claim"],
                    "reference": quelle["reference"],
                    "decision_id": did,
                    "pinpoint": pin,
                    "text_quelle": quelle_label,
                    "text_sha": text_sha(text),
                    "text": text,
                    "fundstelle": f"{quelle['file']}:{quelle['line']}",
                }
            )
        out[idx] = rec
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


def audit_bundle(mcp, bundle, gesetz, article, ledger, jobs_out=None, workers=None):
    sr = sr_from_gesetz(bundle)
    units, quotes, wortlaut = parse_bundle(bundle)
    w = stufe1_wortlaut(mcp, gesetz, article, wortlaut, sr_number=sr)
    ex = stufe2_existenz(mcp, units)
    pp = stufe3_pinpoints(mcp, units, ex)
    vb = stufe4_verbatim(mcp, quotes, ex)
    gr = stufe5_grounding(mcp, units, ex, pp, ledger,
                          jobs_out=jobs_out, workers=workers)
    ak = stufe6_aktualitaet(mcp, sr, article, ex)

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
    offen = [g for g in gr if g["supports"] == "offen"]
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
            "belege_offen": len(offen),
            "judge_modelle": sorted(
                {g.get("judge_model") for g in beurteilt if g.get("judge_model")}
            ),
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


# ---------------------------------------------------------------- Jobs & Ingest


def jobs_dir_for(gesetz, article=None):
    name = gesetz.lower() + ("-" + article if article else "")
    return os.path.join(JOBS_ROOT, name)


def lies_jsonl(pfad):
    """JSONL — toleriert eine JSON-Liste und Code-Fences, weil die Datei von
    einem Subagenten geschrieben wird und nicht jeder Agent JSONL sauber
    trifft. Was nicht parst, wird als Fehlzeile gemeldet, nicht verschluckt."""
    roh = open(pfad, encoding="utf-8").read().strip()
    if roh.startswith("```"):
        roh = roh.split("\n", 1)[-1].rsplit("```", 1)[0].strip()
    if roh.startswith("["):
        try:
            daten = json.loads(roh)
            return [(0, d) for d in daten], []
        except json.JSONDecodeError as e:
            return [], [(0, str(e))]
    out, fehler = [], []
    for i, line in enumerate(roh.split("\n"), 1):
        line = line.strip().rstrip(",")
        if not line or line in ("[", "]"):
            continue
        try:
            out.append((i, json.loads(line)))
        except json.JSONDecodeError as e:
            fehler.append((i, str(e)))
    return out, fehler


def ingest(pfad, ledger):
    """Verdikte einlesen, mechanisch prüfen, Ledger fortschreiben.

    `pfad` ist das Job-Verzeichnis eines Laufs (enthält `jobs.jsonl` und die
    `verdicts*.jsonl` der Subagenten) oder eine einzelne Verdikt-Datei; im
    zweiten Fall werden die Jobs aus dem Nachbarverzeichnis gelesen."""
    pfad = os.path.abspath(pfad)
    if not os.path.exists(pfad):
        print("nichts einzulesen: {} existiert nicht".format(pfad), file=sys.stderr)
        return 1
    if os.path.isdir(pfad):
        vdir = pfad
        vfiles = sorted(
            os.path.join(pfad, f) for f in os.listdir(pfad)
            if f.startswith("verdicts") and f.endswith(".jsonl")
        )
    else:
        vdir = os.path.dirname(pfad)
        vfiles = [pfad]
    jobs = {}
    jpfad = os.path.join(vdir, "jobs.jsonl")
    if os.path.exists(jpfad):
        for _, j in lies_jsonl(jpfad)[0]:
            if j.get("job_id"):
                jobs[j["job_id"]] = j
    else:
        print(
            "WARNUNG: keine jobs.jsonl neben den Verdikten — die Exzerpte "
            "können nicht gegen den Prüftext geprüft werden.",
            file=sys.stderr,
        )
    if not vfiles:
        print("keine verdicts*.jsonl in " + vdir, file=sys.stderr)
        return 1

    uebernommen, verworfen, unbekannt = 0, [], 0
    for vf in vfiles:
        zeilen, fehler = lies_jsonl(vf)
        for ln, e in fehler:
            verworfen.append((os.path.basename(vf), ln, "kein JSON: " + e[:60]))
        for ln, raw in zeilen:
            job = jobs.get((raw or {}).get("job_id")) if isinstance(raw, dict) else None
            if jobs and not job:
                unbekannt += 1
                verworfen.append(
                    (os.path.basename(vf), ln, "job_id gehört zu keinem Job dieses Laufs")
                )
                continue
            rec, grund = validate_verdict(raw, job)
            if grund:
                verworfen.append((os.path.basename(vf), ln, grund))
                continue
            ledger.add(rec)
            uebernommen += 1

    n = ledger.save()
    print(
        "Ingest: {} Verdikte übernommen, {} verworfen ({} Jobs im Lauf)".format(
            uebernommen, len(verworfen), len(jobs)
        ),
        file=sys.stderr,
    )
    for datei, ln, grund in verworfen[:25]:
        print("  verworfen {}:{} — {}".format(datei, ln, grund), file=sys.stderr)
    if len(verworfen) > 25:
        print("  … und {} weitere".format(len(verworfen) - 25), file=sys.stderr)
    print("Ledger: +{} Zeilen → {}".format(n, ledger.path), file=sys.stderr)
    # Ein verworfenes Verdikt ist ein Befund über den Judge, kein Betriebsfehler:
    # Exit 0, damit ein Lauf mit ein paar Ausreissern nicht als Absturz gilt.
    return 0


def import_cache(ledger):
    """Einmalige Übernahme der bereits bezahlten opencaselaw-Verdikte aus dem
    lokalen MCP-Cache. Sie sind bezahlt, brauchbar und dienen ausserdem als
    Vergleichsmassstab für die Kalibrierung neuer Judge-Modelle. Ihre Exzerpte
    sind nie gegen den Prüftext geprüft worden — das hält `excerpt_geprueft`
    fest."""
    if not os.path.exists(CACHE_PATH):
        print("kein MCP-Cache unter " + CACHE_PATH, file=sys.stderr)
        return 1
    cache = json.load(open(CACHE_PATH, encoding="utf-8"))
    datum = time.strftime("%Y-%m-%d", time.localtime(os.path.getmtime(CACHE_PATH)))
    uebernommen, uebersprungen = 0, 0
    for key, v in cache.items():
        if ":check_claim_support:" not in key or not isinstance(v, dict):
            continue
        if v.get("supports") not in SUPPORTS_ENUM:
            uebersprungen += 1      # Fehlantworten des Servers, kein Urteil
            continue
        try:
            args = json.loads(key.split(":check_claim_support:", 1)[1])
        except json.JSONDecodeError:
            uebersprungen += 1
            continue
        jid = job_id(args.get("claim"), args.get("decision_id"), args.get("pinpoint"))
        if ledger.get(jid):
            continue
        ledger.add(
            {
                "job_id": jid,
                "claim_kurz": (args.get("claim") or "")[:160],
                "decision_id": args.get("decision_id"),
                "pinpoint": args.get("pinpoint"),
                "text_quelle": v.get("checked_text_source"),
                "text_sha": None,
                "supports": v["supports"],
                "confidence": round(float(v.get("confidence") or 0.0), 3),
                "supporting_excerpt": v.get("supporting_excerpt"),
                "qualifying_excerpt": v.get("qualifying_excerpt"),
                "reasoning": (v.get("reasoning") or "")[:400],
                "judge_model": "claude-sonnet-4-6",
                "judge_agent": "opencaselaw-mcp (Altbestand, vor der Umstellung)",
                "prompt_version": JUDGE_PROMPT_VERSION,
                "date": datum,
                "excerpt_geprueft": False,
            }
        )
        uebernommen += 1
    n = ledger.save()
    print(
        "Altbestand: {} Verdikte übernommen, {} übersprungen (keine Urteile)\n"
        "Ledger: +{} Zeilen → {}".format(uebernommen, uebersprungen, n, ledger.path),
        file=sys.stderr,
    )
    return 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("pfad", nargs="?",
                    help="Bundle (art-045) oder Gesetzesverzeichnis mit --all")
    ap.add_argument("--all", action="store_true", help="alle art-*-Bundles darunter")
    ap.add_argument("--report", default=None)
    ap.add_argument("--no-cache", action="store_true")
    ap.add_argument("--ledger", default=LEDGER_PATH,
                    help=f"Verdikt-Ledger (Vorgabe {LEDGER_PATH})")
    ap.add_argument("--emit-jobs", nargs="?", const="", default=None, metavar="DIR",
                    help="offene Paare als Judge-Jobs ausgeben (Vorgabe: "
                         "audit-jobs/{gesetz}[-{art}])")
    ap.add_argument("--ingest", default=None, metavar="PFAD",
                    help="Verdikte eines Job-Verzeichnisses einlesen und prüfen")
    ap.add_argument("--import-cache", action="store_true",
                    help="bereits bezahlte opencaselaw-Verdikte aus dem MCP-Cache "
                         "in den Ledger übernehmen (einmalig)")
    ap.add_argument(
        "--jobs",
        type=int,
        default=MAX_WORKERS,
        help=f"parallele Lookups beim Beschaffen der Prüftexte (Vorgabe {MAX_WORKERS}, "
        f"1 = seriell; auch über GLOSSAGENS_AUDIT_JOBS)",
    )
    args = ap.parse_args()

    ledger = Ledger(args.ledger)
    if args.import_cache:
        sys.exit(import_cache(ledger))
    if args.ingest:
        sys.exit(ingest(args.ingest, ledger))
    if not args.pfad:
        ap.error("pfad fehlt (oder --ingest / --import-cache verwenden)")

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
    reports, alle_jobs = [], []
    for b in bundles:
        art = article_from_dir(b)
        if not art:
            print(f"übersprungen (kein art-Bundle): {b}", file=sys.stderr)
            continue
        print(f"→ {gesetz.upper()} Art. {art}", file=sys.stderr)
        r = audit_bundle(
            mcp, b, gesetz, art, ledger,
            jobs_out=alle_jobs if args.emit_jobs is not None else None,
            workers=args.jobs,
        )
        reports.append(r)
        s = r["zusammenfassung"]
        print(
            f"   Paare={r['stufe0_inventar']['paare']} "
            f"Wortlaut={s['wortlaut_status']} "
            f"halluziniert={len(s['referenzen_halluziniert'])} "
            f"Pinpoint-Fehler={len(s['pinpoints_fehlend'])} "
            f"gestützt={s['belege_gestuetzt']}(+{s['belege_teilweise']} teilw.)"
            f"/{s['belege_beurteilt']} offen={s['belege_offen']} "
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

    if mcp.blockiert:
        print("\nACHTUNG: " + mcp.blockiert, file=sys.stderr)

    if args.emit_jobs is not None:
        art = article_from_dir(bundles[0]) if not args.all else None
        d = args.emit_jobs or jobs_dir_for(gesetz, art)
        os.makedirs(d, exist_ok=True)
        jp = os.path.join(d, "jobs.jsonl")
        with open(jp, "w", encoding="utf-8") as f:
            for j in alle_jobs:
                f.write(json.dumps(j, ensure_ascii=False) + "\n")
        print(
            f"Judge-Jobs: {len(alle_jobs)} → {jp}\n"
            f"  Prompt: {os.path.join(SKILL_DIR, 'judge-prompt.md')}\n"
            f"  Urteile als {os.path.join(d, 'verdicts-*.jsonl')} ablegen, dann:\n"
            f"  python3 {os.path.relpath(__file__, REPO_ROOT)} --ingest {os.path.relpath(d, REPO_ROOT)}",
            file=sys.stderr,
        )


if __name__ == "__main__":
    main()
