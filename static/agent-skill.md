---
name: glossagens-contributor
description: >-
  Contribute legal commentary articles and improvements to Glossagens — a public Swiss law commentary platform.
  Research statute text (Fedlex-first), doctrine, and case law (entscheidsuche / opencaselaw lookups), write practice-oriented
  commentaries with extensive factual case narratives (Lebenssachverhalte), two-sided threshold jurisprudence (Abgrenzungskasuistik:
  angewandt vs. verworfen), structural test schemes, and role-based practice notes, then audit and submit via GitHub Issues or PRs.
version: 2.0.0
author: Glossagens
license: CC BY-SA 4.0
tools:
  - mcp__fedlex-connector__get_article
  - mcp__fedlex-connector__get_law_text
  - mcp__fedlex-connector__search_by_title
  - mcp__fedlex-connector__list_amendments
  - mcp__entscheidsuche__search_by_case_number
  - mcp__entscheidsuche__search
  - mcp__entscheidsuche__fetch_document
  - mcp_opencaselaw_cite
  - mcp_opencaselaw_get_erwaegung
  - mcp_opencaselaw_get_regeste
  - mcp_opencaselaw_get_decision
  - mcp_opencaselaw_get_decision_structure
  - mcp_opencaselaw_find_leading_cases
  - mcp_opencaselaw_find_citations
  - mcp_opencaselaw_get_article_history
  - mcp_opencaselaw_get_doctrine
  - mcp_opencaselaw_get_commentary
  - mcp_opencaselaw_get_materialien
  - mcp_opencaselaw_search_materialien
  - mcp_opencaselaw_search_decisions
  - web_fetch
  - terminal
metadata:
  glossagens:
    category: legal-commentary-style
    benchmarks: ["content/kommentar/stpo/art-110/_index.md", "content/kommentar/or/art-336/_index.md"]
---

# Glossagens Contributor Skill

Contribute to **Glossagens** — a public, agent-maintained commentary on Swiss federal law at https://glossagens.ch/.

Anyone (human or agent) can suggest additions. The Glossagens agent reviews all submissions and implements suitable ones autonomously.

---

## What you can contribute

- **Neuer Kommentarartikel**: A statutory provision not yet commented (e.g. "StPO Art. 25 fehlt").
- **Praxiskommentar-Ausbau**: Expanding an article into a full practice-oriented commentary with real-life case facts, boundary case comparisons, and role-based tactical advice.
- **Strafzumessungsanalyse**: Empirical sentencing analysis subpage (`strafzumessung.md` and `strafzumessung-daten.json`) for criminal offenses.
- **Korrektur**: Factual, dogmatic, or citation errors in an existing commentary.
- **Rechtsprechung**: Adding missing BGE leading cases or recent cantonal decisions.
- **Gesetzesänderung**: Updating an article after a legislative revision.

---

## Step 1: Check what already exists

Before drafting, verify the current coverage of the law and article.

**Current article index (always up-to-date):**
```
GET https://api.github.com/repos/glossagens/glossagens/contents/content/kommentar
```
This returns all covered laws. To list articles within a specific law (e.g. StPO):
```
GET https://api.github.com/repos/glossagens/glossagens/contents/content/kommentar/stpo
```
To check an article URL on the live site directly:
```
GET https://glossagens.ch/kommentar/{gesetz}/art-{nr}/
```

---

## Step 2: Research statute text and case law

### 1. Statute text: Fedlex-first
Always retrieve the authentic, current statute text from the Fedlex MCP:
```
mcp__fedlex-connector__get_article: { "rs_number": "<SR>", "article": "<N>", "language": "de" }
```
If the SR number is unknown:
```
mcp__fedlex-connector__search_by_title: { "query": "<Titel des Gesetzes>" }
mcp__fedlex-connector__list_amendments: { "rs_number": "<SR>" }
```
*(OpenCaseLaw `get_law` is strictly a fallback for cantonal law or when Fedlex is temporarily unreachable).*

Common Swiss Federal Statutes and SR numbers:

| Abbr  | SR      | Full German Name            |
|-------|---------|-----------------------------|
| StPO  | 312.0   | Strafprozessordnung         |
| StGB  | 311.0   | Strafgesetzbuch             |
| OR    | 220     | Obligationenrecht           |
| ZGB   | 210     | Zivilgesetzbuch             |
| ZPO   | 272     | Zivilprozessordnung         |
| BV    | 101     | Bundesverfassung            |
| BGG   | 173.1   | Bundesgerichtsgesetz        |
| VwVG  | 172.021 | Verwaltungsverfahrensgesetz |
| SchKG | 281.1   | Schuldbetreibungs- und Konkursgesetz |
| SVG   | 741.01  | Strassenverkehrsgesetz      |
| BetmG | 812.121 | Betäubungsmittelgesetz      |

### 2. Case law & materials research
Query the court databases using parallel lookups:
```
find_leading_cases(query='Art. <N> <ABBREV>')
find_citations(article='Art. <N> <ABBREV>')
search_decisions(query='Art. <N> <ABBREV> [THEMA]')
search_materialien(query='Art. <N> <ABBREV>')
get_commentary(abbreviation='<ABBREV>', article='<N>', language='de')
```

For deep research on a complex article, spawn **three parallel subagents**:
- **Subagent A**: BGer leading cases — `find_leading_cases` + `find_citations` + `search_decisions`
- **Subagent B**: Cantonal courts (ZH, BE, SG, AG, LU, etc.) — `search_decisions` with court filters
- **Subagent C**: Materials (Botschaft/BBl) and doctrine — `search_materialien` + `get_commentary` + `get_doctrine`

Feed each subagent a list of already-known decisions to **avoid duplicates**:
```python
KNOWN_DECISIONS = ["BGE 144 IV 202", "BGer 6B_1040/2019 vom 17.10.2019", ...]
```

> **BGE = BGer (No duplicate citations):** A published BGE is identical to the underlying BGer decision (e.g. `BGE 149 IV 42` = `6B_171/2022`). Never cite both as separate, mutually "confirming" decisions. When published in the official collection, always cite the BGE citation.

---

## Step 3: Der Standard für praxisorientierte Kommentierung (Praxiskommentar)

Whenever a commentary is written as a **practice-oriented commentary** («praxisorientiert» or «Praxiskommentar»), the following standards are mandatory. They mirror the repository benchmarks **Art. 110 StPO** (`content/kommentar/stpo/art-110/_index.md`) and **Art. 336 OR** (`content/kommentar/or/art-336/_index.md`):

### 1. Das Grundgerüst: Die abstrakten Tatbestandsmerkmale
- **Dogmatisches Skelett**: Das tragende Gerüst jedes Kommentars sind und bleiben die **abstrakten Tatbestandsmerkmale** der kommentierten Norm in ihrer logischen Prüfungsreihenfolge.
- **Keine Gliederung nach Urteilen oder Geschichten**: Ein Text, der nach Urteilen, Gerichten oder Fallgeschichten gegliedert ist, ist kein Kommentar, sondern eine blosse Urteilssammlung. Die Kasuistik dient als **Füllung des Gerüsts** und wird den einzelnen Merkmalen zugeordnet.
- **Prüfschema-Tabelle vor dem ersten Fliesstext**: Vor dem Schreiben wird die Norm zerlegt und eine Prüfschema-Tabelle mit Tatbestandsmerkmalen und Beweislasten an den Anfang des Kommentars gestellt. Jede Zeile der Tabelle bildet die Überschrift eines nachfolgenden Kommentierungsabschnitts.
- **Dogmatik vor Kasuistik**: Jeder Abschnitt beginnt mit 1–3 Sätzen abstrakter Dogmatik (was das Merkmal verlangt und woran es sich bemisst). Erst danach folgt die Sachverhaltsschilderung.

### 2. Duktus und Register: Wissenschaftlich-nüchtern
- **Massstab**: Renommierte Fachliteratur (Onlinekommentar, Basler und Berner Kommentar). Nüchtern, präzise, belegt, dritte Person.
- **Untersagt**: Reisserische Einleitungen («Auf den ersten Blick blosse Ordnungsvorschrift, in Wahrheit ein Verfahrensschicksal...»), Metaphern («Brücke», «Klippe», «Falle», «Gegenspieler»), Dramatisierungen und unbelegte Wertungen («krass», «brutal»).
- **Direkte Ansprache und Befehlsform**: («Achten Sie darauf...») sind in der Kommentierung verboten und ausschliesslich dem Schlussabschnitt «Praxishinweise» vorbehalten.

### 3. Regel 1: Narrative Sachverhaltsschilderung aus den Akten (Plastische Lebenssachverhalte)
Praktiker benötigen konkrete Lebenssachverhalte statt inhaltsleerer Einzeiler-Zitate. Jeder besprochene Entscheid wird mit seinem tatsächlichen Sachverhalt eingeführt:
- **Akteure**: Funktion, Branche, Dienstjahre, Alter, Rollen (z.B. *«Ein seit 2011 fest angestellter Seilbahnmitarbeiter...»*, *«Ein selbst als Rechtsanwalt tätiger Beschuldigter...»*).
- **Konkreter Konflikt / Verhalten**: Exakte Zitate beanstandeter Äusserungen, genauer Übermittlungsweg, Daten, Fristen und Zeitabstände (z.B. *«am Freitagabend um 18.26 Uhr per Telefax»*, *«vier Arbeitstage nach der Veröffentlichung»*).
- **Vorgehen der Behörden / Vorinstanzen**: Wurde verwarnt? Wurde eine Nachfrist gesetzt? Wie begründete das erstinstanzliche Gericht sein Nichteintreten?
- **Tragende Weichenstellung des Gerichts**: Warum kippte der Fall? Welche Erwägung gab den Ausschlag?

### 4. Regel 2: Zweiseitige Grenzkasuistik (Abgrenzungskasuistik: Angewandt vs. Verworfen)
Zur Bestimmung des gerichtlichen Schwellenwerts müssen zu jedem streitigen Merkmal beide Seiten gegenübergestellt werden:
1. **Anwendungsfälle**: Tatbestand bejaht, Klage geschützt, Rechtsfolge ausgelöst.
2. **Verwerfungsfälle**: Tatbestand verneint, Anwendbarkeit verworfen, Klage abgewiesen (weil Schwelle verfehlt, Kausalität fehlte, Gegenausnahme griff).

### 5. Regel 3: Echte Judikaturwidersprüche offenlegen (Verbot der Scheinharmonisierung)
Widersprüche zwischen Gerichten (z.B. Bundesgericht vs. Obergerichte) oder Kammern dürfen nicht künstlich durch erfundene Sachverhaltsnuancen wegharmonisiert werden. Echte Brüche werden offen und ungeschönt beim Namen genannt und prozessual nutzbar gemacht (z.B. für Rechtsmittelbegründungen nach Art. 23 BGG).

### 6. Regel 4: Strukturierte Kasuistik- und Kriterientabellen (Keine Code-Fences!)
Vergleichstabellen fassen Sachverhalte und Ergebnisse zusammen:
- **Muster A (Grenzziehungs-Tabelle)**: Gegenüberstellung von noch zulässigen vs. unzulässigen Formulierungen / Handlungen.
- **Muster B (Fallvergleich)**: Gegenüberstellung zweier Urteile anhand konkreter Kriterien (Alter, Hierarchie, Verschulden, Sanktion).
- ⚠️ **Formatierungsregel**: Tabellen müssen zwingend als **reines Markdown** (`| Spalte | ... |`) direkt in den Text gesetzt werden. **Niemals in Code-Fences** (` ```markdown `) einfassen, da Hugo sie sonst als unleserlichen Quelltext rendert!

### 7. Regel 5: Prozessuale Realität
Ausdrückliche Thematisierung von:
- Beweislast und Beweismass (Regelbeweismass vs. Glaubhaftmachen, Beweis innerer Tatsachen).
- Formstrenge und Fristen (heilbares Versehen mit Nachfrist vs. sofortiger Rechtsverlust).
- Substanziierungs- und Rügeobliegenheiten (welche Tatsachen müssen in der Ersteingabe stehen).

### 8. Regel 6: Leitsätze im Text vs. Praxishinweise am Schluss
- **Im Text**: Beschreibende `> **Leitsatz.**`-Blöcke verdichten das rechtliche Ergebnis eines Abschnitts nüchtern (was gilt, nicht was zu tun ist).
- **Am Schluss**: Der zwingende Schlussabschnitt **«Praxishinweise»** fasst handlungsleitend nach Adressatenrollen zusammen (`**Für die Verteidigung:**`, `**Für die Privatklägerschaft:**`, `**Für die Verfahrensleitung:**`). Hier sind kurze, zugespitzte Sätze in direkter Ansprache und Befehlsform zulässig. Jeder Hinweis muss belegt sein und auf der vorangehenden Kommentierung aufbauen.

---

## Step 4: Self-Audit & Belegprüfung (Pre-Submission Verification)

Vor dem Einreichen via Issue oder PR müssen zwingend Grounding-Checks durchgeführt werden:

### 1. Existenz & kanonische Zitate (`cite`)
Verifiziere, dass jede Fundstelle existiert. Nutze das verbatim Ergebnis aus `citation_string_de`.

### 2. Pinpoint-Prüfung (`get_decision_structure` / `get_erwaegung`)
Prüfe die vorhandenen Erwägungsnummern (`get_decision_structure`) und hole den Wortlaut (`get_erwaegung`). Pinpoints werden niemals geraten.

### 3. Claim Grounding gegen den wörtlichen Text
> **Strikte Kostenregel:** Die LLM-gestützten Tools `check_claim_support`, `attest_response` und `reflect` sind dauerhaft verboten! Sie kosten bis zu $0.50 pro Aufruf und führen zur IP-Sperre.

Hole für jede geplante Aussage den Text mit den kostenlosen Lookups (`get_erwaegung`, `get_regeste`, `get_decision`) und beurteile den Satz selbst:
- **`yes`**: Text stützt die Aussage vollständig → übernehmen.
- **`partial`**: Text stützt mit Qualifikator → Aussage präzisieren oder wörtlich zitieren.
- **`no` / `contradicts` / `unrelated`**: Aussage nicht gestützt → Beleg verwerfen!
- **Grundsatz**: Kein Beleg ohne wörtlichen Trägersatz. Ausgebaute Zitate gehören ausschliesslich in einen Abschnitt `## Entfernte Belege` am Ende der Datei.

---

## Step 5: Submit via GitHub Issue (Recommended)

Create an issue using the structured template:
**URL**: https://github.com/glossagens/glossagens/issues/new?template=anregung.yml

### Format for Practice-Oriented Commentary Submissions:
```markdown
**Gesetz**: StPO
**Artikel**: Art. 25
**Typ**: neuer_artikel (praxisorientiert)

**Gesetzeswortlaut** (aus Fedlex get_article):
> [Verbatim statute text]

**Prüfschema & Tatbestandsmerkmale**:
1. Sachliche Zuständigkeit (Abs. 1)
2. Örtliche Zuständigkeit (Abs. 2)
3. Vorbehalt besonderer Bundesgerichtsbarkeit

**Kasuistik & Lebenssachverhalte**:
- [BGE 144 IV 202 E. 2](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-144-IV-202_2018.html#consideration_2): [Konkreter Lebenssachverhalt mit Akteuren, Konflikt und Entscheidgründen]
- Gegenüberstellung angewandt vs. verworfen: [Beispiel A] vs. [Beispiel B]

**Kantonale Praxisfragen & Praxishinweise**:
- [Streitpunkt Obergericht ZH vs. BE]
- [Handlungsempfehlung für die Verteidigung / Verfahrensleitung]
```

---

## Step 6: Direct Pull Request (for complete Page Bundles)

If contributing ready-to-merge files, fork the repository and create a PR:

**Repository**: https://github.com/glossagens/glossagens  
**Branch**: `main`  
**Path**: `content/kommentar/{gesetz}/art-{nr}/`

### Page Bundle Structure:
```text
content/kommentar/{gesetz}/art-{nr}/
  ├── _index.md                    ← Hauptkommentar (Branch Bundle)
  ├── rechtsprechung.md            ← Rechtsprechungsübersicht (mind. 10 Entscheide)
  ├── strafzumessung.md            ← optional: Strafzumessung (nur Straftatbestände)
  └── strafzumessung-daten.json    ← optional: Ledger zur Strafzumessung
```

### Template: `_index.md` (Praxiskommentar)

```markdown
---
title: "Art. {nr} {Gesetz} — {Kurztitel}"
weight: {nr}
date: YYYY-MM-DD
lastmod: YYYY-MM-DD
description: "Praxiskommentar zu Art. {nr} {Gesetz} mit Prüfschema, Lebenssachverhalten und Abgrenzungskasuistik."
tags: ["{Gesetz}", "{Thema1}", "{Thema2}"]
agent_verified: true
revisions:
  - date: YYYY-MM-DD
    by: "Agent Name"
    model: "{Modell-ID}"
    mcp_verified: true
    note: "Praxisorientierte Erstkommentierung mit Prüfschema, Lebenssachverhalten und Grenzkasuistik."
---

## Gesetzeswortlaut

> 1 {Absatz 1 verbatim aus Fedlex get_article}
>
> 2 {Absatz 2 verbatim aus Fedlex get_article}

## I. Überblick und Bedeutung

{Systematische Einordnung, Regelungsgegenstand und Zweck der Norm.}

### Prüfschema

| Nr. | Tatbestandsmerkmal / Prüfungsschritt | Behauptungs- und Beweislast | Beweismass |
|---|---|---|---|
| 1 | {Merkmal 1} | {Partei} | {voller Beweis / Glaubhaftmachen} |
| 2 | {Merkmal 2} | {Partei} | {voller Beweis} |
| 3 | {Rechtsfolge / Ausnahme} | {Partei} | {voller Beweis} |

## II. Kommentierung

### A. {Tatbestandsmerkmal 1}

{1-3 Sätze abstrakte Dogmatik: Was das Merkmal verlangt.}

#### 1. Plastische Lebenssachverhalte aus der Praxis
{Ausführlicher Sachverhalt mit Akteuren, Konflikt, Daten und Entscheidgründen des Gerichts: [BGE 144 IV 202 E. 2](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-144-IV-202_2018.html#consideration_2)}

#### 2. Grenzkasuistik: Angewandt vs. Verworfen
- **Tatbestand bejaht**: {Sachverhalt, in dem das Gericht das Merkmal schützte: [Entscheid](URL)}
- **Tatbestand verneint**: {Sachverhalt, in dem die Anwendbarkeit verworfen wurde: [Entscheid](URL)}

| Sachverhalt / Konstellation | Beurteilung | Entscheid |
|---|---|---|
| {Konkrete Handlung A} | Merkmal bejaht | [BGE ...](URL) |
| {Konkrete Handlung B} | Merkmal verneint | [BGer ...](URL) |

> **Leitsatz.** {Nüchterne, beschreibende Verdichtung des Ergebnisses.}

### B. {Tatbestandsmerkmal 2}
{Analoger Aufbau wie oben.}

## III. Kantonale Praxisfragen

### {Praxisfrage / Divergenz}
{Konkreter Streitpunkt kantonaler Obergerichte mit Entscheidverweisen.}

## IV. Praxishinweise

**Für die Verteidigung / klagende Partei:**
1. {Handlungshinweis 1 mit Fundstelle} ([BGE ...](URL)).
2. {Handlungshinweis 2 mit Fundstelle} ([BGer ...](URL)).

**Für die Verfahrensleitung / Gerichte:**
1. {Verfahrensleitender Hinweis mit Fundstelle} ([OG ...](URL)).

## V. Literatur

- {Schweizer Standardkommentar, Werk, Auflage, Randnote / Seite}
```

### Template: `rechtsprechung.md`

```markdown
---
title: "Rechtsprechung zu Art. {nr} {Gesetz}"
weight: 99
date: YYYY-MM-DD
lastmod: YYYY-MM-DD
description: "Übersicht der Rechtsprechung zu Art. {nr} {Gesetz}."
tags: ["Rechtsprechung", "{Gesetz}", "{Thema1}"]
agent_verified: false
revisions:
  - date: YYYY-MM-DD
    by: "Agent Name"
    model: "{Modell-ID}"
    mcp_verified: true
    note: "Rechtsprechungsübersicht mit 10 verifizierten Entscheiden."
---

## I. Leitentscheide (BGE)

### **Thema des Leitentscheids**
[BGE 144 IV 202 E. 2](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-144-IV-202_2018.html#consideration_2)
Abstract mit Sachverhalt und Kernaussage.

---

## II. Weitere Entscheide

### **Thema des Entscheids**
[BGer 6B_1040/2019 vom 17.10.2019 E. 2.1](https://entscheidsuche.ch/docs/CH_BGer/CH_BGer_006_6B-1040-2019_2019-10-17.html)
Abstract mit Sachverhalt und Kernaussage.
```

---

## Anti-Halluzinations- und Formatierungsregeln (Verbindlich)

1. **Keine erfundenen Zitate**: Alle Fundstellen müssen über `cite` verifiziert sein.
2. **Gesetzeswortlaut aus Fedlex**: Immer authentischen Fedlex-Text via `get_article` einbinden.
3. **Reine Markdown-Tabellen**: Niemals Tabellen in ` ```markdown ` Codeblöcke packen.
4. **Verlinkung auf entscheidsuche.ch**: Links verbatim aus `document_url` der MCP-Antwort übernehmen. `#consideration_{E-Nr}` nur bei HTML-Dokumenten und vorhandener Erwägung.
5. **Keine Scheindubletten (BGE = BGer)**: BGE-Nummer und Geschäftsnummer desselben Entscheids nicht doppelt zitieren.
6. **Schweizer Rechtschreibung**: Durchgehend kein Eszett («ss»).

