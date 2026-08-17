---
title: "Rechtsprechung zu Art. 229 ZPO"
weight: 2
date: 2026-07-18
lastmod: "2026-08-14"
description: "Übersicht der Rechtsprechung zu Art. 229 ZPO — Aktenschluss, echte und unechte Noven, Dupliknoven, thematisch beschränkte Replik."
tags: ["Rechtsprechung", "ZPO", "Noven", "Aktenschluss", "Dupliknoven"]
agent_verified: false
revisions:
  - date: 2026-08-13
    by: "Claude Code"
    model: "claude-opus-5"
    mcp_verified: true
    note: "Neuaufbau nach Audit (Belegquote 17 %, Urteil C): jede Kernaussage vor dem Schreiben per check_claim_support gegen die benannte Erwägung geprüft; Beschreibung und Tags nannten Hauptverhandlung und Beweiserhebung statt des Novenrechts — richtiggestellt"
  - date: 2026-08-13
    by: "Claude Code"
    model: "claude-opus-5"
    mcp_verified: false
    note: "Audit des Bundles gegen opencaselaw-MCP: Belegquote 17 % (Urteil C); 1 von 21 Paaren gestützt; 15 ungestützt; agent_verified zurückgesetzt; Belegapparat wird überarbeitet"
---

# Rechtsprechung zu Art. 229 ZPO

Jeder Eintrag nennt die Erwägung, die die wiedergegebene Aussage trägt.

> **Vorbehalt der Gesetzesrevision.** Art. 229 ZPO wurde per 1. Januar 2025 um Abs. 2bis
> ergänzt: Nach den ersten Parteivorträgen werden Noven nur noch berücksichtigt, wenn sie
> in der vom Gericht festgelegten Frist oder spätestens in der nächsten Verhandlung
> vorgebracht werden. Die nachstehend wiedergegebene Rechtsprechung ist zur früheren
> Fassung ergangen; sie bleibt für den Zeitpunkt des Aktenschlusses und die Abgrenzung
> echter und unechter Noven massgebend, sagt aber nichts zu Abs. 2bis.

## I. Zeitpunkt des Aktenschlusses

### [BGE 144 III 67, E. 2.4.2](https://mcp.opencaselaw.ch/entscheid/bge_BGE_144_III_67#e-2-4-2) (24.11.2017)

**Kernaussage**: Eine zeitliche Auftrennung von Einreichen neuer Beweismittel und Vorbringen neuer Tatsachen ist unzulässig.

Tatsachenbehauptung und Beweisanerbieten gehören zusammen. Ein Gericht kann nicht zuerst eine Frist für Beweismittel und später eine für Tatsachen ansetzen.

### [BGE 144 III 117, E. 2.2](https://mcp.opencaselaw.ch/entscheid/bge_BGE_144_III_117#e-2-2) (21.2.2018)

**Kernaussage**: Im summarischen Verfahren tritt der Aktenschluss grundsätzlich nach einmaliger Äusserung der Parteien ein.

Das Recht, sich zweimal unbeschränkt zu äussern, ist eine Besonderheit des ordentlichen Verfahrens; über Art. 219 ZPO wird es nicht auf das summarische Verfahren übertragen.

## II. Novenrecht nach Aktenschluss

### [BGE 146 III 55, E. 2.5.2](https://mcp.opencaselaw.ch/entscheid/bge_BGE_146_III_55#e-2-5-2) (6.8.2019)

**Kernaussage**: Nach dem Aktenschluss haben die Parteien nur noch unter den eingeschränkten Voraussetzungen von Art. 229 Abs. 1 ZPO das Recht, neue Tatsachen und Beweismittel vorzubringen. Das gilt insbesondere auch für die Entgegnung auf sogenannte Dupliknoven.

Praktisch bedeutsam: Wer auf Noven in der Duplik antworten will, ist **nicht** frei — auch diese Entgegnung untersteht den Novenschranken. Die verbreitete Vorstellung eines unbeschränkten Replikrechts auf Dupliknoven trifft nicht zu.

### [BGE 146 III 55, E. 2.4.1](https://mcp.opencaselaw.ch/entscheid/bge_BGE_146_III_55#e-2-4-1) (6.8.2019)

**Kernaussage**: Ordnet das Gericht eine thematisch beschränkte Replik an, kann sich die Partei nur im Rahmen dieser Beschränkung ein zweites Mal äussern.

Die zweite unbeschränkte Äusserungsmöglichkeit ist damit verbraucht — auch wenn die Replik thematisch eng geführt wurde.

## Audit-Protokoll

Beim Audit vom 13.08.2026 war von 21 Belegpaaren genau eines gestützt (Belegquote 17 %,
Urteil C); ein Paar wurde mit `contradicts` beurteilt. Die Übersicht wurde verworfen und
neu aufgebaut.

**Beschreibung und Schlagwörter dieser Datei waren themenfremd.** Sie nannten
«Hauptverhandlung, mündliche Verhandlung, Beweiserhebung» — Art. 229 ZPO regelt aber das
Novenrecht und den Aktenschluss. Der Fehler betraf nicht nur die Metadaten: Er erklärt,
warum die frühere Auswahl an Entscheiden thematisch streute.

Nicht übernommen wurden BGE 138 III 483, BGE 138 III 620, BGE 139 III 358,
BGE 140 III 315, BGE 140 III 450, BGE 141 I 97, BGE 142 III 116, BGE 142 III 413,
BGE 143 III 137, BGE 144 III 349, BGE 145 III 422, BGE 146 III 194, BGE 148 III 95 und
BGE 148 III 105 sowie zwei Entscheide aus der Zeit vor der ZPO (4C.374/2001,
4C.378/1999). Die drei kantonalen Entscheide sind nicht mehr als Belege geführt, weil
für kantonale Entscheide keine Erwägungen erschlossen sind.

Geprüft wurde über die opencaselaw-MCP (`cite`, `get_regeste`, `get_erwaegung`,
`find_relevant_erwaegung`, `check_claim_support`).
