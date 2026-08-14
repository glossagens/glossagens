---
title: "Rechtsprechung zu Art. 261 ZPO"
weight: 99
date: 2026-07-18
lastmod: "2026-08-13"
description: "Übersicht der Rechtsprechung zu Art. 261 ZPO — Vorsorgliche Massnahmen, Glaubhaftmachung, nicht leicht wiedergutzumachender Nachteil."
tags: ["Rechtsprechung", "ZPO", "Summarisches Verfahren", "Vorsorgliche Massnahmen"]
agent_verified: false
revisions:
  - date: 2026-08-13
    by: "Claude Code"
    model: "claude-opus-5"
    mcp_verified: true
    note: "Neuaufbau nach Audit (Belegquote 35 %, Urteil C): jede Kernaussage vor dem Schreiben per check_claim_support gegen die benannte Erwägung geprüft; zu den Voraussetzungen von Art. 261 Abs. 1 ZPO selbst liess sich keine einschlägige bundesgerichtliche Erwägung finden"
  - date: 2026-08-13
    by: "Claude Code"
    model: "claude-opus-5"
    mcp_verified: false
    note: "Audit des Bundles gegen opencaselaw-MCP: Belegquote 35 % (Urteil C); 3 von 27 Paaren gestützt; 11 ungestützt; agent_verified zurückgesetzt; Belegapparat wird überarbeitet"
---

# Rechtsprechung zu Art. 261 ZPO

Jeder Eintrag nennt die Erwägung oder den Regeste-Satz, der die wiedergegebene Aussage
trägt.

## I. Sachliche Zuständigkeit

### [BGE 137 III 563](https://mcp.opencaselaw.ch/entscheid/bge_BGE_137_III_563) (9.12.2011)

**Kernaussage**: Die Handelsgerichte sind zuständig, die vorläufige Eintragung eines Bauhandwerkerpfandrechts anzuordnen, sofern die Hauptsache — das Verfahren auf definitive Eintragung — handelsrechtlich ist.

Die Zuständigkeit für die vorsorgliche Massnahme folgt der Hauptsache. Ist diese nicht handelsrechtlich, ist auch das Handelsgericht für die Massnahme nicht zuständig.

## II. Aufschiebende Wirkung im Rechtsmittelverfahren

### [BGE 138 III 378](https://mcp.opencaselaw.ch/entscheid/bge_BGE_138_III_378) (30.3.2012)

**Kernaussage**: Stellt der Entscheid über vorsorgliche Massnahmen, für den der Vollstreckungsaufschub während des Berufungsverfahrens verlangt wird, eine Leistungsmassnahme dar, die endgültige Wirkung haben kann, so darf der Aufschub nur verweigert werden, wenn die Berufung offensichtlich unbegründet oder unzulässig erscheint.

Praktisch bedeutsam für die Berufung gegen Massnahmeentscheide: Bei Leistungsmassnahmen mit möglicher endgültiger Wirkung ist die Schwelle für die Verweigerung der aufschiebenden Wirkung **hoch** — «offensichtlich unbegründet oder unzulässig», nicht schon «aussichtslos».

## Audit-Protokoll

Beim Audit vom 13.08.2026 lag die Belegquote bei 35 % (Urteil C); fünf Paare waren
ungestützt, dreizehn nur teilweise gestützt, eines wurde mit `contradicts` beurteilt.

Nicht übernommen wurden BGE 137 III 324, BGE 137 III 380, BGE 137 III 475,
BGE 138 III 337, BGE 139 III 86, BGE 140 III 315, BGE 141 III 376 und BGE 151 III 227.
Die Entscheide existieren; die ihnen zugeschriebenen Aussagen liessen sich in keiner
Erwägung nachweisen. Der kantonale Entscheid (Obergericht Thurgau RBOG 2023 Nr. 27) ist
nicht mehr als Beleg geführt, weil für kantonale Entscheide keine Erwägungen erschlossen
sind.

Zwei Zuschreibungen waren inhaltlich verfehlt: BGE 138 III 378 wurde für das **Beweismass
der Glaubhaftmachung** angeführt; der Entscheid betrifft die aufschiebende Wirkung nach
Art. 315 Abs. 5 ZPO. Und BGE 151 III 227 wurde für die Voraussetzungen von Art. 261
Abs. 1 ZPO zitiert; er behandelt superprovisorische Massnahmen und den nicht wieder
gutzumachenden Nachteil nach Art. 93 BGG.

**Eine Lücke, die bestehen bleibt.** Zu den Voraussetzungen von Art. 261 Abs. 1 ZPO
selbst — Verfügungsanspruch, Verfügungsgrund, nicht leicht wiedergutzumachender Nachteil
— liess sich keine einschlägige bundesgerichtliche Erwägung finden; die Suche lieferte
Entscheide aus den 1960er-Jahren zu kantonalem Recht. Die Voraussetzungen sind im
Kommentartext aus dem Normwortlaut entwickelt und dort nicht mit Rechtsprechung belegt.

Geprüft wurde über die opencaselaw-MCP (`cite`, `get_regeste`, `get_erwaegung`,
`find_relevant_erwaegung`, `check_claim_support`, `search_decisions`).
