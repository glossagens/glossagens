---
title: "Siegelungsrecht: Schutzgründe, Beschlagnahmeverbote und Verfahren"
date: 2026-10-24
lastmod: 2026-10-24
description: "Strafprozessuale Siegelung und Entsiegelung nach Art. 248 und 248a StPO: Beschlagnahme- und Verwertungsverbote nach Art. 264 StPO, Wegfall von Geschäftsgeheimnissen seit der Revision 2024, Verfahrensablauf, gerichtliche Triage und Rechtsmittelweg."
tags: ["Strafprozess", "Siegelung", "Entsiegelung", "Zwangsmassnahmen", "Beschlagnahmeverbot", "Verwertungsverbot", "Anwaltsgeheimnis", "Berufsgeheimnis", "Privatsphäre", "Zwangsmassnahmengericht"]
typ: verfahren
kurz: "Macht eine betroffene Person bei einer Sicherstellung geltend, Aufzeichnungen oder Gegenstände unterlägen einem gesetzlichen Beschlagnahmeverbot nach Art. 264 StPO, sind diese unverzüglich zu siegeln und dürfen von den Strafbehörden weder eingesehen noch verwertet werden. Das Siegelungsbegehren muss innert drei Tagen gestellt werden. Hält die Staatsanwaltschaft am Zugriff fest, hat sie innert 20 Tagen beim Zwangsmassnahmengericht ein Entsiegelungsgesuch einzureichen, das im summarischen Verfahren über die Schutzgründe (Berufsgeheimnisse, Anwaltskorrespondenz, überwiegende Privatgeheimnisse) entscheidet."
sachgebiete: [strafprozess.zwangsmassnahmen]
normen:
  - { gesetz: stpo, art: art-248 }
  - { gesetz: stpo, art: art-248a }
  - { gesetz: stpo, art: art-264 }
  - { gesetz: stpo, art: art-141 }
  - { gesetz: stpo, art: art-171 }
  - { gesetz: stpo, art: art-197 }
stichworte: ["Siegelung", "Entsiegelung", "Siegelungsverfahren", "Entsiegelungsverfahren", "Zwangsmassnahmengericht", "Beschlagnahmeverbot", "Beweisverwertungsverbot", "Anwaltsgeheimnis", "Berufsgeheimnis", "Privatgeheimnis", "Datenspiegelung", "Substanziierungsobliegenheit", "Triage"]
agent_verified: true
revisions:
  - date: 2026-10-24
    by: "Antigravity"
    model: "gemini-3.8-flash"
    mcp_verified: true
    note: "Erstfassung nach Skill glossagens-themen (Typ verfahren). Normtexte Art. 248, 248a und 264 StPO per {{< wortlaut >}} aus der Fedlex-Konsolidierung (scripts/wortlaut.py). Alle 13 Leitentscheide als HTML-Volltext von entscheidsuche.ch verifiziert; Erwägungsnummern, Anker und wörtliche Zitate mit pruefen.py und build-check.sh abgeglichen."
---

## Überblick {#ueberblick}

Das **Siegelungsrecht** gemäss [Art. 248](/kommentar/stpo/art-248/) und [Art. 248a StPO](/kommentar/stpo/art-248a/) bildet das zentrale Schutzinstrument der Strafprozessordnung gegen voreilige, unverhältnismässige oder gesetzwidrige staatliche Eingriffe in geschützte Geheimnisse bei der Durchsuchung von Schriftstücken, elektronischen Datenträgern und Datenspeichern. Wird die Siegelung verlangt, tritt ein sofortiges und absolutes behördliches Zugriffs-, Einsichts- und Verwertungsverbot in Kraft.

Wie das Bundesgericht in ständiger Rechtsprechung festhält,
> «hat im Entsiegelungsverfahren nicht die Untersuchungsbehörde, sondern, allenfalls unter Beizug einer sachverständigen Person, das Zwangsmassnahmengericht zu prüfen, ob schutzwürdige Geheimnisinteressen oder andere gesetzliche Entsiegelungshindernisse einer Durchsuchung entgegenstehen».
>
> — [BGE 148 IV 221](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-148-IV-221_2022.html#consideration_2.3) E. 2.3

Das Siegelungsverfahren bezweckt den lückenlosen Grundrechtsschutz (Art. 13 BV, Art. 8 EMRK): «Dies dient namentlich der Verhinderung von Zufallsfunden sowie der Wahrung der unter verfassungsrechtlichem Schutz stehenden Privat- und Geheimsphäre gemäss Art. 13 BV» ([BGE 148 IV 221](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-148-IV-221_2022.html#consideration_2.3) E. 2.3).

Mit der am 1. Januar 2024 in Kraft getretenen Revision der Strafprozessordnung (AS 2023 468; BBl 2019 6697) hat der Gesetzgeber das Verfahren grundlegend neu geordnet und gestrafft:
- Die materiellen Schutzgründe wurden in [Art. 248 Abs. 1 StPO](/kommentar/stpo/art-248/) ausdrücklich und abschliessend auf die gesetzlichen Beschlagnahmeverbote nach [Art. 264 StPO](/kommentar/stpo/art-264/) verengt ([BGE 151 IV 30](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-151-IV-30_2025.html#consideration_2.4) E. 2.4). Allgemeine Geschäftsgeheimnisse oder das Bankkundengeheimnis berechtigen seither nicht mehr zur Siegelung.
- In [Art. 248a StPO](/kommentar/stpo/art-248a/) wurde ein eigenständiger Verfahrensartikel geschaffen, der kurze, nicht erstreckbare Fristen sowie eine gesetzliche Rückzugsfiktion bei Stillschweigen (Art. 248a Abs. 3 StPO) normiert.
- Bei der technischen Beweissicherung hat das Bundesgericht die strenge Praxis zur Datenspiegelung weiterentwickelt: Bei unmittelbar drohendem Datenverlust dürfen Strafverfolgungsbehörden Mobiltelefone vor der Siegelung durch eine unabhängige forensische Fachperson sichern lassen ([BGE 152 IV 107](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-152-IV-107_2026.html#consideration_5.7.8) E. 5.7.8).

## Rechtsgrundlagen {#rechtsgrundlagen}

Das Zusammenspiel zwischen dem verfahrensrechtlichen Schutz der Siegelung und den materiellen Beschlagnahmeverboten ergibt sich aus den folgenden Bestimmungen der Schweizerischen Strafprozessordnung:

{{< wortlaut gesetz="stpo" art="art-248" >}}

{{< wortlaut gesetz="stpo" art="art-248a" >}}

{{< wortlaut gesetz="stpo" art="art-264" >}}

## Die Beschlagnahme- und Verwertungsverbote (Schutzgründe) {#beschlagnahme-und-verwertungsverbote}

Die Siegelung ist kein Selbstzweck und schützt nicht vor der Strafverfolgung an sich. «Das blosse Motiv, dass eine Person […] strafprozessuale Beweiserhebungen möglichst unterbinden möchte, begründet für sich allein noch kein […] rechtlich geschütztes Geheimnisinteresse im Sinne von Art. 248 Abs. 1 StPO» ([BGE 144 IV 74](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-144-IV-74_2018.html#consideration_2.6) E. 2.6).

Seit der Revision vom 1. Januar 2024 ist der Katalog der zulässigen Siegelungsgründe in [Art. 248 Abs. 1 StPO](/kommentar/stpo/art-248/) akzessorisch an die Beschlagnahmeverbote von [Art. 264 StPO](/kommentar/stpo/art-264/) gebunden.

### Die abschliessende Beschränkung auf Art. 264 StPO {#beschraenkung-auf-art-264}

Unter dem bis Ende 2023 geltenden Recht konnten Betroffene neben Zeugnisverweigerungsrechten auch «andere Gründe» – namentlich Fabrikations- und Geschäftsgeheimnisse sowie das Bankgeheimnis – anrufen. Diesen weiten Geheimnisbegriff hat das Parlament bewusst beseitigt:

> «Der Bundesrat hatte in seiner Botschaft samt Entwurf noch vorgeschlagen, dass es Betroffenen ermöglicht werden sollte, auch "Fabrikations- und Geschäftsgeheimnisse" als Entsiegelungshindernis anzurufen und glaubhaft zu machen […]. Der Nationalrat ist diesem Vorschlag jedoch nicht gefolgt. Stattdessen hat er in seiner Revisionsvorlage […] die im Entsiegelungsverfahren zu schützenden Geheimnisrechte ausdrücklich auf die Beschlagnahmegründe von Art. 264 StPO eingeschränkt».
>
> — [BGE 151 IV 30](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-151-IV-30_2025.html#consideration_2.4) E. 2.4

Das Bundesgericht hat diese Rechtsprechung mehrfach bekräftigt: Gesetzlich geschützte Geheimnisse im Sinne von Art. 173 Abs. 2 StPO (Geschäfts-, Fabrikations-, Steuer- und Bankgeheimnisse) begründen keinen Anspruch auf Siegelung mehr ([BGE 151 IV 175](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-151-IV-175_2025.html#consideration_2.4.2) E. 2.4.2). Werden ausschliesslich solche Geheimnisse vorgebracht, ist auf das Siegelungsbegehren nicht einzutreten bzw. das Entsiegelungsgesuch ohne Weiteres gutzuheissen.

### Anwaltskorrespondenz und Verteidigerprivileg {#anwaltsgeheimnis}

Den stärksten, absoluten Schutz geniessen Gegenstände und Unterlagen aus dem Verkehr der beschuldigten Person mit ihrer Verteidigung ([Art. 264 Abs. 1 lit. a StPO](/kommentar/stpo/art-264/)) sowie Gegenstände und Unterlagen aus dem Verkehr einer anderen Person mit ihrer Anwältin oder ihrem Anwalt, sofern die Anwaltschaft zur Vertretung vor schweizerischen Gerichten befugt ist ([Art. 264 Abs. 1 lit. d StPO](/kommentar/stpo/art-264/) i.V.m. Art. 171 StPO).

- **Absolutes Beschlagnahmeverbot**: Verteidigerunterlagen und Anwaltskorrespondenz unterliegen einem absoluten Beschlagnahme- und Verwertungsverbot, ungeachtet des Aufbewahrungsortes oder des Erstellungszeitpunkts ([Art. 264 Abs. 1 StPO](/kommentar/stpo/art-264/)).
- **Voraussetzung**: Der Anwalt oder die Anwältin darf im gleichen Sachzusammenhang nicht selber als beschuldigte Person geführt werden ([BGE 138 IV 225](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-138-IV-225_2012.html#consideration_6.1) E. 6.1). Ein beschuldigter Anwalt kann untersuchungsrelevante Unterlagen dem Zugriff der Behörden nicht dadurch entziehen, dass er Bürokollegen oder Substituten vorschiebt.

### Berufsgeheimnisse und Zeugnisverweigerungsrechte {#berufsgeheimnisse}

Nach [Art. 264 Abs. 1 lit. c StPO](/kommentar/stpo/art-264/) dürfen Unterlagen aus dem Verkehr der beschuldigten Person mit zeugnisverweigerungsberechtigten Berufsgeheimnisträgern nach Art. 170–173 StPO nicht beschlagnahmt werden:
- **Medizinalpersonen**: Ärztinnen und Ärzte (Art. 171 StPO). Ist die Ärztin oder der Arzt selbst beschuldigt (z.B. wegen Widerhandlung gegen das Heilmittelgesetz), besteht zwar kein absolutes Beschlagnahmeverbot, das Zwangsmassnahmengericht muss jedoch zum Schutz unbeteiligter Patienten eine Triage durchführen und für die Untersuchung unentbehrliche Patientendaten vor der Freigabe anonymisieren ([BGE 141 IV 77](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-141-IV-77_2015.html#consideration_5.5.1) E. 5.5.1).
- **Geistliche und Notare**: Art. 171 Abs. 1 StPO.
- **Quellenschutz für Medienschaffende**: Nach Art. 172 StPO i.V.m. [Art. 264 Abs. 1 lit. c StPO](/kommentar/stpo/art-264/) sind Quellen und Recherchematerial von Medienschaffenden geschützt. Das Bundesgericht legt diesen Schutz weit aus: So
  > «fallen unter die im Sinne von Art. 172 Abs. 1 StPO "befassten" Personen nicht nur die Journalisten im eigentlichen Sinn, sondern sämtliche Personen, die in beliebiger Weise, […] auch nur mittelbar, an der Medienproduktion beteiligt sind. Der Begriff der "Hilfspersonen" ist entsprechend weit zu verstehen».
  >
  > — [BGE 151 IV 153](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-151-IV-153_2025.html#consideration_4.1.1) E. 4.1.1
  
  Dieser Quellenschutz greift auch dann, wenn die Daten auf den Geräten einer beschuldigten Drittperson (z.B. eines Informanten oder Kommunikationschefs) sichergestellt werden.

### Persönliche Aufzeichnungen und Privatsphäre {#privatsphaere}

[Art. 264 Abs. 1 lit. b StPO](/kommentar/stpo/art-264/) schützt persönliche Aufzeichnungen und Korrespondenz der beschuldigten Person (Tagebücher, private Fotos, Chats, Beziehungsnachrichten), allerdings nur unter einer gesetzlichen Interessenabwägung: Das Interesse am Schutz der Persönlichkeit (Art. 13 BV) muss das Strafverfolgungsinteresse überwiegen.

In der Praxis betrifft dies fast ausnahmslos sichergestellte Smartphones und private Computer. Das Bundesgericht hat dazu in zwei Grundsatzentscheiden geklärt:
1. **Kein absoluter Schutz**: «Dementsprechend ist ohne Weiteres davon auszugehen, dass bei der (vollständigen) Durchsuchung von privat genutzten Smartphones persönliche Aufzeichnungen und Korrespondenz im Sinne von Art. 264 Abs. 1 lit. b StPO tangiert sind» ([BGE 151 IV 344](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-151-IV-344_2025.html#consideration_2.7) E. 2.7). Dies genügt für sich allein jedoch nicht: «Persönliche Aufzeichnungen und Korrespondenz der beschuldigten Person sind wie gesehen gerade nicht absolut geschützt, sondern nur dann, wenn das Interesse am Schutz ihrer Persönlichkeit das Strafverfolgungsinteresse überwiegt» ([BGE 151 IV 344](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-151-IV-344_2025.html#consideration_2.7) E. 2.7).
2. **Systemimmanente Sichtung nicht relevanter Daten**: Bei der Prüfung der Geeignetheit ist das Gerät als Gesamtes zu betrachten: «Es liegt in der Natur der Sache, dass bei der Durchsuchung von Aufzeichnungen und Gegenständen auch Inhalte gesichtet werden, die sich in der Folge für die Untersuchung als bedeutungslos erweisen» ([BGE 151 IV 350](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-151-IV-350_2025.html#consideration_2.5.3) E. 2.5.3).
3. **Schwere der Straftat**: «Einerseits kann die Untersuchung Straftaten zum Gegenstand haben, die derart schwer wiegen, dass das öffentliche Interesse an ihrer Aufklärung allfällige Interessen der beschuldigten Person am Schutz ihrer persönlichen Daten grundsätzlich ohne Weiteres überwiegt» ([BGE 151 IV 350](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-151-IV-350_2025.html#consideration_2.5.4) E. 2.5.4).

### Schutz vor Selbstbelastung (Nemo tenetur) {#nemo-tenetur}

Der strafprozessuale Grundsatz *nemo tenetur se ipsum accusare* (Art. 113 Abs. 1 StPO; Art. 14 Abs. 3 lit. g IPBPR; Art. 6 Ziff. 1 EMRK) besagt, dass die beschuldigte Person nicht aktiv zu ihrer eigenen Überführung beitragen muss ([BGE 142 IV 207](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-142-IV-207_2016.html#consideration_8.3) E. 8.3).
- **Passives Dulden**: Der Schutz entbindet nicht von der Pflicht, die Durchsuchung und Beschlagnahme von Beweismitteln zu dulden, die unabhängig vom Willen der Person existieren (Urkunden, E-Mails, Mobiltelefone).
- **Passwörter und PIN-Codes**: Die beschuldigte Person kann nicht gezwungen werden, PIN-Codes oder Verschlüsselungspasswörter offenzulegen ([BGE 148 IV 221](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-148-IV-221_2022.html#consideration_2.2) E. 2.2). Die Weigerung hindert die Behörden jedoch nicht daran, die Geräte durch forensische Methoden zu entsperren.

---

## Phasen des Verfahrens im Überblick {#verfahrensablauf}

Das Verfahren nach [Art. 248](/kommentar/stpo/art-248/) und [Art. 248a StPO](/kommentar/stpo/art-248a/) gliedert sich in vier zeitlich streng getaktete Abschnitte:

| Phase | Zuständige Behörde | Frist | Gegenstand / Handlung | Rechtsmittel |
|---|---|---|---|---|
| **1. Sicherstellung & Siegelung** | Polizei / Staatsanwaltschaft | Sofort oder innert 3 Tagen | Vorbringen des Siegelungsbegehrens durch die Inhaberin/den Inhaber ([Art. 248 Abs. 1 StPO](/kommentar/stpo/art-248/)); Information berechtigter Dritter (3 Tage, Abs. 2) | Keine Beschwerde an kantonale Instanz; ZMG-Verfahren abwarten |
| **2. Entsiegelungsgesuch** | Staatsanwaltschaft | 20 Tage seit Siegelung ([Art. 248 Abs. 3 StPO](/kommentar/stpo/art-248/)) | Gesuch an das Zwangsmassnahmengericht (ZMG); Begründung von Tatverdacht und Untersuchungsrelevanz | Bei Fristversäumnis: Rückgabe der Aufzeichnungen |
| **3. Gerichtsverfahren & Triage** | Zwangsmassnahmengericht (ZMG) | 10 Tage Frist für Stellungnahme ([Art. 248a Abs. 3 StPO](/kommentar/stpo/art-248a/)); Entscheid innert 10 Tagen (Abs. 4) bzw. Verhandlung innert 30 Tagen (Abs. 5) | Substanziierung der Schutzgründe durch Berechtigte; Stillschweigen = Rückzug; Sichtung, Ausscheidung und Triage | Gehörsgewährung; Vorbereitung des Endentscheids |
| **4. Entscheid & Vollzug** | Zwangsmassnahmengericht / Sachrichter | Unverzüglich nach Spruchreife ([Art. 248a Abs. 4/5 StPO](/kommentar/stpo/art-248a/)) | Endgültiger Entscheid des ZMG über Entsiegelung, Teildurchsuchung oder Rückgabe | Beschwerde an das BGer ([Art. 78 ff. BGG](https://www.fedlex.admin.ch/eli/cc/2006/218/de#art_78)) nur bei nicht wieder gutzumachendem Nachteil ([Art. 93 Abs. 1 lit. a BGG](https://www.fedlex.admin.ch/eli/cc/2006/218/de#art_93)) |

---

## Phase 1: Sicherstellung und Siegelungsbegehren {#phase-1-sicherung-und-siegelungsbegehren}

### Legitimation: Inhaber und berechtigte Dritte {#legitimation}

Berechtigt zur Verlangung der Siegelung ist primär die **Inhaberin oder der Inhaber** der sichergestellten Gegenstände oder Daten ([Art. 248 Abs. 1 StPO](/kommentar/stpo/art-248/)), also diejenige Person, bei der die Zwangsmassnahme vollzogen wird (Gewahrsamsinhaber).

Ist die Inhaberin oder der Inhaber nicht identisch mit der am Geheimnis berechtigten Person (z.B. ein E-Mail-Provider, Treuhänder, Arbeitgeber oder eine Bank), gilt folgende Neuregelung per 1. Januar 2024:
- Die Strafbehörde muss der berechtigten Person Gelegenheit geben, innert drei Tagen die Siegelung zu verlangen, sobald sie feststellt, dass Inhaber und Berechtigter auseinanderfallen ([Art. 248 Abs. 2 StPO](/kommentar/stpo/art-248/)).
- Im gerichtlichen Verfahren wiederholt sich dieser Schutz: Stellt das Gericht nach Eingang des Gesuchs fest, dass eine Drittperson berechtigt ist, informiert es diese und setzt eine Frist ([Art. 248a Abs. 2 StPO](/kommentar/stpo/art-248a/)).

### Frist und Form {#frist-und-form}

Das Siegelungsbegehren ist nach [Art. 248 Abs. 1 StPO](/kommentar/stpo/art-248/) **innert drei Tagen seit der Sicherstellung** vorzubringen. Es kann unmittelbar mündlich bei der Durchsuchung zu Protokoll gegeben oder innert der dreitägigen Bedenkfrist schriftlich bei der Verfahrensleitung eingereicht werden. Nach Ablauf der Frist ist das Siegelungsrecht verwirkt; die Behörde darf die Aufzeichnungen ohne Weiteres durchsuchen.

### Gegenstand der Siegelung: Ausschluss reiner Sachbeweise {#gegenstand-der-siegelung}

Der Siegelung unterliegen ausschliesslich Schriftstücke, Aufzeichnungen und elektronische Datenträger ([Art. 246 StPO](/kommentar/stpo/art-246/)), die dem Geheimnisschutz zugänglich sind.
- Reines Sachgut wie mutmassliche Betäubungsmittel, Falschgeld, Tatwerkzeuge, Waffen oder Bargeld unterliegt nicht der Siegelung.
- Diese Gegenstände sind keine Aufzeichnungen, sondern direkt nach [Art. 263 StPO](/kommentar/stpo/art-263/) zu beschlagnahmen und spurentechnisch zu untersuchen ([BGE 144 IV 74](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-144-IV-74_2018.html#consideration_2.6) E. 2.6). Ein auf solche Gegenstände bezogenes Siegelungsbegehren ist unzulässig.

### Das behördliche Inzisionsverbot und die Datenspiegelung {#inzisionsverbot-datenspiegelung}

Sobald die Siegelung verlangt wird (oder während der dreitägigen Bedenkfrist), gilt: «Während dieser Frist und nach einer allfälligen Siegelung darf die Strafbehörde die Aufzeichnungen und Gegenstände weder einsehen noch verwenden» ([Art. 248 Abs. 1 Satz 3 StPO](/kommentar/stpo/art-248/)).

Zur technischen Umsetzung bei Mobiltelefonen und Computern hat sich die Rechtsprechung grundlegend gewandelt:
- **Ausgangspunkt BGE 148 IV 221**: Das Bundesgericht hatte 2022 entschieden, dass die Strafbehörde jeglichen Realakt an den Geräten (inklusive Entsperrung und Erstellung einer forensischen Arbeitskopie/Spiegelung) zu unterlassen habe; Datenspiegelungen durften ausschliesslich durch das ZMG angeordnet werden.
- **Praxisänderung durch BGE 152 IV 107**: Angesichts automatischer Löschroutinen und flüchtiger Speicher droht bei Mobiltelefonen fast immer ein Beweisverlust. Wie das Bundesgericht erwog:
  > «wäre ein Zuwarten mit der Datenspiegelung bis zum Ablauf der in Art. 248 Abs. 1 StPO normierten Bedenkfrist von drei Tagen zwangsläufig mit einem erheblichen und irreversiblen Datenverlust verbunden».
  >
  > — [BGE 152 IV 107](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-152-IV-107_2026.html#consideration_5.7.8) E. 5.7.8
  
  Daher dürfen die Strafverfolgungsbehörden bei unmittelbar drohendem Datenverlust eine vorsorgliche Datenspiegelung durch eine sachverständige Person (z.B. IT-Forensiker der Polizei) anordnen. Voraussetzung ist jedoch zwingend, «dass die mit der Datensicherung betrauten forensischen Sachverständigen später nicht auch in die eigentliche Ermittlungstätigkeit des konkreten Strafverfahrens eingebunden werden dürfen» ([BGE 152 IV 107](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-152-IV-107_2026.html#consideration_5.7.8) E. 5.7.8). Die erstellte Spiegelungskopie ist unverzüglich mitzuversiegeln.

---

## Phase 2: Das Entsiegelungsgesuch der Strafbehörde {#phase-2-entsiegelungsgesuch}

### Die 20-tägige Verwirkungsfrist {#20-tage-frist}

Will die Strafverfolgungsbehörde Einsicht in die versiegelten Unterlagen nehmen, muss sie innert **20 Tagen seit der Siegelung** ein schriftliches Entsiegelungsgesuch stellen ([Art. 248 Abs. 3 StPO](/kommentar/stpo/art-248/)).

- Die Frist ist eine gesetzliche Verwirkungsfrist und nicht erstreckbar.
- Verpasst die Staatsanwaltschaft die Frist, fällt die Berechtigung zur Durchsuchung dahin. Die gesiegelten Gegenstände und Datenträger sind der Inhaberin oder dem Inhaber unverzüglich und ohne inhaltliche Prüfung zurückzugeben ([Art. 248 Abs. 3 StPO](/kommentar/stpo/art-248/)).

### Zuständigkeit {#zustaendigkeit}

Gemäss [Art. 248a Abs. 1 StPO](/kommentar/stpo/art-248a/) entscheidet:
- Im Vorverfahren und im Verfahren vor dem erstinstanzlichen Gericht: das **Zwangsmassnahmengericht (ZMG)** am Sitz der untersuchenden Staatsanwaltschaft.
- In den anderen Fällen (z.B. im Berufungsverfahren): die **Verfahrensleitung des Gerichts**, bei dem der Fall hängig ist.

### Begründungsanforderungen der Staatsanwaltschaft {#begruendung-der-staatsanwaltschaft}

Im Entsiegelungsgesuch darf die Staatsanwaltschaft nicht bloss pauschal auf die Verfahrensakten verweisen. Sie muss darlegen:
1. Den hinreichenden Tatverdacht auf ein konkretes Verbrechen oder Vergehen ([Art. 197 Abs. 1 lit. b StPO](/kommentar/stpo/art-197/));
2. Die potentielle Untersuchungsrelevanz der versiegelten Datenträger bzw. Dokumente (sachliche Konnexität zum Gegenstand der Strafuntersuchung, [BGE 138 IV 225](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-138-IV-225_2012.html#consideration_7.1) E. 7.1).

---

## Phase 3: Gerichtsverfahren, Stellungnahme und Triage {#phase-3-gerichtsverfahren-und-triage}

### Gesetzliche Fiktion bei Stillschweigen {#rueckzugsfiktion}

Mit Eingang des Gesuchs leitet das Gericht das Entsiegelungsverfahren ein. Nach [Art. 248a Abs. 3 StPO](/kommentar/stpo/art-248a/) setzt es der berechtigten Person eine **nicht erstreckbare Frist von 10 Tagen** zur Stellungnahme.

> **Wichtigste Neuerung per 1. Januar 2024:**  
> *Stillschweigen gilt als Rückzug des Siegelungsbegehrens* ([Art. 248a Abs. 3 Satz 2 StPO](/kommentar/stpo/art-248a/)).  
> Reagiert die betroffene Person innert der 10 Tage nicht oder lässt sie die Frist ungenutzt verstreichen, wird das Siegelungsverfahren ohne materielle Prüfung als erledigt abgeschrieben und die Daten werden der Staatsanwaltschaft zur Durchsuchung freigegeben.

Derselbe Grundsatz gilt für eine allfällige Verhandlung: Bleibt die berechtigte Person unentschuldigt fern, gilt das Siegelungsbegehren ebenfalls als zurückgezogen ([Art. 248a Abs. 7 StPO](/kommentar/stpo/art-248a/)).

### Substanziierungsobliegenheit der betroffenen Person {#substanziierungsobliegenheit}

Verlangt die berechtigte Person die Aufrechterhaltung der Siegelung, trifft sie eine strenge Mitwirkungs- und Substanziierungsobliegenheit:

> «Betroffene Inhaber von Aufzeichnungen und Gegenständen, welche die Versiegelung beantragen bzw. Durchsuchungshindernisse geltend machen, haben ihrerseits die prozessuale Obliegenheit, das Zwangsmassnahmengericht bei der Sichtung und Klassifizierung von Dokumenten zu unterstützen».
>
> — [BGE 138 IV 225](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-138-IV-225_2012.html#consideration_7.1) E. 7.1

Die betroffene Person darf sich nicht auf pauschale Behauptungen beschränken. Sie muss dem Gericht konkret darlegen:
- Welche Ordner, Dateitypen, Kommunikationskanäle oder Zeiträume dem Schutz unterliegen;
- Anhand welcher Suchbegriffe, Namen oder Kontaktdaten geschützte Dokumente (z.B. Anwaltskorrespondenz) identifiziert werden können;
- Inwiefern bei privaten Aufzeichnungen das persönliche Schutzinteresse das öffentliche Interesse an der Verfolgung der konkreten Straftat überwiegt ([BGE 142 IV 207](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-142-IV-207_2016.html#consideration_11.) E. 11; [BGE 151 IV 344](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-151-IV-344_2025.html#consideration_2.7) E. 2.7).

### Triage durch das Gericht {#triage-durch-das-gericht}

Ist die Sache spruchreif, entscheidet das Gericht innert 10 Tagen schriftlich ([Art. 248a Abs. 4 StPO](/kommentar/stpo/art-248a/)); andernfalls führt es innert 30 Tagen eine Verhandlung durch (Abs. 5).

Bei der Prüfung nimmt das Gericht eine **Triage** vor:
- «Zwangsmassnahmen setzen überdies voraus, dass ein hinreichender Tatverdacht vorliegt und die streitige Untersuchungshandlung verhältnismässig erscheint» ([BGE 141 IV 77](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-141-IV-77_2015.html#consideration_4.3) E. 4.3).
- «Der Entsiegelungsrichter hat (auch bei grossen Datenmengen) jene Gegenstände auszusondern, die […] für die Strafuntersuchung offensichtlich irrelevant erscheinen» ([BGE 141 IV 77](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-141-IV-77_2015.html#consideration_4.3) E. 4.3).
- Das Gericht kann zur technischen Ausscheidung sachverständige Personen oder IT-Spezialisten der Polizei beiziehen ([Art. 248a Abs. 6 StPO](/kommentar/stpo/art-248a/)).
- Geschützte Anwaltskorrespondenz wird physisch ausgesondert bzw. digital gelöscht; schützenswerte Daten Dritter (wie Patientenakten) werden anonymisiert, bevor die verbleibenden Daten der Staatsanwaltschaft übergeben werden ([BGE 141 IV 77](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-141-IV-77_2015.html#consideration_5.5.1) E. 5.5.1).

### Pflicht zur Prüfung akzessorischer Rügen {#akzessorische-ruegen}

Bringt die betroffene Person gültige Siegelungsgründe nach [Art. 264 StPO](/kommentar/stpo/art-264/) vor, stellt sich regelmässig die Frage, ob das Entsiegelungsgericht auch allgemeine Rügen gegen die Zwangsmassnahme prüfen darf (z.B. fehlender Tatverdacht, Unverhältnismässigkeit der Hausdurchsuchung nach [Art. 197 StPO](/kommentar/stpo/art-197/)).

Das Bundesgericht hat hierzu in [BGE 151 IV 175](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-151-IV-175_2025.html#consideration_3.4) E. 3.4 entschieden:
- Werden zulässige Siegelungsgründe nach [Art. 264 Abs. 1 StPO](/kommentar/stpo/art-264/) (wie Anwaltsgeheimnis oder Privatsphäre) angerufen, **muss** das Entsiegelungsgericht auch akzessorische Rügen bezüglich der Rechtmässigkeit der Massnahme nach [Art. 197 StPO](/kommentar/stpo/art-197/) prüfen.
- Diese Prüfungspflicht entfällt selbst dann nicht, wenn das Gericht die geltend gemachten Geheimnisse materiell verwirft (etwa mangels Substanziierung). Eine Verweisung an die kantonale Beschwerdekammer widerspräche der Prozessökonomie und dem Beschleunigungsgebot.

---

## Phase 4: Entscheid und Rechtsmittelweg {#phase-4-entscheid-und-rechtsmittel}

### Endgültigkeit auf kantonaler Ebene {#endgueltigkeit}

Entscheide des Zwangsmassnahmengerichts im Entsiegelungsverfahren sind nach Bundesrecht **endgültig** ([Art. 248a Abs. 4 und 5 StPO](/kommentar/stpo/art-248a/); Art. 380 StPO). Die kantonale Beschwerde an die Beschwerdekammer des Obergerichts ist ausgeschlossen ([BGE 144 IV 74](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-144-IV-74_2018.html#consideration_2.3) E. 2.3).

### Beschwerde an das Bundesgericht (Art. 78 ff. BGG) {#beschwerde-an-das-bundesgericht}

Gegen den Entsiegelungsentscheid des ZMG steht die Beschwerde in Strafsachen an das Bundesgericht offen ([Art. 78 ff. BGG](https://www.fedlex.admin.ch/eli/cc/2006/218/de#art_78); Art. 80 Abs. 2 Satz 3 BGG).

Da der Entsiegelungsentscheid das Strafverfahren nicht abschliesst, handelt es sich um einen Zwischenentscheid gemäss [Art. 93 BGG](https://www.fedlex.admin.ch/eli/cc/2006/218/de#art_93). Die Beschwerde ist nur zulässig, wenn der Entscheid einen **nicht wieder gutzumachenden Nachteil rechtlicher Natur** bewirken kann ([Art. 93 Abs. 1 lit. a BGG](https://www.fedlex.admin.ch/eli/cc/2006/218/de#art_93); [BGE 141 IV 284](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-141-IV-284_2015.html#consideration_2.2) E. 2.2):
- **Berufsgeheimnisse**: Bei Verletzung von Anwalts-, Arzt- oder Quellenschutzgeheimnissen wird ein nicht wieder gutzumachender Nachteil regelmässig bejaht, da ein einmal offenbartes Berufsgeheimnis unwiederbringlich preisgegeben ist.
- **Privat- und Persönlichkeitsgeheimnisse**: Bei Smartphones oder persönlichen Unterlagen droht nicht automatisch ein rechtlicher Nachteil. Die beschwerdeführende Partei muss vor Bundesgericht substanziieren, inwiefern das Persönlichkeitsinteresse das Strafverfolgungsinteresse überwiegt ([BGE 151 IV 344](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-151-IV-344_2025.html#consideration_2.7) E. 2.7).

### Kostenregelung {#kostenregelung}

Zur Kostenauflage im Entsiegelungsverfahren gilt:
> «Das Entsiegelungsverfahren vor dem Zwangsmassnahmengericht […] stellt ein selbstständiges erstinstanzliches Zwangsmassnahmenverfahren dar. Der Entsiegelungsentscheid schliesst das Strafverfahren nicht ab».
>
> — [BGE 138 IV 225](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-138-IV-225_2012.html#consideration_8.2) E. 8.2

Verliert die beschuldigte Person im Entsiegelungsverfahren vor dem ZMG, dürfen ihr die erstinstanzlichen Gerichtskosten nicht sofort auferlegt werden. Die Kosten sind vorläufig vom Kanton zu tragen ([Art. 423 Abs. 1 StPO](/kommentar/stpo/art-423/)); über die definitive Kostentragung entscheidet der Sachrichter im Endurteil nach Massgabe von Art. 426 StPO ([BGE 138 IV 225](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-138-IV-225_2012.html#consideration_8.2) E. 8.2).

---

## Folgen von Verfahrensfehlern: Verwertungsverbote {#verwertungsverbote}

Das Siegelungsverfahren ist formstreng. Wird das Siegelungsrecht durch die Strafverfolgungsbehörden verletzt, greifen die Bestimmungen über Beweisverwertungsverbote nach [Art. 141 StPO](/kommentar/stpo/art-141/).

### Vorzeitige Durchsuchung oder Einsichtnahme {#vorzeitige-einsichtnahme}

Nimmt die Staatsanwaltschaft oder die Polizei vor der Entscheidung über das Entsiegelungsgesuch oder unter Missachtung eines gestellten Siegelungsbegehrens Einsicht in versiegelte Daten, liegt eine schwere Verletzung von [Art. 248 Abs. 1 StPO](/kommentar/stpo/art-248/) vor:
- Die unrechtmässig erlangten Beweise unterliegen einem Verwertungsverbot ([Art. 141 StPO](/kommentar/stpo/art-141/)).
- Bei schwerwiegenden behördlichen Realakten an gesiegelten Geräten führt dies zur vollständigen Unverwertbarkeit sämtlicher darauf befindlicher Daten, zu deren Löschung und zur Rückgabe der Geräte ([BGE 148 IV 221](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-148-IV-221_2022.html#consideration_4.2) E. 4.2).

### Geltendmachung im Vorverfahren vs. Sachrichtervorbehalt {#sachrichtervorbehalt}

Grundsätzlich ist über Beweisverwertungsverbote erst durch den Sachrichter bei der Hauptverhandlung zu befinden ([Art. 339 Abs. 2 lit. d StPO](/kommentar/stpo/art-339/)). Eine sofortige Aussonderung im Vorverfahren ist jedoch die Ausnahme:

> «Eine solche liegt insbesondere vor, wenn das Gesetz ausdrücklich die sofortige Rückgabe aus den Akten bzw. Vernichtung rechtswidriger Beweise vorsieht […] Ebenso verhält es sich, wenn aufgrund des Gesetzes oder der Umstände des Einzelfalles die Unverwertbarkeit bereits ohne Weiteres feststeht».
>
> — [BGE 143 IV 387](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-143-IV-387_2017.html#consideration_4.4) E. 4.4

Da [Art. 248 Abs. 3 StPO](/kommentar/stpo/art-248/) ausdrücklich die Rückgabe bei nicht rechtzeitiger Entsiegelung anordnet und [Art. 264 StPO](/kommentar/stpo/art-264/) absolute Beschlagnahmeverbote statuiert, sind offensichtlich unzulässige oder unter Missachtung des Siegelungsrechts erhobene Daten bereits durch das Entsiegelungsgericht auszuscheiden.

---

## Praxishinweise {#praxishinweise}

### Für Betroffene und die Verteidigung {#fuer-betroffene-und-verteidigung}

1. **Dreitagesfrist strikt wahren**: Das Siegelungsbegehren muss zwingend innert drei Tagen seit der Sicherstellung erhoben werden ([Art. 248 Abs. 1 StPO](/kommentar/stpo/art-248/)). Bei Hausdurchsuchungen sollte das Begehren vorsorglich direkt ins Durchsuchungsprotokoll diktiert werden.
2. **Keine Berufung auf reine Geschäftsgeheimnisse**: Seit dem 1. Januar 2024 führen Geschäfts-, Fabrikations- und Bankkundengeheimnisse nicht mehr zur Siegelung ([BGE 151 IV 30](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-151-IV-30_2025.html#consideration_2.4)). Die Begründung muss zwingend auf [Art. 264 StPO](/kommentar/stpo/art-264/) gestützt werden (Verteidigerunterlagen, Berufsgeheimnisse, überwiegende Privatgeheimnisse).
3. **Stillschweigensfiktion abwenden**: Sobald das ZMG Frist zur Stellungnahme nach [Art. 248a Abs. 3 StPO](/kommentar/stpo/art-248a/) ansetzt (10 Tage, nicht erstreckbar), **muss** gehandelt werden. Stillschweigen gilt von Gesetzes wegen als Rückzug des Siegelungsbegehrens!
4. **Substanziierte Triageanträge stellen**: Pauschales Verweigern schadet. Dem Gericht sind konkrete Suchfilter (Namen der Anwälte, Zeiträume, Ordnernamen) zu unterbreiten, damit geschützte Daten gezielt ausgesondert werden können ([BGE 138 IV 225](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-138-IV-225_2012.html#consideration_7.1)).
5. **Bundesgerichtsbeschwerde wohlüberlegt erheben**: Bei privaten Mobiltelefonen muss der nicht wieder gutzumachende Nachteil nach [Art. 93 Abs. 1 lit. a BGG](https://www.fedlex.admin.ch/eli/cc/2006/218/de#art_93) eigens begründet werden ([BGE 151 IV 344](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-151-IV-344_2025.html#consideration_2.7)).

### Für Strafverfolgungsbehörden und Polizei {#fuer-strafverfolgungsbehoerden}

1. **Inzisionsverbot beachten**: Ab Eingang des Siegelungsbegehrens darf kein Ermittler in die Daten Einsicht nehmen. Zuwiderhandlungen führen zur absoluten Unverwertbarkeit ([Art. 141 Abs. 1 StPO](/kommentar/stpo/art-141/); [BGE 148 IV 221](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-148-IV-221_2022.html#consideration_4.2)).
2. **Datenspiegelung nur durch unabhängige Forensiker**: Eine vorsorgliche Datenspiegelung zur Abwendung flüchtigen Datenverlusts ist zulässig ([BGE 152 IV 107](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-152-IV-107_2026.html#consideration_5.7.8)). Die beigezogenen Forensiker dürfen danach aber unter keinen Umständen für die eigentlichen materiellen Ermittlungen eingesetzt werden.
3. **20-tägige Entsiegelungsfrist überwachen**: Stellt die Staatsanwaltschaft das Gesuch nicht innert 20 Tagen seit der Siegelung ([Art. 248 Abs. 3 StPO](/kommentar/stpo/art-248/)), sind alle Unterlagen unbesehen zurückzugeben.
4. **Sachbeweise nicht siegeln**: Drogen, Waffen und Bargeld fallen von vornherein nicht unter [Art. 248 StPO](/kommentar/stpo/art-248/) und sind direkt nach [Art. 263 StPO](/kommentar/stpo/art-263/) zu beschlagnahmen ([BGE 144 IV 74](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-144-IV-74_2018.html#consideration_2.6)).

---

## Leitentscheide {#leitentscheide}

| Entscheid | Gegenstand | Kernaussage / Bedeutung |
|---|---|---|
| [BGE 152 IV 107](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-152-IV-107_2026.html#consideration_5.7.8) (2026) | Datenspiegelung bei Siegelungsbegehren | Praxisänderung zu BGE 148 IV 221: Bei unmittelbar drohendem Datenverlust (Smartphones) dürfen Strafbehörden vor der Siegelung eine Datenspiegelung durch unabhängige Sachverständige anordnen. |
| [BGE 151 IV 30](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-151-IV-30_2025.html#consideration_2.4) (2025) | Siegelungsgründe nach neuem Recht 2024 | Die Siegelungsgründe sind in Art. 248 Abs. 1 StPO abschliessend auf Art. 264 StPO beschränkt. Allgemeine Geschäftsgeheimnisse und Bankgeheimnisse berechtigen nicht mehr zur Siegelung. |
| [BGE 151 IV 175](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-151-IV-175_2025.html#consideration_3.4) (2025) | Akzessorische Rügen im Entsiegelungsverfahren | Werden zulässige Schutzgründe nach Art. 264 StPO geltend gemacht, muss das Entsiegelungsgericht auch akzessorische Rügen (Art. 197 StPO) bezüglich der Grundmassnahme prüfen. |
| [BGE 151 IV 344](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-151-IV-344_2025.html#consideration_2.7) (2025) | Durchsuchung von Smartphones | Bei privaten Smartphones ist Art. 264 Abs. 1 lit. b StPO tangiert, gewährt aber keinen absoluten Schutz. Vor Bundesgericht muss dargetan werden, weshalb das Geheimhaltungsinteresse überwiegt. |
| [BGE 151 IV 350](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-151-IV-350_2025.html#consideration_2.5.3) (2025) | Geeignetheit und Triage bei Mobiltelefonen | Die Sichtung für das Verfahren bedeutungsloser Teilmengen bei der Durchsuchung von Datenträgern ist systemimmanent. Bei schweren Delikten überwiegt das Verfolgungsinteresse regelmässig. |
| [BGE 151 IV 153](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-151-IV-153_2025.html#consideration_4.1.1) (2025) | Quellenschutz der Medienschaffenden | Weiter Schutzbereich von Art. 172 StPO i.V.m. Art. 264 Abs. 1 lit. c StPO für Journalisten und Hilfspersonen (inkl. Verlagsleitung), auch auf Geräten Dritter. |
| [BGE 148 IV 221](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-148-IV-221_2022.html#consideration_2.3) (2022) | Zweck der Siegelung und Inzisionsverbot | Die Siegelung schliesst jede behördliche Kenntnisnahme vor dem richterlichen Entscheid aus. Schwere Verletzungen führen zur absoluten Unverwertbarkeit und Datenvernichtung. |
| [BGE 144 IV 74](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-144-IV-74_2018.html#consideration_2.6) (2018) | Abgrenzung Aufzeichnungen und Sachbeweise | Nicht der Geheimhaltung zugängliche Gegenstände (Drogen, Waffen, Bargeld) unterliegen nicht der Siegelung nach Art. 248 StPO, sondern der direkten Beschlagnahme nach Art. 263 StPO. |
| [BGE 142 IV 207](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-142-IV-207_2016.html#consideration_8.3) (2016) | Nemo tenetur und Substanziierung | Tragweite des Grundsatzes gegen Selbstbelastung (Art. 113 Abs. 1 StPO) bei bestehenden Unterlagen sowie Anforderungen an die Substanziierung im Entsiegelungsverfahren. |
| [BGE 141 IV 77](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-141-IV-77_2015.html#consideration_5.5.1) (2015) | Berufsgeheimnis des Arztes und Triage | Bei beschuldigtem Arzt kein absolutes Entsiegelungshindernis; das ZMG hat eine Triage vorzunehmen und Patientendaten vor Weitergabe an die Staatsanwaltschaft zu anonymisieren. |
| [BGE 138 IV 225](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-138-IV-225_2012.html#consideration_7.1) (2012) | Anwaltsgeheimnis, Mitwirkung und Kosten | Substanziierungsobliegenheit der Betroffenen bei der Triage von Datenträgern. Gerichtskosten dürfen der beschuldigten Person im Entsiegelungsverfahren nicht auferlegt werden. |
| [BGE 143 IV 387](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-143-IV-387_2017.html#consideration_4.4) (2017) | Verwertungsverbote im Entsiegelungsverfahren | Ausnahmen vom Sachrichtervorbehalt: Offensichtliche Beweisverwertungsverbote nach Art. 141 StPO sind bereits im Entsiegelungsverfahren zu beachten. |
| [BGE 141 IV 284](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-141-IV-284_2015.html#consideration_2.2) (2015) | Beschwerde an das Bundesgericht (Art. 93 BGG) | Anfechtbarkeit von Zwischenentscheiden über Beweise nur bei drohendem, nicht wieder gutzumachendem Nachteil rechtlicher Natur. |
