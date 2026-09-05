---
name: praxisorientierter-kommentar
description: >-
  Standard für den Stil, Aufbau und die Kasuistik eines praxisorientierten Gesetzeskommentars bei Glossagens nach den Referenzmustern Art. 110 StPO und Art. 336 OR. Gilt immer dann, wenn ein Kommentar ausdrücklich als «praxisorientiert» angefordert oder ausgebaut werden soll. Grundgerüst bleiben stets die abstrakten Tatbestandsmerkmale der kommentierten Norm; die Praxisschilderungen werden entlang dieses Gerüsts gegliedert, nie umgekehrt. Kern: Sehr umfangreiche, plastische Beschreibungen der tatsächlichen Lebenssachverhalte aus publizierten Gerichtsurteilen — sowohl Fälle, in denen die Bestimmung angewandt wurde, als auch Fälle, in denen deren Anwendbarkeit verworfen wurde —, Schwellenwert-Gegenüberstellungen, Kasuistiktabellen, offene Benennung echter Judikaturwidersprüche (ohne Scheinharmonisierung), prozessuale Voraussetzungen und Obliegenheiten sowie — als Schlussabschnitt — adressatenbezogene Praxishinweise. Der Duktus bleibt dabei durchwegs wissenschaftlich-nüchtern (Massstab: Onlinekommentar, Basler und Berner Kommentar); reisserische Einleitungen, Metaphern und Dramatisierungen sind untersagt. Zugespitzt und in direkter Ansprache formuliert wird ausschliesslich im abschliessenden Abschnitt «Praxishinweise».
version: 1.3.0
author: Antigravity Agent
tools:
  - mcp__fedlex-connector__get_article
  - mcp__fedlex-connector__get_law_text
  - mcp__fedlex-connector__search_by_title
  - mcp__fedlex-connector__list_amendments
  - mcp__entscheidsuche__search_by_case_number
  - mcp__entscheidsuche__search
  - mcp__entscheidsuche__fetch_document
metadata:
  glossagens:
    category: legal-commentary-style
    benchmarks: ["content/kommentar/stpo/art-110/_index.md", "content/kommentar/or/art-336/_index.md"]
---

# Leitfaden: Praxisorientierter Gesetzeskommentar

Dieser Skill definiert den massgebenden **Stil**, den **inhaltlichen Aufbau** und die **Kasuistik** für alle Glossagens-Kommentare, die **praxisorientiert** verfasst oder zu einem Praxiskommentar ausgebaut werden sollen.

> **Vorbemerkung I — das Gerüst bleibt dogmatisch.** «Praxisorientiert» beschreibt, *womit* die Kommentierung gefüllt wird, nicht *wie sie gegliedert* ist. Das Gerüst sind und bleiben die abstrakten Tatbestandsmerkmale der kommentierten Norm; die Fallschilderungen hängen an diesem Gerüst. Ein Text, der nach Urteilen, Gerichten oder Fallgeschichten gegliedert ist, ist kein Kommentar, sondern eine Urteilssammlung — siehe Abschnitt 3.

> **Vorbemerkung II — der Duktus bleibt wissenschaftlich.** «Praxisorientiert» ist eine Aussage über den Stoff, nicht über den Ton. Die Sprache folgt dem Massstab der wissenschaftlichen Kommentarliteratur (Onlinekommentar, Basler und Berner Kommentar): nüchtern, präzise, belegt, in der dritten Person. Reisserische Einleitungen, Metaphern, Dramatisierungen und direkte Leseransprache haben in der Kommentierung keinen Platz. Zugespitzt zusammengefasst wird erst im Schlussabschnitt «Praxishinweise» — dort, und nur dort, darf das Wichtigste knapp, adressatenbezogen und in der Befehlsform stehen (siehe Abschnitt 4).

---

## 1. Geltungsbereich und Zweck

Wann immer der Benutzer vorgibt:
- *«schreibe/erstelle den Kommentar praxisorientiert»*
- *«baue Art. X zu einem Praxiskommentar aus»*
- *«im Stil von Art. 110 StPO oder Art. 336 OR»*

gilt **dieser Skill als zwingende Stilleitlinie** ergänzend zu den allgemeinen Workflows von `glossagens-content-creation`.

### Abgrenzung zu Standardkommentaren

| Dimension | Akademischer / Konventioneller Kommentar | Praxisorientierter Kommentar (DIESER SKILL) |
|---|---|---|
| **Duktus / Register** | Wissenschaftlich-nüchtern, unpersönlich, belegorientiert | **Identisch** — wissenschaftlich-nüchtern; zugespitzt und adressierend allein im Schlussabschnitt «Praxishinweise» (siehe Abschnitt 4) |
| **Erkenntnisquelle** | Abstrakt-deduktiv aus Doktrin, Systematik und Gesetzestext | Konkret-induktiv aus tatsächlichen Lebenssachverhalten der Gerichtspraxis — *innerhalb* des dogmatischen Rasters |
| **Gliederung** | Tatbestandsmerkmale, dogmatisch abgehandelt | **Dieselben Tatbestandsmerkmale** als Abschnittsraster — je Merkmal die Kasuistik, die es konkretisiert (nie Gliederung nach Urteilen oder Fallgeschichten) |
| **Urteilsdarstellung** | Schlagwort-Zitat: *«Das Bundesgericht bejahte Missbräuchlichkeit (BGE 131 III 535)»* | **Umfangreiche Sachverhaltserzählung**: Wer, was, welche Vorwürfe, welches Kündigungsschreiben, welche Entlastungsmomente, warum gekippt? |
| **Normgrenzen** | Tatbestandsmerkmale abstrakt umschrieben, ohne Schwellenwert | Jedes Merkmal zusätzlich mit **zweiseitiger Grenzkasuistik** unterlegt: Fälle, in denen es *bejaht*, und Fälle, in denen es *verneint* wurde |
| **Widersprüche** | Scheinharmonisierung («hängt vom Einzelfall ab», feine Sachverhaltsnuancen erfunden) | **Echte Brüche benennen**: Divergenzen zwischen Gerichten/Kammern offen als unvereinbar herausarbeiten |
| **Prozessrealität** | Fokus auf materiellrechtliche Auslegungsfragen | Fokus auf Beweislast, Fristen, Verwirkung, Versehensnachweis und Substanziierungsobliegenheiten |
| **Orientierungshilfe** | Abstrakte Lehrmeinungsstreitigkeiten | Verdichtende **Leitsätze** (`> **Leitsatz.**`) im Text und ein Schlussabschnitt **«Praxishinweise»** mit adressatenbezogenen Handlungsanweisungen (siehe Regel 6 und Abschnitt 6) |
| **Textelement** | Fliessender Prosa-Kommentar | Dichte Kasuistik, Gegenüberstellungstabellen, wörtliche Kernzitate — in derselben nüchternen Sprache |

Die Tabelle stellt **keine** Gegensätze im Ton auf: Sie unterscheidet, *was* der Kommentar enthält, nicht *wie laut* er es sagt. In der sprachlichen Haltung ist der praxisorientierte Kommentar von einem guten wissenschaftlichen Kommentar nicht zu unterscheiden.

---

## 2. Die beiden Referenzmuster (Benchmarks)

Vor dem Verfassen eines praxisorientierten Kommentars sind die beiden Vorzeigekommentare im Repository zu konsultieren:

1. **Art. 110 StPO** (`content/kommentar/stpo/art-110/_index.md`):
   - *Thema*: Formstrenge vs. überspitzter Formalismus bei Eingaben.
   - *Praxis-Stil*: Ausführliche Schilderung realer Gerichtsentscheide (Telefax eines in Deutschland Inhaftierten am Freitagabend; USB-Stick bei Revision; Eingabe mit eingescannter Signatur; E-Mail-Entsiegelungsgesuch der Staatsanwaltschaft; Kasuistik ungebührlicher Rechtsschriften mit Gegenüberstellung extremer Beleidigungen vs. noch zulässiger harter Kritik).
2. **Art. 336 OR** (`content/kommentar/or/art-336/_index.md`):
   - *Thema*: Missbräuchliche Kündigung, verpönte Motive und ungeschriebene Tatbestände.
   - *Praxis-Stil*: Narrative Lebenssachverhalte (WhatsApp-Story eines Seilbahnmitarbeiters mit NS-Pass-Vergleich; Bankvize als Sündenbock nach Millionenveruntreuung eines Dritten; Verdachtskündigung nach anonymer Ombudsfrauen-Meldung und Reichweite von StPO-Garantien; Covid-19-Impfobligatorium bei Flight Attendants; Tabellenvergleich zwischen geschützter und ungeschützter Alterskündigung: 60 J./37 Dienstjahre VR-Präsident vs. 58 J./32 Dienstjahre Sachbearbeiter).

---

## 3. Das Grundgerüst: die abstrakten Tatbestandsmerkmale

**Grundsatz.** Das tragende Gerüst jedes Kommentars sind und bleiben die **abstrakten Tatbestandsmerkmale** der kommentierten Norm — also die einzelnen Voraussetzungen, an die das Gesetz seine Rechtsfolge knüpft, so wie sie sich aus Wortlaut, Systematik und Materialien ergeben. Die Kasuistik ist kein eigenständiger Gliederungspunkt und kein Selbstzweck, sondern die **Füllung dieses Gerüsts**: Jeder geschilderte Lebenssachverhalt steht dort, wo dasjenige Merkmal abgehandelt wird, über dessen Vorliegen er entscheidet.

Der Sinn der Regel: Wer den Kommentar zur Hand nimmt, prüft einen eigenen Fall. Er braucht ein Raster, das er der Reihe nach abarbeiten kann — und an jedem Rasterpunkt die Fälle, die zeigen, wo die Gerichte die Schwelle ziehen. Ein Text, der nach Urteilen, Gerichten oder Fallgeschichten gegliedert ist, zwingt ihn, sich das Raster selbst zu bauen; er ist keine Kommentierung, sondern eine Urteilssammlung.

### 3.1 Merkmalskatalog vor der ersten Zeile Fliesstext

Vor dem Schreiben wird die Norm zerlegt:

1. **Wortlaut verbatim aus Fedlex** holen, Absatz für Absatz (nie aus dem Gedächtnis).
2. **Merkmale herausschälen und in Prüfungsreihenfolge nummerieren**: Geltungsbereich/Anwendbarkeit vor dem Tatbestand; objektive vor subjektiven Merkmalen; Grundtatbestand vor Qualifikation und Privilegierung; Tatbestand vor Rechtsfolge; Ausnahmen und Gegenausnahmen zuletzt. Ungeschriebene Merkmale, die Praxis und Lehre entwickelt haben (z.B. ungeschriebene Missbrauchstatbestände, Kausalität, Verhältnismässigkeit), gehören mit ausdrücklichem Vermerk ihrer Herkunft in denselben Katalog.
3. **Zu jedem Merkmal festhalten**: Wer trägt die Behauptungs- und Beweislast, welches Beweismass gilt (siehe Regel 5)?
4. **Den Katalog als Prüfschema-Tabelle** an den Anfang des Kommentars stellen. Sie ist zugleich das Inhaltsverzeichnis der Kommentierung: Jede Zeile der Tabelle findet sich als Abschnittsüberschrift wieder, in derselben Reihenfolge.

### 3.2 Die Kasuistik folgt dem Merkmalskatalog

- **Ein Abschnitt pro Merkmal.** Die Überschriften benennen Tatbestandsmerkmale, nicht Urteile oder Fallgeschichten.
  - Falsch: *«Die WhatsApp-Story des Seilbahnangestellten»*, *«Der Entscheid BGer 4A_368/2023»*, *«Neuere Rechtsprechung 2024».*
  - Richtig: *«Kündigung wegen Ausübung eines verfassungsmässigen Rechts (Abs. 1 lit. b)»* — die Story steht **darin**.
- **Merkmalssatz vor Fallgeschichte.** Jeder Abschnitt beginnt mit ein bis drei Sätzen abstrakter Dogmatik: was das Merkmal verlangt und woran es sich bemisst. Erst danach folgen die Sachverhalte. Die Leserin muss wissen, wonach sie sucht, bevor sie die Geschichte liest.
- **Rückbindung jeder Schilderung.** Jede Sachverhaltsschilderung schliesst mit dem Satz, welches Merkmal der Entscheid bejaht oder verneint hat — formuliert in der Sprache des Merkmals, nicht bloss im Ergebnis («die Klage wurde abgewiesen» genügt nicht; es muss heissen, an welchem Merkmal sie scheiterte).
- **Grenzkasuistik ist merkmalsbezogen.** Das «angewandt vs. verworfen» aus Regel 2 wird nicht auf die Norm als Ganzes bezogen, sondern auf das einzelne Merkmal. Eine Norm scheitert im Prozess nie «insgesamt», sondern stets an einem bestimmten Merkmal — genau das ist die Information, die der Praktiker braucht.
- **Vollständigkeit des Rasters.** Auch Merkmale, zu denen die Recherche keine plastischen Fälle geliefert hat, erhalten ihren Abschnitt — mit dem ausdrücklichen Vermerk, dass publizierte Praxis dazu fehlt oder sich in Formelzitaten erschöpft. Ein Merkmal darf nie deshalb fehlen, weil es keine gute Geschichte hergibt. Die Lücke ist selbst eine Information: Sie zeigt, wo ein Streitpunkt offen ist.
- **Keine Doppelablage.** Ein Entscheid, der mehrere Merkmale betrifft, wird beim **tragenden** Merkmal ausführlich geschildert; bei den übrigen steht nur ein Querverweis mit dem dort relevanten Satz.
- **Kein Merkmalsproporz nach Materialmenge.** Die Gewichtung folgt der praktischen Bedeutung des Merkmals, nicht der Anzahl gefundener Entscheide. Ein streitanfälliges Merkmal mit drei Entscheiden trägt mehr Text als ein unstreitiges mit dreissig.

> **Grundsatz.** Wer den Kommentar nur quer liest, muss allein an den Überschriften die vollständige Prüfung der Norm ablesen können. Die Fallgeschichten sind das Fleisch — die Tatbestandsmerkmale sind das Skelett. Ohne Skelett fällt der Praxiskommentar zur Anekdotensammlung zusammen.

### 3.3 Beispiel: dieselbe Kasuistik, falsch und richtig aufgehängt

| | Falsch (fallgetrieben) | Richtig (merkmalsgetrieben) |
|---|---|---|
| Überschrift | «Der Fall des Bankvize» | «B. Verpöntes Motiv: Kündigung wegen einer Eigenschaft der anderen Partei (Abs. 1 lit. a)» |
| Einstieg | Sofortige Sachverhaltserzählung | Ein bis drei Sätze: Was verlangt das Merkmal, wer trägt die Beweislast — *dann* der Sachverhalt |
| Abschluss | «Das Bundesgericht wies die Beschwerde ab.» | «Das Merkmal war zu bejahen; die Klage scheiterte erst am **Kausalzusammenhang** — dazu Abschnitt D.» |
| Wirkung | Leser muss aus Geschichten selbst ein Raster bauen | Leser arbeitet sein eigenes Verfahren am Raster ab |

---

## 4. Duktus und Register: wissenschaftlich, nicht werbend

**Grundsatz.** Massstab der Sprache ist die wissenschaftliche Kommentarliteratur — Onlinekommentar, Basler und Berner Kommentar. Der Kommentar beschreibt die Rechtslage; er wirbt nicht für sie, warnt nicht vor ihr und baut keine Spannung auf. Praxisnähe entsteht durch die **Dichte der belegten Sachverhalte**, nicht durch die Temperatur der Sprache.

### 4.1 Was untersagt ist

1. **Reisserische Einleitungen.** Weder der Kommentar als Ganzes noch ein Abschnitt wird über seine Brisanz eingeführt. Ein Abschnitt beginnt mit Regelungsgegenstand, systematischer Stellung und Zweck — nicht mit dem, was schiefgehen kann.
2. **Metaphern und Bilder.** «Brücke zwischen Anklage und Verhandlung», «Verfahrensschicksal», «mit welchen Karten die Parteien an die Hauptverhandlung gehen», «mit leeren Händen dastehen», «Elfenbeinturm», «Klippe», «Falle», «Gegenspieler», «Zweischneide», «der einzige Ausweg».
3. **Dramatisierung und Spannungsbogen.** «Über allem liegt …», «auf den ersten Blick eine blosse Ordnungsvorschrift — in Wahrheit …», rhetorische Fragen, Ausrufe, Ellipsen zur Betonung.
4. **Unbelegte Wertungen.** «krass», «brutal», «verheerend», «schonungslos», «dramatisch». Wertende Aussagen sind zulässig, soweit sie sich aus Entscheid, Materialien oder Lehre belegen lassen oder ausdrücklich als eigene Auffassung gekennzeichnet werden («nach hier vertretener Auffassung»).
5. **Direkte Leseransprache und Befehlsform** in der Kommentierung — «Achten Sie darauf», «prüfen Sie», «vergessen Sie nie». Sie ist dem Schlussabschnitt «Praxishinweise» vorbehalten (Abschnitt 4.3).
6. **Fettauszeichnung als Lautstärkeregler.** Fett kennzeichnet Tatbestandsmerkmale, Rechtsbegriffe und Ergebnisse — nicht die Aufregung des Verfassers.

### 4.2 Plastisch ist nicht dasselbe wie reisserisch

Regel 1 (ausführliche Sachverhaltsschilderung) bleibt uneingeschränkt in Kraft und steht zu diesem Abschnitt nicht in Widerspruch: Erzählt wird der **Sachverhalt** — Funktion, Dienstjahre, Daten, Fristen, Wortlaut der beanstandeten Äusserung, Verfahrensgang. Nicht erzählt wird die **Bedeutung** des Falles für den Leser. Die Details tragen die Anschaulichkeit; die Wertung bleibt sachlich und belegt.

Dasselbe gilt für Regel 3: Eine Judikaturdivergenz wird **präzise benannt und offengelegt**, aber als Meinungs- und Praxisstand referiert, nicht als Konflikterzählung inszeniert.

| | Reisserisch (untersagt) | Wissenschaftlich (verbindlich) |
|---|---|---|
| Einleitung | «Art. 331 StPO ist die Brücke zwischen der Anklage und der mündlichen Verhandlung. Auf den ersten Blick eine blosse Ordnungsvorschrift, in der Praxis ein Verfahrensschicksal: Wer die Frist verpasst, steht mit leeren Händen da.» | «Art. 331 StPO regelt die verfahrensleitende Organisation im Übergangsstadium zwischen der Überweisung der Anklage (Art. 328 ff. StPO) und der erstinstanzlichen Hauptverhandlung. Die Bestimmung bildet die Grundlage für die Vorbereitung des Hauptverfahrens durch die Verfahrensleitung (Art. 61 lit. c StPO).» |
| Abschnittsbeginn | «Abs. 3 ist die zentrale prozessuale Klippe der Norm. Der einzige Ausweg: …» | «Die Ablehnung von Beweisanträgen ist nach Abs. 3 Satz 2 nicht selbständig anfechtbar; als funktionelles Äquivalent gewährleistet das Gesetz das Recht zur erneuten Antragstellung an der Hauptverhandlung.» |
| Normverhältnis | «Art. 65 Abs. 2 StPO ist der Gegenspieler der Nichtanfechtbarkeit.» | «Der fehlenden selbständigen Anfechtbarkeit steht die Befugnis des Gerichts gegenüber, verfahrensleitende Anordnungen nach Art. 65 Abs. 2 StPO jederzeit zu ändern oder zu widerrufen.» |
| Verdichtung im Text | «> **Merksatz für die Verteidigung:** Wer seine Beweisanträge nicht erneuert, hat sie verwirkt — die Nichtanfechtbarkeit ist keine Einladung zur Passivität!» | «> **Leitsatz.** Wird ein von der Verfahrensleitung abgelehnter Beweisantrag an der Hauptverhandlung nicht erneuert, gilt die Rüge im Rechtsmittelverfahren als verwirkt.» |

### 4.3 Wo Zuspitzung erlaubt ist: der Schlussabschnitt «Praxishinweise»

Der Kommentar schliesst — nach den kantonalen Praxisfragen — mit einem Abschnitt **«Praxishinweise»**. Er ist die einzige Stelle, an der das Wichtigste zugespitzt zusammengefasst werden darf: nach Adressatenrollen gegliedert, nummeriert, kurz, in direkter Ansprache und in der Befehlsform.

Es gelten dabei drei Schranken:
- **Nichts Neues.** Jeder Hinweis verdichtet, was in der Kommentierung bereits dogmatisch entwickelt und belegt wurde. Der Abschnitt führt keine Rechtsfrage ein, die vorher nicht behandelt wurde.
- **Jeder Hinweis belegt.** Jede Aussage trägt ihren Entscheid- oder Normverweis mit Link, wie im übrigen Kommentar auch.
- **Zugespitzt heisst nicht unseriös.** Kurz, direkt und handlungsleitend — aber ohne Metaphern, Ausrufezeichen und Übertreibung. Massstab bleibt der Abschnitt «Praxishinweise» der beiden Referenzmuster (Art. 110 StPO, Art. 336 OR).

---

## 5. Die 7 Grundregeln des praxisorientierten Stils

Die folgenden Regeln bestimmen, **wie** die einzelnen Abschnitte des unter Abschnitt 3 aufgestellten Merkmalsrasters ausgefüllt werden. Sie ersetzen dieses Raster nicht und gelten sämtlich innerhalb des Duktus nach Abschnitt 4: Sie verlangen Materialdichte, nicht Lautstärke.

### Regel 1: Narrative Sachverhaltsschilderung aus den Akten

Abstrakte Rechtsregeln sind für die Praxis wenig ergiebig, solange nicht klar ist, auf welche Lebenssachverhalte sie zutreffen. Jeder ausgewertete Entscheid wird deshalb mit seinem **konkreten Lebenssachverhalt** eingeführt.

Erzählt wird dabei der **Sachverhalt**, nicht seine Bedeutung: Details, Daten und Wortlaute tragen die Anschaulichkeit; die rechtliche Würdigung bleibt nüchtern und belegt (Abschnitt 4.2).

#### Was in die Sachverhaltsschilderung gehört:
1. **Die Akteure**: Funktion, Branche, Dienstjahre, Alter, Hierarchiestufe, Rollen (z.B. *«Ein seit 2011 fest angestellter Seilbahn- und Rodelbahnangestellter...»*, *«Ein selbst als Rechtsanwalt tätiger Beschuldigter...»*, *«Die Staatsanwaltschaft Limmattal/Albis...»*).
2. **Der konkrete Konflikt / das Verhalten**: Exakte Zitate der beanstandeten Aussagen, exakter Übermittlungsweg, genaue Daten, Fristen und Zeitabstände (z.B. *«vier Arbeitstage nach der Veröffentlichung»*, *«am Freitagabend um 18.26 Uhr per Telefax»*).
3. **Das Vorgehen der Gegenseite / Behörde**: Wurde verwarnt? Wurde eine Nachfrist gesetzt? Wie begründete das erstinstanzliche Gericht sein Nichteintreten oder seine Abweisung?
4. **Die Weichenstellung des Obergerichts / Bundesgerichts**: Warum genau kippte der Fall? Welche Erwägung gab den Ausschlag?

#### Negativ-Beispiel (abstrakt, verboten):
> Eine Kündigung wegen Äusserungen im privaten Umfeld kann zulässig sein, wenn betriebliche Interessen berührt sind (BGer 4A_368/2023). Auch bei Krankheit ist eine Kündigung nach Fristablauf meist nicht missbräuchlich.

#### Positiv-Beispiel (praxisorientiert, verbindlich):
> **Meinungsäusserung: die WhatsApp-Story eines Seilbahnangestellten**  
> Ein seit 2011 fest angestellter Seilbahn- und Rodelbahnangestellter veröffentlichte Anfang September 2021 auf seinem privaten Mobiltelefon eine dreiteilige WhatsApp-«Story». Im dritten Teil zeigte er das Bild eines «Gesundheitspasses» aus der nationalsozialistischen Zeit samt Hakenkreuz mit der Bemerkung: «Die Geschichte wiederholt sich und wir, die das vorausgesehen hatten, sind die Verschwörungstheoretiker. Leider nicht, kann man dazu sagen.» Der Vorgesetzte schrieb ihm per WhatsApp, extreme Statusmeldungen mit NS-Bezug im Unternehmen nicht zu tolerieren. Am 15. September 2021 kündigte die Arbeitgeberin — sechs Tage bzw. vier Arbeitstage nach der Veröffentlichung — und nannte die Story sowie frühere Verwarnungen (Maskenpflichtmissachtung, Befahren einer gesperrten Piste).  
> **Erster Schritt: Die Äusserung ist geschützt.** Das Kantonsgericht hielt fest, der Vergleich des Corona-Zertifikats mit dem NS-Gesundheitspass sei zwar geschmacklos und schockierend, überschreite aber den Rahmen von Art. 16 Abs. 2 BV nicht ([SG KG BO.2024.11-K3 E. III/4b](https://entscheidsuche.ch/docs/SG_Gerichte/SG_KG_002_BO-2024-11-K3_2024-12-27.pdf)).  
> **Zweiter Schritt: Die Klage scheitert trotzdem.** Weil der Kläger zuvor bereits wegen Sicherheitsverstössen verwarnt worden war, zeigte die Story, dass er Massnahmen bewusst missachtete. Er konnte nicht nachweisen, dass die Kündigung *ohne* die früheren Verwarnungen allein wegen der Äusserung erfolgt wäre ([E. III/5d](https://entscheidsuche.ch/docs/SG_Gerichte/SG_KG_002_BO-2024-11-K3_2024-12-27.pdf)).

---

### Regel 2: Zweiseitige Grenzkasuistik — Angewandt vs. Verworfen

Praktiker lesen einen Kommentar, um die **Grenze des rechtlich Möglichen** auszuloten. Daher müssen zu jedem Streitpunkt zwingend beide Richtungen mit ausführlichen Sachverhalten dargestellt werden:

1. **Anwendungsfälle (Tatbestand bejaht / Klage geschützt / Rechtsfolge ausgelöst)**:
   - Sachverhalte, in denen die Gerichte die Hürde als genommen ansahen.
2. **Verwerfungsfälle (Tatbestand verneint / Anwendbarkeit verworfen / Rechtsfolge verweigert)**:
   - Sachverhalte, in denen eine Partei die Norm anrief, das Gericht aber abwies (weil Schwelle nicht erreicht, Gegenausnahme griff, Kausalität fehlte oder ein Rechtfertigungsgrund vorlag).

#### Der didaktische Zweck:
Durch die Gegenüberstellung von *«Gerade noch geschützt / missbräuchlich / ungebührlich»* und *«Noch zulässig / verworfen»* wird der Schwellenwert der Gerichte greifbar.

**Bezugspunkt ist stets das einzelne Tatbestandsmerkmal**, nicht die Norm als Ganzes (siehe Abschnitt 3.2): Die Gegenüberstellung gehört in denjenigen Abschnitt, dessen Merkmal im geschilderten Verfahren den Ausschlag gab.

---

### Regel 3: Echte Judikaturwidersprüche offenlegen (Verbot der Scheinharmonisierung)

Juristische Urteile stehen nicht immer in eleganter Harmonie zueinander; sie können zueinander in **echtem, unauflösbarem Widerspruch** stehen:
- zwischen verschiedenen Abteilungen oder Kammern desselben Gerichts (z.B. I. öffentlich-rechtliche vs. strafrechtliche Kammer des BGer; verschiedene Zivilkammern eines Obergerichts),
- zwischen der kantonalen Gerichtspraxis (Obergerichte / Kantonsgerichte) und dem Bundesgericht,
- oder im Zeitablauf bei schleichenden oder uneinheitlich vollzogenen Praxisänderungen.

#### Das Verbot der Scheinharmonisierung:
Es ist ein schwerer methodischer Fehler, solche Brüche in der Judikatur **künstlich weg-zuharmonisieren**, indem man behauptet, die Entscheide liessen sich durch vermeintliche Nuancen im Sachverhalt (z.B. minimale Altersunterschiede, Branchenbesonderheiten oder kantonale Herkunft) widerspruchsfrei erklären, obwohl die Gerichte in Wahrheit gegensätzliche rechtliche Massstäbe oder Wertungen angewandt haben.

> **Grundsatz:** Wo Gerichte bei im Kern vergleichbaren Sachverhalten unvereinbare Massstäbe anlegen, wird dieser Widerspruch **offen, präzise und ungeschönt beim Namen genannt** — anstatt ihn mit Scheindifferenzierungen zu übertünchen.

#### Wie Widersprüche darzustellen sind:
1. **Den Konflikt klar benennen**: Explizite Abschnitte wie *«Uneinheitliche Praxis / Judikaturdivergenz»*, *«Gespaltener Massstab»* oder *«Widerspruch zwischen Bundesgericht und kantonaler Praxis»*.
2. **Die unvereinbaren Linien konfrontieren**: Sachverhalte beider Entscheide schildern und zeigen, warum die jeweiligen Begründungen sachlich nicht zusammenpassen.
3. **Keine Scheinerklärungen konstruieren**: Keine Randtatsachen als Erklärung vorschieben, die das Gericht selbst gar nicht als tragend gewertet hat.
4. **Prozessuale Taktik herausarbeiten**:
   - Für die Rechtsmittelpraxis: Ein offener Widerspruch ist der stärkste Hebel, um eine Rechtsfrage von grundsätzlicher Bedeutung zu begründen, eine Plenar- oder Fünferbesetzung (z.B. Art. 23 BGG) zu verlangen oder eine Praxisänderung anzuregen.
   - Für das Instanzgericht: Parteien können gezielt die für sie günstigere Linie unter Hinweis auf die Divergenz einfordern.

---

### Regel 4: Strukturierte Kasuistik- und Kriterientabellen

Wo mehrere Entscheide denselben Tatbestand konkretisieren, fasst eine **Vergleichstabelle** die Sachverhaltskerne und Ergebnisse zusammen.

#### Muster A: Grenzziehungs-Tabelle (z.B. aus Art. 110 StPO)
```markdown
| Sachverhalt / Formulierung | Beurteilung | Entscheid |
|---|---|---|
| Der Bezirksgerichtspräsident sei «womöglich ein schwules Arschloch», «allenfalls ein Rechtsverdreher» | ungebührlich; Relativierungen ändern nichts | [BGer 6B_1272/2017 E. 3.2](https://entscheidsuche.ch/docs/CH_BGer/CH_BGer_006_6B-1272-2017_2018-02-23.html) |
| Vorwurf an zwei Bundesanwälte, sie hätten Gerichte vorsätzlich getäuscht («pour tromper sciemment et volontairement les juges») — ohne jeden Anhaltspunkt | **noch nicht** ungebührlich; unbegründete Kritik bleibt geschützt, solange sachbezogen | [BStGer BB.2020.288 E. 5.3](https://entscheidsuche.ch/docs/CH_BSTG/CH_BSTG_001_BB-2020-288_2021-02-15.pdf) |
```

#### Muster B: Fallvergleichs-Tabelle zweier Leitentscheide (z.B. aus Art. 336 OR)
```markdown
| Kriterium | [BGer 4A_44/2021](https://entscheidsuche.ch/docs/CH_BGer/CH_BGer_004_4A-44-2021_2021-06-02.html) — **nicht** missbräuchlich | [AG OG ZOR.2025.11](https://entscheidsuche.ch/docs/AG_Gerichte/AG_OG_001_ZOR-2025-11_2025-09-01.pdf) — **missbräuchlich** |
|---|---|---|
| Alter / Dienstjahre | 60 Jahre / 37 Jahre | 58 Jahre / 32 Jahre |
| Hierarchiestufe | VR-Mitglied und CEO, Familienmitglied, hoher Lohn | Sachbearbeiter ohne Führung, Normalgehalt |
| Weiterbeschäftigung | faktisch ausgeschlossen | konkret möglich (Stelle per 1.1. neu besetzt) |
| Ergebnis | Kündigung geschützt | Vier Monatslöhne Pönale zugesprochen |
```

---

### Regel 5: Prozessuale Realität — Beweislast, Fristen, Obliegenheiten

Der praxisorientierte Kommentar behandelt die prozessualen Voraussetzungen, an denen Verfahren in der Praxis scheitern, ausdrücklich. Er arbeitet systematisch heraus:

1. **Beweislast und Beweismass**:
   - Wer muss was beweisen? Reicht Glaubhaftmachen oder gilt das Regelbeweismass der vollen Überzeugung?
   - Wie weist man innere Tatsachen nach (z.B. Kündigungsmotiv, Vorsatz, Rechtsmissbrauch)?
2. **Formstrenge und Fristenfalle**:
   - Welche Mängel sind mit Nachfrist heilbar (blosses Versehen) und welche führen zum sofortigen Rechtsverlust (bewusst gewählter Übermittlungsweg, Telefax, unvollständige elektronische Eingabe)?
   - Geltung für Behörden: Trifft Staatsanwaltschaft oder Verwaltung dieselbe Formstrenge wie Private?
3. **Substanziierung und Rügeobliegenheiten**:
   - Welche Tatsachen müssen bereits in der Ersteingabe detailliert dargelegt werden?
   - Was gilt als unzulässiges Nachschieben von Gründen?

---

### Regel 6: Leitsätze im Text — taktische Hinweise erst am Schluss

Verdichtung findet an zwei Stellen statt, in zwei verschiedenen Registern.

#### a) In der Kommentierung: der Leitsatz

Wo die Kasuistik eines Hauptabschnitts eine verdichtbare Regel ergibt, schliesst der Abschnitt mit einem hervorgehobenen **Leitsatz**. Er ist **beschreibend** formuliert — er hält fest, was gilt, nicht was zu tun ist — und bleibt im wissenschaftlichen Duktus (Abschnitt 4). Keine Leseransprache, keine Befehlsform, keine Ausrufezeichen.

```markdown
> **Leitsatz.** Die verfahrensleitende Ablehnung von Beweisanträgen nach Art. 331 Abs. 3 StPO ist eine provisorische Anordnung und begründet für sich allein keinen Anschein der Befangenheit im Sinne von Art. 56 lit. f StPO.
```

Ein Leitsatz wird nicht erzwungen: Ergibt ein Abschnitt keine über die Kommentierung hinausgehende Verdichtung, entfällt er.

#### b) Am Schluss: die Praxishinweise

Handlungsanweisungen — direkte Ansprache, Befehlsform, taktische Zuspitzung — gehören ausschliesslich in den Schlussabschnitt **«Praxishinweise»** (Abschnitt 4.3 und 6). Dort wird das Wichtigste der gesamten Kommentierung nach Adressatenrollen gebündelt:

```markdown
### N. Praxishinweise

**Für die beschuldigte Person und ihre Verteidigung:**

1. Von der Verfahrensleitung abgelehnte Beweisanträge an der Hauptverhandlung ausdrücklich erneuern. Wer sie nicht wiederholt, verliert die Rüge im Rechtsmittelverfahren ([AG OG SBK.2024.132 E. 5.3](https://entscheidsuche.ch/docs/AG_Gerichte/AG_OG_008_SBK-2024-132_2024-05-31.pdf)).
2. Ein Verschiebungsgesuch sofort nach Erhalt der Vorladung einreichen und begründen; ein Gesuch am Vortag der Verhandlung wird regelmässig abgewiesen ([BStGer BB.2026.4](https://entscheidsuche.ch/docs/CH_BSTG/CH_BSTG_001_BB-2026-4_2026-01-21.pdf)).

**Für die Verfahrensleitung:**

1. Die Ablehnung von Beweisanträgen stets kurz begründen; der blosse Verweis auf Art. 331 Abs. 3 StPO genügt der Begründungspflicht nicht.
```

Jeder Hinweis bleibt belegt und verdichtet nur, was die Kommentierung bereits entwickelt hat (Abschnitt 4.3).

> **Übergangsbemerkung.** Ältere Kommentare enthalten inline `> **Merksatz.**`-Blöcke in adressierender Befehlsform (so Art. 336 OR). Wer einen solchen Kommentar überarbeitet, formuliert sie als beschreibende Leitsätze um und verschiebt den handlungsleitenden Gehalt in die Praxishinweise.

---

### Regel 7: Absolutes Grounding & wörtliche Schlüsselerwägungen

Praxiskommentare enthalten niemals erfundene Urteilssachverhalte oder spekulative Sachverhaltsdetails.
- **Volltextrecherche**: Jeder geschilderte Sachverhalt stammt aus einem Urteil, das über `entscheidsuche.ch` oder `mcp.opencaselaw.ch` im Volltext gesichtet wurde.
- **Wörtliche Zitate**: Die entscheidende Begründung des Gerichts wird als Blockzitat (`> «...»`) verbatim übernommen.
- **Exakte Verlinkung**: Verlinkung auf `entscheidsuche.ch` (bzw. opencaselaw-Fallback), bei BGE-Entscheiden wenn möglich mit Erwägungsanker (`#consideration_X.Y`).

---

## 6. Gliederung und Umfang im Page Bundle

Ein praxisorientierter Kommentar wird als vollwertiges Page Bundle angelegt:

```text
content/kommentar/{gesetz}/art-{nr}/
├── _index.md            ← Hauptkommentar mit detaillierter Kasuistik (Branch Bundle)
└── rechtsprechung.md    ← Rechtsprechungsübersicht (mind. 10 strukturierte Entscheide)
```

### Aufbau des Hauptkommentars (`_index.md`)

1. **Frontmatter**:
   - `description`: Erwähnt explizit die Ausrichtung als Praxiskommentar und die wichtigsten Fallgruppen/Kasuistiken — sachlich formuliert, ohne Anpreisung.
   - `tags`: Umfasst spezifische Sachverhalts- und Kasuistik-Schlagworte.
   - `revisions`: Vollständiger Nachweis der ausgewerteten Volltexte und Verifikationen.
2. **Gesetzeswortlaut**:
   - Verbatim nach Fedlex, gegliedert nach Absätzen, mit historischem Gesetzesstand.
   - Bei komplexen Normen: Eine vorangestellte Übersichtstabelle («Die Tatbestände auf einen Blick»).
3. **Überblick und Bedeutung**:
   - 1–2 Absätze zu systematischer Stellung, Regelungsgegenstand und Zweck der Norm sowie zu den Interessen, die sie ausgleicht. Keine Hinführung über die praktische Brisanz, keine Metaphern (Abschnitt 4.1).
   - **Prüfschema / Schichten-Tabelle**: der Merkmalskatalog nach Abschnitt 3.1 — Prüfungsreihenfolge der Tatbestandsmerkmale und Beweislast je Merkmal. Diese Tabelle ist zugleich das Inhaltsverzeichnis der nachfolgenden Kommentierung.
   - Zentrale Leitentscheide im wörtlichen Zitat.
4. **Kommentierung (Abschnitte A, B, C...)**:
   - Gliederung **entlang der Tatbestandsmerkmale** in der Reihenfolge des Prüfschemas (siehe Abschnitt 3.2) — nicht nach Urteilen, Gerichten, Jahrgängen oder Fallgeschichten. Die Absatzgliederung der Norm ist dabei nur der Ausgangspunkt: Trägt ein Absatz mehrere Merkmale, erhält jedes seinen eigenen Abschnitt.
   - Jeder Abschnitt enthält, in dieser Reihenfolge:
     - **Was das Merkmal verlangt** — dogmatische Grundlinie in ein bis drei Sätzen, vor jeder Fallschilderung (siehe Abschnitt 3.2).
     - **Ausführliche Sachverhalte konkreter Urteile** (siehe Regel 1), je mit Rückbindung an das Merkmal.
     - **Gegenüberstellung angewandter vs. verworfener Fälle — bezogen auf dieses Merkmal** (siehe Regel 2).
     - **Offenlegung echter Judikaturwidersprüche ohne Scheinharmonisierung** (siehe Regel 3).
     - **Kasuistik- oder Vergleichstabelle** (siehe Regel 4).
     - **Leitsatz**, wo die Kasuistik eine verdichtbare Regel ergibt — beschreibend, nicht handlungsleitend (siehe Regel 6 lit. a).
5. **Kantonale Praxisfragen**:
   - Mindestens 1–2 konkrete Streitpunkte oder Verfahrensdivergenzen kantonaler Gerichte (z.B. Obergerichte ZH, BE, SG, AG, LU).
6. **Praxishinweise** (Schlussabschnitt, zwingend):
   - Letzter Abschnitt der Kommentierung, unmittelbar vor den Verweisen auf Rechtsprechung und Literatur — als fortlaufend bezeichneter Abschnitt (z.B. `### H. Praxishinweise`).
   - Gliederung **nach Adressatenrollen** in fetten Zwischentiteln, je Rolle eine nummerierte Liste: `**Für die beschuldigte Person und ihre Verteidigung:**`, `**Für die Privatklägerschaft:**`, `**Für die Strafverfolgungsbehörden:**`, `**Für die Verfahrensleitung:**` — bzw. die entsprechenden Rollen des jeweiligen Rechtsgebiets.
   - Hier — und nur hier — sind kurze, zugespitzte Sätze in direkter Ansprache und Befehlsform zulässig; das Wichtigste der gesamten Kommentierung wird in dieser Form zusammengefasst (Abschnitt 4.3).
   - Jeder Hinweis trägt seinen Entscheid- oder Normverweis mit Link und verdichtet ausschliesslich bereits Kommentiertes; keine neuen Rechtsfragen, keine unbelegten Empfehlungen.
   - Massstab sind die Abschnitte «Praxishinweise» der beiden Referenzmuster (Art. 110 StPO Ziff. H; Art. 336 OR Ziff. M).

---

## 7. Qualitäts-Checkliste für den praxisorientierten Kommentar

Vor dem Commit ist der geschriebene Text gegen folgende Punkte zu prüfen:

- [ ] **Merkmalsraster vorhanden**: Beruht die Gliederung auf den abstrakten Tatbestandsmerkmalen der Norm in ihrer Prüfungsreihenfolge — und benennen die Abschnittsüberschriften Merkmale statt Urteile, Gerichte oder Fallgeschichten?
- [ ] **Prüfschema deckungsgleich**: Findet sich jede Zeile der einleitenden Prüfschema-Tabelle als Abschnitt der Kommentierung wieder, in derselben Reihenfolge — und umgekehrt?
- [ ] **Kein Merkmal ausgelassen**: Ist auch jedes Merkmal abgehandelt, zu dem keine plastische Kasuistik gefunden wurde — mit ausdrücklichem Vermerk der fehlenden Praxis?
- [ ] **Dogmatik vor Kasuistik**: Beginnt jeder Abschnitt mit dem, was das Merkmal verlangt, bevor der erste Sachverhalt erzählt wird — und ist jede Schilderung an das Merkmal rückgebunden (nicht bloss ans Ergebnis)?
- [ ] **Sachverhaltstiefe**: Werden die Urteile als konkrete Lebenssachverhalte mit Berufsbezeichnungen, Dienstjahren, Verhaltensweisen, Datumsangaben und Parteivorbringen geschildert (keine Einzeiler-Zitate)?
- [ ] **Doppelte Kasuistik**: Sind zu den Hauptstreitpunkten sowohl Fälle enthalten, in denen das Gericht die Norm angewandt hat, als auch Fälle, in denen es die Anwendung verworfen hat?
- [ ] **Widersprüche offengelegt**: Wurden echte Judikaturdivergenzen und Widersprüche zwischen Gerichten, Kammern oder im Zeitablauf klar benannt, anstatt sie künstlich über feine Sachverhaltsunterschiede wegzuerklären?
- [ ] **Tabellarische Vergleiche**: Gibt es mindestens eine strukturierte Tabelle, die Grenzfälle oder gegensätzliche Gerichtsentscheide nebeneinanderstellt?
- [ ] **Prozessuale Voraussetzungen**: Werden Beweislast, Fristen, Verwirkung, Versehensnachweis oder Substanziierungsobliegenheiten explizit thematisiert?
- [ ] **Wissenschaftlicher Duktus**: Ist der Text durchgehend nüchtern, unpersönlich und belegt — ohne reisserische Einleitung, Metaphern («Brücke», «Klippe», «Verfahrensschicksal», «Gegenspieler»), Dramatisierung, rhetorische Fragen oder unbelegte Wertungen (Abschnitt 4.1)?
- [ ] **Sachliche Hinführung**: Führt der Kommentar — und jeder Abschnitt — über Regelungsgegenstand, Systematik und Zweck ein statt über die praktische Brisanz?
- [ ] **Leitsätze beschreibend**: Halten die hervorgehobenen `> **Leitsatz.**`-Blöcke fest, *was gilt*, statt *was zu tun ist* — ohne Leseransprache und Befehlsform?
- [ ] **Praxishinweise am Schluss**: Gibt es den zwingenden Schlussabschnitt «Praxishinweise», nach Adressatenrollen gegliedert und nummeriert — und ist jeder Hinweis belegt sowie in der Kommentierung bereits entwickelt (Abschnitt 4.3 und 6.6)?
- [ ] **Zuspitzung nur dort**: Findet sich direkte Ansprache, Befehlsform und taktische Zuspitzung ausschliesslich in den Praxishinweisen und nirgends in der Kommentierung?
- [ ] **Volltext-Verifikation**: Ist jeder Sachverhalt und jedes wörtliche Zitat gegen das Originalurteil auf `entscheidsuche.ch` abgeglichen (keine Halluzinationen)?
- [ ] **Schweizer Rechtschreibung**: Durchgehend kein Eszett («ss»), korrekte Schweizer Rechtsterminologie.
