#!/usr/bin/env python3
"""Übernimmt die Sachgebiete aus bger-update nach data/sachgebiete/bger.yaml.

    scripts/sachgebiete.py                         # ../bger-update als Quelle
    scripts/sachgebiete.py --quelle PFAD/sachgebiete.py
    scripts/sachgebiete.py --pruefen               # nur vergleichen, nichts schreiben

Massgebend ist `update/utils/sachgebiete.py` in bger-update: die Sachgebiete nach
der Geschäftsverteilung des Bundesgerichts mit ihren Untergebieten. Glossagens
übernimmt die Schlüssel unverändert, damit bger-update Themen und Kommentare
über dieselben Tags findet, mit denen es Urteile einordnet. Die Datei wird
deshalb nie von Hand bearbeitet; eigene Schlüssel von Glossagens (Grundlagen,
Staatsorganisation, Verfahrensrecht) stehen in data/sachgebiete/eigene.yaml,
die Einordnung der Kommentare in data/sachgebiete/zuordnung.yaml.

Die Quelldatei wird direkt als Modul geladen, ohne Django: sie importiert
ausser `re` nichts. Das Sachgebiet «Übriges» (Restfälle des BGer) wird nicht
übernommen. Nur Standardbibliothek.
"""

import argparse
import importlib.util
import json
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
ZIEL = REPO / "data" / "sachgebiete" / "bger.yaml"
STANDARD_QUELLE = REPO.parent / "bger-update" / "update" / "utils" / "sachgebiete.py"


def laden(pfad):
    spec = importlib.util.spec_from_file_location("bger_sachgebiete", pfad)
    modul = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modul)
    return modul


def q(text):
    # JSON-Strings sind gültiges YAML und nehmen Anführungszeichen, Umlaute und › sicher auf
    return json.dumps(text, ensure_ascii=False)


def erzeugen(modul):
    stand = re.search(r"Stand ([0-9.]+)", modul.__doc__ or "")
    untergebiete = {sg: liste for sg, liste in modul.UNTERGEBIETE}

    z = [
        "# ERZEUGT von scripts/sachgebiete.py — nicht von Hand bearbeiten.",
        "# Quelle: bger-update, update/utils/sachgebiete.py (Geschäftsverteilung des Bundesgerichts).",
        "# Eigene Schlüssel von Glossagens: data/sachgebiete/eigene.yaml.",
        f"quelle: {q('bger-update')}",
        f"stand: {q(stand.group(1) if stand else '')}",
        "hauptgebiete:",
    ]
    for slug, name in modul._HAUPTGEBIETE:
        if slug:
            z.append(f"  - {{ key: {q(slug)}, name: {q(name)} }}")
    z.append("sachgebiete:")
    for key, name, haupt in modul.SACHGEBIETE:
        if not haupt:
            # «Übriges (Aufsichts- und Verwaltungssachen)» ordnet bei bger-update nur
            # Restfälle ein; als Tag für Inhalte taugt es nicht.
            continue
        z.append(f"  - key: {q(key)}")
        z.append(f"    name: {q(name)}")
        z.append(f"    hauptgebiet: {q(haupt)}")
        if key in untergebiete:
            z.append("    untergebiete:")
            for u, uname, _muster in untergebiete[key]:
                z.append(f"      - {{ key: {q(f'{key}.{u}')}, name: {q(uname)} }}")
    return "\n".join(z) + "\n"


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--quelle", type=Path, default=STANDARD_QUELLE)
    ap.add_argument("--pruefen", action="store_true", help="nur vergleichen; Exit 1 bei Abweichung")
    args = ap.parse_args()

    if not args.quelle.is_file():
        sys.exit(f"Quelle nicht gefunden: {args.quelle} (--quelle angeben)")
    neu = erzeugen(laden(args.quelle))
    alt = ZIEL.read_text(encoding="utf-8") if ZIEL.exists() else ""

    if neu == alt:
        print(f"{ZIEL.relative_to(REPO)}: unverändert")
        return
    if args.pruefen:
        sys.exit(f"{ZIEL.relative_to(REPO)} weicht von bger-update ab — scripts/sachgebiete.py ausführen")
    ZIEL.write_text(neu, encoding="utf-8")
    print(f"{ZIEL.relative_to(REPO)}: geschrieben")


if __name__ == "__main__":
    main()
