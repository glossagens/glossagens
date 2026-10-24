---
name: glossagens-themen
description: >-
  Recherchiert und baut ein Glossagens-Thema (content/themen/{slug}/) — eine Darstellung übergeordneter
  Konzepte, Querschnittsthemen oder Rechtsfragen, deren Antwort sich aus mehreren Normen ergibt
  (z. B. pragmatischer Methodenpluralismus, Verfassungsgerichtsbarkeit, Ablauf des Asylverfahrens,
  Folgen einer ungerechtfertigten Kündigung, kantonale Schulsysteme). Führt von der Einordnung
  (Typ, Sachgebiete, Normen) über die Recherche mit Belegledger (entscheidsuche-Volltexte, Fedlex)
  zum Aufbau nach Typ-Gerüst und zur mechanischen Prüfung aller Zitate und Links. Workflows:
  /thema (Vollworkflow), /thema-recherche (nur Ledger), /thema-pruefen (Prüfung eines bestehenden Themas).
version: 1.0.0
author: Claude Code (claude-opus-5-5)
license: CC BY-SA 4.0
tools:
  - mcp__entscheidsuche__search
  - mcp__entscheidsuche__search_by_case_number
  - mcp__entscheidsuche__fetch_document
  - mcp__fedlex-connector__get_article
  - mcp__fedlex-connector__get_law_text
  - mcp__fedlex-connector__search_by_title
metadata:
  glossagens:
    category: content-creation
    benchmarks: ["content/themen/pragmatischer-methodenpluralismus/_index.md"]
    pruefskript: "agent/skills/glossagens-themen/pruefen.py"
---

# Glossagens-Thema recherchieren und aufbauen

Ein **Thema** erklärt eine Rechtsfrage, die sich nicht an einer einzelnen Bestimmung festmachen
lässt: eine Methode, eine Institution, einen Verfahrensablauf, die Folgen eines Rechtsverstosses
oder die unterschiedliche Regelung in den Kantonen. Es verdichtet und verweist auf die Kommentare
der beteiligten Artikel; es wiederholt sie nicht.

Massstab ist das Pilotthema [`pragmatischer-methodenpluralismus`](../../../content/themen/pragmatischer-methodenpluralismus/_index.md).
Die technischen Regeln (Frontmatter, Build-Prüfungen, Index für bger-update) stehen in
`CLAUDE.md`, Abschnitt «Themen». Dieser Skill beschreibt, **wie man zu einem belastbaren Text kommt**.

> **Grundsatz.** Jede Aussage, die ein Gericht oder ein Gesetz zitiert, stammt aus einem
> heruntergeladenen Volltext oder aus Fedlex — nie aus dem Gedächtnis. Glossagens hat hunderte
> Kommentare mit erfundenen Entscheiden und Zitaten bereinigen müssen; die Fehler entstanden
> ausnahmslos dort, wo ein Agent «wusste», was ein Entscheid sagt. Wer etwas nicht belegen kann,
> lässt es weg oder formuliert es als eigene, unbelegte Einordnung.

---

## 0. Abgrenzung: Thema oder Kommentar?

| Frage | Ort |
|---|---|
| Lässt sich die Antwort vollständig an **einem** Artikel festmachen? | Kommentar `content/kommentar/{gesetz}/art-{nr}/` |
| Ergibt sich die Antwort aus **mehreren** Normen, aus Methodik oder aus dem Zusammenspiel von Bund und Kantonen? | Thema `content/themen/{slug}/` |
| Ist das Thema schon vorhanden? | `ls content/themen/` und `https://glossagens.ch/themen/index.json` prüfen — bestehende Themen ausbauen statt ein zweites anlegen |

---

## 1. Einordnung (vor jeder Recherche)

Lege die vier Eckwerte fest und notiere sie im Ledger (Abschnitt 2):

1. **Slug** — kurz, sprechend, ohne Artikelnummern: `ungerechtfertigte-kuendigung`,
   `asylverfahren`. Der Slug ist die stabile URL; bger-update verlinkt darauf.
2. **Typ** (`data/themen/typen.yaml`) — bestimmt das Gerüst (Abschnitt 4):
   `grundlage` · `institution` · `verfahren` · `rechtsfolgen` · `kantonsvergleich`.
3. **Sachgebiete** — Schlüssel aus `data/sachgebiete/bger.yaml` und `eigene.yaml`.
   - So genau wie möglich: Untergebiet vor Sachgebiet (`schuldrecht.arbeit`, nicht `schuldrecht`).
   - Mehrere sind erwünscht, wenn das Thema mehrere Gebiete berührt; mehr als ein Hauptgebiet
     macht es automatisch zum Querschnittsthema.
   - Eigene Glossagens-Schlüssel (`grundlagen.*`, `staatsorganisation.*`, `verwaltungsverfahren`,
     `zivilprozess`, `ipr`) kennt bger-update nicht. Wo ein Thema auch ein BGer-Sachgebiet berührt,
     dieses zusätzlich taggen; sonst `stichworte` setzen, über die bger-update das Thema findet.
4. **Normen** — die Bestimmungen, die das Thema auslegt oder verbindet. Format
   `{ gesetz: or, art: art-336c }`, dreistellig wie das Artikelverzeichnis. Ein noch nicht
   kommentierter Artikel ist zulässig (er erscheint als Lücke mit «Anregung einreichen»), ein
   Gesetz ohne `content/kommentar/{gesetz}/_index.md` nicht.

---

## 2. Recherche mit Belegledger

Das Ledger ist eine Arbeitsdatei im Scratchpad (nicht im Repo). Pro Zeile ein Beleg:

| Baustein | Entscheid | E. | Anker | Wörtliches Zitat (aus dem Volltext kopiert) | Sachverhalt / Ergebnis in einem Satz |
|---|---|---|---|---|---|

Ein **Baustein** ist eine Aussage, die das Thema tragen muss (z. B. «vom klaren Wortlaut nur aus
triftigen Gründen abweichen»). Die Bausteine ergeben sich aus dem Typ-Gerüst (Abschnitt 4).
Ziel: **jeder Baustein mit mindestens einem Leitentscheid**, zentrale Bausteine zusätzlich mit
einem anschaulichen Fall.

### 2.1 Leitformel und Linie finden

Fast jedes Thema hat eine Formel, mit der das Bundesgericht es einleitet. Sie ist der beste Einstieg.

```
mcp__entscheidsuche__search  query: "\"pragmatischen Methodenpluralismus\""  hierarchy: ["CH_BGE"]
```

- **Umfang**: `total` der Phrasensuche zeigt, wie verbreitet die Formel ist (mit Datum nennen).
- **Herkunft**: dieselbe Suche mit `decision_date_to` (z. B. `2000-12-31`) und `sort: "date"`
  liefert die frühesten Fundstellen. Ältere Entscheide zitieren ihre Vorgänger — den Verweisen
  folgen, bis keine frühere Quelle mehr auftaucht.
- **Varianten**: die Formel lautet oft leicht verschieden («hat sich … stets von einem
  Methodenpluralismus leiten lassen»). Mit einem Kernwort ohne Phrase nachsuchen.
- Für Bausteine ohne feste Formel nach der typischen Wendung suchen
  (`"triftige Gründe dafür bestehen"`, `"neueren Texten" Materialien`,
  `"qualifizierten Schweigens"`). Die Treffer-Snippets zeigen die Formulierung; erst der
  Volltext belegt sie.

Kantonale Entscheide (`hierarchy` des Kantons, siehe `mcp__entscheidsuche__list_hierarchy`) sind
für Kantonsvergleiche und Verfahrensthemen unverzichtbar; für Grundsatzfragen genügen meist BGE.

### 2.2 Volltexte laden und Fundstellen verifizieren

`fetch_document` liefert lange Entscheide nur gekürzt oder als Datei. Zuverlässiger: das HTML
direkt laden — es enthält die Erwägungsanker.

```bash
D=$SCRATCH/entscheide; mkdir -p $D
curl -s -o $D/{ID}.html "https://entscheidsuche.ch/docs/CH_BGE/{ID}.html"     # {ID} aus document_url
grep -o 'id="consideration_[^"]*"' $D/{ID}.html | head                       # vorhandene Anker
```

Für jeden Beleg:

1. Die Erwägung im Volltext lesen, nicht nur den Treffer-Satz. Prüfen, ob die Aussage dort
   tragend ist oder nur referiert wird.
2. **Erwägungsnummer** aus dem Text übernehmen (`E. 7.1`, `E. 1d/aa`).
3. **Anker** nur, wenn genau diese Nummer als `id="consideration_…"` existiert. Achtung:
   Ganzzahlige Erwägungen tragen einen Punkt (`#consideration_5.`). Ältere Entscheide haben nur
   Anker auf oberster Ebene — für `E. 1d/aa` oder `E. 5c` dann **ohne** Anker verlinken.
4. **Zitat** aus dem Volltext kopieren, nie abtippen oder glätten.
5. Sachverhalt und Ergebnis aus Regeste und Erwägung festhalten — und das **Dispositiv**
   mitprüfen, wenn das Ergebnis eine Rolle spielt (Glossagens hat Kommentare mit
   invertierten Urteilsergebnissen bereinigt).

Die **URL** wird nie konstruiert, sondern aus `document_url` der entscheidsuche-Antwort übernommen
(Muster `https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_005_BGE-121-III-219_1995-04-25.html`).
opencaselaw ist nur Rückfall, falls entscheidsuche den Entscheid nicht führt (seit 23.08.2026 ist
der Glossagens-Zugang zu opencaselaw gesperrt).

### 2.3 Normtexte

Jede Norm, deren Wortlaut im Thema erscheint, kommt per Shortcode aus der amtlichen Quelle:

```bash
python3 scripts/wortlaut.py content/kommentar/bv/art-190     # Artikelverzeichnis muss nicht existieren
```

```markdown
{{< wortlaut gesetz="bv" art="art-190" >}}
```

Das Skript braucht nur die Gesetzesseite `content/kommentar/{gesetz}/_index.md`. Die erzeugte
`data/wortlaut/{gesetz}/art-{nr}.json` wird mit committet. Normtext nie als Blockquote abschreiben.

### 2.4 Literatur

Lehrmeinungen nur, wenn das Werk eingesehen wurde **oder** ein Entscheid es zitiert — dann exakt
so, wie der Entscheid es angibt (keine ergänzten Vornamen, Auflagen oder Fundstellen), mit dem
Hinweis, dass die Angabe der Zitierung im Entscheid folgt. Lieber keine Literatur als erfundene.

---

## 3. Stil

- **Wissenschaftlich-nüchtern**, dritte Person, wie ein guter Kommentar. Keine Dramatisierung,
  keine Metaphern. Zugespitzt und adressatenbezogen nur im Schlussabschnitt «Praxishinweise».
- **Für Fachleute und interessierte Laien lesbar.** Der Kasten «Das Wichtigste in Kürze»
  (Frontmatter `kurz`) beantwortet die Frage in zwei bis drei Sätzen ohne Fachjargon; der
  Überblick erklärt, warum die Frage wichtig ist.
- **Fälle plastisch, aber knapp**: Sachverhalt in einem Satz, Ergebnis, Bedeutung für die
  Methode. Fälle sind Illustration der Bausteine, nicht deren Gliederung.
- **Zitierweise**: «…» ausschliesslich für wörtliche Zitate; Auslassungen `[…]`; der Satzpunkt
  steht ausserhalb, wenn im Original keiner folgt (oft folgt eine Klammer mit Verweisen).
  Begriffe kursiv, nicht in Guillemets. Fundstelle als `[BGE 150 V 454](URL#anker) E. 7.1`;
  Wiederholungen ohne Link mit Erwägung (`BGE 150 V 454 E. 7.2.3`).
- **Zahlen und Verbreitungsangaben** («178 Leitentscheide») nur mit Quelle und Stichtag.
- **Wertungen** klar als Einordnung formulieren und, wo möglich, an Aussagen des Gerichts binden.
- **Normen zitieren, nicht verlinken**: «Art. 337c Abs. 3 OR». Zitate in dieser Form verlinkt
  das Layout automatisch auf den Kommentar, sobald es einen gibt (`normlinks.html`). Handlinks
  auf `/kommentar/…` nur für Formulierungen wie «Kommentar zu Art. 336 OR».
- **Feste Anker** an jeder `##`/`###`-Überschrift: `## Fristlose Entlassung {#fristlose-entlassung}`.
- Tabellen als reines Markdown, nie in Code-Fences.

---

## 4. Gerüste nach Typ

Alle Typen beginnen mit `## Überblick {#ueberblick}` und enden mit
`## Praxishinweise {#praxishinweise}`, `## Leitentscheide {#leitentscheide}` (Tabelle:
Entscheid · Gegenstand · Bedeutung) und gegebenenfalls `## Literatur {#literatur}`.
Die Abschnitte «Betroffene Bestimmungen» und «Verwandte Themen» erzeugt das Layout selbst.

| Typ | Kernabschnitte dazwischen |
|---|---|
| `grundlage` (Begriff, Methode) | Rechtsgrundlage (mit Wortlaut) · Formel des Bundesgerichts · Herkunft und Entwicklung der Rechtsprechung · Bestandteile/Elemente · Grenzen · Abgrenzungen zu verwandten Figuren · Würdigung |
| `institution` (Verfassungsgerichtsbarkeit, Bundesgericht, Gemeindeautonomie) | Rechtsgrundlagen · Aufbau und Zuständigkeiten · Verfahren und Kognition · Grenzen (z. B. Art. 190 BV) · Bund–Kantone · Würdigung |
| `verfahren` (Asylverfahren, Strafbefehlsverfahren) | Überblick über die Phasen (nummerierte Liste oder Tabelle Phase · Behörde · Frist · Rechtsmittel) · je Phase ein Abschnitt mit Voraussetzungen, Fristen, typischen Fehlern · Rechtsmittelweg · Kosten |
| `rechtsfolgen` (ungerechtfertigte Kündigung, Vertragsverletzung) | Ausgangslage und Abgrenzung der Tatbestände · je Rechtsfolge ein Abschnitt (Voraussetzungen → Folge → Bemessung) · Durchsetzung (Fristen, Verfahren, Beweislast) · Folgen in anderen Rechtsgebieten (z. B. ALV, Steuern) |
| `kantonsvergleich` (Schulsysteme, Polizeirecht) | Bundesrechtlicher Rahmen und Konkordate · Vergleichstabelle (Kanton · Regelung · Erlass mit Fundstelle · Stand) · Gruppenbildung und Tendenzen · Würdigung |

Beim **Kantonsvergleich** gilt: je Kanton Quelle und Stand; wo keine verifizierte Quelle vorliegt,
steht «nicht erhoben» — keine Lücke wird aus dem Gedächtnis gefüllt. Kantonale Normtexte kommen,
wo möglich, über `scripts/wortlaut.py` (LexWork, derzeit Luzern); sonst nur mit Link auf die
amtliche Sammlung und ohne wörtliches Zitat.

---

## 5. Datei anlegen

```bash
hugo new themen/{slug}/_index.md          # Archetyp archetypes/themen.md
```

Frontmatter ausfüllen (siehe `CLAUDE.md` «Themen»): `typ`, `kurz`, `sachgebiete`, `normen`,
`stichworte`, `revisions`. `agent_verified: true` und `mcp_verified: true` nur, wenn **alle**
Zitate und Normtexte nach Abschnitt 2 verifiziert sind und `pruefen.py` keinen Befund meldet.
Die `note` des Revisionseintrags nennt Quellen und Prüfweg (Vorlage: Pilotthema).

---

## 6. Prüfung

```bash
python3 agent/skills/glossagens-themen/pruefen.py content/themen/{slug}   # Zitate, Links, Anker
./scripts/build-check.sh                                                  # Build inkl. Frontmatter-Prüfung
```

`pruefen.py` lädt jeden verlinkten Entscheid, prüft HTTP-Status und Anker und sucht jedes
«…»-Zitat wörtlich in den verlinkten Volltexten. Es prüft **nicht**, ob die Erwägungsnummer im
Fliesstext stimmt und ob ein Entscheid die ihm zugeschriebene Aussage trägt — das leistet nur
das Ledger. Danach:

- Seite lokal ansehen (`hugo server`): Kasten, Badges, betroffene Bestimmungen, verwandte Themen.
- `/themen/index.json` (im Build-Verzeichnis): `verifiziert`, `abschnitte`, `normen` des Themas.
- Auf den Artikelseiten der `normen` erscheint «In Themen behandelt».

### Häufige Fehler (aus dem Pilotthema)

| Fehler | Erkennung | Behebung |
|---|---|---|
| Satzpunkt im Zitat, obwohl im Original eine Klammer folgt | `pruefen.py` meldet «Satzpunkt gehört nicht ins Zitat» | `…unterstellen».` statt `…unterstellen.»` |
| Grammatisch angepasstes Zitat («ein zulässiger Akt» statt «um einen zulässigen Akt») | `pruefen.py`: nicht wörtlich | Satz so umbauen, dass das Original unverändert passt |
| Anker `#consideration_5` statt `#consideration_5.` | `pruefen.py`: Anker fehlt | Anker exakt aus dem HTML übernehmen |
| Anker für `E. 1d/aa` erfunden | `pruefen.py`: Anker fehlt | ohne Anker verlinken |
| Literaturangaben ergänzt (Vornamen, Bandnummern) | nur Durchsicht | exakt wie im zitierenden Entscheid |
| Ungeprüfte Mengen- oder Erstmaligkeitsaussagen | nur Durchsicht | Quelle und Stichtag nennen oder vorsichtig formulieren («frühester nachweisbarer») |
| Überschrift ohne `{#id}` | Build-Warnung und `pruefen.py` | Anker ergänzen |

---

## 7. Abschluss

- Commit nur der eigenen Dateien: `content/themen/{slug}/`, neue `data/wortlaut/…`-Dateien.
- Commit-Nachricht: `feat(themen): {Titel}` mit den tragenden Entscheiden.
- Externe Agenten reichen ein Thema per Pull Request ein und legen die Ausgabe von `pruefen.py`
  in die PR-Beschreibung. Die automatische Verifikation durch Hermes (`agent/executor.py`) kennt
  `content/themen/` noch nicht; bis dahin prüft ein Maintainer.
- Themen sind zugleich **Quelle für die Kommentare** der Normen in `normen`: Die Kommentar-Skills
  lesen sie bei Erstellung und Erweiterung und verweisen auf ihre Abschnittsanker. Anker deshalb
  nicht umbenennen, und `agent_verified` nur setzen, wenn das Thema als Ausgangspunkt taugt.

## Checkliste

- [ ] Kein bestehendes Thema deckt die Frage ab; kein einzelner Artikel genügt
- [ ] Typ, Sachgebiete (so genau wie möglich), Normen, ggf. Stichworte festgelegt
- [ ] Ledger: jeder Baustein mit Leitentscheid, Erwägung, Anker und kopiertem Zitat
- [ ] Volltexte gelesen, Dispositiv geprüft, wo das Ergebnis zählt
- [ ] Normtexte per `{{< wortlaut >}}`, Daten mit `scripts/wortlaut.py` erzeugt
- [ ] Gerüst des Typs eingehalten; `kurz` laienverständlich; feste Anker überall
- [ ] Literatur nur eingesehen oder exakt nach zitierendem Entscheid
- [ ] `pruefen.py` ohne Befund, `build-check.sh` grün, Seite angesehen
- [ ] `revisions`-Eintrag mit Quellen und Prüfweg; `agent_verified` nur bei vollständiger Prüfung
