---
name: glossagens-content-creation
description: >-
  Create and maintain legal commentary articles for the Glossagens Hugo site, with built-in grounding checks (check_claim_support before writing, attest_response before commit). Offers three workflows: /kommentar (full creation), /recherche (research only), /loop (iterative gap analysis with subagents).
version: 4.0.0
author: Hermes Agent
tools:
  - mcp_opencaselaw_check_claim_support
  - mcp_opencaselaw_attest_response
  - mcp_opencaselaw_find_relevant_erwaegung
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
  - mcp_opencaselaw_get_erwaegung
  - mcp_opencaselaw_get_regeste
  - mcp_opencaselaw_list_courts
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
2. GESETZESTEXT abrufen (→ Teil B, Abschnitt 2)
3. RECHERCHE — parallel subagent research (→ Teil B, Abschnitt 3)
4. RECHTSPRECHUNGSDATEI aktualisieren (→ Teil B, Abschnitt 4)
5. **BELEGPRÜFUNG vor dem Schreiben** — jedes Paar (Aussage, Beleg) durch `check_claim_support` (→ Teil D.1)
6. KOMMENTAR schreiben/ergänzen (→ Teil C) — nur mit den Belegen, die Schritt 5 überlebt haben
7. **SCHLUSSATTEST** — `attest_response` auf dem fertigen Text (→ Teil D.3)
8. QUALITÄTSKONTROLLE — Checklisten (→ Teil D.4)
9. HUGO BUILD + COMMIT (→ Teil B, Abschnitt 5)

> Schritt 5 und 7 sind **nicht optional**. `mcp_verified: true` setzt beide voraus (→ Teil D.5).

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

## Workflow 3: `/loop {GESETZ} Art. {N}` — Iterative Lückenanalyse

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
│     - Fehlende Kasuistik zu Kerntatbeständen          │
│     - Konventionsrechtliche Aspekte (EMRK/EGMR)?      │
│     - Gesetzesmaterialien eingearbeitet?              │
│     - Neuere Entscheide (nach letzter Aktualisierung)?│
│                                                       │
│  3. PRIORISIERUNG                                     │
│     (a) Fehlende BGer-Leitentscheide (höchste Prio)  │
│     (b) Unkommentierte Absätze                        │
│     (c) Fehlende Kasuistik                            │
│     (d) EMRK/Konventionsrecht                         │
│     (e) Materialien und Lehre                         │
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
│     melden: check_claim_support(claim, decision_id,   │
│     pinpoint) VOR der Integration.                    │
│     yes/partial → übernehmen (partial: abschwächen)   │
│     no/contradicts/unrelated → verwerfen, nicht       │
│     «thematisch passend» weiterreichen.               │
│                                                       │
│  6. INTEGRATION                                       │
│     - Geprüfte Entscheide → rechtsprechung.md         │
│     - Kommentar ergänzen: neue Abschnitte, Kasuistik  │
│                                                       │
│  7. SCHLUSSATTEST (Teil D.3)                          │
│     attest_response(audit_grounding=true) auf den in  │
│     dieser Iteration NEU geschriebenen Abschnitten.   │
│     ok:false → zurück zu Schritt 5.                   │
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
   Diese Liste jedem Subagenten mitgeben.

---

## 2. GESETZESTEXT — Wortlaut abrufen

```
mcp_opencaselaw_get_law: { "abbreviation": "{ABBREV}", "article": "Art. {N}", "language": "de" }
```

Alternativ:
```
mcp_opencaselaw_get_legislation: { "query": "Art. {N} {ABBREV} SR {SRNR}" }
```

Vollständigen Wortlaut aller Absätze und Buchstaben verwenden.

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
> PINPOINT: {E. X.Y — nur wenn durch get_erwaegung oder find_relevant_erwaegung belegt, sonst «—»}
> THEMA: [2–3 Worte]
> KERNAUSSAGE: [2–4 Sätze]
> EINSCHLÄGIG FÜR: [Absatz/Tatbestandsmerkmal]
> BELEGPRÜFUNG: {supports-Wert aus check_claim_support} ({confidence})
> STATUS: NEU
> ```
>
> **Pflicht vor der Meldung**: Für jeden Entscheid, den du melden willst, einmal
> `check_claim_support(claim=<deine KERNAUSSAGE>, decision_id=..., pinpoint=...)`.
> Melde nur `yes` und `partial`. `no` / `contradicts` / `unrelated` werden **nicht**
> gemeldet — auch nicht mit dem Hinweis «thematisch verwandt». Bei `partial` die
> Kernaussage so umformulieren, dass der Qualifikator des Gerichts drinsteht
> (wörtlich zitieren macht aus `partial` meist ein `yes`).
> **Pinpoint nie raten**: `find_relevant_erwaegung` liefert ihn; bei `no_match` oder
> Konfidenz `low` gar keinen Pinpoint angeben.
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
> BELEGPRÜFUNG: {supports-Wert aus check_claim_support} ({confidence})
> STATUS: NEU
> ```
>
> **Pflicht vor der Meldung**: `check_claim_support(claim=<KERNAUSSAGE>, decision_id=...)`
> — nur `yes` / `partial` melden. Kantonale Entscheide haben keine strukturierten
> Erwägungen; dort ohne `pinpoint` prüfen (der Judge liest dann Regeste bzw. Textanfang)
> und im Kommentar keinen Pinpoint setzen.
>
> VERLINKUNG: Alle Entscheide und Gesetze müssen auf die Originalquelle verlinkt werden (Markdown-Link), sofern möglich.

### Subagent-Vorlage C: Materialien und Lehre

> **Aufgabe**: Recherchiere Gesetzesmaterialien und (soweit für Kontroversen relevant) Schrifttum zu Art. {N} {ABBREV}.
>
> **Materialien** (immer prüfen):
> - `search_materialien` mit query "Art. {N} {ABBREV}"
> - `get_materialien` für relevante Botschafts-Stellen
>
> **Lehre** (nur recherchieren wenn keine Rspr. existiert oder eine Kontroverse aufzubereiten ist):
> - `get_commentary` mit abbreviation="{ABBREV}", article="{N}"
> - `get_doctrine` mit query="Art. {N} {ABBREV}"
>
> **Ausgabeformat:**
> ```
> QUELLE: [Botschaft BBl ... / Kommentar-Autor, Werk, N/S.]
> TYP: Material / Lehre
> KERNAUSSAGE: [2–3 Sätze]
> RELEVANT FÜR: [Absatz / Thema]
> ```
>
> VERLINKUNG: Alle Quellen (Botschaften, Kommentare, Entscheide) müssen auf die Originalquelle verlinkt werden (Markdown-Link), sofern eine URL (z.B. Fedlex, Bger.ch) verfügbar ist.

---

## 4. RECHTSPRECHUNGSDATEI — Aktualisieren

Öffne oder erstelle `/opt/glossagens/content/kommentar/{gesetz}/art-{NNN}/rechtsprechung.md`.

Nur **neue** Entscheide eintragen (Abgleich mit BEKANNTE_ENTSCHEIDE) — und nur solche,
deren `Kernaussage` in der Belegprüfung `yes` oder `partial` erhalten hat (→ Teil D.1).
Die `Kernaussage` ist der Behauptungssatz, gegen den `check_claim_support` und später
`/audit` prüfen: sie muss den Entscheid wiedergeben, nicht das Thema umschreiben.

```markdown
---
title: "Rechtsprechung zu Art. {N} {ABBREV}"
weight: 99
date: {YYYY-MM-DD}
lastmod: {YYYY-MM-DD}
description: "Übersicht der Entscheide zu Art. {N} {ABBREV} – {Kurztitel}"
tags: ["Rechtsprechung", "{ABBREV}", "{topic1}"]
agent_verified: false
revisions:
  - date: {YYYY-MM-DD}
    by: "Glossagens Agent"
    model: "{MODELL-ID}"        # exakte KI-Modell-ID des Bearbeiters
    mcp_verified: {true|false}  # true nur, wenn alle Entscheide via opencaselaw-MCP geprüft
    note: "{kurze Beschreibung}"
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
agent_verified: true          # nur zulässig, wenn jüngste Revision mcp_verified: true
revisions:
  - date: {YYYY-MM-DD}
    by: "Glossagens Agent"
    model: "{MODELL-ID}"        # exakte KI-Modell-ID des Bearbeiters
    mcp_verified: {true|false}  # true nur, wenn Gesetzestexte UND Entscheide via opencaselaw-MCP geprüft
    note: "{kurze Beschreibung}"
---
```

> **Pflicht — Revisions-Vermerk:** Bei **jeder** Änderung (auch Neuanlage) einen neuen Eintrag **zuoberst** in `revisions:` einfügen: `by` (wer), `model` (welches KI-Modell; `human` bei manueller Bearbeitung), `mcp_verified` (`true` nur, wenn alle Gesetzestexte und Entscheide via opencaselaw-MCP `cite`/`get_law`/`get_erwaegung` geprüft wurden). Ältere Einträge bleiben erhalten. `agent_verified: true` nur, wenn die jüngste Revision `mcp_verified: true` trägt.

## Inhaltliche Struktur

```markdown
## Gesetzeswortlaut

> {Verbatim statute text from get_law, in blockquote}

## Kommentierung

### Bedeutung
{2-3 Sätze zur Bedeutung des Artikels}

### Voraussetzungen / Anwendungsbereich
{Tatbestandsmerkmale, oft als Liste}

### Abgrenzungen
{Abgrenzungen zu verwandten Normen, wenn relevant}

### Kasuistik
{Fallgruppen aus der Rechtsprechung — konkrete Konstellationen}

## Literatur

{Hinweise auf Kommentarliteratur, falls get_commentary Ergebnisse liefert}
```

## Inhaltliche Grundsätze

- **Primär Rechtsprechung**: BGE zuerst, dann nicht publizierte BGer-Entscheide, dann kantonale Rspr.
- **Materialien**: Einarbeiten wenn sie der Rspr. etwas hinzufügen oder keine Praxis existiert
- **Lehre**: Nur wenn keine Rspr. existiert oder eine Kontroverse dokumentiert werden muss
- **Kasuistik**: Konkrete Fallkonstellationen aus der Praxis, soweit vorhanden
- **Sprache**: Deutsch, konzis, praxisnah
- **Belegtheit**: Kein Satz mit Beleg, der nicht durch `check_claim_support` gelaufen ist
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
- **Kein `date`, `lastmod`, `tags`, `agent_verified`** — das ist nur für Artikel-Kommentare (`art-{NNN}/_index.md`)!
- **Weight** bestimmt die Reihenfolge im Menü (OR=1, StPO=2, BewG=3, EMRK=4, ZGB=5, etc.)
- **Description** sollte die SR-Nummer und Rechtsgebiet kurz nennen
- **Link auf Fedlex** (wenn die Datei die offizielle Norm enthält)

---

# TEIL D — BELEGPRÜFUNG UND QUALITÄTSKONTROLLE

Ein Kommentar ist nicht dadurch belegt, dass er Entscheide zitiert, sondern dadurch, dass die
zitierten Entscheide die Sätze tragen, für die sie stehen. Die Prüfeinheit ist deshalb das
**Paar (Behauptungssatz, Beleg)**, nie das Zitat für sich.

Zwei Kontrollpunkte, beide obligatorisch:

| | Wann | Tool | Fragt |
|---|---|---|---|
| **D.1 Belegprüfung** | **vor** dem Schreiben, pro Paar | `check_claim_support` | Trägt dieser Entscheid diesen Satz? |
| **D.3 Schlussattest** | **nach** dem Schreiben, pro Abschnitt | `attest_response` | Existiert alles Zitierte, stimmen Pinpoints, Verbatim, Daten — und stützt jeder Beleg seinen Satz? |

Die Reihenfolge ist Absicht. `check_claim_support` einzeln und früh verhindert, dass ein
falscher Beleg überhaupt in den Text kommt; `attest_response` am Schluss fängt, was beim
Schreiben entstanden ist — umgestellte Sätze, verrutschte Belege, aus dem Gedächtnis
ergänzte Zitate. Als Eingangsprüfung liefert `attest_response` nur eine unsortierte
Mängelliste, als Ausgangsprüfung ein belastbares `ok`.

---

## D.1 — Belegprüfung vor dem Schreiben (`check_claim_support`)

Für **jedes** Paar aus geplanter Aussage und Beleg, bevor der Satz geschrieben wird:

```
check_claim_support: {
  "claim": "{der Satz, den der Kommentar behaupten wird — ausformuliert, nicht das Stichwort}",
  "decision_id": "{decision_id aus dem Tool-Ergebnis}",
  "pinpoint": "{E. X.Y, sofern belegt — sonst weglassen}"
}
```

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

**Sparsam einsetzen, wo es nichts bringt**: Für den blossen Gesetzeswortlaut (`get_law`)
und für reine Materialienzitate ist `check_claim_support` nicht das Werkzeug — es prüft
Entscheide. Für Botschaftsstellen `search_botschaft` / `get_materialien` verwenden und
verbatim zitieren.

### Pinpoints (`find_relevant_erwaegung`)

Ein Pinpoint wird **nie geschätzt**. Eine Regeste verweist oft auf «(E. 4)», während die
Erwägung nur als `4.1` / `4.2.1` existiert; `cite` akzeptiert den Verweis trotzdem, und
erst `get_erwaegung` deckt auf, dass er ins Leere zeigt.

```
find_relevant_erwaegung: { "decision_id": "...", "claim": "{Kommentarsatz}", "top_k": 3 }
```

Nur bei Konfidenz `high` übernehmen. Bei `no_match` oder `low`: keinen Pinpoint setzen —
ein Zitat ohne Pinpoint ist korrekt, ein Zitat mit falschem Pinpoint nicht. Der
`highlighted_snippet` liefert zugleich den Satz, den man wörtlich zitieren kann.

Nur Bundesentscheide haben strukturierte Erwägungen; bei kantonalen entfällt der Schritt.

---

## D.2 — Existenz und Wortlaut

Vor dem Schreiben ebenfalls:

- **Jede Zitierung** stammt wörtlich aus `citation_string_de` / `markdown_link` einer
  `cite`- oder Such-Antwort. Nie selbst konstruieren, nie aus dem Gedächtnis ergänzen.
- **Gesetzeswortlaut** verbatim aus `get_law`, mit Konsolidierungsstand.
- **Wörtliche Zitate** (≥ 30 Zeichen) nur aus `get_erwaegung` / `get_regeste` — kopiert,
  nicht nachgeschrieben.

---

## D.3 — Schlussattest (`attest_response`)

Auf dem **fertigen** Text, abschnittsweise (nicht das ganze Bundle auf einmal):

```
attest_response: { "draft_text": "{Abschnitt des Kommentars}", "audit_grounding": true }
```

`audit_grounding: true` ist bei Kommentartext immer zu setzen — er enthält praktisch
nie weniger als zwei Zitierungen. Das Attest prüft fünf Halluzinationsklassen: Existenz
der Entscheide, Auflösbarkeit der Pinpoints, Existenz der Gesetzesartikel,
Verbatim-Treue der Zitate ≥ 30 Zeichen, Übereinstimmung der Entscheiddaten — und mit
`audit_grounding` zusätzlich, ob der jeweils vorangehende Satz durch den Beleg gestützt ist.

Zu attestieren sind **beide** Dateien: `_index.md` und `rechtsprechung.md`. Die
Rechtsprechungsübersicht behauptet in jeder `Kernaussage` etwas über einen Entscheid — sie
ist so belegpflichtig wie der Kommentartext.

Bei `ok: false`: jeden Punkt der `issues`-Liste beheben und erneut attestieren. **Nicht
committen, solange `ok: false` steht.** Beheben heisst je nach Klasse:

| Issue | Behebung |
|---|---|
| Zitierung existiert nicht | Aus `close_matches` korrigieren, wenn der `match_reason` die Identität belegt; sonst Beleg raus |
| Pinpoint löst nicht auf | `find_relevant_erwaegung`; bei `no_match` Pinpoint streichen |
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
| < 50 % | **Nicht committen.** Belegapparat verwerfen, Aussagen behalten, für jede Aussage neu einen Beleg suchen und einzeln über `check_claim_support` prüfen |

---

## D.4 — Checklisten vor dem Commit

**Belegtheit:**
- [ ] Jedes Paar (Aussage, Beleg) durch `check_claim_support` geprüft (D.1)?
- [ ] Kein Beleg mit `no` / `contradicts` / `unrelated` im Text verblieben?
- [ ] `partial`-Aussagen um den Qualifikator ergänzt oder wörtlich zitiert?
- [ ] Jeder Pinpoint durch `get_erwaegung` / `find_relevant_erwaegung` belegt — keiner geschätzt?
- [ ] `attest_response(audit_grounding=true)` auf **beiden** Dateien mit `ok: true` (D.3)?

**Quellenintegrität:**
- [ ] Alle citation_strings aus Tool-Ergebnissen — nicht selbst konstruiert?
- [ ] Gesetzestext verbatim aus `get_law` — nicht aus dem Gedächtnis?
- [ ] Direkte Zitate nur aus `get_erwaegung` oder `get_regeste`?
- [ ] Alle Rechtsquellen (Entscheide, Gesetze, Materialien) auf Originalquelle verlinkt?
- [ ] Unsichere Stellen weggelassen oder als Paraphrase kenntlich gemacht?
- [ ] Literaturzitate als das ausgewiesen, was sie sind: mit den Fall-Tools **nicht**
      verifizierbar — nie als geprüft ausgeben?

**Struktur:**
- [ ] **Gesetzesübersicht vorhanden?** `content/kommentar/{gesetz}/_index.md` mit minimalem Frontmatter (title, weight, description)?
- [ ] Page Bundle korrekt: `art-{NNN}/_index.md` + `art-{NNN}/rechtsprechung.md`?
- [ ] Alle 8 Frontmatter-Felder: `title`, `weight`, `date`, `lastmod`, `description`, `tags`, `agent_verified`, `revisions`?
- [ ] `revisions`-Eintrag in **beiden** Dateien gesetzt (`by`, `model`, `mcp_verified`)?
- [ ] `agent_verified: false` in `rechtsprechung.md`?
- [ ] `agent_verified: true` in `_index.md` (nur nach Verifikation, jüngste Revision `mcp_verified: true`)?

**Inhalt:**
- [ ] Gesetzeswortlaut im Blockquote?
- [ ] Rechtsprechung in absteigender Hierarchie (BGE → BGer → kantonal)?
- [ ] Hugo-Build erfolgreich?

---

## D.5 — Wann `mcp_verified` / `agent_verified` gesetzt werden dürfen

`mcp_verified: true` ist **nur** zulässig, wenn kumulativ:

1. Der Gesetzeswortlaut aus `get_law` stammt,
2. jede Zitierung aus einer Tool-Antwort kopiert ist,
3. jedes Paar (Aussage, Beleg) durch `check_claim_support` gelaufen ist, und
4. `attest_response(audit_grounding=true)` für die Datei `ok: true` liefert.

`agent_verified: true` in `_index.md` setzt zusätzlich voraus, dass **keine offenen
Befunde** verbleiben. Fehlt eine der vier Bedingungen — etwa weil der MCP nicht erreichbar
war oder ein reiner `generate()`-Aufruf den Text erzeugt hat —, dann `mcp_verified: false`
und `agent_verified: false`. Ein Flag ist eine Tatsachenbehauptung über den Prüfvorgang,
kein Gütesiegel: falsch gesetzt ist es schädlicher als weggelassen, weil das nachgelagerte
`/audit` und die PR-Verifikation darauf vertrauen.

Revisionseintrag nach der Prüfung:

```yaml
lastmod: {heute}
revisions:
  - date: {heute}
    by: "Glossagens Agent"
    model: "{exakte Modell-ID}"
    mcp_verified: true
    note: "{was}; Belege via check_claim_support geprüft, attest_response ok"
```

---

## D.6 — Grenzen (im Bericht ausweisen, nicht kaschieren)

- **Literaturzitate.** Die Fall-Tools decken sie nicht ab. `search_scholarship` /
  `find_scholarship_citing_statute` erreichen die OA-Bestände; der klassische
  Kommentarapparat (BSK, ZK, Stämpfli) liegt grösstenteils ausserhalb → Status
  «nicht verifizierbar», nie «korrekt».
- **Botschaften.** `BBl`-Fundstellen prüft `attest_response` nicht; dafür
  `search_botschaft`.
- **Juristische Richtigkeit.** Geprüft wird Belegtheit, nicht Qualität. Ein durchgehend
  belegter Kommentar kann dogmatisch schief sein.
- **Aktualität — der gefährlichste blinde Fleck.** `check_claim_support` beantwortet
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

Belegprüfung (check_claim_support):
  Paare geprüft:  {n}
  gestützt:       {n}      teilweise: {n}
  verworfen:      {n}  ({no}/{contradicts}/{unrelated})
  Belegquote:     {x} %

Pinpoints:        {n} gesetzt, alle via get_erwaegung/find_relevant_erwaegung belegt
Schlussattest:    _index.md {ok|Befunde behoben} · rechtsprechung.md {ok|…}

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
| `get_law` | Gesetzestext verbatim | Immer als erstes |
| `find_leading_cases` | Leitentscheide zu einer Norm | Erstrecherche |
| `find_citations` | Entscheide die Art. zitieren | Breite Abdeckung |
| `search_decisions` | Volltextsuche | Thematische Suche |
| `get_case_brief` | Kurzfassung eines Entscheids | Schnelle Sichtung |
| `get_decision` | Volltext | Vertiefung |
| `get_erwaegung` | Einzelne Erwägung verbatim | Direkte Zitate |
| `get_regeste` | Leitsatz verbatim | Direkte Zitate |
| `list_courts` | Verfügbare Gerichte | Kantonssuche |
| `search_materialien` | Botschaften / Materialien | Entstehungsgeschichte |
| `get_materialien` | Materialien-Volltext | Vertiefung |
| `get_commentary` | OnlineKommentar | Lehrrecherche |
| `get_doctrine` | Lehrmeinungen | Annotationen |
| `cite` | Zitierung auflösen, `close_matches` | Existenz prüfen, Zitierstring holen |
| `find_relevant_erwaegung` | Erwägung zu einer Aussage finden | **Pinpoint statt raten** |
| `check_claim_support` | Trägt der Entscheid die Aussage? | **Vor jedem Beleg** (Teil D.1) |
| `attest_response` | Schlussprüfung des Entwurfs | **Vor jedem Commit** (Teil D.3) |
| `get_article_history` | Revisionen einer Norm | Aktualität alter Belege |

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
- **Falsches Frontmatter in Gesetzesübersicht**: Keine `date`, `lastmod`, `tags`, `agent_verified` — nur `title`, `weight`, `description` (siehe Teil C.5)
- **Page Bundle vs. Flat File**: Immer `art-{NNN}/_index.md` — nie `art-{NNN}.md`
- **rechtsprechung.md**: Liegt im Bundle (`art-{NNN}/rechtsprechung.md`), nicht daneben
- **agent_verified**: In `rechtsprechung.md` immer `false`; in `_index.md` erst nach Verifikation `true` — und nur, wenn die jüngste `revisions`-Zeile `mcp_verified: true` trägt
- **Revisions-Vermerk vergessen**: Bei **jeder** Änderung (auch Neuanlage) muss oben in `revisions:` ein Eintrag mit `by` / `model` / `mcp_verified` ergänzt werden — sonst ist nicht nachvollziehbar, wer mit welchem Modell und mit/ohne MCP-Prüfung gearbeitet hat
- **Citation strings**: Nie selbst konstruieren — immer aus `citation_string_de` des MCP-Tools
- **«Thematisch passend» statt geprüft**: Der häufigste und teuerste Fehler. Ein Entscheid,
  der Stufe «existiert» besteht, kann trotzdem etwas ganz anderes entscheiden — im Bestand
  gab es Artikel, deren sämtliche Belege existierten und **keiner** die Aussage trug.
  `check_claim_support` ist deshalb nicht weglassbar (Teil D.1)
- **Pinpoint geschätzt**: «E. 3.1» ist geraten, wenn es nicht aus `get_erwaegung` oder
  `find_relevant_erwaegung` (Konfidenz `high`) stammt. Regesten verweisen auf «E. 4», wo
  nur `4.1`/`4.2.1` existiert — `cite` merkt das nicht
- **`attest_response` als Eingangsprüfung**: Am Anfang eingesetzt, liefert es nur eine
  unsortierte Mängelliste. Es gehört ans Ende, auf den fertigen Text, mit
  `audit_grounding: true` (Teil D.3)
- **`rechtsprechung.md` ungeprüft gelassen**: Sie behauptet in jeder `Kernaussage` etwas
  über einen Entscheid und ist genauso belegpflichtig wie der Kommentar
- **`mcp_verified: true` als Gütesiegel**: Es ist eine Tatsachenbehauptung über den
  Prüfvorgang (Teil D.5). Falsch gesetzt, richtet es mehr Schaden an als weggelassen —
  `/audit` und die PR-Verifikation vertrauen darauf
- **get_law**: Braucht `abbreviation`, nicht SR-Nummer (obwohl beides funktioniert)
- **StPO vs. StGB**: Nachfragen wenn unklar, beide beginnen mit «St»
- **Remote divergence**: Vor Push immer `git pull --rebase` wenn abgelehnt
