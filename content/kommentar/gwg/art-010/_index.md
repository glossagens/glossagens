---
title: "Art. 10 GwG — Vermögenssperre"
weight: 10
date: 2026-10-16
lastmod: 2026-10-16
description: "Praxisorientierter Gesetzeskommentar zu Art. 10 GwG: Die Vermögenssperre des Finanzintermediärs, zweistufiges Melde- und Sperrsystem (Art. 9a vs. Art. 10 Abs. 1), Sofortsperre bei Terror- und Sanktionslisten (Abs. 1bis), 5-tägige Höchstdauer (Abs. 2), Fristenberechnung (Werktage), Abgrenzung zur strafprozessualen Kontosperre (Art. 266 StPO), zivilrechtlicher Haftungsausschluss (Art. 11 GwG, BGE 143 III 653), Schutznormcharakter (BGE 134 III 529), Kasuistik und kantonale Praxis."
tags: ["GwG", "Vermögenssperre", "Meldepflicht", "MROS", "Kontosperre", "Strafprozessrecht", "Haftungsausschluss", "Bankenrecht", "Compliance"]
revisions:
  - date: 2026-10-16
    by: "Glossagens Agent"
    model: "gemini-3.8-flash"
    note: "Vollständige, praxisorientierte Erstkommentierung zu Art. 10 GwG nach den Vorgaben für Praxiskommentare, inkl. Auswertung der Rechtsprechung zu BGE 143 III 653, BGE 134 III 529, BGer 1B_195/2018 sowie kantonaler Obergerichtspraxis (ZH, BE, GR)."
---

## Gesetzeswortlaut

{{< wortlaut >}}

## Überblick und Bedeutung

Art. 10 GwG regelt die Vermögenssperre des Finanzintermediärs und bildet das sichernde Gegenstück zur Meldepflicht nach Art. 9 GwG bzw. zum Melderecht nach Art. 305ter Abs. 2 StGB. Die Bestimmung bezweckt, deliktsbehaftete oder terroristische Vermögenswerte im Schweizer Finanzsektor temporär einzufrieren, um den Strafverfolgungsbehörden den physischen und rechtlichen Zugriff im Hinblick auf eine spätere Einziehung (Art. 70 ff. StGB) oder Rückerstattung an Geschädigte (Art. 73 StGB) zu sichern ([BGE 144 IV 391 E. 3.4](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-144-IV-391_2018.html#consideration_3.4); [BGer 1B_195/2018 vom 7.6.2018 E. 2.2](https://entscheidsuche.ch/docs/CH_BGer/CH_BGer_001_1B-195-2018_2018-06-07.html)).

Historisch sah Art. 10 GwG in seiner Urfassung von 1997 eine automatische und sofortige Vermögenssperre mit jeder Verdachtsmeldung vor. Diese Konzeption erwies sich in der Praxis als problematisch: Sie führte zu einer faktischen Warnung verdächtiger Personen (*Tipping-off*), sobald Kundenaufträge nicht ausgeführt wurden, und trieb Finanzintermediäre in gravierende Haftungsrisiken, wenn die Meldestelle für Geldwäscherei (MROS) die fünftägige Frist ungenutzt verstreichen liess. 

Mit der Revision zur Umsetzung der revidierten FATF-Empfehlungen von 2012 ([BBl 2014 605](https://www.fedlex.admin.ch/eli/fga/2014/100/de); [AS 2015 1389](https://www.fedlex.admin.ch/eli/oc/2015/289/de), in Kraft seit 1. Januar 2016) und der Nachfolgerevision von 2021 ([BBl 2019 5451](https://www.fedlex.admin.ch/eli/fga/2019/1932/de); [AS 2021 656](https://www.fedlex.admin.ch/eli/oc/2021/656/de), in Kraft seit 1. Januar 2023) vollzog der Gesetzgeber einen grundlegenden Systemwechsel hin zum **zweistufigen Melde- und Sperrsystem** («versetzte Vermögenssperre»):
1. **Stufe 1 (Art. 9a GwG)**: Während der MROS-Analysetätigkeit (Art. 23 Abs. 2 GwG) nach einer Meldung gemäss Art. 9 Abs. 1 lit. a GwG oder Art. 305ter Abs. 2 StGB greift *keine* gesetzliche Vermögenssperre. Der Finanzintermediär führt Kundenaufträge grundsätzlich weiter aus, bedeutende Vermögenswerte jedoch nur in einer Form, die eine Rückverfolgung erlaubt (*paper trail*, Art. 9a Abs. 2 GwG).
2. **Stufe 2 (Art. 10 Abs. 1 GwG)**: Die Vermögenssperre wird erst ausgelöst, sobald die MROS dem Finanzintermediär mitteilt, dass sie die gemeldeten Informationen einer Strafverfolgungsbehörde übermittelt hat (Art. 23 Abs. 4 und 5 GwG).
3. **Sonderregime Sofortsperre (Art. 10 Abs. 1bis GwG)**: Bei Terror- und Sanktionslistenübereinstimmungen (Art. 9 Abs. 1 lit. c GwG) bleibt es bei der unverzüglichen Sofortsperre ohne vorherige MROS-Übermittlungsmitteilung.

Die Vermögenssperre ist zeitlich streng limitiert: Sie dauert längstens **fünf Werktage** (Abs. 2) und fällt mit Eintreffen einer behördlichen Anordnung (insbesondere einer Beschlagnahmeverfügung nach Art. 263 StPO) oder mit Fristablauf *ex lege* dahin.

### Prüfschema: Die Tatbestandsmerkmale der Vermögenssperre

Die folgende Tabelle bildet das verbindliche Raster für die rechtliche Prüfung von Art. 10 GwG und dient als Gliederungsplan der vorliegenden Kommentierung:

| Prüfungsschritt / Tatbestandsmerkmal | Gesetzliche Grundlage | Subjektive & Objektive Voraussetzungen | Beweislast & Beweismass |
|---|---|---|---|
| **I. Normadressat: Der Finanzintermediär** | Abs. 1, Abs. 1bis | Qualifikation als Finanzintermediär nach Art. 2 Abs. 2 oder Abs. 3 GwG; keine direkte Geltung für reine Berater/Händler | Voller Beweis der Unterstellung durch Aufsichts- bzw. Strafbehörde |
| **II. Bezugsobjekt: Anvertraute Vermögenswerte und sachliche Konnexität** | Abs. 1, Abs. 1bis | In der Gewahrsame des Intermediärs befindliche Vermögenswerte, die mit der Meldung im Zusammenhang stehen | Objektiver Nachweis der Kontenbeziehung und Konnexität zum Verdachtssachverhalt |
| **III. Auslöser der versetzten Sperre: MROS-Mitteilung über Übermittlung** | Abs. 1 i.V.m. Art. 23 Abs. 4/5 GwG | Eingang der förmlichen Mitteilung der MROS beim Finanzintermediär über Weiterleitung an die Strafverfolgungsbehörde | Zugangsnachweis der behördlichen Mitteilung beim Intermediär |
| **IV. Sofortsperre bei Terror- und Sanktionslisten** | Abs. 1bis i.V.m. Art. 9 Abs. 1 lit. c GwG | Unverzügliche Sperre unmittelbar bei Meldung infolge Namensübereinstimmung mit Sanktions-/Terrorlisten | Nachweis des Listenabgleichs und des Meldungszeitpunkts |
| **V. Dauer und Beendigung: Die Höchstfrist von fünf Werktagen** | Abs. 2 | Max. 5 Werktage ab MROS-Mitteilung (Abs. 1) bzw. Meldung (Abs. 1bis); Samstage/Sonntage/Feiertage zählen nicht | Exakter Nachweis des Fristenlaufs; ex lege Dahinfallen bei Fristablauf |
| **VI. Abgrenzung zur strafprozessualen Kontosperre und Rechtsschutz** | Art. 10 GwG vs. Art. 263 / 266 StPO | Gesetzliche Pflicht des Instituts (GwG) vs. hoheitliche Beschlagnahmeverfügung der Staatsanwaltschaft (StPO) | Differenzierung der Anfechtbarkeit: Zivilrechtsweg vs. Art. 393 StPO |
| **VII. Zivilrechtliche Wirkungen, Haftungsausschluss und Schutznormcharakter** | Art. 11 GwG, Art. 41 OR, Art. 398 OR | Befreiung von Vertrags- und Geheimnishaltungshaftung bei gutem Glauben (Art. 3 ZGB); keine Haftung gegenüber Drittgeschädigten | Gesetzliche Vermutung des guten Glaubens; Beweislast für bösen Glauben beim Kunden |
| **VIII. Verhalten nach Fristablauf: AGB-Sperren, Nötigungsvorwurf und Grundversorgungsauftrag** | Art. 10 Abs. 2 GwG, Art. 181 StGB, Art. 45 VPG | Pflicht zur Transaktionsausführung nach GwG vs. private Pfand-/Sicherungsrechte der Bank; Ausnahmen vom Kontrahierungszwang | Zivilrechtlicher Nachweis berechtigter Gegenansprüche / AGB-Rechte |
| **IX. Kantonale Praxisfragen** | Kantonale Rechtsprechung | Divergenzen bei der Weiterführung von Kontensperren nach Fristablauf und Berechnung lokaler Feiertage | Praxis der kantonalen Beschwerde- und Handelsgerichte |
| **X. Praxishinweise** | Praxiskommentar-Standard | Handlungspflichten für Institute, betroffene Kunden und Strafverfolgungsbehörden | Rollenbezogene Handlungsanweisungen |

---

## Kommentierung

### A. Normadressat: Der Finanzintermediär (Abs. 1 und Abs. 1bis)

#### 1. Dogmatischer Gehalt
Die Pflicht zur Vornahme einer Vermögenssperre nach Art. 10 GwG trifft ausschliesslich **Finanzintermediäre**. Adressaten sind somit die Institute des regulierten Sektors gemäss Art. 2 Abs. 2 GwG (Banken, Wertpapierhäuser, Fondsleitungen, Portfoliomanager, Versicherungen, Spielbanken) sowie Finanzintermediäre des Parabankensektors gemäss Art. 2 Abs. 3 GwG (Kreditinstitute, Zahlungsdienstleister, Vermögensverwalter, Devisen- und Kryptohändler).

Demgegenüber sind **Händlerinnen und Händler** (Art. 2 Abs. 1 lit. b GwG) sowie **Beraterinnen und Berater** (Gatekeeper nach Art. 2 Abs. 1 lit. c GwG in der Fassung der Revision 2026, [AS 2026 322](https://www.fedlex.admin.ch/eli/oc/2026/322/de)) vom persönlichen Anwendungsbereich von Art. 10 GwG ausgenommen. Diese Berufsgruppen verwalten in der Regel keine fremden Kontoguthaben oder Buchwerte. Können sie selbst keine Vermögenswerte sperren, normiert Art. 10a Abs. 2 GwG eine Durchbrechung des Informationsverbots: Sie dürfen denjenigen Finanzintermediär informieren, der die Vermögenswerte verwaltet und in der Lage ist, eine Sperre vorzunehmen.

#### 2. Kasuistik und Judikatur
Verletzt das leitende Personal oder ein Kundenbetreuer einer Bank die Pflicht zur rechtzeitigen Vornahme der Vermögenssperre, drohen neben strafrechtlichen Konsequenzen (Art. 37 GwG) einschneidende aufsichtsrechtliche Massnahmen der FINMA bis hin zum Berufsverbot gemäss Art. 33 FINMAG ([BVGer B-3626/2017 vom 27.11.2019](https://entscheidsuche.ch/docs/CH_BVGer/CH_BVGE_001_B-3626-2017_2019-11-27.pdf)).

> **Lebenssachverhalt zu BVGer B-3626/2017:** Ein Kundenberater einer Schweizer Privatbank betreute komplexe Offshore-Strukturen mit politisch exponierten Personen (PEP). Trotz massiver Warnzeichen und Einleitung einer internen Untersuchung unterliess es die Compliance-Abteilung, eine MROS-Meldung zu erstatten und eine Vermögenssperre nach Art. 10 GwG zu verhängen, während millionenschwere Auszahlungen kurz bevorstanden. Das Bundesverwaltungsgericht bestätigte, dass die Pflicht zur Verhinderung deliktischer Vermögensabflüsse eine persönliche Garantenstellung begründet, die ein aufsichtsrechtliches Tätigkeitsverbot von mehreren Jahren rechtfertigt ([E. 5](https://entscheidsuche.ch/docs/CH_BVGer/CH_BVGE_001_B-3626-2017_2019-11-27.pdf)).

> **Leitsatz.** Die Pflicht zur Vermögenssperre trifft die Organisation des Finanzintermediärs als Gesamtheit. Organe und Compliance-Verantwortliche tragen eine persönliche Garantenpflicht, organisatorisch sicherzustellen, dass eingehende MROS-Übermittlungsmitteilungen bankintern unverzüglich zu einem effektiven Transaktionsstopp führen.

---

### B. Bezugsobjekt: Anvertraute Vermögenswerte und sachliche Konnexität (Abs. 1 und Abs. 1bis)

#### 1. Dogmatischer Gehalt
Gegenstand der Sperre sind die dem Finanzintermediär «anvertrauten Vermögenswerte», die mit der Verdachtsmeldung «im Zusammenhang stehen».
- **Anvertraute Vermögenswerte**: Dies umfasst sämtliche Buchgelder, Einlagen, Wertschriften, Derivate, Edelmetalle und Schrankfächer, über welche der Finanzintermediär die tatsächliche oder rechtliche Verfügungsmacht ausübt.
- **Sachliche Konnexität**: Die Sperre erfasst nicht schematisch sämtliche Kundenbeziehungen einer Person. Zu sperren sind ausschliesslich diejenigen Konten und Subkonten, auf welche sich die konkreten Verdachtsmomente der MROS-Meldung beziehen. Besteht der Verdacht nur bezüglich einer bestimmten Transaktion oder einer isolierten Tranche, stellt sich die Frage der Verhältnismässigkeit einer Teil- gegenüber einer Gesamtsperre.

#### 2. Grenzkasuistik: Erstreckung auf Privatkonten vs. Trennungsprinzip
In der Praxis stellt sich regelmässig die Frage, ob bei einem Verdacht gegen eine juristische Person auch die Privatkonten des wirtschaftlich Berechtigten oder Organs gesperrt werden dürfen.

- **Angewandt (Erstreckung geschützt)**: Im Entscheid [OGer BE BK 2021 210 vom 12.10.2021](https://entscheidsuche.ch/docs/BE_ZivilStraf/BE_OG_008_BK-2021-210_2021-10-12.pdf) hatte eine Bank im Zuge von Unregelmässigkeiten bei einem Covid-19-Kredit über CHF 200'000 nicht nur das Geschäftskonto der Darlehensnehmerin gesperrt, sondern auch das Privatkonto des alleinigen Geschäftsführers suspendiert. Das Obergericht hielt fest, dass wegen monatlicher Lohnüberweisungen eine Vermischung der Gelder stattgefunden habe. Die Bank durfte wegen des Verdachts auf Vermögensdelikte auch das Privatkonto blockieren, ohne sich der Nötigung (Art. 181 StGB) schuldig zu machen ([E. 6.2](https://entscheidsuche.ch/docs/BE_ZivilStraf/BE_OG_008_BK-2021-210_2021-10-12.pdf)).
- **Verworfen (Unverhältnismässige Gesamtsperre)**: Das Bundesstrafgericht betonte in [BStGer BB.2010.17 vom 18.5.2010](https://entscheidsuche.ch/docs/CH_BSTG/CH_BSTG_001_BB-2010-17_2010-05-18.pdf), dass eine Kontosperre verhältnismässig sein muss. Bei betraglich limitierten Verdachtsmomenten ist eine Kontosperre insoweit aufzuheben oder einzuschränken, als dies zur Begleichung fälliger Steuerforderungen oder unaufschiebbarer Lebenshaltungskosten erforderlich ist ([E. 2](https://entscheidsuche.ch/docs/CH_BSTG/CH_BSTG_001_BB-2010-17_2010-05-18.pdf)).

| Merkmal | Vollständige Kontensperre | Teilweise Freigabe / Beschränkung | Entscheid |
|---|---|---|---|
| Konnexität Firmenkredit & Privatkonto | Bejaht bei Lohnzahlungen und Durchmischung (*paper trail*) | Nicht geboten; Gesamtsperre zulässig | [OGer BE BK 2021 210 E. 6.2](https://entscheidsuche.ch/docs/BE_ZivilStraf/BE_OG_008_BK-2021-210_2021-10-12.pdf) |
| Deliktshöhe vs. Gesamtsaldo | Bejaht, wenn Deliktsbetrag den Saldo übersteigt | Geboten, wenn Vermögenswerte den mutmasslichen Deliktserlös massiv übersteigen | [BStGer BB.2020.285 E. 4.2](https://entscheidsuche.ch/docs/CH_BSTG/CH_BSTG_001_BB-2020-285_2021-03-24.pdf) |
| Existenz- und Steuerbedarf | Verneint | Freigabe für nachgewiesene Steuer- und Lebenshaltungsaufwände | [BStGer BB.2010.17 E. 2](https://entscheidsuche.ch/docs/CH_BSTG/CH_BSTG_001_BB-2010-17_2010-05-18.pdf) |

> **Leitsatz.** Die Konnexität erstreckt sich auf alle Vermögenswerte, die nach dem «paper trail» als Surrogat oder Transitstation deliktischer Zuflüsse in Betracht fallen. Eine formale Trennung zwischen Privat- und Geschäftsvermögen greift nicht, wenn Anhaltspunkte für eine Vermögensvermischung vorliegen.

---

### C. Auslöser der versetzten Vermögenssperre: MROS-Mitteilung über Dossierübermittlung (Abs. 1)

#### 1. Dogmatischer Gehalt
Bei Meldungen nach **Art. 9 Abs. 1 lit. a GwG** (Wissen oder begründeter Verdacht auf Geldwäscherei, kriminelle Organisation oder Vortaten) sowie nach **Art. 305ter Abs. 2 StGB** (Melderecht) tritt die Vermögenssperre nicht im Zeitpunkt der Meldungserstattung ein. 

Auslöser ist vielmehr der formelle Zugang der Mitteilung der MROS gemäss Art. 23 Abs. 5 GwG beim Finanzintermediär, dass die gemeldeten Informationen an eine Strafverfolgungsbehörde übermittelt wurden (Art. 23 Abs. 4 GwG).
- Bis zum Eingang dieser Mitteilung gilt Art. 9a GwG: Kundenaufträge sind grundsätzlich auszuführen. Ein eigenmächtiges, präventives Einfrieren des Kontos durch die Bank stützt sich nicht auf Art. 10 Abs. 1 GwG.
- Sobald die Übermittlungsmitteilung eintrifft, wandelt sich die Rechtspflicht um: Der Finanzintermediär muss jede Ausführung von Kundenaufträgen bezüglich der betroffenen Vermögenswerte mit sofortiger Wirkung blockieren.

#### 2. Kasuistik: Verzögerung von Kundenaufträgen vor MROS-Mitteilung
In [BGE 143 III 653](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_005_BGE-143-III-653_2017.html) rügte der Kunde, die Bank habe seinen Transferauftrag über EUR 3 Mio. bereits während der internen Abklärungen vor der Meldung und vor der MROS-Übermittlung verzögert und dadurch eine Konventionalstrafe von EUR 250'000 verursacht.

> **Wörtliche Erwägung aus BGE 143 III 653 E. 4.5.2:**  
> «Lorsqu'il fait valoir que l'inexécution immédiate de son ordre et le blocage préventif de ses avoirs durant un mois ne reposent sur aucune base légale, dès lors qu'un blocage ne peut intervenir qu'après une communication au MROS, il se méprend sur le sens des art. 9 et 10 LBA-2010 en lien avec la clarification que l'art. 6 al. 2 let. a LBA-2010 impose à la banque et le nécessaire sursis à l'exécution de l'ordre de transfert qui en résulte. Or, il n'a ni质疑 ni prouvé la mauvaise foi de la banque, que ce soit au moment d'effectuer la dénonciation au MROS [...] ou lors de la procédure de clarification préalable.»

Das Bundesgericht stellte klar: Zwar greift Art. 10 Abs. 1 GwG erst mit der MROS-Mitteilung, doch verlangt die vorgängige Abklärungspflicht nach Art. 6 GwG notwendigerweise einen faktischen Aufschub der Transaktionsausführung (*sursis à l'exécution*), der die Bank nicht haftbar macht, solange sie in gutem Glauben handelt.

> **Leitsatz.** Vor Zugang der MROS-Übermittlungsmitteilung besteht keine öffentlich-rechtliche Vermögenssperre nach Art. 10 Abs. 1 GwG. Erforderliche interne Abklärungen nach Art. 6 GwG gebieten jedoch einen temporären Transaktionsaufschub, welcher durch Art. 11 GwG haftungsrechtlich gedeckt ist.

---

### D. Sofortsperre bei Terror- und Sanktionslisten (Abs. 1bis)

#### 1. Dogmatischer Gehalt
Art. 10 Abs. 1bis GwG durchbricht das Konzept der versetzten Vermögenssperre für Verdachtsmeldungen nach **Art. 9 Abs. 1 lit. c GwG**. Stimmen die Daten einer Geschäftsbeziehung mit Sanktions- oder Terrorlisten überein, die dem Finanzintermediär gestützt auf Art. 22a Abs. 2 oder 3 GwG übermittelt wurden, greift die **Sofortsperre**:
- Der Finanzintermediär sperrt die anvertrauten Vermögenswerte **unverzüglich** bei Vornahme der Meldung.
- Eine Analysephase der MROS findet in diesem Kontext nicht statt; das Übermittlungsrisiko wird im Interesse der internationalen Terrorismusbekämpfung und Sanktionsdurchsetzung vorrangig gewichtet.

#### 2. Kasuistik: Embargogesetzgebung und Grundversorgungsauftrag
Im Urteil [HG Bern HG 2024 108 vom 5.11.2025](https://entscheidsuche.ch/docs/BE_ZivilStraf/BE_OG_002_HG-2024-108_2025-11-05.pdf) forderte eine Rohstoffhandelsgesellschaft mit Sitz in der Schweiz, die über zypriotische Holdings von sanktionierten russischen Staatsangehörigen kontrolliert wurde, die Eröffnung eines Zahlungskontos gestützt auf den gesetzlichen Grundversorgungsauftrag der PostFinance (Art. 32 PG, Art. 43 VPG).

Das Handelsgericht wies die Klage ab: PostFinance durfte die Geschäftsbeziehung gestützt auf Art. 45 Abs. 1 VPG verweigern. Drohende Verstösse gegen internationale Sanktionen (OFAC/US-Recht, SECO) und die daraus resultierenden Pflichten zur Vermögensblockierung gemäss GwG und Embargorecht schliessen einen Kontrahierungszwang aus ([E. 18 f.](https://entscheidsuche.ch/docs/BE_ZivilStraf/BE_OG_002_HG-2024-108_2025-11-05.pdf)).

> **Leitsatz.** Ergibt der Abgleich mit behördlichen Sanktions- oder Terrorlisten eine Namensidentität, ist die Vermögenssperre zeitgleich mit der MROS-Meldung auszulösen. Eine vorgängige Kontaktnahme mit der Kundschaft oder ein Zuwarten auf eine behördliche Bestätigung ist unzulässig.

---

### E. Dauer und Beendigung: Die Höchstfrist von fünf Werktagen (Abs. 2)

#### 1. Dogmatischer Gehalt
Die Vermögenssperre nach Art. 10 GwG ist eine vorläufige Massnahme mit strikter gesetzlicher Befristung. Gemäss Abs. 2 darf sie **längstens fünf Werktage** aufrechterhalten werden.

Fristenlauf:
- **Im Fall von Abs. 1**: Die Frist beginnt in dem Zeitpunkt, in dem dem Finanzintermediär die Mitteilung der MROS über die Dossierübermittlung zugeht.
- **Im Fall von Abs. 1bis**: Die Frist beginnt im Zeitpunkt, in dem der Finanzintermediär die Meldung nach Art. 9 Abs. 1 lit. c GwG an die MROS absetzt.
- **Beendigungstatbestände**:
  1. *Fristablauf*: Verstreichen fünf Werktage, ohne dass eine Verfügung der Strafverfolgungsbehörde eintrifft, fällt die Sperre *ex lege* dahin.
  2. *Behördliche Verfügung*: Trifft vor Fristablauf eine Verfügung der Strafverfolgungsbehörde ein (z.B. Beschlagnahmeverfügung nach Art. 263 StPO oder Nichtanhandnahmeverfügung nach Art. 310 StPO), wird die verwaltungsrechtliche Sperre durch den prozessualen Hoheitsakt abgelöst.

#### 2. Fristenberechnung: Werktage vs. Kalendertage
Das Gesetz spricht ausdrücklich von «Werktagen» (*jours ouvrables*, *giorni lavorativi*), nicht von Kalendertagen. 

> **Kasuistik zu KG GR SB 2003 63:**  
> Das Kantonsgericht Graubünden hielt im Urteil [SB 2003 63 vom 9.6.2004](https://entscheidsuche.ch/docs/GR_Gerichte/GR_KG_004_SB-2003-63_2004-06-09.pdf) fest, dass Samstage, Sonntage und am Sitz des Finanzintermediärs anerkannte Feiertage bei der Berechnung der Frist von Art. 10 Abs. 2 GwG nicht mitgezählt werden dürfen. Fällt die MROS-Mitteilung auf einen Freitag, laufen die fünf Werktage erst mit dem darauffolgenden Freitag ab ([E. 3](https://entscheidsuche.ch/docs/GR_Gerichte/GR_KG_004_SB-2003-63_2004-06-09.pdf)).

#### 3. Rechtslage nach Fristablauf
Ergeht innert fünf Werktagen keine Verfügung der Staatsanwaltschaft, hat der Finanzintermediär gestützt auf Art. 10 GwG **weder die Pflicht noch die Berechtigung**, die Vermögenssperre weiter aufrechtzuerhalten ([OGer ZH UE140091 vom 2.2.2015 E. 5.2](https://entscheidsuche.ch/docs/ZH_Obergericht/ZH_OG_002_UE140091_2015-02-02.pdf)).

> **Wörtliche Erwägung aus OGer ZH UE140091 E. 5.2:**  
> «Ergeht innerhalb der fünftägigen Frist seitens der Strafverfolgungsbehörde keine Verfügung, welche die Vermögenssperre aufrechterhält, kann der Finanzintermediär nach eigenem Ermessen entscheiden, ob und in welchem Rahmen er die Geschäftsbeziehung weiterführen will [...]. Treten keine neuen Sachverhaltselemente hinzu, hat der Finanzintermediär in diesem Fall weder die Pflicht noch die Berechtigung, die Vermögenssperre aufrechtzuerhalten, sondern hat die vom Kunden verlangte Transaktion auszuführen. Dabei ist er aber an die Sorgfaltspflicht, insbesondere an die Dokumentationspflicht (paper trail) nach Art. 7 GwG gebunden.»

> **Leitsatz.** Die Fünftagefrist bemisst sich nach Werktagen am Sitz des Finanzinstituts. Bleibt die Strafverfolgungsbehörde innert dieser Frist untätig, entfällt die öffentlich-rechtliche Sperrwirkung des GwG vollständig; eine weitere Blockierung der Kundengelder lässt sich nicht mehr auf Art. 10 GwG stützen.

---

### F. Abgrenzung zur strafprozessualen Kontosperre und Rechtsschutz (Art. 263, 266 StPO)

#### 1. Dogmatischer Gehalt
In der forensischen Praxis wird die Vermögenssperre nach Art. 10 GwG häufig mit der Kontosperre nach Art. 266 Abs. 4 StPO verwechselt. Die Institute unterscheiden sich grundlegend:

| Kriterium | Vermögenssperre nach Art. 10 GwG | Strafprozessuale Kontosperre (Art. 263 / 266 Abs. 4 StPO) |
|---|---|---|
| **Rechtsnatur** | Gesetzliche Unterlassungspflicht des Finanzinstituts | Hoheitliche Zwangsmassnahme (Forderungsbeschlagnahme) |
| **Anordnende Stelle** | Handeln des Finanzintermediärs (automatisch / gesetzlich) | Formelle Verfügung der Staatsanwaltschaft / des Gerichts |
| **Dauer** | Max. 5 Werktage (provisorisch) | Bis zum Abschluss des Strafverfahrens bzw. Aufhebung |
| **Rechtsmittel** | Zivilklage auf Vertragserfüllung (Art. 398 OR); keine StPO-Beschwerde | Beschwerde in Strafsachen an kantonale Beschwerdeinstanz (Art. 393 StPO) |
| **Eröffnungspflicht** | Fällt unter das Informationsverbot (Art. 10a GwG) | Schriftliche Eröffnung an Kontoinhaber (Art. 199, 263 StPO; [BGer 1B_195/2018 E. 2.3](https://entscheidsuche.ch/docs/CH_BGer/CH_BGer_001_1B-195-2018_2018-06-07.html)) |

#### 2. Kasuistik: BGer 1B_195/2018
Im Urteil [BGer 1B_195/2018 vom 7.6.2018](https://entscheidsuche.ch/docs/CH_BGer/CH_BGer_001_1B-195-2018_2018-06-07.html) überwies ein Beschuldigter EUR 500'000 aus einem mutmasslichen Betrugs- und Geldwäschereikomplex (Offshore-Zahlungen aus Curaçao über EUR 3.5 Mio.) an die Gesellschaft seiner Lebenspartnerin, welche den Betrag auf ihr Privatkonto transferierte. Die Staatsanwaltschaft Basel-Stadt verfügte eine Kontosperre über EUR 500'000, welche die Bank der Kontoinhaberin mitteilte. Die Inhaberin rügte das Fehlen einer rechtswirksamen StPO-Beschlagnahme.

> **Wörtliche Erwägung aus BGer 1B_195/2018 E. 2.2:**  
> «Für eine Kontosperre kommen verschiedene Rechtsgrundlagen in Betracht. So statuiert insbesondere Art. 10 des Bundesgesetzes über die Bekämpfung der Geldwäscherei [...] die Pflicht des Finanzintermediärs, Vermögenswerte zu sperren, die Gegenstand einer Meldung nach Art. 9 GwG bilden. Davon zu unterscheiden ist die Kontosperre im Strafprozessrecht, welche von der Staatsanwaltschaft als Strafverfolgungsbehörde verfügt werden kann. Sie bedeutet die Beschlagnahme einer Forderung, welche einer beschuldigten Person oder einer Drittperson gegenüber einem Finanzinstitut zusteht. [...] Die strafprozessuale Kontosperre stellt damit eine besondere Vollzugsform der Forderungsbeschlagnahme gemäss Art. 266 Abs. 4 StPO dar [...].»

Das Bundesgericht bestätigte die Kontosperre. Es stellte klar, dass eine unterbliebene direkte Eröffnung der Verfügung durch die Staatsanwaltschaft die Massnahme nicht nichtig macht, sondern lediglich dazu führt, dass die zehntägige Beschwerdefrist nach Art. 396 Abs. 1 StPO erst ab dem Zeitpunkt tatsächlicher Kenntnisnahme zu laufen beginnt ([E. 2.3](https://entscheidsuche.ch/docs/CH_BGer/CH_BGer_001_1B-195-2018_2018-06-07.html)).

> **Leitsatz.** Gegen die Vornahme einer Vermögenssperre nach Art. 10 GwG steht kein strafprozessuales Rechtsmittel nach Art. 393 StPO zur Verfügung. Der strafprozessuale Rechtsschutz greift erst in dem Moment, in welchem die Staatsanwaltschaft eine formelle Beschlagnahmeverfügung erlässt.

---

### G. Zivilrechtliche Wirkungen, Haftungsausschluss und Schutznormcharakter (Art. 11 GwG, BGE 143 III 653, BGE 134 III 529)

#### 1. Ausschluss vertraglicher Haftung (Art. 11 Abs. 1 GwG)
Verweigert ein Finanzintermediär in Ausführung von Art. 10 GwG die Durchführung von Überweisungen, verstösst er vordergründig gegen seine vertragliche Leistungspflicht aus dem Giro- oder Kontokorrentvertrag (Art. 398 Abs. 2, Art. 475 OR).

Art. 11 Abs. 1 GwG schliesst die vertragliche Haftung sowie die Strafbarkeit wegen Geheimnisverletzung (Art. 273, 320, 321 StGB, Art. 47 BankG) aus, sofern der Finanzintermediär **guten Glaubens** gehandelt hat.
- **Definition des guten Glaubens (Art. 3 ZGB)**: Nach [BGE 143 III 653 E. 4.3.3](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_005_BGE-143-III-653_2017.html) handelt die Bank gutgläubig, wenn sie in gutem Gewissen agiert und jedes unredliche oder moralisch verwerfliche Verhalten ausgeschlossen werden kann.
- **Gesetzliche Vermutung (Art. 3 Abs. 1 ZGB)**: Der gute Glaube wird gesetzlich vermutet. Der Kunde, der Schadenersatz wegen einer Kontosperre verlangt, trägt die volle Beweislast für den bösen Glauben der Bank oder für Umstände, die es ihr nach Art. 3 Abs. 2 ZGB verwehren, sich auf ihren guten Glauben zu berufen.

#### 2. Fehlen des Schutznormcharakters für Drittgeschädigte (BGE 134 III 529)
In der Praxis versuchen häufig Opfer von Anlagebetrug oder Veruntreuung, die Bank des Täters haftbar zu machen, weil diese die verdächtigen Konten nicht rechtzeitig gemäss Art. 10 GwG gesperrt habe, wodurch die Gelder abfliessen konnten.

In [BGE 134 III 529](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_005_BGE-134-III-529_2008.html) und im Urteil [BGer 4A_21/2008 vom 13.6.2008](https://entscheidsuche.ch/docs/CH_BGer/CH_BGer_004_4A-21-2008_2008-06-13.html) wies das Bundesgericht solche Schadenersatzklagen aus Art. 41 Abs. 1 OR ab.

> **Wörtliche Erwägung aus BGE 134 III 529 E. 4.3:**  
> «Visant à protéger l'intégrité de la place financière suisse, les dispositions de la LBA ne sont pas des normes de comportement qui servent à protéger des valeurs patrimoniales individuelles et, partant, ne sont pas susceptibles de fonder une responsabilité civile délictuelle au sens de l'art. 41 CO. Les infractions seront susceptibles d'être réprimées par le juge pénal si les conditions objectives d'un délit pénal sont réalisées [...].»

Auch das Handelsgericht Zürich bestätigte im Entscheid [HG160258 vom 8.5.2019 E. 3.1](https://entscheidsuche.ch/docs/ZH_Obergericht/ZH_HG_001_HG160258_2019-05-08.pdf), dass die Bestimmungen des GwG dem Schutz des Gemeinwesens und der Integrität des Finanzplatzes dienen und geschädigten Dritten keinen zivilrechtlichen Anspruch auf Vornahme einer Kontosperre verleihen.

> **Leitsatz.** Art. 10 GwG ist keine Schutznorm zugunsten von Drittgeschädigten im Sinne von Art. 41 Abs. 1 OR. Bei Streitigkeiten zwischen Bank und Kontoinhaber greift die gesetzliche Vermutung des guten Glaubens gemäss Art. 11 GwG i.V.m. Art. 3 Abs. 1 ZGB; blosse Fehlbeurteilungen begründen keine Haftung.

---

### H. Verhalten nach Fristablauf: AGB-Sperren, Nötigungsvorwurf und Grundversorgungsauftrag

#### 1. Die Kollision zwischen GwG-Fristablauf und privatem Pfandrecht
Läuft die fünftägige Frist von Art. 10 Abs. 2 GwG ohne staatsanwaltschaftliche Verfügung ab, befindet sich die Bank in einem Dilemma: Führt sie den Auftrag aus, riskiert sie den Vorwurf der Geldwäscherei (Art. 305bis StGB), falls die Gelder deliktisch sind. Verweigert sie die Auszahlung, rügt der Kunde eine Vertragsverletzung (Art. 398 OR) oder erstattet Strafanzeige wegen Nötigung (Art. 181 StGB).

Die kantonale Praxis löst dieses Spannungsverhältnis über die **Allgemeinen Geschäftsbedingungen (AGB)** der Banken:
- Banken bedingen sich in ihren AGB regelmässig ein umfassendes Pfand- und Verrechnungsrecht für sämtliche bestehenden oder künftigen Schadenersatzansprüche aus der Geschäftsbeziehung aus (z.B. drohende Bussen oder Kosten infolge Falschangaben des Kunden).
- Das Obergericht Zürich erkannte in [UE140091 vom 2.2.2015 E. 6.2](https://entscheidsuche.ch/docs/ZH_Obergericht/ZH_OG_002_UE140091_2015-02-02.pdf), dass sich die Bank nach Ablauf der Frist von Art. 10 Abs. 2 GwG zwar nicht mehr auf das GwG berufen kann, eine Weiterführung der Kontoblockierung gestützt auf das vertragliche AGB-Pfandrecht jedoch die Rechtswidrigkeit einer Nötigung (Art. 181 StGB) entfallen lässt.
- Dasselbe bestätigte das Obergericht Bern in [BK 2021 210 E. 6.3](https://entscheidsuche.ch/docs/BE_ZivilStraf/BE_OG_008_BK-2021-210_2021-10-12.pdf): Die Verweigerung von Auszahlungen stellt keine Nötigung dar, da der Kontosaldo bloss einen obligatorischen Rückforderungsanspruch bildet, den der Kunde auf dem ordentlichen Zivilweg durchzusetzen hat.

#### 2. Echter Judikatur- und Wertungswiderspruch: GwG vs. Zivilrecht
Es besteht eine offene Divergenz zwischen dem öffentlich-rechtlichen Zweck des GwG und der zivilrechtlichen Praxis:
- **Aufsichts- und strafrechtlicher Zweck**: Der Gesetzgeber wollte mit der strikten Begrenzung auf fünf Werktage in Art. 10 Abs. 2 GwG verhindern, dass Banken ohne richterlichen Beschluss monatelang Konten einfrieren. Die Botschaft ([BBl 2014 605, S. 637](https://www.fedlex.admin.ch/eli/fga/2014/100/de)) betont, dass die Vermögenssperre nach Fristablauf ohne richterliche Beschlagnahme zwingend endet.
- **Kantonale Gerichtspraxis**: Die Obergerichte (ZH, BE) hebeln diesen gesetzlichen Schutz faktisch aus, indem sie den Banken zubilligen, dieselbe Kontosperre nahtlos als «zivilrechtliches Pfandrecht» oder «interne Compliance-Sperre» auf unbestimmte Zeit weiterzuführen, ohne dass Strafgerichte wegen Nötigung einschreiten. Der Kunde wird auf den langwierigen Zivilprozessweg (z.B. Gesuch um vorsorgliche Massnahmen nach Art. 261 ZPO) verwiesen.

> **Leitsatz.** Führt ein Finanzinstitut die Kontensperre nach Ablauf der Frist von Art. 10 Abs. 2 GwG gestützt auf seine AGB weiter, entfällt der öffentlich-rechtliche Schutz von Art. 10 GwG. Strafrechtlich liegt darin zwar regelmässig keine Nötigung (Art. 181 StGB); zivilrechtlich haftet das Institut jedoch nach Art. 97 ff. OR, wenn es das Bestehen einer echten Pfand- oder Gegenforderung nicht substanziieren kann.

---

### I. Kantonale Praxisfragen

#### 1. Praxisfrage 1: Strafanzeige wegen Nötigung (Art. 181 StGB) bei eigenmächtiger Kontosperrung
In der Praxis reagieren Kunden auf Kontoblockierungen häufig mit einer Strafanzeige wegen Nötigung gegen die involvierten Bankmitarbeiter.
- **Kantonale Praxis (ZH, BE)**: Die Staatsanwaltschaften und Obergerichte treten auf solche Anzeigen regelmässig mit Nichtanhandnahmeverfügungen gemäss Art. 310 Abs. 1 lit. a StPO ein ([OGer ZH UE140091 E. 2](https://entscheidsuche.ch/docs/ZH_Obergericht/ZH_OG_002_UE140091_2015-02-02.pdf); [OGer BE BK 2021 210 E. 4](https://entscheidsuche.ch/docs/BE_ZivilStraf/BE_OG_008_BK-2021-210_2021-10-12.pdf)). Da Bankguthaben im Eigentum der Bank stehen und der Kunde lediglich einen schuldrechtlichen Forderungsanspruch besitzt, erfüllt das Nichthonorieren einer Zahlungsanweisung mangels physischer Zwangseinwirkung grundsätzlich keinen Nötigungstatbestand.
- **Prozessuale Konsequenz**: Betroffene Kunden können Kontensperren nicht über den Strafweg aufbrechen, sondern müssen zivilrechtliche Rechtsschutzgesuche (Art. 261 ZPO) beim zuständigen Zivil- oder Handelsgericht einreichen.

#### 2. Praxisfrage 2: Bestimmung des Fristenlaufs bei kantonalen Feiertagen
Die Frist von Art. 10 Abs. 2 GwG bemisst sich nach Werktagen. Da die Feiertagsgesetzgebung kantonal geregelt ist (Art. 20a ArG), variiert die Anzahl der Werktage je nach Standort der Buchungsfiliale.
- Nach der Bündner Rechtsprechung ([KG GR SB 2003 63 E. 3](https://entscheidsuche.ch/docs/GR_Gerichte/GR_KG_004_SB-2003-63_2004-06-09.pdf)) sind kantonale Feiertage am Sitz der Geschäftsstelle, bei welcher die Kundenbeziehung geführt wird, fristverlängernd zu berücksichtigen.
- Fällt ein Feiertag in die fünftägige Frist, verlängert sich die Sperrpflicht der Bank exakt um diese Tage. Dies erfordert von Compliance-Diensten eine präzise Erfassung der Feiertagskalender der jeweiligen Niederlassung.

---

### J. Praxishinweise

**Für Finanzintermediäre und Compliance-Verantwortliche:**

1. **Keine verfrühte Kontensperre:** Bei Meldungen nach Art. 9 Abs. 1 lit. a GwG und Art. 305ter Abs. 2 StGB vor Zugang der MROS-Übermittlungsmitteilung keine Vermögenssperre nach Art. 10 Abs. 1 GwG verhängen. Transaktionen nach Art. 9a GwG unter Wahrung des *paper trail* ausführen ([BGE 143 III 653 E. 4.3.1](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_005_BGE-143-III-653_2017.html)).
2. **Sofortiger Transaktionsstopp bei MROS-Mitteilung:** Sobald die Mitteilung über die Weiterleitung an die Strafverfolgungsbehörde eintrifft, das Konto unverzüglich mit einer technischen Sperre belegen. Den genauen Zeitpunkt (Datum und Uhrzeit) des Eingangs manipulationssicher im System protokollieren.
3. **Fristenüberwachung der 5 Werktage:** Den Fristablauf taggenau nach Werktagen des Standorts der Niederlassung berechnen ([KG GR SB 2003 63 E. 3](https://entscheidsuche.ch/docs/GR_Gerichte/GR_KG_004_SB-2003-63_2004-06-09.pdf)). Samstage, Sonntage und Feiertage ausklammern.
4. **Vorgehen bei Fristablauf:** Trifft am fünften Werktag bis Geschäftsschluss keine Verfügung der Staatsanwaltschaft ein, entfällt die Sperre nach Art. 10 GwG automatisch ([OGer ZH UE140091 E. 5.2](https://entscheidsuche.ch/docs/ZH_Obergericht/ZH_OG_002_UE140091_2015-02-02.pdf)). Soll das Konto weiter blockiert werden, muss dies unverzüglich auf zivilrechtliche AGB-Klauseln (Pfand- und Verrechnungsrechte) umgestellt und gegenüber der Geschäftsleitung begründet werden.
5. **Strikes Tipping-off-Verbot:** Unter keinen Umständen dem Kunden oder Dritten mitteilen, dass eine MROS-Mitteilung vorliegt oder eine GwG-Sperre verhängt wurde (Art. 10a GwG). Auf Kundenanfragen ausschliesslich auf interne Prüfungen oder AGB-Bestimmungen verweisen.

**Für betroffene Kundinnen, Kunden und deren Rechtsvertretung:**

1. **Kein Strafantrag wegen Nötigung:** Keine Strafanzeigen wegen Art. 181 StGB gegen Bankmitarbeiter einreichen. Solche Verfahren werden von den kantonalen Staatsanwaltschaften mangels Rechtswidrigkeit ausnahmslos nicht an die Hand genommen ([OGer ZH UE140091 E. 2](https://entscheidsuche.ch/docs/ZH_Obergericht/ZH_OG_002_UE140091_2015-02-02.pdf); [OGer BE BK 2021 210 E. 6.3](https://entscheidsuche.ch/docs/BE_ZivilStraf/BE_OG_008_BK-2021-210_2021-10-12.pdf)).
2. **Schriftliche Leistungsaufforderung mit Fristansetzung:** Die Bank schriftlich unter Fristansetzung zur Ausführung des Zahlungsauftrags auffordern und für den Verzugsfall Schadenersatz androhen. Damit wird der gute Glaube der Bank nach Art. 11 GwG für die Zeit nach Fristablauf erschüttert ([BGE 143 III 653 E. 4.3.3](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_005_BGE-143-III-653_2017.html)).
3. **Zivilrechtliche Massnahme beantragen:** Bei fortdauernder Blockade nach Ablauf von fünf Werktagen unverzüglich ein Gesuch um Erlass vorsorglicher Massnahmen (Art. 261 ZPO) auf Freigabe des Guthabens beim Handels- oder Zivilgericht einreichen.
4. **Strafprozessuale Beschwerde nach Art. 393 StPO:** Sobald eine Beschlagnahmeverfügung der Staatsanwaltschaft eintrifft, innert 10 Tagen Beschwerde an die kantonale Beschwerdekammer erheben ([BGer 1B_195/2018 E. 1.1](https://entscheidsuche.ch/docs/CH_BGer/CH_BGer_001_1B-195-2018_2018-06-07.html)). Bei Existenzgefährdung unverzüglich ein Gesuch um Teilfreigabe für Lebenshaltungs- und Steuerkosten stellen ([BStGer BB.2010.17 E. 2](https://entscheidsuche.ch/docs/CH_BSTG/CH_BSTG_001_BB-2010-17_2010-05-18.pdf)).

**Für Strafverfolgungsbehörden und die MROS:**

1. **Fristendisziplin einhalten:** Die MROS-Mitteilung an den Finanzintermediär zeitgleich mit der Übermittlung an die zuständige Staatsanwaltschaft absenden, um den Fünftage-Countdown zu synchronisieren.
2. **Rechtzeitige Beschlagnahmeverfügung:** Die Staatsanwaltschaft muss innert der fünf Werktage eine formelle Beschlagnahmeverfügung (Art. 263 StPO) erlassen und der Bank zustellen. Ein Zuwarten führt zum zwingenden Dahinfallen der Sicherung nach Art. 10 Abs. 2 GwG.
3. **Eröffnung an den Betroffenen:** Die Kontosperre dem Kontoinhaber unverzüglich schriftlich eröffnen (Art. 199 StPO), es sei denn, ein formelles Mitteilungsverbot ist aus Untersuchungsgründen zwingend erforderlich ([BGer 1B_195/2018 E. 2.3](https://entscheidsuche.ch/docs/CH_BGer/CH_BGer_001_1B-195-2018_2018-06-07.html)).
