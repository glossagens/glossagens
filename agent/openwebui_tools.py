"""
OpenWebUI Tool-Definitionen für die Glossagens-Schaltzentrale.

Installation: In OpenWebUI unter Workspace → Tools → New Tool
einfügen. Die Umgebungsvariablen werden vom Hetzner-Server gelesen
(AGENT_API_URL, AGENT_API_KEY).
"""

import os
import json
import requests
from typing import Any

AGENT_API_URL = os.getenv("AGENT_API_URL", "http://localhost:8000")
AGENT_API_KEY = os.getenv("AGENT_API_KEY", "")


def _headers() -> dict:
    return {"Authorization": f"Bearer {AGENT_API_KEY}"}


def _post(path: str, data: dict = {}) -> Any:
    r = requests.post(f"{AGENT_API_URL}{path}", json=data, headers=_headers(), timeout=120)
    r.raise_for_status()
    return r.json()


def _get(path: str) -> Any:
    r = requests.get(f"{AGENT_API_URL}{path}", headers=_headers(), timeout=30)
    r.raise_for_status()
    return r.json()


class Tools:

    def list_pending(self) -> str:
        """
        Zeigt alle offenen Einreichungen und PRs in der Glossagens-Queue.
        Gibt eine formatierte Liste mit ID, Typ, Titel und Datum zurück.
        """
        items = _get("/pending")
        if not items:
            return "Keine offenen Einreichungen."
        lines = ["**Offene Einreichungen:**\n"]
        for item in items:
            lines.append(
                f"**#{item['id']}** [{item['type'].upper()}] {item['title']}\n"
                f"  Datum: {item['created_at'][:16]} | URL: {item['url']}\n"
            )
        return "\n".join(lines)

    def approve(self, id: int, instruction: str = "") -> str:
        """
        Gibt eine Einreichung frei und lässt den Agenten die Aktion ausführen.

        :param id: Die ID aus der Pending-Queue (z.B. 42)
        :param instruction: Optionale Zusatzanweisung für den Agenten (z.B. "nur Rechtsprechung ergänzen")
        """
        result = _post("/approve", {"id": id, "instruction": instruction})
        return f"✅ Einreichung #{id} ausgeführt: {result.get('result', '')}"

    def reject(self, id: int, reason: str = "") -> str:
        """
        Lehnt eine Einreichung ab. Der Einreicher erhält eine Benachrichtigung auf GitHub.

        :param id: Die ID aus der Pending-Queue
        :param reason: Begründung für die Ablehnung (wird dem Einreicher mitgeteilt)
        """
        result = _post("/reject", {"id": id, "reason": reason})
        return f"❌ Einreichung #{id} abgelehnt: {result.get('result', '')}"

    def queue_status(self) -> str:
        """
        Zeigt den vollständigen Queue-Status (pending, executed, rejected, errors).
        """
        items = _get("/queue")
        if not items:
            return "Queue ist leer."
        summary: dict[str, int] = {}
        for item in items:
            summary[item["status"]] = summary.get(item["status"], 0) + 1
        lines = ["**Queue-Status:**\n"]
        for status, count in sorted(summary.items()):
            emoji = {"pending": "⏳", "executed": "✅", "rejected": "❌", "error": "🔴", "processing": "🔄"}.get(status, "•")
            lines.append(f"{emoji} {status}: {count}")
        return "\n".join(lines)
