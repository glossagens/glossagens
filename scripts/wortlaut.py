#!/usr/bin/env python3
"""Holt den Gesetzeswortlaut eines Artikels aus der amtlichen Quelle und legt ihn als Daten ab.

    scripts/wortlaut.py content/kommentar/stpo/art-110 [weitere Bundles …]
    scripts/wortlaut.py --stand 2025-04-01 content/kommentar/stpo/art-110
    scripts/wortlaut.py content/kommentar/stpo/art-*      # ganzes Gesetz

Ergebnis: data/wortlaut/{gesetz}/art-{nr}.json, gerendert vom Shortcode
`{{< wortlaut >}}` (layouts/_shortcodes/wortlaut.html).

Bundesrecht (`ebene: bund`) — Fedlex. Kantonales Recht (`ebene: kantonal`) —
die LexWork-Plattform des Kantons (Tabelle LEXWORK; Luzern: srl.lu.ch). Andere
Kantone werden mit einem Fehler abgewiesen, bis ihre Quelle eingetragen ist.

Fedlex: Quelle ist das HTML der Konsolidierung, wie Fedlex es selbst ausliefert: Der
Artikel wird als Fragment übernommen (Absätze, Litterae als <dl>, Fussnoten)
und nur bereinigt, nicht umgebaut — die Darstellung soll der von Fedlex
gleichen, und jeder eigene Zwischenschritt wäre eine Fehlerquelle mehr im
Normtext. Die SR-Nummer kommt aus dem Frontmatter der Gesetzesseite (`sr`),
das ELI und die geltende Fassung aus dem SPARQL-Endpunkt. Fassungen mit
künftigem Inkrafttreten (Fedlex führt sie bereits) werden übergangen.

LexWork: Die API liefert den Erlass als XHTML, in dem Paragraphen, Absätze und
Aufzählungen flach hintereinander stehen. Daraus wird dasselbe Fragment wie bei
Fedlex gebaut; die Änderungstabelle am Ende des Erlasses liefert die
Fassungsvermerke, die Fedlex als Fussnoten führt. Es gilt immer die aktuelle
Fassung (`--stand` wirkt nur auf Fedlex).

Nur Standardbibliothek.
"""

import argparse
import datetime as dt
import hashlib
import html
import json
import re
import sys
import urllib.parse
import urllib.request
from html.parser import HTMLParser
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
CACHE = REPO / "resources" / "wortlaut"        # resources/ ist gitignored

# Kantone mit LexWork-Plattform (gleiche API: /api/de/texts_of_law/{nr}).
LEXWORK = {
    "LU": ("https://srl.lu.ch", "SRL"),
}
SPARQL = "https://fedlex.data.admin.ch/sparqlendpoint"
PREFIXES = """
PREFIX jolux: <http://data.legilux.public.lu/resource/ontology/jolux#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
"""

# Elemente und Attribute, die im Fragment stehen bleiben dürfen.
ERLAUBT = {"p", "sup", "sub", "b", "i", "em", "strong", "dl", "dt", "dd", "a",
           "br", "table", "thead", "tbody", "tr", "th", "td", "ul", "ol", "li",
           "div", "span"}
ATTRIBUTE = {"a": {"href"}, "td": {"colspan", "rowspan"}, "th": {"colspan", "rowspan"}}
LEER = {"br"}


class Fehler(Exception):
    """Ein Artikel lässt sich nicht holen; der Lauf geht mit den übrigen weiter."""


# --------------------------------------------------------------------------
# Fedlex
# --------------------------------------------------------------------------

def sparql(query):
    data = urllib.parse.urlencode({"query": PREFIXES + query}).encode()
    req = urllib.request.Request(SPARQL, data=data, headers={
        "Accept": "application/sparql-results+json"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.load(r)["results"]["bindings"]


def fassung(sr, stand):
    """ELI und jüngste Konsolidierung mit Geltung ab spätestens `stand`.

    Eine SR-Nummer kann mehrfach vergeben sein: Unter 312.0 steht neben der
    StPO auch der aufgehobene BStP, unter 101 neben der BV ein Altbestand ohne
    HTML. Massgebend ist der Erlass mit der jüngsten deutschen HTML-Fassung.
    Fassungen mit künftigem Inkrafttreten führt Fedlex bereits — sie fallen weg.
    """
    rows = sparql(f"""
SELECT ?cc ?d ?url WHERE {{
  ?cc a jolux:ConsolidationAbstract ;
      jolux:classifiedByTaxonomyEntry/skos:notation ?n .
  FILTER(str(?n) = "{sr}")
  ?c jolux:isMemberOf ?cc ; jolux:dateApplicability ?d ; jolux:isRealizedBy ?e .
  ?e jolux:language <http://publications.europa.eu/resource/authority/language/DEU> ;
     jolux:isEmbodiedBy ?m .
  ?m jolux:userFormat <https://fedlex.data.admin.ch/vocabulary/user-format/html> ;
     jolux:isExemplifiedBy ?url .
  FILTER(?d <= "{stand}"^^<http://www.w3.org/2001/XMLSchema#date>)
}} ORDER BY DESC(?d) LIMIT 1""")
    if not rows:
        raise Fehler(f"SR {sr}: keine deutsche HTML-Konsolidierung bis {stand}")
    r = rows[0]
    return r["cc"]["value"], r["d"]["value"], r["url"]["value"]


def lade(url):
    CACHE.mkdir(parents=True, exist_ok=True)
    pfad = CACHE / (hashlib.sha1(url.encode()).hexdigest()[:16] + ".html")
    if not pfad.exists():
        with urllib.request.urlopen(url, timeout=120) as r:
            pfad.write_bytes(r.read())
    return pfad.read_text(encoding="utf-8")


# --------------------------------------------------------------------------
# Minimaler DOM über html.parser
# --------------------------------------------------------------------------

class Knoten:
    def __init__(self, tag, attrs, eltern):
        self.tag, self.attrs, self.eltern, self.kinder = tag, dict(attrs), eltern, []

    def text(self):
        return "".join(k if isinstance(k, str) else k.text() for k in self.kinder)

    def finde(self, pred):
        for k in self.kinder:
            if isinstance(k, Knoten):
                if pred(k):
                    yield k
                yield from k.finde(pred)


class Baum(HTMLParser):
    VOID = {"br", "img", "hr", "meta", "link", "input", "col", "wbr"}

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.wurzel = Knoten("#root", {}, None)
        self.akt = self.wurzel

    def handle_starttag(self, tag, attrs):
        k = Knoten(tag, attrs, self.akt)
        self.akt.kinder.append(k)
        if tag not in self.VOID:
            self.akt = k

    def handle_endtag(self, tag):
        k = self.akt
        while k is not None and k.tag != tag:
            k = k.eltern
        if k is not None and k.eltern is not None:
            self.akt = k.eltern

    def handle_data(self, data):
        self.akt.kinder.append(data)


def parse(text):
    b = Baum()
    b.feed(text)
    return b.wurzel


# --------------------------------------------------------------------------
# Extraktion
# --------------------------------------------------------------------------

def artikel_id(slug_nr):
    """'110' → art_110, '055a' → art_55_a, '024bis' → art_24_bis."""
    m = re.fullmatch(r"0*(\d+)([a-z]*)", slug_nr)
    if not m:
        raise Fehler(f"Artikelnummer nicht lesbar: {slug_nr}")
    zahl, zusatz = m.groups()
    return f"art_{zahl}" + (f"_{zusatz}" if zusatz else ""), zahl + zusatz


def sauber(text):
    return re.sub(r"\s+", " ", text.replace("\xa0", " ")).strip()


def href_umschreiben(k):
    href = k.attrs.get("href", "")
    # SR-Verweise zeigen auf die Taxonomie; das Ziel steht in data-rs-uri.
    if k.attrs.get("data-rs-uri"):
        return k.attrs["data-rs-uri"].replace("fedlex.data.admin.ch", "www.fedlex.admin.ch") + "/de"
    if href.startswith("#fn"):
        return "#wl-" + href[1:]
    if href.startswith("#"):
        return None
    if "fedlex.data.admin.ch/eli/" in href:
        return href.replace("fedlex.data.admin.ch", "www.fedlex.admin.ch") + "/de"
    return href or None


def serialisiere(k):
    if isinstance(k, str):
        return html.escape(k.replace("\xa0", " "), quote=False)
    klassen = k.attrs.get("class", "").split()
    if "display-icon" in klassen or "external-link-icon" in klassen:
        return ""
    innen = "".join(serialisiere(c) for c in k.kinder)
    if k.tag not in ERLAUBT:
        return innen
    if k.tag == "sup" and not innen.strip():
        return ""
    attrs = {}
    for name in ATTRIBUTE.get(k.tag, ()):
        if name in k.attrs:
            attrs[name] = k.attrs[name]
    if k.tag == "a":
        ziel = href_umschreiben(k)
        if ziel is None:
            return innen
        attrs = {"href": ziel}
        if not ziel.startswith("#"):
            attrs.update(target="_blank", rel="noopener")
    if "id" in k.attrs and k.attrs["id"].startswith(("fn-", "fnbck-")):
        attrs["id"] = "wl-" + k.attrs["id"]
    if k.tag == "div" and "footnotes" in klassen:
        attrs["class"] = "wortlaut-fussnoten"
    elif k.tag in ("div", "span") and not attrs:
        return innen
    a = "".join(f' {n}="{html.escape(v)}"' for n, v in attrs.items())
    if k.tag in LEER:
        return f"<{k.tag}{a}>"
    return f"<{k.tag}{a}>{innen}</{k.tag}>"


def text_ohne_sup(k):
    return "".join(c if isinstance(c, str) else ("" if c.tag == "sup" else text_ohne_sup(c))
                   for c in k.kinder)


def gliederung(art):
    """Überschriften der umschliessenden Abschnitte, aussen zuerst."""
    stufen = []
    k = art.eltern
    while k is not None:
        if k.tag == "section":
            for c in k.kinder:
                if isinstance(c, Knoten) and (re.fullmatch(r"h[1-6]", c.tag)
                                              or "heading" in c.attrs.get("class", "").split()):
                    stufen.append(sauber(text_ohne_sup(c)))
                    break
        k = k.eltern
    return list(reversed(stufen))


def extrahiere(doc, aid):
    treffer = list(doc.finde(lambda k: k.tag == "article" and k.attrs.get("id") == aid))
    if len(treffer) != 1:
        raise Fehler(f"{aid}: {len(treffer)} Treffer im Fedlex-HTML")
    art = treffer[0]
    kopf = next(art.finde(lambda k: k.tag == "h6"))
    anker = next(kopf.finde(lambda k: k.tag == "a" and k.attrs.get("href") == f"#{aid}"))
    # <b>Art. 305</b><sup>bis</sup> bzw. <b>Art. 336</b><i>c</i>: Was direkt
    # auf <b> folgt und kein Text ist, gehört zur Nummer; der Rest ist die
    # Sachüberschrift (fehlt, wenn der Randtitel eine Ebene höher steht).
    nummer, titel, in_nummer = "", "", True
    for c in anker.kinder:
        if isinstance(c, Knoten) and c.tag == "b":
            nummer += serialisiere(c)
        elif in_nummer and isinstance(c, Knoten) and c.tag in ("sup", "i") and nummer:
            nummer += f"<{c.tag}>{html.escape(sauber(c.text()))}</{c.tag}>" if sauber(c.text()) else ""
        elif isinstance(c, str) and not c.strip():
            continue
        else:
            in_nummer = False
            titel += c if isinstance(c, str) else text_ohne_sup(c)
    kopf_fn = "".join(serialisiere(c) for c in kopf.kinder
                      if isinstance(c, Knoten) and c.tag == "sup")
    body = next(art.finde(lambda k: "collapseable" in k.attrs.get("class", "").split()))
    return {
        "nummer": nummer.replace("<b>", "").replace("</b>", ""),
        "titel": sauber(titel),
        "titel_fussnoten": kopf_fn,
        "gliederung": gliederung(art),
        "html": "".join(serialisiere(c) for c in body.kinder).strip(),
    }


# --------------------------------------------------------------------------
# LexWork (kantonales Recht)
# --------------------------------------------------------------------------

def klassen(k):
    return k.attrs.get("class", "").split() if isinstance(k, Knoten) else []


def text_ohne_strong(k):
    return "".join(c if isinstance(c, str) else ("" if c.tag == "strong" else text_ohne_strong(c))
                   for c in k.kinder)


def lexwork_inline(k):
    """Text eines Absatzes; Änderungssternchen fallen weg, Fussnoten bleiben."""
    if isinstance(k, str):
        return html.escape(k.replace("\xa0", " "), quote=False)
    if k.tag == "strong" and sauber(k.text()) == "*":
        return ""
    if k.tag == "br":
        return "\n"
    if k.tag == "a" and "footnote" in klassen(k):
        nr = sauber(k.text()).strip("[]")
        return f'<sup><a href="#wl-{k.attrs.get("name", "")}_c" id="wl-{k.attrs.get("name", "")}">{nr}</a></sup>'
    innen = "".join(lexwork_inline(c) for c in k.kinder)
    if k.tag in ("sup", "sub", "i", "em", "b"):
        return f"<{k.tag}>{innen}</{k.tag}>"
    if k.tag == "a" and k.attrs.get("href", "").startswith("http"):
        return f'<a href="{html.escape(k.attrs["href"])}" target="_blank" rel="noopener">{innen}</a>'
    return innen


def extrahiere_lexwork(api, nr, gesetz_nr):
    version = api["text_of_law"]["selected_version"]
    wurzel = parse(version["xhtml_tol"])
    doc = next(wurzel.finde(lambda k: "document" in klassen(k)))
    teile = [k for k in doc.kinder if isinstance(k, Knoten)]
    stufen, treffer = {}, None
    for i, k in enumerate(teile):
        kl = klassen(k)
        stufe = next((int(c[6:]) for c in kl if re.fullmatch(r"level_\d+", c)), None)
        if stufe is not None:
            titel = " ".join(sauber(text_ohne_sup(c)) for c in k.kinder if isinstance(c, Knoten))
            stufen = {s: t for s, t in stufen.items() if s < stufe}
            stufen[stufe] = titel
        elif "article" in kl:
            num = next(k.finde(lambda c: "article_number" in klassen(c)))
            n = sauber(text_ohne_strong(next(num.finde(lambda c: "number" in klassen(c)))))
            if n == nr:
                treffer = i
                break
    if treffer is None:
        raise Fehler(f"§ {nr}: nicht im Erlass gefunden")
    art = teile[treffer]
    titel_k = next(art.finde(lambda c: "article_title" in klassen(c)), None)
    titel = "".join(lexwork_inline(c) for c in titel_k.kinder).strip() if titel_k else ""
    fn_namen = re.findall(r'id="wl-([^"]+)"', titel)
    # «8. Rechtsmittelschrift<br>a. Inhalt»: die oberen Zeilen sind
    # Randtitel einer Paragraphengruppe und gehören in die Gliederung.
    zeilen = [z.strip() for z in titel.split("\n") if z.strip()]
    randtitel, titel = zeilen[:-1], (zeilen[-1] if zeilen else "")

    teile_html, aufz = [], []

    def aufz_schliessen():
        if aufz:
            teile_html.append("<dl>" + "".join(aufz) + "</dl>")
            aufz.clear()

    for k in teile[treffer + 1:]:
        kl = klassen(k)
        if "article" in kl or any(c.startswith("level_") for c in kl) or "footnotes" in kl \
                or any(c.startswith("egress") for c in kl):
            break
        if "paragraph" in kl:
            aufz_schliessen()
            num = next((c for c in k.kinder if "number" in klassen(c)), None)
            p = next((c for c in k.kinder if isinstance(c, Knoten) and c.tag == "p"), None)
            text = "".join(lexwork_inline(c) for c in p.kinder).strip() if p else ""
            text = re.sub(r"\s+", " ", text)
            if num is not None and sauber(num.text()):
                teile_html.append(f"<p><sup>{html.escape(sauber(num.text()))}</sup> {text}</p>")
            else:
                teile_html.append(f"<p>{text}</p>")
        elif k.tag == "table" and "enumeration_item" in kl:
            zellen = list(k.finde(lambda c: c.tag == "td"))
            marke = next((sauber(text_ohne_strong(c)) for c in zellen if "number" in klassen(c)), "")
            text = re.sub(r"\s+", " ", "".join(lexwork_inline(c) for c in zellen[-1].kinder)).strip()
            aufz.append(f"<dt>{html.escape(marke)} </dt><dd>{text}</dd>")
    aufz_schliessen()
    rumpf = "".join(teile_html)
    fn_namen += re.findall(r'id="wl-([^"]+)"', rumpf)

    # Fussnoten des Paragraphen
    fussnoten = []
    alle_fn = {}
    for li in wurzel.finde(lambda c: c.tag == "li"):
        a = next(li.finde(lambda c: c.tag == "a" and "footnote" in klassen(c)), None)
        if a is not None:
            alle_fn[a.attrs.get("name", "")] = (sauber(a.text()).strip("[]"),
                                                 next(li.finde(lambda c: "footnote_text" in klassen(c)), None))
    for name in fn_namen:
        nr_fn, txt = alle_fn.get(name + "_c", ("", None))
        if txt is not None:
            inhalt = re.sub(r"\s+", " ", "".join(lexwork_inline(c) for c in txt.kinder)).strip()
            fussnoten.append(f'<p id="wl-{name}_c"><sup><a href="#wl-{name}">{nr_fn}</a></sup> {inhalt}</p>')

    # Fassungsvermerke aus der Änderungstabelle
    # Die Tabelle steht zweimal im Dokument (nach Paragraf und nach Datum),
    # mit anderer Spaltenfolge; das Element erkennt man am §.
    gesehen = set()
    for tr in wurzel.finde(lambda c: c.tag == "tr" and any(x.startswith("history_info_") for x in klassen(c))):
        zellen = [sauber(c.text()) for c in tr.kinder if isinstance(c, Knoten) and c.tag == "td"]
        if len(zellen) < 5:
            continue
        el_i = next((i for i, z in enumerate(zellen) if z.startswith("§")), None)
        if el_i is None or not re.match(rf"§ {re.escape(nr)}(?![0-9a-z])", zellen[el_i]):
            continue
        daten = [z for z in zellen if re.fullmatch(r"\d{2}\.\d{2}\.\d{4}", z)]
        element = zellen[el_i].rstrip(".")
        aend = zellen[el_i + 1] if el_i == 2 else zellen[3]
        publ = zellen[4]
        schluessel = (element, aend, tuple(daten))
        if len(daten) < 2 or schluessel in gesehen:
            continue
        gesehen.add(schluessel)
        fussnoten.append(f"<p>{html.escape(element)} {html.escape(aend)} durch Änderung vom "
                         f"{daten[0]}, in Kraft seit {daten[1]} ({html.escape(publ)}).</p>")
    if fussnoten:
        rumpf += '<div class="wortlaut-fussnoten">' + "".join(fussnoten) + "</div>"

    return {
        "nummer": f"§ {html.escape(nr)}",
        "titel": sauber(re.sub(r"<sup>.*?</sup>", "", titel)),
        "titel_fussnoten": "".join(re.findall(r"<sup>.*?</sup>", titel)),
        "gliederung": [stufen[s] for s in sorted(stufen)] + [sauber(re.sub(r"<[^>]+>", "", r)) for r in randtitel],
        "html": rumpf,
    }


def lexwork(slug, fm, cache):
    kanton = re.search(r'^kanton:\s*"?([A-Z]{2})"?', fm, re.M)
    nr = re.search(r'^srl:\s*"?([0-9.]+)"?', fm, re.M)
    if not (kanton and nr):
        raise Fehler("Gesetzesseite: `kanton` oder `srl` fehlt")
    kanton, nr = kanton.group(1), nr.group(1)
    if kanton not in LEXWORK:
        raise Fehler(f"Kanton {kanton}: keine Quelle in LEXWORK eingetragen")
    basis, sammlung = LEXWORK[kanton]
    url = f"{basis}/api/de/texts_of_law/{nr}"
    if url not in cache:
        cache[url] = json.loads(lade(url))
    api = cache[url]
    tol = api["text_of_law"]
    if tol.get("abrogated"):
        raise Fehler(f"{sammlung} {nr} ist aufgehoben")
    slug_nr = slug.removeprefix("art-")
    m = re.fullmatch(r"0*(\d+[a-z]*)", slug_nr)
    if not m:
        raise Fehler(f"Paragraphennummer nicht lesbar: {slug_nr}")
    return {
        "sammlung": f"{sammlung} {nr}",
        "art": m.group(1),
        "stand": tol["publication_enactment"],
        "link": tol["canonical_link"],
        "quelle": url,
        "abgerufen": dt.date.today().isoformat(),
        **extrahiere_lexwork(api, m.group(1), nr),
    }


def sr_aus_frontmatter(fm):
    m = re.search(r'^sr:\s*"?([0-9.]+)"?\s*$', fm, re.M)
    if not m:
        raise Fehler("Gesetzesseite: kein `sr` (kantonales Recht? — Fedlex führt nur Bundesrecht)")
    return m.group(1)


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("bundles", nargs="+", type=Path)
    ap.add_argument("--stand", default=dt.date.today().isoformat(),
                    help="geltende Fassung an diesem Tag (Default: heute)")
    args = ap.parse_args()

    fassungen, docs, fehler = {}, {}, []
    for bundle in args.bundles:
        bundle = (REPO / bundle).resolve() if not bundle.is_absolute() else bundle
        try:
            ziel, eintrag = hole(bundle, args.stand, fassungen, docs)
        except Fehler as e:
            fehler.append(f"{bundle.relative_to(REPO)}: {e}")
            print(f"FEHLER {fehler[-1]}", file=sys.stderr)
            continue
        print(f"{ziel.relative_to(REPO)}  ({re.sub('<[^>]+>', '', eintrag['nummer'])} "
              f"{eintrag['titel']}, Stand {eintrag['stand']})")
    if fehler:
        sys.exit(f"{len(fehler)} von {len(args.bundles)} Artikeln nicht geholt")


def hole(bundle, stand_am, fassungen, docs):
    gesetz, slug = bundle.parent.name, bundle.name
    fm = (bundle.parent / "_index.md").read_text(encoding="utf-8")
    bundle_fm = (bundle / "_index.md").read_text(encoding="utf-8") if (bundle / "_index.md").exists() else ""
    eintrag = eintrag_fuer(slug, fm, stand_am, fassungen, docs, bundle_fm=bundle_fm)
    return schreibe(REPO / "data" / "wortlaut" / gesetz / f"{slug}.json", eintrag), eintrag


def eintrag_fuer(slug, fm, stand_am=None, fassungen=None, docs=None, bundle_fm=None):
    """Wortlaut-Daten zu Artikel `slug` (art-110) des Gesetzes mit Frontmatter `fm`.

    Schreibt nichts — für Aufrufer, die die Daten selbst ablegen (z. B. über
    eine API statt ins Arbeitsverzeichnis)."""
    stand_am = stand_am or dt.date.today().isoformat()
    fassungen = {} if fassungen is None else fassungen
    docs = {} if docs is None else docs
    if re.search(r"^ebene:\s*kantonal", fm, re.M):
        return lexwork(slug, fm, docs)
    aid, art_nr = artikel_id(slug.removeprefix("art-"))
    if bundle_fm:
        m_anker = re.search(r'^fedlex_anker:\s*"?([^\s"\n]+)"?\s*$', bundle_fm, re.M)
        if m_anker:
            aid = m_anker.group(1)
    sr = sr_aus_frontmatter(fm)
    if sr not in fassungen:
        fassungen[sr] = fassung(sr, stand_am)
        docs[sr] = parse(lade(fassungen[sr][2]))
    eli, stand, url = fassungen[sr]
    return {
        "sr": sr,
        "art": art_nr,
        "stand": stand,
        "eli": eli.replace("fedlex.data.admin.ch", "www.fedlex.admin.ch"),
        "anker": aid,
        "quelle": url,
        "abgerufen": dt.date.today().isoformat(),
        **extrahiere(docs[sr], aid),
    }


def schreibe(ziel, eintrag):
    """Schreibt nur, wenn sich mehr als das Abrufdatum geändert hat — so zeigt
    `git diff data/wortlaut/` nach einem Lauf genau die Artikel, deren Text
    oder Stand sich in der amtlichen Quelle geändert hat."""
    if ziel.exists():
        alt = json.loads(ziel.read_text(encoding="utf-8"))
        if {k: v for k, v in alt.items() if k != "abgerufen"} == \
                {k: v for k, v in eintrag.items() if k != "abgerufen"}:
            return ziel
    ziel.parent.mkdir(parents=True, exist_ok=True)
    ziel.write_text(json.dumps(eintrag, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return ziel


if __name__ == "__main__":
    main()
