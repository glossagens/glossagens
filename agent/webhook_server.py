import hashlib
import hmac
import json
import os
import smtplib
import sqlite3
from contextlib import contextmanager
from datetime import datetime
from email.mime.text import MIMEText

from fastapi import FastAPI, Header, HTTPException, Request

app = FastAPI()

DB_PATH = os.getenv("DB_PATH", "queue.db")
WEBHOOK_SECRET = os.getenv("WEBHOOK_SECRET", "")
OWNER_EMAIL = os.getenv("OWNER_EMAIL", "")
SMTP_HOST = os.getenv("SMTP_HOST", "")
SMTP_PORT = int(os.getenv("SMTP_PORT", "587"))
SMTP_USER = os.getenv("SMTP_USER", "")
SMTP_PASS = os.getenv("SMTP_PASS", "")


@contextmanager
def db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    try:
        yield conn
        conn.commit()
    finally:
        conn.close()


def init_db():
    with db() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS queue (
                id          INTEGER PRIMARY KEY AUTOINCREMENT,
                created_at  TEXT NOT NULL,
                type        TEXT NOT NULL,
                github_id   INTEGER,
                title       TEXT,
                body        TEXT,
                url         TEXT,
                status      TEXT NOT NULL DEFAULT 'pending',
                result      TEXT
            )
        """)


def verify_signature(payload: bytes, signature: str) -> bool:
    if not WEBHOOK_SECRET:
        return True
    expected = "sha256=" + hmac.new(
        WEBHOOK_SECRET.encode(), payload, hashlib.sha256
    ).hexdigest()
    return hmac.compare_digest(expected, signature)


def send_email(subject: str, body: str):
    if not all([SMTP_HOST, SMTP_USER, SMTP_PASS, OWNER_EMAIL]):
        return
    msg = MIMEText(body, "plain", "utf-8")
    msg["Subject"] = f"[Glossagens] {subject}"
    msg["From"] = SMTP_USER
    msg["To"] = OWNER_EMAIL
    with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as s:
        s.starttls()
        s.login(SMTP_USER, SMTP_PASS)
        s.send_message(msg)


@app.on_event("startup")
def startup():
    init_db()


@app.post("/webhook")
async def github_webhook(
    request: Request,
    x_hub_signature_256: str = Header(default=""),
    x_github_event: str = Header(default=""),
):
    payload = await request.body()

    if not verify_signature(payload, x_hub_signature_256):
        raise HTTPException(status_code=401, detail="Invalid signature")

    event = json.loads(payload)
    action = event.get("action", "")

    # Nur relevante Events verarbeiten
    if x_github_event == "issues" and action == "opened":
        labels = [l["name"] for l in event["issue"].get("labels", [])]
        if "anregung" not in labels and "pending-review" not in labels:
            return {"status": "ignored"}

        item_id = _enqueue(
            type_="issue",
            github_id=event["issue"]["number"],
            title=event["issue"]["title"],
            body=event["issue"]["body"] or "",
            url=event["issue"]["html_url"],
        )
        send_email(
            subject=f"Neue Einreichung #{item_id}: {event['issue']['title']}",
            body=(
                f"Neue Einreichung in der Glossagens-Queue:\n\n"
                f"Titel: {event['issue']['title']}\n"
                f"URL:   {event['issue']['html_url']}\n\n"
                f"Inhalt:\n{event['issue']['body']}\n\n"
                f"---\n"
                f"Freigeben: approve {item_id}\n"
                f"Ablehnen:  reject {item_id} <Begründung>"
            ),
        )
        return {"status": "queued", "id": item_id}

    elif x_github_event == "pull_request" and action == "opened":
        item_id = _enqueue(
            type_="pr",
            github_id=event["pull_request"]["number"],
            title=event["pull_request"]["title"],
            body=event["pull_request"]["body"] or "",
            url=event["pull_request"]["html_url"],
        )
        send_email(
            subject=f"Neuer PR #{item_id}: {event['pull_request']['title']}",
            body=(
                f"Neuer Pull Request zur Verifikation:\n\n"
                f"Titel: {event['pull_request']['title']}\n"
                f"URL:   {event['pull_request']['html_url']}\n\n"
                f"Freigeben: approve {item_id}\n"
                f"Ablehnen:  reject {item_id} <Begründung>"
            ),
        )
        return {"status": "queued", "id": item_id}

    return {"status": "ignored"}


def _enqueue(type_: str, github_id: int, title: str, body: str, url: str) -> int:
    with db() as conn:
        cur = conn.execute(
            "INSERT INTO queue (created_at, type, github_id, title, body, url) VALUES (?,?,?,?,?,?)",
            (datetime.utcnow().isoformat(), type_, github_id, title, body, url),
        )
        return cur.lastrowid


@app.get("/pending")
def list_pending():
    with db() as conn:
        rows = conn.execute(
            "SELECT * FROM queue WHERE status = 'pending' ORDER BY created_at DESC"
        ).fetchall()
    return [dict(r) for r in rows]


@app.get("/queue")
def list_all():
    with db() as conn:
        rows = conn.execute(
            "SELECT * FROM queue ORDER BY created_at DESC LIMIT 50"
        ).fetchall()
    return [dict(r) for r in rows]


@app.post("/approve")
async def approve_item(request: Request):
    from executor import approve
    body = await request.json()
    item_id = body.get("id")
    instruction = body.get("instruction", "")
    if not item_id:
        raise HTTPException(status_code=400, detail="id fehlt")
    result = approve(item_id, instruction)
    return {"result": result}


@app.post("/reject")
async def reject_item(request: Request):
    from executor import reject
    body = await request.json()
    item_id = body.get("id")
    reason = body.get("reason", "")
    if not item_id:
        raise HTTPException(status_code=400, detail="id fehlt")
    result = reject(item_id, reason)
    return {"result": result}
