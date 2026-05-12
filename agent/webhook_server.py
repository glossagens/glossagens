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

    elif x_github_event == "pull_request" and action in ("closed", "merged"):
        # Wenn ein PR auf GitHub geschlossen/gemerged wird, lokale Queue-Zeilen
        # mit derselben github_id als 'executed' markieren, damit sie nicht
        # weiter in /pending auftauchen.
        pr_nr = event["pull_request"]["number"]
        merged = event["pull_request"].get("merged", False)
        with db() as conn:
            conn.execute(
                "UPDATE queue SET status = ?, result = ? "
                "WHERE type = 'pr' AND github_id = ? AND status IN ('pending','processing')",
                ("executed" if merged else "closed", "merged" if merged else "closed on github", pr_nr),
            )
        return {"status": "reconciled", "pr": pr_nr}

    # PRs werden bewusst nicht eingequeued: der Owner entscheidet direkt über
    # PRs (z. B. via Chat) und merged manuell. Issues bleiben der einzige
    # Eingangskanal für die Queue.
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
    """Listet pending Items und reconciled PR-Einträge gegen GitHub.

    PRs, die in der lokalen Queue noch als pending stehen, aber auf GitHub
    bereits gemerged oder geschlossen wurden (z. B. manueller Merge ausserhalb
    des Agents), werden lokal als 'executed'/'closed' markiert und aus der
    Antwort entfernt.
    """
    import github_client as gh

    with db() as conn:
        rows = [dict(r) for r in conn.execute(
            "SELECT * FROM queue WHERE status = 'pending' ORDER BY created_at DESC"
        ).fetchall()]

    still_pending = []
    for item in rows:
        if item["type"] == "pr" and item["github_id"]:
            try:
                st = gh.get_pr_state(item["github_id"])
            except Exception:
                still_pending.append(item)
                continue
            if st["merged"]:
                _mark(item["id"], "executed", "merged on github")
                continue
            if st["state"] == "closed":
                _mark(item["id"], "closed", "closed on github")
                continue
        still_pending.append(item)
    return still_pending


def _mark(item_id: int, status: str, result: str):
    with db() as conn:
        conn.execute(
            "UPDATE queue SET status = ?, result = ? WHERE id = ?",
            (status, result, item_id),
        )


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
