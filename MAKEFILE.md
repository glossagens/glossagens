# Makefile-Befehle

| Befehl | Beschreibung |
|--------|-------------|
| `make ssh` | SSH-Session auf dem Server öffnen |
| `make logs` | Logs des Hermes-Gateways live verfolgen |
| `make dashboard` | Hermes Dashboard auf dem Server starten (mit lokalen Port-Weiterleitungen) |
| `make serve` | Lokalen Hugo-Entwicklungsserver starten (inkl. Entwürfe) |
| `make build-check` | Seite so bauen wie der GitHub-Runner (~30 s); läuft auch automatisch vor jedem Push |

Das Makefile ist lokal und nicht im Git-Repo.

Skills kommen über `git pull` auf den Server (`/opt/glossagens/agent/skills`), nicht per Kopie.
