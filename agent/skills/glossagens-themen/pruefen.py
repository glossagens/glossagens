#!/usr/bin/env python3
"""Prüft ein Glossagens-Thema (oder einen Kommentar) gegen die zitierten Entscheide.

    python3 agent/skills/glossagens-themen/pruefen.py content/themen/{slug}
    python3 agent/skills/glossagens-themen/pruefen.py content/themen/{slug}/_index.md

Prüft:
  1. Jeder Link auf entscheidsuche.ch ist erreichbar (HTTP 200), und ein
     angehängter Anker (#consideration_7.1) kommt im Dokument tatsächlich vor.
  2. Jedes «…»-Zitat steht wörtlich in einem der verlinkten Entscheide.
     Auslassungen […] teilen das Zitat in Stücke, die einzeln gesucht werden.
     Verglichen wird nach Vereinheitlichung von Leerraum und Strichen (– — -);
     Seitenmarken im Volltext («BGE 121 III 219 S. 226») werden entfernt.
  3. Jede ##/###-Überschrift trägt einen festen Anker {#id}.

Die Volltexte werden einmal geladen und im temporären Verzeichnis zwischengespeichert
(glossagens-entscheide/). Exit 1, sobald etwas fehlt. Nur Standardbibliothek.

«…» ist ausschliesslich wörtlichen Zitaten vorbehalten. Begriffe und Bezeichnungen
gehören kursiv gesetzt, sonst meldet das Skript sie als fehlendes Zitat.
"""

import hashlib
import html
import re
import sys
import tempfile
import urllib.request
from pathlib import Path

CACHE = Path(tempfile.gettempdir()) / "glossagens-entscheide"
LINK = re.compile(r"\((https://entscheidsuche\.ch/docs/[^)\s#]+)(?:#([^)\s]+))?\)")
SEITE = re.compile(r"BGE \d+ [IVab]+ \d+ S\. \d+")


def norm(t):
    t = t.replace(" ", " ").replace("–", "-").replace("—", "-")
    return re.sub(r"\s+", " ", t).strip()


def laden(url):
    CACHE.mkdir(exist_ok=True)
    f = CACHE / (hashlib.sha1(url.encode()).hexdigest() + ".html")
    if f.exists():
        return 200, f.read_text(encoding="utf-8", errors="replace")
    try:
        with urllib.request.urlopen(url, timeout=40) as r:
            roh = r.read().decode("utf-8", "replace")
            status = r.status
    except Exception as e:  # noqa: BLE001 — jeder Fehler ist ein Befund
        return str(e), ""
    if status == 200:
        f.write_text(roh, encoding="utf-8")
    return status, roh


def klartext(roh):
    t = html.unescape(re.sub(r"<[^>]+>", " ", roh))
    return norm(SEITE.sub(" ", t))


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    pfad = Path(sys.argv[1])
    if pfad.is_dir():
        pfad = pfad / "_index.md"
    text = pfad.read_text(encoding="utf-8")
    body = text.split("\n---\n", 1)[1] if text.startswith("---") else text
    fehler = 0

    print(f"== Links ({pfad})")
    dokumente = {}
    for url, anker in sorted(set(LINK.findall(body))):
        status, roh = laden(url)
        if url not in dokumente and roh:
            dokumente[url] = klartext(roh)
        a_ok = not anker or f'id="{anker}"' in roh
        ok = status == 200 and a_ok
        fehler += not ok
        hinweis = "" if a_ok else f"  ANKER FEHLT: #{anker}"
        print(f"  {'ok ' if ok else 'XX '} {status} {url.rsplit('/', 1)[-1]}{('#' + anker) if anker else ''}{hinweis}")

    print("\n== Zitate «…»")
    for z in re.findall(r"«([^»]+)»", body):
        teile = [norm(x) for x in z.split("[…]") if len(norm(x)) > 3]
        treffer = [u for u, t in dokumente.items() if all(p in t for p in teile)]
        if not treffer and teile and teile[-1].endswith("."):
            ohne = teile[:-1] + [teile[-1][:-1]]
            if any(all(p in t for p in ohne) for t in dokumente.values()):
                print(f"  XX  Satzpunkt gehört nicht ins Zitat (im Original folgt eine Klammer o. ä.): «{z[:70]}…»")
                fehler += 1
                continue
        if treffer:
            print(f"  ok  «{z[:80]}» → {treffer[0].rsplit('/', 1)[-1]}")
        else:
            fehler += 1
            print(f"  XX  nicht wörtlich in den verlinkten Entscheiden: «{z[:100]}»")

    print("\n== Überschriften")
    for h in re.findall(r"(?m)^#{2,3} [^\n]*$", body):
        if not re.search(r"\{#[a-z0-9-]+\}\s*$", h):
            fehler += 1
            print(f"  XX  ohne festen Anker: {h}")
    print("  (geprüft)")

    print(f"\n{'Keine Befunde.' if not fehler else f'{fehler} Befund(e).'}")
    sys.exit(1 if fehler else 0)


if __name__ == "__main__":
    main()
