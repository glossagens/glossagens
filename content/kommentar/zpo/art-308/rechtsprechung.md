---
title: "Rechtsprechung zu Art. 308 ZPO"
weight: 2
date: 2026-05-23
lastmod: "2026-08-13"
description: "Übersicht der Rechtsprechung zu Art. 308 ZPO — Anfechtbare Entscheide (Berufung), Streitwertgrenze, Endentscheid-Begriff."
tags: ["Rechtsprechung", "ZPO", "Berufung", "Streitwert", "Endentscheid"]
agent_verified: false
revisions:
  - date: 2026-08-13
    by: "Claude Code"
    model: "claude-opus-5"
    mcp_verified: true
    note: "Neuaufbau nach Audit (Belegquote 18 %, Urteil C): jede Kernaussage vor dem Schreiben per check_claim_support gegen die benannte Erwägung geprüft; BGE 138 III 620 stand für die Abgrenzung Zwischen-/Endentscheid, betrifft aber Art. 257 ZPO"
  - date: 2026-08-13
    by: "Claude Code"
    model: "claude-opus-5"
    mcp_verified: false
    note: "Audit des Bundles gegen opencaselaw-MCP: Belegquote 18 % (Urteil C); 0 von 14 Paaren gestützt; 9 ungestützt; agent_verified zurückgesetzt; Belegapparat wird überarbeitet"
---

# Rechtsprechung zu Art. 308 ZPO

Jeder Eintrag nennt die Erwägung, die die wiedergegebene Aussage trägt.

## I. Was ist ein Endentscheid?

### [BGE 148 III 186, E. 6.5](https://mcp.opencaselaw.ch/entscheid/bge_BGE_148_III_186#e-6-5) (18.1.2022)

**Kernaussage**: Die Abschreibung wegen Gegenstandslosigkeit aus anderen Gründen nach Art. 242 ZPO ist ein Endentscheid im Sinn von Art. 308 Abs. 1 lit. a ZPO; er unterliegt bei gegebenem Streitwert der Berufung, ansonsten der Beschwerde nach Art. 319 lit. a ZPO.

Der Entscheid zeigt das Zusammenspiel von Art. 308 und Art. 319 ZPO: Die Rechtsmittelart hängt nicht von der Natur des Entscheids allein ab, sondern zusätzlich vom Streitwert. Unterhalb der Grenze von Fr. 10'000.– bleibt die Beschwerde.

## II. Anwendungsbereich der ZPO

### [BGE 139 III 225](https://mcp.opencaselaw.ch/entscheid/bge_BGE_139_III_225) (25.4.2013)

**Kernaussage**: Im Bereich der freiwilligen Gerichtsbarkeit findet die ZPO nur dort direkte Anwendung, wo das Bundesrecht selbst eine gerichtliche Behörde vorschreibt.

Vorfrage zu Art. 308 ZPO: Wo die ZPO nicht direkt anwendbar ist, richtet sich auch das Rechtsmittel nach kantonalem Recht.

## III. Berufungsverfahren

### [BGE 144 III 394, E. 4.2](https://mcp.opencaselaw.ch/entscheid/bge_BGE_144_III_394#e-4-2) (17.7.2018)

**Kernaussage**: Es obliegt den Parteien, vor erster Instanz angebotene Beweise im Berufungsverfahren erneut anzubieten; das Berufungsgericht muss nicht von sich aus nach nicht wiederholten Beweisanträgen suchen.

Der meistzitierte Entscheid unter den Urteilen, die Art. 308 ZPO anwenden. Praktisch folgenschwer: Wer im Berufungsverfahren auf erstinstanzliche Beweisanträge zurückgreifen will, muss sie ausdrücklich wiederholen.

## Audit-Protokoll

Beim Audit vom 13.08.2026 waren 8 von 16 Belegpaaren ungestützt (Belegquote 18 %,
Urteil C); eines wurde mit `contradicts` beurteilt, zwei waren mangels auflösbarer
Referenz nicht beurteilbar. Die Übersicht wurde verworfen und neu aufgebaut.

**BGE 138 III 620 stand für die Abgrenzung zwischen Zwischen- und Endentscheid.** Der
Entscheid betrifft den Rechtsschutz in klaren Fällen (Art. 257 ZPO) und sagt zur
Abgrenzung nichts. Das war der `contradicts`-Befund.

Nicht übernommen wurden ferner BGE 84 II 134, BGE 102 II 53, BGE 127 III 474,
BGE 129 III 750, BGE 140 III 315, BGE 142 III 116 und BGE 145 III 324 sowie
BGer 4A_169/2021 und 4A_409/2024. Vier Referenzen waren nicht auflösbar, weil
Entscheid-IDs als URL-Pfadbestandteile in den Text geraten waren (4C.316/2006,
4P.315/2004, 5C.46/2001, 5P.341/2004).

Drei der angeführten Entscheide stammen aus der Zeit vor der ZPO (BGE 84 II 134 von
1958, BGE 102 II 53 von 1976, BGE 129 III 750 von 2003). Art. 308 ZPO trat am
1. Januar 2011 in Kraft.

Geprüft wurde über die opencaselaw-MCP (`cite`, `get_regeste`, `get_erwaegung`,
`find_relevant_erwaegung`, `check_claim_support`).
