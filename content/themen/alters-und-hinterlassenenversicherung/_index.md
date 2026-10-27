---
title: "Alters- und Hinterlassenenversicherung (AHV): System, Anspruchsvoraussetzungen und Revisionen"
date: 2026-10-27
lastmod: 2026-10-27
description: "Systematische Darstellung der 1. Säule (AHV): Verfassungsauftrag (Art. 112 BV), Versicherungskreis, Beitragsstatut und Finanzierung im Umlageverfahren, Anspruchsvoraussetzungen für Alters-, Hinterlassenen- und Hilflosenleistungen, Rentenflexibilisierung (AHV 21), Rentenberechnung (Splitting, Erziehungsgutschriften, Plafonierung) sowie Exkurs zu den aktuellen Revisionsbestrebungen (13. AHV-Rente, EGMR Beeler)."
tags: ["AHV", "AHVG", "Altersrente", "Hinterlassenenrente", "1. Säule", "Umlageverfahren", "Beitragspflicht", "Referenzalter", "AHV 21", "13. AHV-Rente", "Rentenplafonierung", "Sozialversicherungsrecht"]
typ: institution
kurz: "Die Alters- und Hinterlassenenversicherung (AHV) bildet als obligatorische Volksversicherung das Fundament der 1. Säule und soll den verfassungsrechtlichen Existenzbedarf bei Alter und Tod sichern. Finanziert im Umlageverfahren über paritätische Lohnbeiträge, Beiträge Selbständiger und Nichterwerbstätiger sowie Bundesmittel, setzt der Anspruch auf eine ordentliche Rente mindestens ein volles Beitragsjahr voraus. Die Höhe der Altersrente bemisst sich nach Beitragsdauer und Erwerbseinkommen unter Einbezug von Splitting, Erziehungs- und Betreuungsgutschriften sowie der Plafonierung auf maximal 150 Prozent für Ehepaare."
sachgebiete: [ahv]
normen:
  - { gesetz: bv, art: art-112 }
  - { gesetz: ahvg, art: art-001a }
  - { gesetz: ahvg, art: art-005 }
  - { gesetz: ahvg, art: art-010 }
  - { gesetz: ahvg, art: art-021 }
  - { gesetz: ahvg, art: art-023 }
  - { gesetz: ahvg, art: art-029 }
  - { gesetz: ahvg, art: art-035 }
  - { gesetz: ahvg, art: art-040b }
  - { gesetz: ahvg, art: art-052 }
stichworte: ["AHV", "AHVG", "Umlageverfahren", "Referenzalter", "Rentenflexibilisierung", "Beitragspflicht", "Selbständigerwerbende", "Nichterwerbstätige", "Einkommenssplitting", "Erziehungsgutschriften", "Plafonierung", "Witwerrente", "13. AHV-Rente", "Beeler"]
agent_verified: true
revisions:
  - date: 2026-10-27
    by: "Antigravity"
    model: "gemini-3.8-flash"
    mcp_verified: true
    note: "Erstfassung nach Skill glossagens-themen (Typ institution). Verfassungs- und Gesetzeswortlaute per {{< wortlaut >}} aus amtlicher Fedlex-Quelle eingebunden (scripts/wortlaut.py). Zwölf Leitentscheide von entscheidsuche.ch im Volltext verifiziert; Erwägungsnummern, Anker (#consideration_...) und wörtliche Zitate «...» vollständig mechanisch abgeglichen (pruefen.py ohne Befund)."
---

## Überblick {#ueberblick}

Die **Alters- und Hinterlassenenversicherung (AHV)** ist das verfassungsrechtliche und gesellschaftliche Kernstück des schweizerischen Sozialstaates. Als obligatorische Volksversicherung erfasst sie grundsätzlich die gesamte Wohnbevölkerung und alle in der Schweiz erwerbstätigen Personen. Zusammen mit der Invalidenversicherung (IV) und den bedarfsabhängigen Ergänzungsleistungen (EL) bildet sie die **1. Säule** der schweizerischen Alters- und Hinterlassenvorsorge (Art. 111 und Art. 112 BV).

Das Bundesgericht hebt seit Jahrzehnten den grundlegenden Charakter dieser Verfassungsordnung hervor: «Die schweizerische Alters-, Hinterlassenen- und Invalidenvorsorge beruht auf der so genannten Dreisäulenkonzeption, die seit 1972 in der Bundesverfassung verankert ist» ([BGE 130 I 205 E. 6](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_001_BGE-130-I-205_2004.html#consideration_6.)). Während die 2. Säule (berufliche Vorsorge) und die 3. Säule (private Selbstvorsorge) im Kapitaldeckungsverfahren finanziert werden und auf die Fortsetzung der gewohnten Lebenshaltung zielen, erfüllt die AHV einen elementaren verfassungsrechtlichen Versorgungsauftrag: Sie soll den grundlegenden **Existenzbedarf** bei Eintritt des Alters oder im Todesfall für die Hinterbliebenen angemessen sichern (Art. 112 Abs. 2 lit. b BV).

Charakteristisch für die AHV ist ihre doppelte Solidaritätsfunktion: Einerseits verwirklicht sie den **Generationenvertrag** über das reine Umlageverfahren, in welchem die arbeitende Generation mit ihren laufenden Beiträgen direkt die Renten der aktuellen Rentnergeneration finanziert. Andererseits bewirkt sie eine ausgeprägte **soziale Umverteilung von wohlhabenden zu einkommensschwächeren Versicherten**: Beiträge auf dem Erwerbseinkommen werden ohne jede Obergrenze (*Plafond*) erhoben, während die daraus resultierenden Renten nach oben strikt auf den Maximalbetrag der Rentenskala begrenzt sind (Verhältnis der Maximalrente zur Minimalrente genau 2:1, Art. 112 Abs. 2 lit. c BV, Art. 34 AHVG).

Dieses Thema analysiert die verfassungsrechtlichen und gesetzlichen Grundlagen der AHV, stellt den Versicherungskreis und das Beitragsstatut dar, erläutert die materiellen Anspruchsvoraussetzungen für Alters-, Hinterlassenen- und Hilflosenleistungen, zerlegt die mathematischen und rechtlichen Mechanismen der Rentenberechnung (Splitting, Erziehungsgutschriften, Plafonierung) und widmet sich in einem abschliessenden Exkurs den gegenwärtigen Revisionsbestrebungen rund um die Reform AHV 21, die 13. AHV-Rente und das EGMR-Urteil *Beeler*.

## Verfassungsrechtliches Fundament und Systemarchitektur {#verfassungsgrundlagen}

### Verfassungsauftrag nach Art. 112 BV {#art-112-bv}

Die Verfassungskompetenz und die tragenden Strukturprinzipien der 1. Säule sind in Art. 112 BV niedergelegt:

{{< wortlaut gesetz="bv" art="art-112" >}}

Aus Art. 112 BV ergeben sich vier zwingende Eckwerte für den Bundesgesetzgeber:
1. **Obligatorium (Volksversicherung)**: Die Versicherung ist allgemein und obligatorisch (Abs. 2 lit. a). Es gibt im Anwendungsbereich des Bundesgesetzes über die Alters- und Hinterlassenenversicherung (AHVG, SR 831.10) keine Befreiungstatbestände aus privaten Vorsorgegründen oder wegen individuellen Reichtums.
2. **Existenzsicherung**: Die Renten haben den Existenzbedarf angemessen zu decken (Abs. 2 lit. b). Reicht eine Rente im Einzelfall zusammen mit eigenem Einkommen und Vermögen nicht zur Deckung des Existenzbedarfs aus, besteht ein Rechtsanspruch auf Ergänzungsleistungen (Art. 112a BV; vgl. das Thema [Ergänzungsleistungen zur AHV und IV](/themen/ergaenzungsleistungen/)).
3. **Bandbreite der Renten**: Das Gesetz setzt eine Mindest- und eine Höchstrente fest, wobei die Höchstrente höchstens das Doppelte der Mindestrente betragen darf (Abs. 2 lit. c; Art. 34 AHVG).
4. **Finanzierungsmix**: Die Finanzierung erfolgt vorrangig durch Beiträge der Versicherten und der Arbeitgeber sowie subsidiär durch Zuschüsse des Bundes (Abs. 3).

### Das Umlageverfahren und der Generationenvertrag {#umlageverfahren}

Im Unterschied zur beruflichen Vorsorge (BVG), die nach dem Kapitaldeckungsverfahren organisiert ist (Ansparen eines individuellen Altersguthabens), folgt die AHV dem **Umlageverfahren** (*Pay-as-you-go*): Die in einem Kalenderjahr eingenommenen Beitrags- und Steuermittel werden im selben Zeitraum unmittelbar zur Auszahlung der laufenden Renten verwendet. 

Zur Glättung kurzfristiger Einnahmenschwankungen und konjunktureller Zyklen führt die AHV einen gesetzlichen Reservefonds, den **AHV-Ausgleichsfonds** (verwaltet durch die öffentlich-rechtliche Anstalt *compenswiss*, Art. 107 ff. AHVG). Gesetzliches Ziel ist es, dass der Fondsstand in der Regel nicht unter die Ausgaben eines Jahres sinken soll (Art. 107 Abs. 3 AHVG).

Die Einnahmen der AHV setzen sich aus drei Hauptquellen zusammen:
- **Beiträge der Versicherten und Arbeitgeber**: Paritätische Lohnbeiträge von Unselbständigerwerbenden (8,7 % für AHV, je 4,35 % zu Lasten von Arbeitnehmer und Arbeitgeber, Art. 5 und Art. 13 AHVG; zusammen mit IV und EO total 10,6 %), Beiträge von Selbständigerwerbenden (sinkende Skala bis zu 8,1 % AHV) und Beiträge Nichterwerbstätiger.
- **Bundesbeitrag**: Der Bund trägt gesetzlich einen festen Anteil an den Gesamtausgaben der AHV (Art. 103 AHVG).
- **Zweckgebundene Fiskalbeiträge**: Einnahmen aus der Mehrwertsteuer (MwSt-Promillepunkte für die AHV, Art. 130 Abs. 3bis und Abs. 3ter BV) sowie der Spielbankenabgabe und der Tabaksteuer.

### Organisation und Durchführung: Ausgleichskassen und Bundesaufsicht {#organisation}

Die Durchführung der AHV ist historisch gewachsen und bewusst **dezentral und miliznah** ausgestaltet (Art. 49 ff. AHVG):
- **Verbandsausgleichskassen**: Gegründet von Gründerverbänden der Wirtschaft und Berufsverbänden (Art. 53 AHVG). Sie wickeln den Beitragsbezug und die Rentenauszahlung für ihre angeschlossenen Mitgliedsunternehmen ab.
- **Kantonale Ausgleichskassen**: Jeder Kanton führt eine kantonale Ausgleichskasse als öffentlich-rechtliche Anstalt (oft integriert in die Sozialversicherungsanstalten, SVA), die für alle nicht verbandlich organisierten Arbeitgeber, für Selbständige und für Nichterwerbstätige zuständig ist (Art. 61 AHVG).
- **Eidgenössische Ausgleichskasse (EAK)** und **Schweizerische Ausgleichskasse (SAK)** in Genf: Die EAK betreut das Bundespersonal und bundesnahe Betriebe; die SAK vollzieht die freiwillige Versicherung und zahlt Renten an Personen mit Wohnsitz im Ausland aus.
- **Zentrale Ausgleichsstelle (ZAS)**: Führt die zentralen Register, verwaltet die Individuellen Konten (IK) über die gesamte Schweiz und koordiniert den Finanzausgleich zwischen den Kassen.
- **Aufsicht**: Die administrative und fachliche Aufsicht über alle Durchführungsstellen liegt beim Bundesamt für Sozialversicherungen (BSV, Art. 72 AHVG).

## Versicherungskreis und Beitragspflicht {#versicherungskreis-und-beitraege}

### Obligatorische Versicherung nach Art. 1a AHVG {#obligatorische-versicherung}

Wer in der schweizerischen AHV versichert ist, bestimmt sich nach dem Territorialitäts- und Wohnsitzprinzip in Art. 1a AHVG:

{{< wortlaut gesetz="ahvg" art="art-001a" >}}

Der Versicherungskreis knüpft an zwei alternative Anknüpfungspunkte an:
1. **Wohnsitz in der Schweiz**: Massgebend ist der zivilrechtliche Wohnsitzbegriff (Art. 13 Abs. 1 ATSG i.V.m. Art. 23 ff. ZGB). Wer in der Schweiz mit der Absicht dauernden Verbleibens weilt, untersteht unabhängig von Staatsangehörigkeit oder Erwerbstätigkeit der Versicherung.
2. **Erwerbsort in der Schweiz**: Wer in der Schweiz eine Erwerbstätigkeit ausübt (z. B. Grenzgängerinnen und Grenzgänger), ist für diese Erwerbstätigkeit obligatorisch versichert, selbst wenn der Wohnsitz im Ausland liegt (vorbehältlich vorrangiger zwischenstaatlicher Abkommen, namentlich der Koordinationsverordnungen [EG] Nr. 883/2004 und 987/2009 im Geltungsbereich des FZA).

Personen, die ausserhalb der Schweiz leben, können sich unter engen gesetzlichen Voraussetzungen (insbesondere nach fünfjähriger ununterbrochener Vorversicherung) der **freiwilligen Versicherung** anschliessen (Art. 2 AHVG).

### Beitragsstatut: Unselbständige, Selbständige und Nichterwerbstätige {#beitragsstatut}

Das Beitragsrecht der AHV differenziert strikt nach dem wirtschaftlichen Status der versicherten Person. Die Beitragspflicht beginnt am 1. Januar nach Vollendung des 17. Altersjahres für Erwerbstätige und am 1. Januar nach Vollendung des 20. Altersjahres für Nichterwerbstätige (Art. 3 Abs. 1 AHVG). Sie dauert grundsätzlich bis zum Erreichen des gesetzlichen Referenzalters fort; bei Erwerbstätigkeit über das Referenzalter hinaus besteht die Beitragspflicht unter Gewährung eines Freibetrags weiter (Art. 4 Abs. 2 AHVG).

#### 1. Unselbständigerwerbende (Art. 5 AHVG) {#unselbststaendige}

{{< wortlaut gesetz="ahvg" art="art-005" >}}

Beitragspflichtig ist der **massgebende Lohn**: jedes Entgelt für in unselbständiger Stellung geleistete Arbeit ([Art. 5 Abs. 2 AHVG](/kommentar/ahvg/art-005/)). Im Beitragsrecht gilt das strikte **Quellenabzugsprinzip**: Die versicherte Arbeitnehmerin bzw. der Arbeitnehmer schuldet ihren Beitrag, doch der Arbeitgeber ist gesetzlich verpflichtet, diesen bei jeder Lohnzahlung in Abzug zu bringen und zusammen mit seinem paritätischen Arbeitgeberanteil an die Ausgleichskasse abzuliefern:

> «Im Beitragssystem der AHV (und der mit ihr verbundenen Versicherungszweige) ist die versicherte erwerbstätige Person grundsätzlich beitragspflichtig für den Arbeitnehmeranteil ( Art. 3 Abs. 1 und Art. 5 Abs. 1 AHVG ). Der Arbeitgeber hat die Beiträge vom Einkommen aus unselbstständiger Erwerbstätigkeit bei jeder Lohnzahlung in Abzug zu bringen und zusammen mit dem Arbeitgeberbeitrag periodisch zu entrichten ( Art. 14 Abs. 1 AHVG ). Es gilt das Prinzip der Beitragserhebung an der Quelle» ([BGE 147 V 174 E. 6.1](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_007_BGE-147-V-174_2021.html#consideration_6.1)).

Ob eine Tätigkeit als selbständig oder unselbständig einzustufen ist, beurteilt sich nach gefestigter Praxis nicht nach den zivilrechtlichen Bezeichnungen der Parteien, sondern nach den realen wirtschaftlichen Gegebenheiten:

> «Nach der Rechtsprechung beurteilt sich die Frage, ob im Einzelfall selbständige oder unselbständige Erwerbstätigkeit vorliegt, nicht aufgrund der Rechtsnatur des Vertragsverhältnisses zwischen den Parteien. Entscheidend sind vielmehr die wirtschaftlichen Gegebenheiten.» ([BGE 144 V 111 E. 4.2](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_007_BGE-144-V-111_2018.html#consideration_4.2)).

Massgebende Kriterien für die Unselbständigkeit sind das Vorliegen eines Subordinationsverhältnisses (Weisungsgebundenheit), die Eingliederung in eine fremde Arbeitsorganisation, das Fehlen eines eigenen Unternehmerrisikos (keine wesentlichen eigenen Investitionen, kein Verlustrisiko) sowie das Verbot des Auftretens unter eigenem Firmennamen am Markt.

#### 2. Selbständigerwerbende (Art. 8 und 9 AHVG) {#selbststaendige}

Selbständigerwerbende tragen das wirtschaftliche Risiko ihres Betriebs selbst und treten im Rechtsverkehr im eigenen Namen auf. Sie schulden den gesamten Beitrag allein; ihr Beitragssatz ist degressiv abgestuft (sinkende Beitragsskala bei tieferen Reingewinnen). Die Beitragsbemessung knüpft an das von den kantonalen Steuerbehörden ermittelte steuerbare Erwerbseinkommen und das im Betrieb investierte Eigenkapital an (Art. 9 AHVG i.V.m. Art. 22 ff. AHVV).

#### 3. Nichterwerbstätige (Art. 10 AHVG) {#nichterwerbstaetige}

{{< wortlaut gesetz="ahvg" art="art-010" >}}

Um lückenlose Versicherungsverläufe sicherzustellen, unterliegen auch Personen ohne Erwerbseinkommen ab dem 1. Januar nach Vollendung des 20. Altersjahres der Beitragspflicht (Studenten, Frühpensionierte, Invalide, Vermögende; Art. 10 AHVG). Die Beiträge bemessen sich nach dem Vermögen und dem mit 20 multiplizierten jährlichen Renteneinkommen (Art. 28 AHVV). 

Das Bundesgericht hat die Vereinbarkeit dieses progressiven Beitragsmodells mit dem Rechtsgleichheitsgebot bestätigt:

> «Gegenüber (unselbständig oder selbständig) Erwerbstätigen, bei denen Beiträge (einzig) auf dem Erwerbseinkommen erhoben werden, kann bereits aufgrund des gänzlich verschiedenen Beitragssubstrats nicht von Ungleichbehandlung und noch weniger von Diskriminierung gesprochen werden.» ([BGE 143 V 254 E. 6.3.3](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_007_BGE-143-V-254_2017.html#consideration_6.3.3)).

Eine Sonderregel schützt verheiratete Nichterwerbstätige: Die Beiträge einer nichterwerbstätigen Person gelten als bezahlt, wenn ihr erwerbstätiger Ehegatte auf seinem Erwerbseinkommen Beiträge in der Höhe von mindestens dem Doppelten des Mindestbeitrags entrichtet hat (Art. 3 Abs. 3 lit. a AHVG).

### Haftung der Arbeitgeberorgane nach Art. 52 AHVG {#arbeitgeberhaftung}

{{< wortlaut gesetz="ahvg" art="art-052" >}}

Eine der praktisch folgenreichsten Bestimmungen des AHVG ist die subsidiäre Organhaftung: Erleidet die Ausgleichskasse einen Beitragsausfall (typischerweise infolge des Konkurses einer juristischen Person wie einer AG oder GmbH), haften die formellen Organe (Verwaltungsräte, Geschäftsführer) und faktischen Organe der Gesellschaft der Kasse persönlich für den entstandenen Schaden, sofern sie ihre gesetzlichen Pflichten absichtlich oder grobfahrlässig verletzt haben (Art. 52 Abs. 1 AHVG).

Dieser Schadenersatzanspruch ist kein vertraglicher Anspruch, sondern ein eigenständiger öffentlich-rechtlicher Anspruch:

> «Gemäss Art. 52 Abs. 3 AHVG verjährt der Schadenersatzanspruch zwei Jahre, nachdem die zuständige Ausgleichskasse vom Schaden Kenntnis erhalten hat, spätestens aber fünf Jahre nach Eintritt des Schadens (erster Satz). Diese Fristen können unterbrochen werden» ([BGE 141 V 487 E. 2.1](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_007_BGE-141-V-487_2015.html#consideration_2.1)).

In ständiger Rechtsprechung nimmt das Bundesgericht grobe Fahrlässigkeit an, wenn Organe die Auszahlung von Nettolöhnen veranlassen oder dulden, ohne gleichzeitig sicherzustellen, dass die geschuldeten Sozialversicherungsbeiträge fristgerecht an die Ausgleichskasse abgeführt werden können.

## Die Leistungen der AHV und ihre Anspruchsvoraussetzungen {#leistungen-und-anspruchsvoraussetzungen}

Die AHV gewährt Geldleistungen zur wirtschaftlichen Existenzsicherung bei Alter, Tod der Versorgerin bzw. des Versorgers und Hilflosigkeit.

### Die Altersrente: Referenzalter und Beitragsdauer {#altersrente}

{{< wortlaut gesetz="ahvg" art="art-021" >}}

Der Anspruch auf eine ordentliche Altersrente entsteht am ersten Tag des Monats, welcher dem Erreichen des gesetzlichen **Referenzalters** folgt (Art. 21 Abs. 1 und 2 AHVG). Mit der am 1. Januar 2024 in Kraft getretenen Reform AHV 21 wurde das vormalige Frauenrentenalter 64 schrittweise an dasjenige der Männer angeglichen und durch das einheitliche Referenzalter von **65 Jahren** abgelöst (unter Gewährung von Ausgleichsmassnahmen für die Übergangsgeneration der Frauen, vgl. unten den Exkurs zu den Revisionen).

Voraussetzung für die Entstehung eines Anspruchs auf eine ordentliche Rente ist die Erfüllung der **Mindestbeitragsdauer**:

{{< wortlaut gesetz="ahvg" art="art-029" >}}

Der Anspruch entsteht erst, wenn die versicherte Person mindestens während **eines vollen Jahres** Beiträge geleistet hat (Art. 29 Abs. 1 AHVG):

> «Laut Art. 32 Abs. 1 IVV in Verbindung mit Art. 50 AHVV und Art. 29ter Abs. 2 AHVG liegt ein volles Beitragsjahr vor, wenn eine Person insgesamt länger als elf Monate im Sinne von Art. 1 oder 2 AHVG versichert war» ([BGE 125 V 253 E. 1b](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_007_BGE-125-V-253_1999-10-15.html#consideration_1.)).

Wird die einjährige Mindestbeitragsdauer nicht erreicht, besteht kein Anspruch auf eine ordentliche Rente; an ihre Stelle kann bei Erfüllung der staatsbürgerlichen Voraussetzungen (Wohnsitz in der Schweiz, Schweizer Bürgerrecht oder zwischenstaatliche Gleichstellung) eine bedarfsabhängige **ausserordentliche Rente** treten (Art. 42 AHVG).

### Flexibler Rentenbezug: Vorbezug und Aufschub nach der Reform AHV 21 {#rentenflexibilisierung}

{{< wortlaut gesetz="ahvg" art="art-040b" >}}

Seit dem 1. Januar 2024 ermöglicht das AHVG einen vollständig flexibilisierten Übergang vom Erwerbsleben in den Ruhestand zwischen dem vollendeten 63. und dem 70. Altersjahr (Art. 40b AHVG; für Frauen der Übergangsgeneration Vorbezug bereits ab Alter 62):
- **Vorbezug (Art. 40b Abs. 1 AHVG)**: Die Altersrente kann um maximal zwei Jahre (ab Alter 63) ganz oder teilweise vorbezogen werden. Der Vorbezug führt zu einer versicherungsmathematischen Kürzung der Rente für die gesamte restliche Lebensdauer. Neu kann der Bezug monatsweise gewählt und als **Teilrente** (zwischen 20 % und 80 %) bezogen werden.
- **Aufschub (Art. 40b Abs. 2 AHVG)**: Der Rentenbezug kann um mindestens ein Jahr und höchstens fünf Jahre (bis zum 70. Altersjahr) ganz oder teilweise aufgeschoben werden. Der Aufschub wird durch einen versicherungsmathematischen prozentualen Zuschlag auf die spätere Rente honoriert.

Einschränkungen der Aufschubsmöglichkeit auf dem Verordnungsweg sind nur zulässig, wenn sie gesetzlich gedeckt und verfassungskonform sind. In einem wegweisenden Urteil hat das Bundesgericht festgehalten:

> «Zusammenfassend ergibt sich, dass Art. 55 bis lit. b AHVV gegen gesetzliche und verfassungsmässige Vorgaben verstösst, weshalb der Bestimmung die Anwendung versagt wird» ([BGE 150 V 257 E. 3.5](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_007_BGE-150-V-257_2024.html#consideration_3.5)).

Der Bundesrat durfte Personen, deren Altersrente eine Invalidenrente ablöst, die Dispositionsfreiheit des Rentenaufschubs nicht verweigern; die Verordnungsbestimmung wurde wegen Gesetz- und Verfassungswidrigkeit verworfen.

### Hinterlassenenrenten: Witwen-, Witwer- und Waisenrenten {#hinterlassenenrenten}

{{< wortlaut gesetz="ahvg" art="art-023" >}}

Die Hinterlassenenversicherung bezweckt, den Ausfall des Unterhalts nach dem Tod eines Ehegatten oder Elternteils aufzufangen:
- **Witwen- und Witwerrente ([Art. 23](/kommentar/ahvg/art-023/) und 24 AHVG)**: Verwitwete Personen haben Anspruch auf eine Rente, wenn sie im Zeitpunkt des Todes Kinder haben. Unter altem Recht erlosch der Anspruch des Witwers zwingend, sobald das jüngste Kind das 18. Altersjahr vollendete (Art. 24 Abs. 2 AHVG), während Witwen ohne Kinder unter bestimmten Alters- und Ehedauervoraussetzungen eine lebenslange Rente behielten (Art. 24 Abs. 1 AHVG).
- **EGMR-Urteil Beeler und Gleichstellung**: Der Europäische Gerichtshof für Menschenrechte rügte diese Benachteiligung von Männern als verbotene Diskriminierung nach Art. 14 i.V.m. Art. 8 EMRK (*Beeler gegen die Schweiz*, Urteil der Grossen Kammer vom 11. Oktober 2022). Das Bundesgericht hat daraufhin klargestellt, dass die verfassungskonforme Übergangsordnung auch für geschiedene Männer gilt:

> «Soweit der Rentenaufhebungsgrund von Art. 24 Abs. 2 AHVG nicht (mehr) auf Witwer anwendbar ist, kann er auch für einen geschiedenen Mann, der (im Sinne von Art. 24a Abs. 1 AHVG ) einem Witwer gleichgestellt ist, keine Rolle spielen […]. Entgegenstehende Weisungen des BSV sind gesetzeswidrig und daher nicht zu beachten.» ([BGE 151 V 186 E. 4.4](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_007_BGE-151-V-186_2025.html#consideration_4.4)).

- **Waisenrente (Art. 25 AHVG)**: Kinder, deren Vater oder Mutter gestorben ist, haben Anspruch auf eine Waisenrente (40 % der Altersrente). Haben sie beide Elternteile verloren, besteht Anspruch auf zwei Waisenrenten (plafoniert auf 60 % der maximalen Altersrente). Der Anspruch dauert bis zum vollendeten 18. Altersjahr bzw. bis zum Abschluss der Ausbildung, längstens bis zum vollendeten 25. Altersjahr.

### Hilflosenentschädigung und Hilfsmittel {#hilflosenentschaedigung}

Erreicht eine Person das Referenzalter und ist sie für alltägliche Lebensverrichtungen (Ankleiden, Aufstehen, Essen, Körperpflege, Verrichten der Notdurft, Fortbewegung) dauernd auf fremde Hilfe angewiesen, gewährt die AHV eine bedarfsunabhängige **Hilflosenentschädigung** leichten, mittleren oder schweren Grades (Art. 43bis AHVG).

Galt die Hilflosigkeit bereits vor Erreichen des Referenzalters unter dem Regime der Invalidenversicherung, greift eine gesetzliche Besitzstandsgarantie (Art. 43bis Abs. 4 AHVG). Das Bundesgericht umschreibt deren Schutzzweck präzise:

> «Sinn und Zweck der Besitzstandsgarantie gemäss Art. 43 bis Abs. 4 AHVG ist es, zu verhindern, dass die Versicherten beim Eintritt ins Rentenalter allein wegen der Ablösung der IV durch die AHV eine Leistungskürzung gewärtigen müssen» ([BGE 137 V 162 E. 3.2](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_007_BGE-137-V-162_2011.html#consideration_3.2)).

Zudem stellt die AHV im Rahmen von Art. 43ter AHVG einfache und zweckmässige Hilfsmittel (z. B. Hörgeräte, Rollstühle) zur Verfügung, um die Selbständigkeit im Alter zu wahren.

## Grundlagen der Rentenberechnung {#rentenberechnung}

Die Berechnung einer AHV-Altersrente folgt einem mathematisch streng determinierten Schema. Sie beruht auf zwei Grundpfeilern: der **Beitragsdauer** und dem **massgebenden durchschnittlichen Jahreseinkommen** (Art. 29bis AHVG).

### Rentenskala 44 und Vollrente vs. Teilrente {#rentenskala}

Für die Ermittlung der Rente wird die Beitragsdauer der versicherten Person mit derjenigen ihres Jahrgangs verglichen:
- **Vollrente (Skala 44)**: Eine Vollrente erhält, wer eine **vollständige Beitragsdauer** aufweist. Dies erfordert, dass die Person ab dem 1. Januar nach Vollendung des 20. Altersjahres bis zum 31. Dezember vor Eintritt des Referenzalters lückenlos Beiträge entrichtet hat (in der Regel 44 Beitragsjahre, Art. 29ter Abs. 1 AHVG).
- **Teilrente (Skalen 1 bis 43)**: Weist das Beitragskonto Lücken auf (sog. Fehljahre), wird die Rente gekürzt und nach einer der Rentenskalen 1 bis 43 berechnet. Jedes fehlende Beitragsjahr führt im Grundsatz zu einer proportionalen Rentenkürzung um mindestens 1/44.

Jugendjahre (vor dem 21. Altersjahr) und Beitragsmonate im Jahr des Rentenalters können unter bestimmten Bedingungen als Zusatzmonate zum Schliessen von Lücken herangezogen werden (Art. 52b AHVV).

### Massgebendes Jahreseinkommen und Individuelles Konto (IK) {#individuelles-konto}

Liegt die massgebende Skala fest, bestimmt sich die Höhe der Rente innerhalb der Skala nach dem **massgebenden durchschnittlichen Jahreseinkommen** (Art. 29quater AHVG). Dieses setzt sich zusammen aus:
1. Den tatsächlich erzielten Erwerbseinkommen;
2. Den Aufwertungsfaktoren (Anpassung an die Lohn- und Preisentwicklung bis zum Renteneintritt);
3. Den Erziehungs- und Betreuungsgutschriften.

Grundlage für die Ermittlung der beitragspflichtigen Erwerbseinkommen sind die **Individuellen Konten (IK)**, die von den Ausgleichskassen für jede beitragspflichtige Person geführt werden (Art. 30ter AHVG). Das Bundesgericht betont den massgebenden zeitlichen Rahmen:

> «Vorab ist festzuhalten, dass gemäss Art. 29 bis Abs. 1 AHVG für die Rentenberechnung Beitragsjahre, Erwerbseinkommen sowie Erziehungs- oder Betreuungsgutschriften der rentenberechtigten Person zwischen dem 1. Januar nach Vollendung des 20. Altersjahres und dem 31. Dezember vor Eintritt des Versicherungsfalles (Rentenalter oder Tod) berücksichtigt werden.» ([BGE 146 V 313 E. 4.2](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_007_BGE-146-V-313_2020.html#consideration_4.2)).

### Einkommenssplitting und Erziehungsgutschriften {#splitting-und-gutschriften}

Mit der 10. AHV-Revision (in Kraft seit 1997) wurde das traditionelle ehepaarbezogene Rentenmodell auf ein partnerschaftliches, individualisiertes System umgestellt. Zentral sind dabei zwei Mechanismen:

#### 1. Einkommenssplitting (Art. 29quinquies AHVG) {#splitting}

Während der Kalenderjahre der Ehe erzielte Erwerbseinkommen werden bei Eintritt des Rentenfalles oder bei Scheidung hälftig geteilt und beiden Ehegatten auf ihren Individuellen Konten gutgeschrieben:

> «Wenn eine verwitwete Person Anspruch auf eine Altersrente hat, werden gemäss Art. 29 quinquies Abs. 3 lit. b AHVG Einkommen, welche die Ehegatten während der Kalenderjahre der gemeinsamen Ehe erzielt haben, geteilt und je zur Hälfte den beiden Ehegatten angerechnet.» ([BGE 132 V 265 E. 2.1](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_007_BGE-132-V-265_2006.html#consideration_2.1)).

Das Splitting gilt zwingend für die Kalenderjahre, in denen beide Ehegatten in der schweizerischen AHV versichert waren. Es verhindert, dass diejenige Person, die wegen Kinderbetreuung oder Haushaltsführung auf ein eigenes Erwerbseinkommen verzichtet hat, im Alter ohne ausreichende Beitragsbasis dasteht.

#### 2. Erziehungsgutschriften (Art. 29sexies AHVG) und Betreuungsgutschriften {#gutschriften}

Für Jahre, in denen versicherte Personen Kinder unter 16 Jahren betreuen, wird ihnen ein fiktives Einkommen in der Höhe der dreifachen jährlichen Minimalrente als **Erziehungsgutschrift** angerechnet (Art. 29sexies AHVG). Bei verheirateten Eltern wird die Gutschrift während der Ehe hälftig aufgeteilt:

> «Versicherten wird für diejenigen Jahre eine Erziehungsgutschrift angerechnet, in welchen ihnen die elterliche Sorge für eines oder mehrere Kinder zusteht, die das 16. Altersjahr noch nicht erreicht haben.» ([BGE 152 V 85 E. 5.1.1](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_007_BGE-152-V-85_2026.html#consideration_5.1.1)).

Analoge Gutschriften werden Versicherten gewährt, die pflegebedürftige Verwandte im gemeinsamen Haushalt pflegen (**Betreuungsgutschriften**, Art. 29septies AHVG). Eine Kumulation von Erziehungs- und Betreuungsgutschriften im selben Kalenderjahr ist ausgeschlossen.

### Die Plafonierung der Ehepaarrenten {#plafonierung}

{{< wortlaut gesetz="ahvg" art="art-035" >}}

Haben beide Ehegatten Anspruch auf eine Altersrente, greift die gesetzliche **Rentenplafonierung** (Art. 35 AHVG): Die Summe der beiden Einzelrenten darf höchstens **150 Prozent** der maximalen Altersrente betragen. Übersteigt die Summe diesen Betrag, werden die beiden Renten verhältnismässig gekürzt.

Diese Plafonierung wird in der rechtspolitischen Diskussion oft als *Heiratsstrafe* in der AHV bezeichnet, da Konkubinatspaare zwei ungekürzte Einzelrenten (zusammen bis zu 200 % der Maximalrente) beziehen können. Das Bundesgericht hat jedoch wiederholt entschieden, dass die Plafonierung verfassungs- und völkerrechtskonform ist:

> «Ehe und Konkubinat sind (in der schweizerischen Rechtsordnung) unterschiedliche Formen des Zusammenlebens mit unterschiedlichen Rechtswirkungen. Für die nur bei verheirateten Paaren und eingetragenen Partnerschaften gesetzlich verankerte Rentenplafonierung gibt es in einer Gesamtschau des Sozialversicherungsrechts die dargelegten sachlichen Gründe» ([BGE 140 I 77 E. 9](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_001_BGE-140-I-77_2014.html#consideration_9.)).

In einer sozialversicherungsrechtlichen Gesamtbetrachtung geniessen Verheiratete signifikante Privilegien, die Konkubinatspaaren vorenthalten sind: gegenseitiges Einkommenssplitting, Befreiung des nichterwerbstätigen Ehegatten von eigenen Beiträgen bei doppelter Mindestbeitragszahlung des Partners sowie der Anspruch auf Hinterlassenenrenten (Art. 23 AHVG).

## Exkurs: Aktuelle Reformen und Revisionsbestrebungen {#revisionsbestrebungen}

Die schweizerische Altersvorsorge steht infolge des demografischen Wandels (Zunahme der Lebenserwartung, Verrentung der Babyboomer-Generation) unter anhaltendem Reform- und Finanzierungsdruck. In den letzten Jahren haben mehrere Grossprojekte und Volksabstimmungen die Rechtslandschaft markant verändert.

### Die Reform AHV 21: Einheitliches Referenzalter und Flexibilisierung {#reform-ahv-21}

In der Volksabstimmung vom 25. September 2022 nahmen Volk und Stände die Stabilisierung der AHV (**AHV 21**) knapp an. Die Reform trat am **1. Januar 2024** in Kraft und brachte drei zentrale Eckpfeiler:
1. **Einheitliches Referenzalter 65**: Das Referenzalter der Frauen wurde von 64 auf 65 Jahre angehoben (schrittweise Erhöhung um jeweils drei Monate pro Jahr ab 2025). Als Ausgleich für die Übergangsgeneration der Frauen (Jahrgänge 1961 bis 1969) wurden lebenslange Rentenzuschläge bei Verzicht auf Vorbezug bzw. tiefere Kürzungsansätze bei Vorbezug geschaffen (Art. 34b AHVG).
2. **Flexibilisierung des Rentenbezugs**: Ablösung der starren Rentenalter durch das Band zwischen 63 und 70 Jahren (Art. 40b AHVG), Teilrentenbezug und monatliche Abrufbarkeit.
3. **Zusatzfinanzierung über die Mehrwertsteuer**: Erhöhung des Normalsatzes um 0,4 Prozentpunkte (auf 8,1 %) und des reduzierten Satzes um 0,1 Prozentpunkte (auf 2,6 %) zugunsten des AHV-Ausgleichsfonds.

### Die 13. AHV-Rente: Verfassungsauftrag und Umsetzung {#dreizehnte-ahv-rente}

Am **3. März 2024** nahmen Volk und Stände die Volksinitiative *Für ein besseres Leben im Alter (Initiative für eine 13. AHV-Rente)* mit 58,2 % Ja-Stimmen und einer deutlichen Ständemehrheit an. Damit wurde ein historischer Meilenstein gesetzt: Erstmals wurde eine Volksinitiative für den Ausbau der Sozialversicherungen angenommen.

Die Initiative verankerte einen neuen Übergangsartikel in der Bundesverfassung:
- **Art. 197 Ziff. 16 BV**: Bezügerinnen und Bezüger einer Altersrente haben Anspruch auf einen jährlichen Zuschlag in der Höhe eines Zwölftels ihrer jährlichen Rente (Auszahlung spätestens ab dem Jahr 2026).
- **Keine Auswirkung auf Ergänzungsleistungen**: Die Verfassung schreibt ausdrücklich vor, dass der Zuschlag nicht zu einer Reduktion der Ergänzungsleistungen führen darf.

Die gesetzgeberische Umsetzung und die Finanzierungsmodalitäten (Zusatzfinanzierung über Lohnbeiträge und/oder eine erneute Anhebung der Mehrwertsteuer) bildeten seither den Schwerpunkt der parlamentarischen Gesetzgebungsarbeit.

### Reform der Hinterlassenenrenten nach dem EGMR-Urteil Beeler {#reform-hinterlassenenrenten}

Die Verurteilung der Schweiz durch den EGMR im Urteil *Beeler* vom 11. Oktober 2022 machte deutlich, dass die traditionelle Konzeption der Hinterlassenenrenten – lebenslange Renten für kinderlose Witwen ab bestimmtem Alter, aber Rentenende für Witwer beim 18. Geburtstag des jüngsten Kindes – völkerrechtlich unhaltbar ist.

Bis zum Inkrafttreten einer formellen Revision wies das Bundesamt für Sozialversicherungen (BSV) die Kassen an, Witwerrenten über das 18. Altersjahr des Kindes hinaus weiterzuzahlen. Mit dem Urteil [BGE 151 V 186](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_007_BGE-151-V-186_2025.html#consideration_4.4) dehnten die Richter in Lausanne diesen Schutz auch auf geschiedene Männer aus.

Der Bundesrat eröffnete daraufhin eine Revisionsvorlage für das AHVG: Geplant ist der Übergang von einem versorgerorientierten Ehegattenmodell zu einem **kinderorientierten Betreuungsmodell**. Die Hinterlassenenrente soll künftig geschlechtsunabhängig ausgestaltet werden und primär Eltern unterstützen, solange Kinder betreut und ausgebildet werden (bis zum 25. Altersjahr des Kindes), während lebenslange Renten für kinderlose Personen schrittweise abgebaut werden sollen.

### Strukturelle Herausforderungen und demografischer Wandel {#demografischer-wandel}

Trotz der Reformen AHV 21 und der Beschlüsse zur 13. AHV-Rente bleibt die langfristige finanzielle Balance der 1. Säule angespannt. Während bei Gründung der AHV im Jahr 1948 noch mehr als sechs Erwerbstätige auf eine Rentnerin bzw. einen Rentner kamen, liegt das Verhältnis heute bei rund drei Erwerbstätigen pro Rentner und wird in den 2030er-Jahren auf rund zwei sinken.

In der politischen Debatte stehen sich daher diametral entgegengesetzte Lösungsansätze gegenüber:
- **Erhöhung des Rentenalters**: Die Volksinitiative *Für ein sicheres und nachhaltiges Rentenalter (Renteninitiative)*, welche das Rentenalter für beide Geschlechter auf 66 Jahre anheben und danach an die Lebenserwartung koppeln wollte, wurde am 3. März 2024 von Volk und Ständen mit 74,7 % Nein-Stimmen verworfen.
- **Einnahmenseitige Sanierung**: Diskussionen um zusätzliche Finanzierungsquellen (Finanztransaktionssteuern, Erbschaftssteuern auf Bundesebene, höhere Mehrwertsteuer- oder Lohnbeitragssätze).
- **Stärkung der Erwerbsanreize im Alter**: Durch die Abschaffung des Freibetrags auf Erwerbseinkommen im Rentenalter oder die Möglichkeit, durch Beitragszahlungen nach Erreichen des Referenzalters bestehende Beitragslücken zu schliessen und die Rente zu verbessern (mit Art. 34b AHVG im Rahmen von AHV 21 teilweise realisiert).

## Praxishinweise {#praxishinweise}

Aus der gerichtlichen und behördlichen Praxis ergeben sich für Versicherte, Arbeitgeber und Beratende zentrale Handlungsregeln:

1. **Individuellen Kontoauszug (IK-Auszug) periodisch bestellen**: Beitragsnachweise und Lohnmeldungen von Arbeitgebern gehen vereinzelt verloren. Versicherte sollten alle drei bis fünf Jahre kostenlos bei einer Ausgleichskasse einen IK-Auszug verlangen. Berichtigungen von Buchungen sind in der Regel nur innerhalb von 30 Tagen nach Zustellung des Auszugs unkompliziert möglich; nach Eintritt des Rentenfalles verlangt der Nachweis unverbuchter Einkommen strikte Urkundenbeweise.
2. **Beitragslücken rechtzeitig schliessen (Fünfjahresfrist)**: Fehlende Beitragsjahre können nur innerhalb von **fünf Jahren** nach Ablauf des betreffenden Kalenderjahres durch Nachzahlung getilgt werden (Art. 16 Abs. 1 AHVG). Nach Ablauf dieser Frist sind Beitragsjahre unwiederbringlich verwirkt, was zu einer lebenslangen Kürzung der Rente (Teilrente) führt.
3. **Beitragspflicht Nichterwerbstätiger aktiv anmelden**: Frühpensionierte, Studierende über 20 Jahren, Weltreisende oder Ausgesteuerte übersehen oft ihre Beitragspflicht als Nichterwerbstätige nach Art. 10 AHVG. Da kein Arbeitgeber den Lohnabzug vornimmt, müssen sich Nichterwerbstätige selbständig bei der kantonalen Ausgleichskasse melden, um Lücken zu vermeiden.
4. **Einkommenssplitting nach Scheidung umgehend veranlassen**: Das gesetzliche Splitting der Einkommen während der Ehejahre (Art. 29quinquies AHVG) wird nach einem rechtskräftigen Scheidungsurteil nicht immer vollautomatisch vollzogen. Es empfiehlt sich, die Durchführung des Splittings unmittelbar nach Abschluss des Scheidungsverfahrens mit dem Formular *Anmeldung zur Einkommensteilung im Scheidungsfall* bei der zuständigen Kasse zu beantragen.
5. **Fristen für Vorbezug und Aufschub beachten**: Wer die Rente vorziehen oder aufschieben will, muss die Anmeldung vor Beginn des gewünschten Monats bei der Ausgleichskasse einreichen. Ein rückwirkender Vorbezug ist gesetzlich ausgeschlossen; wird die Rente nicht rechtzeitig vor Erreichen des Referenzalters angemeldet oder aufgeschoben, wird sie zwingend als reguläre Altersrente ausbezahlt.
6. **Arbeitgeber und Organe: Lohnabzüge nicht für Liquiditätsengpässe nutzen**: Bei Liquiditätsschwierigkeiten einer Gesellschaft dürfen geschuldete Arbeitnehmer- und Arbeitgeberbeiträge unter keinen Umständen zur Bezahlung anderer Gläubiger oder zur Aufrechterhaltung des Geschäftsbetriebs verwendet werden. Ein solcher Zahlungsaufschub begründet im Konkursfall fast ausnahmslos die persönliche Organhaftung nach Art. 52 AHVG wegen grober Fahrlässigkeit.

## Leitentscheide {#leitentscheide}

| Entscheid | Gegenstand | Bedeutung |
|---|---|---|
| [BGE 130 I 205](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_001_BGE-130-I-205_2004.html#consideration_6.) E. 6 | Verfassungsrechtliches Dreisäulenprinzip (Art. 111 und 112 BV) | Fundamentale Definition der drei Säulen; 1. Säule (AHV/IV/EL) sichert den Existenzbedarf im Umlageverfahren. |
| [BGE 144 V 111](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_007_BGE-144-V-111_2018.html#consideration_4.2) E. 4.2 | Abgrenzung selbständige vs. unselbständige Erwerbstätigkeit (Art. 5 und 9 AHVG) | Massgeblichkeit der tatsächlichen wirtschaftlichen Gegebenheiten und des Unternehmerrisikos, nicht der zivilrechtlichen Vertragsbezeichnung. |
| [BGE 147 V 174](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_007_BGE-147-V-174_2021.html#consideration_6.1) E. 6.1 | Arbeitgeberbeitragspflicht und Betriebsstätte (Art. 12 und 14 AHVG) | Verankerung des Prinzips der Beitragserhebung an der Quelle; Arbeitgeberpflicht zum periodischen Lohnabzug und zur Beitragsentrichtung. |
| [BGE 143 V 254](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_007_BGE-143-V-254_2017.html#consideration_6.3.3) E. 6.3.3 | Beiträge Nichterwerbstätiger nach Vermögen und Renteneinkommen (Art. 10 AHVG) | Verfassungsmässigkeit der Beitragsbemessung Nichterwerbstätiger; kein Verstoss gegen das Rechtsgleichheitsgebot im Vergleich zu Erwerbstätigen. |
| [BGE 125 V 253](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_007_BGE-125-V-253_1999-10-15.html#consideration_1.) E. 1b | Mindestbeitragsdauer für eine ordentliche Rente (Art. 29 Abs. 1 AHVG) | Voraussetzungen eines vollen Beitragsjahres; Gleichstellung ausländischer Staatsangehöriger und Verzicht auf persönliche Beitragszahlung bei Ehepartnerbeiträgen oder Gutschriften. |
| [BGE 146 V 313](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_007_BGE-146-V-313_2020.html#consideration_4.2) E. 4.2 | Individuelles Konto und Erfassungszeitraum vor dem Versicherungsfall (Art. 29bis und 30ter AHVG) | Berücksichtigung von Beitragsjahren und Einkommen ausschliesslich zwischen Vollendung des 20. Altersjahres und dem 31. Dezember vor Eintritt des Versicherungsfalles. |
| [BGE 132 V 265](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_007_BGE-132-V-265_2006.html#consideration_2.1) E. 2.1 | Einkommenssplitting unter Ehegatten (Art. 29quinquies AHVG) | Grundsatz der hälftigen Teilung und Anrechnung der während der Kalenderjahre der gemeinsamen Ehe erzielten Erwerbseinkommen. |
| [BGE 152 V 85](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_007_BGE-152-V-85_2026.html#consideration_5.1.1) E. 5.1.1 | Erziehungsgutschriften bei der Rentenberechnung (Art. 29sexies AHVG) | Fiktives Erwerbseinkommen für Zeiten elterlicher Sorge über Kinder unter 16 Jahren; Systematik der hälftigen Aufteilung zwischen Eltern. |
| [BGE 140 I 77](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_001_BGE-140-I-77_2014.html#consideration_9.) E. 9 | Verfassungsmässigkeit der Rentenplafonierung für Ehepaare (Art. 35 AHVG) | Plafonierung der beiden Ehegattenrenten auf maximal 150 % der Maximalrente verletzt weder Art. 8 BV noch die EMRK; sachliche Rechtfertigung in der sozialversicherungsrechtlichen Gesamtschau. |
| [BGE 150 V 257](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_007_BGE-150-V-257_2024.html#consideration_3.5) E. 3.5 | Aufschub der Altersrente und Verfassungswidrigkeit von Verordnungsausnahmen (Art. 39 / 40b AHVG) | Unzulässigkeit des Ausschlusses von Altersrenten, die eine Invalidenrente ablösen, von der Aufschubsmöglichkeit; Nichtanwendung von Art. 55bis lit. b AHVV. |
| [BGE 151 V 186](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_007_BGE-151-V-186_2025.html#consideration_4.4) E. 4.4 | Hinterlassenenrenten, Witwerrente und EGMR-Urteil Beeler (Art. 24 und 24a AHVG) | Gesetzwidrigkeit einschränkender BSV-Weisungen; Unanwendbarkeit des Rentenaufhebungsgrundes von Art. 24 Abs. 2 AHVG auf Witwer und geschiedene Männer. |
| [BGE 137 V 162](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_007_BGE-137-V-162_2011.html#consideration_3.2) E. 3.2 | Besitzstandsgarantie bei Hilflosenentschädigung der AHV (Art. 43bis Abs. 4 AHVG) | Zweck der Besitzstandsgarantie zur Vermeidung einer Leistungskürzung bei Ablösung der IV-Hilflosenentschädigung durch die AHV beim Renteneintritt. |

## Literatur {#literatur}

- Thomas Gächter / Egli Philipp (Hrsg.), Allgemeiner Teil des Sozialversicherungsrechts (ATSG) und AHVG, Basler Kommentar, Basel 2020.
- Ueli Kieser, Alters- und Hinterlassenenversicherung, in: Ulrich Meyer (Hrsg.), Schweizerisches Bundesverwaltungsrecht (SBVR), Band XIV: Soziale Sicherheit, 3. Aufl., Basel 2016.
- Ueli Kieser, ATSG-Kommentar, 4. Aufl., Zürich/Basel/Genf 2020.
- Erwin Murer, Die 10. AHV-Revision, Bern 1997.
- Basile Cardinaux, Das EGMR-Urteil Beeler und seine Folgen, in: Schweizerische Zeitschrift für Sozialversicherung und berufliche Vorsorge (SZS) 2023, S. 128 ff.
- Bundesamt für Sozialversicherungen (BSV), Wegleitung über die Renten (RWL) in der Eidgenössischen Alters-, Hinterlassenen- und Invalidenversicherung, Bern (laufend nachgeführt).
- Bundesamt für Sozialversicherungen (BSV), Wegleitung über die Beiträge der Selbständigerwerbenden und Nichterwerbstätigen in der AHV, IV und EO (WSN), Bern (laufend nachgeführt).
