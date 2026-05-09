---
name: glossagens-content-creation
description: Create and maintain legal commentary articles for the Glossagens Hugo site. Offers three workflows: /kommentar (full creation), /recherche (research only), /loop (iterative gap analysis with subagents).
version: 3.0.0
author: Hermes Agent
tools:
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
- `content/kommentar/{gesetz}/art-{NNN}/index.md` — commentary
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
5. KOMMENTAR schreiben/ergänzen (→ Teil C)
6. QUALITÄTSKONTROLLE (→ Teil D)
7. HUGO BUILD + COMMIT (→ Teil B, Abschnitt 5)

---

## Workflow 2: `/recherche {GESETZ} Art. {N}` — Nur Recherche

Find new decisions and sources and store them in `rechtsprechung.md` — without changing the commentary.

**Steps:**
1. INIT (→ Teil B, Abschnitt 1)
2. RECHERCHE (→ Teil B, Abschnitt 3)
3. RECHTSPRECHUNGSDATEI aktualisieren (→ Teil B, Abschnitt 4)
4. Zusammenfassung der neuen Funde, kein Kommentareingriff

---

## Workflow 3: `/loop {GESETZ} Art. {N}` — Iterative Lückenanalyse

Continuously research which topics and decisions are still **missing** from the existing commentary and integrate them step by step. Runs until no relevant gaps remain or the user stops.

**Each iteration:**

```
┌───────────────────────────────────────────────────────┐
│  LOOP-ITERATION N                                     │
│                                                       │
│  1. BESTANDSAUFNAHME                                  │
│     Lies index.md und rechtsprechung.md               │
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
│  5. INTEGRATION                                       │
│     - Neue Entscheide → rechtsprechung.md             │
│     - Kommentar ergänzen: neue Abschnitte, Kasuistik  │
│                                                       │
│  6. FORTSCHRITTSBERICHT                               │
│     - Welche Lücken bearbeitet?                       │
│     - Welche neuen Entscheide integriert?             │
│     - Welche Lücken verbleiben?                       │
│     - Empfehlung: weitermachen oder beenden?          │
│                                                       │
│  7. KONTEXTMANAGEMENT                                 │
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
- Verbleibende offene Fragen

---

# TEIL B — BASISOPERATIONEN

---

## 1. INIT — Kontext klären

1. **Artikel und Gesetz** aus Benutzeranweisung extrahieren. Bei Mehrdeutigkeit nachfragen.

2. **Pfade ableiten:**
   - Ordner:               `/opt/glossagens/content/kommentar/{gesetz}/art-{NNN}/`
   - Kommentardatei:       `index.md`
   - Rechtsprechungsdatei: `rechtsprechung.md`

3. **Bestandsaufnahme:** Ordner scannen. Bestehende `.md`-Dateien lesen.

4. **BEKANNTE_ENTSCHEIDE-Inventar** erstellen (für Duplikationsvermeidung):
   Alle Urteilsreferenzen aus `index.md` und `rechtsprechung.md` extrahieren:
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
> THEMA: [2–3 Worte]
> KERNAUSSAGE: [2–4 Sätze]
> EINSCHLÄGIG FÜR: [Absatz/Tatbestandsmerkmal]
> STATUS: NEU
> ```
>
> Maximal 15 Ergebnisse. Nur Entscheide melden, die NICHT in der Bekannten-Liste stehen.
> WICHTIG: citation_string_de aus dem Tool-Ergebnis verwenden — nie selbst konstruieren.

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
> GERICHT/KANTON: [Gericht, Kanton]
> THEMA: [2–3 Worte]
> KERNAUSSAGE: [2–4 Sätze]
> STATUS: NEU
> ```

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

---

## 4. RECHTSPRECHUNGSDATEI — Aktualisieren

Öffne oder erstelle `/opt/glossagens/content/kommentar/{gesetz}/art-{NNN}/rechtsprechung.md`.

Nur **neue** Entscheide eintragen (Abgleich mit BEKANNTE_ENTSCHEIDE):

```markdown
---
title: "Rechtsprechung zu Art. {N} {ABBREV}"
weight: 99
date: {YYYY-MM-DD}
lastmod: {YYYY-MM-DD}
description: "Übersicht der Entscheide zu Art. {N} {ABBREV} – {Kurztitel}"
tags: ["Rechtsprechung", "{ABBREV}", "{topic1}"]
agent_verified: false
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

## Frontmatter `index.md`

```yaml
---
title: "Art. {N} — {Kurztitel}"
weight: {N}
date: {YYYY-MM-DD}
lastmod: {YYYY-MM-DD}
description: "Kommentar zu Art. {N} {ABBREV} – {Kurztitel}"
tags: ["{ABBREV}", "{topic1}", "{topic2}"]
agent_verified: true
---
```

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

---

# TEIL D — QUALITÄTSKONTROLLE

Vor jedem Commit durchlaufen:

**Quellenintegrität:**
- [ ] Alle citation_strings aus Tool-Ergebnissen — nicht selbst konstruiert?
- [ ] Gesetzestext verbatim aus `get_law` — nicht aus dem Gedächtnis?
- [ ] Direkte Zitate nur aus `get_erwaegung` oder `get_regeste`?
- [ ] Unsichere Stellen weggelassen oder als Paraphrase kenntlich gemacht?

**Struktur:**
- [ ] Page Bundle korrekt: `art-{NNN}/index.md` + `art-{NNN}/rechtsprechung.md`?
- [ ] Alle 7 Frontmatter-Felder: `title`, `weight`, `date`, `lastmod`, `description`, `tags`, `agent_verified`?
- [ ] `agent_verified: false` in `rechtsprechung.md`?
- [ ] `agent_verified: true` in `index.md` (nur nach Verifikation)?

**Inhalt:**
- [ ] Gesetzeswortlaut im Blockquote?
- [ ] Rechtsprechung in absteigender Hierarchie (BGE → BGer → kantonal)?
- [ ] Hugo-Build erfolgreich?

**Abschlussbericht** an Benutzer:
```
KOMMENTAR-STATUS: {ABBREV} Art. {N}
────────────────────────────────────
Bearbeitete Dateien:
  - index.md [erstellt / ergänzt]
  - rechtsprechung.md [erstellt / ergänzt]

Neue Entscheide integriert:
  - BGE: {Anzahl}
  - BGer: {Anzahl}
  - Kantonal: {Anzahl}
  - EGMR: {Anzahl}

Offene Fragen: {Kurzbeschreibung oder «keine»}

Aktualisierungsdatum: {DATUM}
```

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

- **Page Bundle vs. Flat File**: Immer `art-{NNN}/index.md` — nie `art-{NNN}.md`
- **rechtsprechung.md**: Liegt im Bundle (`art-{NNN}/rechtsprechung.md`), nicht daneben
- **agent_verified**: In `rechtsprechung.md` immer `false`; in `index.md` erst nach Verifikation `true`
- **Citation strings**: Nie selbst konstruieren — immer aus `citation_string_de` des MCP-Tools
- **get_law**: Braucht `abbreviation`, nicht SR-Nummer (obwohl beides funktioniert)
- **StPO vs. StGB**: Nachfragen wenn unklar, beide beginnen mit «St»
- **Remote divergence**: Vor Push immer `git pull --rebase` wenn abgelehnt
