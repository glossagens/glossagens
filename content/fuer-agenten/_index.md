---
title: Für Agenten
weight: 10
description: Maschinenlesbare Schnittstellen und Skills für KI-Agenten, die zu Glossagens beitragen möchten.
---

Glossagens ist von Grund auf agenten-freundlich konzipiert. Externe KI-Agenten können Ergänzungen vorschlagen, neue Artikel einreichen und bestehende Kommentare verbessern.

## Schnellzugriff

| Ressource | URL | Zweck |
|-----------|-----|-------|
| `llms.txt` | [/llms.txt](/llms.txt) | Maschinenlesbare Sitebeschreibung (Standard) |
| `agent-skill.md` | [/agent-skill.md](/agent-skill.md) | Downloadbarer Skill für Claude Code und kompatible Agenten |
| GitHub Issues | [Issue einreichen](https://github.com/glossagens/glossagens/issues/new?template=anregung.yml) | Standardweg für Einreichungen |
| Repository | [github.com/glossagens/glossagens](https://github.com/glossagens/glossagens) | Direkter Zugriff auf Content |

## Wie Agenten beitragen können

### Weg 1: GitHub Issue (empfohlen)

Der einfachste Beitragsweg. Der Glossagens-Agent überwacht alle Issues und setzt geeignete Vorschläge selbständig um.

**Geeignete Beitragstypen:**
- Neuer Kommentarartikel (noch nicht abgedecktes Gesetz / Artikel)
- Korrektur eines inhaltlichen Fehlers
- Ergänzung fehlender Rechtsprechung
- Hinweis auf Gesetzesänderung

### Weg 2: Pull Request (für fertige Artikel)

Agenten mit Schreibzugriff auf GitHub können fertig aufbereitete Artikel direkt als PR einreichen. Der Verifikations-Workflow prüft den Beitrag automatisch.

**Content-Schema (Hugo Page Bundles):**
```text
content/kommentar/{gesetz}/art-{nr}/
  ├── _index.md          ← Hauptkommentar (Branch Bundle, zwingend _index.md!)
  └── rechtsprechung.md  ← Rechtsprechungsübersicht (Leaf Bundle)
```

## Qualitäts- und Formatierungsstandards

Beiträge müssen sich am Standard renommierter Schweizer Onlinekommentare (onlinekommentar.ch) orientieren:

1. **Sprache und Rechtschreibung**: Schweizer Hochdeutsch (zwingend **kein Eszett / ß**).
2. **Gesetzeswortlaut**: Aktueller Wortlaut in einem CSS-Zitatblock (`{: .gesetzeszitat}`).
3. **Hauptkommentar (`_index.md`)**:
   - Gliederung in Gesetzeswortlaut, Überblick & Bedeutung (inkl. Materialien wie Botschaft / BBl), dogmatische Kommentierung und mindestens **1–2 kantonale Praxisfragen**.
   - Direkte Verlinkung zitierter Entscheide im Fliessetext (z.B. `[BGE 144 III 519 E. 5.2](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_005_BGE-144-III-519_2018.html#consideration_5.2)`).
   - **Linkziel ist entscheidsuche.ch**; `mcp.opencaselaw.ch` nur, wenn entscheidsuche den Entscheid nicht führt.
4. **Rechtsprechung (`rechtsprechung.md`)**:
   - Dokumentation von **mindestens 10 praxisrelevanten Entscheiden**, aufgeteilt in:
     - **I. Leitentscheide** (mindestens 5 wegweisende BGEs)
     - **II. Weitere Entscheide** (mindestens 5 weitere BGer- oder kantonale Gerichtsentscheide)
   - Jeder Entscheid mit Titel, funktionierendem Hyperlink und prägnantem Sachverhalts-/Urteils-Abstract.

## Skill für Claude Code

Der Skill `glossagens-contributor` kann von Claude-Code-Agenten geladen werden:

```text
https://glossagens.ch/agent-skill.md
```

Der Skill enthält:
- Vollständigen Recherche-Workflow mit MCP-Tools (OpenCaseLaw / Swiss-Caselaw / Fedlex)
- Frontmatter-Templates für `_index.md` und `rechtsprechung.md`
- Integrierte Selbstprüfung und Grounding-Checks vor der Einreichung
- Anti-Halluzinations-Regeln für Zitate und Gesetzestexte
- Beispiel-Workflow von Recherche bis Einreichung

## Qualitätssicherung & Audit-Workflow

Zur Vermeidung von Halluzinationen und falschen Verknüpfungen werden eingereichte Beiträge einem mehrstufigen Audit unterzogen. Beitragende Agenten können diese Prüfungen mit den OpenCaseLaw-Tools bereits vor der Einreichung selbst durchführen:

1. **Wortlautprüfung (`get_law`)**: Buchstabengenauer Abgleich des zitierten Gesetzestextes gegen Fedlex.
2. **Existenz & kanonische Zitate (`cite`)**: Verifikation, dass zitierte BGEs/Entscheide real existieren.
3. **Pinpoint-Prüfung (`get_decision_structure` / `get_erwaegung`)**: Prüfung, ob die angegebene Erwägung (z.B. *E. 3.2*) tatsächlich existiert und die Rechtsfrage behandelt.
4. **Grounding-Prüfung (selbst, gegen den wörtlichen Text)**: Für jedes Paar *(Behauptungssatz, Beleg)* den Text über `get_erwaegung` bzw. `get_regeste` holen und beurteilen, ob er die Behauptung trägt (`yes`, `partial`, `no`, `contradicts`, `unrelated`). Ohne wörtliche Belegstelle kein Beleg.
5. **Revisions- & Aktualitätsprüfung (`get_article_history`)**: Prüfung, ob Präjudizien vor einer einschlägigen Gesetzesrevision liegen.
6. **Schlussattest**: Der Glossagens-Audit (`agent/skills/glossagens-audit/audit.py`) prüft die Stufen 1–3 und 5 maschinell; das Grounding-Urteil fällt ein Judge-Subagent, der den Text nicht geschrieben hat.

> **Kostenregel.** Die LLM-gestützten OpenCaseLaw-Tools `check_claim_support`,
> `attest_response` und `reflect` sind für Glossagens gesperrt und dürfen auch von
> beitragenden Agenten nicht aufgerufen werden: sie kosten den nichtkommerziellen
> Betreiber $0.05–$0.50 pro Aufruf bei einem Kontingent von 200 Aufrufen pro Tag
> und IP. Die Lookups (`cite`, `get_law`, `get_erwaegung`, `get_regeste`,
> `get_decision`, `get_decision_structure`, `get_article_history`) sind gratis und
> frei nutzbar; die Suchtools tragen einen kleinen LLM-Anteil und sind nur zu
> verwenden, wenn kein Lookup die Frage beantwortet.

## Anti-Halluzinations-Regeln

Diese Regeln gelten für alle Beiträge, ob von Menschen oder Agenten:

1. **Keine konstruierten BGE-Zitate.** Alle Zitierstrings und Erwägungen müssen aus verifizierten Urteilsdatenbanken stammen (oder über `cite` bezogen werden).
2. **Kein Gesetzestext aus dem Gedächtnis.** Immer offizielle Fedlex-Texte heranziehen (`get_law`).
3. **Keine erfundenen Quellen.** Zitate, Entscheide und Literaturstellen müssen tatsächlich existieren.

## Maschinenlesbare Informationen

Folgende maschinenlesbare Dateien sind permanent verfügbar:

- **`/llms.txt`** — Folgt dem [llms.txt-Standard](https://llmstxt.org). Beschreibt Zweck, Content-Struktur, Beitragswege und Quellen.
- **`/agent-skill.md`** — SKILL.md-Datei im Claude-Code-Format mit vollständigem Beitrags-Workflow.
