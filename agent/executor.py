import os
import sqlite3
from contextlib import contextmanager
from datetime import datetime

import requests

import github_client as gh

DB_PATH = os.getenv("DB_PATH", "queue.db")
LLM_API_URL = os.getenv("LLM_API_URL", "http://localhost:11434/v1")
LLM_API_KEY = os.getenv("LLM_API_KEY", "")
LLM_MODEL = os.getenv("LLM_MODEL", "hermes3")


@contextmanager
def db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    try:
        yield conn
        conn.commit()
    finally:
        conn.close()


# ── LLM ──────────────────────────────────────────────────────────────────────

def generate(system: str, user: str) -> str:
    resp = requests.post(
        f"{LLM_API_URL}/chat/completions",
        headers={"Authorization": f"Bearer {LLM_API_KEY}"},
        json={
            "model": LLM_MODEL,
            "messages": [
                {"role": "system", "content": system},
                {"role": "user", "content": user},
            ],
            "temperature": 0.3,
        },
        timeout=120,
    )
    resp.raise_for_status()
    return resp.json()["choices"][0]["message"]["content"].strip()


# ── Queue-Zustand ─────────────────────────────────────────────────────────────

def _get_item(item_id: int) -> dict | None:
    with db() as conn:
        row = conn.execute("SELECT * FROM queue WHERE id = ?", (item_id,)).fetchone()
    return dict(row) if row else None


def _set_status(item_id: int, status: str, result: str = ""):
    with db() as conn:
        conn.execute(
            "UPDATE queue SET status = ?, result = ? WHERE id = ?",
            (status, result, item_id),
        )


# ── Approve ───────────────────────────────────────────────────────────────────

def approve(item_id: int, instruction: str = "") -> str:
    item = _get_item(item_id)
    if not item:
        return f"Item {item_id} nicht gefunden."
    if item["status"] != "pending":
        return f"Item {item_id} hat Status '{item['status']}', nicht 'pending'."

    _set_status(item_id, "processing")

    try:
        if item["type"] == "issue":
            result = _execute_issue(item, instruction)
        elif item["type"] == "pr":
            result = _execute_pr_merge(item)
        else:
            result = f"Unbekannter Typ: {item['type']}"

        _set_status(item_id, "executed", result)
        return result

    except Exception as e:
        _set_status(item_id, "error", str(e))
        raise


def _execute_issue(item: dict, instruction: str) -> str:
    """Analysiert Issue, erstellt Artikeländerung als PR (Page Bundle)."""
    import re
    title = item["title"]
    body = item["body"]
    issue_nr = item["github_id"]

    system_prompt = """Du bist ein juristischer Redaktor für einen öffentlichen Gesetzeskommentar (Glossagens).
Du erstellst und aktualisierst Kommentare zu Schweizer Gesetzesartikeln im Markdown-Format.
Artikel werden als Hugo Page Bundles gespeichert: content/kommentar/{gesetz}/art-{NNN}/_index.md
Schreibe präzise, quellenbasiert und im Stil eines akademischen Kommentars.
Verwende keine erfundenen Zitate. Neue Rechtsprechungshinweise nur als Paraphrase mit Vorbehalt."""

    # Versuche bestehenden Artikel zu finden (Page Bundle: art-NNN/_index.md)
    article_path = gh.article_path(title)  # gibt art-NNN/_index.md zurück falls vorhanden
    existing_content = None
    if article_path:
        try:
            existing_content, _ = gh.get_file(article_path)
        except Exception:
            pass

    if existing_content:
        user_prompt = f"""Einreichung #{issue_nr}: {title}

Inhalt der Einreichung:
{body}

Zusätzliche Anweisung: {instruction}

Bestehender Artikeltext:
{existing_content}

Erstelle den aktualisierten Artikeltext mit der eingearbeiteten Änderung. Gib nur den vollständigen Markdown-Text zurück."""
    else:
        user_prompt = f"""Einreichung #{issue_nr}: {title}

Inhalt: {body}
Anweisung: {instruction}

Bestimme das betroffene Gesetz und die Artikelnummer. Erstelle den Kommentartext.
Antworte mit:
PFAD: content/kommentar/<gesetz>/art-<NNN>/_index.md

INHALT:
<markdown>"""

    new_content = generate(system_prompt, user_prompt)

    branch = f"einreichung-{issue_nr}-{datetime.utcnow().strftime('%Y%m%d%H%M%S')}"
    gh.create_branch(branch)

    if article_path:
        index_path = article_path
    else:
        m = re.search(r"PFAD:\s*(content/[^\n]+)", new_content)
        index_path = m.group(1).strip() if m else f"content/kommentar/todo/art-{issue_nr}/_index.md"
        m2 = re.search(r"INHALT:\s*(.+)", new_content, re.DOTALL)
        new_content = m2.group(1).strip() if m2 else new_content

    # Sicherstellen, dass Pfad auf _index.md im Bundle endet
    if not index_path.endswith("/_index.md"):
        # Flat-File-Pfad korrigieren: art-001.md → art-001/_index.md
        index_path = re.sub(r"(art-\d+)\.md$", r"\1/_index.md", index_path)
        index_path = re.sub(r"(art-\d+)/index\.md$", r"\1/_index.md", index_path)

    gh.create_or_update_file(
        path=index_path,
        content=new_content,
        message=f"Einreichung #{issue_nr}: {title}",
        branch=branch,
    )

    # _index.md für neues Gesetz anlegen falls nötig
    law_dir = "/".join(index_path.split("/")[:3])  # content/kommentar/stpo
    law_index_path = f"{law_dir}/_index.md"
    try:
        gh.get_file(law_index_path, branch)
    except Exception:
        law_abbrev = law_dir.split("/")[-1].upper()
        law_content = f"""---
title: "{law_abbrev} — Gesetzestitel"
weight: 1
description: "Bundesgesetz ... (SR ...)"
---

Kommentar zum Bundesgesetz. Tippe auf einen Artikel, um den Kommentar zu öffnen.
"""
        gh.create_or_update_file(
            path=law_index_path,
            content=law_content,
            message=f"Neues Gesetz: {law_abbrev}",
            branch=branch,
        )

    pr_nr = gh.create_pr(
        title=f"Einreichung #{issue_nr}: {title}",
        body=f"Automatisch erstellt aus Issue #{issue_nr}.\n\nOriginal-Einreichung: {item['url']}",
        head=branch,
    )

    gh.comment_issue(issue_nr, f"Deine Einreichung wurde verarbeitet und als [PR #{pr_nr}](https://github.com/{gh.REPO}/pull/{pr_nr}) eingereicht. Sie wird vor Veröffentlichung geprüft.")
    gh.close_issue(issue_nr)

    return f"PR #{pr_nr} erstellt: {index_path}"


def _execute_pr_merge(item: dict) -> str:
    """Merged den PR ohne autonome Verifikation.

    Der Owner entscheidet über PRs direkt (z. B. via Telegram-Chat). `/approve`
    bedeutet hier ausschliesslich: jetzt mergen. Keine LLM-Verifikation, kein
    automatisches Schliessen.
    """
    pr_nr = item["github_id"]
    gh.merge_pr(pr_nr, "Approved by owner")
    return f"PR #{pr_nr} gemerged."


# ── Reject ────────────────────────────────────────────────────────────────────

def reject(item_id: int, reason: str = "") -> str:
    item = _get_item(item_id)
    if not item:
        return f"Item {item_id} nicht gefunden."
    if item["status"] != "pending":
        return f"Item {item_id} hat Status '{item['status']}'."

    _set_status(item_id, "rejected", reason)

    msg = f"Deine Einreichung wurde geprüft und leider nicht aufgenommen."
    if reason:
        msg += f"\n\nGrund: {reason}"

    gh.comment_issue(item["github_id"], msg)
    gh.close_issue(item["github_id"])

    return f"Item {item_id} abgelehnt."
