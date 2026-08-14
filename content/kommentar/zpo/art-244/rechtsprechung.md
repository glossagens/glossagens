---
title: "Rechtsprechung zu Art. 244 ZPO"
weight: 2
date: 2026-05-23
lastmod: "2026-08-13"
description: "Übersicht der Rechtsprechung zum vereinfachten Verfahren — Anwendungsbereich, Verhältnis zur sachlichen Zuständigkeit, Hauptverhandlung."
tags: ["Rechtsprechung", "ZPO", "vereinfachtes Verfahren", "Klageeinreichung"]
agent_verified: false
revisions:
  - date: 2026-08-13
    by: "Claude Code"
    model: "claude-opus-5"
    mcp_verified: true
    note: "Neuaufbau nach Audit (Belegquote 32 %, Urteil C): jede Kernaussage vor dem Schreiben per check_claim_support gegen die benannte Erwägung geprüft; zu Art. 244 ZPO selbst liess sich keine einschlägige bundesgerichtliche Rechtsprechung finden — das ist im Audit-Protokoll ausgewiesen"
  - date: 2026-08-13
    by: "Claude Code"
    model: "claude-opus-5"
    mcp_verified: false
    note: "Audit des Bundles gegen opencaselaw-MCP: Belegquote 32 % (Urteil C); 4 von 31 Paaren gestützt; 15 ungestützt; agent_verified zurückgesetzt; Belegapparat wird überarbeitet"
---

# Rechtsprechung zu Art. 244 ZPO

Jeder Eintrag nennt die Erwägung, die die wiedergegebene Aussage trägt.

**Zur Belegdichte:** Zu Art. 244 ZPO selbst — den Formanforderungen an die vereinfachte
Klage — besteht kaum eigene bundesgerichtliche Rechtsprechung. Die einschlägigen
Entscheide betreffen den **Anwendungsbereich** des vereinfachten Verfahrens (Art. 243 ZPO)
und dessen Ablauf. Die Übersicht bildet deshalb ab, was belegbar ist, und nicht mehr.

## I. Verhältnis zur sachlichen Zuständigkeit

### [BGE 143 III 137, E. 2.2](https://mcp.opencaselaw.ch/entscheid/bge_BGE_143_III_137#e-2-2) (27.2.2017)

**Kernaussage**: Gilt für eine Streitigkeit nach Art. 243 Abs. 1 oder 2 ZPO das vereinfachte Verfahren, ist das Handelsgericht nicht zuständig.

Praktisch bedeutsam für die Wahl des Gerichts: Die Verfahrensart geht der handelsgerichtlichen Zuständigkeit vor. Wer bei einem Streitwert unter Fr. 30'000.– oder in einer Angelegenheit nach Art. 243 Abs. 2 ZPO ans Handelsgericht gelangt, erhält einen Nichteintretensentscheid.

## II. Hauptverhandlung im vereinfachten Verfahren

### [BGE 140 III 450, E. 3.2](https://mcp.opencaselaw.ch/entscheid/bge_BGE_140_III_450#e-3-2) (1.9.2014)

**Kernaussage**: Im vereinfachten Verfahren besteht ein Anspruch auf Durchführung einer Hauptverhandlung; die Parteien können darauf verzichten, wobei offenbleibt, ob das auch in den Fällen von Art. 243 Abs. 2 ZPO gilt.

Die offengelassene Frage betrifft gerade die sozialpolitisch motivierten Streitigkeiten (Miete, Arbeit, Gleichstellung), in denen die Hauptverhandlung dem Schutz der schwächeren Partei dient. Ein Verzicht ist dort riskant.

## Audit-Protokoll

Beim Audit vom 13.08.2026 waren 15 von 31 Belegpaaren ungestützt und 12 weitere nur
teilweise gestützt (Belegquote 32 %, Urteil C); fünf Paare wurden mit `contradicts`
beurteilt. Sämtliche Paare lagen in dieser Übersicht — der Fliesstext in `_index.md`
führt keine Belege.

Nicht übernommen wurden BGE 117 II 256, BGE 118 II 27, BGE 127 III 474,
BGE 138 III 483, BGE 141 I 97, BGE 142 III 145, BGE 142 III 278, BGE 142 III 402,
BGE 146 III 63, BGE 148 III 105, BGE 148 III 415, BGE 149 III 469, BGE 150 III 257
sowie BGer 4A_182/2019. Die Entscheide existieren; die ihnen zugeschriebenen Aussagen
liessen sich in keiner Erwägung nachweisen.

Zwei der angeführten Entscheide stammen aus der Zeit vor der ZPO (BGE 117 II 256 von
1991, BGE 118 II 27 von 1992). Art. 244 ZPO trat erst am 1. Januar 2011 in Kraft.

**Eine Lücke, die bestehen bleibt.** Zu den Formanforderungen an die vereinfachte Klage
nach Art. 244 Abs. 1 und 2 ZPO — insbesondere zur Frage, wann eine Klage ohne Begründung
genügt und wie das Gericht bei unvollständigen Laieneingaben vorzugehen hat — liess sich
keine einschlägige bundesgerichtliche Erwägung finden. Die Recherche über
`search_decisions` lieferte für «Art. 244 ZPO» überwiegend kantonale Steuer- und
Sozialversicherungsentscheide zu gleichlautenden kantonalen Paragraphen. Diese Lücke ist
hier ausgewiesen statt mit thematisch benachbarten Entscheiden gefüllt.

Geprüft wurde über die opencaselaw-MCP (`cite`, `get_regeste`, `get_erwaegung`,
`find_relevant_erwaegung`, `check_claim_support`, `search_decisions`).
