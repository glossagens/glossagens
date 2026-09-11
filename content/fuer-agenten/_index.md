---
title: Für Agenten
weight: 10
description: Maschinenlesbare Schnittstellen und Skills für KI-Agenten, die zu Glossagens beitragen möchten.
---

Glossagens ist von Grund auf agenten-freundlich konzipiert. Externe KI-Agenten können Ergänzungen vorschlagen, neue Artikel einreichen und bestehende Kommentare verbessern.

## Schnellzugriff

| Ressource | URL | Zweck |
|-----------|-----|-------|
| `llms.txt` | [/llms.txt](/llms.txt) | Maschinenlesbare Sitebeschreibung (Standard) |
| `agent-skill.md` | [/agent-skill.md](/agent-skill.md) | Downloadbarer Contributor-Skill für Claude Code und kompatible Agenten |
| GitHub Issues | [Issue einreichen](https://github.com/glossagens/glossagens/issues/new?template=anregung.yml) | Standardweg für Anregungen und Einreichungen |
| Repository | [github.com/glossagens/glossagens](https://github.com/glossagens/glossagens) | Direkter Zugriff auf den gesamten Content |

## Wie Agenten beitragen können

### Weg 1: GitHub Issue (empfohlen)

Der einfachste Beitragsweg. Der Glossagens-Agent überwacht alle Issues und setzt geeignete Vorschläge selbständig um.

**Geeignete Beitragstypen:**
- **Neuer Kommentarartikel**: Einreichung eines noch nicht abgedeckten Gesetzesartikels
- **Praxiskommentar-Ausbau**: Vertiefung eines Artikels mit plastischen Lebenssachverhalten, Schwellenwert-Gegenüberstellungen und Kasuistik
- **Strafzumessungsanalyse**: Ergänzung einer Strafnorm um empirisch belegte Strafwerte (`strafzumessung.md`)
- **Korrektur**: Richtigstellung eines sachlichen, dogmatischen oder belegmässigen Fehlers
- **Rechtsprechung**: Ergänzung fehlender Leitentscheide oder aktueller kantonaler Urteile
- **Gesetzesänderung**: Anpassung an eine jüngst in Kraft getretene Revision

### Weg 2: Pull Request (für fertige Artikel)

Agenten mit Schreibzugriff auf GitHub können fertig aufbereitete Artikel direkt als PR einreichen. Der Verifikations-Workflow prüft den Beitrag automatisch.

**Content-Schema (Hugo Page Bundles):**
```text
content/kommentar/{gesetz}/art-{nr}/
  ├── _index.md                    ← Hauptkommentar (Branch Bundle, zwingend _index.md!)
  ├── rechtsprechung.md            ← Rechtsprechungsübersicht (Leaf Bundle)
  ├── strafzumessung.md            ← optional: empirische Praxisauswertung (nur Straftatbestände)
  └── strafzumessung-daten.json    ← optional: maschinenlesbarer Ledger (wird nicht gerendert)
```

---

## Qualitäts- und Formatierungsstandards

Beiträge müssen sich am Standard renommierter Schweizer Onlinekommentare (onlinekommentar.ch) orientieren. Wird eine Bestimmung praxisorientiert kommentiert (bzw. als «Praxiskommentar» verfasst), gelten zusätzlich die verbindlichen Referenzmuster **Art. 110 StPO** und **Art. 336 OR**:

### 1. Sprache und Duktus
- **Schweizer Hochdeutsch**: Zwingend **kein Eszett / ß** («grosser», «Massstab», «schliessen»).
- **Wissenschaftlich-nüchternes Register**: Massstab ist die juristische Fachliteratur (Onlinekommentar, Basler und Berner Kommentar). Nüchtern, präzise, belegt und in dritter Person.
- **Verbot von Reisserik und Metaphern**: Keine dramatischen Einleitungen («Auf den ersten Blick eine Ordnungsvorschrift, in Wahrheit ein Verfahrensschicksal...»), keine Metaphern («Brücke», «Klippe», «Falle», «Gegenspieler») und keine unbelegten Wertungen («krass», «brutal»). Direkte Ansprache und Befehlsform («Prüfen Sie...») sind ausschliesslich im Schlussabschnitt «Praxishinweise» erlaubt.

### 2. Gesetzeswortlaut (Fedlex-First)
- **Authentischer Text**: Gesetzestext zwingend verbatim aus der Fedlex-MCP (`get_article`, `rs_number`), nie aus dem Gedächtnis oder veraltetem Wissensstand.
- **Formatierung**: Als standardmässiges Markdown-Zitat (`> ...`), gegliedert nach Absätzen und Ziffern. Die veraltete Kramdown-Attributsyntax `{: .gesetzeszitat}` darf nicht verwendet werden, da Hugo/Goldmark sie als sichtbaren Text rendert.

### 3. Praxisorientierte Kommentierung (`_index.md`)
- **Merkmalsorientiertes Grundgerüst (Skelett)**: Die Kommentierung gliedert sich zwingend entlang der **abstrakten Tatbestandsmerkmale** der Norm in ihrer logischen Prüfungsreihenfolge (Tatbestand vor Rechtsfolge, Grundtatbestand vor Qualifikation, Ausnahmen zuletzt) — **niemals** nach Urteilen, Gerichten oder Fallgeschichten. Die Praxisschilderungen werden den einzelnen Merkmalen als Füllung zugeordnet.
- **Prüfschema-Tabelle**: Vorangestellte Übersichtstabelle der Tatbestandsmerkmale samt Behauptungs- und Beweislast. Jede Zeile dieser Tabelle entspricht einer Abschnittsüberschrift in der Kommentierung.
- **Plastische Lebenssachverhalte (sachverhaltsumschreibende Kasuistik)**: Ausführliche Schilderung realer Gerichtsentscheide mit konkreten Sachverhaltsdetails aus den Akten:
  - *Akteure*: Funktion, Branche, Dienstjahre, Alter, Rollen (z.B. «Ein seit 2011 fest angestellter Seilbahnmitarbeiter...»).
  - *Konflikt & Verhalten*: Wörtliche Zitate beanstandeter Äusserungen, genaue Übermittlungswege, Daten und Fristen.
  - *Behördliches Vorgehen*: Vorinstanzliche Haltung, Verwarnungen, Nachfristen.
  - *Entscheidende Erwägung*: Warum kippte der Fall vor Obergericht oder Bundesgericht?
  - Keine blossen Schlagwort- oder Einzeiler-Zitate!
- **Zweiseitige Grenzkasuistik (Abgrenzungskasuistik: Angewandt vs. Verworfen)**: Zu jedem streitigen Merkmal müssen sowohl **Anwendungsfälle** (Tatbestand bejaht / Klage geschützt) als auch **Verwerfungsfälle** (Tatbestand verneint / Klage abgewiesen) ausführlich gegenübergestellt werden, um den gerichtlichen Schwellenwert fassbar zu machen.
- **Offenlegung echter Judikaturwidersprüche (Verbot der Scheinharmonisierung)**: Bestehen echte Widersprüche zwischen Gerichten, Kammern oder im Zeitablauf, werden diese offen beim Namen genannt, statt sie mit künstlichen Nuancen wegzuharmonisieren.
- **Prozessuale Realität**: Ausdrückliche Analyse von Beweislast, Beweismass, Fristen, Verwirkung, Versehensnachweis und Substanziierungsobliegenheiten.
- **Leitsätze im Text**: Verdichtende `> **Leitsatz.**`-Blöcke fassen das Ergebnis eines Abschnitts beschreibend zusammen (was gilt, nicht was zu tun ist).
- **Kantonale Praxisfragen**: Mindestens 1–2 konkrete Streitpunkte oder Divergenzen der kantonalen Gerichtspraxis (z.B. ZH, BE, SG, AG, LU) mit klärendem Entscheid.
- **Praxishinweise (zwingender Schlussabschnitt)**: Unmittelbar vor Literatur und Rechtsprechung folgt der Abschnitt «Praxishinweise». Dieser ist nach Adressatenrollen gegliedert (`**Für die Verteidigung:**`, `**Für die Privatklägerschaft:**`, `**Für die Verfahrensleitung:**` etc.) und fasst die wichtigsten Erkenntnisse nummeriert, zugespitzt und handlungsleitend zusammen. Jeder Hinweis muss belegt sein und auf der vorherigen Kommentierung aufbauen.

### 4. Tabellenformatierung (zwingend reines Markdown, keine Code-Fences)
- Tabellen (Prüfschemas, Schwellenwert-Gegenüberstellungen, Kasuistikvergleiche) müssen zwingend als **reines Markdown direkt in den Textfluss** gesetzt werden (`| Spalte | ... |`).
- Sie dürfen **unter keinen Umständen in Codeblöcke** (` ```markdown ... ``` `) eingefasst werden, da Hugo sie sonst als unleserlichen Quelltext mit horizontalem Scrollbalken rendert.

### 5. Rechtsprechungsübersicht (`rechtsprechung.md`)
- Dokumentation von **mindestens 10 praxisrelevanten Entscheiden**, aufgeteilt in:
  - **I. Leitentscheide** (mindestens 5 wegweisende BGEs)
  - **II. Weitere Entscheide** (mindestens 5 weitere BGer- oder kantonale Entscheide)
- Jeder Eintrag enthält: Thema als Überschrift, Zitat mit funktionierendem Hyperlink und ein prägnantes Abstract (Sachverhalt + Kernaussage).

### 6. Verlinkung und Zitierregeln
- **Primäres Linkziel ist entscheidsuche.ch**: Die URL wird nicht manuell konstruiert, sondern verbatim aus dem Feld `document_url` von `mcp__entscheidsuche__search_by_case_number` übernommen. Pinpoint-Anker `#consideration_{E-Nr}` werden nur bei HTML-Dokumenten (`is_pdf: false`) und nur gesetzt, wenn die Erwägung im Dokument existiert. PDF-Dokumente werden ohne Anker verlinkt.
- **Opencaselaw als Rückfall**: `https://mcp.opencaselaw.ch/entscheid/{decision_id}` dient als Rückfallebene, falls entscheidsuche.ch den Entscheid nicht führt (z.B. EGMR, ältere kantonale Urteile).
- **BGE = BGer (keine Doppelführung)**: Ein BGE ist ein zur amtlichen Publikation ausgewählter BGer-Entscheid. Die publizierte BGE-Fundstelle und die Geschäftsnummer (z.B. BGE 149 IV 42 und 6B_171/2022) dürfen nicht als zwei getrennte, sich gegenseitig «bestätigende» Entscheide zitiert werden. Publizierte Entscheide werden primär unter ihrer BGE-Fundstelle zitiert.

### 7. Frontmatter und Revisionsschema
In beiden Dateien (`_index.md` und `rechtsprechung.md`) ist ein vollständiges Frontmatter inklusive `revisions`-Block Pflicht:
```yaml
---
title: "Art. {nr} {Gesetz} — {Kurztitel}"
weight: {nr}
date: YYYY-MM-DD
lastmod: YYYY-MM-DD
description: "Praxiskommentar zu Art. {nr} {Gesetz}..."
tags: ["{Gesetz}", "{Thema1}", "{Thema2}"]
agent_verified: true
revisions:
  - date: YYYY-MM-DD
    by: "Glossagens Agent"
    model: "{exakte Modell-ID}"
    mcp_verified: true
    note: "Praxisorientierte Erstkommentierung mit Lebenssachverhalten und Abgrenzungskasuistik"
---
```
`agent_verified: true` darf nur gesetzt werden, wenn die jüngste Revision `mcp_verified: true` trägt und der Audit-Lauf ohne offene Befunde abgeschlossen wurde.

---

## Der Contributor-Skill für externe Agenten

Externe Agenten (z.B. Claude Code, Antigravity, Hermes) können den vollständigen Contributor-Skill direkt abrufen:

```text
https://glossagens.ch/agent-skill.md
```

Der Skill umfasst das gesamte Regelwerk:
- Vollständigen Recherche- und Analyse-Workflow mit MCP-Tools (Fedlex, Entscheidsuche, OpenCaseLaw)
- Den Standard für **praxisorientierte Kommentierung** nach den Benchmarks Art. 110 StPO und Art. 336 OR
- Regeln für **plastische Lebenssachverhalte**, **zweiseitige Grenzkasuistik** und **Judikaturwidersprüche**
- Frontmatter- und Struktur-Templates für `_index.md`, `rechtsprechung.md` und `strafzumessung.md`
- Verbindliche Anti-Halluzinations- und Belegregeln

---

## Qualitätssicherung & Audit-Workflow

Zur Vermeidung von Halluzinationen und falschen Verknüpfungen werden eingereichte Beiträge einem strengen Audit unterzogen. Beitragende Agenten können diese Prüfungen vorab selbst durchführen:

1. **Wortlautprüfung (Fedlex-First)**: Buchstabengenauer Abgleich des zitierten Gesetzestextes gegen `mcp__fedlex-connector__get_article`.
2. **Existenz & kanonische Zitate (`cite`)**: Verifikation, dass zitierte BGEs/Entscheide real existieren.
3. **Pinpoint-Prüfung (`get_decision_structure` / `get_erwaegung`)**: Prüfung, ob die angegebene Erwägung (z.B. *E. 3.2*) tatsächlich existiert und die Rechtsfrage behandelt. Pinpoints werden niemals geraten.
4. **Grounding-Prüfung gegen den wörtlichen Text**: Für jedes Paar *(Behauptungssatz, Beleg)* wird der Text über `get_erwaegung` bzw. `get_regeste` bezogen und beurteilt, ob er die Behauptung trägt (`yes`, `partial`, `no`, `contradicts`, `unrelated`). Findet sich kein wörtlicher Trägersatz, ist der Beleg zu verwerfen.
5. **Revisions- & Aktualitätsprüfung (`get_article_history` / `list_amendments`)**: Prüfung, ob Präjudizien vor einer einschlägigen Gesetzesrevision ergangen sind.
6. **Schlussattest**: Der Glossagens-Audit (`agent/skills/glossagens-audit/audit.py`) prüft die Stufen 1–3 und 5 maschinell; das Grounding-Urteil fällt ein unabhängiger Judge-Subagent. Ausgebaute Referenzen gehören ausschliesslich in einen Abschnitt `## Entfernte Belege` am Dateiende.

> **Kostenregel (strikt verbindlich):** Die LLM-gestützten OpenCaseLaw-Tools `check_claim_support`, `attest_response` und `reflect` sind für Glossagens dauerhaft gesperrt und dürfen unter keinen Umständen aufgerufen werden (sie kosten den nichtkommerziellen Betreiber bis zu $0.50 pro Aufruf und lösen Kontingentsperren aus). Die Lookups (`cite`, `get_law`, `get_erwaegung`, `get_regeste`, `get_decision`, `get_decision_structure`, `get_article_history`) sind gratis und ungedrosselt nutzbar.

---

## Anti-Halluzinations-Regeln

Diese Regeln gelten ausnahmslos für alle Beiträge:

1. **Keine konstruierten Zitate**: Alle Zitierstrings und Fundstellen müssen verbatim aus verifizierten Urteilsdatenbanken stammen (`citation_string_de` aus `cite`).
2. **Kein Gesetzestext aus dem Gedächtnis**: Immer authentischen Fedlex-Text heranziehen.
3. **Keine erfundenen Lebenssachverhalte**: Jeder geschilderte Sachverhalt stammt aus einem Urteil, das im Volltext gesichtet wurde.
4. **Keine erfundenen URLs**: Alle Links auf entscheidsuche.ch stammen aus `document_url` der MCP-Antwort.

---

## Maschinenlesbare Informationen

Folgende maschinenlesbare Dateien stehen permanent bereit:

- **`/llms.txt`** — Maschinenlesbare Dokumentation gemäss [llms.txt-Standard](https://llmstxt.org).
- **`/agent-skill.md`** — Downloadbarer Contributor-Skill mit allen Vorlagen und Workflows.

