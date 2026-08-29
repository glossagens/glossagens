# Glossagens — Öffentlicher Juristischer Gesetzeskommentar

## Projektidee

Glossagens ist ein öffentlicher, juristisch fundierter Gesetzeskommentar, der durch einen autonomen Agenten erstellt und gepflegt wird. Jeder kann Artikel bearbeiten (Wiki-Stil), aber Bearbeitungen werden vor Veröffentlichung durch den Agenten verifiziert. Die Öffentlichkeit kann anonym Anregungen und Aufträge einreichen, die der Agent selbständig umsetzt.

## Architektur

### Stack

| Schicht | Technologie |
|---------|-------------|
| Frontend | Hugo + Hextra-Theme → GitHub Pages |
| Content | Markdown-Dateien im GitHub-Repo |
| Deployment | GitHub Actions (auto-deploy bei Push auf `main`) |
| Verifikationspipeline | GitHub Actions Webhook → Hermes Agent |
| Öffentliche Einreichungen | GitHub Issues (strukturiertes Formular) |
| Agent-Hosting | Externer Hetzner-Server mit Nous-Hermes via externer LLM-API |

### Datenfluss

Zwei Eingangskanäle — beide landen in derselben Queue:

```
Kanal A: Anregung (GitHub Issue)          Kanal B: Fertiger Beitrag (Pull Request)
         ↓                                          ↓
Hermes Agent empfängt Webhook             Hermes Agent empfängt Webhook
         ↓                                          ↓
LLM generiert Kommentartext               Strukturprüfung (Page Bundle, Frontmatter)
         ↓                                          ↓
Agent erstellt PR gegen main              LLM-Qualitätsprüfung (Inhalt, Zitate)
         ↓                                          ↓
verify-pr.yml triggert Verifikations-     bei Bestehen: Merge
Webhook                                   bei Ablehnung: PR-Kommentar + Schliessen
         ↓
bei Bestehen: Merge → GitHub Pages Deploy
bei Ablehnung: PR-Kommentar + Schliessen
```

**Kanal A (Issue)**: Für Anregungen — der Agent generiert den Inhalt selbständig.  
**Kanal B (PR)**: Für fertige Beiträge von Menschen oder externen Agenten — der Agent verifiziert nur, generiert nichts.

### Content-Struktur

Artikel werden als **Hugo Page Bundles** angelegt (nicht als Flat-Files):

```
content/
├── kommentar/{gesetz}/
│   ├── _index.md                     ← Gesetzesübersicht
│   └── art-{nr}/                     ← Page Bundle pro Artikel
│       ├── _index.md                 ← Hauptkommentar (Branch Bundle, nicht index.md!)
│       └── rechtsprechung.md         ← Rechtsprechungsübersicht
├── einreichung/_index.md             ← Einreichungsformular
└── ueber/_index.md                   ← Projektbeschreibung

data/
└── systematik/{gesetz}.yaml          ← Gliederung der Artikelübersicht

agent/
├── executor.py                       ← Issue- und PR-Verarbeitungslogik
├── webhook_server.py                 ← FastAPI-Endpoints (/webhook, /queue, /approve, /reject)
├── github_client.py                  ← GitHub API-Wrapper
├── requirements.txt
├── .env.example
├── glossagens-agent.service          ← systemd-Unit für Hetzner
└── skills/
    ├── glossagens-content-creation/  ← Skill für Hermes: Artikel erstellen
    │   └── SKILL.md
    └── glossagens-queue/             ← Skill für Hermes: Queue verwalten
        └── SKILL.md

static/
└── agent-skill.md                    ← Öffentlicher Contributor-Skill (für externe Agenten)

.github/
├── workflows/deploy.yml              ← GitHub Pages Deploy
├── workflows/verify-pr.yml           ← Webhook an Hermes bei PR
└── ISSUE_TEMPLATE/anregung.yml       ← Strukturiertes Issue-Formular
```

**Wichtig für den Agenten**: Neue Artikel immer als Page Bundle erstellen:
1. Verzeichnis `content/kommentar/{gesetz}/art-{nr}/` anlegen
2. `_index.md` für den Kommentar (Branch Bundle — nicht `index.md`!)
3. `rechtsprechung.md` für die Rechtsprechungsübersicht
4. In **beiden** Dateien einen `revisions`-Eintrag setzen (wer / welches KI-Modell / `mcp_verified`) — Pflicht bei jeder Änderung, siehe Abschnitt „Revisions-Vermerk".

### Frontmatter-Schema — Gesetzesübersicht (`content/kommentar/{gesetz}/_index.md`)

Die Übersicht unter `/kommentar/` wird **vollständig aus diesen Feldern generiert** (`layouts/_partials/kommentar/gesetze-grid.html`) — sie gruppiert nach SR-Sachgruppe und sortiert nach SR-Nummer. Es gibt keine handgepflegte Liste; ein neues Gesetz erscheint automatisch.

```yaml
---
title: "SR 311.0 — StGB — Schweizerisches Strafgesetzbuch"
ebene: bund              # "bund" oder "kantonal"
sr: "311.0"              # Bundesrecht: SR-Nummer ohne Präfix — Pflicht
kuerzel: "StGB"          # Pflicht — steht als Ankertext in der Übersicht
gesetz_name: "Schweizerisches Strafgesetzbuch"   # Pflicht — ohne SR und Kürzel
weight: 17               # Rang in SR-Sortierung; steuert die Sidebar-Reihenfolge
...
---
```

Kantonale Erlasse statt `sr`:

```yaml
ebene: kantonal
kanton: "LU"
srl: "40"                # Nummer der kantonalen Sammlung, nicht SR
```

Regeln:
- `sr` bzw. `srl` ist **zwingend**. Fehlt es, bricht der Hugo-Build mit `errorf` ab — das Gesetz würde sonst lautlos aus der Übersicht verschwinden.
- Die Sachgruppe wird aus der ersten Ziffer der SR-Nummer abgeleitet (`0.101` → Gruppe 0, `311.0` → Gruppe 3). Nichts von Hand zuordnen.
- `weight` beim Anlegen eines neuen Gesetzes so setzen, dass die Sidebar der SR-Reihenfolge folgt (Weights der Nachbargesetze prüfen).
- Der Body enthält **nur** den Einleitungssatz mit Fedlex-Link. Die Artikelliste rendert `articles.html` automatisch — **keine** Artikelliste oder -tabelle von Hand pflegen.

### Systematik-Gliederung (`data/systematik/{gesetz}.yaml`)

Gliedert die Artikelübersicht einer Gesetzesseite nach der Systematik des Erlasses. Optional: fehlt die Datei, wird flach gerendert.

```yaml
gruppen:
  - name: "Besondere Bestimmungen — Strafbare Handlungen gegen Leib und Leben"
    von: 111
    bis: 136
  - name: "Strafbefehlsverfahren"    # Untergruppe der vorangehenden Gruppe
    von: 352
    bis: 357
    ebene: 2
```

Regeln:
- Die Zuordnung erfolgt über die Artikelnummer im **Verzeichnisnamen** (`art-305bis` → 305), nicht über `weight`.
- Ein Artikel landet in der **engsten** passenden Gruppe. Untergruppen (`ebene: 2`) dürfen sich deshalb mit ihrer Oberkategorie überschneiden, ohne dass Artikel doppelt erscheinen.
- Eine Oberkategorie ohne eigene Artikel wird trotzdem angezeigt, wenn ihre Untergruppen Artikel tragen.
- Artikel, die in keine Gruppe fallen, erscheinen unter „Weitere Artikel". Das ist kein Fehler, sondern der Hinweis, dass ein Bereich fehlt — die Liste bleibt in jedem Fall vollständig.
- Gruppen ohne kommentierte Artikel werden stillschweigend übersprungen; die Datei darf die vollständige Systematik des Erlasses abbilden.

### Reihenfolge der Artikel: nicht über `weight`

Sortierung und Artikelnummer stammen ausschliesslich aus dem Verzeichnisnamen (`art-024bis`). `weight` ist dafür unbrauchbar: die Werte kollidieren (`art-305` und `art-305bis` tragen beide 305), fehlen teils ganz (OHG) und sind stellenweise falsch (StGB Art. 47 trug `weight: 1`, RPG behalf sich für Art. 24a–24d mit 241–244).

Der Slug ist dreistellig genullt; seine lexikografische Ordnung entspricht der Reihenfolge auf Fedlex — dort steht `24, 24a, 24b, 24bis, 24c, 24d, 24e, 24f, 24quater, 24quinquies, 24ter`. Beim Anlegen eines Artikels also **immer** dreistellig benennen: `art-007`, nicht `art-7`.

### Frontmatter-Schema — Kommentarartikel (`_index.md`)

```yaml
---
title: "Art. X — Kurztitel"
weight: X
date: YYYY-MM-DD
lastmod: YYYY-MM-DD
description: "..."
tags: ["...", "..."]
agent_verified: true   # nur nach Verifikation; nur zulässig, wenn jüngste Revision mcp_verified: true
revisions:             # Pflicht — neuester Eintrag zuoberst (siehe Abschnitt „Revisions-Vermerk")
  - date: YYYY-MM-DD
    by: "Name des Bearbeiters"    # Mensch oder Agent, z. B. "Claude Code", "Hermes Agent", "Jonas Achermann"
    model: "claude-opus-4-8"      # exakte KI-Modell-ID; "human" bei rein manueller Bearbeitung
    mcp_verified: true            # true nur, wenn Gesetzestexte (Fedlex) UND Entscheide (entscheidsuche/opencaselaw) geprüft
    note: "kurze Beschreibung der Änderung"   # optional
---
```

### Frontmatter-Schema — Rechtsprechungsseite (`rechtsprechung.md`)

```yaml
---
title: "Rechtsprechung zu Art. X Gesetz"
weight: 99
date: YYYY-MM-DD
lastmod: YYYY-MM-DD
description: "Übersicht der Entscheide zu Art. X ..."
tags: ["Rechtsprechung", ...]
agent_verified: false  # wird separat verifiziert
revisions:             # Pflicht — neuester Eintrag zuoberst (siehe Abschnitt „Revisions-Vermerk")
  - date: YYYY-MM-DD
    by: "Name des Bearbeiters"
    model: "claude-opus-4-8"      # exakte KI-Modell-ID; "human" bei rein manueller Bearbeitung
    mcp_verified: true            # true nur, wenn alle Entscheide via entscheidsuche/opencaselaw geprüft
    note: "kurze Beschreibung der Änderung"   # optional
---
```

### Quellen für Gesetzeswortlaute: Fedlex zuerst, opencaselaw nur als Rückfall

Der **authentische Normtext** kommt aus der **Fedlex-MCP** — sie ist die amtliche Quelle und
unabhängig von der Verfügbarkeit von opencaselaw:

| Zweck | Aufruf |
|---|---|
| Einzelner Artikel | `mcp__fedlex-connector__get_article` (`rs_number`, `article`, optional `date`) |
| Ganzer Erlass / Abschnitt | `mcp__fedlex-connector__get_law_text` |
| SR-Nummer unbekannt | `mcp__fedlex-connector__search_by_title` |
| Änderungshistorie | `mcp__fedlex-connector__list_amendments` |

`get_law` der opencaselaw-MCP ist **nur Rückfallebene** — zu verwenden, wenn Fedlex die Norm nicht
liefert, praktisch also bei **kantonalem Recht** (Fedlex führt nur Bundesrecht). Wird auf den
Rückfall ausgewichen, gehört das in die `note` des Revisionseintrags.

Grund: Am 23.08.2026 wurde der Glossagens-Client von opencaselaw per IP gesperrt (HTTP 403 auf
alles). Seither scheitert jede Prüfung, die den Normtext von dort holt — `audit.py` meldet Stufe 1
seither `nicht_verifizierbar`. Fedlex war davon nie betroffen. Für **Entscheide** bleibt es bei
opencaselaw bzw. **entscheidsuche** als gleichwertigem Weg; nur der Gesetzestext wandert zu Fedlex.

Unverändert gilt: **Nie** einen Gesetzeswortlaut aus dem Gedächtnis schreiben.

### Verlinkung von Entscheiden: entscheidsuche.ch zuerst, opencaselaw nur als Rückfall

Jeder im Text zitierte Entscheid wird **auf entscheidsuche.ch verlinkt**, soweit dort ein Dokument
vorliegt. `mcp.opencaselaw.ch/entscheid/...` ist nur noch **Rückfallebene** — zulässig, wenn
entscheidsuche den Entscheid nicht führt (kommt bei älteren kantonalen Entscheiden und bei
EGMR-Urteilen vor).

Grund: entscheidsuche.ch ist die etablierte, offen zugängliche Publikationsplattform der Schweizer
Gerichte; ihre Dokument-URLs sind stabil und für Leserinnen und Leser ohne Umweg über einen
MCP-Server erreichbar. opencaselaw bleibt als Rechercheinstrument massgebend — nur das *Linkziel*
wechselt.

**Die URL wird nie von Hand konstruiert.** Sie enthält eine nicht ableitbare Sammlungsnummer
(`CH_BGE_005_…`) und wird deshalb **verbatim** aus dem Feld `document_url` einer Antwort von
`mcp__entscheidsuche__search_by_case_number` bzw. `mcp__entscheidsuche__search` übernommen:

```
BGE  → https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_005_BGE-144-III-519_2018.html
BGer → https://entscheidsuche.ch/docs/CH_BGer/CH_BGer_004_4A-466-2020_2021-02-10.html
```

Regeln:
- **Pinpoint als Anker**: HTML-Dokumente tragen `id="consideration_{E-Nr}"`. Der Link auf eine
  Erwägung lautet also `…_2018.html#consideration_5.2.1`. Den Anker nur anhängen, wenn die
  Erwägungsnummer im Dokument tatsächlich vorkommt — sonst ohne Anker verlinken.
- **PDF-Dokumente** (`is_pdf: true`, viele kantonale Entscheide) haben keine Anker: ohne `#`
  verlinken, der Pinpoint steht dann nur im Zitattext.
- Findet `search_by_case_number` den Entscheid nicht, gilt der Rückfall auf
  `https://mcp.opencaselaw.ch/entscheid/{decision_id}`. Kein Vermerk nötig; die inhaltliche
  Verifikation des Entscheids bleibt davon unberührt.
- Die Entscheidung gilt **nur für die Zukunft**: neue und überarbeitete Kommentare. Bestehende
  opencaselaw-Links werden nicht migriert — sie funktionieren weiter. Wer ohnehin einen Abschnitt
  überarbeitet, darf die dortigen Links mitziehen, muss aber nicht.

### Pflicht: Revisions-Vermerk bei jeder Änderung

**Jede** inhaltliche Änderung an einem Kommentarartikel (`_index.md` **und** `rechtsprechung.md`) — auch die Neuanlage — MUSS als neuer Eintrag **zuoberst** in der `revisions:`-Liste des Frontmatters vermerkt werden. So ist jederzeit nachvollziehbar, wer mit welchem KI-Modell den Beitrag erstellt/geändert hat und ob die Zitate maschinell verifiziert wurden. Pflichtangaben pro Eintrag:

| Feld | Bedeutung |
|------|-----------|
| `date` | Datum der Änderung (`YYYY-MM-DD`) |
| `by` | **Wer** die Änderung vorgenommen hat — Mensch (`"Jonas Achermann"`) oder Agent (`"Claude Code"`, `"Hermes Agent"`) |
| `model` | **Mit welchem KI-Modell** — exakte Modell-ID (z. B. `claude-opus-4-8`, `hermes3`); bei rein manueller Bearbeitung ohne KI: `human` |
| `mcp_verified` | `true` **nur**, wenn **alle** zitierten Gesetzestexte **und** Entscheide maschinell verifiziert wurden — Gesetzestexte über die **Fedlex-MCP**, Entscheide über entscheidsuche (`search_by_case_number` / `fetch_document`) oder opencaselaw (`cite` / `get_erwaegung` / `get_regeste`). Andernfalls `false` (siehe „Quellen für Gesetzeswortlaute" und „Verlinkung von Entscheiden") |
| `note` | optional — kurze Beschreibung der Änderung |

Regeln:
- Neuester Eintrag **zuoberst**; ältere Einträge bleiben erhalten (Historie, nicht überschreiben).
- `agent_verified: true` darf **nur** gesetzt werden, wenn die jüngste Revision `mcp_verified: true` trägt. Ein von einem LLM ohne MCP-Zugang (z. B. reiner Hermes-`generate()`-Aufruf) erzeugter Text ist niemals `agent_verified: true` — er trägt `mcp_verified: false`.
- Fehlt der `revisions`-Block bei einem eingereichten PR, ist das ein Strukturfehler (siehe „PR-Verifikation").

## PR-Verifikation durch Hermes

Wenn ein externer PR eintrifft, prüft `executor.py` zweistufig:

1. **Strukturprüfung** (automatisch, kein LLM):
   - Kein Flat-File (`art-001.md`) — nur Page Bundle (`art-001/_index.md`)
   - Alle 8 Pflichtfelder im Frontmatter: `title`, `weight`, `date`, `lastmod`, `description`, `tags`, `agent_verified`, `revisions`
   - `revisions` enthält mindestens einen Eintrag mit `date`, `by`, `model`, `mcp_verified`

2. **Inhaltsprüfung** (LLM):
   - Sachliche Korrektheit, keine erfundenen Zitate
   - Akademischer Zitierstil
   - Kohärenz mit bestehendem Kontext

Bei Strukturfehler: sofortiger Reject ohne LLM-Call.  
Bei Bestehen beider Stufen: automatischer Merge + Deploy.

## Build-Check vor dem Push

Ein fehlerhaftes Template bricht **den gesamten** Hugo-Build ab, nicht nur die betroffene Seite — der Deploy bleibt dann rot und die veröffentlichte Seite altert stillschweigend vor sich hin (11.–12.08.2026: sieben Commits lang unbemerkt, weil GitHub standardmässig nur bei Fehlschlägen mailt).

Absicherung:

- `.hugo-version` ist die **einzige** Stelle, an der die Hugo-Version steht. `deploy.yml` liest sie, `scripts/build-check.sh` vergleicht die lokale Installation dagegen und warnt bei Abweichung. Die Versionen müssen übereinstimmen: Der Auslöser des Ausfalls war ein Template-Ausdruck, der unter 0.147.4 (CI) anders auswertete als unter 0.161.1 (lokal) — lokal grün, in CI Cast-Fehler.
- Der Check bricht ab, wenn der **Submodul-Stand** (`themes/hextra`) von dem im Parent-Repo aufgezeichneten Commit abweicht. Der Runner checkt den aufgezeichneten Commit aus — weicht der lokale ab, prüft der Build lokal ein anderes Theme als die CI baut. Am 17.08.2026 der Auslöser dreier roter Deploys: aufgezeichnet war hextra `c9feec7`, ausgecheckt `38d18a5`; der Projekt-Override `layouts/_partials/toc.html` ruft `utils/headings.html` auf, das es erst im neueren Stand gibt. Beheben mit `git add themes/hextra && git commit`. Theme-Anpassungen gehören nie ins Submodul, sondern nach `layouts/` — das überschreibt `themes/`.
- `.githooks/pre-push` baut vor jedem Push, der `content/`, `layouts/`, `data/`, `assets/`, `i18n/`, `static/`, `themes/`, `archetypes/`, `hugo.toml` oder `.hugo-version` berührt (~30 s); andere Pushes laufen ungebremst durch. Einmalig pro Klon zu aktivieren: `git config core.hooksPath .githooks`.
- Manuell: `make build-check` bzw. `./scripts/build-check.sh`. Notausgang: `git push --no-verify`.

Beim Anheben der Hugo-Version genügt es, `.hugo-version` zu ändern; CI zieht automatisch nach.

## GitHub Secrets

- `HERMES_WEBHOOK_URL` — Endpoint auf dem Hetzner-Server
- `HERMES_API_KEY` — Auth-Token für den Webhook

## Offene nächste Schritte

- [ ] Weitere Gesetze/Artikel befüllen
- [x] Handgepflegte Artikellisten aus den Bodies entfernt; Systematik nach `data/systematik/` überführt
- [x] Hugo-Build-Check vor Merge in `_execute_pr_merge` einbauen
