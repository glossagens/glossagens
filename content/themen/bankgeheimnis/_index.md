---
title: "Bankgeheimnis"
date: 2026-10-25
lastmod: 2026-10-25
description: "Das schweizerische Bankkundengeheimnis (Art. 47 BankG): Dogmatische Grundlagen im Zivil- und Verfassungsrecht, historische Entwicklung von 1934 über die UBS-Krise und den AIA bis zur StPO-Revision 2024 sowie Grenzen und heutiges Spannungsfeld."
tags: ["Bankgeheimnis", "Bankkundengeheimnis", "BankG", "Finanzmarktrecht", "Steueramtshilfe", "AIA", "Art. 47 BankG", "Siegelung", "Persönlichkeitsschutz"]
typ: grundlage
kurz: "Das schweizerische Bankgeheimnis schützt als Ausfluss des zivilrechtlichen Persönlichkeitsschutzes und der vertraglichen Treuepflicht die finanziellen Verhältnisse der Bankkunden und ist in Art. 47 BankG strafrechtlich bewehrt. Nach seiner Hochphase im 20. Jahrhundert wurde es im internationalen Steuerverhältnis ab 2009 zugunsten des OECD-Amtshilfestandards und des automatischen Informationsaustauschs (AIA) weitgehend abgelöst, während es im Inland bei direkten Steuern fortbesteht. Im Strafverfahren entbindet das Bankgeheimnis nicht von der Zeugnis- und Editionspflicht und berechtigt seit der StPO-Revision 2024 auch nicht mehr zur Siegelung."
sachgebiete:
  - wirtschaftsaufsicht
  - amtshilfe_steuer
  - steuern.steuerstrafrecht
  - schuldrecht.werk_auftrag
normen:
  - { gesetz: bankg, art: art-047 }
  - { gesetz: bv, art: art-013 }
  - { gesetz: or, art: art-398 }
  - { gesetz: stpo, art: art-248 }
stichworte: ["Bankgeheimnis", "Bankkundengeheimnis", "Art. 47 BankG", "Automatischer Informationsaustausch", "AIA", "OECD-Musterabkommen", "Steueramtshilfe", "Steuerhinterziehung", "Steuerbetrug", "Siegelung", "UBS-Krise", "Falciani"]
agent_verified: true
revisions:
  - date: 2026-10-25
    by: "Antigravity"
    model: "gemini-3.8-flash"
    mcp_verified: true
    note: "Erstfassung des Themas Bankgeheimnis. Normtexte Art. 47 BankG und Art. 13 BV per {{< wortlaut >}} über scripts/wortlaut.py. 14 Bundesgerichtsentscheide als Volltext von entscheidsuche.ch geladen und verifiziert (BGE 137 II 431, BGE 145 IV 114, BGE 151 IV 30, BGE 151 IV 175, BGE 133 III 664, BGE 95 I 439, BGE 121 IV 45, BGE 125 II 83, BGE 119 IV 175, BGE 86 III 114, BGE 112 III 6, BGE 139 II 404, BGE 143 II 136, BGE 143 II 224); Erwägungen, Anker und Zitate mit pruefen.py und build-check.sh geprüft."
---

## Überblick {#ueberblick}

Das schweizerische **Bankgeheimnis** – in der juristischen Fachsprache präziser als **Bankkundengeheimnis** bezeichnet – regelt die Pflicht von Bankinstituten und deren Mitarbeitenden, sämtliche kundenbezogenen Informationen gegenüber Dritten und Behörden vertraulich zu behandeln. Entgegen verbreiteten Missverständnissen handelt es sich nicht um ein Institut, das isoliert im Nebenstrafrecht entstanden ist oder den Banken als Privileg dient. Seine Wurzeln liegen vielmehr im bürgerlichen Recht: Es ist der zivilrechtliche Ausfluss der vertraglichen Sorgfalts- und Treuepflicht ([Art. 398 Abs. 2 OR](/kommentar/or/art-398/#b-getreue-und-sorgfältige-ausführung-abs-2)) sowie des zivilrechtlichen Persönlichkeitsschutzes (Art. 28 ZGB), verfassungsrechtlich flankiert durch den Schutz der Privatsphäre gemäss [Art. 13 Abs. 1 BV](/kommentar/bv/art-013/#1-privatleben-art-13-abs-1-var-1). Art. 47 BankG normiert lediglich die strafrechtliche Bewehrung dieser vorbestehenden Verschwiegenheitspflicht.

Kaum ein anderes Rechtsinstitut hat in der schweizerischen Rechts- und Wirtschaftsgeschichte eine derart fundamentale Transformation durchlaufen wie das Bankgeheimnis:
- **1934 bis 2008**: Das Bankgeheimnis diente als zentraler Pfeiler des Schweizer Finanzplatzes. Durch die strikte gesetzliche Unterscheidung zwischen einfacher Steuerhinterziehung (blosse Nichtdeklaration ohne Urkundenfälschung) und Steuerbetrug verweigerte die Schweiz ausländischen Staaten jahrzehntelang die Rechtshilfe und Steueramtshilfe bei Steuerdelikten, soweit keine qualifizierte Urkundenfälschung vorlag.
- **2008/2009 (Der Wendepunkt)**: Die globale Finanzkrise und der Steuerstreit der Grossbank UBS mit dem US-Justizministerium (DOJ) führten zu einem beispiellosen Paradigmenwechsel. Um den Zusammenbruch der UBS und schwere Schäden für die schweizerische Gesamtwirtschaft abzuwenden, ordnete die FINMA gestützt auf die polizeiliche Generalklausel die sofortige Herausgabe von Kundendaten an die USA an ([BGE 137 II 431](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_004_BGE-137-II-431_2011.html#consideration_3.2)). Am 13. März 2009 beschloss der Bundesrat die vollständige Übernahme des OECD-Standards (Art. 26 des OECD-Musterabkommens) und gab die Differenzierung zwischen Steuerhinterziehung und Steuerbetrug im zwischenstaatlichen Verhältnis auf.
- **Ab 2017/2018 (Transparenz nach aussen)**: Mit der Einführung des Automatischen Informationsaustauschs in Steuersachen (AIA) übermitteln Schweizer Finanzinstitute Kontodaten ausländischer Steuerpflichtiger regelmässig und automatisiert an deren Heimatstaaten. International ist das Bankgeheimnis im Steuerbereich damit de facto erloschen.
- **Gegenwart (Dualismus und prozessuale Schranken)**: Im Inland gilt das Bankgeheimnis gegenüber den Steuerbehörden bei den direkten Steuern im ordentlichen Veranlagungsverfahren weiter (Art. 127 Abs. 2 DBG). Im Strafprozess entband das Bankgeheimnis ohnehin nie von der Zeugnis- und Herausgabepflicht; seit der StPO-Revision vom 1. Januar 2024 berechtigt es die Betroffenen nicht einmal mehr zur Siegelung ([Art. 248 Abs. 1 StPO](/kommentar/stpo/art-248/#1-der-ausschluss-von-fabrikations--geschäfts--und-bankgeheimnissen); [BGE 151 IV 30](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-151-IV-30_2025.html#consideration_2.4.1)).

## Rechtsgrundlagen: Art. 47 BankG und Art. 13 BV {#rechtsgrundlagen}

Die strafrechtliche Kernnorm findet sich in Art. 47 des Bankengesetzes (BankG, SR 952.0):

{{< wortlaut gesetz="bankg" art="art-047" >}}

Verfassungsrechtlich ruht der Schutz der wirtschaftlichen Privatsphäre auf Art. 13 BV:

{{< wortlaut gesetz="bv" art="art-013" >}}

## Begriff und dogmatische Natur {#begriff-und-natur}

### Schutzbereich und Rechtsnatur {#schutzbereich}

Das Bundesgericht hat die dogmatische Natur und die Begriffsmerkmale des Bankkundengeheimnisses in ständiger Rechtsprechung präzisiert:

> «Das Bankkundengeheimnis bezeichnet die durch Straf- und allenfalls aufsichtsrechtliche Sanktionen verstärkte Pflicht einer Bank und ihrer Angehörigen, alle Informationen, die ihnen im Laufe der Geschäftsbeziehung vom Kunden anvertraut werden oder ihnen in diesem Rahmen zur Kenntnis kommen, nach aussen hin geheim zu halten. Es beruht auf der vertraglichen Beziehung zwischen der Bank und dem Kunden einerseits und dessen Persönlichkeitsschutz andererseits».
>
> — [BGE 137 II 431](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_004_BGE-137-II-431_2011.html#consideration_2.1.1) E. 2.1.1

Das Bankkundengeheimnis ist somit ein Rechtsinstitut mit einer doppelten Dimension:
1. **Zivilrechtliche Grundlage**: Das Grundverhältnis zwischen Bank und Kunde untersteht in aller Regel dem Auftragsrecht (Art. 394 ff. OR) oder weist auftragsrechtliche Elemente auf. Aus [Art. 398 Abs. 2 OR](/kommentar/or/art-398/#b-getreue-und-sorgfältige-ausführung-abs-2) fliesst eine strenge Treue- und Verschwiegenheitspflicht des Beauftragten. Diese Pflicht wird durch den zivilrechtlichen Persönlichkeitsschutz (Art. 28 ZGB) untermauert, da die Vermögenslage und die finanziellen Dispositionen einer Person deren Privatsphäre angehören.
2. **Strafrechtliche Akzessorietät**: Art. 47 BankG begründet kein eigenes materielles Recht auf Geheimhaltung, sondern bewehrt die zivilrechtliche Pflicht strafrechtlich:
   > «Art. 47 BankG regelt nicht das Bankkundengeheimnis als solches, sondern die (strafrechtliche) Sanktion bei dessen Verletzung».
   >
   > — [BGE 137 II 431](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_004_BGE-137-II-431_2011.html#consideration_2.1.1) E. 2.1.1

In [BGE 145 IV 114](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-145-IV-114_2019.html#consideration_3.3.2) (Fall Rudolf Elmer / Julius Bär) hat das Bundesgericht diesen doppelten Charakter nochmals bekräftigt:
> «Der Schutzbereich von Art. 47 BankG entspricht dem Umfang des Bankgeheimnisses. Dieses hat eine individuelle und eine institutionelle Dimension: Betroffen ist einerseits das Persönlichkeitsrecht des Bankkunden, anderseits die Funktionsfähigkeit des Finanzplatzes».
>
> — BGE 145 IV 114 E. 3.3.2

Die Norm fungiert als Scharnier: «Art. 47 BankG nimmt die auftragsrechtliche Verpflichtung der Bank gegenüber ihrem Kunden, dessen Daten vertraulich zu behandeln (Art. 398 Abs. 1 in Verbindung mit Art. 321a Abs. 4 OR ), auf und sichert sie ab, indem er das diesbezüglich pflichtwidrige Verhalten von natürlichen und juristischen Personen, die für die Bank tätig sind, unter Strafe stellt. Die Bestimmung ist das strafrechtliche Pendant zur Vertraulichkeitsverpflichtung des Bankinstituts» (BGE 145 IV 114 E. 3.3.2).

### Kein absoluter Verfassungsrang {#kein-verfassungsrang}

Obwohl die Vermögensverhältnisse zur geschützten Privatsphäre nach [Art. 13 Abs. 1 BV](/kommentar/bv/art-013/#1-privatleben-art-13-abs-1-var-1) und Art. 8 Ziff. 1 EMRK zählen, geniesst das Bankgeheimnis als solches keinen absoluten Verfassungsrang:

> «Dem Bankkundengeheimnis kommt nach der Rechtsprechung nicht der Rang eines eigenständigen geschriebenen oder ungeschriebenen verfassungsmässigen Rechts zu, sodass es bei Kollisionen mit anderen Interessen diesen stets vorgehen würde».
>
> — [BGE 137 II 431](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_004_BGE-137-II-431_2011.html#consideration_2.1.2) E. 2.1.2

Schon in [BGE 125 II 83](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_004_BGE-125-II-83_1998-10-29.html#consideration_5.) hielt das Gericht fest: «Das Bankgeheimnis […] hat nicht Verfassungsrang. Es behält die eidgenössischen und kantonalen Bestimmungen über die Zeugnis- und die Auskunftspflicht gegenüber einer Behörde ausdrücklich vor» (E. 5). Wie jede Einschränkung von Grundrechten ist ein Eingriff in das Bankgeheimnis nach Massgabe von Art. 36 BV zulässig, wenn er auf einer gesetzlichen Grundlage beruht, durch ein öffentliches Interesse gerechtfertigt ist und sich als verhältnismässig erweist (BGE 137 II 431 E. 2.1.2).

### Kreis der Geheimnispflichtigen {#pflichtige}

Art. 47 Abs. 1 lit. a BankG umschreibt den Kreis der tauglichen Täter als echtes Sonderdelikt. Geheimnispflichtig sind:
- Organe der Bank (Verwaltungsrat, Geschäftsleitung),
- Angestellte,
- Beauftragte und Liquidatoren,
- Organe und Angestellte der zugelassenen Prüfgesellschaft.

Der Begriff des *Beauftragten* wurde mit der BankG-Revision von 1971 eingefügt, um namentlich externe Rechenzentren und IT-Dienstleister zu erfassen. Die Rechtsprechung legt den Begriff funktionell aus: Auch ein von der Bank beauftragter Rechtsanwalt, der gegen einen Kunden einen Zivilprozess führt, untersteht hinsichtlich der ihm anvertrauten Kundendaten dem Bankgeheimnis: «Das Bankgeheimnis würde durchlöchert, wenn Anwälte, die von einer Bank für die Führung eines Prozesses beigezogen werden, nicht an das Bankgeheimnis gebunden wären» ([BGE 121 IV 45](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-121-IV-45_1995-03-02.html#consideration_2.) E. 2b).

Grenzen des persönlichen Geltungsbereichs: In BGE 145 IV 114 verneinte das Bundesgericht die Strafbarkeit eines Mitarbeiters einer ausländischen Tochtergesellschaft (Cayman Islands), da diese formell nicht als Bank im Sinne des schweizerischen BankG qualifizierte und keine direkte Anstellung oder Beauftragung durch die schweizerische Muttergesellschaft vorlag. Das strafrechtliche Legalitätsprinzip (Art. 1 StGB) verbietet eine extensive Ausdehnung des Täterkreises über die klaren Grenzen des Gesetzeswortlauts hinaus (E. 3.3.2 ff.).

### Geheimnisherr und Auskunftsansprüche der Erben {#geheimnisherr}

Geheimnisherr ist ausschliesslich der Bankkunde (bzw. die an der Geschäftsbeziehung berechtigte Person). Die Bank ist lediglich Geheimnisträgerin:
- **Einwilligung**: Der Kunde kann die Bank jederzeit ermächtigen, Daten an Dritte oder Behörden weiterzugeben. Eine solche Entbindung hebt die Geheimhaltungspflicht auf und schliesst die Rechtswidrigkeit einer Offenbarung aus ([BGE 137 II 431](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_004_BGE-137-II-431_2011.html#consideration_2.1.2) E. 2.1.2).
- **Keine Geltung gegenüber dem Kunden selbst**: Gegenüber dem Kunden greift das Bankgeheimnis nicht. Die Bank ist ihm gegenüber aus Art. 400 Abs. 1 OR umfassend zur Rechenschaft und Auskunft verpflichtet ([BGE 133 III 664](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_005_BGE-133-III-664_2007.html#consideration_2.6) E. 2.6).
- **Erbrechtliche Universalsukzession (Art. 560 ZGB)**: Stirbt der Kunde, geht der vertragliche Auskunftsanspruch ungeschmälert auf seine Erben über:
  > «Aus dem Wesen der Universalsukzession im Sinn von Art. 560 ZGB folgt, dass nicht nur sämtliche Vermögensrechte, sondern insbesondere auch die vertraglichen Auskunftsansprüche auf die Erben übergehen, soweit sie nicht höchstpersönliche Rechte des Erblassers beschlagen, wobei diese Ansprüche jedem Erben einzeln zustehen».
  >
  > — [BGE 133 III 664](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_005_BGE-133-III-664_2007.html#consideration_2.5) E. 2.5

Eine Weigerung der Bank, den gesetzlichen oder eingesetzten Erben über die Konten, Salden und historischen Transaktionen des Erblassers Auskunft zu erteilen, ist unzulässig: «Ins Leere stösst sodann der Verweis auf das Bankgeheimnis gemäss Art. 47 BankG : Dieses gilt nur gegenüber Dritten, während es gegenüber dem Geheimnisherrn - und im Rahmen der Erbfolge auch gegenüber seinen Universalsukzessoren - von vornherein nicht greifen kann» (BGE 133 III 664 E. 2.6; bereits [BGE 89 II 87](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_004_BGE-89-II-87_1963-03-19.html) E. 6).

## Historische Entwicklung {#entwicklung}

### Kodifikation im Bankengesetz 1934 {#kodifikation-1934}

Vor 1934 existierte in der Schweiz keine spezialgesetzliche Strafnorm für Bankiers. Die Schweigepflicht leitete sich ausschliesslich aus dem kantonalen Zivilrecht bzw. nach 1912 aus dem eidgenössischen Obligationenrecht (Auftrag, Art. 398 OR) und dem Zivilgesetzbuch (Art. 28 ZGB) ab.

Die Aufnahme einer strafrechtlichen Sanktion in Art. 47 des Bankengesetzes vom 8. November 1934 (in Kraft seit 1. März 1935) war das Resultat einer doppelten historischen Krise:
1. **Wirtschaftskrise und Gläubigerschutz**: Nach den Zusammenbrüchen mehrerer Schweizer Banken infolge der Weltwirtschaftskrise von 1929 forderte die Politik eine staatliche Aufsicht über das Bankwesen zum Schutz der Sparer und Gläubiger.
2. **Abwehr ausländischer Spionage**: Im Oktober 1932 kam es in Paris zum sogenannten Basler Bankenskandal: Die französische Polizei durchsuchte Geschäftsräume der Basler Handelsbank und beschlagnahmte Kundenlisten wohlhabender Franzosen. Zur gleichen Zeit verschärfte das nationalsozialistische Regime im Deutschen Reich die Devisengesetze drakonisch und bedrohte Kapitalflucht ins Ausland mit der Todesstrafe. Die Verankerung von Art. 47 BankG sollte Bankangestellte unter Strafdrohung stellen, um sie gegen ausländischen Druck und Bestechungsversuche zur Herausgabe von Kundendaten abzuschirmen.

### Nachkriegszeit bis zur Jahrtausendwende {#nachkriegszeit}

In den Jahrzehnten nach dem Zweiten Weltkrieg etablierte sich das Bankgeheimnis als weltweites Markenzeichen des Schweizer Finanzplatzes. Es bot Anlegern aus politisch oder wirtschaftlich instabilen Ländern Diskretion und Schutz vor Enteignung und Verfolgung.

Zugleich bildete sich die schweizerische Praxis heraus, zwischen zwei Formen der Steuerverkürzung zu unterscheiden:
- **Einfache Steuerhinterziehung**: Das blosse Verschweigen von Einkünften oder Vermögenswerten in der Steuererklärung galt im schweizerischen Recht lediglich als Steuerübertretung (Ordnungswidrigkeit), nicht als Straftat. Weder die inländischen Steuerbehörden noch ausländische Staaten erhielten hierfür Einblick in Bankunterlagen.
- **Steuerbetrug**: Erst wenn der Steuerpflichtige arglistig gefälschte oder verfälschte Urkunden (z. B. fingierte Bilanzen, gefälschte Lohnausweise) einsetzte, lag ein Vergehen nach Art. 186 DBG vor. Nur bei Steuerbetrug wurde im internationalen Verhältnis Rechtshilfe oder Steueramtshilfe gewährt ([BGE 96 I 737](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_001_BGE-96-I-737_1970-12-23.html) E. 6; [BGE 139 II 404](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_004_BGE-139-II-404_2013.html#consideration_9.3) E. 9.3).

In den 1990er Jahren geriet das Bankgeheimnis erstmals unter schweren internationalen Druck im Zusammenhang mit den nachrichtenlosen Vermögen von Holocaust-Opfern, was zu umfassenden historischen Untersuchungen (Bergier-Kommission) und einem globalen Vergleich führte.

### Die Zäsur 2008/2009: UBS-Krise und polizeiliche Generalklausel {#ubs-krise}

Der eigentliche Bruch mit der traditionellen Doktrin vollzog sich im Gefolge der Finanzkrise ab 2008:
- Die US-Steuerbehörde Internal Revenue Service (IRS) und das US-Justizministerium (DOJ) warfen der Grossbank UBS vor, tausenden US-Bürgern bei der massiven Steuerhinterziehung geholfen zu haben.
- Im Februar 2009 drohte die US-Justiz der UBS mit einer strafrechtlichen Anklage (Indictment), was nach einhelliger Einschätzung der Behörden den sofortigen Zusammenbruch der systemrelevanten Grossbank und schwere Verwerfungen im gesamten weltweiten Finanzsystem zur Folge gehabt hätte.
- Um diese akute Existenzbedrohung abzuwenden, ordnete die FINMA am 18. Februar 2009 gestützt auf Art. 25 und 26 BankG sowie die verfassungsrechtliche Notstandskompetenz (Art. 185 Abs. 3 BV bzw. die polizeiliche Generalklausel) an, dass die UBS unverzüglich die Daten von rund 250 bis 300 US-Kunden an das DOJ herausgeben müsse.

Das Bundesgericht bestätigte in [BGE 137 II 431](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_004_BGE-137-II-431_2011.html#consideration_3.2) nachträglich die Rechtmässigkeit dieses Vorgehens: Zwar durften reguläre bankenrechtliche Schutzmassnahmen das Bankgeheimnis nicht umgehen (E. 2.2); die Anwendung der polizeilichen Generalklausel war jedoch zulässig, da eine unmittelbare, schwere Gefahr für das schweizerische Wirtschaftsgefüge bestand und keine regulären rechtshilferechtlichen Mittel rechtzeitig greifen konnten (E. 3.2 ff.).

### Übergang zum OECD-Standard und Steueramtshilfe {#oecd-standard}

Unter dem Eindruck des US-Drucks und der Androhung von Sanktionen durch die G20 und die OECD fasste der Bundesrat am **13. März 2009** einen historischen Grundsatzbeschluss:
- Die Schweiz erklärte sich bereit, den internationalen Standard zur Amtshilfe in Steuersachen gemäss **Art. 26 des OECD-Musterabkommens** vorbehaltlos zu übernehmen.
- In allen neu verhandelten oder revidierten Doppelbesteuerungsabkommen (DBA) wurde die bisherige Unterscheidung zwischen Steuerhinterziehung und Steuerbetrug aufgehoben. Die Schweiz verpflichtete sich, auf Ersuchen hin auch bei reiner Steuerhinterziehung umfassend Bankauskünfte zu erteilen ([BGE 139 II 404](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_004_BGE-139-II-404_2013.html#consideration_7.2.1) E. 7.2.1).

In der Folge entwickelte sich die Rechtsprechung zur Steueramtshilfe rasant weiter:
- **Gruppenersuchen**: In [BGE 143 II 136](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_004_BGE-143-II-136_2017.html#consideration_5.3.4) (Fall Niederlande / UBS) entschied das Bundesgericht, dass Amtshilfe auch bei Gesuchen ohne namentliche Nennung der Kontoinhaber («Gruppenersuchen») zulässig ist, sofern das Verhaltensmuster der betroffenen Personen hinreichend präzise umschrieben ist und keine unzulässige Beweisausforschung (*fishing expedition*) vorliegt: «Den Informationsaustauschbestimmungen in Doppelbesteuerungsabkommen liegt zugrunde, dass ein Staat sich die für die Durchführung seines innerstaatlichen Steuerrechts notwendigen, nicht öffentlich zugänglichen Informationen nicht ohne Weiteres selber beschaffen kann, wenn sich diese ausserhalb seines Hoheitsgebietes befinden» (E. 5.3.4).
- **Gestohlene Bankdaten (Affäre Falciani)**: In [BGE 143 II 224](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_004_BGE-143-II-224_2017.html#consideration_6.4) stellte das Bundesgericht klar, dass gestützt auf Art. 7 lit. c StAhiG und das völkerrechtliche Prinzip von Treu und Glauben keine Amtshilfe geleistet werden darf, wenn der ersuchende Staat Bankdaten aktiv gekauft hat, die durch strafbare Handlungen in der Schweiz entwendet wurden (E. 6.4). Hat der ersuchende Staat die Daten hingegen nicht aktiv erworben, sondern auf dem regulären Dienstweg erhalten, steht Art. 7 lit. c StAhiG der Amtshilfe nicht zwingend entgegen ([BGE 143 II 202](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_004_BGE-143-II-202_2017.html) E. 8.5 ff.).

### Automatischer Informationsaustausch (AIA) {#aia}

Der finale Schritt im internationalen Steuerverhältnis erfolgte mit dem Wechsel von der Amtshilfe auf Ersuchen zum **Automatischen Informationsaustausch (AIA)**:
- Das Bundesgesetz über den internationalen automatischen Informationsaustausch in Steuersachen (AIAG, SR 653.1) trat per 1. Januar 2017 in Kraft.
- Seit Herbst 2018 tauscht die Eidgenössische Steuerverwaltung (ESTV) mit über 100 Partnerstaaten jährlich und vollautomatisch Finanzkontendaten (Kontostände, Zinsen, Dividenden, Erlöse aus Veräusserungen) von Personen aus, die im jeweiligen Partnerstaat steuerlich ansässig sind.
- Im internationalen Verhältnis existiert für Nicht-Residenten damit kein Bankgeheimnis mehr.

### Revision 2015 von Art. 47 BankG und Whistleblower-Debatte {#revision-2015}

Während das Bankgeheimnis international abgebaut wurde, verschärfte das Schweizer Parlament den innerstaatlichen Schutz gegen Leaks:
- Per 1. Juli 2015 wurden **Art. 47 Abs. 1 lit. c** und **Abs. 1bis BankG** eingefügt. Damit wird mit Freiheitsstrafe bis zu drei bzw. fünf Jahren bestraft, wer ein ihm offenbartes Bankgeheimnis an weitere Personen weitergibt oder für sich ausnützt (*Datenhehlerei*).
- Diese Norm geriet ab 2022 international massiv in die Kritik (u. a. im Rahmen der Berichterstattung über die *Suisse Secrets*). Internationale Organisationen, Medienschaffende und die UN-Sonderberichterstatterin für Meinungsäusserungsfreiheit rügten, dass die Strafnorm investigative Journalisten und Whistleblower kriminalisiere und eine unzulässige Einschränkung der Medienfreiheit (Art. 10 EMRK, Art. 17 BV) darstelle.

Zugleich scheiterte der Versuch, das Bankgeheimnis auf Verfassungsebene zu verankern: Die Volksinitiative *Ja zum Schutz der Privatsphäre* (sogenannte Bankgeheimnis-Initiative), die ein absolutes Bankgeheimnis im Inland in Art. 13 BV festschreiben wollte, wurde 2018 von den Initianten zurückgezogen, nachdem sich das Parlament gegen eine Gesetzesaufweichung ausgesprochen hatte.

## Grenzen und Durchbrechungen {#grenzen}

Das Bankkundengeheimnis war zu keinem Zeitpunkt schrankenlos. Das Bundesgericht fasst die Systematik der Durchbrechungen zusammen:

> «Es findet seine Grenzen (1) im Willen des Kunden, (2) in einschlägigen, rechtsgenügend gestalteten rechtlichen Eingriffsgrundlagen oder (3) in überwiegenden eigenen (berechtigten) Interessen der Bank».
>
> — [BGE 137 II 431](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_004_BGE-137-II-431_2011.html#consideration_2.1.2) E. 2.1.2

Art. 47 Abs. 5 BankG enthält hierzu den ausdrücklichen Vorbehalt: *Vorbehalten bleiben die eidgenössischen und kantonalen Bestimmungen über die Zeugnispflicht und über die Auskunftspflicht gegenüber einer Behörde.*

### Strafverfahren und Zeugnispflicht {#strafverfahren}

Im Strafverfahren geniessen Bankiers kein Berufsgeheimnis im Sinne von Art. 171 StPO:
- Banken und deren Mitarbeitende sind gegenüber den Strafverfolgungsbehörden uneingeschränkt zeugnis- und editionspflichtig (Art. 165 ff., Art. 246, 265 StPO).
- Das Bundesgericht stellte schon 1969 in [BGE 95 I 439](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_001_BGE-95-I-439_1969-10-01.html#consideration_2.) klar: «wie denn überhaupt das Bankgeheimnis als Ausfluss der zivilrechtlichen Regeln über den Persönlichkeitsschutz aufgefasst werden kann» (E. 2b) und führte aus, dass das Bankgeheimnis niemals von den strafprozessualen Aussage- und Herausgabepflichten entbindet (E. 2b/c).
- In [BGE 119 IV 175](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-119-IV-175_1993-08-16.html#consideration_3.) bestätigte das Gericht, dass die Bank im Verwaltungsstrafverfahren (VStrR) keinen Anspruch darauf hat, die Aussage oder Aktenherausgabe unter Berufung auf das Bankgeheimnis zu verweigern (E. 3).

### Rechtsentwicklung 2024: Ausschluss der Siegelung {#siegelung}

Eine grundlegende Praxisänderung brachte die Revision der Strafprozessordnung per **1. Januar 2024**:
- Nach altem Recht ([Art. 248 aStPO](/kommentar/stpo/art-248/)) konnten Kontoinhaber oder Banken bei der Sicherstellung von Bankunterlagen die *Siegelung* verlangen, indem sie geltend machten, es stünden schutzwürdige Geheimnisse entgegen. Dies führte regelmässig zu jahrelangen Verzögerungen im Entsiegelungsverfahren vor dem Zwangsmassnahmengericht.
- Mit dem Inkrafttreten des revidierten Art. 248 Abs. 1 StPO schloss der Gesetzgeber das Bankgeheimnis bewusst aus dem Katalog der zulässigen Siegelungsgründe aus:
  > «Damit werden die schutzwürdigen Geheimnisinteressen, die einer Entsiegelung entgegenstehen können, abschliessend definiert und gegenüber dem alten Recht restriktiver gefasst. In Frage kommen nur noch die in Art. 264 StPO geregelten Geheimnisschutzgründe. Geschäftsgeheimnisse bzw. "Geschäftsschutzinteressen" fallen nicht darunter, das Bankkundengeheimnis […] ebenfalls nicht».
  >
  > — [BGE 151 IV 30](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-151-IV-30_2025.html#consideration_2.4.1) E. 2.4.1

Diese Rechtsprechung wurde in [BGE 151 IV 175](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-151-IV-175_2025.html#consideration_2.4.2) E. 2.4.2 bestätigt: Weder die Bank noch der betroffene Bankkunde können die Beschlagnahme von Kontounterlagen mit einem Siegelungsbegehren blockieren. Private Geheimhaltungsinteressen können ausschliesslich über verfahrensleitende Massnahmen zum Schutz der Privatsphäre (z. B. Einschränkung des Akteneinsichtsrechts Dritter nach Art. 102 und 108 StPO) gewahrt werden ([BGE 151 IV 30 E. 2.4.3](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-151-IV-30_2025.html#consideration_2.4.3)).

### Zivil- und Schuldbetreibungsverfahren {#zivil-schkg}

- **Zivilprozess (ZPO)**: Nach Art. 166 Abs. 1 lit. b ZPO können Dritte die Mitwirkung verweigern, soweit sie Tatsachen dartun, die einem Berufsgeheimnis nach Art. 321 StGB unterstehen. Das Bankgeheimnis fällt nicht darunter; Bankiers können die Aussage oder Urkundenedition nur verweigern, wenn sie glaubhaft machen, dass das Geheimhaltungsinteresse das Interesse an der Wahrheitsfindung überwiegt (Art. 166 Abs. 2 ZPO).
- **Schuldbetreibung und Konkurs (SchKG)**:
  - Im Arrest- und Pfändungsverfahren sind Banken gegenüber den Betreibungsbehörden zur Auskunft verpflichtet, ob verarrestierbare Vermögenswerte vorhanden sind und an welchem Domizil der Schuldner gemeldet ist ([BGE 112 III 6](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_005_BGE-112-III-6_1986-04-10.html#consideration_4.) E. 4). Die blosse Berufung auf das Bankgeheimnis schützt nicht vor Säumnisfolgen ([BGE 104 III 42](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_005_BGE-104-III-42_1978-07-04.html) E. 4c).
  - Im Konkurs einer Bank gilt das Bankgeheimnis gegenüber der Konkursverwaltung nicht: «Einerseits gilt das Bankgeheimnis nicht gegenüber dem Konkursverwalter, sondern wird durch die konkursrechtliche Auskunftspflicht des Gemeinschuldners, also der Bankorgane, ausgeschaltet» ([BGE 86 III 114](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_005_BGE-86-III-114_1960-10-21.html#consideration_1.) E. 1).

### Geldwäschereibekämpfung und Aufsichtsrecht {#geldwaescherei-aufsicht}

- **Geldwäschereigesetz (GwG)**: Nach Art. 9 GwG sind Finanzintermediäre bei begründetem Verdacht auf Geldwäscherei (Art. 305bis StGB) oder Terrorismusfinanzierung gesetzlich verpflichtet, unverzüglich der Meldestelle für Geldwäscherei (MROS) Meldung zu erstatten. Art. 11 GwG schliesst hierfür jede zivil- oder strafrechtliche Verantwortlichkeit wegen Verletzung des Bankgeheimnisses ausdrücklich aus.
- **Finanzmarktaufsicht (FINMAG)**: Banken haben der FINMA alle Auskünfte und Unterlagen herauszugeben, die diese zur Erfüllung ihrer Aufsichtsfunktion benötigt (Art. 29 FINMAG). Gegenüber der Aufsichtsbehörde kann das Bankgeheimnis nicht angerufen werden.

## Der schweizerische Dualismus: Inlands- vs. Auslandstransparenz {#dualismus}

Die historische Entwicklung hat zu einer bemerkenswerten Asymmetrie in der schweizerischen Rechtsordnung geführt:

| Kriterium | Verhältnis zum Ausland (Nicht-Residenten) | Verhältnis im Inland (in der Schweiz Ansässige) |
|---|---|---|
| **Rechtsregime** | Automatischer Informationsaustausch (AIAG) & OECD-Amtshilfe (Art. 26 DBA) | Direkte Bundessteuer (DBG) & kantonale Steuergesetze (StHG) |
| **Erhebung von Bankdaten** | Vollautomatische jährliche Meldung aller Kontosalden, Erträge und Veräusserungserlöse an ausländische Steuerbehörden | Kein automatischer Abgleich; keine direkte Auskunftspflicht der Banken im Veranlagungsverfahren |
| **Auskunftspflicht der Bank** | Unmittelbare Meldepflicht der Finanzinstitute an die ESTV zur Weiterleitung ins Ausland | Schutz durch Art. 127 Abs. 2 Satz 2 DBG: Banken sind gegenüber den Steuerbehörden nicht bescheinigungspflichtig |
| **Durchbrechung bei Steuerdelikten** | Bei jeder Steuerhinterziehung (volle Transparenz) | Nur bei vollendetem oder versuchtem Steuerbetrug im Strafverfahren (Art. 186/190 DBG) |

Dieser Dualismus führt dazu, dass der Schweizer Staat über die Kontoverhältnisse einer in Frankreich oder Deutschland wohnhaften Person lückenlos informiert wird und diese Daten weiterleitet, während eine kantonale Steuerverwaltung bei einem in Zürich oder Bern ansässigen Steuerzahler bei blossem Verdacht auf Steuerhinterziehung keine Bankauskünfte verlangen kann.

## Abgrenzungen {#abgrenzungen}

### Abgrenzung zum klassischen Berufsgeheimnis (Art. 321 StGB) {#abgrenzung-berufsgeheimnis}

Das Bankkundengeheimnis unterscheidet sich in Tragweite und Schutzniveau grundlegend vom Berufsgeheimnis der Ärzte, Anwälte, Notare und Geistlichen:
- **Abschliessender Täterkreis in Art. 321 StGB**: Bankiers und Finanzintermediäre fallen nicht unter Art. 321 StGB:
  > «Zu dem Kreis von Personen, auf welche Art. 321 StGB anwendbar ist, zählen jene nicht, die das Bankgeheimnis zu wahren haben. Die Aufzählung der in Betracht fallenden Berufe ist abschliessend».
  >
  > — [BGE 95 I 439](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_001_BGE-95-I-439_1969-10-01.html#consideration_2.) E. 2c
- **Zeugnisverweigerungsrecht**: Während Träger des Berufsgeheimnisses nach Art. 171 StPO im Strafprozess ein absolutes Zeugnisverweigerungsrecht geniessen (soweit sie nicht entbunden sind), haben Bankorgane und Bankangestellte kein solches Recht. Sie unterstehen der vollen Aussagepflicht gemäss Art. 47 Abs. 5 BankG.
- **Beschlagnahmefreiheit und Siegelung**: Anwalts- und Arztakten unterliegen dem Beschlagnahmeverbot nach Art. 264 Abs. 1 lit. a/c StPO und begründen ein Siegelungsrecht. Bankunterlagen sind beschlagnahmefähig und berechtigen nach der StPO-Revision 2024 nicht mehr zur Siegelung ([BGE 151 IV 30](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-151-IV-30_2025.html#consideration_2.4.1) E. 2.4.1).

### Abgrenzung zu Geschäftsgeheimnis und Amtsgeheimnis {#abgrenzung-geschaefts-amtsgeheimnis}

- **Geschäfts- und Fabrikationsgeheimnis (Art. 162 StGB)**: Schützt das wirtschaftliche Interesse eines Betriebsinhabers an der Geheimhaltung betriebsinterner Tatsachen (z. B. Rezepturen, Kalkulationen). Das Bankkundengeheimnis schützt demgegenüber primär die Privatsphäre des *Kunden* und erst sekundär das Institut.
- **Amtsgeheimnis (Art. 320 StGB / Art. 14 FINMAG)**: Mitarbeitende der Aufsichtsbehörde FINMA und der Schweizerischen Nationalbank (SNB) unterstehen dem Amtsgeheimnis, nicht dem Bankkundengeheimnis ([BGE 137 II 431](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_004_BGE-137-II-431_2011.html#consideration_2.1.1) E. 2.1.1). Sie haben in diesem Rahmen jedoch die schutzwürdigen Berufsgeheimnisse der Beaufsichtigten zu wahren.

## Würdigung {#wuerdigung}

Die Entwicklung des Bankgeheimnisses verdeutlicht die Anpassungsfähigkeit, aber auch die Verwundbarkeit eines nationalen Rechtsinstituts unter dem Einfluss globaler wirtschaftlicher Machtverhältnisse:
1. **Verlust des Mythos, Erhalt des Kerns**: Das Bankgeheimnis hat seinen jahrzehntelangen Mythos als undurchdringliche Festung gegen den weltweiten Steuerfiskus vollständig eingebüsst. Was als Schutz vor Devisenspionage und Verfolgung 1934 begann, wurde im späten 20. Jahrhundert zunehmend zu einem Geschäftsmodell des unversteuerten Offshore-Bankings verzerrt. Mit dem Fall UBS und der Einführung des AIA wurde dieser Aspekt irreversibel beendet.
2. **Dogmatische Bereinigung**: Aus juristischer Sicht hat die Entmystifizierung zu einer dogmatischen Klärung geführt. Das Bankkundengeheimnis wird heute wieder als das verstanden, was es von Beginn an war: ein bürgerlich-rechtlicher Schutz der finanziellen Intimsphäre des Kunden im Rahmen eines privatrechtlichen Auftragsverhältnisses.
3. **Legitimitätskrise im Inland**: Der fortbestehende Dualismus zwischen vollständiger internationaler Steuertransparenz (AIA) und inländischem Schutz vor den eigenen Steuerbehörden steht rechtspolitisch und rechtsgleichheitlich unter permanentem Rechtfertigungsdruck. Während ausländische Staaten automatisiert informiert werden, bleibt der inländische Fiskus auf die Deklarationsdisziplin des Steuerpflichtigen angewiesen.
4. **Entschärfung im Strafprozess**: Die StPO-Revision 2024 hat dem Bankgeheimnis im Strafverfahren die letzte verfahrensverzögernde Bastion genommen. Dass Bankkundendaten nicht mehr gesiegelt werden können ([BGE 151 IV 30](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-151-IV-30_2025.html#consideration_2.4.1)), stellt klar, dass der Schutz des Vermögensgeheimnisses hinter einer effektiven und zügigen Strafrechtspflege zurückzutreten hat.

## Praxishinweise {#praxishinweise}

* **Für Bankkunden im Strafverfahren**: Versuchen Sie nicht, die Edition von Bankunterlagen durch die Staatsanwaltschaft mit einem Siegelungsbegehren nach Art. 248 StPO zu blockieren. Seit dem 1. Januar 2024 weist das Zwangsmassnahmengericht Siegelungsanträge, die sich auf das Bankgeheimnis stützen, gestützt auf [BGE 151 IV 30](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-151-IV-30_2025.html#consideration_2.4.1) und [BGE 151 IV 175](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-151-IV-175_2025.html#consideration_2.4.2) ohne Weiteres ab. Verlangen Sie stattdessen bei der Verfahrensleitung der Staatsanwaltschaft Schutzmassnahmen nach Art. 102 und 108 StPO (z. B. Schwärzung von Drittkontodaten, Beschränkung der Akteneinsicht für Zivilparteien).
* **Für Erben**: Lassen Sie sich von Banken nicht mit dem Hinweis auf das Bankgeheimnis abwimmeln. Als Universalsukzessor (Art. 560 ZGB) rücken Sie vollumfänglich in die Auskunfts- und Rechenschaftsrechte des Erblassers aus Art. 400 Abs. 1 OR ein. Das Bankgeheimnis gilt nach [BGE 133 III 664](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_005_BGE-133-III-664_2007.html#consideration_2.6) nur gegenüber Dritten, niemals gegenüber den Erben. Jeder Miterbe kann diese Auskunft zur Feststellung des Nachlasses selbständig verlangen.
* **Für Bankinstitute und deren Angestellte**: Beachten Sie die erweiterte Strafdrohung von Art. 47 Abs. 1 lit. c und Abs. 1bis BankG. Wer unberechtigt weitergegebene Bankkundendaten entgegennimmt, an Dritte weiterleitet oder für sich verwertet (*Datenhehlerei*), riskiert Freiheitsstrafen bis zu fünf Jahren. Interne Compliance-Vorgaben müssen sicherstellen, dass Whistleblowing ausschliesslich über die gesetzlich geschützten internen Kanäle oder an die Aufsichtsbehörde FINMA erfolgt.
* **Für Steuerpflichtige in der Schweiz**: Das inländische Bankgeheimnis schützt nur vor proaktiven Bankauskünften der Steuerbehörde im ordentlichen Veranlagungsverfahren. Werden gefälschte Belege oder fingierte Darlehensverträge eingereicht, liegt der Verdacht auf Steuerbetrug (Art. 186 DBG) vor. In diesem Fall kann die Behörde gestützt auf Art. 190 DBG den Einblick in Bankunterlagen erzwingen.

## Leitentscheide {#leitentscheide}

| Entscheid | Gegenstand | Kernaussage und Tragweite |
|---|---|---|
| [BGE 137 II 431](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_004_BGE-137-II-431_2011.html#consideration_2.1.1) (2011) | FINMA-Datenherausgabe UBS an US-Behörden | Grundlegende Definition des Bankkundengeheimnisses als Pflicht aus Persönlichkeitsschutz und Vertrag; Verneinung eines absoluten Verfassungsrangs; Zulässigkeit der Datenherausgabe gestützt auf die polizeiliche Generalklausel. |
| [BGE 145 IV 114](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-145-IV-114_2019.html#consideration_3.3.2) (2019) | Geltungsbereich Art. 47 BankG (Fall Elmer / Julius Bär) | Individuelle und institutionelle Dimension des Schutzbereichs; Akzessorietät von Art. 47 BankG zur vertraglichen Treuepflicht (Art. 398 OR); keine extensive Ausdehnung des Täterkreises auf Angestellte von Auslandstöchtern ohne Bankenstatus. |
| [BGE 151 IV 30](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-151-IV-30_2025.html#consideration_2.4.1) (2025) | StPO-Revision 2024 / Entsiegelungsverfahren | Das Bankkundengeheimnis fällt nicht unter die gesetzlichen Geheimnisschutzgründe von Art. 264 StPO und berechtigt nach Art. 248 Abs. 1 StPO nF nicht mehr zur Siegelung. |
| [BGE 151 IV 175](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-151-IV-175_2025.html#consideration_2.4.2) (2025) | Bestätigung Ausschluss Bankgeheimnis von der Siegelung | Bestätigung der Rechtsprechung zu Art. 248 Abs. 1 StPO: Bank- und Geschäftsgeheimnisse berechtigen Dritte nicht zur Siegelung bei strafprozessualer Sicherstellung. |
| [BGE 133 III 664](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_005_BGE-133-III-664_2007.html#consideration_2.5) (2007) | Auskunftsanspruch des Kunden und der Erben (Art. 400 OR) | Übergang der vertraglichen Auskunftsansprüche kraft Universalsukzession (Art. 560 ZGB) auf die Erben; das Bankgeheimnis gilt nur gegenüber Dritten, nicht gegenüber dem Kunden oder dessen Erben. |
| [BGE 95 I 439](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_001_BGE-95-I-439_1969-10-01.html#consideration_2.) (1969) | Bankgeheimnis und Strafprozess | Bankgeheimnis als Ausfluss des Persönlichkeitsschutzes; kein Entbinden von der strafprozessualen Zeugnis- und Editions- bzw. Beschlagnahmepflicht; Abgrenzung zu Art. 321 StGB. |
| [BGE 121 IV 45](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-121-IV-45_1995-03-02.html#consideration_2.) (1995) | Beauftragter i.S.v. Art. 47 BankG (Rechtsanwalt) | Unterstellung des von einer Bank mit der Prozessführung gegen einen Kunden betrauten Rechtsanwalts unter das Bankgeheimnis zur Vermeidung von Schutzlücken. |
| [BGE 125 II 83](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_004_BGE-125-II-83_1998-10-29.html#consideration_5.) (1998) | Börsenaufsichtliche Amtshilfe (Insiderhandel) | Bankgeheimnis hat keinen Verfassungsrang; steht aufsichtsrechtlicher Amtshilfe nicht entgegen, es sei denn, wesentliche Interessen der Schweiz würden durch Aushöhlung berührt. |
| [BGE 119 IV 175](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-119-IV-175_1993-08-16.html#consideration_3.) (1993) | Verwaltungsstrafverfahren (VStrR) / Durchsuchung | Bankgeheimnis verleiht keinen absoluten Anspruch auf Aussageverweigerung oder Aktenverweigerung gegenüber den Untersuchungsbehörden; Reichweite ist geringer als bei Art. 321 StGB. |
| [BGE 86 III 114](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_005_BGE-86-III-114_1960-10-21.html#consideration_1.) (1960) | Konkurs von Banken (SchKG) | Bankgeheimnis gilt nicht gegenüber dem Konkursverwalter; die konkursrechtliche Auskunftspflicht der Bankorgane geht der Geheimhaltungspflicht vor. |
| [BGE 112 III 6](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_005_BGE-112-III-6_1986-04-10.html#consideration_4.) (1986) | Betreibungs- und Arrestverfahren | Auskunftspflicht der Banken gegenüber Betreibungsbehörden über Wohnort oder Zustelldomizil eines Kunden; Bankgeheimnis kann nicht entgegengehalten werden. |
| [BGE 139 II 404](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_004_BGE-139-II-404_2013.html#consideration_7.2.1) (2013) | Steueramtshilfe USA / Gruppenanfragen | Zulässigkeit von Gruppenanfragen nach Art. 26 DBA-USA 96; historische Unterscheidung zwischen Steuerhinterziehung und Steuerbetrug (Lügengebäude) und Übergang zum OECD-Standard. |
| [BGE 143 II 136](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_004_BGE-143-II-136_2017.html#consideration_5.3.4) (2017) | Steueramtshilfe Niederlande / Gruppenersuchen | Zulässigkeit von Gruppenersuchen ohne Namensnennung auf Basis des OECD-Standards nach Art. 26 DBA CH-NL; Abgrenzung zu verbotenen Fishing Expeditions. |
| [BGE 143 II 224](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_004_BGE-143-II-224_2017.html#consideration_6.4) (2017) | Steueramtshilfe und gestohlene Daten (Affäre Falciani) | Völkerrechtlicher Grundsatz von Treu und Glauben und Art. 7 lit. c StAhiG: Verweigerung der Amtshilfe, wenn der ersuchende Staat gestohlene Schweizer Bankdaten aktiv erworben hat. |

## Literatur {#literatur}

* Basler Kommentar zum Bankengesetz, 2. Aufl., Basel 2013, Art. 47 BankG.
* Basler Kommentar zum Obligationenrecht I, 7. Aufl., Basel 2020, Art. 398 OR.
* Maurice Aubert / Jean-Philippe Kernen / Christian Schönle, Le secret bancaire suisse, 3. Aufl., Bern 1995.
* Peter Ch. Kleiner / Renate Schwob / Christoph Winzeler, Kommentar zum Bundesgesetz über die Banken und Sparkassen, Bodmer/Kleiner/Lutz (Hrsg.), Zürich 2009, Art. 47 BankG.
* Rolf H. Weber, Individuelle Geheimhaltung und öffentliche Interessen – ein unüberbrückbares Spannungsfeld?, ZSR 130/2011 I S. 159 ff.
* Christoph Winzeler, Rechtsentwicklungen um das Bankkundengeheimnis, AJP 2010 S. 158 ff.
