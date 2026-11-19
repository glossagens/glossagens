---
title: "Baubewilligung von Mobilfunkantennen: Strahlenschutz, Kaskadenordnung, 5G und Nachbarrechtsschutz"
date: 2026-11-19
lastmod: 2026-11-19
description: "Systematische Darstellung der Rechtsgrundlagen und Leitpraxis zur Baubewilligung von Mobilfunkanlagen: Kompetenzaufteilung zwischen Bund und Kantonen, abschliessender Immissionsschutz nach USG und NISV, planerische Kaskadenmodelle der Gemeinden, Bewilligungspflicht adaptiver Antennen (5G) sowie Einspracheberechtigung der Nachbarschaft."
tags: ["Mobilfunk", "Mobilfunkantennen", "NISV", "USG", "Baubewilligung", "5G", "Adaptive Antennen", "Kaskadenmodell", "Ortsbildschutz", "Beschwerdelegitimation", "Raumplanung"]
typ: grundlage
kurz: "Der Bau und Betrieb von Mobilfunkanlagen untersteht einem dualen Regime: Während der Bund den Schutz vor nichtionisierender Strahlung im Umweltschutzgesetz und der NISV abschliessend regelt und Kantonen wie Gemeinden verschärfende Grenzwerte untersagt, obliegt die ortsbauliche Steuerung den Gemeinden. Diese dürfen Mobilfunkantennen über städtebauliche Kaskadenordnungen lenken, sofern der fernmelderechtliche Versorgungsauftrag nicht vereitelt wird. Bei modernen 5G-Anlagen mit adaptiven Antennen bedingt die Umstellung auf Korrekturfaktoren mit kurzzeitigen Leistungsspitzen zwingend ein ordentliches Baubewilligungsverfahren, wobei Nachbarn im 10%-Berechnungsradius zur Einsprache legitimiert sind."
sachgebiete: [raumplanung.mobilfunk, raumplanung.baubewilligung, umwelt]
normen:
  - { gesetz: usg, art: art-011 }
  - { gesetz: usg, art: art-012 }
  - { gesetz: usg, art: art-013 }
  - { gesetz: rpg, art: art-022 }
  - { gesetz: rpg, art: art-024 }
  - { gesetz: bgg, art: art-089 }
stichworte: ["Mobilfunk", "Mobilfunkantenne", "Mobilfunkanlage", "NISV", "Elektrosmog", "nichtionisierende Strahlung", "Anlagegrenzwert", "Immissionsgrenzwert", "OMEN", "adaptive Antennen", "Korrekturfaktor", "Beamforming", "5G", "Kaskadenmodell", "Standortdatenblatt", "Qualitätssicherungssystem", "Worst-Case-Szenario", "Bagatelländerung"]
revisions:
  - date: 2026-11-19
    by: "Antigravity"
    model: "gemini-3.8-flash"
    note: "Erstfassung (Typ grundlage). Belege über entscheidsuche.ch als Volltext geladen und verifiziert (u. a. BGE 126 II 399, BGE 128 II 168, BGE 128 II 340, BGE 128 II 378, BGE 133 II 64, BGE 133 II 321, BGE 138 II 173, BGE 138 II 570, BGE 141 II 245, BGE 150 II 379, BGE 151 II 593). Zitate, Erwägungsnummern und Anker mit pruefen.py mechanisch abgeglichen. Stand der Gesetzgebung anhand der Bundesratsvernehmlassung zur FMG-Revision vom 12.12.2025 und Curia Vista nachgewiesen. Literaturangaben exakt nach den Zitaten in den BGE."
---

## Überblick {#ueberblick}

Kaum ein baurechtlicher Gegenstand führt in der schweizerischen Rechtsprechung zu einer so anhaltenden Fülle von Einsprachen, Verwaltungsgerichtsverfahren und bundesgerichtlichen Leitentscheiden wie die Bewilligung von Mobilfunkantennen. Ob Neuerrichtung eines Antennenmastes oder technische Umrüstung auf die Mobilfunkgenerationen 4G und 5G: Fast jedes Baugesuch stösst auf vehementen Widerstand der Anwohnerschaft und veranlasst Gemeinden regelmässig zum Erlass von Planungszonen, Moratorien oder restriktiven Baureglementen.

Die juristische Ursache dieser Dauerstreitigkeit liegt in der komplexen Überlagerung mehrerer Rechtsgebiete und Zuständigkeitsebenen:

1. **Fernmelderechtlicher Versorgungsauftrag**: Der Bund gewährleistet eine zuverlässige, erschwingliche und qualitativ hochstehende fernmeldetechnische Grundversorgung für alle Bevölkerungskreise (Art. 92 BV, Art. 1 FMG). Die konzessionierten Betreiberinnen sind verpflichtet, ihre Funknetze flächendeckend und nach dem Stand der Technik auszubauen.
2. **Abschliessender bundesrechtlicher Immissionsschutz**: Der Schutz der Bevölkerung vor nichtionisierender Strahlung (NIS, umgangssprachlich «Elektrosmog») ist im Umweltschutzgesetz (USG) und der Verordnung über den Schutz vor nichtionisierender Strahlung (NISV) auf Bundesebene geregelt. Diese Ordnung ist abschliessend: Kantone und Gemeinden besitzen keinerlei Kompetenz, strengere Grenzwerte festzulegen oder Bauvorhaben aus Gründen des Gesundheitsschutzes zu verweigern.
3. **Kantonale und kommunale Bau- und Planungshoheit**: Die Kantone und autonomen Gemeinden bestimmen die Bodennutzung, das Zonenrecht, das Baubewilligungsverfahren sowie den Ortsbild- und Denkmalschutz (Art. 75 BV, RPG). Sie versuchen häufig, Antennen aus Wohngebieten fernzuhalten.
4. **Technologischer Wandel (5G und adaptive Antennen)**: Die Einführung adaptiver Antennen (Beamforming), die ihre Sendeleistung bedarfsgerecht bündeln, warf die Frage auf, wie deren Strahlung rechnerisch zu erfassen ist (Korrekturfaktor, Mittelung über 6 Minuten) und ob die Umstellung bestehender Anlagen ohne ordentliches Baubewilligungsverfahren zulässig ist.

Das Baubewilligungsverfahren wird von Einsprechenden oft als Ventil genutzt, um fundamentale gesundheitspolitische Bedenken gegen elektromagnetische Strahlung vorzubringen. Materiell beschränkt sich die gerichtliche Kognition jedoch strikt auf die Einhaltung der bundesrechtlich vorgegebenen NISV-Grenzwerte und der raumplanerischen Einordnungskriterien.

---

## Rechtsgrundlagen und Kompetenzverteilung {#rechtsgrundlagen}

### Bundeskompetenz für Strahlenschutz und Fernmeldewesen {#bundeskompetenz}

Die verfassungsrechtliche Kompetenzordnung trennt scharf zwischen dem Schutz vor Umwelteinwirkungen einerseits und der Raumordnung andererseits. Gestützt auf Art. 74 BV erlässt der Bund Vorschriften über den Schutz des Menschen und seiner natürlichen Umwelt vor schädlichen oder lästigen Einwirkungen.

Im Bundesgesetz über den Umweltschutz (USG) hat der Gesetzgeber das zweistufige Vorsorgeprinzip verankert:

{{< wortlaut gesetz="usg" art="art-011" >}}

Ergänzend ermächtigt Art. 12 Abs. 1 lit. a und Abs. 2 USG sowie Art. 13 USG den Bundesrat, Emissions- und Immissionsgrenzwerte durch Verordnung festzulegen. Für die nichtionisierende Strahlung ortsfester Anlagen hat der Bundesrat die Verordnung über den Schutz vor nichtionisierender Strahlung (NISV; SR 814.710) erlassen.

Im Fernmeldewesen obliegt dem Bund gemäss Art. 92 BV die Gesetzgebung zur Gewährleistung ausreichender und preiswerter Fernmeldedienste. Das Fernmeldegesetz (FMG; SR 784.10) bezweckt einen wirksamen Wettbewerb und eine zuverlässige Infrastruktur (Art. 1 FMG), wobei den Betreiberinnen ein Recht auf Zugang zu Grundstücken im Gemeingebrauch und zur Durchleitung eingeräumt wird (Art. 35 ff. FMG).

### Kantonale und kommunale Bauhoheit und Raumplanung {#kantonale-bauhoheit}

Die Kantone und Gemeinden sind für das Raumplanungs- und Baurecht zuständig (Art. 75 BV). Nach Bundesraumplanungsrecht bedürfen Bauten und Anlagen einer behördlichen Bewilligung:

{{< wortlaut gesetz="rpg" art="art-022" >}}

In [Art. 22 Abs. 2 lit. a RPG](/kommentar/rpg/art-022/#c-zonenkonformität-abs-2-lit-a) wird verlangt, dass Bauten dem Zweck der Nutzungszone entsprechen. Ausserhalb der Bauzonen ist eine Errichtung nur über die Ausnahmebewilligung gemäss [Art. 24 RPG](/kommentar/rpg/art-024/#c-relative-standortgebundenheit-und-alternativenprüfung-abs-1-lit-a) zulässig, die eine Standortgebundenheit und das Fehlen überwiegender Gegeninteressen voraussetzt.

---

## Das zweistufige Schutzkonzept der NISV {#zweistufiges-schutzkonzept}

### Immissionsgrenzwerte und vorsorgliche Anlagegrenzwerte {#grenzwerte}

Das Bundesgericht hat bereits im Grundsatzurteil [BGE 126 II 399](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_004_BGE-126-II-399_2000-08-30.html#consideration_3.) E. 3 festgehalten, dass das Schutzkonzept der NISV zwei Stufen unterscheidet:

«Immissionsgrenzwerte zum Schutz vor den wissenschaftlich nachgewiesenen thermischen Wirkungen und Anlagegrenzwerte zur vorsorglichen Emissionsbegrenzung»

1. **Immissionsgrenzwerte (IGW)** (Art. 13 USG, Art. 13 NISV i.V.m. Anhang 2 NISV):
   Die IGW basieren auf den Empfehlungen der Internationalen Kommission zum Schutz vor nichtionisierender Strahlung (ICNIRP) und der Weltgesundheitsorganisation (WHO). Sie bezwecken den Schutz vor den wissenschaftlich zweifelsfrei nachgewiesenen *thermischen* Gewebeerwärmungen. Die IGW gelten an allen Orten, an denen sich Menschen aufhalten können (z. B. 41 bis 61 V/m je nach Frequenzbereich), und dürfen zu keinem Zeitpunkt überschritten werden.
2. **Anlagegrenzwerte (AGW)** (Art. 11 Abs. 2 USG, Art. 4 NISV i.V.m. Anhang 1 Ziff. 64 NISV):
   Weil nach dem Vorsorgeprinzip des USG Einwirkungen, die schädlich oder lästig werden könnten, frühzeitig zu begrenzen sind, legte der Bundesrat vorsorgliche Anlagegrenzwerte fest. Diese dienen dem präventiven Schutz vor möglichen *nicht-thermischen* biologischen Langzeitwirkungen, für welche zwar Verdachtsmomente, aber keine abschliessenden wissenschaftlichen Beweise vorliegen.
   Die AGW sind rund zehnmal strenger als die IGW (z. B. 4.0 V/m für Frequenzen um 900 MHz; 5.0 V/m für 1800 MHz; 6.0 V/m für Frequenzen ab 2 GHz). Sie gelten nicht flächendeckend, sondern ausschliesslich an definierten sensiblen Aufenthaltsorten.

### Orte mit empfindlicher Nutzung (OMEN) und Nutzungsreserven {#omen-nutzungsreserven}

Die strengen Anlagegrenzwerte müssen gemäss Art. 3 Abs. 3 NISV an sogenannten **Orten mit empfindlicher Nutzung (OMEN)** eingehalten werden. Als OMEN gelten:
- Räume in Gebäuden, in denen sich Personen regelmässig während längerer Zeit aufhalten (Wohn- und Schlafräume, Schulzimmer, Spitäler, ständige Arbeitsplätze);
- öffentliche oder private, für Kinder bestimmte Spielplätze;
- noch nicht überbaute Bauparzellen, soweit dort zonenkonform Räume der vorgenannten Art errichtet werden dürfen.

Nicht als OMEN qualifizieren nach der bundesgerichtlichen Rechtsprechung Balkone, Dachterrassen, Treppenhäuser, Waschküchen oder Garagen ([BGE 128 II 378](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_004_BGE-128-II-378_2002.html) E. 6). Dort gilt allein der höhere Immissionsgrenzwert (IGW).

Befindet sich eine Mobilfunkanlage in der Nachbarschaft einer Liegenschaft mit noch ungenutzten baulichen Nutzungsreserven (z. B. Baulücke oder Aufstockungspotenzial), ist im Zeitpunkt der Baubewilligung nach dem Verhältnismässigkeitsprinzip auf die bestehende Nutzung abzustellen. Der Betreiber muss sich jedoch verpflichten, die Anlage anzupassen oder die Leistung zu reduzieren, sobald die Nutzungsreserve realisiert wird ([BGE 128 II 340](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_004_BGE-128-II-340_2002.html) E. 2–5).

### Abschliessender Charakter des Bundesrechts {#abschliessender-charakter}

Ein zentraler Pfeiler der Antennenrechtsprechung ist das Verbot kantonaler und kommunaler Sondernormen zum Strahlenschutz. In [BGE 133 II 64](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_004_BGE-133-II-64_2007.html#consideration_5.2) E. 5.2 stellte das Bundesgericht klar:

«Diese Regelung ist abschliessend, und zwar nicht nur hinsichtlich des Schutzes vor schädlicher und lästiger Strahlung, sondern auch im Bereich des vorsorglichen Immissionsschutzes»

Daraus folgt:
- Weder Kantone noch Gemeinden dürfen strengere Grenzwerte als die NISV erlassen.
- Moratorien gegen den Antennenbau oder 5G gestützt auf gesundheitliche Befürchtungen sind bundesrechtswidrig und nichtig.
- Bestimmungen in kommunalen Bau- und Zonenreglementen, die Mindestabstände von Mobilfunkantennen zu Wohnbauten, Schulen oder Kindergärten vorschreiben, sind unzulässig, wenn sie mit Strahlenschutz oder Gesundheitsvorsorge begründet werden.

---

## Herkunft und Entwicklung der bundesgerichtlichen Rechtsprechung {#entwicklung-der-rechtsprechung}

### Erste Phase: Inkrafttreten der NISV und Berechnungsradien (2000–2006) {#phase-eins-nisv}

Nach dem Inkrafttreten der NISV am 1. Februar 2000 überprüfte das Bundesgericht in [BGE 126 II 399](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_004_BGE-126-II-399_2000-08-30.html#consideration_3.) die Verfassungsmässigkeit der Verordnung und schützte das zweistufige Konzept.

In verfahrensrechtlicher Hinsicht schuf das Bundesgericht mit [BGE 128 II 168](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_004_BGE-128-II-168_2002.html#consideration_2.3) E. 2.3 eine pragmatische Formel für die Parteistellung von Nachbarn:

«Einspracheberechtigt sind alle Personen, die innerhalb eines Radius wohnen, ausserhalb dessen in jedem Fall eine tiefere Strahlung als 10% des Anlagegrenzwertes erzeugt wird»

Damit wurde verhindert, dass Nachbarn bereits im Vorfeld der Einsprache aufwendige Strahlungsgutachten vorlegen müssen, um ihre Beschwerdelegitimation zu beweisen.

### Zweite Phase: Zonenkonformität, Kaskadenmodelle und Ästhetik (2007–2018) {#phase-zwei-kaskaden}

In einer zweiten Phase verlagerte sich der Schwerpunkt der Streitigkeiten auf das Raumplanungsrecht. Gemeinden suchten nach Wegen, Antennen aus Wohnquartieren fernzuhalten, ohne sich auf den unzulässigen Strahlenschutz zu berufen:

- **Grundsätzliche Zonenkonformität**: In [BGE 133 II 321](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_004_BGE-133-II-321_2007.html#consideration_4.3.4) E. 4.3 bestätigte das Gericht: «Auf die Festsetzung von Standorten für Mobilfunkantennen kann mit raumplanerischen Massnahmen eingewirkt werden, sofern die Schranken beachtet werden, die sich aus dem Telekommunikations- und dem Umweltschutzrecht des Bundes ergeben». In Bauzonen sind Mobilfunkantennen als Infrastrukturanlagen grundsätzlich zonenkonform ([Art. 22 RPG](/kommentar/rpg/art-022/#c-zonenkonformität-abs-2-lit-a)), selbst wenn sie gebietsübergreifend auch angrenzende Nichtbauzonen versorgen ([BGE 141 II 245](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_004_BGE-141-II-245_2015.html) E. 2).
- **Zulässigkeit von Kaskadenmodellen**: In [BGE 138 II 173](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_004_BGE-138-II-173_2012.html) beurteilte das Bundesgericht das Baureglement der Gemeinde Urtenen-Schönbühl. Es hielt fest, dass Gemeinden die Errichtung von Antennen über ein Kaskadenmodell steuern dürfen (Priorität für Arbeits- und Gewerbezonen; Wohnzonen nur subsidiär bei nachgewiesenem Versorgungsbedarf für das Quartier). Tragend war: «Das angefochtene Reglement sieht ein Kaskadenmodell vor, das grundsätzlich mit der Bundesfernmeldegesetzgebung vereinbar ist» ([BGE 138 II 173](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_004_BGE-138-II-173_2012.html#consideration_6.5) E. 6.5) und «Die Zonenkonformität von Mobilfunksendeanlagen in Wohnzonen kann davon abhängig gemacht werden, dass die Anlagen der Versorgung der Nachbarschaft dienen» ([BGE 138 II 173](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_004_BGE-138-II-173_2012.html#consideration_5.2) E. 5.2).
- **Schranken kommunaler Ästhetikvorschriften**: In [BGE 141 II 245](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_004_BGE-141-II-245_2015.html#consideration_7.1) E. 7.1 schützte das Gericht den Versorgungsauftrag vor übermässigem Ortsbildschutz: «Die Erfüllung des Versorgungsauftrags der Mobilfunkbetreiber gemäss dem Fernmelderecht des Bundes darf durch die Anwendung kommunaler Ästhetikvorschriften nicht vereitelt oder über Gebühr erschwert werden».

### Dritte Phase: Technologiewechsel 5G, adaptive Antennen und Korrekturfaktor (ab 2019) {#phase-drei-5g-und-adaptive-antennen}

Mit der Einführung von 5G rüsteten die Mobilfunkbetreiberinnen ihre Netze mit **adaptiven Antennen** (Massive MIMO) aus. Im Unterschied zu konventionellen Antennen, die ein starres, konstantes Abstrahldiagramm aufweisen, verändern adaptive Antennen ihre Strahlungsrichtung in Bruchteilen von Sekunden und richten Signale gezielt auf das verbundene Endgerät aus («Beamforming», [BGE 150 II 379](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_004_BGE-150-II-379_2024.html#consideration_2.1) E. 2.1).

Weil eine dauerhafte Ausstrahlung der theoretischen Maximalleistung in alle Richtungen physikalisch nicht der Realität entspricht, führte das Bundesamt für Umwelt (BAFU) im Februar 2021 einen **Korrekturfaktor** (Ziff. 63 Anhang 1 NISV) ein. Dies entfachte einen schweizweiten Rechtsstreit darüber, ob bestehende Antennen im formlosen Bagatellverfahren umgerüstet werden dürfen und ob der Korrekturfaktor mit dem Vorsorgeprinzip vereinbar ist.

In zwei Meilenstein-Urteilen hat das Bundesgericht diese Streitfragen entschieden:
- **BGE 150 II 379** (2024): Die Anwendung des Korrekturfaktors erfordert **zwingend ein ordentliches Baubewilligungsverfahren**.
- **BGE 151 II 593** (2025): Der Korrekturfaktor und die Mittelung über 6 Minuten sind **materiell gesetzmässig** und verletzen das umweltrechtliche Vorsorgeprinzip nicht.

---

## Kernstreitpunkte im Baubewilligungsverfahren {#kernstreitpunkte}

### Baubewilligungspflicht versus Bagatellverfahren bei adaptiven Antennen {#baubewilligungspflicht-adaptive-antennen}

Die Baubewilligungspflicht richtet sich nach [Art. 22 Abs. 1 RPG](/kommentar/rpg/art-022/#b-errichten-oder-ändern-abs-1). Massgebend ist, ob mit einer Massnahme nach dem gewöhnlichen Lauf der Dinge so wichtige räumliche oder umweltbezogene Folgen verbunden sind, dass ein Interesse der Öffentlichkeit oder der Nachbarschaft an einer vorgängigen Kontrolle besteht.

In [BGE 150 II 379](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_004_BGE-150-II-379_2024.html#consideration_4.2) E. 4.2 hielt das Bundesgericht zur Umstellung auf den Korrekturfaktor fest:

«Die Anwendung des Korrekturfaktors auf bisher nach dem "Worst-Case-Szenario" bewilligte adaptive Antennen führt zu Leistungsspitzen, die deutlich […] über der bisherigen maximalen Sendeleistung liegen können»

Die Urteilsbegründung stützt sich auf folgende Erwägungen:
1. **Kurzzeitige Leistungsspitzen**: Zwar ist die mittlere Strahlenbelastung bei adaptiven Antennen tendenziell geringer; durch den Korrekturfaktor darf die Sendeleistung kurzzeitig jedoch um ein Vielfaches über der bewilligten Dauerleistung liegen, sofern der 6-Minuten-Mittelwert eingehalten wird.
2. **Rechtsschutz und Gehör**: Die Anwohnerinnen und Anwohner haben Anspruch darauf, im Rahmen eines ordentlichen Auflage- und Einspracheverfahrens prüfen zu lassen, ob das Standortdatenblatt korrekt berechnet wurde und die Schutzabstände gewahrt sind ([BGE 150 II 379](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_004_BGE-150-II-379_2024.html#consideration_4.3) E. 4.3).
3. **Keine Bagatelländerung**: Die Umstellung kann folglich nicht im internen Melde- oder Bagatellverfahren bewilligt werden, wenn zuvor nur eine Genehmigung nach dem starren «Worst-Case-Szenario» vorlag.

### Gesetzmässigkeit des Korrekturfaktors und 6-Minuten-Mittelung {#gesetzmaessigkeit-korrekturfaktor}

In [BGE 151 II 593](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_004_BGE-151-II-593_2025.html) bestätigte das Bundesgericht die materielle Rechtmässigkeit von Ziff. 63 Anhang 1 NISV:
- **Vereinbarkeit mit dem Vorsorgeprinzip** (Art. 11 Abs. 2 USG): Der Korrekturfaktor bildet die tatsächliche Sendecharakteristik realistisch ab. Statistische Untersuchungen belegen, dass die Immissionen an OMEN auch unter Berücksichtigung des Korrekturfaktors im Mittel weit unter den vorsorglichen Anlagegrenzwerten bleiben.
- **Zulässigkeit der zeitlichen Mittelung**: Das Bundesgericht stellte klar, dass:

«auch die Immissionsgrenzwerte in den für den Mobilfunk massgebenden Frequenzen nicht in jedem Moment, sondern über 6 Minuten ausgemittelt eingehalten werden müssen» ([BGE 151 II 593](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_004_BGE-151-II-593_2025.html#consideration_6.3.2) E. 6.3.2).

Eine zeitliche Mittelung ist dem Umweltrecht nicht fremd (vgl. auch Lärmschutzrecht) und führt bei nicht-thermischen Wirkungen zu keiner Absenkung des Schutzniveaus.

### Das Qualitätssicherungssystem (QS-System) als Kontrollinstrument {#qualitaetssicherungssystem}

Weil die Einhaltung der maximal bewilligten Strahlungsleistung im Betrieb nicht permanent durch behördliche Vor-Ort-Messungen überprüft werden kann, stützt sich der Vollzug auf das **Qualitätssicherungssystem (QS-System)** der Betreiberinnen.

Das QS-System ist eine zentrale, computergestützte Datenbank, die kontinuierlich die Betriebsdaten (Sendeleistung, Auslastung, Absenkungswinkel) aller Sendeantennen erfasst. Stellt das System eine Abweichung von den bewilligten Parametern fest, erfolgt eine automatische Leistungsdrosselung oder Alarmierung der kantonalen NIS-Fachstelle.

In [BGE 151 II 593](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_004_BGE-151-II-593_2025.html#consideration_7.2) E. 7.2 bestätigte das Bundesgericht die Tauglichkeit des QS-Systems auch für adaptive Antennen mit Korrekturfaktor. Da das Bundesamt für Kommunikation (BAKOM) die Softwareerweiterungen zertifiziert und regelmässig auditiert, besteht eine hinreichende Gewähr für den gesetzeskonformen Betrieb. Eine lückenlose Echtzeitüberwachung durch die Behörden ist nicht erforderlich.

### Raumplanerische Steuerung: Kaskadenordnung und Trennungsgrundsatz {#raumplanerische-steuerung}

Gemeinden, die den Bau von Mobilfunkanlagen steuern wollen, dürfen dies über städtebauliche Instrumente tun:

| Instrument | Zulässigkeit | Voraussetzungen / Grenzen |
|---|---|---|
| **Kaskadenmodell** | **Zulässig** ([BGE 138 II 173](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_004_BGE-138-II-173_2012.html)) | Begründung ausschliesslich über Ortsbildschutz, Schutz von Wohnzonen vor optischer Beeinträchtigung (ideelle Immissionen); **kein** faktisches Verbot; Ausweichen in Wohnzone muss möglich sein, wenn Arbeitszonen ungeeignet sind. |
| **Generelles Antennenverbot in Wohnzonen** | **Unzulässig** ([BGE 133 II 64](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_004_BGE-133-II-64_2007.html)) | Verletzt Bundesrecht, da es die Erfüllung des fernmelderechtlichen Versorgungsauftrags (Art. 92 BV, FMG) vereitelt. |
| **Mindestabstand zu Schulen / Wohnbauten** | **Unzulässig** (st. Rspr.) | Gilt als verdeckter, unzulässiger Strahlenschutz und greift in die abschliessende NISV-Kompetenz des Bundes ein. |
| **Ästhetikklausel / Einordnung** | **Bedingt zulässig** ([BGE 141 II 245](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_004_BGE-141-II-245_2015.html)) | Allgemeine Schutzvorschriften für Ortsbilder dürfen angewandt werden; Verweigerung nur zulässig, wenn taugliche Alternativstandorte vorliegen. |

### Mobilfunkantennen ausserhalb der Bauzonen (Art. 24 RPG) {#antennen-ausserhalb-bauzone}

Befindet sich ein geplanter Antennenstandort ausserhalb der Bauzone (z. B. in der Landwirtschaftszone), richtet sich die Zulässigkeit nach [Art. 24 RPG](/kommentar/rpg/art-024/#c-relative-standortgebundenheit-und-alternativenprüfung-abs-1-lit-a):
1. **Positive Standortgebundenheit** ([Art. 24 lit. a RPG](/kommentar/rpg/art-024/#b-erste-kumulative-voraussetzung-positive-und-absolute-standortgebundenheit-abs-1-lit-a)):
   Die Antenne muss aus funktechnischen Gründen auf einen Standort ausserhalb der Bauzone angewiesen sein. Dies wird bejaht, wenn die Antenne primär der Abdeckung von Verkehrswegen (Autobahnen, Bahnlinien) oder von Landwirtschaftsgebieten dient ([BGE 138 II 570](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_004_BGE-138-II-570_2012.html) E. 4.2).
2. **Relative Standortgebundenheit und Alternativenprüfung**:
   Soll eine Antenne in der Nichtbauzone errichtet werden, um eine Versorgungslücke in einer Bauzone zu schliessen (sog. negative Standortgebundenheit), verlangt das Bundesgericht den strikten Nachweis, dass innerhalb der Bauzone kein zweckmässiger Standort realisierbar ist ([BGE 141 II 245](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_004_BGE-141-II-245_2015.html) E. 7.8; [BGE 133 II 321](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_004_BGE-133-II-321_2007.html) E. 4.3.3).
3. **Keine überwiegenden Interessen** (Art. 24 lit. b RPG):
   Dem Vorhaben dürfen keine überwiegenden Interessen des Landschafts-, Natur- oder Denkmalschutzes entgegenstehen.

---

## Rechtsschutz und Einsprachebefugnis der Nachbarschaft {#rechtsschutz-und-einsprachebefugnis}

### Das 10%-Radiusmodell zur Beschwerdelegitimation {#radiusmodell-legitimation}

Im Baubewilligungsverfahren richtet sich die Einsprache- und Beschwerdebefugnis der Nachbarschaft nach kantonalem Recht sowie für das Verfahren vor Bundesgericht nach Art. 89 Abs. 1 BGG. Die Rechtsprechung knüpft an die räumliche Nähe zur Sendeanlage an.

Massgeblich ist das in [BGE 128 II 168](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_004_BGE-128-II-168_2002.html#consideration_2.3) E. 2.3 definierte **10%-Radiusmodell**:
- Ausgehend von der Sendeleistung der Antenne und dem massgebenden Anlagegrenzwert wird ein kreisförmiger Radius um den Antennenstandort gezogen, an dessen äusserer Grenze die rechnerische Strahlung noch genau 10% des AGW betragen kann.
- Jede Person, die innerhalb dieses Perimeters wohnt, Grundeigentum besitzt oder eine ständige Arbeitsstätte hat, ist ohne Weiteres zur Einsprache und Beschwerde legitimiert.
- Die Legitimation besteht selbst dann, wenn das konkrete Gebäude durch Dämpfungseffekte (z. B. Nachbargebäude oder Abschattung) tatsächlich einer geringeren Strahlung als 10% ausgesetzt ist.

Personen, die ausserhalb dieses 10%-Perimeters wohnen, sind praxisgemäss nicht zur Beschwerde zugelassen, es sei denn, sie könnten eine besondere, atypische Betroffenheit nachweisen.

### Rügeprinzip und Ausschluss abstrakter Gesundheitsbedenken {#ruegeprinzip-gesundheitsbedenken}

In der Praxis bringen Einsprechende häufig vor, dass die Grenzwerte der NISV unzureichend seien, *Elektrosensibilität* bestehe oder Langzeitrisiken drohten. Solche Rügen sind vor den Baubehörden und Gerichten von vornherein wirkungslos:

1. **Bindung an Bundesverordnungen**: Gerichte sind an die Bundesgesetze gebunden (Art. 190 BV). Die NISV stützt sich auf eine formellgesetzliche Delegation im USG. Da das Bundesgericht die Verfassungsmässigkeit der Grenzwerte mehrfach geprüft und bestätigt hat ([BGE 126 II 399](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_004_BGE-126-II-399_2000-08-30.html#consideration_3.), [BGE 151 II 593](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_004_BGE-151-II-593_2025.html)), können kantonale Instanzen die Grenzwerte nicht im Einzelfall infrage stellen.
2. **Zulässige Rügen**: Einwände im Baubewilligungsverfahren haben nur Aussicht auf Erfolg, wenn sie konkrete Rechtsverletzungen dartun:
   - Rechenfehler oder unvollständige Angaben im Standortdatenblatt (falscher Antennengewinn, unberücksichtigte OMEN);
   - Überschreitung des AGW an einem konkreten OMEN;
   - Verletzung einer rechtsgültigen kommunalen Kaskadenordnung oder mangelhafte Alternativenprüfung;
   - schwerwiegende Verletzung von Ortsbild- und Denkmalschutzvorschriften;
   - Durchführung eines Meldeverfahrens statt eines zwingenden ordentlichen Baubewilligungsverfahrens ([BGE 150 II 379](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_004_BGE-150-II-379_2024.html)).

---

## Stand der Gesetzgebung {#stand-der-gesetzgebung}

Auf Bundesebene ist die Beschleunigung der Antennenbewilligungsverfahren Gegenstand intensiver legislativer Arbeiten:

- **Bundesratsvorlage zur FMG-Teilrevision (Vernehmlassung vom 12. Dezember 2025)**:
  Um den schleppenden Netzausbau zu überwinden und Verfahrensabläufe zu straffen, hat der Bundesrat am 12. Dezember 2025 eine grundlegende Reform in die Vernehmlassung geschickt. Kern der Vorlage ist die **Entkoppelung des Immissionsschutzes vom klassischen Baubewilligungsverfahren**. Die Überprüfung der NISV-Grenzwerte soll künftig primär in einem standardisierten bundesrechtlichen Meldeverfahren durch die Fachstellen erfolgen. Baubewilligungspflichtig blieben im Wesentlichen nur noch die rein baulichen und raumplanerischen Aspekte (Statik, Ortsbild, Zonenkonformität), wodurch Bagatellaufrüstungen und Frequenzanpassungen massiv beschleunigt werden sollen.
- **Parlamentarische Vorstösse (Curia Vista)**:
  - **Postulat 23.3764** (*Keine Versorgungslücken im Mobilfunk mehr!*, KVF-NR, angenommen im Februar 2024): Der Bundesrat legte im Mai 2024 einen Bericht vor, der die kantonal uneinheitliche Bewilligungspraxis analysierte und Vereinfachungen bei der Modernisierung bestehender Antennen forderte.
  - **Anfrage 24.1040** (*Modernisierung von Mobilfunkanlagen* vom 18. März 2024): Thematisiert die durch BGE 150 II 379 entstandenen Verzögerungen bei der 5G-Umstellung und verlangt Rechtssicherheit für Betreiberinnen und Baubehörden.

---

## Würdigung und Ausblick {#wuerdigung-und-ausblick}

Die Rechtsprechung zu Mobilfunkantennen veranschaulicht das Spannungsfeld zwischen föderalistischer Raumplanung und zentralisierter Umwelt- und Infrastrukturpolitik. Das Bundesgericht hat über zweieinhalb Jahrzehnte hinweg eine bemerkenswert konsistente Linie verfolgt:

1. **Schutz der Bundeskompetenz**: Der Schutz vor Strahlung ist ausschliessliche Bundessache. Lokale Versuche, den Antennenbau durch verdeckte Strahlenschutzregeln (wie Abstandsgebote) zu unterbinden, wurden ausnahmslos verworfen.
2. **Respektierung städtebaulicher Gestaltung**: Gemeinden dürfen Standorte über Kaskadenmodelle lenken, solange sie das Netz nicht faktisch verunmöglichen und flexibel bleiben.
3. **Hohe formelle Anforderungen an den Rechtsschutz**: Trotz der Bestätigung der materiellen Gesetzmässigkeit von 5G und adaptiven Antennen ([BGE 151 II 593](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_004_BGE-151-II-593_2025.html)) pocht das Bundesgericht strikt auf das ordentliche Baubewilligungsverfahren ([BGE 150 II 379](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_004_BGE-150-II-379_2024.html)).

Die geplante Reform des Fernmeldegesetzes zielt darauf ab, die von der Rechtsprechung gezogenen engen verfahrensrechtlichen Leitplanken gesetzgeberisch zu lockern, um den Zielkonflikt zwischen digitaler Infrastruktur und Nachbarschaftsopposition neu auszutarieren.

---

## Praxishinweise {#praxishinweise}

### Für Mobilfunkbetreiberinnen und Gesuchsteller {#fuer-betreiber}

> [!TIP]
> **Ordnungsgemässes Baubewilligungsverfahren bei Korrekturfaktoren**: Nach [BGE 150 II 379](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_004_BGE-150-II-379_2024.html) führt der Einsatz von Korrekturfaktoren bei adaptiven Antennen zwingend über das ordentliche Baubewilligungsverfahren mit Planauflage. Der Versuch, die Umstellung im Meldeverfahren abzuwickeln, führt bei Einsprachen unausweichlich zur Aufhebung der Bewilligung und zu langjährigen Verzögerungen.
>
> **Standortdatenblatt akribisch dokumentieren**: Alle OMEN im Berechnungsperimeter (inklusive unüberbauter Bauparzellen mit Nutzungsreserven) müssen lückenlos deklariert werden. Das QS-System muss vor Inbetriebnahme durch das BAKOM validiert sein.
>
> **Kaskadenordnung frühzeitig prüfen**: Gilt in der Gemeinde ein Kaskadenmodell gemäss [BGE 138 II 173](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_004_BGE-138-II-173_2012.html), muss das Baugesuch für einen Standort in der Wohnzone detailliert belegen, weshalb prioritäre Arbeits- oder Gewerbezonen funktechnisch nicht infrage kommen.

### Für Baubewilligungsbehörden und Gemeinden {#fuer-behoerden}

> [!IMPORTANT]
> **Keine Ablehnung gestützt auf Strahlenschutz**: Gemeinden dürfen Antennenbaugesuche unter keinen Umständen mit gesundheitlichen Bedenken, Elektrosmog-Ängsten oder fehlenden Langzeitstudien abweisen. Liegt ein positives Gutachten der kantonalen NIS-Fachstelle vor und sind die AGW eingehalten, ist die Bewilligung umweltrechtlich zwingend zu erteilen.
>
> **Rechtssichere Kaskadenmodelle ausgestalten**: Will die Gemeinde die Standortwahl steuern, muss das Reglement rein städtebaulich begründet sein (Ortsbild, Schutz des Wohncharakters). Es darf keine starre Negativplanung darstellen, sondern muss bei fehlenden Alternativen einen Standort in der Wohnzone zulassen.
>
> **Formelle Prüfung der Einsprachen**: Zur Einsprache ist nur befugt, wer innerhalb des 10%-Berechnungsradius liegt ([BGE 128 II 168](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_004_BGE-128-II-168_2002.html)). Auf Einsprachen weiter entfernter Personen ist in der Regel nicht einzutreten.

### Für die Nachbarschaft und Einsprechende {#fuer-nachbarn}

> [!WARNING]
> **Keine Aussicht mit abstrakter Grenzwertkritik**: Einsprachen, die sich ausschliesslich gegen die Grenzwerte der NISV richten oder die Schädlichkeit von 5G rügen, werden von den Gerichten kostenfällig abgewiesen ([BGE 126 II 399](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_004_BGE-126-II-399_2000-08-30.html), [BGE 151 II 593](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_004_BGE-151-II-593_2025.html)).
>
> **Fokus auf technische und planerische Mängel**: Erfolgversprechend sind Rügen nur, wenn sie konkrete Fehler des Projekts nachweisen:
> - Wurde ein Wohn- oder Schlafraum im Standortdatenblatt fälschlicherweise nicht als OMEN qualifiziert?
> - Wurden bestehende Nutzungsreserven (mögliche Gebäudeaufstockungen) übersehen ([BGE 128 II 340](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_004_BGE-128-II-340_2002.html))?
> - Liegt die Liegenschaft in einer Gemeinde mit Kaskadenordnung und hat die Betreiberin taugliche Alternativstandorte in der Gewerbezone nicht ernsthaft geprüft?
> - Wurde das ordentliche Baubewilligungsverfahren umgangen?

---

## Leitentscheide {#leitentscheide}

| Entscheid | Gegenstand | Bedeutung für die Praxis |
|---|---|---|
| [BGE 126 II 399](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_004_BGE-126-II-399_2000-08-30.html#consideration_3.) | Zweistufiges NISV-Schutzkonzept | Bestätigung der Verfassungsmässigkeit der NISV; Trennung von Immissionsgrenzwerten (IGW) für thermische Effekte und Anlagegrenzwerten (AGW) zur Vorsorge. |
| [BGE 128 II 168](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_004_BGE-128-II-168_2002.html#consideration_2.3) | Einspracheberechtigung der Nachbarn | Etablierung des 10%-Radiusmodells: Zur Beschwerde legitimiert ist, wer innerhalb des Perimeters wohnt, an dessen Rand die Strahlung 10% des AGW erreicht. |
| [BGE 128 II 340](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_004_BGE-128-II-340_2002.html) | OMEN und bauliche Nutzungsreserven | Bei Baugesuchen ist primär auf den bestehenden Zustand abzustellen; der Betreiber muss jedoch Anpassungen vornehmen, sobald Nutzungsreserven realisiert werden. |
| [BGE 128 II 378](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_004_BGE-128-II-378_2002.html) | Standortdatenblatt und OMEN-Begriff | Prüfung der Sendeleistung ERP; Bestätigung, dass Balkone und Dachterrassen keine Orte mit empfindlicher Nutzung (OMEN) darstellen. |
| [BGE 133 II 64](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_004_BGE-133-II-64_2007.html#consideration_5.2) | Abschliessender Charakter des Bundesrechts | Bund regelt Strahlenschutz abschliessend; kantonale und kommunale Sondergrenzwerte oder strahlenschutzbegründete Abstandsregeln sind unzulässig. |
| [BGE 133 II 321](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_004_BGE-133-II-321_2007.html#consideration_4.3.4) | Standortfestlegung innerhalb/ausserhalb Bauzone | Raumplanerische Steuerung ist zulässig, muss aber Umwelt- und Fernmelderecht respektieren; Zonenkonformität in Bauzonen grundsätzlich gegeben. |
| [BGE 138 II 173](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_004_BGE-138-II-173_2012.html#consideration_6.5) | Kommunales Kaskadenmodell | Gemeinden dürfen Standorte aus städtebaulichen Gründen steuern (Vorrang von Arbeitszonen), sofern Wohnzonen bei funktechnischem Bedarf zugänglich bleiben. |
| [BGE 138 II 570](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_004_BGE-138-II-570_2012.html#consideration_4.2) | Antennen in der Landwirtschaftszone | Bejahung der Standortgebundenheit nach Art. 24 lit. a RPG für Antennen zur Abdeckung von Hauptverkehrsachsen (Bahnlinien/Autobahnen). |
| [BGE 141 II 245](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_004_BGE-141-II-245_2015.html#consideration_7.1) | Zonenkonformität und Ästhetikschranken | Schutz des Ortsbilds darf den bundesrechtlichen Versorgungsauftrag nicht vereiteln; Ausweichen auf Nichtbauzonen setzt konkrete Bewilligungsfähigkeit nach Art. 24 RPG voraus. |
| [BGE 150 II 379](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_004_BGE-150-II-379_2024.html#consideration_4.2) | Baubewilligungspflicht für adaptive Antennen | Umstellung auf Korrekturfaktor führt zu Leistungsspitzen und bedingt zwingend ein ordentliches Baubewilligungsverfahren mit Gehörs- und Einspracherechten. |
| [BGE 151 II 593](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_004_BGE-151-II-593_2025.html#consideration_6.3.2) | Gesetzmässigkeit des Korrekturfaktors | Korrekturfaktor und 6-Minuten-Mittelung für adaptive Antennen (5G) sind mit Art. 11 Abs. 2 USG vereinbar; QS-System ist als Überwachungsinstrument tauglich. |

---

## Literatur {#literatur}

Die folgenden Werke werden in den zitierten Leitentscheiden des Bundesgerichts als massgebend herangezogen:

- **IRENE GRAF/JEAN-LUC NIKLAUS**, Mobilfunkanlagen - Beschwerderecht der Nachbarn, KPG-Bulletin 1/2001 S. 29 ff. (zitiert in [BGE 128 II 168](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_004_BGE-128-II-168_2002.html#consideration_2.3) E. 2.3 zur Berechnung des 10%-Radius).
- **BENJAMIN WITTWER**, Bewilligung von Mobilfunkanlagen, Diss. Zürich 2004, S. 200 f. (zitiert in [BGE 133 II 64](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_004_BGE-133-II-64_2007.html#consideration_5.2) E. 5.2 zum abschliessenden Charakter des Immissionsschutzrechts des Bundes).
- **JEAN-BAPTISTE ZUFFEREY/VALENTIN SEYDOUX**, Le permis de construire pour les antennes de téléphonie mobile, in: Baurecht/Droit de la construction 2021 S. 39 ff. (zitiert in [BGE 150 II 379](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_004_BGE-150-II-379_2024.html#consideration_4.3) E. 4.3 zur Notwendigkeit des Baubewilligungsverfahrens für adaptive Antennen).
