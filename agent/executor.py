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
Artikel werden als Hugo Page Bundles gespeichert: content/kommentar/{gesetz}/art-{NNN}/index.md
Schreibe präzise, quellenbasiert und im Stil eines akademischen Kommentars.
Verwende keine erfundenen Zitate. Neue Rechtsprechungshinweise nur als Paraphrase mit Vorbehalt."""

    # Versuche bestehenden Artikel zu finden (Page Bundle: art-NNN/index.md)
    article_path = gh.article_path(title)  # gibt art-NNN/index.md zurück falls vorhanden
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
PFAD: content/kommentar/<gesetz>/art-<NNN>/index.md

INHALT:
<markdown>"""

    new_content = generate(system_prompt, user_prompt)

    branch = f"einreichung-{issue_nr}-{datetime.utcnow().strftime('%Y%m%d%H%M%S')}"
    gh.create_branch(branch)

    if article_path:
        index_path = article_path
    else:
        m = re.search(r"PFAD:\s*(content/[^\n]+)", new_content)
        index_path = m.group(1).strip() if m else f"content/kommentar/todo/art-{issue_nr}/index.md"
        m2 = re.search(r"INHALT:\s*(.+)", new_content, re.DOTALL)
        new_content = m2.group(1).strip() if m2 else new_content

    # Sicherstellen, dass Pfad auf index.md im Bundle endet
    if not index_path.endswith("/index.md"):
        # Flat-File-Pfad korrigieren: art-001.md → art-001/index.md
        index_path = re.sub(r"(art-\d+)\.md$", r"\1/index.md", index_path)

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
        law_name = law_dir.split("/")[-1].upper()
        gh.create_or_update_file(
            path=law_index_path,
            content=f"---\ntitle: {law_name}\nweight: 1\n---\n",
            message=f"Neues Gesetz: {law_name}",
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


def _verify_pr_structure(diff: str) -> list[str]:
    """Prüft Page-Bundle-Struktur im Diff. Gibt Liste von Fehlern zurück."""
    import re
    errors = []

    added_files = re.findall(r"^\+\+\+ b/(content/kommentar/.+)$", diff, re.MULTILINE)

    for path in added_files:
        # Neue Artikel müssen als Page Bundle vorliegen: .../art-NNN/index.md
        if re.search(r"/art-\d+\.md$", path):
            errors.append(f"Flat-File statt Page Bundle: {path} → sollte {path[:-3]}/index.md sein")
        # Frontmatter-Pflichtfelder prüfen (nur für index.md)
        if path.endswith("/index.md"):
            file_section = re.search(
                rf"\+\+\+ b/{re.escape(path)}.+?(?=\ndiff |\Z)", diff, re.DOTALL
            )
            if file_section:
                added_lines = "\n".join(
                    l[1:] for l in file_section.group().splitlines() if l.startswith("+")
                )
                for field in ["title:", "weight:", "date:", "lastmod:", "description:", "tags:", "agent_verified:"]:
                    if field not in added_lines:
                        errors.append(f"Fehlendes Frontmatter-Feld '{field}' in {path}")

    return errors


def _execute_pr_merge(item: dict) -> str:
    """Verifiziert PR-Inhalt (Struktur + Qualität) und merged bei Bestehen."""
    pr_nr = item["github_id"]
    diff = gh.get_pr_diff(pr_nr)

    # 1. Strukturelle Prüfung (Page Bundle, Frontmatter)
    struct_errors = _verify_pr_structure(diff)
    if struct_errors:
        error_list = "\n".join(f"- {e}" for e in struct_errors)
        msg = f"Strukturprüfung fehlgeschlagen:\n{error_list}"
        gh.comment_issue(pr_nr, msg)
        gh.close_pr(pr_nr)
        return f"PR #{pr_nr} abgelehnt (Struktur): {'; '.join(struct_errors)}"

    # 2. Inhaltliche Prüfung durch LLM
    verdict = generate(
        system="""Du prüfst Änderungen an einem juristischen Gesetzeskommentar (Glossagens).
Beurteile ob die Änderung:
(1) sachlich korrekt ist und keine erfundenen Zitate enthält
(2) den akademischen Zitierstil einhält
(3) kohärent mit dem bestehenden Kontext ist
(4) dem Hugo Page Bundle Format entspricht (index.md im art-NNN/ Verzeichnis)
Antworte mit APPROVE oder REJECT, gefolgt von einer Begründung (max. 2 Sätze).""",
        user=f"Diff:\n{diff[:4000]}",
    )

    if verdict.upper().startswith("APPROVE"):
        gh.merge_pr(pr_nr, f"Verifiziert: {verdict}")
        return f"PR #{pr_nr} gemerged. Begründung: {verdict}"
    else:
        gh.comment_issue(pr_nr, f"Inhaltliche Verifikation fehlgeschlagen:\n\n{verdict}")
        gh.close_pr(pr_nr)
        return f"PR #{pr_nr} abgelehnt (Inhalt): {verdict}"


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
