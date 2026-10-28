---
name: glossagens-lint
description: >
  Verifiziert die Gesetzeswortlaute der Glossagens-Kommentarartikel gegen den authentischen Fedlex-Text und korrigiert
  Befunde. Bietet den Workflow /lint ({gesetz} | Art. {NR} {gesetz}): prüft jeden zitierten Gesetzestext auf
  Korrektheit/Aktualität (korrekt, veraltet, falsche Norm, halluziniert, unvollständig), wendet sichere Korrekturen
  automatisch an (Wortlaut, Übersichts-Labels) und schlägt inhaltliche Überarbeitungen sowie Löschungen unbrauchbarer
  Artikel zur Bestätigung vor.
version: 2.0.0
author: Hermes Agent
license: MIT
tools:
  - mcp__fedlex-connector__get_article
  - mcp__fedlex-connector__get_law_text
  - mcp__fedlex-connector__get_article
  - mcp__fedlex-connector__search_by_title
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
konsolidierten Fedlex-Text ab und behebt Befunde nach einem festen Autonomie-Vertrag.

> **Seit Oktober 2026: Wortlaut per Shortcode.** Der Normtext steht nicht mehr als
> Blockquote im Bundle. Der Abschnitt `## Gesetzeswortlaut` enthält nur
> `{{< wortlaut >}}`; der Text liegt in `data/wortlaut/{gesetz}/art-{nr}.json` und wird von
> `scripts/wortlaut.py` aus der amtlichen Quelle erzeugt (Bundesrecht: Fedlex-HTML der
> geltenden Konsolidierung; kantonales Recht: LexWork-API der kantonalen Sammlung). Ein
> Wortlaut-Fehler im Sinne von «halluziniert» oder «falsche Norm» ist damit für
> umgestellte Artikel ausgeschlossen. Der Lint prüft deshalb zweierlei: ob die Daten
> **aktuell** sind (Gesetzesrevision seit dem letzten Lauf?) und ob noch **Altbestand**
> mit Blockquote existiert, der umzustellen ist.

> **Quelle: Fedlex zuerst.** Der Normtext kommt aus der Fedlex-MCP —
> `mcp__fedlex-connector__get_article` (`rs_number`, `article`; `date` für einen
> historischen Stand), `get_law_text` für ganze Erlasse, `search_by_title` wenn die
> SR-Nummer unklar ist. `get_law` der opencaselaw-MCP ist **nur Rückfallebene**: bei
> kantonalem Recht (Fedlex führt nur Bundesrecht) oder wenn Fedlex die Norm nicht
> liefert. Grund: opencaselaw sperrt den Glossagens-Client seit dem 23.08.2026 per IP
> (HTTP 403); Fedlex war nie betroffen. Wird der Rückfall benutzt, im Revisionsvermerk
> festhalten. Für **Entscheide** bleibt opencaselaw bzw. entscheidsuche massgebend.


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
| `scripts/wortlaut.py` laufen lassen (Daten auf geltenden Stand bringen) | ✅ ja (sichere Korrektur) |
| Altbestand-Blockquote durch `{{< wortlaut >}}` **ersetzen** | ✅ ja (sichere Korrektur) |
| Falsches Themen-Label in der Übersichts-Tabelle korrigieren | ✅ ja (sichere Korrektur) |
| `lastmod` im Frontmatter aktualisieren | ✅ ja |
| `revisions`-Eintrag für die Lint-Änderung ergänzen | ✅ ja (Pflicht bei jeder Änderung) |
| Kommentar-**Fliesstext** sachlich überarbeiten | ⛔ erst nach Bestätigung |
| Artikel/Bundle **löschen** + Tabellenzeile entfernen | ⛔ erst nach Bestätigung |

Sichere Fixes betreffen ausschliesslich den **wörtlich aus Fedlex übernommenen Text**
und faktisch belegbare Labels. Alles, was inhaltliche Wertung erfordert, wird nur
**vorgeschlagen** und nach Freigabe ausgeführt.

---


### Kostenregel gegenüber opencaselaw (verbindlich)

opencaselaw ist nichtkommerziell und stellt den Bestand gratis bereit. Die
Lookups laufen gegen lokale SQLite-Indizes und sind laut Fair-Use-Richtlinie
ausdrücklich frei nutzbar: `get_law`, `get_legislation`, `get_decision`,
`get_decision_structure`, `get_erwaegung`, `get_regeste`, `get_materialien`,
`cite`, `get_article_history`.

**Gesperrt — nie aufrufen:** `check_claim_support`, `attest_response`, `reflect`.
Diese Tools rufen serverseitig Claude auf und kosten den Betreiber $0.05–$0.50
pro Aufruf; das Kontingent liegt bei 200 Aufrufen pro Tag und IP. Am 23.08.2026
wurde der Glossagens-Client wegen Überzugs (4229 Aufrufe an einem Tag) per IP
gesperrt. Ob ein Entscheid eine Aussage trägt, wird stattdessen selbst beurteilt:
Text über `get_erwaegung` / `get_regeste` holen und den Satz gegen **diesen** Text
prüfen — ohne wörtliche Belegstelle kein Beleg. Regeln dazu in
`agent/skills/glossagens-audit/judge-prompt.md` im Glossagens-Repo.

**Sparsam:** Die Suchtools (`search_*`, `find_*`) tragen einen kleinen LLM-Anteil
(Query-Parse, Expansion, Rerank). Wer eine Referenz kennt, schlägt sie nach
(`cite`), statt sie zu suchen; wer eine Erwägungsnummer sucht, holt die Struktur
(`get_decision_structure`), statt `find_relevant_erwaegung` zu rufen.

## ANTI-HALLUZINATIONS-REGELN

1. **Nie** einen Gesetzeswortlaut aus dem Gedächtnis schreiben — und auch keinen von Hand
   in den Bundle setzen. Der Text kommt ausschliesslich über `scripts/wortlaut.py` in
   `data/wortlaut/`. Die Fedlex-MCP (`mcp__fedlex-connector__get_article`) dient der
   Gegenkontrolle und der Recherche, nicht als Kopiervorlage.
2. Im Bericht stets das **Konsolidierungsdatum** aus der Fedlex-Antwort nennen
   (z.B. „Stand 2026-01-01").
3. Findet Fedlex einen Artikel nicht (z.B. SR-Nr. unklar), zuerst
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

## Schritt 2 — BESTAND AUFNEHMEN

```bash
cd content/kommentar/{gesetz}
grep -L '{{< wortlaut' art-*/_index.md     # Altbestand: noch kein Shortcode
grep -l '{{< wortlaut' art-*/_index.md     # umgestellt
```

Altbestand erkennt man auch am Blockquote unter `## Gesetzeswortlaut` / `## Gesetzestext` /
`## Wortlaut`. Artikel ganz ohne Wortlaut-Abschnitt sind kein Befund, sondern ein Hinweis:
Abschnitt anlegen (Schritt 6).

## Schritt 3 — DATEN AKTUALISIEREN

```bash
python3 scripts/wortlaut.py content/kommentar/{gesetz}/art-*        # ganzes Gesetz
python3 scripts/wortlaut.py content/kommentar/{gesetz}/art-{nr}     # ein Artikel
git diff --stat data/wortlaut/{gesetz}/
```

Das Skript holt die **geltende** Fassung (Fedlex: jüngste Konsolidierung mit Inkrafttreten
bis heute; künftige Fassungen werden übergangen; `--stand YYYY-MM-DD` für einen anderen
Stichtag). Eine Datei wird nur neu geschrieben, wenn sich mehr als das Abrufdatum geändert
hat — der `git diff` zeigt also genau die Artikel, deren Text oder Konsolidierungsstand sich
seit dem letzten Lauf geändert hat. Fehlermeldungen (`FEHLER …`) betreffen nur den
jeweiligen Artikel; typische Ursachen: falsche SR-Nummer in der Gesetzesseite, Kanton ohne
Eintrag in `LEXWORK` (scripts/wortlaut.py), Artikel auf Fedlex nicht vorhanden.

## Schritt 4 — ÄNDERUNGEN KLASSIFIZIEREN

Für jede geänderte Datei den Diff von `html` lesen:

| Status | Bedeutung |
|--------|-----------|
| ✅ NUR STAND | `stand`/`quelle` neu, Normtext unverändert (neue Konsolidierung wegen anderer Artikel) |
| 🟠 REVIDIERT | Normtext geändert — Gesetzesrevision. Kommentar prüfen (Schritt 5) |
| 🔴 AUFGEHOBEN | Artikel auf Fedlex aufgehoben («Aufgehoben durch …») |

Beim **Altbestand** zusätzlich den bisherigen Blockquote mit den Daten vergleichen und wie
bisher klassifizieren: ✅ KORREKT · 🟡 UNVOLLSTÄNDIG · 🟠 VERALTET · 🔴 FALSCHE NORM ·
🔴 HALLUZINIERT. Aufgehobene Absätze zeigt Fedlex als «… Aufgehoben durch …».

## Schritt 5 — KOMMENTAR-BRAUCHBARKEIT (nur für 🟠/🔴)

Den Kommentar-Fliesstext lesen und beurteilen, ob er die **richtige** Norm behandelt:
- **Unbrauchbar**, wenn der Kommentar durchgehend eine andere/falsche Norm oder
  aufgehobenes Recht erklärt (Fliesstext lässt sich nicht durch blossen Wortlaut-Tausch
  retten). → Kandidat für **Löschung** (Bestätigung nötig).
- **Brauchbar mit Korrektur**, wenn der Kommentar die richtige Norm behandelt und nur der
  Wortlaut bzw. einzelne Absatzverweise/Passagen falsch sind. → Wortlaut-Fix (sicher) +
  ggf. vorgeschlagene Fliesstext-Korrektur (Bestätigung nötig).

## Schritt 6 — SICHERE FIXES ANWENDEN (ohne Rückfrage)

1. **Altbestand umstellen**: Den Blockquote unter der Wortlaut-Überschrift durch die Zeile
   `{{< wortlaut >}}` ersetzen, ebenso reine Quellen-/Standzeilen darunter («*Wortlaut
   geprüft gegen Fedlex …*», «*Quelle: Fedlex …*») — Stand und Fassungsvermerke zeigt der
   Shortcode selbst. Inhaltliche Sätze (z. B. zur Entstehungsgeschichte) bleiben stehen.
   Fehlt der Abschnitt, `## Gesetzeswortlaut` mit dem Shortcode vor dem ersten anderen
   `##`-Abschnitt anlegen. Zitiert der Abschnitt eine Bezugsnorm mit, dafür
   `{{< wortlaut gesetz="{gesetz}" art="art-{nr}" >}}` (Daten vorher mit dem Skript holen).
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
       note: "Lint: Wortlaut auf Fedlex-Stand {stand} nachgeführt / auf Shortcode umgestellt"
   ```
   Der Eintrag ist auch dann Pflicht, wenn sich nur `data/wortlaut/…json` geändert hat
   (🟠 REVIDIERT): Der Leser sieht einen anderen Normtext, das gehört in die Historie des
   Artikels. Der Lint prüft nur den Gesetzestext, nicht die Entscheide — die `note`
   sagt deshalb nichts über die Belege. Ältere Einträge unverändert erhalten.

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
Geprüft:        {N} Artikel ({U} umgestellt, {A} Altbestand)
✅ Unverändert / nur Stand: {Anzahl}
🟠 Revidiert:    {Liste + was sich geändert hat}
🔴 Aufgehoben:   {Liste}
Altbestand:     {Liste + Klassifikation alt vs. Fedlex}

Sichere Fixes angewendet:
  - Daten nachgeführt:   {Artikel}
  - Auf Shortcode umgestellt: {Artikel}
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
| `python3 scripts/wortlaut.py {bundles…}` | **Primär.** Erzeugt/aktualisiert `data/wortlaut/` aus Fedlex bzw. LexWork; nur Standardbibliothek |
| `mcp__fedlex-connector__get_article` | Gegenkontrolle eines einzelnen Artikels; liefert das Konsolidierungsdatum |
| `mcp__fedlex-connector__search_by_title` | SR-Nummer klären, wenn sie unbekannt ist |
| `mcp_opencaselaw_get_law` | **Nur Rückfall** — kantonales Recht oder wenn Fedlex die Norm nicht führt |
| `mcp_opencaselaw_search_laws` | Rückfall, um Abkürzung/SR-Nummer zu klären |

**Effizienz**: Das Skript lädt pro Erlass ein einziges HTML-Dokument (Cache in
`resources/wortlaut/`, gitignored) — ein Gesamt-Lint über alle Gesetze dauert wenige Minuten.

**Schweizer Rechtschreibung** in allen Ausgaben (kein Eszett).
