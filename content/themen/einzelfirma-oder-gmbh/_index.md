---
title: "Rechtsformwahl: Einzelfirma oder GmbH im Kleingewerbe"
date: 2026-11-01
lastmod: 2026-11-01
description: "Rechtlicher und praktischer Vergleich zwischen Einzelfirma und GmbH für kleine Gewerbebetriebe und freiberufliche Praxen: Gründung, Haftung, SchKG-Betreibung, Steuern, Sozialversicherungen und KVG-Zulassung."
tags: ["Gesellschaftsrecht", "Rechtsformen", "Einzelfirma", "Einzelunternehmen", "GmbH", "Haftung", "Sozialversicherungen", "Steuern", "Physiotherapie", "KVG"]
typ: grundlage
kurz: "Wer ein kleines Gewerbe oder eine freiberufliche Praxis wie eine Physiotherapie eröffnet, steht vor der Grundsatzfrage zwischen Einzelfirma und GmbH. Während die Einzelfirma rasch, günstig und ohne Stammkapital gegründet ist, schützt die GmbH das Privatvermögen vor unternehmerischen Risiken und bietet steuerlichen Spielraum – fordert dafür jedoch CHF 20'000 Mindestkapital, Notariatskosten, doppelten Buchhaltungsaufwand und schliesst den Inhaber faktisch vom Arbeitslosengeld aus."
sachgebiete: [schuldrecht.gesellschaft, steuern.einkommen_vermoegen, ahv, schkg.konkurs]
normen:
  - { gesetz: or, art: art-772 }
  - { gesetz: or, art: art-773 }
  - { gesetz: or, art: art-934 }
  - { gesetz: or, art: art-945 }
  - { gesetz: schkg, art: art-039 }
  - { gesetz: ahvg, art: art-012 }
  - { gesetz: avig, art: art-031 }
  - { gesetz: kvg, art: art-035 }
stichworte: ["Rechtsformwahl", "Einzelfirma", "Einzelunternehmen", "GmbH", "Kleingewerbe", "Praxisgründung", "Physiotherapie", "Haftung", "Trennungsprinzip", "Durchgriff", "Sozialversicherungen", "Scheinselbständigkeit", "wirtschaftliche Doppelbesteuerung", "Konkursbetreibung"]
revisions:
  - date: 2026-11-01
    by: "Antigravity"
    model: "gemini-3.8-flash"
    note: "Erstfassung nach Skill glossagens-themen (Typ grundlage). Normtexte Art. 772, 773, 934, 945 OR, Art. 39 SchKG, Art. 12 AHVG, Art. 31 AVIG, Art. 35 KVG per {{< wortlaut >}} (scripts/wortlaut.py). Volltexte zu Trennungsprinzip (BGE 132 III 489), Organverantwortlichkeit (BGE 139 III 24), Konkursbetreibung (BGE 122 III 204), AHV-Status (BGE 144 V 111), Ausschluss vom ALV-Taggeld (BGE 145 V 200) und Steuerdrittvergleich (BGE 138 II 57) über entscheidsuche geladen; Erwägungen, Anker und Zitate mit dem Volltext abgeglichen. Kantonale Praxis zur KVG-Zulassung als Organisation der Physiotherapie nach VG SZ III 2024 140 dokumentiert."
---

## Überblick {#ueberblick}

Bei der Gründung eines Kleinunternehmens, Handwerksbetriebs oder einer freiberuflichen Praxis – etwa einer Physiotherapie-, Massage- oder Psychotherapiepraxis – konzentriert sich die Rechtsformwahl in der Schweizer Praxis meist auf zwei Optionen: die **Einzelfirma** (das Einzelunternehmen) oder die **Gesellschaft mit beschränkter Haftung (GmbH)**. 

Die Entscheidung berührt nicht nur das Gesellschaftsrecht (OR), sondern hat weitreichende Auswirkungen auf die persönliche Haftung und die Betreibungsart (SchKG), die steuerliche Belastung (DBG, StHG), den sozialversicherungsrechtlichen Status (AHVG, BVG, AVIG) sowie sektorspezifische Zulassungen (z. B. nach KVG).

| Kriterium | Einzelfirma (Einzelunternehmen) | Gesellschaft mit beschränkter Haftung (GmbH) |
|---|---|---|
| **Rechtspersönlichkeit** | Keine juristische Person; identisch mit der natürlichen Person | Eigene juristische Person (Art. 772 Abs. 1 OR) |
| **Mindestkapital** | Keines vorgeschrieben | Mindestens CHF 20'000, voll liberiert (Art. 773 f. OR) |
| **Gründungsverfahren** | Formlos durch Aufnahme der Geschäftstätigkeit; kostengünstig | Öffentliche Beurkundung (Notar), Statuten, konstitutiver HR-Eintrag (Art. 777 ff. OR) |
| **Handelsregister (HR)** | Obligatorisch erst ab CHF 100'000 Jahresumsatz (Art. 934 OR) | Zwingend und konstitutiv (Art. 779 Abs. 1 OR) |
| **Firmenname** | Muss zwingend den amtlichen Familiennamen enthalten (Art. 945 Abs. 1 OR) | Frei wählbar mit zwingendem Rechtsformzusatz *GmbH* (Art. 950 OR) |
| **Haftung & Betreibung** | Unbeschränkte Haftung mit gesamtem Geschäfts- und Privatvermögen; Konkursbetreibung bei HR-Eintrag (Art. 39 SchKG) | Grundsätzlich haftet nur das Gesellschaftsvermögen (Art. 772 Abs. 1 OR); Inhaberprivatvermögen geschützt |
| **Steuern** | Keine Doppelbesteuerung: Reingewinn und Geschäftsvermögen werden direkt beim Inhaber als Einkommen/Vermögen besteuert | Wirtschaftliche Doppelbesteuerung: Gewinn-/Kapitalsteuer auf GmbH-Ebene, Einkommenssteuer auf Lohn und Dividenden beim Inhaber |
| **Sozialversicherungen** | Inhaber gilt als *Selbständigerwerbender* (Art. 12 AHVG); keine BVG-Pflicht, kein Anspruch auf ALV | Inhaber gilt als *Angestellter* der eigenen GmbH; BVG-/UVG-Pflicht; aber kein ALV-Taggeldanspruch (Art. 31 Abs. 3 lit. c AVIG) |
| **Abrechnung mit Kassen (KVG)** | Direkt über persönliche Zulassung und ZSR-Nummer des Therapeuten (Art. 35 Abs. 2 lit. h KVG) | Über *Organisation der Physiotherapie* (Art. 35 Abs. 2 lit. k KVG) oder angestellte Therapeuten |
| **Nachfolge / Verkauf** | Umständlich: Einzelübertragung von Aktiven/Verträgen oder Vermögensübertragung nach Fusionsgesetz | Einfach: Veräusserung der Stammanteile (*Share Deal*, Art. 784 OR) |

---

## Rechtsgrundlagen und Gründungsaufwand {#rechtsgrundlagen-und-gruendungsaufwand}

### Die Einzelfirma: Maximale Flexibilität ohne Hürden {#einzelfirma-flexibilitaet}

Die Einzelfirma ist die einfachste und am weitesten verbreitete Form unternehmerischer Betätigung in der Schweiz. Sie entsteht formlos durch die tatsächliche Aufnahme einer auf dauernden Erwerb gerichteten selbständigen wirtschaftlichen Tätigkeit durch eine natürliche Person. 

{{< wortlaut gesetz="or" art="art-934" >}}

Solange der Jahresumsatz unter CHF 100'000 liegt, besteht keine Pflicht zur Eintragung in das Handelsregister (Art. 934 Abs. 1 OR). Eine freiwillige Eintragung ist jedoch jederzeit möglich. Im Firmennamen muss bei der Einzelfirma zwingend der Familienname der Gründerin oder des Gründers aufgeführt sein (Art. 945 Abs. 1 OR), Fantasie- oder Sachbezeichnungen sind nur als Zusatz gestattet (z. B. *Physiotherapie Müller*). 

Ein gesetzliches Mindestkapital existiert nicht; die Gründung verursacht mit Ausnahme allfälliger freiwilliger Registergebühren keine Transaktions- oder Notariatskosten. Für Unternehmen mit weniger als CHF 500'000 Umsatzerlös genügt steuerlich und buchhalterisch eine einfache Einnahmen- und Ausgabenrechnung mit Vermögensdarstellung (*Milchbüchleinrechnung*, Art. 957 Abs. 2 Ziff. 1 OR).

### Die GmbH: Eigene Rechtspersönlichkeit und Kapitalbindung {#gmbh-rechtspersoenlichkeit}

Die GmbH ist eine personenbezogene Kapitalgesellschaft und besitzt eigene Rechtspersönlichkeit.

{{< wortlaut gesetz="or" art="art-772" >}}

{{< wortlaut gesetz="or" art="art-773" >}}

Zur Errichtung einer GmbH ist ein Stammkapital von mindestens CHF 20'000 erforderlich (Art. 773 OR), welches bei der Gründung voll liberiert und auf ein Sperrkonto bei einer Schweizer Bank einbezahlt oder durch eine Sacheinlage gedeckt werden muss (Art. 777c OR). 

Die Gründung bedarf zwingend der öffentlichen Beurkundung durch eine Notarin oder einen Notar (Art. 777 Abs. 1 OR) sowie der Genehmigung schriftlicher Statuten. Die Rechtspersönlichkeit entsteht erst mit dem konstitutiven Eintrag im Handelsregister (Art. 779 Abs. 1 OR). Die Gründungsphase verursacht typischerweise Notariats-, Handelsregister- und Beratungskosten von rund CHF 1'500 bis CHF 3'000. Zudem unterliegt jede GmbH zwingend den Vorschriften über die kaufmännische Buchführung nach Art. 957 Abs. 1 Ziff. 2 OR (doppelte Buchhaltung mit Bilanz, Erfolgsrechnung und Anhang).

---

## Haftung, Gläubigerschutz und Insolvenzrisiko {#haftung-und-insolvenz}

Der gravierendste rechtliche Unterschied zwischen beiden Formen liegt in der Haftungsordnung und dem Gläubigerzugriff bei einer Schieflage des Betriebs.

### Unbeschränkte persönliche Haftung bei der Einzelfirma {#haftung-einzelfirma}

Bei der Einzelfirma existiert keine juristische Trennung zwischen geschäftlicher Sphäre und Privatvermögen. Der Inhaber haftet für sämtliche geschäftlichen Verpflichtungen (Lieferantenrechnungen, Geräteleasing, Bankkredite, Mietzinsverpflichtungen für Praxisräume oder Löhne von Angestellten) **unbeschränkt und unmittelbar mit seinem gesamten gegenwärtigen und zukünftigen Privatvermögen**.

Wird die Einzelfirma im Handelsregister eingetragen, greift zudem das scharfe Vollstreckungsregime des Bundesgesetzes über Schuldbetreibung und Konkurs (SchKG):

{{< wortlaut gesetz="schkg" art="art-039" >}}

Gemäss Art. 39 Abs. 1 Ziff. 1 SchKG unterliegt der Inhaber einer im Handelsregister eingetragenen Einzelfirma zwingend der **Konkursbetreibung** – und zwar für alle Schulden, gleichgültig ob sie geschäftlicher oder rein privater Natur sind ([BGE 80 III 97](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_005_BGE-80-III-97_1954-11-05.html)). 

Wird der Betrieb aufgegeben und die Einzelfirma im Handelsregister gelöscht, schützt dies die Gründerin nicht sofort: Nach Art. 40 Abs. 1 SchKG bleibt die Konkursfähigkeit noch während eines halben Jahres nach der Veröffentlichung im Schweizerischen Handelsamtsblatt (SHAB) bestehen. Das Bundesgericht hielt in [BGE 122 III 204](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_005_BGE-122-III-204_1996-06-18.html#consideration_2.) E. 2. unmissverständlich fest:

> «Gemäss Art. 40 Abs. 1 SchKG unterliegen die Personen, die im Handelsregister eingetragen waren, noch während sechs Monaten, nachdem die Streichung durch das Schweizerische Handelsamtsblatt bekanntgemacht worden ist, der Konkursbetreibung.»

### Haftungsprivileg der GmbH und das Trennungsprinzip {#haftungsprivileg-gmbh}

Bei der GmbH haftet für die Schulden der Gesellschaft ausschliesslich das Gesellschaftsvermögen (Art. 772 Abs. 1 OR). Das Privatvermögen der Gesellschafter bleibt für Gesellschaftsschulden unangreifbar. Geht die Gesellschaft in Konkurs, verliert der Gesellschafter sein eingebrachtes Stammkapital und allfällige der Gesellschaft gewährte Darlehen, sein sonstiges Privatvermögen (z. B. privates Wohneigentum, Sparkonten) bleibt jedoch geschützt.

Dieses strikte *Trennungsprinzip* zwischen Gesellschaft und Inhaber bildet das Fundament des schweizerischen Körperschaftsrechts. Eine Durchbrechung im Wege des zivilrechtlichen **Durchgriffs** kommt nur unter ausserordentlichen Voraussetzungen in Betracht, wenn die juristische Person rechtsmissbräuchlich vorgeschoben wird ([Art. 2 Abs. 2 ZGB](/kommentar/zgb/art-002/)). In [BGE 132 III 489](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_005_BGE-132-III-489_2006.html#consideration_3.2) E. 3.2 brachte das Bundesgericht diese Doktrin auf den Punkt:

> «Beim Durchgriff, welchen das Kantonsgericht zur Begründung herangezogen hat, wird die rechtliche Selbstständigkeit einer juristischen Person nicht beachtet. Dazu bedarf es eines eigentlichen Rechtsmissbrauchs, einer offenbar zweckwidrigen, missbräuchlichen Verwendung der juristischen Person durch die beherrschende Person.»

### Grenzen der Haftungsbeschränkung: Organverantwortlichkeit und Behandlungsfehler {#grenzen-haftungsbeschraenkung}

Das Haftungsprivileg der GmbH ist in der Praxis jedoch kein absoluter Freipass:

1. **Organverantwortlichkeit ([Art. 754](/kommentar/or/art-754/) i.V.m. Art. 827 OR):**  
   Verletzt die geschäftsführende Person ihre Treue- und Sorgfaltspflichten – beispielsweise durch verspätete Konkursanmeldung bei Überschuldung ([Art. 725b](/kommentar/or/art-725b/) i.V.m. Art. 820 OR), Nichtabführen von Arbeitnehmerbeiträgen der AHV ([Art. 52 AHVG](/kommentar/ahvg/art-052/)) oder unzulässige Vermögensentnahmen –, haftet sie der Gesellschaft und den Gläubigern gegenüber persönlich mit ihrem Privatvermögen. Das Bundesgericht stellte in [BGE 139 III 24](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_005_BGE-139-III-24_2013.html#consideration_3.2) E. 3.2 klar:
   > «Nach Art. 717 Abs. 1 OR müssen die Mitglieder des Verwaltungsrats, sowie Dritte, die mit der Geschäftsführung befasst sind, ihre Aufgaben mit aller Sorgfalt erfüllen und die Interessen der Gesellschaft in guten Treuen wahren.»
2. **Bankgarantien und Bürgschaften:**  
   Geschäftsbanken verlangen bei Krediten an kleine GmbHs (z. B. für Praxisausbau oder Medizingeräte) von den Gesellschaftern praktisch ausnahmslos persönliche Solidarbürgschaften (Art. 492 ff. OR). In diesem Umfang wird das gesellschaftsrechtliche Haftungsprivileg vertraglich ausgehebelt.
3. **Persönliche Deliktshaftung bei Behandlungsfehlern (Art. 41 OR):**  
   In therapeutischen und medizinischen Berufen (wie der Physiotherapie) schützt die GmbH nicht vor der persönlichen Haftung für eigene Behandlungsfehler. Zwar wird der Behandlungsvertrag primär mit der GmbH geschlossen (vertragliche Haftung nach Art. 97 OR), die behandelnde Fachperson haftet der Patientin bei einer Körperverletzung jedoch stets auch persönlich und direkt aus unerlaubter Handlung (Art. 41 OR). Gegen dieses Behandlungsrisiko schützt daher in beiden Rechtsformen ausschliesslich eine solide Berufshaftpflichtversicherung.

---

## Steuerliche Behandlung und Gestaltungsspielraum {#steuerliche-behandlung}

Die steuerliche Behandlung unterscheidet sich grundlegend darin, ob das Unternehmen als steuerlich transparentes Gebilde oder als eigenständiges Steuersubjekt behandelt wird.

### Einzelfirma: Direkte Zurechnung und Progression {#steuern-einzelfirma}

Die Einzelfirma ist steuerlich kein eigenes Subjekt. Der gesamte Reingewinn des Geschäftsjahres wird der Inhaberin als persönliches Einkommen aus selbständiger Erwerbstätigkeit zugerechnet (Art. 18 DBG) und zusammen mit allfälligen übrigen Einkünften der ordentlichen Einkommenssteuer von Bund, Kanton und Gemeinde unterworfen. Ebenso wird das im Betrieb gebundene Netto-Geschäftsvermögen dem steuerbaren Privatvermögen zugeschlagen.

* **Nachteil:** Bei erfolgreichem Geschäftsgang treiben hohe Gewinne die Steuerprogression massiv in die Höhe. Gewinne können nicht steuerneutral im Betrieb thesauriert werden; auch reinvestiertes Geld wurde vorgängig voll versteuert.
* **Vorteil:** Anfängliche Geschäftsverluste (typisch in den ersten Aufbaujahren einer Praxis) können direkt mit anderen privaten Einkünften der Gründerin verrechnet werden (Art. 31 DBG).

### GmbH: Trennung der Steuersubjekte und wirtschaftliche Doppelbesteuerung {#steuern-gmbh}

Die GmbH ist als juristische Person ein eigenständiges Steuersubjekt (Art. 49 Abs. 1 lit. a DBG):

1. **Ebene Gesellschaft:** Die GmbH versteuert ihren Reingewinn (Gewinnsteuer) und ihr Eigenkapital (Kapitalsteuer).
2. **Ebene Inhaber:** Der Inhaber versteuert den von der GmbH an ihn ausgerichteten Lohn als Einkommen aus unselbständiger Erwerbstätigkeit (Art. 17 DBG). Schüttet die GmbH Dividenden aus, unterliegen diese beim Inhaber als Vermögensertrag der Einkommenssteuer ([Art. 20 Abs. 1 lit. c DBG](/kommentar/dbg/art-020/)), wobei das System der Teilbesteuerung (auf Bundesebene zu 70 %, im Kanton meist zu 50–70 %) die wirtschaftliche Doppelbesteuerung mildert.

* **Gestaltungsvorteil (Thesaurierung):** Werden Gewinne zur Bildung von Reserven oder für künftige Geräteinvestitionen in der GmbH belassen, fallen nur die moderaten kantonalen und eidgenössischen Gewinnsteuern an (je nach Standort ca. 12–15 % Gesamtbelastung). Der Spitzensteuersatz der Einkommenssteuer (bis zu 35–45 %) wird vermieden, solange keine Ausschüttung erfolgt.
* **Schranke des Drittvergleichs (*Dealing at arm's length*):**  
  Der Inhaber kann Löhne und Entnahmen nicht willkürlich festsetzen, um Steuern oder Sozialabgaben zu optimieren. Übermässige Lohnzahlungen oder zinslose Aktionärsdarlehen qualifizieren steuerlich als verdeckte Gewinnausschüttung bzw. geldwerte Leistung. In [BGE 138 II 57](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_004_BGE-138-II-57_2012.html#consideration_3.1) E. 3.1 hielt das Bundesgericht fest:
  > «Eine geldwerte Leistung liegt aber insoweit vor, als von diesen Drittbedingungen bzw. einem üblichen und marktgerechten Geschäftsgebaren abgewichen wird. Bei diesem Drittvergleich […] sind in jedem Einzelfall, ausgehend von dem zwischen der Gesellschaft und dem Beteiligten abgeschlossenen Vertrag, alle konkreten Umstände zu berücksichtigen»

---

## Sozialversicherungsstatut und berufliche Vorsorge {#sozialversicherungen}

Die Wahl der Rechtsform determiniert den beitrags- und leistungsrechtlichen Status in den Sozialversicherungen.

### Selbständigerwerbende bei der Einzelfirma {#sozialversicherung-einzelfirma}

Der Inhaber einer Einzelfirma wird von der Ausgleichskasse als Selbständigerwerbender eingestuft:

{{< wortlaut gesetz="ahvg" art="art-012" >}}

* **1. Säule (AHV/IV/EO):** Beiträge werden auf Basis des steuerlich veranlagten Reingewinns erhoben (degressive Skala ab ca. 5.3 % bis zum Maximalsatz von rund 10.0 %). Der Inhaber zahlt die gesamten Beiträge alleine (keine Arbeitgeberhälfte).
* **2. Säule (BVG):** Für Selbständigerwerbende besteht **kein BVG-Obligatorium**. Sie können sich freiwillig einer Vorsorgeeinrichtung anschliessen (Art. 44 BVG).
* **3. Säule (Säule 3a):** Zum Ausgleich für das fehlende BVG-Obligatorium steht Selbständigen der grosse 3a-Abzug offen (bis zu 20 % des Erwerbseinkommens, max. CHF 35'280, Stand 2026).
* **Unfallversicherung (UVG) & Krankentaggeld:** Keine Pflichtversicherung; Unfälle und Erwerbsausfälle bei Krankheit müssen vollumfänglich über private Zusatzversicherungen gedeckt werden.
* **Arbeitslosenversicherung (ALV):** Selbständige können sich nicht gegen Arbeitslosigkeit versichern; sie zahlen keine ALV-Beiträge und haben keinen Anspruch auf Leistungen.

### Angestelltenstatus bei der GmbH – mit dem Fallstrick der ALV {#sozialversicherung-gmbh}

Wer als Gesellschafter-Geschäftsführer in der eigenen GmbH tätig ist, gilt sozialversicherungsrechtlich als **Unselbständigerwerbender** (Arbeitnehmer).

* **Paritätische Beiträge:** Die GmbH rechnet auf dem Geschäftsführerlohn die vollen paritätischen Beiträge für AHV/IV/EO, ALV und Familienausgleichskasse ab.
* **BVG-Obligatorium:** Übersteigt der Jahreslohn die BVG-Eintrittsschwelle (CHF 22'680, Stand 2026), ist die GmbH verpflichtet, den Geschäftsführer bei einer Pensionskasse zu versichern. Dies erzwingt einen systematischen Sparprozess für das Alter, verursacht jedoch fixe monatliche Lohnnebenkosten.
* **UVG-Obligatorium:** Der Geschäftsführer ist obligatorisch gegen Berufsunfälle (und ab 8 Wochenstunden auch gegen Nichtberufsunfälle) versichert.
* **Der Fallstrick bei der ALV (Ausschluss trotz Beitragspflicht):**  
  Obwohl die GmbH für den geschäftsführenden Inhaber monatlich ALV-Beiträge abführen muss, erhält dieser bei einem Auftragsrückgang oder einer Betriebsschliessung **weder Kurzarbeitsentschädigung noch Arbeitslosentaggeld**. 

{{< wortlaut gesetz="avig" art="art-031" >}}

Gemäss Art. 31 Abs. 3 lit. c AVIG sind Personen mit arbeitgeberähnlicher Stellung vom Anspruch ausgeschlossen. In [BGE 145 V 200](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_007_BGE-145-V-200_2019.html#consideration_4.1) E. 4.1 und E. 4.5.3 bestätigte das Bundesgericht, dass dieser Ausschluss bei Gesellschaftern einer GmbH absolut gilt:

> «Gemäss Art. 31 Abs. 3 lit. c AVIG haben Personen, die in ihrer Eigenschaft als Gesellschafter, als finanziell am Betrieb Beteiligte oder als Mitglieder eines obersten betrieblichen Entscheidungsgremiums die Entscheidungen des Arbeitgebers bestimmen oder massgeblich beeinflussen können, sowie ihre mitarbeitenden Ehegatten keinen Anspruch auf Kurzarbeitsentschädigung. Praxisgemäss ist diese der Vermeidung von Missbräuchen dienende Bestimmung analog auf arbeitgeberähnliche Personen und deren Ehegatten anzuwenden, die Arbeitslosenentschädigung verlangen»

Erst wenn der Gesellschafter seine Beteiligung und Geschäftsführerfunktion endgültig und nachweisbar aufgibt (oder die GmbH vollständig liquidiert wird), lebt der Anspruch auf Arbeitslosenentschädigung auf.

### Das Risiko der Scheinselbständigkeit in Praxisgemeinschaften {#scheinselbstaendigkeit}

In der Praxis mieten sich selbständige Therapeuten häufig in bestehende Gemeinschaftspraxen oder Institute ein. Hier lauert das Risiko, dass die Ausgleichskasse die Tätigkeit nicht als selbständige Einzelfirma anerkennt, sondern als beitragspflichtiges Anstellungsverhältnis umqualifiziert. 

Das Bundesgericht stellte in [BGE 144 V 111](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_007_BGE-144-V-111_2018.html#consideration_4.2) E. 4.2 am Beispiel einer in einem Institut tätigen Therapeutin klar, dass nicht die vertragliche Bezeichnung, sondern die wirtschaftliche Realität massgebend ist:

> «Nach der Rechtsprechung beurteilt sich die Frage, ob im Einzelfall selbständige oder unselbständige Erwerbstätigkeit vorliegt, nicht aufgrund der Rechtsnatur des Vertragsverhältnisses zwischen den Parteien. Entscheidend sind vielmehr die wirtschaftlichen Gegebenheiten.»

Fehlt es an erheblichem eigenem Unternehmerrisiko (z. B. wenn die Praxis die Patienten zuweist, das Inkasso führt und Vorgaben zur Behandlung macht), fordert die Ausgleichskasse rückwirkend Sozialversicherungsbeiträge vom Praxisinhaber als Arbeitgeber ein.

---

## Besonderheiten bei Gesundheitsberufen (Beispiel Physiotherapie) {#gesundheitsberufe-physiotherapie}

Für Praxen im Gesundheitswesen treten neben die allgemeinen gesellschaftsrechtlichen Regeln spezifische regulatorische Hürden des Bundes- und kantonalen Rechts.

### KVG-Zulassung als Einzelperson vs. Organisation der Physiotherapie {#kvg-zulassung}

{{< wortlaut gesetz="kvg" art="art-035" >}}

Zur Abrechnung zulasten der obligatorischen Krankenpflegeversicherung (OKP) definiert Art. 35 Abs. 2 KVG die zulässigen Leistungserbringer:

1. **Einzelfirma:** Die Physiotherapeutin rechnet unmittelbar als zugelassene Person nach Art. 35 Abs. 2 lit. h KVG ab. Voraussetzung sind ein anerkanntes Diplom, eine zweijährige praktische Tätigkeit (Art. 47 KVV) und eine persönliche ZSR-Nummer (Zahlstellenregister) der SASIS AG.
2. **GmbH:** Wird die Praxis als juristische Person geführt, tritt die GmbH selbst als *Organisation der Physiotherapie* nach Art. 35 Abs. 2 lit. k KVG auf (Art. 52c KVV).  
   * Die Organisation erhält eine eigene ZSR-Nummer.
   * Sämtliche in der Organisation tätigen Therapeutinnen und Therapeuten müssen über eine kantonale Berufsausübungsbewilligung verfügen.
   * Wie das [Verwaltungsgericht Schwyz im Entscheid III 2024 140 vom 17. Januar 2025](https://entscheidsuche.ch/docs/SZ_Verwaltungsgericht/SZ_VG_001_III-2024-140_2025-01-17.pdf) festhielt, ist bei einer als Organisation zugelassenen Praxis die Organisation selbst die abrechnende Leistungserbringerin im Sinne des KVG; die dort angestellten Therapeuten rechnen nicht individuell über eigene Nummern ab, sondern die Organisation haftet für die Erfüllung der Qualitätsanforderungen nach Art. 58a ff. KVG.

### Praxisnachfolge und Veräusserung {#nachfolge}

Ein oft unterschätzter Aspekt bei der Gründung ist die spätere Übergabe oder der Verkauf der Praxis:

* **Einzelfirma:** Da keine gesonderte juristische Person existiert, müssen beim Verkauf sämtliche Mietverträge, Patientendossiers (unter Beachtung des Berufsgeheimnisses nach [Art. 321 StGB](/kommentar/stgb/art-321/)), Geräteleasings und Arbeitsverträge im Rahmen eines aufwendigen *Asset Deals* (oder einer partiellen Vermögensübertragung nach Art. 69 ff. FusG) einzeln übertragen werden. Vermieter oder Vertragspartner können Zustimmungen verweigern.
* **GmbH:** Die Übertragung erfolgt unkompliziert durch Abtretung der Stammanteile (*Share Deal*, Art. 784 OR). Sämtliche Verträge der Praxis mit Dritten, Vermietern, Lieferanten und Krankenkassen laufen unverändert mit der Gesellschaft weiter.

---

## Praxishinweise {#praxishinweise}

### Typische Hürden und Streitpunkte {#huerden-und-streitpunkte}

1. **Unterschätzte Fixkosten der GmbH:**  
   Viele Gründer kleiner Praxen lassen sich von der Haftungsbeschränkung blenden, unterschätzen jedoch die laufenden Administrations- und Fixkosten einer GmbH: separate Steuererklärung, zwingende doppelte Buchhaltung, BVG-Verwaltungsgebühren und Revisionsstellen-Verzichtserklärung (*Opting-out*, Art. 727a Abs. 2 OR). Liegt der Jahresgewinn unter ca. CHF 80'000 bis CHF 100'000, fressen diese Mehrkosten den steuerlichen Nutzen der GmbH in der Regel vollständig auf.
2. **Vermeintlicher Schutz bei Patientenschäden:**  
   Die GmbH schirmt unternehmerische Risiken (Miete, Leasing, Lieferantenschulden) ab. Bei Kunstfehlern oder therapeutischen Verletzungen greift jedoch die persönliche Haftung der behandelnden Person aus unerlaubter Handlung (Art. 41 OR). Die Berufshaftpflichtversicherung ist daher in beiden Rechtsformen existentiell und darf bei einer GmbH keinesfalls vernachlässigt werden.
3. **Beitragslücke bei Scheinselbständigkeit:**  
   Wer eine Praxisgemeinschaft betreibt und Kollegen einquartiert, muss zwingend darauf achten, dass diese als echte Einzelfirmen mit eigenem Patientenstamm, eigenem Inkasso und eigener ZSR-Nummer auftreten. Andernfalls drohen nach [BGE 144 V 111](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_007_BGE-144-V-111_2018.html#consideration_4.2) massive AHV-Nachzahlungen für vermeintlich freie Mitarbeiter.

### Entscheidungsmatrix: Wann Einzelfirma, wann GmbH? {#entscheidungsmatrix}

| Kriterium | Einzelfirma empfohlen | GmbH empfohlen |
|---|---|---|
| **Finanzierungsbedarf zu Beginn** | Gering; wenig Startkapital vorhanden | CHF 20'000 Stammkapital problemlos verfügbar |
| **Geschäftsrisiko & Fixkosten** | Geringe Miet- und Fixkosten; wenig Investitionen in Grossgeräte | Hohe Investitionen, teure Praxisgeräte, langjährige Mietverträge |
| **Personal** | Einzelpraxis ohne angestelltes Fachpersonal | Mehrere angestellte Therapeuten oder Assistenten |
| **Erwarteter Reingewinn** | Bis ca. CHF 80'000–100'000 p.a. | Deutlich über CHF 100'000 p.a. (Thesaurierung lohnt sich) |
| **Planungshorizont** | Eher kurzfristig oder Testphase | Langfristig, spätere Aufnahme von Partnern oder Praxisverkauf geplant |

---

## Leitentscheide {#leitentscheide}

| Entscheid | Fundstelle / Volltext | Gegenstand | Kernaussage |
|---|---|---|---|
| **Trennungsprinzip & Durchgriff** | [BGE 132 III 489](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_005_BGE-132-III-489_2006.html#consideration_3.2) E. 3.2 | Missbräuchliche Verwendung der juristischen Person | Die rechtliche Selbständigkeit einer juristischen Person ist strikt zu beachten; ein Durchgriff auf den Inhaber setzt eigentlichen Rechtsmissbrauch voraus. |
| **Organhaftung der Geschäftsführung** | [BGE 139 III 24](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_005_BGE-139-III-24_2013.html#consideration_3.2) E. 3.2 | Treue- und Sorgfaltspflicht der Organe (Art. 717 / 754 OR) | Für die Sorgfalt gilt ein objektiver Massstab; die Pflichtverletzung führt zur persönlichen Haftung der Organe gegenüber Gesellschaft und Gläubigern. |
| **Konkursbetreibung nach Löschung** | [BGE 122 III 204](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_005_BGE-122-III-204_1996-06-18.html#consideration_2.) E. 2. | Nachhaftung im Handelsregister (Art. 40 SchKG) | Der im Handelsregister eingetragene Inhaber einer Einzelfirma unterliegt auch nach Publikation der Löschung noch während 6 Monaten der Konkursbetreibung. |
| **Kein ALV-Taggeld bei GmbH-Organstellung** | [BGE 145 V 200](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_007_BGE-145-V-200_2019.html#consideration_4.1) E. 4.1 / 4.5.3 | Arbeitgeberähnliche Stellung nach Art. 31 Abs. 3 lit. c AVIG | Gesellschafter einer GmbH haben wegen ihrer gesetzlichen Einflussmöglichkeit unabhängig von der Beteiligungshöhe keinen Anspruch auf Arbeitslosenentschädigung. |
| **AHV-Status und Scheinselbständigkeit** | [BGE 144 V 111](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_007_BGE-144-V-111_2018.html#consideration_4.2) E. 4.2 | Abgrenzung selbständig / unselbständig (Art. 12 AHVG) | Massgebend sind die tatsächlichen wirtschaftlichen Gegebenheiten (Unternehmerrisiko und Abhängigkeit), nicht die zivilrechtliche Vertragsbezeichnung. |
| **Steuerlicher Drittvergleich** | [BGE 138 II 57](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_004_BGE-138-II-57_2012.html#consideration_3.1) E. 3.1 | Geldwerte Leistungen und Darlehen an Gesellschafter | Geschäfte zwischen Inhaber und Gesellschaft müssen dem Drittvergleich (*Dealing at arm's length*) standhalten, andernfalls liegt eine verdeckte Gewinnausschüttung vor. |
| **KVG-Zulassung als Organisation** | [SZ VG III 2024 140 vom 17.01.2025](https://entscheidsuche.ch/docs/SZ_Verwaltungsgericht/SZ_VG_001_III-2024-140_2025-01-17.pdf) | Zulassung als Organisation der Physiotherapie (Art. 35 KVG) | Die als Organisation der Physiotherapie zugelassene Praxis tritt als eigenständige Leistungserbringerin auf; angestellte Therapeuten rechnen nicht individuell über eigene Nummern ab. |

---

## Literatur {#literatur}

* **Arthur Meier-Hayoz / Peter Forstmoser / Hans-Ueli Vogt**, Schweizerisches Gesellschaftsrecht, 13. Aufl., Bern 2024.
* **Peter Böckli**, Schweizer Aktienrecht, 4. Aufl., Zürich/Basel/Genf 2009.
* **Thomas Bauer**, in: Basler Kommentar, Bundesgesetz über Schuldbetreibung und Konkurs I, 3. Aufl., Basel 2021, Art. 39–40 SchKG.
* **Boris Rubin**, Commentaire de la loi sur l'assurance-chômage, Genf/Zürich/Basel 2014, Art. 31 AVIG.
* **Ueli Kieser**, ATSG-Kommentar, 4. Aufl., Zürich/Basel/Genf 2020.
