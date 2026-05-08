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

```
Öffentliche Einreichung (GitHub Issue)
        ↓
Hermes Agent (Hetzner) empfängt Webhook
        ↓
LLM-Analyse via externer API (Nous-Hermes)
        ↓
Agent erstellt PR gegen main
        ↓
verify-pr.yml triggert Verifikations-Webhook
        ↓
bei Bestehen: Merge → GitHub Pages Deploy
bei Ablehnung: PR-Kommentar + Schliessen
```

### Content-Struktur

```
content/
├── kommentar/{gesetz}/art-{nr}.md   ← Kommentarseiten
├── einreichung/_index.md             ← Einreichungsformular
└── ueber/_index.md                   ← Projektbeschreibung

pending/                              ← Zwischenlager für ungeprüfte Einreichungen
.github/
├── workflows/deploy.yml              ← GitHub Pages Deploy
├── workflows/verify-pr.yml           ← Webhook an Hermes bei PR
└── ISSUE_TEMPLATE/anregung.yml       ← Strukturiertes Issue-Formular
```

### Frontmatter-Schema pro Kommentarartikel

```yaml
---
title: "Art. X — Kurztitel"
weight: X
date: YYYY-MM-DD
lastmod: YYYY-MM-DD
description: "..."
tags: ["...", "..."]
agent_verified: true   # nur nach Verifikation durch Hermes
---
```

## GitHub Secrets (noch zu setzen)

- `HERMES_WEBHOOK_URL` — Endpoint auf dem Hetzner-Server
- `HERMES_API_KEY` — Auth-Token für den Webhook

## Offene nächste Schritte

- [ ] GitHub Repo erstellen (`glossagens/glossagens`)
- [ ] GitHub Pages aktivieren (Settings → Pages → Source: GitHub Actions)
- [ ] Secrets setzen
- [ ] Webhook-Endpoint auf Hetzner implementieren
- [ ] Weitere Gesetze/Artikel befüllen
