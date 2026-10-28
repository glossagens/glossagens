---
title: "Das Schweizer Strafregister: Funktionsweise, Einträge und Löschfristen"
date: 2026-10-26
lastmod: 2026-10-26
description: "Laiengerechter und juristisch präziser Leitfaden zum schweizerischen Strafregister nach dem neuen Strafregistergesetz (StRegG): Funktionsweise von VOSTRA, Abgrenzung von Privatauszug, Sonderprivatauszug und Behördenauszug, Eintragsvoraussetzungen bei Verbrechen, Vergehen, Strafbefehlen und Übertretungen sowie die genauen Aufbewahrungs- und Entfernungsfristen."
tags: ["Strafregister", "VOSTRA", "StRegG", "Privatauszug", "Sonderprivatauszug", "Behördenauszug", "Strafbefehl", "Löschungsfristen", "Vorstrafen", "Recht auf Vergessen"]
typ: institution
kurz: "Das schweizerische Strafregister (VOSTRA) unterscheidet grundlegend zwischen dem behördlichen Gesamtsystem und dem Privatauszug für Dritte: Verbrechen und Vergehen – einschliesslich Strafbefehle – werden stets registriert, während Übertretungen nur ausnahmsweise (etwa bei Bussen über 5'000 Franken) eingetragen werden. Im Privatauszug für Arbeitgeber oder Vermieter werden bedingte Strafen bereits nach erfolgreichem Ablauf der Probezeit nicht mehr angezeigt, während unbedingte Strafen für zwei Drittel der 15-jährigen Entfernungsfrist sichtbar bleiben. Gegenüber den Justiz- und Sicherheitsbehörden bleiben Einträge wesentlich länger gespeichert (10 bis 25 Jahre, bei schwersten Verbrechen bis zum Tod)."
sachgebiete: [strafvollzug, strafrecht.strafzumessung, strafprozess.strafbefehl]
normen:
  - { gesetz: stgb, art: art-010 }
  - { gesetz: stgb, art: art-034 }
  - { gesetz: stgb, art: art-042 }
  - { gesetz: stgb, art: art-047 }
  - { gesetz: stgb, art: art-052 }
  - { gesetz: stgb, art: art-067 }
  - { gesetz: stgb, art: art-106 }
  - { gesetz: stpo, art: art-352 }
  - { gesetz: stpo, art: art-354 }
stichworte: ["Strafregister", "VOSTRA", "StRegG", "Privatauszug", "Sonderprivatauszug", "Behördenauszug", "Strafbefehl", "Geldstrafe", "Freiheitsstrafe", "Busse", "Übertretung", "Probezeit", "Löschfrist", "Entfernungsfrist", "Recht auf Vergessen", "Tätigkeitsverbot"]
revisions:
  - date: 2026-10-26
    by: "Antigravity"
    model: "gemini-3.8-flash"
    note: "Erstfassung nach Skill glossagens-themen (Typ institution). Normtext Art. 10 StGB per {{< wortlaut >}} eingebunden; StRegG (SR 330) und StRegV über Fedlex verifiziert. Zehn Leitentscheide von entscheidsuche.ch als Volltext abgeglichen, Erwägungsnummern, HTML-Anker und wörtliche Zitate geprüft. Mechanische Prüfung durch pruefen.py bestanden."
---

## Überblick {#ueberblick}

Kaum ein behördliches Dokument löst in der Bevölkerung so viel Unsicherheit aus wie das Strafregister. Viele Menschen befürchten, nach einer Geschwindigkeitsbusse oder einem schriftlichen Strafbefehl der Staatsanwaltschaft lebenslang gebrandmarkt zu sein und keine Stelle oder Wohnung mehr zu finden.

Das schweizerische Strafregisterrecht beruht auf einem **Zwei-Ebenen-System**: Was im zentralen behördlichen Computerregister gespeichert ist, unterscheidet sich grundlegend von dem, was auf dem Auszug steht, den man bei einer Stellenbewerbung vorlegt.

Am 23. Januar 2023 ist das Bundesgesetz über das Strafregister-Informationssystem VOSTRA (Strafregistergesetz, StRegG, SR 330) in Kraft getreten. Es hat die früheren Bestimmungen der Art. 365 ff. aStGB abgelöst und das Register grundlegend modernisiert. Das System verfolgt zwei gegenläufige Zwecke:
1. **Strafverfolgung und Sicherheit**: Gerichte, Staatsanwaltschaften und Polizeibehörden müssen rasch und vollständig wissen, ob eine beschuldigte Person bereits straffällig geworden ist ([BGE 148 IV 356 E. 2.4.2](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-148-IV-356_2022.html#consideration_2.4.2)).
2. **Rehabilitation und Recht auf Vergessen**: Eine Person, die ihre Strafe verbüsst oder sich während einer gerichtlichen Probezeit bewährt hat, soll sich wieder unbeschwert in die Gesellschaft und das Arbeitsleben eingliedern können, ohne dauerhaft durch alte Verfehlungen diskriminiert zu werden ([BGE 150 IV 103 E. 2.2.2](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-150-IV-103_2024.html#consideration_2.2.2)).

Das Gesetz löst dieses Spannungsverhältnis dadurch, dass es strikt zwischen der internen Datenspeicherung im System VOSTRA und den nach aussen sichtbaren Auszügen unterscheidet.

## Rechtsgrundlagen und Registeraufbau {#rechtsgrundlagen}

Das schweizerische Strafregister wird vom **Bundesamt für Justiz (BJ)** in Bern zentral für die gesamte Eidgenossenschaft als Informatiksystem namens **VOSTRA** betrieben.

| Ebene | Erlass | Regelungsgegenstand |
|---|---|---|
| Bundesverfassung | Art. 13 BV | Schutz der Privatsphäre und Schutz vor Missbrauch persönlicher Daten |
| Bundesgesetz | StRegG (SR 330) | Gesetz über das Informationssystem VOSTRA: Organisation, Einträge, Zugriffsrechte, Fristen und Auszüge |
| Verordnung | StRegV (SR 330.1) | Vollzugsverordnung mit technischen Details und Gebühren |
| Materielles Strafrecht | [Art. 10 StGB](/kommentar/stgb/art-010/) | Dreiteilung der Delikte: Verbrechen, Vergehen und Übertretungen |
| Sanktionenrecht | [Art. 34](/kommentar/stgb/art-034/), Art. 40, [Art. 42](/kommentar/stgb/art-042/), [Art. 106 StGB](/kommentar/stgb/art-106/) | Strafarten: Geldstrafe, Freiheitsstrafe, bedingter Vollzug und Busse |
| Massnahmenrecht | [Art. 67 StGB](/kommentar/stgb/art-067/) | Tätigkeitsverbote (Grundlage für den Sonderprivatauszug) |
| Strafprozessrecht | [Art. 352 ff. StPO](/kommentar/stpo/art-352/) | Strafbefehlsverfahren und Gleichstellung des Strafbefehls mit dem Urteil |
| Jugendstrafrecht | JStG (SR 311.1) | Schutzmassnahmen und Strafen für Minderjährige zwischen 10 und 18 Jahren |

Für die Frage, ob eine Handlung überhaupt im Strafregister auftaucht, ist die gesetzliche Einteilung der Straftaten nach Art. 10 StGB der entscheidende Ausgangspunkt:

{{< wortlaut gesetz="stgb" art="art-010" >}}

## Wann wird man im Strafregister eingetragen? {#wann-eintrag}

In der Praxis herrscht oft Verwirrung darüber, welche Verstösse registriert werden. Das Gesetz knüpft die Eintragungspflicht an den Schweregrad der Straftat und die Rechtsnatur der Sanktion (Art. 18 StRegG).

### 1. Verbrechen und Vergehen (stets eintragungspflichtig) {#verbrechen-vergehen}

Jeder rechtskräftige Schuldspruch wegen eines Verbrechens (vorsätzliche Taten mit Strafdrohung von mehr als 3 Jahren Freiheitsstrafe, z. B. schwerer Diebstahl, Raub, schwere Körperverletzung) oder Vergehens (Strafdrohung bis zu 3 Jahren Freiheitsstrafe oder Geldstrafe, z. B. einfache Körperverletzung, gewöhnlicher Diebstahl, Veruntreuung, fahrlässige schwere Verkehrsregelverletzung) wird **ausnahmslos in VOSTRA eingetragen** (Art. 18 Abs. 1 Ziff. 1 StRegG).

Dabei spielt es keine Rolle, ob die Strafe:
- als Freiheitsstrafe (Art. 40 StGB) oder als [Geldstrafe](/kommentar/stgb/art-034/) ausgesprochen wird;
- [bedingt](/kommentar/stgb/art-042/) (auf Bewährung aufgeschoben), [teilbedingt](/kommentar/stgb/art-043/) oder unbedingt (sofort zu vollziehen) verhängt wird.

Auch eine bedingte Geldstrafe von wenigen Tagessätzen wegen einer Unachtsamkeit im Strassenverkehr ist die Sanktion für ein Vergehen und führt daher zwingend zur Registrierung in VOSTRA.

### 2. Der Strafbefehl: Eintrag ohne Gerichtsverhandlung {#strafbefehl}

Ein weit verbreiteter Irrglaube lautet: *"Ich stand nie vor Gericht, sondern erhielt bloss Post von der Staatsanwaltschaft, also habe ich keinen Strafregistereintrag."*

Das Gegenteil ist der Fall: In der Schweiz werden über 90 Prozent aller Strafurteile im summarischen Strafbefehlsverfahren nach [Art. 352 ff. StPO](/kommentar/stpo/art-352/) durch die Staatsanwaltschaft gefällt. Erhebt die betroffene Person innert 10 Tagen keine Einsprache, gilt der Grundsatz, dass «ohne gültige Einsprache der Strafbefehl zum rechtskräftigen Urteil wird» ([BGE 142 IV 11 E. 1.2.2](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-142-IV-11_2016.html#consideration_1.2.2); [BGE 145 IV 438 E. 1.3](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-145-IV-438_2019.html#consideration_1.3)).

Ein rechtskräftiger Strafbefehl wegen eines Verbrechens oder Vergehens ist registerrechtlich einem Urteil eines Gerichts völlig gleichgestellt und wird unmittelbar in VOSTRA erfasst.

### 3. Übertretungen: Grundsatz der Nichteintragung {#uebertretungen}

Übertretungen sind Taten, die das Gesetz nur mit Busse bedroht (Art. 103 StGB), etwa geringfügiger Diebstahl unter 300 Franken (Art. 172ter StGB), Tätlichkeiten (Art. 126 StGB), Ruhestörung oder einfache Verkehrsregelverletzungen.

Für Übertretungen gilt der umgekehrte Grundsatz: **Sie werden in der Regel nicht im Strafregister eingetragen** ([BGE 147 IV 471 E. 5.1.1](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-147-IV-471_2021.html#consideration_5.1.1)).

Eine Eintragung von Übertretungen in VOSTRA erfolgt nach Art. 18 Abs. 1 Ziff. 3 StRegG ausschliesslich unter folgenden strengen Voraussetzungen:
- Die ausgesprochene Busse beträgt **mehr als 5'000 Franken** oder es wurden mehr als 180 Stunden gemeinnützige Arbeit verhängt ([BGE 135 IV 170 E. 4.5](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-135-IV-170_2009.html#consideration_4.5));
- Das Gesetz verpflichtet oder ermächtigt die Behörde bei Rückfall zu einer Strafschärfung;
- Die Übertretung wird zusammen mit einem anderen einzutragenden Vergehen im selben Urteil beurteilt; oder
- Es wird ein Tätigkeitsverbot ([Art. 67 StGB](/kommentar/stgb/art-067/)) bzw. ein Kontakt- und Rayonverbot angeordnet.

### 4. Was niemals ins Strafregister gelangt {#kein-eintrag}

Folgende Vorgänge führen zu keinem Eintrag:
- **Ordnungsbussen**: Bussen im Ordnungsbussenverfahren nach dem Ordnungsbussengesetz (OBG), wie Parkbussen oder standardisierte Geschwindigkeitsbussen der Polizei. Sie werden anonym bezahlt, das Verfahren wird ohne Namensprotokollierung abgeschlossen.
- **Freisprüche und Nichteinstellungsverfügungen**: Endet ein Strafverfahren mit einem Freispruch oder einer Verfahrenseinstellung nach [Art. 319 StPO](/kommentar/stpo/art-319/), erfolgt kein Eintrag.
- **Strafbefreiung nach Art. 52 StGB**: Hat das Gericht oder die Staatsanwaltschaft zwar die Schuld festgestellt, aber wegen Geringfügigkeit von Schuld und Tatfolgen oder infolge Wiedergutmachung von einer Bestrafung abgesehen ([Art. 52 StGB](/kommentar/stgb/art-052/)), schliesst Art. 18 Abs. 1 Ziff. 1 StRegG den Registereintrag ausdrücklich aus.
- **Hängige Verfahren im Privatauszug**: Ein laufendes Strafverfahren wird zwar für die Justiz in VOSTRA vermerkt (Art. 24 StRegG), erscheint aber wegen der verfassungsrechtlichen Unschuldsvermutung (Art. 32 Abs. 1 BV, [Art. 10 StPO](/kommentar/stpo/art-010/)) **niemals auf dem Privatauszug** (Art. 41 StRegG).

### 5. Jugendstrafen {#jugendstrafen}

Urteile gegen Jugendliche (10 bis 18 Jahre) nach dem Jugendstrafgesetz (JStG) unterliegen einem stark erzieherischen Regime. Leichte Sanktionen wie ein Verweis oder eine persönliche Arbeitsleistung gelangen nicht in den Privatauszug. Eingetragen werden nach Art. 18 Abs. 2 JStG nur gravierende Sanktionen wie ein Freiheitsentzug (Art. 25 JStG), eine geschlossene oder offene Unterbringung ([Art. 15 JStG](/kommentar/jstg/art-015/)) oder ein Tätigkeitsverbot (Art. 16a JStG).

## Die verschiedenen Auszugsarten {#auszugsarten}

Das Gesetz trennt sauber zwischen dem Schutz der Privatsphäre der Bürger und den Kontrollbedürfnissen des Staates. Es bestehen drei Hauptkategorien von Auszügen:

| Auszugsart | Gesetzliche Grundlage | Wer erhält ihn? | Was ist ersichtlich? |
|---|---|---|---|
| **Privatauszug** | Art. 41 i.V.m. Art. 40 StRegG | Nur die betroffene Person selbst (zur Vorlage bei Dritten) | Stark gefiltert: Verurteilungen zu Freiheitsstrafen und Geldstrafen nur für begrenzte Zeit; bedingte Strafen verschwinden nach bestandener Probezeit; keine hängigen Verfahren |
| **Sonderprivatauszug** | Art. 42 StRegG | Betroffene Person bei Nachweis einer Tätigkeit mit Schutzbedürftigen | Ausschliesslich gerichtliche Berufs-, Tätigkeits-, Kontakt- und Rayonverbote zum Schutz von Minderjährigen und besonders schutzbedürftigen Personen |
| **Behördenauszug 1** | Art. 37 StRegG | Strafgerichte, Staatsanwaltschaften, Strafvollzugsbehörden | Vollständiger Einblick: Alle Grundurteile, nachträglichen Entscheide und hängigen Strafverfahren bis zur definitiven Entfernung |
| **Behördenauszug 2 & 3** | Art. 38 & 39 StRegG | Polizei, Nachrichtendienst, Migrationsbehörden, Einbürgerungsbehörden, KESB | Differenzierte behördliche Einsicht je nach gesetzlichem Aufgabengebiet |

### Der normale Privatauszug (Art. 41 StRegG) {#normaler-privatauszug}

Der Privatauszug ist das Standarddokument, das man bei Stellenbewerbungen, Wohnungssuchen oder Bewilligungsanträgen vorlegt. 

Er vermittelt Zugang zu den Daten des Behördenauszugs 4 (Art. 40 StRegG), schliesst jedoch hängige Strafverfahren ausdrücklich aus (Art. 41 StRegG). Er ist so konzipiert, dass verjährte oder leichtere Verfehlungen möglichst rasch unsichtbar werden, um die wirtschaftliche Existenz der Person nicht zu gefährden.

### Der Sonderprivatauszug (Art. 42 StRegG) {#sonderprivatauszug}

Der Sonderprivatauszug wurde als direkte Konsequenz der Volksinitiative *Pädophilen-Initiative* eingeführt. Arbeitgeber oder Trägerorganisationen (wie Schulen, Kindergärten, Heime, Sportvereine oder Pflegedienste) sind gesetzlich gehalten, von Personen, die regelmässig mit Minderjährigen oder schutzbedürftigen Erwachsenen arbeiten, diesen Spezialauszug zu verlangen.

Der Sonderprivatauszug enthält **ausschliesslich** gerichtliche Tätigkeitsverbote nach [Art. 67 Abs. 2–4 StGB](/kommentar/stgb/art-067/) sowie Kontakt- und Rayonverbote nach Art. 67b StGB ([BGE 149 IV 161 E. 2.5.1](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-149-IV-161_2023.html#consideration_2.5.1)). 

Hat eine Person beispielsweise eine Veruntreuung begangen, ist der normale Privatauszug belastet, der Sonderprivatauszug jedoch leer. Wurde hingegen ein Tätigkeitsverbot wegen Delikten gegen Kinder verhängt, erscheint dieses Verbot im Sonderprivatauszug so lange, wie das Verbot rechtswirksam ist – im Regelfall lebenslänglich (Art. 42 Abs. 3 StRegG).

## Wie lange bleibt ein Eintrag sichtbar? Die Fristen {#fristen}

Hinsichtlich der Dauer unterscheidet das Gesetz präzise zwischen zwei Zeiträumen:
1. Wie lange ein Urteil auf dem **Privatauszug** für Arbeitgeber und Vermieter zu sehen ist (Erscheinungsdauer); und
2. Wie lange die Daten intern im behördlichen Informationssystem **VOSTRA** gespeichert bleiben, bis sie physisch vernichtet werden (Entfernungsfrist).

| Art der Strafe | Sichtbarkeit im Privatauszug (Art. 40 StRegG) | Aufbewahrung in VOSTRA (Art. 30 StRegG) |
|---|---|---|
| **Bedingte Geldstrafe oder bedingte Freiheitsstrafe** (ohne Widerruf) | **Nur während der Probezeit** (in der Regel 2 bis 3 Jahre, max. 5 Jahre; Art. 40 Abs. 3 lit. b StRegG) | **15 Jahre** ab Urteilsrechtskraft (Art. 30 Abs. 2 lit. d StRegG) |
| **Busse wegen Vergehen oder Verbrechen** | **2 Jahre** Bewährungszeit ab Urteilsrechtskraft (Art. 40 Abs. 3 lit. c StRegG) | **15 Jahre** ab Urteilsrechtskraft |
| **Unbedingte Geldstrafe / Freiheitsstrafe unter 1 Jahr** | **10 Jahre** (zwei Drittel der 15-jährigen VOSTRA-Frist; Art. 40 Abs. 3 lit. a StRegG) | **15 Jahre** ab Rechtskraft |
| **Freiheitsstrafe von 1 bis unter 5 Jahren** | Zwei Drittel der VOSTRA-Frist | **20 Jahre** ab Rechtskraft zuzüglich Strafdauer (Art. 30 Abs. 2 lit. a Ziff. 2 StRegG) |
| **Freiheitsstrafe ab 5 Jahren** | Zwei Drittel der VOSTRA-Frist | **25 Jahre** ab Rechtskraft zuzüglich Strafdauer (Art. 30 Abs. 2 lit. a Ziff. 1 StRegG) |
| **Lebenslängliche Freiheitsstrafe / Mord / Verwahrung** | Bis zum Tod (Art. 40 Abs. 3 lit. a StRegG) | **Bis zum Tod** der verurteilten Person (Art. 30 Abs. 2 lit. c StRegG) |
| **Landesverweisung** ([Art. 66a StGB](/kommentar/stgb/art-066a/)) | Mindestens bis zum Ende der Landesverweisung | **Bis zum Tod** der verurteilten Person (Art. 30 Abs. 2 lit. n StRegG) |

### Die Probezeit als Schlüssel zum leeren Privatauszug {#probezeit-schluessel}

Für den Rechtsalltag von Privatpersonen ist Art. 40 Abs. 3 lit. b StRegG die wichtigste Norm:
Wird eine Person zu einer bedingten Strafe verurteilt (was bei Ersttätern für Geldstrafen und Freiheitsstrafen bis zu 2 Jahren der Regelfall nach [Art. 42 StGB](/kommentar/stgb/art-042/) ist), setzt das Gericht eine Probezeit von zwei bis fünf Jahren fest. 

Bewährt sich die verurteilte Person während dieser Probezeit – begeht sie also kein neues Verbrechen oder Vergehen –, **verschwindet der Eintrag mit Ablauf der Probezeit automatisch aus dem Privatauszug**.

*Beispiel*: Jemand wird am 1. Februar 2024 per Strafbefehl wegen eines Vergehens zu einer bedingten Geldstrafe mit 2 Jahren Probezeit verurteilt. 
- Vom 1. Februar 2024 bis zum 31. Januar 2026 erscheint die Strafe auf dem Privatauszug.
- Am 1. Februar 2026 ist die Probezeit abgelaufen. Wird nun ein Privatauszug bestellt, ist dieser leer.
- Im internen Behördenregister VOSTRA bleibt das Urteil jedoch bis zum 1. Februar 2039 (15 Jahre) gespeichert.

### Kaskadenwirkung bei neuen Straftaten {#kaskadenwirkung}

Die Entfernungsfristen verlängern sich, wenn eine Person vor Ablauf der Frist erneut straffällig wird (Art. 30 Abs. 1 StRegG). Ein Grundurteil wird erst dann aus VOSTRA entfernt, wenn bei **allen** eingetragenen Urteilen derselben Person die massgebliche Frist abgelaufen ist. Ein neuer Schuldspruch reisst daher frühere Verurteilungen mit und verhindert deren fristgerechte Löschung.

## Datenschutz, Einsichtsrecht und Verwertbarkeit {#datenschutz-verwertbarkeit}

Das Strafregister unterliegt strengsten datenschutzrechtlichen Anforderungen. Niemand kann ohne Weiteres das Strafregister einer Drittperson einsehen.

### 1. Drittauskünfte verboten {#drittauskuenfte-verboten}

Private Dritte – wie Arbeitgeber, Vermieter, Versicherungen oder Nachbarn – haben **keinerlei direkten Zugriff** auf das Strafregister. Die registerführende Stelle darf Privaten über fremde Personen keine Auskunft erteilen; eine Verletzung dieser Pflicht erfüllt den Tatbestand der Amtsgeheimnisverletzung ([BGE 127 IV 122 E. 3.](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-127-IV-122_2001-05-01.html#consideration_3.)).

Dritte können lediglich die betroffene Person bitten, selbst einen Privatauszug zu bestellen und vorzulegen.

### 2. Das eigene Auskunftsrecht (Art. 48 StRegG) {#eigenes-auskunftsrecht}

Jede Person hat das verfassungs- und datenschutzrechtliche Recht zu erfahren, was der Staat über sie gespeichert hat (Art. 13 Abs. 2 BV; Art. 25 DSG; Art. 48 StRegG). Auf schriftliches Gesuch hin stellt das BJ einer Person einen vollständigen Auszug über sämtliche zu ihr in VOSTRA gespeicherten Daten (inklusive hängiger Verfahren und behördlicher Einträge) zu.

### 3. Was gilt, wenn ein Eintrag gelöscht ist? {#folgen-loeschung}

Sobald ein Eintrag nach Ablauf der Fristen aus dem Register entfernt worden ist, gilt das verfassungsrechtliche **Recht auf Vergessen**: «können dem Betroffenen entfernte Strafen nicht mehr entgegen gehalten werden» ([BGE 135 IV 87 E. 2.4](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-135-IV-87_2009.html#consideration_2.4)). 

Ein Strafrichter darf eine aus VOSTRA entfernte Verurteilung in einem späteren Verfahren bei der Strafzumessung ([Art. 47 StGB](/kommentar/stgb/art-047/)) oder beim Entscheid über den Strafaufschub grundsätzlich nicht mehr strafschärfend berücksichtigen. Dasselbe Verwertungsverbot bindet auch den Haftrichter bei der Prüfung der Wiederholungsgefahr ([BGE 135 I 71 E. 2.10](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_001_BGE-135-I-71_2009.html#consideration_2.10)). 

Im neuen Strafregistergesetz hat der Bundesgesetzgeber die Voraussetzungen für die Berücksichtigung entfernter Urteile im Bereich psychiatrischer Gutachten gelockert, die strikten Entfernungsfristen jedoch verlängert ([BGE 150 IV 103 E. 2.2.2](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-150-IV-103_2024.html#consideration_2.2.2)).

## Praxishinweise {#praxishinweise}

In der Beratungspraxis stellen sich regelmässig dieselben Kernfragen:

### 1. Darf ich mich bei einer Bewerbung als nicht vorbestraft bezeichnen? {#bewerbung-vorbestraft}
Ja, im privaten Geschäftsverkehr (gegenüber privaten Arbeitgebern und Vermietern) gilt: Weist der Privatauszug keinen Eintrag auf, darf sich die betroffene Person wahrheitsgemäss als nicht vorbestraft bezeichnen. Dies gilt auch dann, wenn das Urteil im internen Behördensystem VOSTRA noch verzeichnet ist. 

Etwas anderes gilt nur gegenüber Behörden in gesetzlich streng geregelten Sicherheitsüberprüfungen (z. B. Nachrichtendienst, Polizei, Zulassung als Rechtsanwalt nach [BGE 150 II 308 E. 5.6](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_004_BGE-150-II-308_2024.html#consideration_5.6)), die gesetzlich zur Einsicht in die Behördenauszüge 1 bis 3 ermächtigt sind.

### 2. Darf jeder Arbeitgeber einen Strafregisterauszug verlangen? {#arbeitgeber-auszug}
Nein. Nach dem Datenschutzgesetz (Art. 6 DSG) und dem Arbeitsrecht (Art. 328b OR) dürfen Arbeitgeber nur Daten erheben, die für das konkrete Arbeitsverhältnis unmittelbar relevant sind. 
- **Zulässig**: Ein Privatauszug bei einem Bankangestellten mit Kassen- oder Vermögenszugriff oder bei einem Chauffeur (bezüglich Verkehrsdelikten);
- **Unzulässig**: Die pauschale Einforderung eines Strafregisterauszugs für Tätigkeiten ohne besonderes Vertrauens- oder Gefahrenpotenzial (z. B. Hilfsarbeiten im Lager).

### 3. Wie bestelle ich den Strafregisterauszug? {#bestellung-auszug}
Der Auszug kann auf zwei Wegen bezogen werden:
1. **Online**: Über das offizielle Portal des Bundesamts für Justiz ([www.strafregister.admin.ch](https://www.strafregister.admin.ch)). Der Auszug kann digital signiert als PDF oder per Post zugestellt werden (Kosten: CHF 17.–).
2. **Am Postschalter**: In jeder Filiale der Schweizerischen Post unter persönlicher Vorlage eines gültigen Ausweises (Kosten: CHF 20.–).

Für den **Sonderprivatauszug** verlangt das BJ zwingend eine schriftliche Bestätigung des Arbeitgebers oder der Organisation, dass die betroffene Person eine Funktion mit Minderjährigen ausübt.

### 4. Was tun bei fehlerhaften Einträgen? {#fehlerhafte-eintraege}
Stellt eine Person fest, dass im Register ein falsches Urteil erfasst ist, Fristen nicht berechnet wurden oder ein Freispruch fälschlicherweise als Schuldspruch aufgeführt wird, kann sie nach Art. 56 StRegG bei der registerführenden Stelle des BJ schriftlich ein **Berichtigungs- oder Löschungsgesuch** stellen. Das BJ prüft die Gerichtsakten und nimmt die Korrektur von Amtes wegen vor.

## Leitentscheide {#leitentscheide}

| Entscheid | Fundstelle | Kernaussage zum Registerrecht |
|---|---|---|
| **BGE 150 IV 103** | [BGE 150 IV 103 E. 2.2.2](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-150-IV-103_2024.html#consideration_2.2.2) | Inkrafttreten des StRegG am 23. Januar 2023; Verlängerung der Aufbewahrungsfristen im VOSTRA und Reichweite des Rechts auf Vergessen bei der Verwertung früherer Strafakten und Gutachten. |
| **BGE 148 IV 356** | [BGE 148 IV 356 E. 2.4.2](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-148-IV-356_2022.html#consideration_2.4.2) | Das Sachgericht hat vor Erlass des Urteils von Amtes wegen einen aktuellen Strafregisterauszug über die beschuldigte Person einzuholen; ein 8 Monate alter Auszug genügt nicht. |
| **BGE 142 IV 11** | [BGE 142 IV 11 E. 1.2.2](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-142-IV-11_2016.html#consideration_1.2.2) | Ohne gültige Einsprache wird der Strafbefehl zum rechtskräftigen Urteil ([Art. 354 Abs. 3 StPO](/kommentar/stpo/art-354/)) und begründet die Eintragungspflicht im Strafregister. |
| **BGE 135 IV 87** | [BGE 135 IV 87 E. 2.4](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-135-IV-87_2009.html#consideration_2.4) | Verwertungsverbot: Aus dem Strafregister entfernte Vorstrafen dürfen dem Betroffenen bei der Strafzumessung und beim Entscheid über den Strafaufschub nicht mehr entgegengehalten werden. |
| **BGE 135 IV 170** | [BGE 135 IV 170 E. 4.5](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-135-IV-170_2009.html#consideration_4.5) | Schwellenwert bei Übertretungen: Eine Eintragung in VOSTRA erfolgt erst bei Bussen von mehr als 5'000 Franken; massgebend ist die tatsächlich ausgesprochene Busse, nicht die Ersatzstrafe. |
| **BGE 149 IV 161** | [BGE 149 IV 161 E. 2.5.1](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-149-IV-161_2023.html#consideration_2.5.1) | Tätigkeitsverbot nach [Art. 67 StGB](/kommentar/stgb/art-067/) zum Schutz von Minderjährigen als massgebliche Grundlage für die Eintragung im Sonderprivatauszug. |
| **BGE 147 IV 471** | [BGE 147 IV 471 E. 5.1.1](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-147-IV-471_2021.html#consideration_5.1.1) | Systematische Differenzierung zwischen Geldstrafe (Vergehen, registrierungspflichtig) und Übertretungsbusse (Übertretung, im Regelfall nicht registrierungspflichtig). |
| **BGE 135 I 71** | [BGE 135 I 71 E. 2.10](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_001_BGE-135-I-71_2009.html#consideration_2.10) | Beachtung der Registerlöschungsfristen durch den Haftrichter: Gelöschte Vorstrafen dürfen nicht zur Begründung des Haftgrundes der Wiederholungsgefahr verwertet werden. |
| **BGE 150 II 308** | [BGE 150 II 308 E. 5.6](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_004_BGE-150-II-308_2024.html#consideration_5.6) | Quervergleich zwischen Berufsaufsichtsregistern (z. B. Anwaltsregister) und dem Strafregister hinsichtlich der Berücksichtigung gelöschter Sanktionen. |
| **BGE 127 IV 122** | [BGE 127 IV 122 E. 3.](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-127-IV-122_2001-05-01.html#consideration_3.) | Schutz des Strafregisters vor Ausspähung durch Dritte: Auszüge über fremde Personen dürfen nicht an Private herausgegeben werden; Amtsgeheimnisschutz nach Art. 320 StGB. |
