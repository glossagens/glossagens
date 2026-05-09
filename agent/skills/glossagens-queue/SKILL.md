---
name: glossagens-queue
description: Manage the Glossagens legal commentary queue. View, approve, and reject public submissions that arrive via GitHub Issues.
version: 2.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [Glossagens, Legal, GitHub, Queue, Commentary]
---

# Glossagens Queue Management

The Glossagens agent runs on **localhost:8000** (systemd service: `glossagens-agent.service`). The LLM backend is on **localhost:8642** (Open WebUI-compatible endpoint). No auth header is needed — the API is open.

## Key Files

| File | Purpose |
|------|---------|
| `/opt/glossagens/.env` | LLM_API_URL, LLM_API_KEY, LLM_MODEL config |
| `/opt/glossagens/agent/executor.py` | Core approve/reject logic, LLM calls |
| `/opt/glossagens/agent/webhook_server.py` | FastAPI endpoints (/webhook, /pending, /queue, /approve, /reject) |
| `/var/lib/glossagens/queue.db` | SQLite queue database |

## API Endpoints (no auth required)

```
GET  /pending   — list items with status='pending'
GET  /queue     — list all items
POST /approve   — body: {"id": <ID>, "instruction": "<optional>"}
POST /reject    — body: {"id": <ID>, "reason": "<reason>"}
POST /webhook   — GitHub webhook receiver
```

## View Pending Submissions

```bash
curl -s http://localhost:8000/pending | python3 -c "
import sys, json
items = json.load(sys.stdin)
if not items:
    print('Keine offenen Einreichungen.')
else:
    for i in items:
        print(f\"#{i['id']} [{i['type']}] {i['title']}\")
        print(f\"  {i['url']}\")
        print(f\"  {i['body'][:200]}\")
        print()"
```

## Approve a Submission

```bash
# IMPORTANT: LLM generation takes 2-5 minutes. Use -m 360 (6 min timeout).
curl -s -m 360 -X POST \
  -H "Content-Type: application/json" \
  http://localhost:8000/approve \
  -d '{"id": <ID>, "instruction": "<optional instruction>"}'
```

**Timeout pitfall:** The LLM call to generate a legal commentary takes 2-5 minutes. Default curl timeout (120s) will cause "Internal Server Error". Always use `-m 360` or higher.

## Reject a Submission

```bash
curl -s -X POST \
  -H "Content-Type: application/json" \
  http://localhost:8000/reject \
  -d '{"id": <ID>, "reason": "<Begründung>"}'
```

## Queue Overview

```bash
curl -s http://localhost:8000/queue | python3 -c "
import sys, json
from collections import Counter
items = json.load(sys.stdin)
for status, count in Counter(i['status'] for i in items).items():
    print(f'{status}: {count}')"
```

## Troubleshooting

### Timeout on approve — "Internal Server Error" after ~120s
The `requests.post(timeout=300)` in executor.py allows 300s, but uvicorn's `--timeout-keep-alive` default kills the connection at ~120s. Fix:
```bash
# The systemd service already has --timeout-keep-alive 300
# If you see ReadTimeout errors, check:
cat /etc/systemd/system/glossagens-agent.service
# Should have: --timeout-keep-alive 300
# If missing, add it and restart:
systemctl daemon-reload && systemctl restart glossagens-agent.service
```

### Wrong LLM model in .env
If LLM_MODEL doesn't match an available model on the endpoint (port 8642), you get ReadTimeout. Fix:
```bash
# Check available models:
curl -s http://localhost:8642/v1/models | python3 -c "import sys,json; [print(m['id']) for m in json.load(sys.stdin)['data']]"
# Update .env:
# LLM_MODEL=hermes-agent  (must match an available model)
# Then restart:
systemctl restart glossagens-agent.service
```

### Reset a stuck queue item from 'error' back to 'pending'
```python
import sqlite3
conn = sqlite3.connect('/var/lib/glossagens/queue.db')
conn.execute("UPDATE queue SET status='pending', result=NULL WHERE id=<ID>")
conn.commit()
conn.close()
```

### Service Management
```bash
# Check status
systemctl status glossagens-agent.service

# Restart (picks up .env changes)
systemctl restart glossagens-agent.service

# View logs
journalctl -u glossagens-agent.service -f
journalctl -u glossagens-agent.service --since "5 min ago"
```