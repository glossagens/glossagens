# Makefile-Befehle

| Befehl | Beschreibung |
|--------|-------------|
| `make deploy-skills` | Skill-Dateien auf den Hetzner-Server übertragen (fragt nach Passwort) |
| `make ssh` | SSH-Session auf dem Server öffnen |
| `make logs` | Agent-Logs live verfolgen |
| `make dashboard` | Hermes Dashboard auf dem Server starten (mit lokalen Port-Weiterleitungen) |
| `make serve` | Lokalen Hugo-Entwicklungsserver starten (inkl. Entwürfe) |
| `make build-check` | Seite so bauen wie der GitHub-Runner (~30 s); läuft auch automatisch vor jedem Push |

Das Makefile ist lokal und nicht im Git-Repo.
