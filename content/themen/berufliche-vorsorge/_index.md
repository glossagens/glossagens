---
title: "Berufliche Vorsorge (BVG): Das System der 2. Säule in der Altersvorsorge"
date: 2026-10-27
lastmod: 2026-10-27
description: "Systematische Erörterung der beruflichen Vorsorge (2. Säule, BVG und FZG): Versicherungspflicht (Pensionskassenpflicht), Eintrittsschwelle, koordinierter Lohn, Altersgutschriften, Kapitaldeckungsverfahren, Auszahlungsmodalitäten (Rente, Kapitalbezug, Barauszahlung) und Rechtsschutz nach Art. 73 BVG."
tags: ["Berufliche Vorsorge", "BVG", "FZG", "2. Säule", "Pensionskasse", "Altersvorsorge", "Eintrittsschwelle", "Koordinierter Lohn", "Kapitalbezug", "Sozialversicherungsrecht"]
typ: institution
kurz: "Die berufliche Vorsorge (2. Säule) sichert zusammen mit der AHV/IV die Fortsetzung der gewohnten Lebenshaltung im Kapitaldeckungsverfahren. Arbeitnehmende unterstehen ab dem 1. Januar nach Vollendung des 17. Altersjahres für die Risiken Tod und Invalidität und ab dem 1. Januar nach Vollendung des 24. Altersjahres für das Alter der obligatorischen Versicherung (Pensionskassenpflicht), sofern ihr massgebender Jahreslohn die gesetzliche Eintrittsschwelle von CHF 22'680.- übersteigt. Die Altersleistung wird im Grundsatz als lebenslange Rente basierend auf dem Mindestumwandlungssatz (6.8 %) oder auf Verlangen zu mindestens einem Viertel als Kapitalabfindung ausbezahlt, wofür bei Verheirateten die schriftliche Zustimmung des Ehegatten erforderlich ist."
sachgebiete: [bvg, schuldrecht.arbeit]
normen:
  - { gesetz: bv, art: art-113 }
  - { gesetz: bvg, art: art-002 }
  - { gesetz: bvg, art: art-007 }
  - { gesetz: bvg, art: art-008 }
  - { gesetz: bvg, art: art-013 }
  - { gesetz: bvg, art: art-014 }
  - { gesetz: bvg, art: art-015 }
  - { gesetz: bvg, art: art-016 }
  - { gesetz: bvg, art: art-037 }
  - { gesetz: bvg, art: art-037a }
  - { gesetz: bvg, art: art-073 }
  - { gesetz: fzg, art: art-002 }
  - { gesetz: fzg, art: art-005 }
stichworte: ["Berufliche Vorsorge", "BVG", "FZG", "Pensionskasse", "2. Säule", "Eintrittsschwelle", "Koordinierter Lohn", "Umwandlungssatz", "Kapitalbezug", "Kapitalabfindung", "Barauszahlung", "Altersgutschriften", "Freizügigkeitsleistung", "Art. 73 BVG"]
revisions:
  - date: 2026-10-27
    by: "Antigravity"
    model: "gemini-3.8-flash"
    note: "Erstfassung nach Skill glossagens-themen (Typ institution). Verfassungs- und Gesetzeswortlaute (Art. 113 BV; Art. 2, 7, 8, 13, 14, 15, 16, 37, 37a, 73 BVG; Art. 2, 5 FZG) per {{< wortlaut >}} aus amtlicher Fedlex-Quelle eingebunden (scripts/wortlaut.py). 14 Leitentscheide von entscheidsuche.ch im Volltext verifiziert; Erwägungsnummern, Anker (#consideration_...) und wörtliche Zitate «...» vollständig mechanisch abgeglichen (pruefen.py ohne Befund)."
---

## Überblick {#ueberblick}

Die berufliche Vorsorge bildet die **2. Säule** des schweizerischen Vorsorgesystems. Zusammen mit der staatlichen Alters- und Hinterlassenenversicherung (1. Säule, AHV) soll sie Betagten, Hinterlassenen und Invaliden die Fortsetzung ihrer gewohnten Lebenshaltung in angemessener Weise ermöglichen. Das Bundesgericht umschreibt diese Kernaufgabe in gefestigter Rechtsprechung: «Die berufliche Vorsorge soll als zweite Säule zusammen mit der ersten die Fortsetzung der gewohnten Lebenshaltung in angemessener Weise ermöglichen» ([BGE 130 I 205 E. 6.2](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_001_BGE-130-I-205_2004.html#consideration_6.2)). Sozialpolitisches Leistungsziel von 1. und 2. Säule zusammen ist das Erreichen eines Renteneinkommens von rund 60 Prozent des vormaligen Erwerbseinkommens.

Während die 1. Säule als staatliche Volksversicherung im Umlageverfahren finanziert wird, basiert die 2. Säule auf dem **Kapitaldeckungsverfahren** ([BGE 151 III 143 E. 8.3.1](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_005_BGE-151-III-143_2025.html#consideration_8.3.1)): Die Arbeitnehmenden sparen zusammen mit ihren Arbeitgebern über die Dauer des Erwerbslebens einen individuellen Kapitalstock an (Altersguthaben), der verzinst und bei Erreichen des Referenzalters über den gesetzlichen oder reglementarischen Umwandlungssatz in eine lebenslange Rente umgerechnet oder in Kapitalform bezogen wird.

Gegenstand dieses Themenbeitrags sind die Funktionsweise des Pensionskassensystems, die gesetzlichen Kriterien für den Beginn und den Umfang der **Pensionskassenpflicht** (Eintrittsschwelle, Altersgrenzen, koordinierter Lohn) sowie die Modalitäten der **Auszahlung der Vorsorgeleistungen** (Altersrente, Kapitalabfindung, Barauszahlung bei Stellenwechsel nach FZG, Vorbezug und Besteuerung).

---

## Verfassungsauftrag und gesetzliche Grundlagen {#verfassung-und-grundlagen}

### Art. 113 BV: Verfassungsauftrag der beruflichen Vorsorge {#art-113-bv}

Das Fundament der zweiten Säule ist in Art. 113 BV verankert. Die Verfassungsnorm verpflichtet den Bund zur Gesetzgebung über die berufliche Alters-, Hinterlassenen- und Invalidenvorsorge und grenzt das Versicherungsobligatorium der Arbeitnehmenden ab:

{{< wortlaut gesetz="bv" art="art-113" >}}

Art. 113 Abs. 1 BV begründet eine umfassende Gesetzgebungskompetenz des Bundes, während Abs. 2 die tragenden Leitprinzipien vorgibt: die obligatorische Versicherung für unselbstständig Erwerbende, die paritätische Beitragsleistung durch Arbeitgebende und Arbeitnehmende sowie die Möglichkeit für Selbstständigerwerbende, sich freiwillig zu versichern ([BGE 130 V 369 E. 6.1](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_007_BGE-130-V-369_2004.html#consideration_6.1); [BGE 134 V 170 E. 3.1](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_007_BGE-134-V-170_2008.html#consideration_3.1)).

### Zweistufigkeit: Gesetzliches Obligatorium (Säule 2a) versus Überobligatorium (Säule 2b) {#obligatorium-und-ueberobligatorium}

Das Recht der beruflichen Vorsorge zeichnet sich durch eine grundlegende Zweiteilung aus:

1. **Gesetzliches Obligatorium (Säule 2a)**: Das Bundesgesetz über die berufliche Alters-, Hinterlassenen- und Invalidenvorsorge (BVG, SR 831.40) statuiert gemäss Art. 6 BVG zwingende *Mindestvorschriften*. Das Obligatorium erfasst Arbeitnehmende, deren Jahreslohn die gesetzliche Eintrittsschwelle übersteigt, und beschränkt sich auf den Bereich des sogenannten koordinierten Lohns (Art. 8 BVG). In diesem Kernbereich gelten zwingende Mindestaltersgutschriften (Art. 16 BVG), eine gesetzliche Mindestverzinsung (Art. 15 Abs. 2 BVG) sowie der Mindestumwandlungssatz (Art. 14 Abs. 2 BVG).
2. **Weitergehende Vorsorge / Überobligatorium (Säule 2b)**: Den Vorsorgeeinrichtungen steht es nach Art. 49 Abs. 1 BVG frei, über die Mindestleistungen hinauszugehen (sog. *umhüllende Vorsorgeeinrichtungen*). Sie können Löhne unterhalb der Eintrittsschwelle, Lohnanteile oberhalb des BVG-Höchstbetrags oder grosszügigere Sparpläne versichern. Im überobligatorischen Bereich geniessen die Kassen eine weitgehende reglementarische Satzungsautonomie; sie können reglementarische Umwandlungssätze und Verzinsungen autonom festlegen ([BGE 130 V 369 E. 6.1](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_007_BGE-130-V-369_2004.html#consideration_6.1)).

Wie das Bundesgericht präzisiert hat, gelten für umhüllende Kassen im weitergehenden Bereich nur ausgewählte zwingende Vorschriften: «Gewährt eine Vorsorgeeinrichtung […] mehr als die Mindestleistungen ("umhüllende Vorsorgeeinrichtung"), so gelten die im Verweiskatalog von Art. 49 Abs. 2 BVG aufgezählten BVG-Normen auch für die weitergehende Vorsorge» ([BGE 141 V 355 E. 3.3](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_007_BGE-141-V-355_2015.html#consideration_3.3)). Zur Wahrung der verfassungs- und gesetzmässigen Mindestgarantie führen umhüllende Vorsorgeeinrichtungen eine permanente Vergleichsrechnung (*Schattenrechnung*): Die dem Versicherten tatsächlich zustehenden Gesamtleistungen dürfen zu keinem Zeitpunkt hinter den zwingenden Mindestleistungen des BVG-Obligatoriums zurückbleiben.

### Trägerschaft und Organisation: Die Vorsorgeeinrichtungen {#organisation-und-traegerschaft}

Die Durchführung der beruflichen Vorsorge obliegt nicht staatlichen Amtsstellen, sondern selbstständigen **Vorsorgeeinrichtungen** (Pensionskassen). Nach Art. 48 BVG müssen sich Vorsorgeeinrichtungen, die an der Durchführung der obligatorischen beruflichen Vorsorge teilnehmen wollen, in das Register für die berufliche Vorsorge eintragen lassen:

- **Rechtsformen**: Vorsorgeeinrichtungen werden regelmässig als privatrechtliche Stiftungen (Art. 80 ff. ZGB), Genossenschaften oder öffentlich-rechtliche Körperschaften bzw. Anstalten errichtet. Das Rechtsverhältnis zwischen der Kasse und den Versicherten stützt sich auf das Vorsorgereglement. Das Bundesgericht wendet für dessen Auslegung vertragsrechtliche Grundsätze an: «Die Auslegung des Reglements einer privatrechtlichen Vorsorgeeinrichtung als vorformulierter Inhalt des Vorsorgevertrages geschieht nach dem Vertrauensprinzip» ([BGE 151 V 144 E. 6.1](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_007_BGE-151-V-144_2025.html#consideration_6.1); vgl. auch [BGE 141 V 162 E. 3.3.1](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_007_BGE-141-V-162_2015.html#consideration_3.3.1)).
- **Paritätische Verwaltung**: Gemäss Art. 51 BVG sind das oberste Organ und die Verwaltung der Vorsorgeeinrichtung zwingend paritätisch aus Vertretern der Arbeitnehmer und der Arbeitgeber zusammenzusetzen.
- **Sicherheitsfonds BVG (Art. 56 BVG)**: Der Sicherheitsfonds sichert die gesetzlichen und reglementarischen Leistungen bei Zahlungsunfähigkeit (Insolvenz) von Vorsorgeeinrichtungen und richtet Zuschüsse an Kassen mit ungünstiger Altersstruktur aus.
- **Stiftung Auffangeinrichtung BVG (Art. 60 BVG)**: Die Auffangeinrichtung fungiert als gesetzliches Auffangnetz: Sie schliesst Arbeitgeber zwangsweise an, die ihrer Anschlusspflicht nicht nachkommen, führt Freizügigkeitskonten für ausgetretene Versicherte ohne neue Kasse und versichert Personen auf freiwilliger Basis oder Arbeitslose (Art. 2 Abs. 3 BVG).
- **Aufsicht**: Die direkte Stiftungsaufsicht obliegt kantonalen oder regionalen Aufsichtsbehörden (Art. 61 BVG). Die gesamtschweizerische Aufsicht und Harmonisierung der Praxis wird durch die unabhängige Oberaufsichtskommission Berufliche Vorsorge (OAK BV, Art. 64a BVG) wahrgenommen.

---

## Pensionskassenpflicht: Ab wann besteht die Versicherungspflicht? {#pensionskassenpflicht}

### Persönliche Voraussetzungen und Altersstufen (Art. 2 und 7 BVG) {#altersstufen-und-voraussetzungen}

Das Gesetz knüpft die obligatorische Versicherung an das Vorliegen eines Arbeitsverhältnisses, ein Mindestalter und das Überschreiten einer Lohnschwelle. Die Unterstellung unter die obligatorische Versicherung wird im Grundsatz durch Art. 2 BVG geregelt:

{{< wortlaut gesetz="bvg" art="art-002" >}}

Das Bundesgericht hält fest: «Die Unterstellung unter die obligatorische Versicherung wird in Art. 2 BVG geregelt» ([BGE 129 V 132 E. 3.1](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_007_BGE-129-V-132_2003.html#consideration_3.1)). Konkretisiert wird dieser Grundsatz durch Art. 7 BVG, der die Altersstufen und den Mindestlohn definiert:

{{< wortlaut gesetz="bvg" art="art-007" >}}

Der zeitliche Verlauf der Versicherungspflicht gliedert sich in zwei aufeinanderfolgende Phasen:

1. **Risikoversicherung (Tod und Invalidität)**: Ab dem **1. Januar nach Vollendung des 17. Altersjahres** (Art. 7 Abs. 1 BVG). Jugendliche Arbeitnehmende ab dem Kalenderjahr, in dem sie 18 Jahre alt werden, sind obligatorisch gegen die Risiken Invalidität und Tod versichert. In dieser Phase werden ausschliesslich Risikobeiträge erhoben; es findet noch kein Sparprozess für das Alter statt.
2. **Altersvorsorge (Sparprozess)**: Ab dem **1. Januar nach Vollendung des 24. Altersjahres** (Art. 7 Abs. 1 BVG). Erst ab dem Kalenderjahr, in dem die versicherte Person das 25. Altersjahr vollendet, setzt der obligatorische Sparprozess für die Altersvorsorge ein. Ab diesem Stichtag werden neben den Risikoprämien auch die Altersgutschriften nach Art. 16 BVG erhoben und dem Altersguthaben gutgeschrieben.

Die obligatorische Versicherung beginnt von Gesetzes wegen mit dem Antritt des Arbeitsverhältnisses ([BGE 120 V 15 E. 2.](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_007_BGE-120-V-15_1994.html#consideration_2.); Art. 10 Abs. 1 BVG). Sie endet mit dem Erreichen des Referenzalters, der Beendigung des Arbeitsverhältnisses oder dem Unterschreiten des Mindestlohns (Art. 10 Abs. 2 BVG), wobei für die Risiken Tod und Invalidität eine gesetzliche Nachdeckung von einem Monat besteht (Art. 10 Abs. 3 BVG).

### Wirtschaftliche Voraussetzungen: Eintrittsschwelle und Lohnbegriff {#eintrittsschwelle-und-lohn}

Nicht jede Erwerbstätigkeit begründet eine Pensionskassenpflicht. Das Gesetz verlangt das Erreichen eines Mindestjahreslohns (**Eintrittsschwelle**):

- **Gesetzlicher Schwellenwert**: Nach Art. 2 Abs. 1 und Art. 7 Abs. 1 BVG in Verbindung mit Art. 5 der Verordnung über die berufliche Alters-, Hinterlassenen- und Invalidenvorsorge (BVV 2, SR 831.441.1) beträgt die Eintrittsschwelle **CHF 22'680.-** pro Kalenderjahr (Stand: 2025/2026). Dies entspricht drei Vierteln der maximalen AHV-Altersrente (Art. 8 Abs. 1 BVG).
- **Massgebender Lohn**: Als massgebender Lohn gilt das im Sinne der AHV beitragspflichtige Bruttoerwerbseinkommen (Art. 7 Abs. 2 BVG i.V.m. Art. 5 Abs. 2 AHVG), einschliesslich regelmässiger Zulagen, Gratifikationen und 13. Monatslöhne.
- **Unterjährige Beschäftigung**: Dauert das Arbeitsverhältnis weniger als ein Jahr oder wird es unterjährig aufgenommen, wird der Lohn auf ein ganzes Jahr hochgerechnet (Art. 2 Abs. 2 BVG). Ein Monatslohn von mehr als CHF 1'890.- (CHF 22'680.- / 12) begründet demnach die Versicherungspflicht, selbst wenn das Anstellungsverhältnis nur für einige Monate eingegangen wird (vorbehaltlich befristeter Verträge bis 3 Monate).

### Der koordinierte Lohn als Bemessungsbasis (Art. 8 BVG) {#koordinierter-lohn}

Beiträge und Gutschriften werden im BVG-Obligatorium nicht auf dem gesamten Bruttolohn berechnet, sondern auf dem **koordinierten Lohn**. Zweck des Koordinationsabzugs ist die Abstimmung der 2. Säule auf die Leistungen der 1. Säule (AHV), damit Lohnanteile, die bereits durch die AHV-Rente rentenbildend erfasst sind, nicht doppelt versichert werden:

{{< wortlaut gesetz="bvg" art="art-008" >}}

Die Berechnungsparameter des koordinierten Lohns (Stand 2025/2026) lauten wie folgt:

| Parameter | Gesetzliche Bestimmung | Betrag (CHF) |
|---|---|---|
| **Eintrittsschwelle** | Art. 2 Abs. 1, Art. 7 Abs. 1 BVG (3/4 der max. AHV-Rente) | **22'680.-** |
| **Koordinationsabzug** | Art. 8 Abs. 1 BVG (7/8 der max. AHV-Rente) | **26'460.-** |
| **Oberer Grenzbetrag** | Art. 8 Abs. 1 BVG (3-fache max. AHV-Rente) | **90'720.-** |
| **Maximal koordinierter Lohn** | Art. 8 Abs. 1 BVG (CHF 90'720.- abzüglich CHF 26'460.-) | **64'260.-** |
| **Minimal koordinierter Lohn** | Art. 8 Abs. 2 BVG (1/8 der max. AHV-Rente) | **3'780.-** |

Liegt der AHV-Jahreslohn knapp über der Eintrittsschwelle (z. B. bei CHF 24'000.-), würde der rechnerische Abzug von CHF 26'460.- zu einem negativen Betrag führen. In diesem Fall greift die Schutzvorschrift von Art. 8 Abs. 2 BVG: Der koordinierte Lohn wird von Gesetzes wegen auf das Minimum von **CHF 3'780.-** aufgerundet.

### Befristete Arbeitsverhältnisse, Nebenerwerb und Mehrfachbeschäftigung {#befristung-und-mehrfachbeschaeftigung}

In der Praxis stellen sich häufig Abgrenzungsfragen bei atypischen Beschäftigungsverhältnissen:

- **Befristete Arbeitsverhältnisse**: Arbeitnehmende mit einem auf höchstens drei Monate befristeten Arbeitsvertrag sind von der obligatorischen Versicherung ausgenommen (Art. 1j Abs. 1 lit. b BVV 2). Wird das Arbeitsverhältnis jedoch über die Dauer von drei Monaten hinaus verlängert, entsteht die Versicherungspflicht ab dem Zeitpunkt, in dem die Verlängerung vereinbart wurde. Werden mehrere aufeinanderfolgende befristete Anstellungen beim selben Arbeitgeber aneinandergereiht, die zusammen länger als drei Monate dauern und bei denen kein Unterbruch drei Monate übersteigt, ist die Person ab Beginn des insgesamt vierten Monats versichert (Kettendienstverträge).
- **Mehrfachbeschäftigung**: Arbeitet eine Person bei mehreren Arbeitgebern, wird die Eintrittsschwelle grundsätzlich für jedes Arbeitsverhältnis gesondert beurteilt. Erreicht der Lohn bei keinem einzelnen Arbeitgeber CHF 22'680.-, besteht von Gesetzes wegen keine Versicherungspflicht, selbst wenn das Gesamteinkommen die Schwelle deutlich übersteigt.
- **Mehrfache Versicherungspflicht**: Werden hingegen bei mehreren Arbeitgebern Löhne oberhalb der Eintrittsschwelle erzielt, besteht bei jeder zuständigen Vorsorgeeinrichtung eine eigenständige Versicherungspflicht. Das Bundesgericht hat klargestellt: «Zusammenfassend ist bei mehreren nebeneinander ausgeübten gleichwertigen Erwerbstätigkeiten von einer mehrfachen Versicherungspflicht auszugehen» ([BGE 129 V 132 E. 3.4.5](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_007_BGE-129-V-132_2003.html#consideration_3.4.5)).

### Ausnahmen vom Versicherungsobligatorium {#ausnahmen-obligatorium}

Gestützt auf Art. 2 Abs. 4 BVG und Art. 1j BVV 2 sind folgende Kategorien von Personen von der obligatorischen Versicherung ausgenommen:

- **Selbstständigerwerbende**: Das BVG statuiert eine Pflichtversicherung ausschliesslich für Arbeitnehmende. Das Bundesgericht betont: «Selbstständigerwerbende sind dem Obligatorium der beruflichen Vorsorge nicht von Gesetzes wegen unterstellt» ([BGE 134 V 170 E. 3.1](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_007_BGE-134-V-170_2008.html#consideration_3.1)). Sie können sich jedoch freiwillig bei der Vorsorgeeinrichtung ihres Berufsverbandes oder bei der Auffangeinrichtung versichern (Art. 4 und 44 BVG).
- **Hauptberuflich Selbstständige im Nebenerwerb**: Arbeitnehmende, die neben einer hauptberuflichen selbstständigen Erwerbstätigkeit eine unselbstständige Nebentätigkeit ausüben (Art. 1j Abs. 1 lit. a BVV 2).
- **Invalide Personen**: Personen, die im Sinne der Invalidenversicherung (IV) zu mindestens 70 Prozent invalid sind (Art. 1j Abs. 1 lit. d BVV 2).
- **Familienglieder in der Landwirtschaft**: Im Betrieb mitarbeitende Familienglieder des Betriebsleiters in der Landwirtschaft (Art. 1j Abs. 1 lit. e BVV 2).

---

## Finanzierung und Vermögensaufbau im Kapitaldeckungsverfahren {#finanzierung-und-altersguthaben}

### Paritätische Finanzierung und Altersgutschriften (Art. 16 BVG) {#altersgutschriften-und-beitraege}

Die Finanzierung der Altersvorsorge erfolgt über Beiträge, die vom Arbeitgeber und Arbeitnehmer aufgebracht werden. Gemäss Art. 66 Abs. 1 BVG legt die Vorsorgeeinrichtung die Höhe der Beiträge im Reglement fest; der Beitrag des Arbeitgebers muss jedoch mindestens gleich gross sein wie die Gesamtheit der Beiträge seiner Arbeitnehmer (*Paritätsprinzip*). Der Arbeitgeber schuldet der Vorsorgeeinrichtung die gesamten Beiträge (Arbeitgeber- und Arbeitnehmeranteil) und zieht den Arbeitnehmeranteil monatlich vom Lohn ab (Art. 66 Abs. 2 und 3 BVG).

Die Beiträge finanzieren die Risikoprämien, Verwaltungskosten und die gesetzlichen **Altersgutschriften**. Die Altersgutschriften werden jährlich in Prozenten des koordinierten Lohns berechnet und dem individuellen Alterskonto gutgeschrieben:

{{< wortlaut gesetz="bvg" art="art-016" >}}

Die Staffelung der gesetzlichen Mindestaltersgutschriften steigt mit zunehmendem Alter markant an:

| Alterskategorie (vollendetes Altersjahr) | Altersgutschrift in % des koordinierten Lohns |
|---|---|
| **25 bis 34 Jahre** | 7 % |
| **35 bis 44 Jahre** | 10 % |
| **45 bis 54 Jahre** | 15 % |
| **55 bis Referenzalter (65)** | 18 % |

### Das Altersguthaben und die Mindestverzinsung (Art. 15 BVG) {#altersguthaben-und-zins}

Das für die spätere Rentenhöhe massgebende Altersguthaben setzt sich aus den einbezahlten Sparbeiträgen und den Zinsen zusammen:

{{< wortlaut gesetz="bvg" art="art-015" >}}

Das Altersguthaben besteht aus der Summe der Altersgutschriften samt Zinsen sowie den eingebrachten Freizügigkeitsleistungen und Einkaufsbeträgen. Der Bundesrat legt nach Anhörung der Eidgenössischen Kommission für die berufliche Vorsorge jährlich den gesetzlichen **Mindestzinssatz** fest (Art. 15 Abs. 2 BVG; 2024: 1.25 %, 2025/2026: 1.25 %). Dieser Zinssatz gilt zwingend für das Altersguthaben im gesetzlichen Obligatorium.

### Freiwilliger Einkauf und die dreijährige Sperrfrist (Art. 79b BVG) {#einkauf-und-sperrfrist}

Bestehen im Altersguthaben Beitragslücken (etwa infolge von Ausbildungszeiten, Lohnerhöhungen, Babypausen oder Zuzug aus dem Ausland), können Versicherte freiwillige Einkäufe leisten (Art. 79b BVG). Einkaufsbeiträge können vom steuerbaren Einkommen bei der direkten Bundessteuer sowie den Kantons- und Gemeindesteuern in voller Höhe abgezogen werden.

Um eine missbräuchliche Ausnutzung dieses Steuervorteils zu verhindern, sieht Art. 79b Abs. 3 BVG eine strenge **dreijährige Sperrfrist** vor: Wurden freiwillige Einkäufe getätigt, dürfen die daraus resultierenden Leistungen innerhalb der folgenden drei Jahre nicht in Kapitalform bezogen werden. Das Bundesgericht judiziert in ständiger Praxis streng teleologisch: «Das Ziel eines Einkaufs von Beitragsjahren besteht im Aufbau bzw. in der Verbesserung der beruflichen Vorsorge» ([BGE 142 II 399 E. 3.3.4](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_004_BGE-142-II-399_2016.html#consideration_3.3.4)). Werden innerhalb von drei Jahren nach einem Einkauf dennoch Altersleistungen in Kapitalform bezogen, verweigern die Steuerbehörden rückwirkend die steuerliche Abzugsfähigkeit des Einkaufs wegen Steuerumgehung. Einzige gesetzliche Ausnahme: der Wiedereinkauf nach einer Ehescheidung zur Wiederherstellung des Vorsorgeschutzes (Art. 79b Abs. 4 BVG; [BGE 142 II 399 E. 3.3.4](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_004_BGE-142-II-399_2016.html#consideration_3.3.4)).

---

## Auszahlung der Altersleistungen: Rentenbezug, Kapitalabfindung und Vorbezug {#auszahlung-der-altersleistungen}

### Der Grundsatz: Die lebenslange Altersrente und der Mindestumwandlungssatz (Art. 13 und 14 BVG) {#altersrente-und-umwandlungssatz}

Die Altersleistung wird bei Erreichen des Referenzalters fällig. Das Referenzalter der beruflichen Vorsorge entspricht nach der Reform AHV 21 dem Referenzalter der AHV (Alter 65 für Frauen und Männer, Art. 13 Abs. 1 BVG):

{{< wortlaut gesetz="bvg" art="art-013" >}}

Der gesetzliche Regelfall ist die Ausrichtung einer lebenslangen monatlichen Altersrente (Art. 37 Abs. 1 BVG). Die Höhe der jährlichen Altersrente bestimmt sich über den **Umwandlungssatz**:

{{< wortlaut gesetz="bvg" art="art-014" >}}

Im gesetzlichen Obligatorium beträgt der Mindestumwandlungssatz für das Referenzalter 65 unverändert **6.8 Prozent** (Art. 14 Abs. 2 BVG). Ein obligatorisches Altersguthaben von CHF 300'000.- ergibt demnach eine garantierte jährliche Altersrente von CHF 20'400.- (CHF 1'700.- pro Monat). 

Im überobligatorischen Bereich (umhüllende Kassen) wenden viele Pensionskassen tiefere umhüllende Umwandlungssätze an (oft zwischen 5.0 und 5.8 Prozent). Dies ist nach der Rechtsprechung zulässig, sofern die daraus resultierende Gesamrente nicht geringer ausfällt als die Rente, die sich aus dem BVG-Mindestguthaben mit 6.8 Prozent errechnet ([BGE 130 V 369 E. 6.1](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_007_BGE-130-V-369_2004.html#consideration_6.1); Schattenrechnung).

### Der Kapitalbezug (Kapitalabfindung nach Art. 37 BVG) {#kapitalbezug-und-abfindung}

Neben der Rente räumt das Gesetz den Versicherten einen Rechtsanspruch auf teilweisen oder vollständigen Kapitalbezug ein:

{{< wortlaut gesetz="bvg" art="art-037" >}}

Die Ausgestaltung des Kapitalbezugs folgt klaren Regeln:
- **Gesetzlicher Anspruch (Mindestanspruch)**: Nach Art. 37 Abs. 2 BVG hat jede versicherte Person das Recht zu verlangen, dass ihr **mindestens ein Viertel (25 %)** ihres obligatorischen Altersguthabens als einmalige Kapitalabfindung ausbezahlt wird ([BGE 141 V 355 E. 3.3](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_007_BGE-141-V-355_2015.html#consideration_3.3); [BGE 141 V 162 E. 4.5.1](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_007_BGE-141-V-162_2015.html#consideration_4.5.1)).
- **Reglementarischer Vollbezug**: Die Vorsorgeeinrichtung kann im Reglement vorsehen, dass die Versicherten anstelle der Rente eine vollständige Kapitalabfindung (bis zu 100 %) wählen dürfen (Art. 37 Abs. 4 lit. a BVG).
- **Fristen**: Die Kasse kann im Reglement verlangen, dass der Wunsch nach Kapitalabfindung mit einer bestimmten Vorankündigungsfrist (in der Praxis meist 1 bis 6 Monate vor der Pensionierung) schriftlich gemeldet werden muss (Art. 37 Abs. 4 lit. b BVG). Wer diese reglementarische Frist versäumt, verliert den überobligatorischen Kapitalanspruch und kann lediglich den gesetzlichen Viertel nach Art. 37 Abs. 2 BVG beanspruchen ([BGE 141 V 162 E. 4.5.1](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_007_BGE-141-V-162_2015.html#consideration_4.5.1)).
- **Bagatellabfindung**: Beträgt die berechnete Altersrente weniger als 10 Prozent der AHV-Mindestrente, kann die Vorsorgeeinrichtung die Rente zwangsweise durch eine einmalige Kapitalabfindung ablösen (Art. 37 Abs. 3 BVG).

### Das Erfordernis der schriftlichen Ehegattenzustimmung (Art. 37a BVG) {#ehegattenzustimmung}

Ein zentraler Schutzmechanismus im schweizerischen Recht ist das Zustimmungserfordernis des Partners bei Kapitalauszahlungen:

{{< wortlaut gesetz="bvg" art="art-037a" >}}

Ist die versicherte Person verheiratet oder lebt sie in eingetragener Partnerschaft, ist die Auszahlung einer Kapitalabfindung nur gültig, wenn der Ehegatte oder Partner **schriftlich zustimmt** (Art. 37a Abs. 1 BVG). In der Praxis verlangen die Reglemente der Pensionskassen regelmässig eine amtlich beglaubigte Unterschrift des Ehegatten. 

Zweck der Bestimmung ist der Schutz der Familie: Da der Bezug von Kapital das spätere Renteneinkommen mindert und den Anspruch auf Hinterlassenenrenten schmälert, soll der andere Ehepartner nicht vor vollendete Tatsachen gestellt werden. Verweigert der Ehegatte die Zustimmung grundlos oder kann sie nicht beigebracht werden (z. B. bei unbekanntem Aufenthalt), kann der Versicherte das Zivilgericht anrufen, um die Zustimmung gerichtlich ersetzen zu lassen (Art. 37a Abs. 1 Satz 2 BVG). Bis zur Beibringung der Zustimmung schuldet die Kasse keinen Verzugszins (Art. 37a Abs. 2 BVG). 

Zahlt eine Vorsorgeeinrichtung das Alterskapital ohne die erforderliche Zustimmung des Ehegatten aus, leistet sie nicht mit befreiender Wirkung und haftet dem geschädigten Ehegatten gegenüber auf erneute Leistungsausrichtung ([BGE 133 V 205 E. 4.3](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_007_BGE-133-V-205_2007.html#consideration_4.3)). Allerdings greift dieses Zustimmungserfordernis nur dort, wo das Gesetz es ausdrücklich statuiert: Das Bundesgericht verwarf eine Ausdehnung über den Wortlaut hinaus: «Die Ausdehnung des Zustimmungserfordernisses auf sämtliche Fälle der in Kapitalform ausgerichteten Leistungen der beruflichen Vorsorge ist indessen nur de lege ferenda möglich» ([BGE 134 V 182 E. 4.4](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_007_BGE-134-V-182_2008.html#consideration_4.4)).

### Vorzeitiger Altersrücktritt und Rentenaufschub (Art. 13 Abs. 2 und 3 BVG) {#vorbezug-und-aufschub}

Seit dem Inkrafttreten der Reform AHV 21 per 1. Januar 2024 ist der Leistungsbezug gesetzlich flexibilisiert:
- **Vorbezug**: Die Altersleistung kann ab dem vollendeten 63. Altersjahr von Gesetzes wegen vorbezogen werden (Art. 13 Abs. 2 BVG). Die Vorsorgeeinrichtungen können im Reglement ein noch tieferes Alter vorsehen, jedoch frühestens ab vollendetem 58. Altersjahr (Art. 13 Abs. 3 BVG i.V.m. Art. 1 Abs. 3 BVV 2). Bei einem Vorbezug wird der Umwandlungssatz versicherungsmathematisch gekürzt, weil das Kapital über eine längere statistische Lebenserwartung reichen muss.
- **Aufschub**: Wird die Erwerbstätigkeit über das Referenzalter hinaus fortgesetzt, kann der Rentenbezug bis höchstens zur Vollendung des 70. Altersjahres aufgeschoben werden (Art. 13 Abs. 2 BVG), was zu einem entsprechend höheren Umwandlungssatz führt.
- **Teilpensionierung**: Die Altersleistung kann schrittweise in bis zu drei Stufen bezogen werden, sofern die Erwerbstätigkeit entsprechend reduziert wird (Art. 13a BVG).

### Vorbezug für selbstbewohntes Wohneigentum (WEF, Art. 30a ff. BVG) {#wohneigentumsfoerderung-wef}

Versicherte können ihr Altersguthaben vor dem Pensionierungsalter für den Erwerb oder die Erstellung von Wohneigentum zum eigenen Bedarf, für wertvermehrende Umbauten oder zur Amortisation von Hypotheken einsetzen (**Wohneigentumsförderung mit Mitteln der beruflichen Vorsorge — WEF**, Art. 30a ff. BVG):
- **Mindestbetrag und Frequenz**: Ein WEF-Vorbezug muss mindestens CHF 20'000.- betragen (ausser beim Erwerb von Anteilen an Wohnbaugenossenschaften) und kann nur alle fünf Jahre geltend gemacht werden (Art. 30c Abs. 4 BVG). Bis zum vollendeten 50. Altersjahr kann das gesamte Guthaben bezogen werden; danach höchstens das Guthaben im Alter 50 oder die Hälfte des aktuellen Guthabens.
- **Veräusserungsbeschränkung**: Zur Sicherung des Vorsorgezwecks wird im Grundbuch von Amtes wegen eine Veräusserungsbeschränkung angemerkt (Art. 30d BVG). Wird die Liegenschaft später verkauft oder nicht mehr selbst bewohnt, muss der vorbezogene Betrag zwingend an die Vorsorgeeinrichtung zurückbezahlt werden.
- **Ehegattenzustimmung**: Auch der WEF-Vorbezug und die Verpfändung von Vorsorgeguthaben verlangen zwingend die schriftliche Zustimmung des Ehegatten (Art. 30c Abs. 5 BVG).
- **Ausschluss nach Eintritt des Vorsorgefalls**: Nach Eintritt eines Vorsorgefalls (Alter oder Invalidität) ist ein WEF-Vorbezug unwiderruflich ausgeschlossen ([BGE 130 V 191 E. 3](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_007_BGE-130-V-191_2004.html#consideration_3.)).

### Barauszahlung der Freizügigkeitsleistung bei Beendigung vor dem Rentenalter (Art. 5 FZG) {#barauszahlung-fzg}

Endet das Arbeitsverhältnis vor Erreichen des Rentenalters, verlässt die versicherte Person die Vorsorgeeinrichtung. In diesem Moment entsteht der Anspruch auf eine **Austrittsleistung** (Freizügigkeitsleistung):

{{< wortlaut gesetz="fzg" art="art-002" >}}

Der fundamentale Grundsatz lautet: **Erhaltung des Vorsorgeschutzes**. Die Freizügigkeitsleistung darf nicht konsumiert werden, sondern muss zwingend an die Vorsorgeeinrichtung des neuen Arbeitgebers oder auf eine Freizügigkeitspolice bzw. ein Freizügigkeitskonto überwiesen werden. Das Bundesgericht betont, «dass sie sich nach erfolgtem Bezug ihres Freizügigkeitsguthabens nicht mehr auf den Vorsorgeschutz gemäss Art. 2 ff. und Art. 20 ff. FZG sowie Art. 10 ff. FZV berufen kann» ([BGE 148 V 114 E. 7.2.1](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_007_BGE-148-V-114_2022.html#consideration_7.2.1)).

Eine **Barauszahlung** der Freizügigkeitsleistung an die austretende Person ist von Gesetzes wegen nur in drei eng umgrenzten Ausnahmefällen zulässig:

{{< wortlaut gesetz="fzg" art="art-005" >}}

Die drei gesetzlichen Barauszahlungsgründe nach Art. 5 Abs. 1 FZG lauten:

1. **Endgültiges Verlassen der Schweiz (Auswanderung, lit. a)**: Verlegt die versicherte Person ihren Wohnsitz definitiv ins Ausland. **Massgebliche Einschränkung durch Art. 25f FZG**: Wandert die Person in einen Mitgliedstaat der Europäischen Union (EU) oder der EFTA aus und untersteht sie dort weiterhin den gesetzlichen Pflichtversicherungen für Alter, Tod und Invalidität, ist die Barauszahlung für den Teil des BVG-Obligatoriums gesetzlich verboten ([BGE 134 V 170 E. 3.1](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_007_BGE-134-V-170_2008.html#consideration_3.1)). Nur das Überobligatorium darf bar bezogen werden; das obligatorische BVG-Guthaben muss auf einem Schweizer Freizügigkeitskonto deponiert bleiben, bis das Rentenalter erreicht ist.
2. **Aufnahme einer selbstständigen Erwerbstätigkeit (lit. b)**: Nimmt der Versicherte eine hauptberufliche selbstständige Erwerbstätigkeit auf und untersteht er nicht mehr der obligatorischen beruflichen Vorsorge. Die Aufnahme der Selbstständigkeit ist durch die Bestätigung der zuständigen AHV-Ausgleichskasse nachzuweisen.
3. **Geringfügigkeit (lit. c)**: Ist die Austrittsleistung geringer als der persönliche Jahresbeitrag des Arbeitnehmers bei der bisherigen Vorsorgeeinrichtung.

Auch für die Barauszahlung nach Art. 5 FZG verlangt Abs. 2 zwingend die schriftliche Zustimmung des Ehegatten: Das Bundesgericht judiziert strikt, «wonach bei verheirateten Anspruchsberechtigten die Barauszahlung nur zulässig ist, wenn der Ehegatte schriftlich zustimmt» ([BGE 133 V 205 E. 4.3](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_007_BGE-133-V-205_2007.html#consideration_4.3)). Wer freiwillig auf die Geltendmachung eines ihm zustehenden Barauszahlungsanspruchs verzichtet, muss sich das Guthaben bei der Bedürftigkeitsprüfung (z. B. für unentgeltliche Rechtspflege) dennoch als liquides Vermögen anrechnen lassen ([BGE 135 I 288 E. 2.4](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_001_BGE-135-I-288_2009.html#consideration_2.4)).

### Steuerliche Behandlung der Auszahlung {#steuerliche-behandlung}

Die steuerliche Behandlung unterscheidet fundamental zwischen Rentenbezug und Kapitalabfindung:
- **Rentenleistungen**: Laufende Altersrenten aus der 2. Säule sind gemäss Art. 22 des Bundesgesetzes über die direkte Bundessteuer (DBG, SR 642.11) zu **100 Prozent als ordentliches Einkommen** steuerbar. Zusammen mit den AHV-Renten unterliegen sie der vollen Einkommenssteuerprogression.
- **Kapitalleistungen**: Einmalige Kapitalabfindungen bei Pensionierung, Vorbezüge für Wohneigentum (WEF) sowie Barauszahlungen nach Art. 5 FZG werden gemäss Art. 38 DBG und den entsprechenden kantonalen Steuergesetzen **getrennt vom übrigen Einkommen** besteuert. Sie unterliegen einer stark reduzierten Sondersteuer (bei der direkten Bundessteuer zu einem Fünftel des ordentlichen Steuertarifs; in den Kantonen gelten ähnliche Privilegierungen). Guthaben auf Freizügigkeitskonten sind bis zum Bezug von der Vermögens- und Ertragssteuer befreit.

---

## Rechtsweg und Verfahren nach Art. 73 BVG {#rechtsweg-und-verfahren}

Im Unterschied zur 1. Säule (AHV), in der öffentlich-rechtliche Ausgleichskassen formelle Verfügungen nach dem ATSG erlassen, ist das Rechtspflegesystem der beruflichen Vorsorge gerichtlich ausgestaltet:

{{< wortlaut gesetz="bvg" art="art-073" >}}

Das Bundesgericht hat wiederholt die Besonderheit dieses Verfahrens herausgearbeitet:
1. **Keine Verfügungsgewalt der Kassen**: Vorsorgeeinrichtungen sind keine Verwaltungsbehörden. Schreiben, Leistungsabrechnungen oder Rückforderungsbegehren einer Pensionskasse stellen keine Verfügungen dar, sondern blosse Willenserklärungen. Das Bundesgericht hält ausdrücklich fest, «dass die Vorsorgeeinrichtungen im Rahmen von Art. 73 BVG praxisgemäss […] keine Verfügungskompetenz besitzen» ([BGE 129 V 27 E. 2.1.1](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_007_BGE-129-V-27_2003.html#consideration_2.1.1)).
2. **Direkte Klage beim Berufsvorsorgegericht**: Streitigkeiten zwischen Vorsorgeeinrichtungen, Arbeitgebern und Anspruchsberechtigten werden durch direkte Klage vor dem vom jeweiligen Kanton bezeichneten Berufsvorsorgegericht (in der Regel das kantonale Versicherungs- oder Sozialversicherungsgericht) ausgetragen (Art. 73 Abs. 1 BVG).
3. **Örtliche Zuständigkeit**: Örtlich zuständig ist das Gericht am schweizerischen Sitz oder Wohnsitz des Beklagten oder am Ort des Betriebes, bei dem der Versicherte angestellt war (Art. 73 Abs. 3 BVG).
4. **Verfahrensgrundsätze**: Das Verfahren vor dem kantonalen Gericht ist einfach, rasch und in der Regel für die Parteien kostenlos (Art. 73 Abs. 2 BVG). Es gilt der Untersuchungsgrundsatz, wonach das Gericht den Sachverhalt von Amtes wegen feststellt.
5. **Weiterzug an das Bundesgericht**: Gegen Urteile des kantonalen Berufsvorsorgegerichts steht die Beschwerde in öffentlich-rechtlichen Angelegenheiten an das Bundesgericht (sozialrechtliche Abteilungen in Luzern) offen (Art. 82 lit. a, Art. 86 Abs. 1 lit. d BGG).
6. **Verjährung**: Periodische Beiträge und Leistungen verjähren nach fünf Jahren, übrige Ansprüche nach zehn Jahren (Art. 41 Abs. 1 BVG). Ansprüche auf Altersleistungen sind jedoch nach Art. 41 Abs. 2 BVG unverjährbar, solange die versicherte Person lebt.

---

## Praxishinweise {#praxishinweise}

### Für Arbeitnehmende und Versicherte {#hinweise-arbeitnehmende}

1. **Vorsorgeausweis jährlich analysieren**: Auf dem jährlichen Pensionskassenausweis sind die wichtigsten Eckwerte ersichtlich: das aktuelle Altersguthaben, der versicherte und koordinierte Lohn, die voraussichtlichen Altersrenten im Referenzalter sowie das maximal mögliche freiwillige Einkaufspotenzial.
2. **Entscheidung Rente oder Kapitalbezug frühzeitig planen**: Der Entscheid zwischen monatlicher Altersrente und Kapitalbezug ist bei Auszahlung endgültig und irreversibel:
   - *Vorteile Rente*: Lebenslange finanzielle Absicherung, kein individuelles Anlagerisiko, automatische Hinterlassenenrente für den überlebenden Ehepartner.
   - *Vorteile Kapital*: Volle Dispositionsfreiheit über das Vermögen, Vererbbarkeit an Nachkommen bei vorzeitigem Versterben, Reduktion der Steuerbelastung durch Sondersteuersatz (wobei das Kapital danach der Vermögenssteuer unterliegt).
3. **Reglementarische Meldefristen beachten**: Wer einen Kapitalbezug plant, muss zwingend die Fristen im Vorsorgereglement prüfen. Versäumte Fristen können dazu führen, dass die Pensionskasse den überobligatorischen Kapitalbezug ablehnen darf und nur der gesetzliche Mindestanteil von 25 % ausbezahlt wird ([BGE 141 V 162 E. 4.5.1](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_007_BGE-141-V-162_2015.html#consideration_4.5.1)).
4. **Ehegattenzustimmung rechtzeitig beibringen**: Bei Verheirateten ist für Kapitalbezüge (Art. 37a BVG), WEF-Vorbezüge (Art. 30c Abs. 5 BVG) und Barauszahlungen (Art. 5 Abs. 2 FZG) zwingend die schriftliche, meist amtlich beglaubigte Zustimmung des Partners erforderlich. Ohne diese Unterschrift darf die Kasse kein Geld überweisen.
5. **3-Jahres-Sperrfrist bei Einkäufen einhalten (Art. 79b Abs. 3 BVG)**: Wer plant, sich kurz vor der Pensionierung in die Pensionskasse einzukaufen, um Steuern zu sparen, muss zwischen dem letzten Einkauf und dem Kapitalbezug zwingend eine Frist von mindestens drei vollen Jahren einhalten ([BGE 142 II 399 E. 3.3.4](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_004_BGE-142-II-399_2016.html#consideration_3.3.4)). Andernfalls wird der Steuerabzug nachträglich widerrufen.
6. **Lücken bei Stellenwechsel vermeiden**: Beim Verlassen einer Arbeitsstelle ohne unmittelbare Folgeanstellung muss das Freizügigkeitsguthaben auf ein Freizügigkeitskonto transferiert werden. Das Guthaben sollte aktiv nachgeführt werden; über die Zentralstelle 2. Säule kann nach vergessenen Guthaben gesucht werden.

### Für Arbeitgeber {#hinweise-arbeitgeber}

1. **Gesetzliche Anschlusspflicht (Art. 11 BVG)**: Jeder Arbeitgeber, der obligatorisch zu versichernde Arbeitnehmende beschäftigt, muss einer im Register eingetragenen Vorsorgeeinrichtung angeschlossen sein. Versäumt der Arbeitgeber den Anschluss, schliesst ihn die Auffangeinrichtung rückwirkend zwangsweise an (Art. 12 und 60 BVG).
2. **Überwachung der Eintrittsschwelle bei Stundenlöhnern**: Bei schwankenden Pensen oder Stundenlöhnen ist laufend zu überwachen, ob das hochgerechnete Jahresgehalt die Eintrittsschwelle von CHF 22'680.- übersteigt. Tritt die Versicherungspflicht ein, muss die Anmeldung bei der Pensionskasse unverzüglich erfolgen.
3. **Paritätische Beitragsabführung und Haftung**: Der Arbeitgeber schuldet der Vorsorgeeinrichtung die gesamten Beiträge (Art. 66 Abs. 2 BVG). Behält der Arbeitgeber die vom Lohn abgezogenen Arbeitnehmerbeiträge ein, ohne sie an die Pensionskasse weiterzuleiten, macht er sich strafbar (Art. 76 BVG) und haftet den Organen und Arbeitnehmenden persönlich für den entstandenen Schaden.

---

## Leitentscheide {#leitentscheide}

Die folgende Tabelle fasst die massgeblichen Bundesgerichtsentscheide zur Organisation, zur Versicherungspflicht und zur Auszahlung der beruflichen Vorsorge zusammen:

| Entscheid | Gegenstand | Kernaussage und Bedeutung |
|---|---|---|
| [BGE 130 I 205 E. 6.2](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_001_BGE-130-I-205_2004.html#consideration_6.2) | Verfassungsauftrag der 2. Säule (Art. 113 BV) | Die berufliche Vorsorge soll zusammen mit der AHV die Fortsetzung der gewohnten Lebenshaltung in angemessener Weise ermöglichen; Unterscheidung zwischen BVG-Obligatorium (Säule 2a) und Überobligatorium (Säule 2b). |
| [BGE 130 V 369 E. 6.1](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_007_BGE-130-V-369_2004.html#consideration_6.1) | Autonomie und Schattenrechnung (Art. 49 und 6 BVG) | Gesetzliche Mindestvorschriften des BVG binden umhüllende Kassen; im überobligatorischen Bereich geniessen Einrichtungen Satzungsautonomie, dürfen aber das BVG-Minimum insgesamt nicht unterschreiten. |
| [BGE 129 V 132 E. 3.1, 3.4.5](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_007_BGE-129-V-132_2003.html#consideration_3.1) | Mehrfachbeschäftigung und Versicherungspflicht (Art. 2 und 7 BVG) | Bei mehreren nebeneinander ausgeübten gleichwertigen Erwerbstätigkeiten oberhalb der Eintrittsschwelle besteht bei den Vorsorgeeinrichtungen beider Arbeitgeber eine eigenständige obligatorische Versicherungspflicht. |
| [BGE 120 V 15 E. 2.](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_007_BGE-120-V-15_1994.html#consideration_2.) | Beginn des Versicherungsverhältnisses (Art. 10 BVG) | Die obligatorische Versicherung beginnt von Gesetzes wegen mit dem Antritt des Arbeitsverhältnisses; Doppelversicherungen im Obligatorium sind ausgeschlossen. |
| [BGE 141 V 355 E. 3.3](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_007_BGE-141-V-355_2015.html#consideration_3.3) | Anspruch auf Kapitalabfindung (Art. 37 Abs. 2 BVG) | Der gesetzliche Anspruch auf Auszahlung von mindestens einem Viertel des Altersguthabens gilt zwingend für Altersleistungen im BVG-Obligatorium, ist jedoch bei bestehender ganzer Invalidenrente ausgeschlossen. |
| [BGE 141 V 162 E. 3.3.1, 4.5.1](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_007_BGE-141-V-162_2015.html#consideration_3.3.1) | Reglementarische Fristen für Kapitalbezug | Auslegung von Vorsorgereglementen nach dem Vertrauensprinzip; bei Versäumung reglementarischer Vorankündigungsfristen für die Kapitalabfindung besteht lediglich Anspruch auf das gesetzliche Viertel nach Art. 37 Abs. 2 BVG. |
| [BGE 134 V 182 E. 4.4](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_007_BGE-134-V-182_2008.html#consideration_4.4) | Grenzen der Ehegattenzustimmung | Keine gesetzliche Lücke: Das Erfordernis der schriftlichen Zustimmung des Ehegatten gilt nur dort, wo das Gesetz es ausdrücklich statuiert (z. B. Art. 37a BVG, Art. 5 Abs. 2 FZG), nicht jedoch für alle Freizügigkeitsleistungen schlechthin. |
| [BGE 133 V 205 E. 4.3](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_007_BGE-133-V-205_2007.html#consideration_4.3) | Haftung bei fehlender Ehegattenzustimmung (Art. 5 Abs. 2 FZG) | Leistet eine Vorsorgeeinrichtung eine Barauszahlung ohne schriftliche Zustimmung des Ehegatten, leistet sie mangels Gutgläubigkeit nicht mit befreiender Wirkung und haftet bei Scheidung auf erneute Auszahlung. |
| [BGE 142 II 399 E. 3.3.4](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_004_BGE-142-II-399_2016.html#consideration_3.3.4) | Einkauf und 3-jährige Sperrfrist (Art. 79b Abs. 3 BVG) | Zweck des Einkaufs ist der Vorsorgeaufbau; ein Kapitalbezug innert drei Jahren nach dem Einkauf führt zur steuerlichen Verweigerung des Einkaufsabzugs wegen Steuerumgehung (Ausnahme: Wiedereinkauf nach Scheidung). |
| [BGE 134 V 170 E. 3.1](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_007_BGE-134-V-170_2008.html#consideration_3.1) | Keine Versicherungspflicht für Selbstständige (Art. 4 BVG, Art. 25f FZG) | Selbstständige sind dem BVG-Obligatorium nicht unterstellt; bei Auswanderung in einen EU/EFTA-Staat ist die Barauszahlung des BVG-Obligatoriums nach Art. 25f FZG ausgeschlossen. |
| [BGE 129 V 27 E. 2.1.1](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_007_BGE-129-V-27_2003.html#consideration_2.1.1) | Fehlen hoheitlicher Verfügungsgewalt (Art. 73 BVG) | Vorsorgeeinrichtungen besitzen keine hoheitliche Verfügungskompetenz; Streitigkeiten sind durch direkte Klage vor dem kantonalen Berufsvorsorgegericht auszutragen. |
| [BGE 151 V 144 E. 6.1](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_007_BGE-151-V-144_2025.html#consideration_6.1) | Auslegung von Vorsorgereglementen | Reglemente privatrechtlicher Vorsorgeeinrichtungen sind nach dem Vertrauensprinzip sowie der Unklarheits- und Ungewöhnlichkeitsregel wie vorformulierte Allgemeine Versicherungsbedingungen auszulegen. |
| [BGE 135 I 288 E. 2.4](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_001_BGE-135-I-288_2009.html#consideration_2.4) | Freizügigkeitsleistung und Bedürftigkeit (Art. 5 FZG) | Wer freiwillig auf die Barauszahlung einer fälligen Freizügigkeitsleistung verzichtet, muss sich das Guthaben bei der Beurteilung der Bedürftigkeit für unentgeltliche Rechtspflege als Vermögen anrechnen lassen. |
| [BGE 148 V 114 E. 7.2.1](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_007_BGE-148-V-114_2022.html#consideration_7.2.1) | Grundsatz der Erhaltung des Vorsorgeschutzes (Art. 2 ff. FZG) | Nach tatsächlichem Bezug des Freizügigkeitskapitals erlischt der besondere vorsorgerechtliche Schutz und die Unpfändbarkeit nach SchKG. |

---

## Literatur {#literatur}

- Thomas Flückiger (Hrsg.), Praxiskommentar zum Bundesgesetz über die berufliche Alters-, Hinterlassenen- und Invalidenvorsorge (BVG), Bern 2019.
- Bettina Kahil-Wolff / Isabelle Vetter-Schreiber (Hrsg.), BVG und FZG, Handkommentar, 2. Aufl., Bern 2021.
- Ueli Kieser, Schweizerisches Sozialversicherungsrecht, 2. Aufl., Zürich 2020.
- Jacques-André Schneider / Guy Longchamp (Hrsg.), Commentaire LPP et LFLP, Bern 2010.
- Hans-Ulrich Stauffer, Berufliche Vorsorge, 3. Aufl., Zürich 2020.
- Isabelle Vetter-Schreiber, Berufliche Vorsorge: Kommentar zu BVG und FZG, 4. Aufl., Zürich 2021.
