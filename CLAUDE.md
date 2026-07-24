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
    mcp_verified: true            # true nur, wenn Gesetzestexte UND Entscheide via opencaselaw-MCP geprüft
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
    mcp_verified: true            # true nur, wenn alle Entscheide via opencaselaw-MCP geprüft
    note: "kurze Beschreibung der Änderung"   # optional
---
```

### Pflicht: Revisions-Vermerk bei jeder Änderung

**Jede** inhaltliche Änderung an einem Kommentarartikel (`_index.md` **und** `rechtsprechung.md`) — auch die Neuanlage — MUSS als neuer Eintrag **zuoberst** in der `revisions:`-Liste des Frontmatters vermerkt werden. So ist jederzeit nachvollziehbar, wer mit welchem KI-Modell den Beitrag erstellt/geändert hat und ob die Zitate maschinell verifiziert wurden. Pflichtangaben pro Eintrag:

| Feld | Bedeutung |
|------|-----------|
| `date` | Datum der Änderung (`YYYY-MM-DD`) |
| `by` | **Wer** die Änderung vorgenommen hat — Mensch (`"Jonas Achermann"`) oder Agent (`"Claude Code"`, `"Hermes Agent"`) |
| `model` | **Mit welchem KI-Modell** — exakte Modell-ID (z. B. `claude-opus-4-8`, `hermes3`); bei rein manueller Bearbeitung ohne KI: `human` |
| `mcp_verified` | `true` **nur**, wenn **alle** zitierten Gesetzestexte **und** Entscheide über die opencaselaw-MCP verifiziert wurden (`cite` / `get_law` / `get_erwaegung` / `get_regeste`). Andernfalls `false` |
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

## GitHub Secrets

- `HERMES_WEBHOOK_URL` — Endpoint auf dem Hetzner-Server
- `HERMES_API_KEY` — Auth-Token für den Webhook

## Offene nächste Schritte

- [ ] Weitere Gesetze/Artikel befüllen
- [ ] Hugo-Build-Check vor Merge in `_execute_pr_merge` einbauen
