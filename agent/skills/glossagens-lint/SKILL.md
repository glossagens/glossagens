---
name: glossagens-lint
description: >
  Verifiziert die Gesetzeswortlaute der Glossagens-Kommentarartikel gegen den authentischen Fedlex-Text und korrigiert
  Befunde. Bietet den Workflow /lint ({gesetz} | Art. {NR} {gesetz}): prüft jeden zitierten Gesetzestext auf
  Korrektheit/Aktualität (korrekt, veraltet, falsche Norm, halluziniert, unvollständig), wendet sichere Korrekturen
  automatisch an (Wortlaut, Übersichts-Labels) und schlägt inhaltliche Überarbeitungen sowie Löschungen unbrauchbarer
  Artikel zur Bestätigung vor.
version: 1.0.0
author: Hermes Agent
license: MIT
tools:
  - mcp_opencaselaw_get_law
  - mcp_opencaselaw_search_laws
metadata:
  hermes:
    tags: [Glossagens, Legal, Lint, Verification, QualityControl]
---

# Glossagens Lint — Gesetzestext-Verifikation

## Zweck

Dieser Skill prüft, ob die in den Glossagens-Kommentaren zitierten **Gesetzeswortlaute**
tatsächlich korrekt und aktuell sind oder ob sie veraltet, falsch (andere Norm/anderes
Gesetz) oder halluziniert sind. Er gleicht jeden zitierten Text mit dem authentischen,
konsolidierten Fedlex-Text ab (`get_law`) und behebt Befunde nach einem festen
Autonomie-Vertrag.

## Geltungsbereich

Nur für **dieses Repo** (die publizierte Hugo-Site, üblicher Pfad `/repos/glossagens` bzw.
`/opt/glossagens`). Artikel liegen als **Page Bundles**:

```
content/kommentar/{gesetz}/
├── _index.md                 ← Gesetzesübersicht (Tabelle „Kommentierte Artikel")
└── art-{nr}/
    ├── _index.md             ← Hauptkommentar, enthält den zitierten Gesetzestext
    └── rechtsprechung.md
```

Das andere Skill `gesetzeskommentar-workflows` arbeitet auf dem Flat-File-Arbeitsrepo
(`Art_NR_StPO.md`) — **nicht** verwechseln.

---

## AUTONOMIE-VERTRAG (verbindlich)

**Modus: «Prüfen + sichere Fixes».**

| Aktion | Erlaubt ohne Rückfrage? |
|--------|--------------------------|
| Gesetzeswortlaut gegen Fedlex verifizieren | ✅ ja |
| Gesetzeswortlaut durch verifizierten Fedlex-Text **ersetzen** | ✅ ja (sichere Korrektur) |
| Falsches Themen-Label in der Übersichts-Tabelle korrigieren | ✅ ja (sichere Korrektur) |
| `lastmod` im Frontmatter aktualisieren | ✅ ja |
| `revisions`-Eintrag für die Lint-Änderung ergänzen | ✅ ja (Pflicht bei jeder Änderung) |
| Kommentar-**Fliesstext** sachlich überarbeiten | ⛔ erst nach Bestätigung |
| Artikel/Bundle **löschen** + Tabellenzeile entfernen | ⛔ erst nach Bestätigung |
| `agent_verified` auf `true` setzen | ⛔ nur wenn explizit verlangt |

Sichere Fixes betreffen ausschliesslich den **wörtlich aus `get_law` übernommenen Text**
und faktisch belegbare Labels. Alles, was inhaltliche Wertung erfordert, wird nur
**vorgeschlagen** und nach Freigabe ausgeführt.

---

## ANTI-HALLUZINATIONS-REGELN

1. **Nie** einen Gesetzeswortlaut aus dem Gedächtnis schreiben. Jeder Ersatztext stammt
   wörtlich aus dem `text`-Feld von `mcp_opencaselaw_get_law`.
2. Im Bericht stets das **Konsolidierungsdatum** aus der `get_law`-Antwort nennen
   (z.B. „Stand 2026-01-01").
3. Findet `get_law` einen Artikel nicht (z.B. SR-Nr./Abkürzung unklar), zuerst
   `search_laws` zur Klärung; im Zweifel als „nicht verifizierbar" melden, **nicht** raten.
4. Keine neuen Urteils-/Literaturzitate in Korrekturen erfinden; bei inhaltlichen
   Überarbeitungen nur belegbare Verweise verwenden.

---

# WORKFLOW: `/lint`

## Aufrufformen

- `/lint {gesetz}` — prüft **alle** Artikel eines Gesetzes (z.B. `/lint stgb`).
- `/lint {gesetz} art-{nr}` oder `/lint Art. {NR} {gesetz}` — prüft **einen** Artikel.
- `/lint` ohne Argument → nachfragen, welches Gesetz/welcher Artikel.

`{gesetz}` ist der Verzeichnisname unter `content/kommentar/` (z.B. `stgb`, `stpo`, `or`)
und zugleich die Fedlex-Abkürzung in Grossschreibung (`StGB`, `StPO`, `OR`, …).

---

## Schritt 1 — INIT

1. Zielverzeichnis bestimmen: `content/kommentar/{gesetz}/`. Existiert es nicht →
   `ls content/kommentar/` zeigen und nachfragen.
2. Bei Gesamt-Lint: alle `art-*/`-Bundles auflisten.
3. Fedlex-Abkürzung ableiten (`stgb` → `StGB`). Falls unklar → `search_laws`.

## Schritt 2 — GESETZESTEXT EXTRAHIEREN

Aus jeder `art-{nr}/_index.md` den zitierten Wortlaut herausziehen. Die Überschrift
variiert in den Bestandsdaten — **alle** Varianten berücksichtigen:

```
## Gesetzeswortlaut   |   ## Gesetzestext   |   ## Wortlaut
### Wortlaut          |   ## Art. X — Wortlaut
```

Praktisch: den Blockquote-Abschnitt (`>`-Zeilen) zwischen der Wortlaut-Überschrift und
der nächsten `##`/`###`-Überschrift bzw. bis `> **Annotation`. Sammel-Extraktion z.B.:

```bash
cd content/kommentar/{gesetz}
for d in art-*/; do
  f="${d}_index.md"; [ -f "$f" ] || continue
  echo "===== $f ====="
  awk '/^#{2,3} *(Gesetzeswortlaut|Gesetzestext|Wortlaut|Art\. .*Wortlaut)/{flag=1;next}
       /^#{2,3} /{if(flag)exit} /^> \*\*Annotation/{exit} flag' "$f"
done
```

## Schritt 3 — ARTIKELNUMMER → `get_law`-PARAMETER

Aus dem Verzeichnisnamen `art-{nr}` den `article`-Parameter bilden:
- führendes `art-` entfernen, führende Nullen des Zahlteils streichen, Buchstabensuffix behalten.
- `art-001` → `"1"`, `art-090` → `"90"`, `art-066a` → `"66a"`, `art-077b` → `"77b"`,
  `art-305bis` → `"305bis"`.

## Schritt 4 — VERIFIZIEREN

Für jeden Artikel `mcp_opencaselaw_get_law` mit `{ abbreviation: "{GESETZ}", article: "{nr}" }`
aufrufen (parallele Aufrufe in Batches von ~6–8 sind effizient). Den zurückgegebenen Text
**Absatz für Absatz** mit dem zitierten Wortlaut vergleichen und klassifizieren:

| Status | Bedeutung |
|--------|-----------|
| ✅ KORREKT | Wortlaut stimmt (geringfügige Formatunterschiede ignorieren) |
| 🟡 UNVOLLSTÄNDIG | richtiger Artikel, aber Absätze/Ziffern fehlen |
| 🟠 VERALTET | frühere, nicht mehr geltende Fassung (z.B. Begriffe „Zuchthaus/Gefängnis", alte Strafdrohung, Vor-Revisions-Text) |
| 🔴 FALSCHE NORM | zitiert einen anderen Artikel/ein anderes Gesetz (z.B. Art. 90 SVG statt StGB; „Verwahrung" unter Art. 60) |
| 🔴 HALLUZINIERT | Absätze/Sätze, die im Gesetz nicht existieren |

**Hinweise**
- Aufgehobene Absätze: `get_law` zeigt sie als „… Aufgehoben durch …". Zitiert ein
  Kommentar Inhalt für einen aufgehobenen Absatz → 🔴.
- Revisionen prüfen: Wenn der Kommentar vorgibt, die geltende Fassung zu behandeln, der
  Text aber einer früheren entspricht → 🟠 (z.B. Sexualstrafrecht seit 1.7.2024).

## Schritt 5 — KOMMENTAR-BRAUCHBARKEIT (nur für 🟠/🔴)

Den Kommentar-Fliesstext lesen und beurteilen, ob er die **richtige** Norm behandelt:
- **Unbrauchbar**, wenn der Kommentar durchgehend eine andere/falsche Norm oder
  aufgehobenes Recht erklärt (Fliesstext lässt sich nicht durch blossen Wortlaut-Tausch
  retten). → Kandidat für **Löschung** (Bestätigung nötig).
- **Brauchbar mit Korrektur**, wenn der Kommentar die richtige Norm behandelt und nur der
  Wortlaut bzw. einzelne Absatzverweise/Passagen falsch sind. → Wortlaut-Fix (sicher) +
  ggf. vorgeschlagene Fliesstext-Korrektur (Bestätigung nötig).

## Schritt 6 — SICHERE FIXES ANWENDEN (ohne Rückfrage)

1. **Wortlaut ersetzen**: Den zitierten Block durch den verifizierten `get_law`-Text
   ersetzen. Formatierung des Bundles beibehalten (Blockquote `>`, Absatznummerierung
   `1`, `2`, … wie im Bestand). Fedlex-Quellenfussnoten (`Fassung gemäss …`) dürfen
   gekürzt werden, der **normative Satz** muss wörtlich stimmen.
2. **Übersichts-Labels**: In `content/kommentar/{gesetz}/_index.md` Themen-Labels, die dem
   (korrekten) Artikelinhalt widersprechen, auf den zutreffenden Randtitel korrigieren.
3. **`lastmod`** im Frontmatter geänderter Dateien auf das heutige Datum setzen
   (`date` unverändert lassen).
4. **`revisions`-Eintrag** (Pflicht): In jeder geänderten Datei **zuoberst** in der
   `revisions:`-Liste einen neuen Eintrag ergänzen (Liste anlegen, falls sie fehlt):
   ```yaml
   revisions:
     - date: {heute}
       by: "Claude Code"
       model: "{exakte Modell-ID, z. B. claude-opus-4-8}"
       mcp_verified: true          # Wortlaut/Entscheide wurden per opencaselaw-MCP (get_law/cite) geprüft
       note: "Lint: Wortlaut gegen Fedlex verifiziert / Labels korrigiert"
   ```
   `mcp_verified: true` ist hier zulässig, weil der Lint jeden Ersatztext aus `get_law`
   bezieht. Ältere Einträge unverändert erhalten.

## Schritt 7 — BESTÄTIGUNGSPFLICHTIGES VORSCHLAGEN

Eine **Aktionsliste** präsentieren und auf Freigabe warten:
- inhaltliche Fliesstext-Überarbeitungen (mit konkreten Diffs/Stellen),
- Löschungen unbrauchbarer Bundles (`rm -rf art-{nr}/`) + Entfernen der Tabellenzeile.

Erst nach „ja/ok" ausführen. Vor jeder Löschung den Bundle-Inhalt nochmals kurz prüfen und
sicherstellen, dass keine anderen Artikel darauf verlinken
(`grep -rn "\.\./art-{nr}"`).

## Schritt 8 — BERICHT

Strukturierten Bericht ausgeben:

```
LINT-BERICHT: {GESETZ}  (Fedlex-Stand: {Konsolidierungsdatum})
──────────────────────────────────────────────
Geprüft:        {N} Artikel
✅ Korrekt:      {Liste}
🟡 Unvollständig: {Liste + was fehlt}
🟠 Veraltet:     {Liste + alte vs. geltende Fassung}
🔴 Falsch/halluz.: {Liste + Befund}

Sichere Fixes angewendet:
  - Wortlaut korrigiert: {Artikel}
  - Labels korrigiert:   {Artikel}

Zur Bestätigung vorgeschlagen:
  - Fliesstext-Überarbeitung: {Artikel + Begründung}
  - Löschung (unbrauchbar):   {Artikel + Begründung}

Nicht verifizierbar: {Liste + Grund}
```

Commit/Push nur, wenn der Benutzer es verlangt (Projektkonvention: direkter Commit auf
`main` löst Auto-Deploy aus).

---

## Technische Referenz

| Call | Einsatz |
|------|---------|
| `mcp_opencaselaw_get_law` | Autoritativer Artikel-Wortlaut (`abbreviation`+`article`); liefert Konsolidierungsdatum |
| `mcp_opencaselaw_search_laws` | Abkürzung/SR-Nummer klären, falls `get_law` nicht greift |

**Effizienz**: `get_law`-Aufrufe parallel batchen. Bei Gesamt-Lint zuerst alle Wortlaute
extrahieren, dann in Batches verifizieren, dann Fixes bündeln.

**Schweizer Rechtschreibung** in allen Ausgaben (kein Eszett).
