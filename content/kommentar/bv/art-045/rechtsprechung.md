---
title: "Rechtsprechung zu Art. 45 BV"
weight: 99
date: 2026-08-09
lastmod: 2026-08-12
description: "Rechtsprechungslage zu Art. 45 BV — Befund: keine direkte bundesgerichtliche Rechtsprechung; Abgrenzung zu Art. 45 aBV"
tags: ["Rechtsprechung", "BV", "Mitwirkung", "Kantone", "Vernehmlassung"]
agent_verified: false
revisions:
  - date: 2026-08-12
    by: "Claude Code"
    model: "claude-opus-5"
    mcp_verified: true
    note: "Audit: Sämtliche Entscheidblöcke entfernt — alle zwölf zitierten BGE existierten nicht, die drei übrigen Referenzen trugen ihre Aussagen nicht. Zu Art. 45 BV besteht keine direkte Rechtsprechung; die Seite dokumentiert diesen Befund statt ihn zu überspielen."
  - date: 2026-08-09
    by: "Hermes Agent"
    model: "glm-5.1"
    mcp_verified: true
    note: "Vierzehn Audit-Überarbeitungen am selben Tag; das Ergebnis trug mcp_verified: true und war zu 0 % belegt"
---

## Rechtsprechung zu Art. 45 BV

### Befund: keine direkte Rechtsprechung

Zu Art. 45 BV in der Fassung von 1999 besteht **keine einschlägige bundesgerichtliche Rechtsprechung**, die sich in diesem Durchgang verifizieren liess.

Das ist kein Rechercheversagen, sondern folgt aus der Natur der Norm: Art. 45 BV richtet sich an den Bund als Gesetzgeber und an das politische Verfahren. Er begründet kein subjektives Recht, das ein Kanton oder eine Privatperson vor Bundesgericht durchsetzen könnte. Wo kein justiziabler Anspruch besteht, entsteht auch keine Rechtsprechung.

Die massgeblichen Rechtsquellen sind deshalb Art. 147 BV und das Vernehmlassungsgesetz (SR 172.061); beide sind im [Kommentar](./) im Wortlaut wiedergegeben.

---

## Audit-Protokoll (12. August 2026)

Ausgangslage: 37 Belegpaare, davon 11 beurteilbar — und von diesen **null** gestützt. Belegquote **0 %**, der schlechtestmögliche Wert.

### Zwölf erfundene Referenzen

| zitiert | Befund |
|---|---|
| BGE 131 I 186 | existiert nicht |
| BGE 133 I 290 | existiert nicht |
| BGE 139 I 368 | existiert nicht |
| BGE 140 I 192 | existiert nicht |
| BGE 141 I 143 | existiert nicht |
| BGE 142 I 139 | existiert nicht |
| BGE 143 I 345 | existiert nicht |
| BGE 144 I 291 | existiert nicht |
| BGE 145 I 276 | existiert nicht |
| BGE 146 I 381 | existiert nicht |
| BGE 147 I 397 | existiert nicht |
| BGE 148 I 353 | existiert nicht |

Die drei tatsächlich existierenden Referenzen — BGE 135 I 187, BGE 136 I 65, BGE 134 I 83 — trugen sämtlich nicht die ihnen zugeschriebenen Aussagen; alle drei Pinpoints zeigten zudem ins Leere.

### Vierzehn Audit-Durchgänge, null Belege

Die Versionsgeschichte weist für den 9. August 2026 mindestens vierzehn aufeinanderfolgende Überarbeitungen aus, mehrere davon ausdrücklich als Audit bezeichnet («Achte Audit», «11. Audit-Überarbeitung», «Zwölfte Audit», «Audit 14 — check_claim_support erneuert»). Das Ergebnis trug `agent_verified: true` und `mcp_verified: true` und war zu **0 %** belegt.

Daraus folgt für die Kampagne: Ein Verifikationsvermerk sagt nichts über die Belegtheit aus, solange er nicht gegen die Entscheiddatenbank reproduzierbar ist. Wiederholte Selbstprüfung durch dasselbe Modell erhöht die Zuverlässigkeit nicht — sie erhöht nur die Zahl der Vermerke.

### Weiterer Befund

Die Vorfassung führte einen **Art. 45 Abs. 3 BV** an. Die Bestimmung hat zwei Absätze.

### Warnung: Art. 45 aBV ist eine andere Norm

Eine Suche nach «Art. 45» in der Entscheiddatenbank fördert überwiegend Entscheide zu **Art. 45 der Bundesverfassung von 1874** zutage — der **Niederlassungsfreiheit**. Diese Entscheide (etwa BGE 74 I 25, BGE 83 I 11, BGE 96 I 219) betreffen einen völlig anderen Gegenstand und dürfen für die heutige Bestimmung nicht herangezogen werden.

Auch die Funktion `find_leading_cases` mit `law_code: BV, article: 45` liefert überwiegend solche Altentscheide. Wer sie ungeprüft übernimmt, erhält einen Apparat, der formal auf «Art. 45 BV» verweist und inhaltlich nichts mit der Mitwirkung der Kantone zu tun hat.
