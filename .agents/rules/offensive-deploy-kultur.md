---
trigger: always_on
---

# Offensive Deploy-Kultur

In diesem Repository herrscht eine **offensive Deploy-Kultur**:

1. **Autonomer Abschluss**: Sobald ein Beitrag (Thema, Gesetzeskommentar, Skript, Korrektur) inhaltlich fertiggestellt ist und alle mechanischen Verifikationen (`pruefen.py`, `build-check.sh`, `hugo`) fehlerfrei durchlaufen sind, wird **ohne Zögern und ohne Rückfrage committet und gepusht**.
2. **Proaktives Deployment**: Jeder Push auf `main` triggert automatisch den GitHub-Pages-Deploy-Workflow (`deploy.yml`). Es wird nicht auf gesonderte Aufforderung gewartet, um geprüfte, fertige Arbeit zu veröffentlichen.
3. **Strenge Vorabprüfung, dann sofortiger Push**: Die Entschlossenheit beim Deployment entbindet nicht von der Pflicht zur sorgfältigen Verifikation (keine Halluzinationen, alle Zitate wörtlich abgeglichen, alle Links und Anker verifiziert). Ist die Verifikation grün: sofort `git commit` und `git push origin main`.
4. **Behandlung von Pull Requests (PRs sauber mergen)**: Wird ein Pull Request übernommen, werden nötige Ergänzungen (z. B. Wortlaut-Daten, Rechtsprechungsübersichten, Korrekturen) direkt in den jeweiligen PR-Branch committet und gepusht, bis die CI-Checks grün sind. Anschliessend wird der PR regulär über `gh pr merge` (z. B. `--squash` oder `--rebase`) gemergt, damit er auf GitHub offiziell als **Merged** geführt wird. Ein Schliessen via `gh pr close` bei eigentlich übernommenen Inhalten ist untersagt.
