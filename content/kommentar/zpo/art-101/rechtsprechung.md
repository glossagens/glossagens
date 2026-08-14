---
title: "Rechtsprechung zu Art. 101 ZPO"
weight: 2
date: 2026-05-23
lastmod: "2026-08-13"
description: "Übersicht der Rechtsprechung zu Art. 101 ZPO — Fristansetzung, zwingende Nachfrist, Fristwahrung bei Zahlung, Kostenfolgen des Nichteintretens."
tags: ["Rechtsprechung", "ZPO", "Sicherheitsleistung", "Parteientschädigung", "Vorschuss", "Nachfrist"]
agent_verified: false
revisions:
  - date: 2026-08-13
    by: "Claude Code"
    model: "claude-opus-5"
    mcp_verified: true
    note: "Neuaufbau nach Audit (Belegquote 37 %, Urteil C): jede Kernaussage vor dem Schreiben per check_claim_support gegen die benannte Erwägung geprüft"
  - date: 2026-08-13
    by: "Claude Code"
    model: "claude-opus-5"
    mcp_verified: false
    note: "Audit des Bundles gegen opencaselaw-MCP: Belegquote 37 % (Urteil C); 5 von 31 Paaren gestützt; 13 ungestützt; agent_verified zurückgesetzt; Belegapparat wird überarbeitet"
---

# Rechtsprechung zu Art. 101 ZPO

Jeder Eintrag nennt die Erwägung, die die wiedergegebene Aussage trägt.

## I. Fristansetzung und zwingende Nachfrist

### [BGer 4A_26/2021 vom 12. Februar 2021, E. 4.2](https://mcp.opencaselaw.ch/entscheid/bger_4A_26_2021#e-4-2)

**Kernaussage**: Nach Art. 101 Abs. 1 ZPO setzt das Gericht eine Frist zur Leistung des Vorschusses; die fristgerechte Bezahlung ist eine Prozessvoraussetzung (Art. 59 Abs. 2 lit. f ZPO). Wird der Vorschuss nicht geleistet, darf das Gericht nicht sofort einen Nichteintretensentscheid fällen, sondern muss zunächst eine Nachfrist ansetzen.

Der praktisch wichtigste Satz zur Norm: Die Nachfrist nach Abs. 3 ist **zwingend**. Ein Nichteintretensentscheid ohne vorgängige Nachfrist ist bundesrechtswidrig.

## II. Wahrung der Zahlungsfrist

### [BGE 139 III 364, E. 3.1](https://mcp.opencaselaw.ch/entscheid/bge_BGE_139_III_364#e-3-1) (26.7.2013)

**Kernaussage**: Gemäss Art. 143 Abs. 3 ZPO ist die Frist für eine Zahlung an das Gericht eingehalten, wenn der Betrag spätestens am letzten Tag der Frist zugunsten des Gerichts der Schweizerischen Post übergeben oder einem Post- oder Bankkonto in der Schweiz belastet worden ist.

Massgebend ist die **Belastung** des Kontos, nicht der Eingang beim Gericht. Bei E-Banking-Aufträgen am letzten Tag kommt es damit auf das Valutadatum der Belastung an.

## III. Kostenfolgen des Nichteintretens

### [BGE 139 III 334, E. 3.1](https://mcp.opencaselaw.ch/entscheid/bge_BGE_139_III_334#e-3-1) (8.7.2013)

**Kernaussage**: Es ist zulässig, das Nichteintreten auf eine Klage mangels fristgemässer Leistung des Kostenvorschusses mit Kosten zu verbinden.

### [BGE 140 III 159, E. 4.2.1](https://mcp.opencaselaw.ch/entscheid/bge_BGE_140_III_159#e-4-2-1) (7.5.2014)

**Kernaussage**: Eine bundesrechtliche Verpflichtung des Gerichts, mit der Zustellung der Klage und der Ansetzung der Frist zur Klageantwort zuzuwarten, bis der Kostenvorschuss geleistet ist, lässt sich nicht aus einer Pflicht herleiten, dem Kläger unnötige Kosten zu ersparen.

Zusammen mit dem vorstehenden Entscheid ergibt sich das volle Kostenrisiko der säumigen klagenden Partei: Gerichtsgebühr für den Nichteintretensentscheid **und** allfällige Parteientschädigung, wenn die Klage bereits zugestellt war.

## Audit-Protokoll

Beim Audit vom 13.08.2026 waren 13 von 31 Belegpaaren ungestützt und weitere 13 nur
teilweise gestützt (Belegquote 37 %, Urteil C). Die Übersicht wurde verworfen und neu
aufgebaut.

Nicht übernommen wurden BGE 139 III 358, BGE 139 III 498, BGE 141 III 369,
BGE 142 III 413, BGE 144 III 394, BGE 145 III 153, BGE 148 III 21, BGE 148 III 182,
BGE 148 III 186 sowie BGer 1C_466/2022, 2C_107/2019, 4A_29/2014, 4A_310/2021,
4A_360/2018, 5A_242/2025, 5A_964/2014, 5A_979/2025 und 5A_997/2014. Die Entscheide
existieren; die ihnen zugeschriebenen Aussagen liessen sich in keiner Erwägung
nachweisen.

Auffällig an diesem Bundle: Die Referenzliste überschnitt sich stark mit derjenigen von
Art. 98 und Art. 95 — dieselben Entscheide wurden mehreren Artikeln mit jeweils anderer
Aussage zugeschrieben. Das ist ein Muster, das für sich schon verdächtig ist: Ein
Entscheid trägt in der Regel eine Aussage, nicht drei verschiedene.

Geprüft wurde über die opencaselaw-MCP (`cite`, `get_regeste`, `get_erwaegung`,
`find_relevant_erwaegung`, `check_claim_support`).
