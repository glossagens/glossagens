---
name: glossagens-content-creation
description: >-
  Create and maintain legal commentary articles for the Glossagens Hugo site, with built-in grounding checks (judge the claim against the verbatim Erwägung before writing, run the audit harness before commit). No LLM-backed opencaselaw tool is ever called — only free lookups. Offers three workflows: /kommentar (full creation), /recherche (research only), /loop (iterative gap analysis with subagents).
version: 5.0.0
author: Hermes Agent
tools:
  - mcp__fedlex-connector__get_article
  - mcp__fedlex-connector__get_law_text
  - mcp__fedlex-connector__search_by_title
  - mcp__fedlex-connector__list_amendments
  - mcp__entscheidsuche__search_by_case_number
  - mcp__entscheidsuche__search
  - mcp__entscheidsuche__fetch_document
  - mcp_opencaselaw_cite
  - mcp_opencaselaw_get_law
  - mcp_opencaselaw_get_legislation
  - mcp_opencaselaw_get_doctrine
  - mcp_opencaselaw_get_commentary
  - mcp_opencaselaw_search_decisions
  - mcp_opencaselaw_find_leading_cases
  - mcp_opencaselaw_find_citations
  - mcp_opencaselaw_get_case_brief
  - mcp_opencaselaw_get_decision
  - mcp_opencaselaw_get_decision_structure
  - mcp_opencaselaw_get_erwaegung
  - mcp_opencaselaw_get_regeste
  - mcp_opencaselaw_list_courts
  - mcp_opencaselaw_get_article_purpose
  - mcp_opencaselaw_get_article_history
  - mcp_opencaselaw_search_botschaft
  - mcp_opencaselaw_get_materialien
  - mcp_opencaselaw_search_materialien
  - write_file
  - terminal
  - agent
---

# Glossagens Content Creation

Create and maintain legal commentary articles for the Glossagens Hugo site at `/opt/glossagens/`.

Articles are stored as **Hugo Page Bundles** — each article gets its own directory:
- `content/kommentar/{gesetz}/art-{NNN}/_index.md` — commentary
- `content/kommentar/{gesetz}/art-{NNN}/rechtsprechung.md` — case law overview

---

# TEIL A — WORKFLOWS

Three independent workflows. Each can be called directly.

---

## Workflow 1: `/kommentar {GESETZ} Art. {N}` — Vollworkflow

Create a new commentary from scratch or comprehensively update an existing one.

**Steps:**
1. INIT (→ Teil B, Abschnitt 1)
2. GESETZESTEXT abrufen und als Daten ablegen: `python3 scripts/wortlaut.py content/kommentar/{gesetz}/art-{NNN}` (→ Teil B, Abschnitt 2)
3. GESETZGEBERISCHE IDEEN & ZWECKE ERMITTELN — Materialien zur Schaffung und zu allfälligen Revisionen via `get_article_purpose`, `get_article_history`, `get_materialien` analysieren (→ Teil B, Abschnitt 2b)
4. RECHERCHE — parallele Subagenten-Recherche nach Rechtsprechung, Materialien und Lehre (→ Teil B, Abschnitt 3)
5. RECHTSPRECHUNGSDATEI aktualisieren (→ Teil B, Abschnitt 4)
6. **BELEGPRÜFUNG vor dem Schreiben** — jedes Paar (Aussage, Beleg) gegen den wörtlichen Entscheidtext bzw. die Botschaft (→ Teil D.1)
7. KOMMENTAR schreiben/ergänzen (→ Teil C) — inklusive Entstehungsgeschichte, Ratio Legis und Revisionsmotiven
8. **SCHLUSSATTEST** — Audit-Lauf über das fertige Bundle (→ Teil D.3)
9. QUALITÄTSKONTROLLE — Checklisten (→ Teil D.4)
10. HUGO BUILD + COMMIT (→ Teil B, Abschnitt 5)

> Schritt 6 und 8 sind **nicht optional**. Was davon erledigt ist, hält die `note` der Revision fest (→ Teil D.5).

---

## Workflow 2: `/recherche {GESETZ} Art. {N}` — Nur Recherche

Find new decisions and sources and store them in `rechtsprechung.md` — without changing the commentary.

**Steps:**
1. INIT (→ Teil B, Abschnitt 1)
2. RECHERCHE (→ Teil B, Abschnitt 3)
3. **BELEGPRÜFUNG** der Kernaussagen jedes neuen Entscheids (→ Teil D.1) — auch die
   Rechtsprechungsübersicht behauptet etwas über den Entscheid
4. RECHTSPRECHUNGSDATEI aktualisieren (→ Teil B, Abschnitt 4)
5. Zusammenfassung der neuen Funde, kein Kommentareingriff

---

## Workflow 3: `/anreicherung {GESETZ} Art. {N}` — Iterative Lückenanalyse

Continuously research which topics and decisions are still **missing** from the existing commentary and integrate them step by step. Runs until no relevant gaps remain or the user stops.

**Each iteration:**

```
┌───────────────────────────────────────────────────────┐
│  LOOP-ITERATION N                                     │
│                                                       │
│  1. BESTANDSAUFNAHME                                  │
│     Lies _index.md und rechtsprechung.md               │
│     Inventar:                                         │
│     - Welche Themen/Absätze sind kommentiert?         │
│     - Welche Entscheide bereits zitiert?              │
│     - Welche Annotationen/Abgrenzungen fehlen?        │
│                                                       │
│  2. LÜCKENANALYSE                                     │
│     Protokoll:                                        │
│     - Absätze ohne Rechtsprechung                     │
│     - Gesetzgeberische Ideen/Zwecke eingearbeitet?   │
│     - Revisionsmotive (falls geändert) dokumentiert?  │
│     - Fehlende Kasuistik zu Kerntatbeständen          │
│     - Konventionsrechtliche Aspekte (EMRK/EGMR)?      │
│     - Gesetzesmaterialien eingearbeitet?              │
│     - Neuere Entscheide (nach letzter Aktualisierung)?│
│     - Was tragen verwandte Themen, das hier fehlt?    │
│       (→ Teil B, Abs. 1 Ziff. 5)                      │
│                                                       │
│  3. PRIORISIERUNG                                     │
│     (a) Fehlende BGer-Leitentscheide (höchste Prio)  │
│     (b) Gesetzgeberischer Zweck / Revisionsmotive     │
│     (c) Unkommentierte Absätze                        │
│     (d) Fehlende Kasuistik                            │
│     (e) EMRK/Konventionsrecht                         │
│     (f) Materialien und Lehre                         │
│     → Top 1–3 Lücken für diese Runde auswählen        │
│                                                       │
│  4. GEZIELTE SUBAGENTEN-RECHERCHE                     │
│     Parallele Subagenten für die gewählten Lücken     │
│     (→ Subagenten-Vorlagen in Teil B, Abs. 3)         │
│     Jeder Subagent erhält die BEKANNTE_ENTSCHEIDE     │
│     Liste zur Duplikationsvermeidung.                 │
│                                                       │
│  5. BELEGPRÜFUNG (Teil D.1)                           │
│     Für JEDEN neuen Entscheid, den die Subagenten     │
│     melden: Urteil gegen den wörtlichen Text der      │
│     Erwägung/Regeste VOR der Integration.             │
│     yes/partial → übernehmen (partial: abschwächen)   │
│     no/contradicts/unrelated → verwerfen, nicht       │
│     «thematisch passend» weiterreichen.               │
│                                                       │
│  6. INTEGRATION                                       │
│     - Geprüfte Entscheide → rechtsprechung.md         │
│     - Kommentar ergänzen: neue Abschnitte, Kasuistik  │
│                                                       │
│  7. SCHLUSSATTEST (Teil D.3)                          │
│     audit.py über das Bundle; offene Paare durch      │
│     Judge-Subagenten beurteilen lassen.               │
│     Befunde offen → zurück zu Schritt 5.              │
│                                                       │
│  8. FORTSCHRITTSBERICHT                               │
│     - Welche Lücken bearbeitet?                       │
│     - Welche neuen Entscheide integriert?             │
│     - Wie viele Belege in Schritt 5 verworfen?        │
│     - Welche Lücken verbleiben?                       │
│     - Empfehlung: weitermachen oder beenden?          │
│                                                       │
│  9. KONTEXTMANAGEMENT                                 │
│     Bei vollem Kontext → /compact, dann fortfahren    │
│                                                       │
└──────────── Wiederholen bis ──────────────────────────┘
   (a) Benutzer abbricht, oder
   (b) Keine relevanten Lücken mehr gefunden, oder
   (c) Keine neuen Entscheide mehr auffindbar
```

**Loop-Abschlussbericht:**
- Total Iterationen
- Neu integrierte Entscheide (BGE / BGer / kantonal / EGMR)
- In der Belegprüfung verworfene Entscheide (mit Grund)
- Attest-Status der letzten Iteration
- Verbleibende offene Fragen

---

# TEIL B — BASISOPERATIONEN

---

## 1. INIT — Kontext klären

1. **Artikel und Gesetz** aus Benutzeranweisung extrahieren. Bei Mehrdeutigkeit nachfragen.

2. **Pfade ableiten:**
   - Ordner:               `/opt/glossagens/content/kommentar/{gesetz}/art-{NNN}/`
   - Kommentardatei:       `_index.md`
   - Rechtsprechungsdatei: `rechtsprechung.md`

3. **Bestandsaufnahme:**
   - Prüfe: Existiert `content/kommentar/{gesetz}/_index.md` (Gesetzesübersicht)?
   - Falls NEIN: Vor dem ersten Artikel anlegen (siehe Teil C.5)
   - Falls JA: Ordner scannen. Bestehende `.md`-Dateien lesen.

4. **BEKANNTE_ENTSCHEIDE-Inventar** erstellen (für Duplikationsvermeidung):
   Alle Urteilsreferenzen aus `_index.md` und `rechtsprechung.md` extrahieren:
   ```
   BEKANNTE_ENTSCHEIDE = [
     "BGE 144 IV 202",
     "BGer, 6B_1040/2019 v. 3.8.2020",
     ...
   ]
   ```

5. **Verwandte Themen** als zusätzliche Quelle (`content/themen/`, siehe `CLAUDE.md` «Themen»):
   ```bash
   grep -l "gesetz: {gesetz}, art: art-{NNN} }" content/themen/*/_index.md      # Themen, die den Artikel in normen führen
   # live: https://glossagens.ch/themen/index.json → normen["{gesetz}/art-{NNN}"].themen
   ```
   Auch Themen desselben Sachgebiets (`data/sachgebiete/zuordnung.yaml`) durchsehen. Ein Thema
   liefert systematische Stellung, Abgrenzungen zu Nachbarnormen, Leitformeln und Leitentscheide;
   was es trägt, der Kommentar aber nicht, ist eine Lücke und gehört ins BEKANNTE_ENTSCHEIDE-Inventar.
   - **Kein Beleg**: Das Thema ist Sekundärquelle der Plattform selbst. Übernommene Entscheide und
     Pinpoints durchlaufen die Belegprüfung (Teil D.1) wie jeder andere und werden direkt auf den
     Entscheid verlinkt. Das Thema ist nicht geprüft — es liefert Hinweise, keine Belege.
   - **Nicht doppeln**: Den übergreifenden Zusammenhang in einem Satz verdichten und auf den
     Abschnittsanker verweisen (`/themen/{slug}/#{anker}`); «In Themen behandelt» setzt das Layout selbst.
   - **Widerspruch**: Erweist sich ein Thema als falsch oder überholt, nicht stillschweigend
     abweichen — das Thema mit eigenem Revisionseintrag korrigieren oder den Befund melden.
   Diese Liste jedem Subagenten mitgeben.

---

## 2. GESETZESTEXT — Wortlaut abrufen

> **Quelle: Fedlex zuerst.** Der Normtext kommt aus der Fedlex-MCP —
> `mcp__fedlex-connector__get_article` (`rs_number`, `article`; `date` für einen
> historischen Stand), `get_law_text` für ganze Erlasse, `search_by_title` wenn die
> SR-Nummer unklar ist. `get_law` der opencaselaw-MCP ist **nur Rückfallebene**: bei
> kantonalem Recht (Fedlex führt nur Bundesrecht) oder wenn Fedlex die Norm nicht
> liefert. Grund: opencaselaw sperrt den Glossagens-Client seit dem 23.08.2026 per IP
> (HTTP 403); Fedlex war nie betroffen. Wird der Rückfall benutzt, im Revisionsvermerk
> festhalten. Für **Entscheide** bleibt opencaselaw bzw. entscheidsuche massgebend.
> **Linkziel für Entscheide ist entscheidsuche.ch** (siehe D.2a), opencaselaw nur als Rückfall.

```
mcp__fedlex-connector__get_article: { "rs_number": "{SRNR}", "article": "{N}", "language": "de" }
```

Ganzer Erlass bzw. SR-Nummer unbekannt:
```
mcp__fedlex-connector__get_law_text:   { "rs_number": "{SRNR}" }
mcp__fedlex-connector__search_by_title: { "query": "{Gesetzestitel}" }
```

Rückfall (nur kantonales Recht oder wenn Fedlex nichts liefert):
```
mcp_opencaselaw_get_law: { "abbreviation": "{ABBREV}", "article": "Art. {N}", "language": "de" }
mcp_opencaselaw_get_legislation: { "query": "Art. {N} {ABBREV} SR {SRNR}" }
```

Vollständigen Wortlaut aller Absätze und Buchstaben verwenden.

**Darstellung im Bundle — nur per Shortcode.** Die MCP-Abfrage dient dem Lesen und der
Recherche. In den Artikel kommt der Normtext **nicht** als Blockquote, sondern so:

```bash
python3 scripts/wortlaut.py content/kommentar/{gesetz}/art-{NNN}
# → data/wortlaut/{gesetz}/art-{NNN}.json (mit committen)
```

```markdown
## Gesetzeswortlaut

{{< wortlaut >}}
```

Das Skript holt den Text aus dem HTML der geltenden Fedlex-Konsolidierung (kantonal: aus
der LexWork-Sammlung, derzeit Luzern) und übernimmt Absätze, Litterae und Fussnoten
unverändert; der Shortcode setzt ihn im Satzbild von Fedlex mit Stand und Quellenlink.
Keine eigene Quellen- oder Standzeile darunter. Eine Bezugsnorm, die zum Verständnis
mitgelesen werden muss: `{{< wortlaut gesetz="{gesetz}" art="art-{NNN}" >}}` (Daten
ebenfalls mit dem Skript holen). Fehlt die Daten-Datei, bricht der Hugo-Build ab —
gewollt, damit kein leerer Wortlaut-Abschnitt live geht.

---

## 2b. GESETZGEBERISCHE IDEEN UND ZWECKE (Materialien zur Schaffung und Änderung)

> **Zwingende Ermittlung von Ratio Legis und Entstehungsgeschichte:**
> Eine seriöse Kommentierung beruht auf der methodenpluralistischen Auslegung. Die Entstehungsgeschichte (historische Auslegung) und der Normzweck (teleologische Auslegung) bilden das Fundament, auf dem die Rechtsprechung aufbaut und an dem sich Tatbestandsmerkmale sowie deren Grenzziehungen messen lassen.
> 
> Vor dem Abfassen des Kommentars ist deshalb stets zu überprüfen:
> 1. **Idee und Zweck bei der Schaffung**: Welcher gesetzgeberische Zweck und welche Motive lagen dem Erlass der Norm zugrunde? Welche Missstände, Schutzbedürfnisse oder Rechtsunsicherheiten wollte das Parlament beseitigen?
> 2. **Revisionsgründe bei Gesetzesänderungen**: Wurde der Artikel seit Inkrafttreten revidiert? Welche praktischen Probleme, veränderten gesellschaftlichen Realitäten oder Urteile führten zur Gesetzesänderung, und welche Absicht verfolgte der Gesetzgeber mit der Neuformulierung?

### Werkzeuge in opencaselaw:

1. **`get_article_purpose` (Primärwerkzeug für Botschafts-Volltext):**
   Liefert die wörtlichen Erwägungen des Bundesrates (aus der Botschaft oder Erläuterungsberichten) zum Zweck des konkreten Artikels — sowohl für den ursprünglichen Erlass als auch für spätere Revisionsbotschaften. Enthält exakte Fundstellen (`bbl_citation, S. {page}`) für das Verbatim-Zitieren.
   ```
   mcp_opencaselaw_get_article_purpose: { "sr_number": "{SRNR}", "article": "{N}", "language": "de" }
   ```

2. **`get_article_history` (Entwicklungsbogen und Revisionen):**
   Gibt die chronologische Geschichte der Bestimmung zurück: aktueller Gesetzestext + jede verknüpfte Botschaft (Erlass und alle Änderungen) + Leitentscheide + Lehrmeinungen in zeitlicher Abfolge.
   ```
   mcp_opencaselaw_get_article_history: { "sr_number": "{SRNR}", "article": "{N}", "language": "de" }
   ```

3. **`get_materialien` (Materialien-Übersicht & Vernehmlassungen):**
   Liefert per-Artikel-Intent-Digests (BV und BGFA), verknüpfte Bundesblatt-Dokumente (`botschaft_documents` mit BBl-Nummer und Fedlex-Link), Vernehmlassungen (`vernehmlassungen`) und Fussnoten-Referenzen (`amendment_refs`).
   ```
   mcp_opencaselaw_get_materialien: { "law_code": "{ABBREV}", "article": "{N}" }
   ```

4. **`search_botschaft` (Volltextsuche in Materialien):**
   Volltextsuche über Botschaften, Berichte und Vernehmlassungsdokumente bei speziellen Begriffen oder Kontroversen im Gesetzgebungsverfahren:
   ```
   mcp_opencaselaw_search_botschaft: { "query": "Art. {N} {ABBREV} Zweck" }
   ```

> **Regel R4 — Spekulationsverbot über den Gesetzeszweck:**
> Niemals über den Willen des Gesetzgebers oder die Teleologie spekulieren («die Bestimmung dürfte bezwecken...»). Der gesetzgeberische Wille ist zwingend anhand der authentischen Materialien (Botschaften) nachzuweisen und mit BBl-Fundstelle zu belegen. Direkte Zitate müssen aus `get_article_purpose` oder `search_botschaft` stammen.

---

## 3. RECHERCHE — Subagenten für Rechtsprechung und Materialien

Starte parallele Subagenten (Agent-Tool) für alle drei Vorlage-Typen gleichzeitig.

### Subagent-Vorlage A: Bundesgerichtsentscheide

> **Aufgabe**: Recherchiere Bundesgerichtsentscheide zu Art. {N} {ABBREV}.
>
> **Kontext**: [Spezifische Lücke / Teilfrage, oder «alle Aspekte von Art. {N} {ABBREV}»]
>
> **Bereits bekannte Entscheide** (nicht nochmals melden):
> [BEKANNTE_ENTSCHEIDE-Liste einfügen]
>
> **MCP-Calls** (in dieser Reihenfolge):
> 1. `find_leading_cases` mit query "Art. {N} {ABBREV}"
> 2. `find_citations` mit article "Art. {N} {ABBREV}"
> 3. `search_decisions` mit query "Art. {N} {ABBREV} [THEMA]"
> 4. Für vielversprechende Treffer: `get_case_brief` oder `get_regeste`
>
> **Ausgabeformat** (je Entscheid):
> ```
> URTEIL: {citation_string_de}
> DECISION_ID: {decision_id aus dem Tool-Ergebnis}
> PINPOINT: {E. X.Y — nur wenn durch get_erwaegung belegt, sonst «—»}
> THEMA: [2–3 Worte]
> KERNAUSSAGE: [2–4 Sätze]
> EINSCHLÄGIG FÜR: [Absatz/Tatbestandsmerkmal]
> BELEGPRÜFUNG: {dein Urteil: yes | partial} ({Konfidenz 0–1})
> BELEGSTELLE: {wörtlicher Satz aus der geholten Erwägung/Regeste, der die KERNAUSSAGE trägt}
> STATUS: NEU
> ```
>
> **Pflicht vor der Meldung** (→ Teil D.1): Hole den Text, gegen den du urteilst —
> `get_erwaegung` für die Erwägung, sonst `get_regeste` —, und beurteile deine
> KERNAUSSAGE gegen **diesen Text**, nicht gegen deine Erinnerung an den Entscheid.
> Melde nur `yes` und `partial`. `no` / `contradicts` / `unrelated` werden **nicht**
> gemeldet — auch nicht mit dem Hinweis «thematisch verwandt». Bei `partial` die
> Kernaussage so umformulieren, dass der Qualifikator des Gerichts drinsteht
> (wörtlich zitieren macht aus `partial` meist ein `yes`).
> **Ohne BELEGSTELLE keine Meldung**: Findest du im geholten Text keinen Satz, der
> die Kernaussage trägt, ist der Entscheid kein Beleg.
> **Pinpoint nie raten**: `get_decision_structure` listet die vorhandenen
> Erwägungsnummern, `get_erwaegung` bestätigt sie; sonst gar keinen Pinpoint angeben.
>
> Maximal 15 Ergebnisse. Nur Entscheide melden, die NICHT in der Bekannten-Liste stehen.
> WICHTIG: citation_string_de aus dem Tool-Ergebnis verwenden — nie selbst konstruieren.
> VERLINKUNG: Rechtsquellen (Entscheide, Gesetze) müssen zwingend auf die Originalquelle verlinkt werden (Markdown-Link: [Zitat](URL)), sofern das Tool eine URL liefert.

### Subagent-Vorlage B: Kantonale Rechtsprechung und EGMR

> **Aufgabe**: Suche kantonale Urteile und EGMR-Entscheide zu Art. {N} {ABBREV}.
>
> **Kontext**: [Spezifische Lücke / Teilfrage]
>
> **Bereits bekannte Entscheide**: [BEKANNTE_ENTSCHEIDE-Liste]
>
> **Suchstrategie:**
> 1. `search_decisions` mit query "Art. {N} {ABBREV}" (ohne court-Filter oder mit verschiedenen Kantonsgerichten)
> 2. `list_courts` um verfügbare kantonale Gerichte zu identifizieren
> 3. Für EMRK-Bezug: `search_decisions` mit query "Art. {N} {ABBREV} EMRK"
>
> **Besonders wertvoll**: Kantonale Entscheide, die von BGer-Praxis abweichen oder noch nicht höchstrichterlich entschiedene Aspekte behandeln.
>
> **Ausgabeformat** (je Entscheid):
> ```
> URTEIL: {citation_string_de}
> DECISION_ID: {decision_id aus dem Tool-Ergebnis}
> GERICHT/KANTON: [Gericht, Kanton]
> THEMA: [2–3 Worte]
> KERNAUSSAGE: [2–4 Sätze]
> BELEGPRÜFUNG: {dein Urteil: yes | partial} ({Konfidenz 0–1})
> BELEGSTELLE: {wörtlicher Satz aus dem geholten Text}
> STATUS: NEU
> ```
>
> **Pflicht vor der Meldung** (→ Teil D.1): Text über `get_regeste` bzw.
> `get_decision` holen und die KERNAUSSAGE gegen diesen Text beurteilen — nur
> `yes` / `partial` melden, und nie ohne wörtliche BELEGSTELLE. Kantonale
> Entscheide haben keine strukturierten Erwägungen; dort ohne Pinpoint arbeiten
> und im Kommentar keinen setzen.
>
> VERLINKUNG: Alle Entscheide und Gesetze müssen auf die Originalquelle verlinkt werden (Markdown-Link), sofern möglich.

### Subagent-Vorlage C: Materialien, gesetzgeberischer Zweck und Lehre

> **Aufgabe**: Eruiere die gesetzgeberischen Ideen, Zwecke und Motive bei der Schaffung von Art. {N} {ABBREV} sowie bei allfälligen späteren Gesetzesänderungen anhand der amtlichen Gesetzesmaterialien. Recherchiere zudem (soweit für Kontroversen relevant) das Schrifttum.
>
> **Gesetzgeberischer Zweck & Materialien** (immer zwingend durchführen):
> 1. `get_article_purpose` mit sr_number="{SRNR}", article="{N}":
>    Wörtliche Botschaftserwägungen zu Normzweck und Absichten des Bundesrates (Erlass + Revisionen) abrufen.
> 2. `get_article_history` mit sr_number="{SRNR}", article="{N}":
>    Chronologischen Revisionsbogen und verknüpfte Botschaften prüfen.
> 3. `get_materialien` mit law_code="{ABBREV}", article="{N}":
>    Fundstellen (BBl-Dokumente, Vernehmlassungen, Fussnoten) erfassen.
> 4. `search_botschaft` mit query="Art. {N} {ABBREV}":
>    Für gezielte Detailfragen oder Beratungsdiskussionen im Parlament.
>
> **Lehre** (nur recherchieren wenn keine Rspr. existiert oder eine Kontroverse aufzubereiten ist):
> - `get_commentary` mit abbreviation="{ABBREV}", article="{N}"
> - `get_doctrine` mit query="Art. {N} {ABBREV}"
>
> **Ausgabeformat:**
> ```
> QUELLE: [Botschaft BBl ... / Kommentar-Autor, Werk, N/S.]
> TYP: Gesetzgeberischer Zweck / Revisionsmotiv / Lehre
> KERNAUSSAGE: [2–4 Sätze: Welcher Zweck/welche Idee wurde verfolgt? Warum wurde die Norm erlassen oder geändert?]
> FUNDSTELLE_BBL: [BBl-Zitat mit genauer Seitenzahl, z.B. BBl 2006 1085, S. 1120]
> RELEVANT FÜR: [Bedeutung / Normzweck / Absatz / Tatbestandsmerkmal]
> ```
>
> VERLINKUNG: Alle Quellen (Botschaften mit Fedlex-Link, Kommentare, Entscheide) müssen auf die Originalquelle verlinkt werden (Markdown-Link), sofern eine URL verfügbar ist.

---

## 4. RECHTSPRECHUNGSDATEI — Aktualisieren

Öffne oder erstelle `/opt/glossagens/content/kommentar/{gesetz}/art-{NNN}/rechtsprechung.md`.

Nur **neue** Entscheide eintragen (Abgleich mit BEKANNTE_ENTSCHEIDE) — und nur solche,
deren `Kernaussage` in der Belegprüfung `yes` oder `partial` erhalten hat (→ Teil D.1).
Die `Kernaussage` ist der Behauptungssatz, gegen den die Belegprüfung und später
`/audit` prüfen: sie muss den Entscheid wiedergeben, nicht das Thema umschreiben.

```markdown
---
title: "Rechtsprechung zu Art. {N} {ABBREV}"
weight: 99
date: {YYYY-MM-DD}
lastmod: {YYYY-MM-DD}
description: "Übersicht der Entscheide zu Art. {N} {ABBREV} – {Kurztitel}"
tags: ["Rechtsprechung", "{ABBREV}", "{topic1}"]
revisions:
  - date: {YYYY-MM-DD}
    by: "Glossagens Agent"
    model: "{MODELL-ID}"        # exakte KI-Modell-ID des Bearbeiters
    note: "{was; Prüfweg}"      # siehe Teil D.5
---

## Leitentscheide (BGE)

### {citation_string_de}, E. {X.X}
- **Thema**: {Stichwort}
- **Kernaussage**: {2–4 Sätze}
- **Einschlägig für**: {Abs./Tatbestandsmerkmal}

---

## Weitere Bundesgerichtsentscheide

### {citation_string_de}, E. {X.X}
- **Thema**: {Stichwort}
- **Kernaussage**: {2–4 Sätze}

---

## Kantonale Entscheide

### {citation_string_de}, E. {X.X}
- **Kanton**: {Kanton}
- **Thema**: {Stichwort}
- **Kernaussage**: {2–4 Sätze}

---

*Letzte Aktualisierung: {DATUM}*
```

---

## 5. HUGO BUILD + COMMIT

```bash
# Build-Check
cd /opt/glossagens && hugo --minify 2>&1 | tail -5

# Commit (nur bei erfolgreichen Build)
git add content/kommentar/{gesetz}/
git commit -m "feat: {ABBREV} Art. {N} kommentiert"
git push origin main
```

**Git-Auth-Setup** (falls noch nicht konfiguriert):
```bash
cd /opt/glossagens
git config user.email "agent@glossagens.ch"
git config user.name "Glossagens Agent"
source .env && echo "$GITHUB_TOKEN" | gh auth login --with-token
git remote set-url origin "https://$(gh auth token)@github.com/glossagens/glossagens.git"
```

**Bei Push-Ablehnung** (Remote hat neue Commits):
```bash
git stash
git pull --rebase origin main
git stash pop
git push origin main
```

---

# TEIL C — KOMMENTAR SCHREIBEN

---

## Frontmatter `_index.md`

```yaml
---
title: "Art. {N} — {Kurztitel}"
weight: {N}
date: {YYYY-MM-DD}
lastmod: {YYYY-MM-DD}
description: "Kommentar zu Art. {N} {ABBREV} – {Kurztitel}"
tags: ["{ABBREV}", "{topic1}", "{topic2}"]
revisions:
  - date: {YYYY-MM-DD}
    by: "Glossagens Agent"
    model: "{MODELL-ID}"        # exakte KI-Modell-ID des Bearbeiters
    note: "{was; Prüfweg}"      # siehe Teil D.5
---
```

> **Pflicht — Revisions-Vermerk:** Bei **jeder** Änderung (auch Neuanlage) einen neuen Eintrag **zuoberst** in `revisions:` einfügen: `by` (wer), `model` (welches KI-Modell; `human` bei manueller Bearbeitung), `note` (was geändert wurde und wie die Belege geprüft wurden, Teil D.5). Ältere Einträge bleiben erhalten. `agent_verified` und `mcp_verified` gibt es nicht mehr — nicht setzen.

## Inhaltliche Struktur

```markdown
## Gesetzeswortlaut

{{< wortlaut >}}

## Kommentierung

### Bedeutung und gesetzgeberischer Zweck
{Gesetzgeberische Idee und Zweck der Norm (Ratio Legis) gemäss Botschaft bei der Schaffung; Entstehungsgeschichte. Wurde die Bestimmung novelliert: Darstellung der Revisionsmotive und gesetzgeberischen Überlegungen der Gesetzesänderung(en). Belegt mit amtlicher Fundstelle, z.B. [Botschaft BBl 2006 1085, S. 1120](Fedlex-URL).}

### Voraussetzungen / Anwendungsbereich
{Tatbestandsmerkmale, oft als Liste, ausgelegt im Lichte des Normzwecks}

### Abgrenzungen
{Abgrenzungen zu verwandten Normen, wenn relevant}

### Kasuistik
{Fallgruppen aus der Rechtsprechung — konkrete Konstellationen}

## Literatur

{Hinweise auf Kommentarliteratur, falls get_commentary Ergebnisse liefert}
```

## Inhaltliche Grundsätze

- **Primär Rechtsprechung**: BGE zuerst, dann nicht publizierte BGer-Entscheide, dann kantonale Rspr.
- **BGE = BGer, keine Dublette**: Ein BGE ist ein BGer-Entscheid, den das Bundesgericht zur Publikation
  in der Amtlichen Sammlung ausgewählt hat — nicht zwei verschiedene Entscheide. Der Urteilskopf jeder
  BGE-Randnote nennt die zugrunde liegende Geschäftsnummer (z.B. „BGE 149 IV 42 … 6B_171/2022 vom 29.
  November 2022"): dieselbe Entscheidung, zweimal referenzierbar. Nie die Geschäftsnummer als eigenen,
  „bestätigenden" oder chronologisch späteren Entscheid neben dem BGE zitieren (z.B. „BGE X E. Y;
  bestätigt in BGer Z") — das erzeugt eine Schein-Bestätigung durch Selbstzitat und ist zudem oft
  chronologisch unsinnig, da BGE-Bandnummern dem Publikationsjahr folgen, nicht dem Urteilsdatum.
  Ist ein Entscheid als BGE publiziert, **ausschliesslich aus dem BGE zitieren** (E.-Nummern und Regeste
  sind dort massgeblich); die Geschäftsnummer nur nennen, wenn keine BGE-Fundstelle existiert, oder um
  bei „nicht publ. in: BGE X" auf eine in der amtlichen Sammlung fehlende Erwägung zu verweisen.
- **Gesetzgeberische Ideen und Zwecke (Materialien)**: Jede Bestimmung ist vorab anhand der amtlichen
  Materialien auf ihre Entstehungsgeschichte, die gesetzgeberische Absicht und ihren Normzweck (Ratio Legis)
  zu überprüfen (`get_article_purpose`, `get_article_history`, `get_materialien`). Wurde die Norm novelliert,
  sind die Erwägungen, Missstände und Ziele der Gesetzesänderung darzulegen. Dies bildet das Fundament für
  die teleologische Auslegung der Tatbestandsmerkmale. Es gilt strikt Regel R4: Niemals über den Normzweck
  spekulieren; Aussagen zum Zweck stets mit authentischen Botschaftserwägungen (BBl-Fundstelle und Link) belegen.
- **Lehre**: Nur wenn keine Rspr. existiert oder eine Kontroverse dokumentiert werden muss
- **Kasuistik**: Konkrete Fallkonstellationen aus der Praxis, soweit vorhanden
- **Sprache**: Deutsch, konzis, praxisnah
- **Belegtheit**: Kein Satz mit Beleg, der nicht durch die Belegprüfung gelaufen ist
  (→ Teil D.1). Lieber eine Aussage ohne Beleg als eine mit dem falschen — und lieber
  wörtlich zitieren als paraphrasieren: das macht aus `partial` ein `yes`.
- **Ausgebaute Belege**: Wird ein Beleg in einer Überarbeitung verworfen, gehört er in
  einen Abschnitt `## Entfernte Belege` am Dateiende — **nicht** in den Fliesstext.
  Im Fliesstext genannt, erzeugt er dort neue Prüfpaare, die `/audit` prompt als
  `unrelated` meldet; der eigene Ehrlichkeitsvermerk drückt dann die Belegquote.
>- **Verlinkung**: Alle Verweise auf Rechtsquellen (BGE, BGer, kantonale Entscheide, Gesetze, Botschaften) müssen zwingend als Markdown-Links auf die Originalquelle (z.B. [BGE 140 III 86](URL)) ausgestaltet werden, sofern eine URL verfügbar ist. Dies gilt sowohl für den Kommentar-Haupttext als auch für die Rechtsprechungsübersicht.

---

# TEIL C.5 — GESETZESÜBERSICHT (_index.md FÜR GESETZESORDNER)

Für jedes neue Gesetz: Zuerst einen Ordner `content/kommentar/{gesetz}/` anlegen und darin eine `_index.md` für die Gesetzesübersicht.

**Pfad:** `/opt/glossagens/content/kommentar/{gesetz}/_index.md`

**Frontmatter:**
```yaml
---
title: "{ABBREV} — {Gesetzestitel}"
weight: {N}
description: "Bundesgesetz ... (SR {SRNR})"
---
```

**Inhalt (eine bis zwei Zeilen):**
```markdown
Kommentar zum [Bundesgesetz ... vom ... (SR {SRNR})](https://www.fedlex.admin.ch/eli/cc/.../de). Tippe auf einen Artikel, um den Kommentar zu öffnen.
```

**Wichtig:**
- **Nur bei NEUEN Gesetzen anlegen**: `content/kommentar/{gesetz}/_index.md` wird ausschliesslich **einmalig bei der erstmaligen Einführung eines neuen Erlasses** angelegt.
- **Bei Artikelbearbeitung/Erweiterung NIEMALS anrühren**: Bei der Neuerstellung, Erweiterung oder Pflege einzelner Artikel (`art-{nr}/`) darf `content/kommentar/{gesetz}/_index.md` **unter keinen Umständen** geändert oder mit Revisions-Einträgen versehen werden. Die Artikelliste im Inhaltsverzeichnis wird von Hugo und `data/systematik/{gesetz}.yaml` vollautomatisch generiert. Die Revisionshistorie von Artikeländerungen gehört ausschliesslich in das jeweilige Page Bundle (`art-{nr}/_index.md` und `rechtsprechung.md`).
- **Kein `date`, `lastmod`, `tags`** — das ist nur für Artikel-Kommentare (`art-{NNN}/_index.md`)!
- **Weight** bestimmt die Reihenfolge im Menü (OR=1, StPO=2, BewG=3, EMRK=4, ZGB=5, etc.)
- **Description** sollte die SR-Nummer und Rechtsgebiet kurz nennen
- **Link auf Fedlex** (wenn die Datei die offizielle Norm enthält)

---

# TEIL D — BELEGPRÜFUNG UND QUALITÄTSKONTROLLE

Ein Kommentar ist nicht dadurch belegt, dass er Entscheide zitiert, sondern dadurch, dass die
zitierten Entscheide die Sätze tragen, für die sie stehen. Die Prüfeinheit ist deshalb das
**Paar (Behauptungssatz, Beleg)**, nie das Zitat für sich.

Zwei Kontrollpunkte, beide obligatorisch:

| | Wann | Wie | Fragt |
|---|---|---|---|
| **D.1 Belegprüfung** | **vor** dem Schreiben, pro Paar | eigenes Urteil gegen den wörtlichen Entscheidtext | Trägt dieser Entscheid diesen Satz? |
| **D.3 Schlussattest** | **nach** dem Schreiben, pro Bundle | `audit.py` + unabhängige Judge-Subagenten | Existiert alles Zitierte, stimmen Pinpoints, Verbatim — und stützt jeder Beleg seinen Satz? |

Die Reihenfolge ist Absicht. Die Einzelprüfung früh verhindert, dass ein falscher
Beleg überhaupt in den Text kommt; der Audit-Lauf am Schluss fängt, was beim
Schreiben entstanden ist — umgestellte Sätze, verrutschte Belege, aus dem
Gedächtnis ergänzte Zitate.

**Beide Kontrollpunkte laufen ohne LLM-Tool von opencaselaw.** `check_claim_support`
und `attest_response` sind serverseitige Claude-Aufrufe, die den Betreiber je
Aufruf $0.05–$0.50 kosten; dieser Skill hat sein Tageskontingent im August 2026
um mehr als das Zwanzigfache überzogen und die Sperre des Clients ausgelöst.
Sie werden nicht mehr aufgerufen — auch nicht «nur einmal zur Kontrolle».
Die Lookups (`cite`, `get_law`, `get_erwaegung`, `get_regeste`,
`get_decision`, `get_decision_structure`, `get_article_history`) bleiben frei
nutzbar; Suchtools (`search_*`, `find_*`) tragen einen kleinen LLM-Anteil und
sind nur zu verwenden, wenn kein Lookup die Frage beantwortet.

---

## D.1 — Belegprüfung vor dem Schreiben (Urteil gegen den wörtlichen Text)

Für **jedes** Paar aus geplanter Aussage und Beleg, bevor der Satz geschrieben wird:

1. **Text holen** — `get_erwaegung(decision_id, e_number)` für die Erwägung, sonst
   `get_regeste(decision_id)`, sonst `get_decision(decision_id)`. Alles Lookups,
   alles kostenlos.
2. **Urteilen** — beurteile den geplanten Kommentarsatz gegen **diesen Text** nach
   den Regeln in `agent/skills/glossagens-audit/judge-prompt.md` (dieselbe Skala,
   die auch das Audit anlegt).
3. **Belegstelle festhalten** — den wörtlichen Satz aus dem Text, der die Aussage
   trägt. Findest du keinen, ist das Urteil `no`, nicht `partial`.

Der `claim` ist der **Kommentarsatz**, nicht das Thema. «Fristwiederherstellung bei
unverschuldeter Säumnis» ist kein claim; «Die Frist wird nur wiederhergestellt, wenn die
Partei kein Verschulden trifft» ist einer. Ein vager claim erzeugt ein wertloses `yes`.

| `supports` | Bedeutung | Was zu tun ist |
|---|---|---|
| `yes` | Der Entscheid trägt die Aussage | Übernehmen |
| `partial` | Trägt sie, aber die Paraphrase ist zu weit | Aussage um den Qualifikator ergänzen oder wörtlich zitieren, dann erneut prüfen |
| `no` | Der Entscheid sagt das nicht | Beleg verwerfen — anderen suchen oder Aussage streichen |
| `contradicts` | Der Entscheid sagt das Gegenteil | Beleg verwerfen; die Aussage ist vermutlich falsch |
| `unrelated` | Anderes Thema | Beleg verwerfen |

**`no` / `contradicts` / `unrelated` bei hoher Konfidenz sind Befunde, keine
Messungenauigkeit.** Ein Entscheid, der thematisch passt, die konkrete Rechtsfolge aber
nicht stützt, ist genau der Fehler, der einem Praktiker vor Gericht schadet. Nicht
«abschwächen und trotzdem zitieren» — verwerfen.

Wiederkehrende Beobachtung aus dem Bestand: ein `partial` heisst meist, dass die
Paraphrase einen Qualifikator des Gerichts weggelassen hat («in Anbetracht der Schwere
der Grundrechtseinschränkung», «verfassungsmässiges *Individual*recht»). Wörtlich
zitieren macht daraus ein `yes`.

**Das Urteil über die eigene Aussage ist eine Vorprüfung, kein Attest.** Wer
schreibt und zugleich urteilt, ist milde mit sich; deshalb prüft D.3 dieselben
Paare nochmals — dort mit einem Judge, der den Satz nicht geschrieben hat. Das
Verfahren fängt trotzdem den grössten Teil ab, weil es die Frage stellt, bevor
der Satz existiert.

**Wo es nichts bringt**: Für den blossen Gesetzeswortlaut (Fedlex `get_article`) und für
reine Materialienzitate ist die Grounding-Prüfung nicht das Werkzeug — sie prüft
Entscheide. Für Botschaftsstellen `get_materialien` verwenden und verbatim zitieren.

### Pinpoints (`get_decision_structure` + `get_erwaegung`)

Ein Pinpoint wird **nie geschätzt**. Eine Regeste verweist oft auf «(E. 4)», während die
Erwägung nur als `4.1` / `4.2.1` existiert; `cite` akzeptiert den Verweis trotzdem, und
erst `get_erwaegung` deckt auf, dass er ins Leere zeigt.

```
get_decision_structure: { "decision_id": "..." }   → erwaegungen_paragraphs = die
                                                     tatsächlich vorhandenen Nummern
get_erwaegung:          { "decision_id": "...", "e_number": "4.2" }   → Wortlaut
```

Die richtige Erwägung ist die, deren Wortlaut die Aussage trägt — festgestellt durch
Lesen, nicht durch ein Suchtool. Findet sich keine: keinen Pinpoint setzen. Ein Zitat
ohne Pinpoint ist korrekt, ein Zitat mit falschem Pinpoint nicht.

Nur Bundesentscheide haben strukturierte Erwägungen; bei kantonalen entfällt der Schritt.

---

## D.2 — Existenz und Wortlaut

Vor dem Schreiben ebenfalls:

- **Jede Zitierung** stammt wörtlich aus `citation_string_de` / `markdown_link` einer
  `cite`- oder Such-Antwort. Nie selbst konstruieren, nie aus dem Gedächtnis ergänzen.
- **Gesetzeswortlaut** per `{{< wortlaut >}}` aus `scripts/wortlaut.py` — nie von Hand.
- **Wörtliche Zitate** (≥ 30 Zeichen) nur aus `get_erwaegung` / `get_regeste` — kopiert,
  nicht nachgeschrieben.

---

## D.2a — Linkziel: entscheidsuche.ch, opencaselaw nur als Rückfall

Jeder zitierte Entscheid wird **auf entscheidsuche.ch verlinkt**, soweit dort ein
Dokument vorliegt. `mcp.opencaselaw.ch/entscheid/...` ist nur noch **Rückfallebene** —
für Entscheide, die entscheidsuche nicht führt (ältere kantonale Entscheide, EGMR).
Am Rechercheweg ändert das nichts: opencaselaw bleibt für `cite`, `get_erwaegung` und
`get_regeste` massgebend; nur das *Linkziel* wechselt.

**Die URL nie konstruieren.** Sie enthält eine nicht ableitbare Sammlungsnummer
(`CH_BGE_005_...`). Verbatim aus dem Feld `document_url` übernehmen:

```
mcp__entscheidsuche__search_by_case_number: { "case_number": "BGE 144 III 519", "size": 3 }
→ document_url: https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_005_BGE-144-III-519_2018.html
```

- **Pinpoint als Anker**: HTML-Dokumente tragen `id="consideration_{E-Nr}"` —
  `[BGE 144 III 519 E. 5.2](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_005_BGE-144-III-519_2018.html#consideration_5.2)`.
  Anker nur setzen, wenn die Erwägungsnummer im Dokument wirklich vorkommt.
- **PDF-Dokumente** (`is_pdf: true`, viele kantonale Entscheide) haben keine Anker:
  ohne `#` verlinken.
- Kein Treffer bei entscheidsuche → Rückfall `https://mcp.opencaselaw.ch/entscheid/{decision_id}`.
- Die Regel gilt **nur für die Zukunft**: bestehende opencaselaw-Links werden nicht
  migriert.

---

## D.3 — Schlussattest (Audit-Lauf über das Bundle)

Auf dem **fertigen** Bundle, beide Dateien auf einmal:

```bash
python3 agent/skills/glossagens-audit/audit.py content/kommentar/{gesetz}/art-{nr} --emit-jobs
# offene Paare durch Judge-Subagenten beurteilen lassen (glossagens-audit, Schritt 1b)
python3 agent/skills/glossagens-audit/audit.py --ingest audit-jobs/{gesetz}-{nr}
python3 agent/skills/glossagens-audit/audit.py content/kommentar/{gesetz}/art-{nr}
```

Der Lauf prüft dieselben Halluzinationsklassen, die früher `attest_response`
prüfte — Existenz der Entscheide, Auflösbarkeit der Pinpoints, Gesetzeswortlaut,
Verbatim-Treue der Zitate ≥ 30 Zeichen —, und für das Grounding urteilt ein
Judge-Subagent, der den Text nicht geschrieben hat. Das ist der Punkt: die
Prüfung taugt nur, solange sie unabhängig vom Schreiben ist.

Geprüft werden **beide** Dateien: `_index.md` und `rechtsprechung.md`. Die
Rechtsprechungsübersicht behauptet in jeder `Kernaussage` etwas über einen Entscheid — sie
ist so belegpflichtig wie der Kommentartext.

**Nicht committen, solange Paare `offen` sind oder Befunde offenstehen.** Beheben
heisst je nach Klasse:

| Issue | Behebung |
|---|---|
| Zitierung existiert nicht | Aus `close_matches` korrigieren, wenn der `match_reason` die Identität belegt; sonst Beleg raus |
| Pinpoint löst nicht auf | Nummer aus `get_decision_structure` prüfen; findet sich keine tragende Erwägung, Pinpoint streichen |
| Verbatim weicht ab | Durch den Wortlaut aus `get_erwaegung` / `get_regeste` ersetzen |
| Datum stimmt nicht | Aus der Tool-Antwort korrigieren |
| Grounding-Beanstandung | Wie D.1: Aussage schärfen oder Beleg verwerfen |

### Belegquote

Aus den Ergebnissen von D.1 und D.3:

```
Belegquote = (yes + 0.5 × partial) / beurteilte Paare
```

`partial` zählt halb — die Aussage ist tragfähig, aber zu weit gefasst. Nicht beurteilbare
Paare (Literaturzitate, Materialien) bleiben aus dem Nenner.

| Belegquote | Konsequenz |
|---|---|
| ≥ 80 % | Commit nach Behebung der Einzelbefunde |
| 50–79 % | Vor dem Commit überarbeiten: schwach belegte Passagen abschwächen oder streichen |
| < 50 % | **Nicht committen.** Belegapparat verwerfen, Aussagen behalten, für jede Aussage neu einen Beleg suchen und einzeln gegen den Entscheidtext prüfen |

---

## D.4 — Checklisten vor dem Commit

**Belegtheit:**
- [ ] Jedes Paar (Aussage, Beleg) gegen den wörtlichen Entscheidtext geprüft (D.1)?
- [ ] Kein Beleg mit `no` / `contradicts` / `unrelated` im Text verblieben?
- [ ] `partial`-Aussagen um den Qualifikator ergänzt oder wörtlich zitiert?
- [ ] Jeder Pinpoint durch `get_erwaegung` belegt — keiner geschätzt?
- [ ] Audit-Lauf über das Bundle ohne `offen` und ohne offene Befunde (D.3)?
- [ ] Kein Aufruf von `check_claim_support` / `attest_response` / `reflect`?

**Quellenintegrität:**
- [ ] Alle citation_strings aus Tool-Ergebnissen — nicht selbst konstruiert?
- [ ] Gesetzestext per `{{< wortlaut >}}` (Daten aus `scripts/wortlaut.py`, mit committet) — kein Blockquote?
- [ ] Direkte Zitate nur aus `get_erwaegung` oder `get_regeste`?
- [ ] Alle Rechtsquellen (Entscheide, Gesetze, Materialien) auf Originalquelle verlinkt?
- [ ] Unsichere Stellen weggelassen oder als Paraphrase kenntlich gemacht?
- [ ] Literaturzitate als das ausgewiesen, was sie sind: mit den Fall-Tools **nicht**
      verifizierbar — nie als geprüft ausgeben?

**Struktur:**
- [ ] **Gesetzesübersicht vorhanden?** `content/kommentar/{gesetz}/_index.md` mit minimalem Frontmatter (title, weight, description)?
- [ ] Page Bundle korrekt: `art-{NNN}/_index.md` + `art-{NNN}/rechtsprechung.md`?
- [ ] Alle 7 Frontmatter-Felder: `title`, `weight`, `date`, `lastmod`, `description`, `tags`, `revisions`?
- [ ] `revisions`-Eintrag in **beiden** Dateien gesetzt (`by`, `model`, `note` mit Prüfweg)?
- [ ] Kein `agent_verified` / `mcp_verified` im Frontmatter?

**Inhalt:**
- [ ] `## Gesetzeswortlaut` enthält `{{< wortlaut >}}` und `data/wortlaut/{gesetz}/art-{NNN}.json` existiert?
- [ ] Gesetzgeberische Ideen und Zwecke der Bestimmung (Schaffung und allfällige Revisionen) via `get_article_purpose`, `get_article_history` oder `get_materialien` eruiert und in «Bedeutung und gesetzgeberischer Zweck» eingearbeitet?
- [ ] Regel R4 eingehalten: Keine freie Spekulation über Gesetzeszweck/Teleologie, sondern Beleg durch authentische Botschaftserwägungen (BBl-Fundstelle und Link)?
- [ ] Rechtsprechung in absteigender Hierarchie (BGE → BGer → kantonal)?
- [ ] Hugo-Build erfolgreich?

---

## D.5 — Prüfweg im Revisionseintrag festhalten

Prüfflags (`mcp_verified`, `agent_verified`) gibt es seit 28.10.2026 nicht mehr: Sie waren
Selbstauskünfte, und gerade die fabrizierten Bestände trugen `true`. An ihre Stelle tritt
die `note` der Revision, die in Klartext sagt, **was** geprüft wurde. Die Prüfung selbst
bleibt Pflicht:

1. Der Gesetzeswortlaut stammt per `{{< wortlaut >}}` aus der amtlichen Quelle (`scripts/wortlaut.py`),
2. jede Zitierung ist aus einer Tool-Antwort kopiert,
3. jedes Paar (Aussage, Beleg) ist gegen den wörtlichen Entscheidtext beurteilt (D.1), und
4. der Audit-Lauf über das Bundle zeigt kein `offen` und keine offenen Befunde mehr (D.3).

Fehlt ein Schritt — etwa weil eine Quelle nicht erreichbar war —, steht das ebenso in der
`note`. Nichts behaupten, was nicht geschehen ist: Die `note` ist eine Aussage über den
Prüfvorgang, keine Zierde.

Revisionseintrag nach der Prüfung:

```yaml
lastmod: {heute}
revisions:
  - date: {heute}
    by: "Glossagens Agent"
    model: "{exakte Modell-ID}"
    note: "{was}; Belege gegen den Entscheidtext geprüft, Audit-Lauf ohne offene Befunde"
```

---

## D.6 — Grenzen (im Bericht ausweisen, nicht kaschieren)

- **Literaturzitate.** Die Fall-Tools decken sie nicht ab. `search_scholarship` /
  `find_scholarship_citing_statute` erreichen die OA-Bestände; der klassische
  Kommentarapparat (BSK, ZK, Stämpfli) liegt grösstenteils ausserhalb → Status
  «nicht verifizierbar», nie «korrekt».
- **Botschaften.** `BBl`-Fundstellen prüft das Audit nicht; dafür `get_article_purpose`, `get_materialien`
  (und nur wenn nötig `search_botschaft`).
- **Juristische Richtigkeit.** Geprüft wird Belegtheit, nicht Qualität. Ein durchgehend
  belegter Kommentar kann dogmatisch schief sein.
- **Aktualität — der gefährlichste blinde Fleck.** Die Grounding-Prüfung beantwortet
  «sagt der Entscheid das?», nicht «gilt das noch?». Ein `yes` ist kein
  Aktualitätsnachweis. Bei Leitentscheiden, die älter als rund zehn Jahre sind, deshalb
  zusätzlich `get_article_history` (Gesetzesrevision dazwischen?) und `search_decisions`
  mit dem Sachthema + «Praxisänderung» bzw. dem EGMR-Fallnamen.

---

## D.7 — Abschlussbericht an den Benutzer

```
KOMMENTAR-STATUS: {ABBREV} Art. {N}
────────────────────────────────────
Bearbeitete Dateien:
  - _index.md [erstellt / ergänzt]
  - rechtsprechung.md [erstellt / ergänzt]

Neue Entscheide integriert:
  - BGE: {Anzahl}   BGer: {Anzahl}   Kantonal: {Anzahl}   EGMR: {Anzahl}

Belegprüfung (gegen den Entscheidtext):
  Paare geprüft:  {n}
  gestützt:       {n}      teilweise: {n}
  verworfen:      {n}  ({no}/{contradicts}/{unrelated})
  Belegquote:     {x} %

Pinpoints:        {n} gesetzt, alle via get_erwaegung belegt
Schlussattest:    Audit-Lauf {Belegquote} %, offen {n}, Befunde {behoben|Liste}

Nicht verifizierbar: {Literatur/Materialien — Liste + Grund, oder «keine»}
Offene Fragen:       {Kurzbeschreibung oder «keine»}

Aktualisierungsdatum: {DATUM}
```

Verhältnis zu den anderen Skills: `/lint` prüft den **Gesetzeswortlaut**, `/audit` prüft
den **Belegapparat bestehender** Artikel nachträglich und maschinell über den gesamten
Bestand. Teil D ist die vorgelagerte Fassung derselben Prüfung — sie soll verhindern, dass
`/audit` überhaupt etwas zu finden hat. Bei grösseren Überarbeitungen nach dem Commit
zusätzlich `/audit {gesetz} art-{NNN}` laufen lassen.

---

# TEIL E — TECHNISCHE REFERENZ

## opencaselaw MCP — Verfügbare Calls

| Call | Beschreibung | Typischer Einsatz |
|------|-------------|-------------------|
| `mcp__fedlex-connector__get_article` | Gesetzestext verbatim | **Immer als erstes** |
| `get_law` (opencaselaw) | Gesetzestext verbatim | Nur Rückfall: kantonales Recht / Fedlex führt die Norm nicht |
| `find_leading_cases` | Leitentscheide zu einer Norm | Erstrecherche |
| `find_citations` | Entscheide die Art. zitieren | Breite Abdeckung |
| `search_decisions` | Volltextsuche | Thematische Suche |
| `get_case_brief` | Kurzfassung eines Entscheids | Schnelle Sichtung |
| `get_decision` | Volltext | Vertiefung |
| `get_erwaegung` | Einzelne Erwägung verbatim | Direkte Zitate |
| `get_regeste` | Leitsatz verbatim | Direkte Zitate |
| `list_courts` | Verfügbare Gerichte | Kantonssuche |
| `get_article_purpose` | Wörtliche Botschaftserwägungen zum Normzweck | **Gesetzgeberische Idee und Zweck (Erlass + Revision)** |
| `get_article_history` | Chronologie der Norm (Text + Botschaften + Leitentscheide) | **Revisionsgeschichte & Entwicklungsbogen** |
| `search_botschaft` | Botschaften / Materialien Volltextsuche | Entstehungsgeschichte, Beratungsdetails |
| `get_materialien` | Materialien-Übersicht & Vernehmlassungen | Fundstellen (BBl), Erläuternde Berichte |
| `search_materialien` | FTS-Suche in Materialien | Thematische Materialiensuche |
| `get_commentary` | OnlineKommentar | Lehrrecherche |
| `get_doctrine` | Lehrmeinungen | Annotationen |
| `cite` | Zitierung auflösen, `close_matches` | Existenz prüfen, Zitierstring holen |
| `get_decision_structure` | vorhandene Erwägungsnummern | **Pinpoint statt raten** |
| `get_article_history` | Revisionen einer Norm | Aktualität alter Belege |

**Gesperrt — nie aufrufen:** `check_claim_support`, `attest_response`, `reflect`.
Das sind serverseitige Claude-Aufrufe zulasten von opencaselaw ($0.05–$0.50 je
Aufruf, Kontingent 200/Tag/IP); ihre Aufgabe übernehmen D.1 und D.3.
**Sparsam — nur wenn kein Lookup reicht:** `search_decisions`, `find_leading_cases`,
`find_citations` und die übrigen `search_*` / `find_*` (Query-Parse, Expansion und
Rerank sind kleine LLM-Aufrufe).

## Gesetz-Abkürzungen → SR-Nummern

| Abbr | SR | Verzeichnis | Vollname |
|------|-----|-----------|----------|
| StPO | 312.0 | `stpo` | Strafprozessordnung |
| StGB | 311.0 | `stgb` | Strafgesetzbuch |
| OR | 220 | `or` | Obligationenrecht |
| ZGB | 210 | `zgb` | Zivilgesetzbuch |
| BV | 101 | `bv` | Bundesverfassung |
| BGG | 173.1 | `bgg` | Bundesgerichtsgesetz |
| VwVG | 172.021 | `vwvg` | Verwaltungsverfahrensgesetz |
| SchKG | 281.1 | `schkg` | SchKG |

## Tipps für Subagenten

1. **Parallel starten**: Subagenten A, B und C gleichzeitig (parallele Agent-Tool-Aufrufe in einer Nachricht).

2. **Enge Fragestellung** (im /loop): Nicht «alles zu Art. X», sondern «Entscheide zur Frage Y in Art. X Abs. Z» — enger Auftrag, präzisere Ergebnisse.

3. **Duplikation vermeiden**: BEKANNTE_ENTSCHEIDE-Liste jedem Subagenten mitgeben.

4. **Kontextmanagement**: Nach 2–3 Loop-Iterationen `/compact` ausführen. Wichtige Infos vorher in `.md`-Dateien speichern.

5. **Abbruchkriterien für /loop:**
   - Zwei aufeinanderfolgende Iterationen ohne neue Entscheide
   - Alle Absätze kommentiert
   - Manueller Abbruch durch Benutzer

## Pitfalls

- **Gesetzesübersicht vergessen**: Für jedes neue Gesetz MUSS zuerst `content/kommentar/{gesetz}/_index.md` angelegt werden — sonst zeigt Hugo keine Menü-Übersicht und die Artikel sind schwer zu finden
- **Falsches Frontmatter in Gesetzesübersicht**: Keine `date`, `lastmod`, `tags` — nur `title`, `weight`, `description` (siehe Teil C.5)
- **Page Bundle vs. Flat File**: Immer `art-{NNN}/_index.md` — nie `art-{NNN}.md`
- **rechtsprechung.md**: Liegt im Bundle (`art-{NNN}/rechtsprechung.md`), nicht daneben
- **`agent_verified` / `mcp_verified`**: abgeschafft — nicht mehr setzen, auch nicht aus alten Vorlagen übernehmen
- **Revisions-Vermerk vergessen**: Bei **jeder** Änderung (auch Neuanlage) muss oben in `revisions:` ein Eintrag mit `by` / `model` / `note` ergänzt werden — sonst ist nicht nachvollziehbar, wer mit welchem Modell und mit welchem Prüfweg gearbeitet hat
- **Citation strings**: Nie selbst konstruieren — immer aus `citation_string_de` des MCP-Tools
- **Linkziel**: Entscheide auf entscheidsuche.ch verlinken (`document_url` verbatim), opencaselaw nur als Rückfall — siehe D.2a
- **«Thematisch passend» statt geprüft**: Der häufigste und teuerste Fehler. Ein Entscheid,
  der Stufe «existiert» besteht, kann trotzdem etwas ganz anderes entscheiden — im Bestand
  gab es Artikel, deren sämtliche Belege existierten und **keiner** die Aussage trug.
  Die Belegprüfung gegen den wörtlichen Text ist deshalb nicht weglassbar (Teil D.1)
- **Pinpoint geschätzt**: «E. 3.1» ist geraten, wenn es nicht aus `get_erwaegung`
  stammt. Regesten verweisen auf «E. 4», wo nur `4.1`/`4.2.1` existiert — `cite`
  merkt das nicht
- **Selbst geschrieben, selbst attestiert**: Das eigene Urteil über den eigenen Satz
  ist eine Vorprüfung. Das Attest muss von einem Judge kommen, der den Satz nicht
  geschrieben hat — dafür der Audit-Lauf am Ende (Teil D.3)
- **LLM-Tool von opencaselaw aufgerufen**: `check_claim_support`, `attest_response`
  und `reflect` kosten den Betreiber je Aufruf $0.05–$0.50. Sie sind gesperrt; im
  August 2026 hat ein Überzug des Kontingents die Sperrung des Clients ausgelöst
- **`rechtsprechung.md` ungeprüft gelassen**: Sie behauptet in jeder `Kernaussage` etwas
  über einen Entscheid und ist genauso belegpflichtig wie der Kommentar
- **Prüfweg geschönt**: Die `note` behauptet eine Prüfung, die nicht stattfand (Teil D.5).
  Lieber «Entscheide nur auf Existenz geprüft» als ein falsches «verifiziert»
- **Fedlex `get_article`**: Braucht `rs_number` (SR-Nummer), nicht die Abkürzung
- **get_law** (Rückfall): Braucht `abbreviation`, nicht SR-Nummer (obwohl beides funktioniert)
- **StPO vs. StGB**: Nachfragen wenn unklar, beide beginnen mit «St»
- **Remote divergence**: Vor Push immer `git pull --rebase` wenn abgelehnt
