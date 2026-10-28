---
title: "Haftgründe und Ersatzmassnahmen im Strafverfahren"
date: 2026-10-24
lastmod: 2026-10-24
description: "Voraussetzungen, Ablauf und Rechtsschutz bei Untersuchungs- und Sicherheitshaft nach Art. 221 ff. StPO: dringender Tatverdacht, Haftgründe (Flucht-, Kollusions-, einfache und qualifizierte Wiederholungsgefahr), Vorrang von Ersatzmassnahmen (Art. 237 StPO), Fristen des gerichtlichen Verfahrens und Rüge von Haftbedingungen."
tags: ["Strafprozess", "Haft", "Untersuchungshaft", "Sicherheitshaft", "Haftgründe", "Ersatzmassnahmen", "Fluchtgefahr", "Kollusionsgefahr", "Wiederholungsgefahr", "Zwangsmassnahmengericht", "Electronic Monitoring"]
typ: verfahren
kurz: "Freiheitsentzug im Strafverfahren ist die schärfste Zwangsmassnahme und setzt neben dringendem Tatverdacht einen besonderen Haftgrund voraus: Flucht-, Kollusions-, Wiederholungs- oder Ausführungsgefahr. Nach dem Grundsatz der Verhältnismässigkeit müssen Gerichte und Staatsanwaltschaften stets prüfen, ob mildere Ersatzmassnahmen – wie Meldepflichten, Schriftensperren, Rayonverbote oder Electronic Monitoring – denselben Zweck erfüllen. Für Anordnung, Haftverlängerung und Entlassungsgesuche gelten strikte Fristen (maximal 96 Stunden bis zum erstinstanzlichen Haftentscheid) und eine zwingende richterliche Kontrolle."
sachgebiete: [strafprozess.haft, strafprozess.verteidigung, grundrechte]
normen:
  - { gesetz: stpo, art: art-130 }
  - { gesetz: stpo, art: art-221 }
  - { gesetz: stpo, art: art-222 }
  - { gesetz: stpo, art: art-225 }
  - { gesetz: stpo, art: art-226 }
  - { gesetz: stpo, art: art-227 }
  - { gesetz: stpo, art: art-228 }
  - { gesetz: stpo, art: art-236 }
  - { gesetz: stpo, art: art-237 }
  - { gesetz: bv, art: art-031 }
  - { gesetz: emrk, art: art-003 }
  - { gesetz: emrk, art: art-005 }
stichworte: ["Untersuchungshaft", "Sicherheitshaft", "Haftgründe", "Ersatzmassnahmen", "Fluchtgefahr", "Kollusionsgefahr", "Wiederholungsgefahr", "qualifizierte Wiederholungsgefahr", "Electronic Monitoring", "Zwangsmassnahmengericht", "Champ-Dollon", "notwendige Verteidigung"]
revisions:
  - date: 2026-10-24
    by: "Antigravity Agent"
    model: "gemini-3.8-flash"
    note: "Erstfassung nach Skill glossagens-themen (Typ verfahren, Querschnitt StPO/BV/EMRK). Fristen- und Phasenablauf nach Art. 224 ff. StPO strukturiert. BGE-Leitentscheide (BGE 137 IV 92, 137 IV 122, 140 IV 19, 140 IV 74, 141 IV 190, 142 IV 29, 143 IV 316, 143 IV 330, 145 IV 503, 150 IV 149) und aktuelle Praxis der II. strafrechtlichen Abteilung (BGer 7B_1035/2024, 7B_1311/2026) ausgewertet und verlinkt; Zitate, Links und Anker mit pruefen.py verifiziert."
---

## Überblick {#ueberblick}

Die Anordnung von Untersuchungshaft (im Vorverfahren) und Sicherheitshaft (ab Anklageerhebung) stellt den intensivsten Grundrechtseingriff dar, den die Strafprozessordnung kennt. Er berührt unmittelbar das Recht auf persönliche Freiheit ([Art. 10 Abs. 2](/kommentar/bv/art-010/), [Art. 31 BV](/kommentar/bv/art-031/)) und die Garantie des Schutzes vor willkürlichem Freiheitsentzug gemäss [Art. 5 EMRK](/kommentar/emrk/art-005/).

Aus diesem Grund unterliegt die strafprozessuale Haft einem dreifachen Schutzmechanismus:
1. **Materiell** darf Haft nur angeordnet werden, wenn die beschuldigte Person eines Verbrechens oder Vergehens dringend verdächtig ist und kumulativ ein besonderer Haftgrund (Flucht-, Kollusions-, Wiederholungs- oder Ausführungsgefahr gemäss [Art. 221 StPO](/kommentar/stpo/art-221/)) vorliegt.
2. **Teleologisch** gilt der verfassungs- und konventionsrechtliche Vorrang milderer Massnahmen: Haft ist stets *ultima ratio*; lässt sich die bestehende Gefahr durch Ersatzmassnahmen nach [Art. 237 StPO](/kommentar/stpo/art-237/) bannen, müssen diese angeordnet werden.
3. **Verfahrensrechtlich** gilt ein striktes Regime richterlicher Kontrolle mit kurzen, gesetzlichen Maximalfristen für Anordnung, Verlängerung und Haftentlassung ([Art. 224 ff. StPO](/kommentar/stpo/art-226/)).

### Die Phasen des Haftverfahrens im Überblick {#phasen-ueberblick}

| Phase | Zuständige Behörde | Gesetzliche Frist | Gegenstand / Massnahme | Rechtsschutz |
|---|---|---|---|---|
| **Vorläufige Festnahme** (Art. 217–219 StPO) | Polizei | max. 24 Stunden | Zuführung an Staatsanwaltschaft oder Freilassung | Haftbeschwerde (Art. 393 StPO) |
| **Haftantrag Vorverfahren** (Art. 224 StPO) | Staatsanwaltschaft | max. 48 Stunden seit Festnahme | Einreichung des begründeten Haftantrags beim Zwangsmassnahmengericht (ZMG) | Rüge im Verfahren vor ZMG |
| **Haftentscheid Erstinstanz** (Art. 226 StPO) | Zwangsmassnahmengericht (ZMG) | max. 48 Stunden seit Haftantrag (total max. 96h seit Festnahme) | Anordnung Untersuchungshaft (max. 3 Monate) oder Ersatzmassnahmen oder Freilassung | Beschwerde an kantonale Beschwerdeinstanz innert 10 Tagen (Art. 393 Abs. 1 lit. c StPO) |
| **Haftverlängerung** (Art. 227 StPO) | Staatsanwaltschaft & ZMG | spätestens 4 Tage vor Haftablauf Gesuch der StA | Verlängerung der Untersuchungshaft (je max. 3 Monate, bei Verbrechen bis zu 6 Monate) | Beschwerde innert 10 Tagen an Beschwerdeinstanz |
| **Haftentlassungsgesuch** (Art. 228 StPO) | Staatsanwaltschaft & ZMG | StA leitet Gesuch innert 3 Tagen weiter; ZMG entscheidet innert 5 Tagen | Überprüfung des Fortbestands von Tatverdacht und Haftgründen; Ersatzmassnahmen | Beschwerde innert 10 Tagen an Beschwerdeinstanz |
| **Sicherheitshaft** (Art. 229–233 StPO) | Verfahrensleitung des Sachgerichts / ZMG | ab Eingang der Anklageschrift | Sicherung des Haupt- und Rechtsmittelverfahrens bis zum rechtskräftigen Urteil | Beschwerde an kantonale Beschwerdeinstanz bzw. BGer |
| **Vollzug von Ersatzmassnahmen** (Art. 237 StPO) | ZMG bzw. Sachgericht | periodische Befristung (analog Art. 227 StPO) | Meldepflichten, Schriftensperre, Kaution, Rayonverbote, Electronic Monitoring | Beschwerde innert 10 Tagen (Art. 237 Abs. 4 StPO) |

Dieses Thema fasst das Zusammenspiel der materiellen Haftgründe, der Ersatzmassnahmen und des Fristenlaufs systematisch zusammen. Die vertiefte Kommentierung der einzelnen Bestimmungen findet sich in den Kommentaren zu [Art. 221 StPO](/kommentar/stpo/art-221/), [Art. 226 StPO](/kommentar/stpo/art-226/), [Art. 227 StPO](/kommentar/stpo/art-227/), [Art. 228 StPO](/kommentar/stpo/art-228/) und [Art. 237 StPO](/kommentar/stpo/art-237/).

---

## Die materiellen Haftvoraussetzungen {#materielle-voraussetzungen}

{{< wortlaut gesetz="stpo" art="art-221" >}}

### Dringender Tatverdacht (Art. 221 Abs. 1 Ingress StPO) {#tatverdacht}

Der dringende Tatverdacht ist die unverzichtbare Grundvoraussetzung jeder strafprozessualen Haft. Liegt kein dringender Tatverdacht vor, darf keine Haft und auch keine Ersatzmassnahme angeordnet werden.

Das Bundesgericht grenzt die Kognition des Haftrichters beim Tatverdacht strikt von derjenigen des erkennenden Sachrichters ab: «Im Gegensatz zum erkennenden Sachrichter hat das Bundesgericht bei der Überprüfung des allgemeinen Haftgrundes des dringenden Tatverdachtes (Art. 221 Abs. 1 Ingress StPO) keine erschöpfende Abwägung sämtlicher belastender und entlastender Beweisergebnisse vorzunehmen.» ([BGE 143 IV 330](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-143-IV-330_2017.html#consideration_2.1) E. 2.1). Im Haftprüfungsverfahren genügt vielmehr der «Nachweis von konkreten Verdachtsmomenten, wonach das untersuchte Verhalten mit erheblicher Wahrscheinlichkeit die fraglichen Tatbestandsmerkmale erfüllen könnte» (BGE 143 IV 330 E. 2.1).

Die Anforderungen an die Dichte des Tatverdachts wandeln sich mit fortschreitender Verfahrensdauer:
* **Zu Beginn der Untersuchung** genügen hinreichende und konkrete Anhaltspunkte, die den Verdacht einer strafbaren Handlung begründen, da die Beweise erst erhoben werden müssen ([BGE 143 IV 316](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-143-IV-316_2017.html#consideration_2.) E. 2).
* **Je länger die Haft andauert**, desto höher sind die Anforderungen an die Verdachtsdichte. Die Strafverfolgungsbehörden müssen den Verdacht durch konkrete Untersuchungsergebnisse erhärten.
* **Prozesshindernisse schliessen den Tatverdacht aus**: Steht fest, dass die vorgeworfene Tat mit grosser Wahrscheinlichkeit bereits verjährt ist oder andere unüberwindbare Prozesshindernisse vorliegen, fehlt es am haftbegründenden Tatverdacht, was zur sofortigen Haftentlassung führt ([BGE 151 IV 57](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-151-IV-57_2025.html#consideration_3.1) E. 3.1).

---

### Die besonderen Haftgründe nach Art. 221 StPO {#besondere-haftgruende}

Neben dem Tatverdacht muss mindestens einer der gesetzlichen Haftgründe nachgewiesen sein:

#### 1. Fluchtgefahr (Abs. 1 lit. a) {#fluchtgefahr}

Fluchtgefahr liegt vor, wenn ernsthaft zu befürchten ist, die beschuldigte Person werde sich durch Flucht dem Strafverfahren oder der zu erwartenden Sanktion entziehen. Das Bundesgericht verlangt eine Gesamtwürdigung aller Umstände des Einzelfalls:
> «Selon la jurisprudence, le risque de fuite doit s'analyser en fonction d'un ensemble de critères tels que le caractère de l'intéressé, sa moralité, ses ressources, ses liens avec l'Etat qui le poursuit ainsi que ses contacts à l'étranger, qui font apparaître le risque de fuite non seulement possible mais également probable.» ([BGE 145 IV 503](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-145-IV-503_2019.html#consideration_2.2) E. 2.2).

* **Stufung in moderate und ausgeprägte Fluchtgefahr**: Eine ausländische Staatsangehörigkeit oder das Fehlen familiärer Bindungen in der Schweiz begründen für sich allein noch keine ausgeprägte Fluchtgefahr. Ist die Straferwartung gering und liegen keine Fluchtvorbereitungen vor, begründet etwa die existenzielle Angewiesenheit auf behördliche Fürsorgeleistungen oder Asylnothilfe einen faktischen Verankerungsfaktor; die Fluchtgefahr ist in solchen Konstellationen lediglich als *moderat* einzustufen ([BGer 7B_1311/2026 vom 15.10.2026](https://bger-update.ch/zusammenfassung/34698/)).
* **Surrogatverbot**: Strafprozessuale Untersuchungshaft dient ausschliesslich der Sicherung des hängigen Strafverfahrens. Sie darf niemals als Surrogat für ausländerrechtliche Administrativhaft (wie Ausschaffungs- oder Dublin-Haft nach Art. 75 ff. AIG) missbraucht werden.
* **Hohe Straferwartung**: Droht eine langjährige Freiheitsstrafe, namentlich nach erstinstanzlicher Verurteilung wegen eines schweren Gewaltverbrechens, intensiviert sich der Fluchtreiz massiv; in solchen Fällen scheiden mildere Ersatzmassnahmen regelmässig aus (BGE 145 IV 503 E. 2.3).

#### 2. Kollusionsgefahr (Abs. 1 lit. b) {#kollusionsgefahr}

Kollusionsgefahr (Verdunkelungsgefahr) bezweckt die Sicherung der Wahrheitsfindung:
> «Die strafprozessuale Haft wegen Kollusionsgefahr soll verhindern, dass die beschuldigte Person die Freiheit dazu missbrauchen würde, die wahrheitsgetreue Abklärung des Sachverhalts zu vereiteln oder zu gefährden.» ([BGE 137 IV 122](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-137-IV-122_2011.html#consideration_4.2) E. 4.2).

Kollusionsgefahr darf nicht abstrakt behauptet werden. Erforderlich sind konkrete Anhaltspunkte, etwa dass die beschuldigte Person Zeugen, Auskunftspersonen oder Mitbeschuldigte bedroht, beeinflusst oder Absprachen trifft, Spuren verwischt oder Beweismittel beseitigt. Nach Abschluss der wesentlichen Untersuchungshandlungen (insbesondere nach Durchführung der Schlusseinvernahmen) nimmt die Kollusionsgefahr typischerweise ab und bedarf einer besonders strengen Begründung (BGE 137 IV 122 E. 4.2).

#### 3. Einfache Wiederholungsgefahr (Abs. 1 lit. c) {#wiederholungsgefahr}

Die einfache Wiederholungsgefahr schützt potenzielle Opfer vor neuen Straftaten. Mit der StPO-Revision per 1. Januar 2024 hat der Gesetzgeber die Anforderungen grundlegend verschärft und die frühere Rechtsprechung invalidiert:
* **Zwingendes Erfordernis von zwei rechtskräftigen Vorstrafen**: Gemäss revidiertem Art. 221 Abs. 1 lit. c StPO und der Leitpraxis des Bundesgerichts ([BGer 7B_1035/2024 vom 19.11.2024](https://entscheidsuche.ch/docs/CH_BGer/CH_BGer_007_7B-1035-2024_2024-11-19.html)) setzt einfache Wiederholungsgefahr zwingend voraus, dass die beschuldigte Person **zuvor wegen mindestens zwei gleichartigen Verbrechen oder schweren Vergehen rechtskräftig verurteilt** worden ist.
* **Keine Anrechnung hängiger Verfahren**: Handlungen aus der laufenden Untersuchung – selbst bei erdrückender Beweislage, Geständnis oder Überführung auf frischer Tat – gelten nicht als rechtskräftige Vortaten im Sinne von Abs. 1 lit. c.

#### 4. Qualifizierte Wiederholungsgefahr (Abs. 1bis) {#qualifizierte-wiederholungsgefahr}

Um die durch das strikte Vortatenerfordernis entstandene Schutzlücke bei gefährlichen Ersttätern zu schliessen, schuf der Gesetzgeber per 1. Januar 2024 den neuen Haftgrund der *qualifizierten Wiederholungsgefahr*:
* **Voraussetzungen**: Dringender Verdacht, durch ein Verbrechen oder schweres Vergehen die physische, psychische oder sexuelle Integrität einer Person schwer beeinträchtigt zu haben (lit. a), und die ernsthafte und unmittelbare Gefahr, dass die beschuldigte Person ein gleichartiges schweres Verbrechen verüben wird (lit. b).
* **Umgekehrte Proportionalität**: Nach [BGE 150 IV 149](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-150-IV-149_2024.html#consideration_3.2) E. 3.2 f. gilt hier das Prinzip, dass an die Wahrscheinlichkeit eines Rückfalls umso geringere Anforderungen zu stellen sind, je schwerer die drohende Tat wiegt (z.B. bei Tötungs- oder schweren Sexualdelikten).
* **Zeitliche Schranken**: Die «Unmittelbarkeit» der drohenden Gefahr entfällt, wenn sich die beschuldigte Person nach der Anlasstat über einen langen Zeitraum (etwa über ein Jahr) in Freiheit vollkommen delikts- und beanstandungsfrei verhalten hat.

#### 5. Ausführungsgefahr (Abs. 2) {#ausfuehrungsgefahr}

Ausführungsgefahr liegt vor, wenn die beschuldigte Person droht, ein schweres Verbrechen oder Vergehen auszuführen, das sie zuvor angekündigt hat. Sie dient dem präventiven Rechtsgüterschutz und setzt eine ernsthafte, konkrete Bedrohungslage voraus. Häufigster Anwendungsbereich sind Drohungen im Rahmen eskalierender Paarkonflikte oder häuslicher Gewalt ([BGE 140 IV 19](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-140-IV-19_2014.html#consideration_2.) E. 2).

---

## Der Vorrang von Ersatzmassnahmen (Art. 237 StPO) {#ersatzmassnahmen}

{{< wortlaut gesetz="stpo" art="art-237" >}}

### Das Subsidiaritätsprinzip: Haft als ultima ratio {#subsidiaritaet}

Art. 237 Abs. 1 StPO konkretisiert das verfassungsrechtliche Verhältnismässigkeitsprinzip ([Art. 36 Abs. 3 BV](/kommentar/bv/art-036/)): Das zuständige Gericht **muss** anstelle von Untersuchungs- oder Sicherheitshaft eine oder mehrere mildere Massnahmen anordnen, wenn diese den gleichen Zweck wie die Haft erfüllen.
> «Untersuchungshaft ist somit "ultima ratio" […]. Kann der damit verfolgte Zweck - die Verhinderung von Flucht-, Kollusions-, Wiederholungs- oder Ausführungsgefahr - mit milderen Massnahmen erreicht werden, sind diese anzuordnen» ([BGE 140 IV 74](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-140-IV-74_2014.html#consideration_2.2) E. 2.2).
> «Strafprozessuale Haft darf nur als "ultima ratio" angeordnet oder aufrechterhalten werden. Wo sie durch weniger einschneidende Massnahmen ersetzt werden kann, muss von ihrer Anordnung oder Fortdauer abgesehen und an ihrer Stelle eine solche Ersatzmassnahme verfügt werden» ([BGE 150 IV 149](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-150-IV-149_2024.html#consideration_3.3) E. 3.3.1).

Die Prüfung von Ersatzmassnahmen ist von Amtes wegen vorzunehmen; Gerichte dürfen Haftanträge nicht bewilligen, ohne begründet darzulegen, weshalb mildere Massnahmen zur Gefahrenbannung nicht ausreichen.

### Der Massnahmenkatalog im Einzelnen {#katalog-ersatzmassnahmen}

Art. 237 Abs. 2 StPO enthält einen nicht abschliessenden Katalog möglicher Ersatzmassnahmen:
* **Sicherheitsleistung / Kaution (lit. a)**: Hinterlegung eines Geldbetrags oder einer Bankgarantie zur Bannung von Fluchtgefahr. Die Höhe richtet sich nach den finanziellen Verhältnissen der beschuldigten Person und dem Fluchtanreiz.
* **Schriftensperre (lit. b)**: Hinterlegung von Reisepass, Identitätskarte oder Führerausweis bei den Strafbehörden.
* **Rayon-, Kontakt- und Wohnsitzauflagen (lit. c und g)**: Hausarrest, das Verbot, ein bestimmtes Gebiet oder Gebäude zu betreten, sowie das Verbot der Kontaktaufnahme mit Opfern oder Zeugen (insbesondere bei häuslicher Gewalt und Kollusionsgefahr).
* **Meldepflichten (lit. d)**: Die Pflicht, sich periodisch (z.B. täglich oder wöchentlich) bei einem Polizeiposten zu melden. Wirkt vor allem bei moderater Fluchtgefahr disziplinierend und kontrollierend.
* **Therapie- und Kontrollauflagen (lit. f)**: Verpflichtung zur Durchführung einer ambulanten psychiatrischen Behandlung oder zur regelmässigen Abgabe von Urin- oder Blutproben (Abstinenzkontrolle).

### Electronic Monitoring und seine Grenzen (Abs. 3) {#electronic-monitoring}

Zur Überwachung von Ersatzmassnahmen (wie Hausarrest oder Rayonverboten) kann das Gericht den Einsatz elektronischer Überwachungsgeräte (Fussfesseln / Electronic Monitoring) anordnen (Art. 237 Abs. 3 StPO).

Das Bundesgericht hat jedoch die technischen und rechtlichen Grenzen dieser Technologie verdeutlicht:
* **Keine physische Barriere**: Electronic Monitoring meldet das Verlassen eines Rayons oder das Entfernen des Geräts stets nur nachträglich (*ex post*). Es bietet keine physische Verhinderung einer Flucht ([BGE 145 IV 503](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-145-IV-503_2019.html#consideration_3.3.1) E. 3.3.1).
* **Untauglichkeit bei hoher Straferwartung**: Droht eine langjährige Freiheitsstrafe oder besteht eine ausgeprägte Fluchtgefahr im grenznahen Raum, genügt Electronic Monitoring nicht, da die Person die Grenze überschreiten kann, bevor die Einsatzkräfte eingreifen können (BGE 145 IV 503 E. 3.3.3).
* **Tauglichkeit bei Ausführungsgefahr**: Hingegen eignet sich Electronic Monitoring in Verbindung mit Rayonverboten hervorragend, um Annäherungen an Opfer im Rahmen häuslicher Konflikte frühzeitig zu erkennen und zu unterbinden ([BGE 140 IV 19](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-140-IV-19_2014.html#consideration_2.) E. 2.6).

### Bindung an die Anträge der Staatsanwaltschaft (Dispositionsmaxime) {#antragsbindung}

Im Haftprüfungsverfahren gilt eine strikte verfahrensrechtliche Schranke:
> «Das Zwangsmassnahmengericht kann von Gesetzes wegen keine Untersuchungshaft verfügen oder aufrechterhalten, wenn die Staatsanwaltschaft lediglich Ersatzmassnahmen beantragt hat.» ([BGE 142 IV 29](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-142-IV-29_2016.html#consideration_3.5) E. 3.5).

Beantragt die Staatsanwaltschaft ausschliesslich Ersatzmassnahmen, darf das Zwangsmassnahmengericht zwar andere oder schärfere Ersatzmassnahmen anordnen, jedoch unter keinen Umständen Haft verfügen. Will die Staatsanwaltschaft für den Fall der Untauglichkeit von Ersatzmassnahmen Haft sicherstellen, muss sie zwingend einen Eventualantrag auf Anordnung von Untersuchungshaft stellen (BGE 142 IV 29 E. 3.5).

### Befristung und periodische Verlängerung {#befristung-ersatzmassnahmen}

Ersatzmassnahmen dürfen nicht zeitlich unbeschränkt angeordnet werden. In analoger Anwendung von Art. 227 StPO müssen einschneidende Ersatzmassnahmen (insbesondere Hausarrest, Rayonverbote und Electronic Monitoring) befristet werden und unterliegen der regelmässigen richterlichen Kontrolle und Verlängerung ([BGE 141 IV 190](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-141-IV-190_2015.html#consideration_3.3) E. 3.3).

---

## Das gerichtliche Haftverfahren: Phasen und Fristen {#haftverfahren-phasen}

### Vorläufige Festnahme und Haftanordnung (Art. 224–226 StPO) {#anordnung-fristen}

Das Verfahren zur erstmaligen Anordnung von Untersuchungshaft unterliegt einem zweistufigen Fristenregime:
1. **Frist für die Staatsanwaltschaft**: Die Staatsanwaltschaft muss innert **48 Stunden** seit der Festnahme beim Zwangsmassnahmengericht schriftlich die Anordnung von Untersuchungshaft beantragen oder die Person freilassen ([Art. 224 Abs. 2 StPO](/kommentar/stpo/art-224/)).
2. **Frist für das Zwangsmassnahmengericht**: Das Zwangsmassnahmengericht hat unverzüglich, spätestens aber innert **48 Stunden** nach Eingang des Antrags zu entscheiden ([Art. 226 Abs. 1 StPO](/kommentar/stpo/art-226/)).

Das Bundesgericht stellte in [BGE 137 IV 92](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-137-IV-92_2011.html#consideration_3.2.1) die Tragweite dieser Fristen klar:
> «Daraus ergibt sich, dass die Aufrechterhaltung der Haft nicht schon dann gesetzwidrig wird, wenn die Staatsanwaltschaft den Haftantrag nicht innert 48 Stunden nach der Festnahme dem Haftrichter einreicht, sondern erst, wenn der Haftrichter den Haftentscheid dem Festgenommenen nicht innert 96 Stunden nach der Festnahme eröffnet hat.» (E. 3.2.1).

Die gesetzlichen Fristen von je 48 Stunden sind Maximalfristen. Eine Überschreitung der 48-Stunden-Frist durch die Staatsanwaltschaft führt zwar zur Feststellung der Rechtswidrigkeit im Dispositiv und zu Kostenfolgen zulasten des Staates, macht die Haft aber erst dann unrechtmässig und führt zur Freilassung, wenn die absolute Gesamtobergrenze von 96 Stunden bis zum richterlichen Entscheid überschritten wird (BGE 137 IV 92 E. 3.2.1–3.2.3).

### Haftverlängerung (Art. 227 StPO) {#haftverlaengerung}

Untersuchungshaft wird für höchstens drei Monate angeordnet; bei Verbrechen kann das ZMG die Haft jeweils um bis zu sechs Monate verlängern (Art. 227 Abs. 7 StPO).
* **Verlängerungsgesuch**: Will die Staatsanwaltschaft die Haft verlängern, muss sie das begründete Gesuch spätestens **vier Tage vor Ablauf der Haftdauer** beim ZMG einreichen (Art. 227 Abs. 2 StPO).
* **Geltung des Beschleunigungsgebots**: Mit zunehmender Haftdauer steigen die Anforderungen an die Begründungsdichte. Bei langer Verfahrensdauer prüft das Gericht eingehend, ob die Strafbehörden das Verfahren ohne ungerechtfertigte Verzögerungen vorantreiben (Art. 5 StPO).

### Haftentlassungsgesuch (Art. 228 StPO) {#haftentlassungsgesuch}

Die inhaftierte Person kann jederzeit schriftlich oder mündlich zu Protokoll ein Haftentlassungsgesuch stellen. Das Verfahren ist dreistufig aufgebaut:
1. Die Staatsanwaltschaft prüft das Gesuch. Will sie dem Gesuch nicht entsprechen, leitet sie es innert **drei Tagen** mit einer begründeten Stellungnahme an das ZMG weiter (Art. 228 Abs. 2 StPO).
2. Das ZMG stellt die Stellungnahme der inhaftierten Person zur Replik zu (Art. 228 Abs. 3 StPO).
3. Das ZMG entscheidet innert **fünf Tagen** nach Eingang der Stellungnahme oder Replik endgültig (Art. 228 Abs. 4 StPO).
* **Gesuchssperre (Abs. 5)**: Hat das ZMG ein Haftentlassungsgesuch abgewiesen, kann es für das Einreichen weiterer Gesuche eine Frist von bis zu einem Monat festsetzen, sofern die beschuldigte Person keine veränderten Umstände geltend macht.

### Sicherheitshaft und vorzeitiger Massnahmenvollzug (Art. 229–236 StPO) {#sicherheitshaft-massnahmenvollzug}

Mit Eingang der Anklageschrift beim erstinstanzlichen Sachgericht geht die Haftkompetenz vom Zwangsmassnahmengericht auf die **Verfahrensleitung des Sachgerichts** über (Art. 229 Abs. 1 StPO); aus Untersuchungshaft wird Sicherheitshaft.

* **Vorzeitiger Massnahmenvollzug (Art. 236 StPO)**: Die beschuldigte Person kann beantragen, freiheitsentziehende Massnahmen (Art. 59–61, 63 StGB) vorzeitig anzutreten.
* **Widerruf des vorzeitigen Vollzugs**: Der Widerruf eines vorzeitigen Massnahmenvollzugs und die damit verbundene Rückversetzung in strafprozessuale Sicherheitshaft greifen massiv in die Rechtsstellung der betroffenen Person ein. Ein solcher Widerruf bedarf einer formellen, ausreichend begründeten Verfügung unter vorgängiger Gewährung des rechtlichen Gehörs und Beizug der Verteidigung ([Art. 130 StPO](/kommentar/stpo/art-130/)).

---

## Verfahrensgarantien, Verteidigung und Haftbedingungen {#garantien-und-haftbedingungen}

### Notwendige Verteidigung (Art. 130 StPO) {#notwendige-verteidigung}

Strafprozessuale Haft löst zwingend das Institut der notwendigen Verteidigung aus:
* **10-Tage-Regel**: Dauert die Untersuchungshaft einschliesslich der vorläufigen Festnahme mehr als zehn Tage, liegt ein Fall notwendiger Verteidigung nach [Art. 130 lit. a StPO](/kommentar/stpo/art-130/#1-lit-a--untersuchungshaft--vorläufige-festnahme--10-tage) vor.
* **Drohende Sanktion**: Droht eine Freiheitsstrafe von mehr als einem Jahr oder eine freiheitsentziehende Massnahme, greift [Art. 130 lit. b StPO](/kommentar/stpo/art-130/#2-lit-b--drohende-freiheitsstrafe--1-jahr--freiheitsentziehende-massnahme--landesverweisung).
* Hat die beschuldigte Person nicht bereits eine Wahlverteidigung mandatiert, ordnet die Verfahrensleitung unverzüglich eine amtliche Verteidigung an (Art. 131 StPO). Die Mitwirkung der Verteidigung gilt auch für haftrechtliche Nebenentscheide und Anhörungen vor dem ZMG.

### Haftbedingungen und Menschenwürde (Art. 3 EMRK, Art. 10 Abs. 3 BV) {#haftbedingungen}

Die Bedingungen des Haftvollzugs müssen mit der Menschenwürde ([Art. 7 BV](/kommentar/bv/art-007/)) und dem Folterverbot ([Art. 10 Abs. 3 BV](/kommentar/bv/art-010/), [Art. 3 EMRK](/kommentar/emrk/art-003/)) im Einklang stehen.

* **Zellengrösse und Überbelegung**: In seiner Champ-Dollon-Rechtsprechung hielt das Bundesgericht fest, dass eine anhaltende Überbelegung (z.B. sechs Personen in einer für drei Personen ausgelegten 23 m²-Zelle bei 23 Stunden Zelleinschluss pro Tag) Art. 3 EMRK verletzt ([BGE 140 I 125](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_001_BGE-140-I-125_2014.html) E. 3.6.3). Als Richtwert für Einzelhaft gilt eine Nettofläche von mindestens 9 bis 10 m², bei Mehrfachbelegung mindestens 4 m² Bodenfläche pro Insasse (zuzüglich abgetrennter Sanitäranlagen).
* **Anspruch auf gerichtliche Feststellung**: Nicht jede Widrigkeit des Vollzugs rechtfertigt eine sofortige Haftentlassung; die inhaftierte Person hat jedoch einen verfassungsmässigen Anspruch auf rasche gerichtliche Prüfung und Feststellung der Rechtswidrigkeit unzulässiger Haftbedingungen ([BGE 139 IV 41](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-139-IV-41_2013.html#consideration_3.1) E. 3.1).
* **Wiedergutmachung**: Wurde rechtswidrige Haft oder ein Vollzug unter menschenrechtswidrigen Bedingungen festgestellt, erfolgt die Entschädigung in der Regel durch eine angemessene Reduktion der im Sachurteil ausgesprochenen Strafe oder durch finanzielle Genugtuung nach Art. 431 StPO ([BGE 142 IV 245](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-142-IV-245_2016.html) E. 4.3).
* **Sperrwirkung des Haftbeschwerdeverfahrens**: Rügen bezüglich der Vollzugsbedingungen müssen zeitnah im ordentlichen Haftbeschwerdeverfahren erhoben werden. Wurden sie dort rechtskräftig beurteilt, greift im nachgelagerten Sachurteil die materielle Rechtskraft (*res iudicata*); dieselben Rügen können im Sachurteil nicht erneut aufgerollt werden.

### Der Rechtsmittelweg {#rechtsmittelweg}

Gegen Entscheide des Zwangsmassnahmengerichts über die Anordnung, Verlängerung oder Aufhebung von Untersuchungshaft sowie über Ersatzmassnahmen steht die **Beschwerde** an die kantonale Beschwerdeinstanz offen ([Art. 393 Abs. 1 lit. c StPO](/kommentar/stpo/art-393/)):
* **Beschwerdefrist**: 10 Tage ab Eröffnung des Entscheids (Art. 396 Abs. 1 StPO).
* **Keine aufschiebende Wirkung**: Die Beschwerde hat keine aufschiebende Wirkung, es sei denn, die Verfahrensleitung der Beschwerdeinstanz ordnet diese ausnahmsweise an (Art. 387 StPO).
* **Weiterzug ans Bundesgericht**: Gegen den Entscheid der kantonalen Beschwerdeinstanz kann Beschwerde in Strafsachen an das Bundesgericht geführt werden (Art. 78 ff. BGG). Trotz Zwischenentscheidcharakter ist das Erfordernis des nicht wiedergutzumachenden Nachteils (Art. 93 Abs. 1 lit. a BGG) bei Freiheitsentzug regelmässig erfüllt.

---

## Praxishinweise {#praxishinweise}

* **Eventualanträge bei Ersatzmassnahmen stellen**: Beantragt die Staatsanwaltschaft beim ZMG Ersatzmassnahmen, ist das Gericht an diesen Antrag gebunden und darf keine Haft verfügen ([BGE 142 IV 29](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-142-IV-29_2016.html#consideration_3.5)). Die Staatsanwaltschaft muss daher stets mindestens im Eventualstandpunkt die Anordnung von Haft beantragen, falls das ZMG die Ersatzmassnahmen als ungenügend einstuft.
* **Fristenkontrolle im Vorverfahren (96-Stunden-Frist)**: Die Verteidigung hat den genauen Festnahmezeitpunkt minutengenau zu prüfen. Überschreitet die Staatsanwaltschaft ihre 48-Stunden-Frist, ist die Rüge im ZMG-Verfahren zwingend zu protokollieren, um Kostenfolgen und Genugtuungsansprüche zu wahren ([BGE 137 IV 92](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-137-IV-92_2011.html#consideration_3.2.1)). Wird der Haftentscheid nicht innert 96 Stunden nach Festnahme eröffnet, ist unverzüglich Haftentlassung zu verlangen.
* **Konkretisierung von Ersatzmassnahmen durch die Verteidigung**: Das pauschale Begehren um «Ersatzmassnahmen» bleibt vor Gerichten meist erfolglos. Die Verteidigung sollte bereits vor der Einvernahme vor dem ZMG ein ausformuliertes Konzept vorlegen (z.B. Bestätigung eines Mietverhältnisses, Nachweis einer Arbeitsstelle oder Therapiebereitschaft, Beibringung von Ausweispapieren, Kaution von Angehörigen, Zustimmung zu Rayonverboten mit Fussfessel).
* **Prüfung des neuen Vortatenerfordernisses (Art. 221 Abs. 1 lit. c StPO)**: Liegen keine zwei rechtskräftigen Vorstrafen wegen gleichartiger Taten vor, ist einfache Wiederholungsgefahr rechtlich ausgeschlossen ([BGer 7B_1035/2024](https://entscheidsuche.ch/docs/CH_BGer/CH_BGer_007_7B-1035-2024_2024-11-19.html)). Die Staatsanwaltschaft kann sich diesfalls nur auf die qualifizierte Wiederholungsgefahr (Abs. 1bis) berufen, was jedoch eine schwere Anlasstat gegen Leib, Leben oder sexuelle Integrität und Gutachtenbedürftigkeit voraussetzt.
* **Haftbedingungen unverzüglich rügen**: Missstände bei der Unterbringung (Zellengrösse, Lichteinfall, Spaziergang, medizinische Versorgung) müssen unverzüglich bei der Anstaltsleitung und dem Haftrichter gerügt werden. Wer die Rüge erst im Sachurteil anbringt, riskiert Rechtsverlust wegen Verwirkung und *res iudicata*.

---

## Leitentscheide {#leitentscheide}

| Entscheid | Gegenstand | Kernaussage |
|---|---|---|
| [BGE 137 IV 92](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-137-IV-92_2011.html#consideration_3.2.1) E. 3.2.1 | Fristen im Haftanordnungsverfahren (Art. 224, 226 StPO) | Staatsanwaltschaft (48h) und ZMG (48h) haben je Maximalfristen; gesetzwidrig wird die Haft erst bei Überschreitung der 96-Stunden-Gesamtfrist nach Festnahme. |
| [BGE 137 IV 122](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-137-IV-122_2011.html#consideration_4.2) E. 4.2 | Kollusionsgefahr (Art. 221 Abs. 1 lit. b StPO) | Haft wegen Kollusionsgefahr verlangt konkrete Anhaltspunkte für Verdunkelungshandlungen; nach Abschluss der Untersuchung besonders sorgfältige Prüfung geboten. |
| [BGE 140 IV 19](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-140-IV-19_2014.html#consideration_2.) E. 2.6 | Ersatzmassnahmen bei Ausführungsgefahr (Art. 237 StPO) | Rayon- und Kontaktverbote, allenfalls überwacht mittels Electronic Monitoring, sind bei häuslicher Gewalt ein wirksames Mittel zur Minderung von Ausführungsgefahr. |
| [BGE 140 IV 74](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-140-IV-74_2014.html#consideration_2.2) E. 2.2 | Verhältnismässigkeit von Ersatzmassnahmen | Haft ist *ultima ratio*; Ersatzmassnahmen müssen zur Gefahrenbannung ausreichen und ihrerseits den Grundsatz der Verhältnismässigkeit wahren. |
| [BGE 141 IV 190](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-141-IV-190_2015.html#consideration_3.3) E. 3.3 | Befristung von Ersatzmassnahmen (Art. 237 Abs. 4 StPO) | Einschneidende Ersatzmassnahmen (Hausarrest, Rayonverbote, Electronic Monitoring) müssen wie Untersuchungshaft befristet und periodisch verlängert werden. |
| [BGE 142 IV 29](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-142-IV-29_2016.html#consideration_3.5) E. 3.5 | Antragsbindung des ZMG (Dispositionsmaxime) | Beantragt die Staatsanwaltschaft lediglich Ersatzmassnahmen, darf das Zwangsmassnahmengericht von Gesetzes wegen keine Untersuchungshaft anordnen. |
| [BGE 143 IV 316](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-143-IV-316_2017.html#consideration_2.) E. 2 | Dringender Tatverdacht zu Beginn der Untersuchung | Zu Beginn des Vorverfahrens genügen hinreichende und konkrete Verdachtsmomente; Beweise müssen noch nicht liquiden Charakter haben. |
| [BGE 143 IV 330](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-143-IV-330_2017.html#consideration_2.1) E. 2.1 | Kognition beim dringenden Tatverdacht | Der Haftrichter nimmt keine erschöpfende Beweiswürdigung wie der Sachrichter vor; erforderlich ist erhebliche Wahrscheinlichkeit der Tatbestandserfüllung. |
| [BGE 145 IV 503](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-145-IV-503_2019.html#consideration_2.2) E. 2.2, 3.3.1 | Fluchtgefahr und Grenzen von Electronic Monitoring | Electronic Monitoring meldet Grenzübertritte nur nachträglich und ist bei hoher Straferwartung und akuter Fluchtgefahr ungeeignet. |
| [BGE 150 IV 149](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-150-IV-149_2024.html#consideration_3.2) E. 3.2 f. | Qualifizierte Wiederholungsgefahr (Art. 221 Abs. 1bis StPO) | Schliessung der Schutzlücke für Ersttäter bei schwersten Delikten; umgekehrte Proportionalität zwischen Schwere der Tat und Rückfallwahrscheinlichkeit. |
| [BGE 151 IV 57](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-151-IV-57_2025.html#consideration_3.1) E. 3.1 | Wegfall des Tatverdachts bei Verjährung | Wahrscheinliche Verjährung schliesst den dringenden Tatverdacht aus und führt zur sofortigen Haftentlassung. |
| [BGE 140 I 125](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_001_BGE-140-I-125_2014.html) E. 3.6.3 | Haftbedingungen und Überbelegung (Champ-Dollon) | Schwere und dauerhafte Zellenüberbelegung verletzt Art. 3 EMRK und Art. 10 Abs. 3 BV; Anspruch auf Feststellung der Rechtswidrigkeit. |
| [BGE 139 IV 41](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-139-IV-41_2013.html#consideration_3.1) E. 3.1 | Feststellungsanspruch bei rechtswidrigen Haftbedingungen | Rechtswidrige Haftbedingungen führen nicht zwingend zur Freilassung, begründen aber einen Anspruch auf gerichtliche Feststellung. |
| [BGE 142 IV 245](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-142-IV-245_2016.html) E. 4.3 | Kompensation unzulässiger Haftbedingungen | Rechtswidrige Haftbedingungen können wahlweise durch Strafreduktion im Sachurteil oder finanzielle Entschädigung kompensiert werden. |
| [BGer 7B_1035/2024 vom 19.11.2024](https://entscheidsuche.ch/docs/CH_BGer/CH_BGer_007_7B-1035-2024_2024-11-19.html) | Neue Praxis zu Art. 221 Abs. 1 lit. c StPO | Gesetzgeberische Invalidierung der Altpraxis: Einfache Wiederholungsgefahr verlangt zwingend mindestens zwei rechtskräftige Vorstrafen. |

---

## Literatur {#literatur}

- Forster Marc, in: Niggli/Heer/Wiprächtiger (Hrsg.), Basler Kommentar zur Schweizerischen Strafprozessordnung, 3. Aufl., Basel 2023, Vor Art. 212–240, Art. 221, Art. 226 und Art. 237 StPO.
- Goldschmid Peter / Maurer Thomas / Sollberger Jürg / Vogt Daniela, Textausgabe zur Schweizerischen Strafprozessordnung mit Erläuterungen, 3. Aufl., Bern 2023.
- Hug Daniel / Scheidegger Beat, in: Donatsch/Lieber/Summers/Wohlers (Hrsg.), Kommentar zur Schweizerischen Strafprozessordnung, 3. Aufl., Zürich 2020, Art. 221, Art. 224–228 und Art. 237 StPO.
- Schmid Niklaus / Jositsch Daniel, Schweizerische Strafprozessordnung: Praxiskommentar, 4. Aufl., Zürich 2023, Art. 221–237 StPO.
