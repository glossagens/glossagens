---
title: "Das System der obligatorischen Krankenversicherung (OKP)"
date: 2026-10-26
lastmod: 2026-10-26
description: "Umfassender Leitfaden zum schweizerischen Krankenversicherungssystem (OKP nach KVG): Obligatorium, Leistungskatalog, Kopfprämien, Franchise, Selbstbehalt, Spitalbeitrag, alternative Versicherungsmodelle, Abrechnung und Kassenwechsel."
tags: ["Krankenversicherung", "KVG", "OKP", "Grundversicherung", "Franchise", "Selbstbehalt", "Kopfprämie", "Prämienverbilligung", "Sozialversicherungsrecht"]
typ: institution
kurz: "Die obligatorische Krankenpflegeversicherung (OKP) sichert allen Personen mit Wohnsitz in der Schweiz eine medizinische Grundversorgung nach einheitlichem Leistungskatalog zu, finanziert über einkommensunabhängige Kopfprämien. Im Krankheitsfall tragen Erwachsene die Kosten über eine feste Jahresfranchise (CHF 300.- bis 2'500.-) und einen 10%igen Selbstbehalt (maximal CHF 700.- pro Jahr) teilweise mit, bevor die Krankenkasse die restlichen Kosten vollständig übernimmt."
sachgebiete: [kv]
normen:
  - { gesetz: bv, art: art-117 }
  - { gesetz: kvg, art: art-003 }
  - { gesetz: kvg, art: art-025 }
  - { gesetz: kvg, art: art-032 }
  - { gesetz: kvg, art: art-061 }
  - { gesetz: kvg, art: art-064 }
  - { gesetz: kvg, art: art-065 }
stichworte: ["Krankenversicherung", "Grundversicherung", "OKP", "Franchise", "Selbstbehalt", "Spitalbeitrag", "Kopfprämie", "Wahlfranchise", "Aufnahmezwang", "Freizügigkeit", "Tiers garant", "Tiers payant", "Hausarztmodell", "Telmed", "HMO", "Prämienverbilligung", "Kassenwechsel"]
agent_verified: true
revisions:
  - date: 2026-10-26
    by: "Antigravity"
    model: "gemini-3.8-flash"
    mcp_verified: true
    note: "Erweiterung um die mathematische Beweisführung zur Unrentabilität von Zwischenfranchisen (70%-Grenze gemäss Art. 95 KVV, tabellarischer Gesamtkostenvergleich und Wendepunkt-Analyse)."
  - date: 2026-10-26
    by: "Antigravity"
    model: "gemini-3.8-flash"
    mcp_verified: true
    note: "Erstfassung nach Skill glossagens-themen (Typ institution). Umfassende Darstellung des OKP-Systems und laienverständliche Aufbereitung der Kernbegriffe (Franchise, Selbstbehalt, Spitalbeitrag, Kopfprämie, Tiers garant/payant, AVM). Normtexte Art. 117 BV, Art. 3 und 64 KVG per {{< wortlaut >}} (scripts/wortlaut.py). Volltexte der BGEs via entscheidsuche.ch geladen, Erwägungsnummern, Anker und wörtliche Zitate exakt abgeglichen."
---

## Überblick {#ueberblick}

Das schweizerische Gesundheitssystem zählt zu den leistungsfähigsten, aber auch teuersten der Welt. Das Herzstück der gesundheitlichen Absicherung bildet die **obligatorische Krankenpflegeversicherung (OKP)**, im Volksmund meist schlicht als *Grundversicherung* bezeichnet. Sie ist im Bundesgesetz über die Krankenversicherung (KVG) vom 18. März 1994 geregelt und am 1. Januar 1996 in Kraft getreten.

Die OKP beruht auf einem doppelten Grundprinzip:
1. **Obligatorium und Solidarität**: Jede Person mit Wohnsitz in der Schweiz muss versichert sein; im Gegenzug darf keine Krankenkasse eine Person wegen ihres Alters, ihres Geschlechts oder ihres Gesundheitszustands ablehnen oder mit Vorbehalten belegen.
2. **Finanzierung über Kopfprämien und Kostenbeteiligung**: Die Versicherungsbeiträge werden nicht als prozentualer Lohnabzug erhoben, sondern als feste *Kopfprämie* pro versicherter Person. Im Krankheitsfall beteiligen sich die Versicherten über eine feste *Franchise* und einen prozentualen *Selbstbehalt* an den Behandlungskosten, um ein gewisses Kostenbewusstsein zu wahren.

Für Laien wirkt das Zusammenspiel aus Prämien, Franchisen, Selbstbehalten, Spitalbeiträgen, alternativen Versicherungsmodellen und Zusatzversicherungen oft unübersichtlich. Dieser Beitrag erklärt den rechtlichen Aufbau des Systems und definiert die zentralen Begriffe Schritt für Schritt.

## Verfassungsrechtlicher und gesetzlicher Rahmen {#rechtsgrundlagen}

Die Bundesverfassung weist dem Bund in Art. 117 BV die Kompetenz zu, die Krankenversicherung zu regeln und für obligatorisch zu erklären:

{{< wortlaut gesetz="bv" art="art-117" >}}

Gestützt darauf regelt das KVG die soziale Krankenversicherung. Das System wird durch drei Erlasse des Bundesrechts getragen:
* **Bundesgesetz über die Krankenversicherung (KVG; SR 832.10)**: Definiert die Versicherungspflicht, den Leistungskatalog, die Vertragsbeziehungen zu Ärzten und Spitälern, die Tarife sowie die Finanzierung und Kostenbeteiligung.
* **Verordnung über die Krankenversicherung (KVV; SR 832.102)**: Konkretisiert die gesetzlichen Bestimmungen, insbesondere die Franchisenstufen (Art. 90 ff. KVV), den Höchstbetrag des Selbstbehalts (Art. 103 KVV) und die Ausnahmen von der Versicherungspflicht.
* **Krankenversicherungsaufsichtsgesetz (KVAG; SR 832.12)**: Regelt die staatliche Aufsicht des Bundesamtes für Gesundheit (BAG) über die zugelassenen Krankenkassen und stellt sicher, dass die Kassen über ausreichende Reserven und Solvenz verfügen.

## Das Fundament: Obligatorium, Aufnahmezwang und Solidarität {#fundament-des-systems}

### Die Versicherungspflicht (Art. 3 KVG) {#versicherungspflicht}

{{< wortlaut gesetz="kvg" art="art-003" >}}

In der Schweiz gilt eine umfassende **Versicherungspflicht**. Jede Person muss sich innerhalb von **drei Monaten** nach der Wohnsitznahme in der Schweiz oder nach der Geburt bei einer anerkannten Krankenkasse ihrer Wahl versichern (Art. 3 Abs. 1 KVG). Erfolgt der Beitritt rechtzeitig innert drei Monaten, gilt der Versicherungsschutz rückwirkend ab dem Tag der Geburt bzw. Wohnsitznahme. Bei verspätetem Beitritt beginnt der Schutz erst ab dem Beitrittsdatum, und es kann ein Prämienzuschlag erhoben werden (Art. 5 Abs. 2 KVG).

Das Bundesgericht hat wiederholt unterstrichen, dass das Versicherungsobligatorium an den zivilrechtlichen Wohnsitz (Art. 23 ff. ZGB) anknüpft und die gesamte Wohnbevölkerung erfassen soll: «Gemäss Art. 3 Abs. 1 KVG ist jede Person mit Wohnsitz in der Schweiz der obligatorischen Krankenpflegeversicherung unterstellt, wobei sich der Wohnsitz nach Art. 23 bis 26 ZGB definiert» ([BGE 129 V 77](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_007_BGE-129-V-77_2003.html#consideration_4.2) E. 4.2). Dies gilt nach ständiger Rechtsprechung selbst für Personen ohne geregelten ausländerrechtlichen Aufenthaltsstatus (*Sans-Papiers*), da der Schutz vor Verarmung im Krankheitsfall und der seuchenhygienische Schutz der Allgemeinheit keine Lücken dulden.

### Freie Kassenwahl und Kontrahierungszwang (Art. 4 und Art. 12 KVG) {#aufnahmezwang}

Jede versicherte Person hat das Recht, ihre Krankenkasse unter denjenigen Versicherern frei zu wählen, die an ihrem Wohnort tätig sind. Spiegelbildlich dazu gilt für die Krankenkassen ein strikter **gesetzlicher Aufnahmezwang (Kontrahierungszwang)**:
* Die Kasse muss **jede** versicherungspflichtige Person aufnehmen, die an ihrem Tätigkeitsort wohnt.
* Es dürfen **keine Vorbehalte** (Ausschlüsse bestehender Krankheiten) angebracht werden.
* Es dürfen **keine Wartefristen** verhängt werden.
* Es darf **keine Gesundheitsprüfung** verlangt werden (Fragebogen zum Gesundheitszustand sind in der Grundversicherung unzulässig).

### Gemeinnützigkeit und Verbot des Erwerbszwecks (Art. 13 KVG, Art. 2 KVAG) {#gemeinnuetzigkeit}

In der obligatorischen Grundversicherung dürfen die Krankenkassen **keinen Gewinn erzielen**. Die Anerkennung als Krankenkasse setzt zwingend voraus, «dass sie keinen Erwerbszweck verfolgt und hauptsächlich die soziale Krankenversicherung betreibt» ([BGE 128 V 272](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_007_BGE-128-V-272_2002.html#consideration_4.) E. 4.a). Sämtliche Einnahmen aus den Prämien der Grundversicherung dürfen ausschliesslich zur Deckung der medizinischen Leistungen, der Verwaltungskosten und zur Bildung der gesetzlich vorgeschriebenen Sicherheitsreserven verwendet werden. Überschüssige Reserven müssen nach Vorgabe des Aufsichtsrechts durch Prämienanpassungen oder Reservenabbau an die Versicherten zurückerstattet werden.

### Der Risikoausgleich unter den Krankenkassen {#risikoausgleich}

Da die Kassen allen Versicherten einer Region dieselbe Prämie verlangen müssen, hätten Versicherer einen wirtschaftlichen Anreiz, vor allem junge und gesunde Menschen anzuwerben (*Risikoselektion*). Um dies zu verhindern, existiert ein gesetzlicher **Risikoausgleich** (Art. 105 KVG i.V.m. der Verordnung über den Risikoausgleich in der Krankenversicherung, VORA):
Krankenkassen mit einem überdurchschnittlich jungen und gesunden Versichertenbestand müssen Ausgleichszahlungen an diejenigen Kassen leisten, die einen hohen Anteil an älteren, chronisch kranken oder multimorbiden Versicherten betreuen. Damit wird der Wettbewerb auf die Qualität des Kundenservice und die Verwaltungseffizienz gelenkt, statt auf die Abweisung teurer Patientengruppen.

## Grundversicherung (OKP) vs. Zusatzversicherungen (VVG) {#grund-vs-zusatzversicherung}

Eine der häufigsten Fehlerquellen für Konsumenten ist die Vermischung von Grundversicherung und Zusatzversicherungen. Obwohl beide Policen oft vom selben Versicherungskonzern auf einer einzigen Rechnung ausgewiesen werden, unterstehen sie völlig unterschiedlichen Rechtsregimen:

| Merkmal | Obligatorische Krankenpflegeversicherung (OKP) | Freiwillige Zusatzversicherung |
|---|---|---|
| **Rechtsgrundlage** | Bundesgesetz über die Krankenversicherung (KVG) | Versicherungsvertragsgesetz (VVG) |
| **Rechtsnatur** | Öffentliches Sozialversicherungsrecht | Privatrechtlicher Versicherungsvertrag |
| **Versicherungspflicht** | Obligatorisch für alle Personen mit Wohnsitz CH | Freiwillig |
| **Aufnahme** | Gesetzlicher Aufnahmezwang ohne Vorbehalt | Volle Vertragsfreiheit (Kasse kann ablehnen) |
| **Gesundheitsprüfung** | Streng verboten | Zulässig und üblich (Gesundheitsfragebogen) |
| **Kündigung durch Kasse** | Bei Privatpersonen verboten | Kündigung im Schadenfall vertraglich möglich |
| **Prämiengestaltung** | Kopfprämie nach Region/Altersstufe, kein Gewinn | Risikoprämie nach Alter, Geschlecht und Risiko |
| **Streitigkeiten / Gerichte** | Kostenloses Verfahren vor kantonalem Versicherungsgericht | Zivilgerichte (Art. 243 Abs. 2 lit. f ZPO) |

Das Bundesgericht betont die strikte rechtliche Trennung zwischen KVG und VVG: Streitigkeiten über den Inhalt einer Zusatzversicherung sind reine Zivilstreitigkeiten nach VVG, die vor die Zivilgerichte gehören ([BGE 124 III 44](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_005_BGE-124-III-44_1997-11-13.html#consideration_2.) E. 2.a). 

> [!IMPORTANT]
> **Gesetzliches Koppelungsverbot (Art. 7 Abs. 5 KVG):** 
> Eine Krankenkasse darf den Abschluss einer Grundversicherung niemals davon abhängig machen, dass gleichzeitig eine Zusatzversicherung abgeschlossen wird. Umgekehrt verliert eine versicherte Person ihre bestehenden Zusatzversicherungen **nicht**, wenn sie die Grundversicherung kündigt und zu einer günstigeren Krankenkasse wechselt!

## Der Leistungskatalog: Was bezahlt die Grundversicherung? {#leistungskatalog-und-wzw}

Der Leistungskatalog der Grundversicherung ist für alle Krankenkassen in der ganzen Schweiz **gesetzlich identisch**. Keine Kasse darf in der OKP mehr oder weniger Leistungen erbringen als gesetzlich vorgesehen (Art. 34 Abs. 1 KVG).

### Die Grundleistungen nach Art. 25 KVG {#grundleistungen}

Gestützt auf [Art. 25 KVG](/kommentar/kvg/art-025/) umfasst die OKP:
* **Ärztliche Leistungen**: Untersuchungen, Diagnostik und Therapien durch zugelassene Ärztinnen und Ärzte.
* **Arzneimittel**: Alle vom Bundesamt für Gesundheit in die **Spezialitätenliste (SL)** aufgenommenen rezeptpflichtigen und kassenpflichtigen Medikamente.
* **Spitalbehandlung**: Aufenthalt und Behandlung in der *allgemeinen Abteilung* eines Spitals, das auf der Spitalliste des Wohnkantons steht (oder zum Referenztarif des Wohnkantons).
* **Pflegeleistungen**: Leistungen der häuslichen Krankenpflege (*Spitex*) und im Pflegeheim nach [Art. 25a KVG](/kommentar/kvg/art-025a/).
* **Mutterschaft**: Kontrolluntersuchungen, Ultraschall, Geburtsvorbereitung, Entbindung und Stillberatung nach Art. 29 KVG.
* **Medizinische Rehabilitation und Transportkosten**: Transport- und Rettungskosten zu 50 % bis zu gesetzlichen Jahresgrenzen (Art. 26 und 27 KLV).

### Was die Grundversicherung NICHT bezahlt {#leistungsausschlusse}

Ein häufiges Missverständnis unter Laien betrifft Bereiche, die traditionell nicht oder nur unter extremen Ausnahmen von der Grundversicherung bezahlt werden:
* **Zahnbehandlungen**: Gewöhnliche Kariesbehandlungen, Kronen, Brücken, Spangen oder Dentalhygiene sind von der Grundversicherung **nicht** gedeckt. Die Kosten werden nach Art. 31 KVG nur übernommen, wenn die Zahnbehandlung durch eine schwere, nicht vermeidbare Erkrankung des Kausystems oder eine schwere Allgemeinerkrankung bedingt ist ([BGE 127 V 328](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_007_BGE-127-V-328_2001-09-19.html#consideration_2.) E. 2 & 3). Für Zahnarztkosten schliessen viele Familien daher VVG-Zusatzversicherungen ab.
* **Brillen und Kontaktlinsen für Erwachsene**: Bei Erwachsenen besteht in der Regel keine Kostenübernahme (ausser bei schweren krankheitsbedingten Sehveränderungen); für Kinder bis 18 Jahre gewährt die MiGeL einen gesetzlichen Beitrag von CHF 180.- pro Jahr.
* **Spitalkomfort**: Halbprivat- oder Privatzimmer, freie Arztwahl im Spital (Chefarztbehandlung) gehören ausschliesslich in den Bereich der VVG-Spitalzusatzversicherung.

### Das Wirtschaftlichkeitsgebot: Die WZW-Kriterien (Art. 32 KVG) {#wzw-kriterien}

Jede Leistung der OKP muss nach [Art. 32 Abs. 1 KVG](/kommentar/kvg/art-032/) drei zwingende Voraussetzungen erfüllen:
1. **Wirksamkeit**: Die Behandlung muss medizinisch-wissenschaftlich nachgewiesenermassen geeignet sein, den angestrebten Heilungserfolg zu erreichen.
2. **Zweckmässigkeit**: Die Massnahme muss im Einzelfall indiziert sein und das günstigste Nutzen-Risiko-Verhältnis aufweisen.
3. **Wirtschaftlichkeit**: Die Leistung muss im Verhältnis zum Heilerfolg kostenmässig verhältnismässig sein.

Das Bundesgericht betont stets «den komparativen Charakter der Wirtschaftlichkeit und das damit verbundene Kosten-Nutzen-Verhältnis einer medizinischen Leistung» ([BGE 142 V 26](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_007_BGE-142-V-26_2016.html#consideration_5.2.1) E. 5.2.1). Stehen mehrere gleich wirksame Behandlungsmethoden oder Medikamente zur Verfügung, schuldet die Krankenkasse nur die kostengünstigere Variante.

## Die Finanzierung: Kopfprämie und kantonale Unterschiede {#finanzierung-und-praemien}

Die obligatorische Krankenversicherung unterscheidet sich in ihrer Finanzierung fundamental von den übrigen Sozialversicherungen wie AHV, IV oder ALV. Während dort Lohnbeiträge prozentual vom Einkommen erhoben werden, gilt im KVG das System der **Kopfprämie (Einheitsprämie)** nach Art. 61 KVG:

Jede versicherte Person bezahlt für dieselbe Kasse und dasselbe Modell an ihrem Wohnort denselben festen Frankenbetrag pro Monat — unabhängig davon, ob sie Millionär oder Sozialhilfeempfänger ist.

Die Prämie unterscheidet sich ausschliesslich nach folgenden Kriterien:
1. **Wohnkanton und Prämienregion**: Das KVG erlaubt den Kantonen, bis zu drei Prämienregionen zu bilden (Art. 61 Abs. 2 KVG). In städtischen Gebieten mit hoher Spital- und Ärztedichte sind die Gesundheitskosten pro Kopf höher als in ländlichen Regionen, weshalb die Prämien entsprechend variieren.
2. **Altersstufen**:
   * *Kinder* (bis 18 Jahre): Stark reduzierte Prämien (in der Regel mindestens 70 % günstiger).
   * *Junge Erwachsene* (19 bis 25 Jahre): Ermässigte Prämien (Kassen bieten reduzierte Tarife an, um den Berufseinstieg zu erleichtern).
   * *Erwachsene* (ab 26 Jahre): Volle Standardprämie.
3. **Gewähltes Versicherungsmodell und Franchise**: Wer eine höhere Franchise oder ein alternatives Modell wählt, erhält einen gesetzlichen Prämienrabatt.
4. **Verwaltungskosten und Reserven der Kasse**: Weil jede Krankenkasse eigene Verwaltungskosten hat und ihre Reserven unterschiedlich kalkuliert, unterscheiden sich die Prämien zwischen den Kassen für exakt dieselbe gesetzliche Grundleistung teils um über CHF 1'000.- pro Jahr.

## Kostenbeteiligung: Franchise, Selbstbehalt und Spitalbeitrag {#kostenbeteiligung-im-detail}

Das KVG sieht vor, dass sich Versicherte bei Inanspruchnahme von medizinischen Leistungen an den Kosten beteiligen müssen:

{{< wortlaut gesetz="kvg" art="art-064" >}}

Die Kostenbeteiligung setzt sich für Erwachsene aus drei separaten Komponenten zusammen:
1. **Franchise** (fester Jahresgrundbetrag)
2. **Selbstbehalt** (10 % der darüber hinausgehenden Kosten, maximal CHF 700.- pro Jahr)
3. **Spitalbeitrag** (CHF 15.- pro Tag bei stationärem Spitalaufenthalt)

Das Bundesgericht fasst die gesetzliche Struktur wie folgt zusammen: «Nach Art. 64 Abs. 1 KVG beteiligen sich die Versicherten an den Kosten der für sie erbrachten Leistungen. Diese Kostenbeteiligung besteht gemäss Abs. 2 der Vorschrift aus einem festen Jahresbetrag (Franchise; lit. a) und zehn Prozent der die Franchise übersteigenden Kosten (Selbstbehalt; lit. b)» ([BGE 141 V 612](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_007_BGE-141-V-612_2015.html#consideration_4.3) E. 4.3).

### 1. Die Franchise: Der jährliche Grundbetrag {#franchise}

Die **Franchise** ist derjenige Betrag, den eine versicherte Person in jedem Kalenderjahr (1. Januar bis 31. Dezember) **zuerst vollständig selbst bezahlen muss**, bevor die Krankenkasse überhaupt einen einzigen Franken an die Rechnungen beisteuert.

* **Ordentliche Franchise (Basisfranchise)**: Für Erwachsene beträgt sie von Gesetzes wegen **CHF 300.-** pro Jahr (Art. 90 KVV). Für Kinder wird von Gesetzes wegen **keine Franchise** erhoben (CHF 0.-; Art. 64 Abs. 4 KVG).
* **Wählbare Franchisen (Wahlfranchisen)**: Versicherte können freiwillig eine höhere Franchise wählen. Wer bereit ist, im Krankheitsfall mehr Kosten selbst zu tragen, erhält im Gegenzug einen monatlichen **Prämienrabatt**.

Die gesetzlich zulässigen Franchisestufen nach Art. 93 KVV und die maximal erlaubten Rabatte nach Art. 95 KVV gestalten sich wie folgt:

| Alterskategorie | Mögliche Franchisen (CHF) | Maximaler gesetzlicher Prämienrabatt |
|---|---|---|
| **Erwachsene (ab 19 Jahren)** | **300** (Basis) | CHF 0.- (Standardprämie) |
| | **500** | CHF 140.- / Jahr (70 % des Mehrrisikos von CHF 200.-) |
| | **1'000** | CHF 490.- / Jahr (70 % des Mehrrisikos von CHF 700.-) |
| | **1'500** | CHF 840.- / Jahr (70 % des Mehrrisikos von CHF 1'200.-) |
| | **2'000** | CHF 1'190.- / Jahr (70 % des Mehrrisikos von CHF 1'700.-) |
| | **2'500** (Maximum) | **CHF 1'540.- / Jahr** (70 % des Mehrrisikos von CHF 2'200.-) |
| **Kinder (bis 18 Jahre)** | **0** (Basis) | CHF 0.- |
| | 100 / 200 / 300 / 400 / **600** | Maximal CHF 420.- / Jahr bei Franchise 600 |

> [!NOTE]
> Die Franchise gilt immer pro **Kalenderjahr** (nicht ab Abschlussdatum der Police). Rechnungen von Behandlungen aus dem Dezember werden an die Franchise des alten Jahres angerechnet, Behandlungen ab dem 1. Januar an die Franchise des neuen Jahres. Massgebend ist das Behandlungsdatum, nicht das Datum der Rechnungsstellung.

### 2. Der Selbstbehalt: Die 10 % nach Erreichen der Franchise {#selbstbehalt}

Sobald die aufgelaufenen Gesundheitskosten im Kalenderjahr die gewählte Franchise übersteigen, greift die Leistungspflicht der Krankenkasse. Allerdings übernimmt die Kasse die Kosten nicht sofort zu 100 %: Die versicherte Person muss einen **Selbstbehalt von 10 %** der weiteren Rechnungsbeträge bezahlen (Art. 64 Abs. 2 lit. b KVG).

Der Selbstbehalt ist gesetzlich durch eine jährliche Obergrenze geschützt (Art. 103 KVV):
* Für **Erwachsene** beträgt der maximale Selbstbehalt **CHF 700.- pro Kalenderjahr**.
* Für **Kinder** beträgt der maximale Selbstbehalt **CHF 350.- pro Kalenderjahr**.

Sobald eine erwachsene Person im laufenden Jahr Rechnungen über weitere CHF 7'000.- bezogen hat (10 % davon = CHF 700.-), ist der Selbstbehalt ausgeschöpft. Ab diesem Zeitpunkt übernimmt die Krankenkasse alle weiteren kassenpflichtigen Leistungen bis zum 31. Dezember zu **100 %**.

#### Erhöhter Selbstbehalt von 20 % bei Originalpräparaten {#erhoehter-selbstbehalt}
Um den Einsatz kostengünstiger Nachahmermedikamente zu fördern, gilt nach Art. 38a KLV für bestimmte Originalmedikamente ein **erhöhter Selbstbehalt von 20 %**. Verlangt ein Patient ausdrücklich das teurere Originalpräparat, obwohl ein wirkstoffgleiches, austauschbares Generikum oder Biosimilar existiert, das mindestens 10 % günstiger ist, muss der Patient 20 % statt 10 % Selbstbehalt tragen (es sei denn, der Arzt bestätigt eine medizinische Unverträglichkeit des Generikums).

### 3. Der Spitalbeitrag: Kostenbeteiligung bei stationärem Aufenthalt {#spitalbeitrag}

Muss eine versicherte Person im Spital übernachten (*stationäre Behandlung*), fällt nach Art. 64 Abs. 5 KVG i.V.m. Art. 104 KVV ein zusätzlicher **Spitalbeitrag von CHF 15.- pro Tag** an.

**Zweck:** Der Spitalbeitrag ist kein Zuschlag für medizinische Leistungen, sondern entspricht der häuslichen Ersparnis für Verpflegung und Unterkunft, die der Patient während des Spitalaufenthalts zu Hause einspart (*Haushaltsersparnis*).

**Gesetzliche Ausnahmen (Art. 64 Abs. 5 KVG, Art. 104 Abs. 2 KVV):**
Vom Spitalbeitrag befreit sind:
* Kinder bis 18 Jahre;
* junge Erwachsene bis 25 Jahre, die in Ausbildung stehen;
* Frauen für Spitalaufenthalte im Rahmen der Mutterschaft.

### 4. Volle Befreiung bei Mutterschaft (Art. 64 Abs. 7 KVG) {#mutterschaftsbefreiung}

Eine fundamentale Ausnahme vom Prinzip der Kostenbeteiligung statuiert Art. 64 Abs. 7 KVG zum Schutz der Mutterschaft:
Für spezifische Leistungen bei Mutterschaft (Art. 29 KVG: Schwangerschaftskontrollen, Geburt, Ultraschall, Nachkontrolle) darf **keinerlei Kostenbeteiligung** (weder Franchise noch Selbstbehalt noch Spitalbeitrag) erhoben werden.

Zudem gilt seit der KVG-Revision von 2014: **Ab der 13. Schwangerschaftswoche bis 8 Wochen nach der Geburt** ist die versicherte Frau auch für sämtliche allgemeinen Krankheitsbehandlungen (z. B. eine Grippe, ein Beinbruch oder sonstige Erkrankungen während der Schwangerschaft) vollständig von Franchise, Selbstbehalt und Spitalbeitrag befreit (Art. 64 Abs. 7 lit. b KVG).

### 5. Das maximale finanzielle Jahresrisiko: Ein Rechenbeispiel {#rechenbeispiel}

Viele Versicherte fragen sich: Was muss ich im schlimmsten Fall (z. B. bei einer schweren Operation oder Krebserkrankung) im Jahr maximal aus der eigenen Tasche für medizinische Leistungen bezahlen?

Das maximale Jahresrisiko ergibt sich aus der Addition von Franchise und maximalem Selbstbehalt (ohne Spitalbeitrag):

| Gewählte Franchise | Maximaler Selbstbehalt | Maximales medizinisches Jahresrisiko |
|---|---|---|
| **CHF 300.-** | CHF 700.- | **CHF 1'000.-** |
| **CHF 500.-** | CHF 700.- | **CHF 1'200.-** |
| **CHF 1'000.-** | CHF 700.- | **CHF 1'700.-** |
| **CHF 1'500.-** | CHF 700.- | **CHF 2'200.-** |
| **CHF 2'000.-** | CHF 700.- | **CHF 2'700.-** |
| **CHF 2'500.-** | CHF 700.- | **CHF 3'200.-** |

#### Konkreter Beispielfall: Behandlungskosten von CHF 4'300.-
Frau M. erkrankt im Februar und benötigt Behandlungen und Medikamente in Höhe von insgesamt CHF 4'300.-. Wie viel bezahlt sie selbst?

* **Szenario A (Franchise CHF 300.-):**
  1. Franchise: Frau M. bezahlt die ersten **CHF 300.-** vollständig selbst.
  2. Verbleibender Betrag: CHF 4'300.- minus CHF 300.- = CHF 4'000.-.
  3. Selbstbehalt: Frau M. bezahlt 10 % von CHF 4'000.- = **CHF 400.-**.
  4. Krankenkasse übernimmt: 90 % von CHF 4'000.- = CHF 3'600.-.
  * **Gesamte Kosten für Frau M.:** CHF 300.- + CHF 400.- = **CHF 700.-** (Kasse zahlt CHF 3'600.-).

* **Szenario B (Franchise CHF 2'500.-):**
  1. Franchise: Frau M. bezahlt die ersten **CHF 2'500.-** vollständig selbst.
  2. Verbleibender Betrag: CHF 4'300.- minus CHF 2'500.- = CHF 1'800.-.
  3. Selbstbehalt: Frau M. bezahlt 10 % von CHF 1'800.- = **CHF 180.-**.
  4. Krankenkasse übernimmt: 90 % von CHF 1'800.- = CHF 1'620.-.
  * **Gesamte Kosten für Frau M.:** CHF 2'500.- + CHF 180.- = **CHF 2'680.-** (Kasse zahlt CHF 1'620.-).

### 6. Die Wahl der optimalen Franchise: Faustregel für Konsumenten {#franchisenwahl}

Aus versicherungsmathematischer und finanzieller Sicht gilt in der Schweiz eine klare Faustregel: **Zwischenfranchisen (CHF 500.-, 1'000.-, 1'500.-, 2'000.-) lohnen sich rechnerisch fast nie.**

In der Praxis existieren nur zwei sinnvolle Optionen:

1. **Die Maximalfranchise (CHF 2'500.-)**:
   * **Für wen?** Gesunde Personen, die selten zum Arzt gehen und im laufenden Jahr voraussichtlich weniger als ca. CHF 1'800.- bis 2'000.- an Gesundheitskosten erwarten.
   * **Vorteil:** Man spart die maximale Prämienreduktion (bis zu CHF 1'540.- pro Jahr).
   * **Zwingende Voraussetzung:** Man muss finanziell in der Lage sein, im Ernstfall jederzeit die maximalen Selbstkosten von **CHF 3'200.-** (Franchise 2'500 + Selbstbehalt 700) flüssig auf dem Sparkonto bereitzuhalten.

2. **Die Minimalfranchise (CHF 300.-)**:
   * **Für wen?** Personen mit absehbaren regelmässigen Gesundheitskosten (z. B. chronisch Kranke, Personen mit Dauertherapie oder geplanter Operation) von mehr als ca. CHF 2'000.- pro Jahr, sowie Personen, die im Krankheitsfall keine Ersparnisse von CHF 3'200.- aufbringen können.
   * **Vorteil:** Das finanzielle Jahresrisiko ist auf maximal CHF 1'000.- begrenzt.

### 7. Mathematischer Beweis: Warum Zwischenfranchisen unrentabel sind {#mathematischer-beweis-franchisen}

Dass sich für Erwachsene in der Schweiz rein rechnerisch **nur die Mindestfranchise (CHF 300.-) oder die Höchstfranchise (CHF 2'500.-)** lohnen, ist keine blosse Faustregel, sondern eine mathematische Gesetzmässigkeit des KVG-Prämiensystems. Es gibt **keinen einzigen Betrag an jährlichen Gesundheitskosten**, bei dem eine Zwischenfranchise (CHF 500.-, 1'000.-, 1'500.- oder 2'000.-) günstiger abschneidet als *beide* Extreme.

#### Die gesetzliche Ursache: Der 70%-Deckel (Art. 95 KVV)
Der Bundesrat regelt in Art. 95 KVV, wie viel Prämienrabatt eine Krankenkasse für eine höhere Franchise gewähren darf: Der Rabatt darf **höchstens 70 % des zusätzlich übernommenen finanziellen Risikos** betragen. Für jeden Franken mehr Franchise, den eine versicherte Person selbst riskiert, spart sie maximal 70 Rappen an Prämie.

#### Gesamtkostenvergleich über alle Franchisen
Die tatsächliche jährliche finanzielle Belastung einer versicherten Person berechnet sich nach der Formel:

$$\text{Nettobelastung} = (\text{Behandlungskosten bis Franchise}) + (10\ \% \text{ Selbstbehalt bis CHF 700.-}) - (\text{Prämienrabatt})$$

Vergleicht man diese Nettobelastung (relativ zur Grundprämie der Basisfranchise 300) über das gesamte Spektrum möglicher Krankheitskosten, zeigt sich das mathematische Dilemma der Zwischenfranchisen:

| Reale Behandlungskosten | F = 300 | F = 500 | F = 1'000 | F = 1'500 | F = 2'000 | F = 2'500 | Rechnerisch beste Option |
|---|---|---|---|---|---|---|---|
| **CHF 0.-** (gesund) | CHF 0.- | -CHF 140.- | -CHF 490.- | -CHF 840.- | -CHF 1'190.- | **-CHF 1'540.-** | **F = 2'500** (CHF 1'540.- Ersparnis) |
| **CHF 500.-** | +CHF 320.- | +CHF 360.- | +CHF 10.- | -CHF 340.- | -CHF 690.- | **-CHF 1'040.-** | **F = 2'500** |
| **CHF 1'000.-** | +CHF 370.- | +CHF 410.- | +CHF 510.- | +CHF 160.- | -CHF 190.- | **-CHF 540.-** | **F = 2'500** |
| **CHF 1'500.-** | +CHF 420.- | +CHF 460.- | +CHF 560.- | +CHF 660.- | +CHF 310.- | **-CHF 40.-** | **F = 2'500** |
| **CHF 1'800.-** | +CHF 450.- | +CHF 490.- | +CHF 590.- | +CHF 690.- | +CHF 610.- | **+CHF 260.-** | **F = 2'500** |
| **CHF 2'000.-** | +CHF 470.- | +CHF 510.- | +CHF 610.- | +CHF 710.- | +CHF 810.- | **+CHF 460.-** | **F = 2'500** |
| *Wendepunkt (~ CHF 2'030.-)* | | | | | | | |
| **CHF 2'500.-** | **+CHF 520.-** | +CHF 560.- | +CHF 660.- | +CHF 760.- | +CHF 860.- | +CHF 960.- | **F = 300** |
| **CHF 5'000.-** | **+CHF 770.-** | +CHF 810.- | +CHF 910.- | +CHF 1'010.- | +CHF 1'110.- | +CHF 1'210.- | **F = 300** |
| **CHF 10'000.-** (schwer krank) | **+CHF 1'000.-** | +CHF 1'060.- | +CHF 1'210.- | +CHF 1'360.- | +CHF 1'510.- | +CHF 1'660.- | **F = 300** (CHF 660.- Ersparnis) |

*(Hinweis: Negative Zahlen bedeuten eine Nettoersparnis gegenüber den Kosten bei Franchise 300 ohne Arztbesuch).*

#### Die strukturelle Benachteiligung der Zwischenstufen
Aus der Tabelle ergibt sich die strukturelle Fehlallokation von Zwischenstufen:
* **Bei geringen Kosten (unter ca. CHF 2'000.-)**: Hier gewinnt **ausnahmslos Franchise 2'500**. Wer beispielsweise eine Franchise von CHF 1'500.- wählt, verschenkt bei guter Gesundheit Jahr für Jahr bis zu CHF 700.- an möglichem Prämienrabatt.
* **Bei hohen Kosten (über ca. CHF 2'000.-)**: Hier gewinnt **ausnahmslos Franchise 300**. Wer eine Franchise von CHF 1'500.- wählt und hospitalisiert wird, zahlt unter dem Strich CHF 360.- mehr als mit der Basisfranchise 300.

Zwischenfranchisen bieten keinen echten Mittelweg, sondern vereinen die Nachteile beider Welten: Man erhält nicht den vollen Rabatt, muss im Krankheitsfall aber dennoch erhebliche Mehrkosten selbst tragen. Die Wahl reduziert sich daher auf die Frage: Erwartet man Kosten unter oder über dem Wendepunkt von rund CHF 2'000.-, und verfügt man über die Liquidität, um das maximale Jahresrisiko von CHF 3'200.- bei Franchise 2'500 jederzeit tragen zu können?

## Alternative Versicherungsmodelle (AVM) {#alternative-versicherungsmodelle}

Neben der Wahl der Franchise können Versicherte ihre monatliche Prämie durch die Wahl eines **alternativen Versicherungsmodells (AVM)** senken (Art. 62 KVG):

* **Standardmodell (freie Arztwahl)**: Der Versicherte kann bei gesundheitlichen Problemen direkt und ohne Rücksprache zu jedem beliebigen zugelassenen Arzt oder Spezialisten in der Schweiz gehen. Dies ist das teuerste Modell.
* **Hausarztmodell**: Der Versicherte verpflichtet sich vertraglich, bei allen gesundheitlichen Beschwerden immer zuerst seinen fest gewählten Hausarzt zu konsultieren. Dieser fungiert als Koordinator (*Gatekeeper*) und überweist bei Bedarf an Spezialisten. Rabatt: ca. 10 % bis 15 %.
* **Telmed-Modell**: Der Versicherte muss vor jedem Arztbesuch zwingend eine medizinische Telefon-Hotline der Kasse oder eines Telemedizin-Partners anrufen. Dort wird eine erste Triage vorgenommen und ein Behandlungsfenster eröffnet. Rabatt: ca. 15 % bis 20 %.
* **HMO-Modell (Gesundheitszentrum)**: Der Versicherte wählt eine Gruppenpraxis (HMO-Zentrum), in der Allgemeinärzte und verschiedene Therapeuten unter einem Dach zusammenarbeiten. Rabatt: bis zu 20 % bis 25 %.

> [!WARNING]
> **Pflichten bei Sparmodellen:** Wer ein AVM-Modell wählt, muss sich strikt an die Spielregeln halten (ausser bei echten medizinischen Notfällen und routinemässigen Augen- oder Frauenarztbesuchen). Konsultiert man ohne Überweisung direkt einen Spezialisten, darf die Kasse nach ihren vertraglichen Bedingungen die Kostenübernahme verweigern, den Versicherten verwarnen oder ihn per sofort in das teurere Standardmodell zurückstufen.

Das Bundesgericht hat klargestellt, dass solche vertraglichen Beschränkungen der freien Arztwahl im Verhältnis zwischen Versichertem und Kasse verbindlich sind; gegenüber Spitälern im System des Tiers payant schlagen sie jedoch nicht zulasten der Spitalvergütung durch ([BGE 141 V 546](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_007_BGE-141-V-546_2015.html#consideration_4.) E. 4.1).

## Abrechnungssysteme: Tiers garant und Tiers payant {#abrechnungssysteme}

Wie gelangen Rechnungen von Arzt oder Spital zur Krankenkasse? Das KVG sieht zwei Abrechnungssysteme vor (Art. 42 KVG):

1. **Tiers garant (Art. 42 Abs. 1 KVG)**:
   * Dies ist das gesetzliche Grundmodell im ambulanten Bereich (Arztpraxen).
   * Der Leistungserbringer (Arzt) stellt die Rechnung an den **Patienten**. Der Patient schuldet das Honorar dem Arzt und bezahlt die Rechnung.
   * Anschliessend sendet der Patient den Rückforderungsbeleg an seine Krankenkasse, welche ihm den Betrag abzüglich Franchise und Selbstbehalt zurückerstattet (*Rückerstattungsprinzip*).

2. **Tiers payant (Art. 42 Abs. 2 KVG)**:
   * Dies ist das Standardmodell bei stationären Spitalaufenthalten sowie in vielen Apotheken.
   * Der Leistungserbringer (Spital, Apotheke) sendet die Rechnung direkt an die **Krankenkasse**.
   * Die Kasse bezahlt die gesamte Rechnung an das Spital und stellt der versicherten Person anschliessend die anfallende Franchise, den Selbstbehalt und den Spitalbeitrag in Rechnung.

*Pflicht zur Rechnungskopie (Art. 42 Abs. 3 KVG):* Rechnet der Arzt oder das Spital im System des Tiers payant direkt mit der Kasse ab, ist er gesetzlich verpflichtet, dem Patienten unaufgefordert eine kostenlose Kopie der Abrechnung zuzustellen, damit dieser prüfen kann, ob nur tatsächlich erbrachte Leistungen abgerechnet wurden.

## Soziale Abfederung: Individuelle Prämienverbilligung (IPV) {#praemienverbilligung}

Weil die Kopfprämie das Einkommen nicht berücksichtigt, würde die Krankenkassenprämie einkommensschwache Haushalte unverhältnismässig hart treffen. Als soziales Korrektiv sieht [Art. 65 KVG](/kommentar/kvg/art-065/) die **individuelle Prämienverbilligung (IPV)** vor:

Bund und Kantone stellen jährlich Milliardenbeträge zur Verfügung, um Versicherten in bescheidenen wirtschaftlichen Verhältnissen die Prämie ganz oder teilweise zu verbilligen.

* **Kantonale Zuständigkeit**: Jeder Kanton regelt die Voraussetzungen, Einkommensgrenzen und Berechnungsmodelle selbständig in kantonalen Erlassen (z. B. Ausgleichskasse oder SVA).
* **Pflicht zur Verbilligung für Kinder und junge Erwachsene (Art. 65 Abs. 1bis KVG)**: Das Bundesrecht verpflichtet die Kantone ausdrücklich, die Prämien von Kindern sowie jungen Erwachsenen in Ausbildung aus Familien mit unteren und mittleren Einkommen um **mindestens 50 %** zu verbilligen.
* Das Bundesgericht wacht streng über dieses Schutzziel: Als der Kanton Luzern die Einkommensgrenzen so tief ansetzte, dass Familien des Mittelstandes leer ausgingen, hob das Bundesgericht die kantonale Verordnung wegen Verletzung von Bundesrecht auf: «dass die Kantone für untere und mittlere Einkommen die Prämien von Kindern und jungen Erwachsenen in Ausbildung um mindestens 50 % zu verbilligen haben» ([BGE 145 I 26](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_001_BGE-145-I-26_2019.html#consideration_6.1) E. 6.1).

## Praxishinweise für Versicherte {#praxishinweise}

### Kassenwechsel: Termine und Formvorschriften {#kassenwechsel}

* **Herbst-Kündigungsfrist (30. November)**:
  Die Krankenkassen müssen die neuen Prämien für das Folgejahr bis Ende September publizieren. Versicherte haben das Recht, die Grundversicherung per 31. Dezember zu kündigen. Das Kündigungsschreiben muss **bis spätestens zum letzten Arbeitstag im November (30. November)** bei der bisherigen Kasse eingetroffen sein (Datum des Poststempels genügt nicht; der Eingang bei der Kasse ist massgebend!).
* **Wechsel bei ordentlicher Franchise (30. Juni)**:
  Wer die ordentliche Basisfranchise von CHF 300.- im Standardmodell hat, kann die Grundversicherung zusätzlich mit einer Frist von drei Monaten auch per **30. Juni** kündigen (Eingang der Kündigung bis 31. März).
* **Anpassung der Franchise**:
  * Eine *Herabsetzung* der Franchise (z. B. von 2'500 auf 300) muss der Kasse bis zum 30. November mitgeteilt werden.
  * Eine *Erhöhung* der Franchise (z. B. von 300 auf 2'500) kann der Kasse bis zum 31. Dezember mitgeteilt werden.

### Keine Kündigung bei unbezahlten Ausständen! {#schuldenfalle}

Wer mit Prämien oder Kostenbeteiligungen im Rückstand ist, darf den Krankenversicherer gesetzlich **nicht wechseln** (Art. 64a Abs. 6 KVG). Das Bundesgericht hat entschieden, dass der Wechsel erst zulässig ist, wenn sämtliche Ausstände einschliesslich Zinsen und Betreibungskosten restlos getilgt sind: «Gemäss Abs. 6 Satz 1 von Art. 64a KVG kann die säumige Person den Versicherer - in Abweichung von Art. 7 KVG - nicht wechseln, solange sie die ausstehenden Prämien und Kostenbeteiligungen sowie die Verzugszinse und Betreibungskosten nicht vollständig bezahlt hat» ([BGE 144 V 380](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_007_BGE-144-V-380_2018.html#consideration_6.2) E. 6.2.1).

### Die Zusatzversicherungs-Falle vermeiden {#vvg-falle}

* **Niemals die Zusatzversicherung voreilig kündigen:** Wer die Krankenkasse wechseln möchte, um Prämien zu sparen, sollte vorerst **nur die Grundversicherung** wechseln.
* Möchte man auch die Zusatzversicherungen (VVG) wechseln, muss man bei der neuen Kasse zuerst den Gesundheitsfragebogen einreichen und die **schriftliche, vorbehaltlose Aufnahmebestätigung** abwarten, bevor man die alten Zusatzversicherungen kündigt. Im Gegensatz zur Grundversicherung darf die neue Kasse den Aufnahmeantrag für Zusatzversicherungen jederzeit grundlos ablehnen oder Vorbehalte anbringen.
* Die Grundversicherung kann problemlos bei Kasse A geführt werden, während die Zusatzversicherung bei Kasse B verbleibt. Kassen dürfen dies nicht verweigern.

## Leitentscheide {#leitentscheide}

| Entscheid | Gegenstand | Kernaussage |
|---|---|---|
| [BGE 129 V 77](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_007_BGE-129-V-77_2003.html#consideration_4.2) E. 4.2 | Versicherungsobligatorium (Art. 3 KVG) | Das Versicherungsobligatorium knüpft an den Wohnsitz nach ZGB an und erfasst lückenlos die gesamte Wohnbevölkerung, einschliesslich Sans-Papiers. |
| [BGE 128 V 272](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_007_BGE-128-V-272_2002.html#consideration_4.) E. 4.a | Gemeinnützigkeit und Risikoselektion | Krankenkassen dürfen in der sozialen Krankenversicherung keinen Erwerbszweck verfolgen; Ausgleich von Risikoselektion über den gesetzlichen Risikoausgleich. |
| [BGE 124 III 44](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_005_BGE-124-III-44_1997-11-13.html#consideration_2.) E. 2.a | Abgrenzung Grund- vs. Zusatzversicherung | Zusatzversicherungen unterstehen reinem Privatrecht (VVG); Streitigkeiten gehören vor Zivilgerichte, während die OKP öffentlich-rechtlicher Natur ist. |
| [BGE 142 V 26](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_007_BGE-142-V-26_2016.html#consideration_5.2.1) E. 5.2.1 | WZW-Kriterien (Art. 32 KVG) | Der Begriff der Wirtschaftlichkeit hat zwingend komparativen Charakter; die Kasse vergütet nur das günstigste von mehreren gleich wirksamen Verfahren. |
| [BGE 127 V 328](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_007_BGE-127-V-328_2001-09-19.html#consideration_2.) E. 2 & 3 | Zahnbehandlungen im Leistungskatalog | Gewöhnliche Zahnarztbehandlungen fallen nicht unter Art. 25 KVG, sondern werden nur bei schweren, nicht vermeidbaren Erkrankungen nach Art. 31 KVG vergütet. |
| [BGE 141 V 612](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_007_BGE-141-V-612_2015.html#consideration_4.3) E. 4.3 | Kostenbeteiligung (Art. 64 KVG) | Die Kostenbeteiligung gliedert sich in feste Jahresfranchise und 10 % Selbstbehalt (Höchstbetrag CHF 700.- für Erwachsene). |
| [BGE 124 V 333](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_007_BGE-124-V-333_1998-11-23.html#consideration_1.) E. 1.a | Wahlfranchisen und Prämienreduktion | Systematik der Wahlfranchisen und Prämienreduktionen bei freiwilliger Übernahme eines höheren finanziellen Selbstbeteiligungsrisikos. |
| [BGE 141 V 546](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_007_BGE-141-V-546_2015.html#consideration_4.) E. 4.1 | Alternative Versicherungsmodelle und Tiers payant | Verbindlichkeit vertraglicher Wahleinschränkungen bei Managed-Care- und Hausarztmodellen sowie deren Verhältnis zum Vergütungssystem des Tiers payant. |
| [BGE 144 V 380](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_007_BGE-144-V-380_2018.html#consideration_6.2) E. 6.2.1 | Kassenwechsel und Ausstände (Art. 64a KVG) | Ein Wechsel des Krankenversicherers ist bei Zahlungsrückständen solange ausgeschlossen, bis alle Prämien, Kostenbeteiligungen und Betreibungskosten getilgt sind. |
| [BGE 145 I 26](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_001_BGE-145-I-26_2019.html#consideration_6.1) E. 6.1 | Prämienverbilligung IPV (Art. 65 KVG) | Kantone müssen die Bundesvorgabe zur 50%igen Verbilligung für Kinder und junge Erwachsene aus unteren und mittleren Einkommen wirksam umsetzen. |

## Literatur {#literatur}

* **Gebhard Eugster**, Die obligatorische Krankenpflegeversicherung, in: Schweizerisches Bundesverwaltungsrecht (SBVR), Soziale Sicherheit, 3. Aufl., Basel 2016.
* **Ueli Kieser**, ATSG-Kommentar, 4. Aufl., Zürich/Basel/Genf 2020.
* **Thomas Gächter / Bernhard Rütsche**, Gesundheitsrecht, 4. Aufl., Basel 2023.
* **Bundesamt für Gesundheit (BAG)**, Leitfaden zur Krankenversicherung, Bern (laufend aktualisiert).
