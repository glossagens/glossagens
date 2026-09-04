---
title: "Art. 141 — Verwertbarkeit rechtswidrig erlangter Beweise"
weight: 141
date: "2026-05-09"
lastmod: "2026-09-04"
description: "Praxiskommentar zu Art. 141 StPO – Beweisverwertungsverbot: dreistufiges System und Fernwirkung mit ausführlicher Kasuistik zu PIN-Erfragung, verdeckter Ermittlung, Landfriedensbruch/Dashcam, Gültigkeits- vs. Ordnungsvorschriften und Aktenbereinigung"
tags: ["StPO", "Beweisverwertungsverbot", "Fernwirkung", "Beweisrecht", "Praxiskommentar", "nemo tenetur", "verdeckte Ermittlung", "Gültigkeitsvorschrift"]
agent_verified: true
revisions:
  - date: 2026-09-04
    by: "Claude Code"
    model: "claude-sonnet-5"
    mcp_verified: true
    note: "Praxisorientierter Ausbau (Skill praxisorientierter-kommentar): narrative Sachverhaltsschilderungen zu BGE 151 IV 73, 148 IV 205, 147 IV 9, 147 IV 16, 151 IV 18, 139 IV 128 und BGer 7B_1429/2025 ergänzt, Judikaturspannung Gültigkeits-/Ordnungsvorschrift offengelegt, Kasuistiktabellen und Merksätze eingefügt. Gesetzestext unverändert aus Vorrevision übernommen (bereits Fedlex-verifiziert); alle neu ausgewerteten Entscheide im Volltext über opencaselaw geprüft, Verlinkung auf entscheidsuche.ch umgestellt (CLAUDE.md-Vorgabe vom 29.08.2026)."
  - date: 2026-08-14
    by: "Hermes Agent"
    model: "glm-5.1"
    mcp_verified: true
    note: "BGer-Update: BGer 7B_1429/2025 (SkyECC-Daten, Aktenbereinigung, Zwischenentscheid) ergaenzt. check_claim_support: partial (Kontextzitat zu Art. 141 Abs. 5). Alle 23+22 OCL-Links verifiziert (HTTP 200)."
  - date: 2026-08-13
    by: "Hermes Agent"
    model: "glm-5.1"
    mcp_verified: true
    note: "Voll-Audit Schritt 1-6: Gesetzestext mit Fedlex (SR 312.0) verifiziert, alle OCL-Links geprueft (HTTP 200), Frontmatter aktualisiert."
---

## Gesetzeswortlaut

> **Art. 141 StPO — Verwertbarkeit rechtswidrig erlangter Beweise**
>
> 1 Beweise, die in Verletzung von Artikel 140 erhoben wurden, sind in keinem Falle verwertbar. Dasselbe gilt, wenn dieses Gesetz einen Beweis als unverwertbar bezeichnet.
>
> 2 Beweise, die Strafbehörden in strafbarer Weise oder unter Verletzung von Gültigkeitsvorschriften erhoben haben, dürfen nicht verwertet werden, es sei denn, ihre Verwertung sei zur Aufklärung schwerer Straftaten unerlässlich.
>
> 3 Beweise, bei deren Erhebung Ordnungsvorschriften verletzt worden sind, sind verwertbar.
>
> 4 Ermöglichte ein Beweis, der nach Absatz 1 oder 2 nicht verwertet werden darf, die Erhebung eines weiteren Beweises, so ist dieser nur dann verwertbar, wenn er auch ohne die vorhergehende Beweiserhebung möglich gewesen wäre.
>
> 5 Die Aufzeichnungen über unverwertbare Beweise werden aus den Strafakten entfernt, bis zum rechtskräftigen Abschluss des Verfahrens unter separatem Verschluss gehalten und danach vernichtet.

## Die drei Stufen auf einen Blick

| Absatz | Was wurde verletzt? | Rechtsfolge | Korrektur über Interessenabwägung möglich? |
|---|---|---|---|
| **Abs. 1** | Art. 140 StPO (verbotene Vernehmungsmethode) oder eine gesetzliche Unverwertbarkeitsanordnung | **Absolutes** Verwertungsverbot | **Nein** — auch die Aufklärung schwerster Straftaten rechtfertigt die Verwertung nicht |
| **Abs. 2** | Strafbare Beweiserhebung oder eine **Gültigkeitsvorschrift** | **Relatives** Verwertungsverbot | Ja — wenn zur Aufklärung einer **schweren Straftat unerlässlich** |
| **Abs. 3** | Eine blosse **Ordnungsvorschrift** | Verwertbar | — (keine Abwägung nötig) |
| **Abs. 4** | Ein Folgebeweis stammt aus einem nach Abs. 1/2 unverwertbaren Primärbeweis | Unverwertbar, ausser bei **hypothetisch rechtmässiger Erlangbarkeit** | Nachweis obliegt den Strafverfolgungsbehörden |
| **Abs. 5** | — (Vollzugsnorm) | Entfernung aus den Akten, Verschluss bis Rechtskraft, danach Vernichtung | — |

## Überblick und Bedeutung

Art. 141 StPO ist die zentrale Norm des strafprozessualen Beweisverwertungsrechts und zugleich eine der praxisrelevantesten Bestimmungen der StPO überhaupt: Kaum ein Verfahren mit Zwangsmassnahmen, verdeckter Ermittlung oder privater Beweiserhebung kommt ohne eine Auseinandersetzung mit dieser Norm aus. Sie ist Ausdruck des Grundsatzes, dass der Staat nicht durch Rechtsbrüche zu seinem Recht kommen darf («keine Frucht des vergifteten Baumes») — steht aber in einem Dauerspannungsfeld zum ebenso legitimen Interesse an der materiellen Wahrheitsfindung (Art. 139 StPO).

Der grösste praktische Stolperstein liegt nicht im Gesetzestext selbst, sondern in der **Abgrenzung zwischen den drei Stufen**: Ob eine verletzte Norm eine Gültigkeits- oder eine blosse Ordnungsvorschrift darstellt, entscheidet das Bundesgericht seit jeher nach dem **Schutzzweck der Norm** — mit einer Kasuistik, die für dieselbe Grundnorm (z.B. das Erfordernis eines staatsanwaltschaftlichen Befehls) je nach Zwangsmassnahme und Fallkonstellation zu gegensätzlichen Ergebnissen kommt (dazu unten Abschnitt D). Wer die Verwertbarkeit eines Beweises beurteilen will, sollte deshalb schematisch vorgehen:

### Prüfschema

| Schritt | Frage | Bei Bejahung |
|---|---|---|
| 1 | Wurde der Beweis unter Verletzung von Art. 140 StPO erhoben oder erklärt ihn das Gesetz ausdrücklich für unverwertbar? | **Absolut unverwertbar** (Abs. 1) — Prüfung endet hier |
| 2 | Wurde der Beweis von Strafbehörden **strafbar** erhoben oder wurde eine **Gültigkeitsvorschrift** verletzt? | Weiter zu Schritt 3 |
| 3 | Ist die Verwertung zur Aufklärung einer **schweren Straftat unerlässlich** (konkrete Tatschwere, nicht abstrakte Strafdrohung)? | Verwertbar (Abs. 2); sonst unverwertbar |
| 4 | Wurde nur eine **Ordnungsvorschrift** verletzt? | **Verwertbar** (Abs. 3) |
| 5 | Wurde ein **Folgebeweis** erst durch einen unverwertbaren Primärbeweis ermöglicht? | Nur verwertbar, wenn auch ohne den Primärbeweis erlangbar (Abs. 4, Fernwirkung) |

## A. Absolutes Beweisverwertungsverbot (Abs. 1)

### Der Zugangscode-Fall: Die PIN-Erfragung als verdeckte Einvernahme (BGE 151 IV 73)

Ein Bezirksgericht Zofingen verurteilte 2022 einen Mann wegen versuchter sexueller Nötigung, sexueller Handlungen mit Kindern und Pornografie zu zwölf Monaten bedingt; das Obergericht Aargau erhöhte im Berufungsverfahren 2023 auf drei Jahre teilbedingt. Grundlage für einen Teil der Schuldsprüche (Vorwürfe zulasten weiterer, im Verfahren als B., C., D. und E. bezeichneter Geschädigter) waren Daten, die von einem Mobiltelefon LG V20 stammten. Bei einer Hausdurchsuchung am 11. November 2018 hatte die Polizei den Beschuldigten nach dem Zugangscode zu seinem Telefon gefragt — ohne ihn vorher über sein Aussage- und Mitwirkungsverweigerungsrecht nach Art. 158 Abs. 1 lit. b StPO zu belehren. Über die so entschlüsselten Handydaten stiess die Polizei auf weitere mutmassliche Opfer auf Facebook und Lovoo.

**Erstinstanz contra Berufungsinstanz.** Das Bezirksgericht sprach den Beschuldigten von diesen Vorwürfen frei: Die PIN-Erfragung sei eine Einvernahme gewesen, die Belehrung habe gefehlt, die Handydaten und alle Folgebeweise seien daher unverwertbar. Das Obergericht Aargau hob dies auf — gestützt auf ein Bundesgerichtsurteil in einem Entsiegelungsverfahren (1B_535/2021), das im Konjunktiv festgehalten hatte, die Frage nach dem Zugangscode «dürfte» keine Einvernahme sein, weil sie der Erleichterung der Hausdurchsuchung nach Art. 245 Abs. 2 StPO diene.

**Das Bundesgericht korrigiert die Vorinstanz.** In [BGE 151 IV 73](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-151-IV-73_2025.html) hält die I. strafrechtliche Abteilung fest, dass die vom Obergericht zitierte Konjunktiv-Erwägung aus einem Entsiegelungsverfahren stammte, in dem Verwertungsverbote nur bei **offensichtlicher** Unverwertbarkeit zu prüfen sind, und dass sie in der Lehre «stark kritisiert» worden war (E. 2.5.1). Massgebend sei ein **materieller Einvernahmebegriff**: Entscheidend ist nicht die formelle Etikettierung, sondern ob die Äusserung von der Strafverfolgungsbehörde provoziert wurde. Nicht ersichtlich sei, inwiefern die Frage nach dem Zugangscode die Hausdurchsuchung erleichtern könnte — die Erhebung eines Entsperrcodes bei bereits bestehendem Tatverdacht ohne vorgängige Belehrung begründe vielmehr eine unzulässige Aushöhlung des nemo-tenetur-Grundsatzes. Die Unverwertbarkeit gelte absolut (Art. 141 Abs. 1 Satz 2 StPO).

**Fernwirkung.** Für die Folgebeweise (Auswertung von Facebook/Lovoo) prüfte das Gericht Art. 141 Abs. 4 StPO n.F.: Seit 1. Januar 2024 erfasst die Norm ausdrücklich auch absolute Verwertungsverbote nach Abs. 1 (zuvor nur Abs. 2 — eine in der Lehre umstrittene und in BGE 138 IV 169 E. 3.2 offengelassene Frage). Massgebend ist weiterhin die vor 2024 entwickelte Rechtsprechung: keine strikte Fernwirkung, sondern die Frage, ob der Folgebeweis auch ohne den Primärbeweis erlangt worden wäre. Ein solcher Nachweis «ist regelmässig nur schwer zu erbringen» (E. 2.5.2) — im konkreten Fall fehlte er, weshalb sämtliche Folgebeweise ebenfalls unverwertbar waren und der Beschwerdeführer in diesem Punkt obsiegte.

> **Merksatz.** Wer bei einer Hausdurchsuchung nach dem Gerätecode gefragt wird, befindet sich materiell in einer Einvernahmesituation — unabhängig davon, ob die Frage formell als «Erleichterung der Durchsuchung» getarnt wird. Fehlt die vorgängige Belehrung nach Art. 158 Abs. 1 lit. b StPO, ist nicht nur das Telefon selbst, sondern grundsätzlich auch jeder darauf gestützte Folgebeweis unverwertbar — die Strafverfolgungsbehörden tragen die (in der Praxis meist unerfüllbare) Beweislast für die hypothetisch rechtmässige Erlangbarkeit.

### Die Wahrsagerin als verdeckte Ermittlerin: Umgehung des Aussageverweigerungsrechts (BGE 148 IV 205)

Am frühen Morgen des 19. Oktober 2009 wurde B.A. vor der ehelichen Wohnung in Zürich erschossen. Ihr Ehemann A.A. bestritt während der jahrelangen Strafuntersuchung durchgehend, etwas mit der Tat zu tun zu haben. Weil die Ermittlungen ins Stocken gerieten, ordnete die Staatsanwaltschaft eine verdeckte Ermittlung an: «C.» baute über Monate ein Vertrauensverhältnis zum Beschuldigten auf; als dieser sich in Bedrängnis fühlte, schlug «C.» ihm — im Wissen, dass A.A. an übersinnliche Wesen glaubte und schon früher Wahrsager aufgesucht hatte — einen Besuch bei der Hellseherin «D.» vor. Auch «D.» war eine verdeckte Ermittlerin.

**Die Eskalation.** «D.» nutzte ihr Wissen über die Ermittlungen, um A.A. von ihren «magischen Kräften» zu überzeugen, beschwor einen bösen Geist des Opfers herauf, der «hartnäckiger» werde, und suggerierte eine konkrete Gefahr für ihn und seine Kinder. An einem Treffen am 5. September 2015 erklärte sie, sie spüre die Anwesenheit des Geistes im Raum und sehe «eine Pistole». A.A. antwortete zunächst ausweichend, er kenne die Todesursache nur aus der Presse und halte eine andere Person für die Täterin. Danach entdeckte er an seinem Auto einen zuvor von den Ermittlern angebrachten «Blutsegen» (ein roter, handförmiger Farbklecks) — für ihn das von der Wahrsagerin angekündigte Zeichen des Geistes. Auf der Heimfahrt zerstreute «C.» geschickt die aufkommenden Zweifel und riet ihm, sich «zu befreien». Am folgenden Tag legte A.A. gegenüber «C.» ein umfassendes Geständnis ab — eingeleitet mit dem Satz, er wolle nun endlich Ruhe haben und Schutz für sich und seine Kinder.

**Die rechtliche Weichenstellung.** Das Obergericht Zürich sprach A.A. 2020 frei und erklärte das Geständnis für unverwertbar; das Bundesgericht bestätigte dies in [BGE 148 IV 205](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-148-IV-205_2022.html). Kernfrage war das Verhältnis zwischen Art. 293 Abs. 4 StPO (Strafmilderung bei übermässiger Einwirkung eines verdeckten Ermittlers auf den **Tatentschluss**) und Art. 141 Abs. 1 StPO (absolute Unverwertbarkeit bei Verletzung von Art. 140 StPO). Das Gericht zieht eine scharfe Grenze: **Täuschung** ist der verdeckten Ermittlung inhärent und wird toleniert (E. 2.5.1) — wird aber eine **vernehmungsähnliche Situation** geschaffen, in der der verdeckte Ermittler unter Ausnützung des Vertrauensverhältnisses gezielt Fragen stellt, die einer förmlichen Einvernahme vorbehalten wären, und den Beschuldigten zur Aussage drängt, liegt eine unzulässige **Umgehung der Selbstbelastungsfreiheit** vor (E. 2.5.2). Nicht geschützt ist der Beschuldigte hingegen davor, dass ein verdeckter Ermittler blosse **Spontanäusserungen** zur Kenntnis nimmt, die dieser aus eigenem Antrieb macht.

Das Bundesgericht verwarf ausdrücklich die von der Beschwerdeführerin (Oberstaatsanwaltschaft Zürich) vertretene «Strafzumessungslösung»: Der deutsche Bundesgerichtshof hatte eine analoge Lösung nach EGMR-Rechtsprechung (*Akbay und andere gegen Deutschland*; *Furcht gegen Deutschland*) aufgegeben, weil eine blosse Strafmilderung eine Verletzung des fair-trial-Gebots nicht kompensiere — «for the trial to be fair … all evidence obtained as a result of police incitement must be excluded». Das Bundesgericht liess offen, ob Art. 293 Abs. 4 StPO generell konventionskonform ist, hielt aber fest, dass er jedenfalls nicht auf das gezielte Aushorchen eines bereits Beschuldigten über eine vergangene Tat zugeschnitten ist (E. 2.8.4 f.).

> **Merksatz.** Die Grenze zwischen zulässiger List und unzulässiger Umgehung der Aussageverweigerung verläuft nicht bei der Täuschung als solcher, sondern bei der **Funktion** der Interaktion: Sobald der verdeckte Ermittler faktisch Vernehmungsfragen zu einer bereits begangenen Tat stellt und gezielt Druck aufbaut, tritt Art. 293 Abs. 4 StPO (Strafmilderung) zurück und es greift das absolute Verwertungsverbot nach Art. 141 Abs. 1 StPO — unabhängig davon, ob sich der Beschuldigte zuvor ausdrücklich auf sein Schweigerecht berufen hat.

## B. Relatives Beweisverwertungsverbot (Abs. 2): Die Schwere-Straftat-Kasuistik

### Zwei private Filmaufnahmen, zwei Ergebnisse

Die Frage, wann eine Straftat «schwer» genug ist, um die Verwertung eines rechtswidrig erhobenen Beweises zu rechtfertigen, lässt sich am besten anhand zweier Bundesgerichtsurteile im Abstand von zwei Monaten illustrieren — beide betreffen private Videoaufnahmen, beide betreffen (rechtlich betrachtet) blosse **Vergehen**, und dennoch fallen sie gegensätzlich aus.

**Fall 1 — Landfriedensbruch verwertbar.** Am 25. April 2015 versammelten sich rund 300 Personen zu einer unbewilligten Kundgebung auf dem Bundesplatz in Bern. Während des Umzugs kam es zu Sachbeschädigungen an einer Bankfiliale, einem Hotel, einem Coiffeursalon und der Lorrainebrücke; vermummte Sprayer wurden von der Menge wiederholt vor der Polizei versteckt. A. nahm am Umzug teil und verteilte Flugblätter, ohne selbst Gewalt auszuüben. Er wurde wegen Landfriedensbruchs zu 60 Tagessätzen bedingt verurteilt — auf der Grundlage von Videoaufnahmen der Sicherheitskamera eines Hotels, die ohne gesetzliche Grundlage angefertigt worden waren. In [BGE 147 IV 9](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-147-IV-9_2021.html) bestätigte das Bundesgericht die Verwertung: Massgebend für den Begriff der «schweren Straftat» nach Art. 141 Abs. 2 StPO sei nicht das abstrakt angedrohte Strafmass, sondern die **Schwere der konkreten Tat** (E. 1.4.2). Landfriedensbruch als kollektive Gewalttätigkeit verletze gewichtige Rechtsgüter (die öffentliche Friedensordnung), und der Tatbestand trage überdies der typischen Beweisnot bei Massendelikten Rechnung — wer sich in der Anonymität der Zusammenrottung verstecke, solle sich nicht zusätzlich auf ein Verwertungsverbot berufen können (E. 1.4.3). Massgebend seien dabei die Gesamtumstände der Kundgebung, nicht der individuelle, hier bescheidene Tatbeitrag des Beschwerdeführers (E. 1.4.4).

**Fall 2 — Verkehrsregelverletzung nicht verwertbar.** Am 18. Mai 2018 überholte ein Autofahrer in Lausanne einen Elektrocyclomotoristen in einer langen Linkskurve, hupte grundlos, fuhr mit rund zehn Metern Abstand an ihm vorbei, scherte dann abrupt vor ihm ein und bremste — der Cyclomotorist musste ebenfalls scharf bremsen und schlug mit der Hand gegen das Fahrzeugheck, um auf sich aufmerksam zu machen; im Moment des Vorfalls betrug der Abstand zwischen Trottoirkante und Fahrzeug weniger als 70 cm. Der Cyclomotorist hatte die Szene mit einer am Lenker montierten GoPro-Kamera gefilmt und das Video zu den Akten gegeben. Das kantonale Gericht verurteilte den Autofahrer wegen einfacher und grober Verkehrsregelverletzung (Art. 90 Abs. 1 und 2 SVG) auf der Basis dieses Videos. In [BGE 147 IV 16](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-147-IV-16_2021.html) hob das Bundesgericht dies auf: Die GoPro-Aufnahme sei — wie eine Dashcam — kontinuierlich, nicht erkennbar und ohne Diskriminierung erfolgt, was eine Persönlichkeitsverletzung nach Art. 4 Abs. 4, Art. 12 Abs. 2 lit. a DSG darstelle (E. 7.1). Ein Rechtfertigungsgrund nach Art. 13 DSG scheide aus, weil die Verkehrsüberwachung eine staatliche Aufgabe sei und der «Apprenti-Shérif»-Gedanke keinen privaten Rechtfertigungsgrund begründe (E. 3, 5). Und selbst wenn man diese Hürde nähme: Verkehrsregelverletzungen nach Art. 90 Abs. 1 und 2 SVG seien — anders als der Landfriedensbruch im Parallelfall — abstrakt keine schweren Straftaten, und auch die konkreten Umstände (kein Unfall, keine Verletzung) erreichten die erforderliche Schwelle nicht (E. 7.2).

**Die Tabelle im Vergleich:**

| Kriterium | [BGE 147 IV 9](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-147-IV-9_2021.html) — Landfriedensbruch (**verwertbar**) | [BGE 147 IV 16](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-147-IV-16_2021.html) — Verkehrsregelverletzung (**nicht verwertbar**) |
|---|---|---|
| Abstrakte Einordnung | Vergehen (Art. 260 Abs. 1 StGB) | Vergehen/Übertretung (Art. 90 Abs. 1 und 2 SVG) |
| Konkreter Vorfall | Teilnahme an gewalttätiger Kundgebung, keine eigene Gewalt des Beschwerdeführers | Gefährliches Überholmanöver, Cyclomotorist auf < 70 cm an Trottoirkante gedrängt, kein Unfall |
| Geschütztes Rechtsgut | Öffentliche Friedensordnung (kollektiv) | Verkehrssicherheit (Individualgefährdung) |
| Institutionelles Argument | Beweisnot bei Massendelikten spricht für Verwertung | «Apprenti-Shérif»-Verbot spricht gegen private Verkehrsüberwachung |
| Ergebnis der Interessenabwägung | Öffentliches Interesse überwiegt — **verwertbar** | Privates Interesse überwiegt — **unverwertbar** |

Der Vergleich zeigt eine **Spannung, die das Bundesgericht selbst nicht auflöst**: Der Cyclomotorist wurde real und unmittelbar gefährdet (Sturzgefahr, weniger als eine Armlänge Abstand zur Bordsteinkante), während dem Landfriedensbruch-Teilnehmer kein eigener Gewaltakt vorgeworfen wurde. Dennoch wiegt die kollektive Falschheit des einen Delikts abstrakt schwerer als die individuelle Gefährdung des anderen — eine Wertung, die sich aus dem institutionellen Zweck von Art. 260 StGB (Bekämpfung der Beweisnot bei Massendelikten) erklärt, nicht aus der tatsächlichen Gefährdungsintensität. Für die Praxis bedeutet dies: Die «Schwere der konkreten Tat» ist kein rein empirisches, sondern ein normativ mitbestimmtes Kriterium, bei dem der Deliktstyp (Kollektivdelikt vs. Individualdelikt) mindestens so stark wirkt wie die tatsächliche Gefährdung im Einzelfall.

> **Merksatz.** Wer sich auf die Unverwertbarkeit privat erhobener Beweise beruft, sollte nicht allein mit der abstrakten Strafdrohung argumentieren — das Bundesgericht fragt nach der konkreten Tatschwere. Bei Kollektivdelikten (Landfriedensbruch, Raufhandel) ist die Hürde wegen des institutionellen Beweisnot-Arguments tendenziell tiefer als bei Individualdelikten mit vergleichbarer oder höherer abstrakter Strafdrohung.

### Private Beweiserhebung: zweistufige Prüfung

Werden Beweise nicht vom Staat, sondern von Privaten rechtswidrig erhoben, prüft das Bundesgericht seit [BGE 146 IV 226](https://mcp.opencaselaw.ch/entscheid/bge_BGE_146_IV_226) zweistufig: Erst ist zu fragen, ob ein Rechtfertigungsgrund nach Art. 13 DSG (Einwilligung, überwiegendes privates oder öffentliches Interesse, gesetzliche Grundlage) die datenschutzrechtliche Widerrechtlichkeit beseitigt — bejahendenfalls ist der Beweis **uneingeschränkt verwertbar**. Erst wenn die Rechtswidrigkeit bestehen bleibt, folgt die strafprozessuale Prüfung nach Art. 141 Abs. 2 StPO (BGE 147 IV 16 E. 5). Rechtfertigungsgründe werden bei Dashcam-artigen Dauer- und Streuaufnahmen «nur mit grosser Zurückhaltung» anerkannt (BGE 147 IV 16 E. 3.3), während sie bei punktuellen, situativ ausgelösten Aufnahmen (z.B. Bodycam-Video eines konkreten Vorfalls) eher in Betracht kommen (BGer 6B_810/2020 E. 2.6).

## C. Ordnungsvorschrift oder Gültigkeitsvorschrift? Der Schutzzweck-Test in der Praxis

### Zwei Grenzfälle, gegensätzlich entschieden — und ein Gericht, das die eigene Vorentscheidung einhegt

Ob eine verletzte Verfahrensvorschrift eine Gültigkeits- oder eine blosse Ordnungsvorschrift darstellt, entscheidet sich «primär nach dem Schutzzweck der Norm»: Hat die Vorschrift für die zu schützenden Interessen eine derart erhebliche Bedeutung, dass sie ihr Ziel nur bei Ungültigkeit der Verfahrenshandlung erreichen kann, liegt eine Gültigkeitsvorschrift vor. Dieser abstrakt einleuchtende Massstab führt in der Anwendung zu einer Kasuistik, die selbst das Bundesgericht zur ausdrücklichen Distanzierung von einer eigenen früheren Erwägung zwingt.

**Der iPhone-Fall (Ordnungsvorschrift, verwertbar).** Am 28. Januar 2011 wurde eine stark alkoholisierte brasilianische Staatsangehörige um 7:15 Uhr in einer «Kontaktbar» im Zürcher Rotlichtmilieu polizeilich angehalten. Da sie sich weder ausweisen konnte noch wollte, wurde sie auf den Polizeiposten geführt. Dort durchsuchten die Beamten ihr iPhone — ohne den nach Art. 241 Abs. 1 StPO an sich erforderlichen staatsanwaltschaftlichen Durchsuchungsbefehl — und fanden «offensichtliche Freier-Adressen», die auf unbewilligte Prostitution hindeuteten. In [BGE 139 IV 128](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-139-IV-128_2013.html) qualifizierte das Bundesgericht das Fehlen des Durchsuchungsbefehls als **blosse Ordnungsvorschrift** (E. 1.7) — allerdings ausdrücklich nur «unter Berücksichtigung der konkreten Umstände»: Die Beamten hätten sich auf die Einsicht in die gespeicherten Adressen beschränkt, es gebe keine Anhaltspunkte für ein vorsätzliches, rechtsmissbräuchliches Umgehen der Zuständigkeitsordnung, und die Zuständigkeiten seien angesichts der Möglichkeit dringlichen Handelns nach Art. 241 Abs. 3 StPO «in einer gewissen Hinsicht fliessend».

**Der Cannabis-Fall (Gültigkeitsvorschrift, unverwertbar).** Am 6. Dezember 2019 wurde ein Autofahrer beim Grenzübergang Au (SG) kontrolliert; im Kofferraum fanden Grenzwachtbeamte 175 Hanfsetzlinge. Die Staatsanwaltschaft ordnete telefonisch eine Analyse der Pflanzen durch den Forensisch-Naturwissenschaftlichen Dienst an — eine faktische Beschlagnahme —, bestätigte diese mündliche Anordnung aber entgegen Art. 263 Abs. 2 Satz 2 StPO nie schriftlich. Das Kantonsgericht St. Gallen erachtete dies als blosse Ordnungsvorschriftverletzung: Der Beschuldigte hätte ja selbst eine schriftliche Bestätigung verlangen können. In [BGE 151 IV 18](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-151-IV-18_2025.html) widersprach das Bundesgericht: Die Pflicht zur schriftlichen Bestätigung diene der Dokumentationspflicht und dem rechtlichen Gehör (Art. 29 Abs. 2 BV) sowie dem Beginn der zehntägigen Beschwerdefrist nach Art. 396 Abs. 1 StPO — sie sei **Gültigkeitsvorschrift** (E. 4.4.11), unabhängig davon, ob der Beschuldigte eine Bestätigung verlangt hatte.

**Die ausdrückliche Distanzierung.** Bemerkenswert ist, wie das Gericht in BGE 151 IV 18 mit dem eigenen iPhone-Präjudiz umgeht: Es hält fest, die Qualifikation in BGE 139 IV 128 sei «ausdrücklich ‹unter Berücksichtigung der konkreten Umstände› des Einzelfalls» erfolgt, weshalb «eine Übertragung auf den vorliegenden Fall ausgeschlossen» sei (E. 4.4.6). Das ist keine stille Harmonisierung über angeblich unterschiedliche Sachverhaltsnuancen, sondern eine offene Feststellung, dass dieselbe Grundnorm — das Erfordernis eines staatsanwaltschaftlichen Zwangsmassnahmenbefehls — im einen Fall als entbehrlich, im anderen als unverzichtbar behandelt wird, **ohne dass sich daraus eine generalisierbare Regel ableiten liesse**. Ergänzend zieht das Gericht das Urteil 6B_307/2017 zur Blutprobenanordnung heran, wo die Schriftlichkeit nach Art. 241 Abs. 1 StPO ausdrücklich als Gültigkeitsvoraussetzung bezeichnet wurde (E. 4.3.6) — ein drittes Beispiel derselben Grundnorm mit wiederum eigenständigem Ergebnis. Auch bei der örtlichen Zuständigkeit einer Blutprobenanordnung (BGE 142 IV 23) qualifizierte das Bundesgericht die verletzte Norm als Ordnungsvorschrift.

**Die Kasuistik-Tabelle:**

| Verletzte Norm | Konkreter Sachverhalt | Qualifikation | Entscheid |
|---|---|---|---|
| Art. 241 Abs. 1 StPO (STA-Durchsuchungsbefehl) | iPhone-Durchsuchung bei polizeilicher Anhaltung, keine Vorsatz-Umgehung erkennbar | **Ordnungsvorschrift** (im konkreten Fall) | [BGE 139 IV 128](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-139-IV-128_2013.html) |
| Art. 263 Abs. 2 Satz 2 StPO (schriftl. Bestätigung mündl. Beschlagnahme) | Cannabis-Setzlinge, Bestätigung fehlte gänzlich | **Gültigkeitsvorschrift** | [BGE 151 IV 18](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-151-IV-18_2025.html) |
| Art. 241 Abs. 1 StPO (schriftl. Anordnung Blutprobe) | Keine schriftliche Anordnung/Bestätigung in den Akten | **Gültigkeitsvorschrift** | BGer 6B_307/2017 E. 1.2.2 |
| Örtliche Zuständigkeit bei Blutprobenentnahme | Kantonspolizei örtlich unzuständig | **Ordnungsvorschrift** | BGE 142 IV 23 |

> **Annotation.** Für die Verteidigung bedeutet diese Kasuistik: Ein Verweis auf «das ist doch dieselbe Norm wie in BGE X» genügt nicht — das Bundesgericht hat sich diese Verallgemeinerung in BGE 151 IV 18 ausdrücklich verbeten. Massgebend ist stets eine konkrete Schutzzweck-Argumentation zur jeweiligen Fallkonstellation: Wessen Interesse schützt die verletzte Formvorschrift (Verteidigungsrechte? Rechtsmittelfrist? Dokumentationspflicht?), und wird dieses Interesse durch den konkreten Verstoss real beeinträchtigt oder bleibt es abstrakt? Wer sich auf eine frühere «Ordnungsvorschrift»-Qualifikation beruft, muss darlegen, dass die konkreten Umstände jenen des Präjudizes tatsächlich entsprechen — nicht bloss die verletzte Gesetzesbestimmung.

> **Merksatz.** Bei Zwangsmassnahmen mit **Rechtsmittelfrist-Relevanz** (insb. Beschlagnahme, deren Anfechtungsfrist erst mit schriftlicher Zustellung zu laufen beginnt) tendiert das Bundesgericht zur Gültigkeitsvorschrift; bei Massnahmen ohne unmittelbare Auswirkung auf die Verteidigungsrechte und ohne Anhaltspunkte für ein bewusstes Umgehen der Zuständigkeitsordnung eher zur Ordnungsvorschrift. Eine sichere Prognose erlaubt beides nicht.

## D. Fernwirkung (Abs. 4)

Abs. 4 wurde durch Ziff. I des BG vom 17. Juni 2022 (in Kraft seit 1.1.2024) neu gefasst und erfasst seither ausdrücklich **sowohl** Abs. 1 **als auch** Abs. 2 (zuvor nur Abs. 2). Die Frage, ob bei absoluten Verwertungsverboten eine strikte Fernwirkung gelten sollte, war zuvor umstritten und in BGE 138 IV 169 E. 3.2 offengelassen worden. In BGer 7B_257/2022 vom 4. Dezember 2023 und bestätigend in [BGE 151 IV 73](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-151-IV-73_2025.html) E. 2.5.2 entschied das Bundesgericht, dass die bisherige — nicht nach der Art des Verwertungsverbots differenzierende — Rechtsprechung auch unter neuem Recht weitergilt: **Keine strikte Fernwirkung**, sondern die (regelmässig schwer zu erbringende) Frage, ob der Folgebeweis auch ohne den unverwertbaren Primärbeweis mit grosser Wahrscheinlichkeit erlangt worden wäre (BGE 138 IV 169 E. 3.3.3; BGE 133 IV 329 E. 4.5). Die blosse theoretische Möglichkeit rechtmässiger Erlangung genügt nicht.

**Anwendungsbeispiele aus der jüngeren Praxis:**
- Aussagen in der Hauptverhandlung, die auf Vorhalt einer unverwertbaren polizeilichen Einvernahme beruhen, sind unverwertbar, wenn sie ohne diesen Vorhalt nicht in dieser Form ergangen wären (BGer 6B_865/2025).
- Bei der PIN-Erfragung (BGE 151 IV 73) mussten die Strafverfolgungsbehörden aufzeigen, dass das Mobiltelefon auch ohne den Code hätte ausgelesen werden können — der Nachweis scheiterte im konkreten Fall vollständig.
- Beim Zufallsfund über ein BÜPF-Verfahren (BGE 133 IV 329) war ein Geständnis verwertbar, weil es mit an Sicherheit grenzender Wahrscheinlichkeit auch ohne den illegalen Zufallsfund erlangt worden wäre.

> **Merksatz.** In der Praxis ist die Fernwirkungsfrage regelmässig **entscheidend** für den Verfahrensausgang, weil die Strafverfolgungsbehörden einen hypothetischen Kausalverlauf nachträglich kaum je lückenlos rekonstruieren können. Die Verteidigung sollte deshalb nicht nur den Primärverstoss, sondern konsequent jeden darauf gestützten Folgebeweis einzeln adressieren und dessen selbstständige, hypothetisch rechtmässige Erlangbarkeit aktiv bestreiten.

## E. Aktenbereinigung (Abs. 5) und die SkyECC-Prozessfalle

### Der irreparable Nachteil als Wächter des Rechtswegs

Nach ständiger Rechtsprechung stellt der blosse Verbleib eines angeblich unverwertbaren Beweismittels in den Akten grundsätzlich **keinen** nicht wieder gutzumachenden Nachteil dar — die Frage kann bis zum Sachurteil offenbleiben (BGE 141 IV 289 E. 1.2 f.). Anders liegt es, wenn eine kantonale Beschwerdeinstanz **während des Vorverfahrens** entgegen der Ansicht der Staatsanwaltschaft ein Beweismittel für unverwertbar erklärt und dessen Entfernung anordnet — dann droht der Staatsanwaltschaft ein irreparabler Nachteil, wenn dadurch die Weiterführung des Verfahrens verunmöglicht oder stark erschwert wird (BGE 141 IV 289 E. 1.4).

**Der SkyECC-Fall.** Ein Zürcher Betäubungsmittelverfahren stützte sich massgeblich auf entschlüsselte Kommunikationsdaten der Plattform SkyECC, die eine europäische Ermittlungsgruppe (Frankreich, Belgien, Niederlande, Eurojust, Europol) über Server in Roubaix abgefangen hatte. Das Bezirksgericht Dielsdorf verurteilte den Beschuldigten 2024 zu zehn Jahren und neun Monaten Freiheitsstrafe. In der Berufung beantragte die Verteidigung, das Verfahren zu zweiteilen: In einem ersten Teil solle **ausschliesslich** über die Verwertbarkeit der SkyECC-Daten verhandelt werden. Das Obergericht Zürich gab diesem Antrag statt und erklärte die Daten — hauptsächlich wegen Verletzung des Territorialitätsprinzips — für unverwertbar und aus den Akten zu entfernen. Die Oberstaatsanwaltschaft focht diesen Zwischenentscheid beim Bundesgericht an.

**Die prozessuale Volte.** In [BGer 7B_1429/2025](https://entscheidsuche.ch/docs/CH_BGer/CH_BGer_007_7B-1429-2025_2026-08-05.html) prüfte das Bundesgericht die materielle Verwertbarkeitsfrage gar nicht erst. Es hielt zunächst fest, dass der Verfahrensstand gegen einen irreparablen Nachteil der Staatsanwaltschaft spreche: Anders als in BGE 141 IV 289 war das Vorverfahren hier bereits abgeschlossen und Anklage erhoben, das erstinstanzliche Gericht hatte die Beweise sogar als verwertbar erachtet — das Verfahren stand also kurz vor dem Endurteil, sodass die Staatsanwaltschaft den Zwischenentscheid ohne Weiteres zusammen mit dem Endurteil hätte anfechten können (Art. 93 Abs. 3 BGG; E. 1.8).

Entscheidender aber: Das Gericht erklärte die vom Obergericht vorgenommene **Zweiteilung selbst als unzulässig**. Art. 342 Abs. 1 StPO kennt abschliessend nur zwei Formen der Zweiteilung — das **Schuldinterlokut** (Tat- und Schuldfrage vs. Folgen) und das **Tatinterlokut** (Tatfrage vs. Schuldfrage und Folgen). Eine Zweiteilung, die einzig die Verwertbarkeit eines Beweismittels isoliert vorab klärt, ist darin nicht vorgesehen und widerspricht dem Grundsatz der Einheit der Hauptverhandlung (Art. 340 Abs. 1 lit. a StPO) sowie dem Grundsatz der Formstrenge (Art. 2 Abs. 2 StPO; E. 2–2.4). Der so zustande gekommene Zwischenentscheid war deshalb schon aus diesem Grund nicht selbstständig anfechtbar — auf die Beschwerde der Oberstaatsanwaltschaft wurde nicht eingetreten.

> **Merksatz.** Wer eine Verwertbarkeitsfrage vorab und isoliert vom Sachgericht klären lassen will, braucht ein nach Art. 342 StPO zulässiges Schuld- oder Tatinterlokut — eine reine «Verwertbarkeits-Zweiteilung» der Hauptverhandlung ist prozessual unzulässig, selbst wenn beide Parteien sie beantragen und das Gericht sie gewährt. Der Entscheid über die Verwertbarkeit bleibt bis zum Endurteil hängig und ist erst mit diesem anfechtbar (Art. 342 Abs. 4, Art. 93 Abs. 3 BGG). Für die Verteidigung wie für die Staatsanwaltschaft gilt: Ein prozessual verlockender Vorab-Entscheid über ein zentrales Beweismittel kann sich als Zeitverlust erweisen, wenn er auf einer unzulässigen Verfahrensaufteilung beruht.

## Kantonale Praxisfragen

**Zuständigkeit für Beweisverwertungsverbote.** Kantonale Beschwerdeinstanzen betonen wiederholt, dass die Beurteilung von Beweisverwertungsverboten grundsätzlich dem **Sachgericht** vorbehalten ist und die Beschwerdeinstanz nicht vorgreifen darf (Kantonsgericht St. Gallen, Anklagekammer AK.2014.227; Kantonsgericht Basel-Landschaft, 470 19 121). Der SkyECC-Fall (BGer 7B_1429/2025) bestätigt diese Zurückhaltung indirekt: Auch eine gerichtlich bewilligte Zweiteilung der Hauptverhandlung darf diesen Grundsatz nicht unterlaufen.

**Reichweite der EMRK.** Das Kantonsgericht Solothurn hält fest, dass eine EMRK-Widrigkeit (Art. 8 EMRK) bei rechtswidrigen privaten Observationen nicht automatisch zu einem strafprozessualen Beweisverwertungsverbot nach Art. 141 StPO führt — der EGMR entwickle keine eigenständige, der StPO-Systematik entsprechende Doktrin (STBER.2021.55). Diese Trennung von Konventionsrecht und innerstaatlichem Beweisverwertungsrecht ist für die Praxis zentral: Eine EMRK-Verletzung ist notwendige, aber nicht hinreichende Bedingung für die Unverwertbarkeit nach Art. 141 StPO.

**Offene Streitfrage in der Lehre.** Die Qualifikation des Schriftlichkeitserfordernisses nach Art. 263 Abs. 2 StPO als Gültigkeits- oder Ordnungsvorschrift war vor BGE 151 IV 18 in Lehre und kantonaler Praxis gespalten: Während AEBI, BOMMER/GOLDSCHMID und GRAF eine Gültigkeitsvorschrift annahmen, vertraten HEIMGARTNER sowie mehrere Walliser und Zürcher Instanzen (Kantonsgericht Wallis P3 23 98; Obergericht Zürich UH160206) sowie das Bundesstrafgericht (SK.2022.6) die Gegenposition. Das Bundesgericht hat sich nun für die strengere Linie entschieden — für vor 2024/25 ergangene kantonale Entscheide, die der Gegenmeinung folgten, bedeutet dies eine überholte Rechtslage.

## Abgrenzungen

- **Art. 140 StPO** (verbotene Vernehmungsmethoden): Art. 141 Abs. 1 setzt eine Verletzung von Art. 140 voraus; die beiden Normen sind zusammen zu lesen.
- **Art. 6 Ziff. 1 EMRK** (fair trial): Der EGMR prüft die Fairness des Gesamtverfahrens und entwickelt keine eigenständige, der StPO-Systematik entsprechende Verwertungsverbots-Doktrin — die Trennlinien ziehen sich unterschiedlich (BGE 148 IV 205 E. 2.8.6, unter Verweis auf die deutsche Bundesgerichtshof-Praxis).
- **Art. 13 DSG**: Bei privater Beweiserhebung ist zunächst das Datenschutzrecht zu prüfen, bevor Art. 141 StPO überhaupt zur Anwendung kommt (BGE 147 IV 16 E. 5).
- **Art. 293 Abs. 4 StPO**: Regelt nur die Strafzumessungsfolgen übermässiger Einwirkung eines verdeckten Ermittlers auf den Tatentschluss — nicht das gezielte Aushorchen über eine bereits begangene Tat (BGE 148 IV 205 E. 2.8.4).
- **Art. 342 StPO**: Die abschliessend geregelte Zweiteilung der Hauptverhandlung (Schuld- oder Tatinterlokut) deckt keine isolierte Vorab-Klärung der Beweisverwertbarkeit ab (BGer 7B_1429/2025).
- **Art. 362 Abs. 4 StPO**: Gesetzlicher Fall der Unverwertbarkeit i.S.v. Art. 141 Abs. 1 Satz 2 (BGE 144 IV 189).

## Kasuistik im Überblick

**Absolute Unverwertbarkeit (Abs. 1)**: Erfragung des Zugangscodes bei Hausdurchsuchung ohne Belehrung ([BGE 151 IV 73](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-151-IV-73_2025.html)). Verdeckte Ermittlerin als Wahrsagerin zur Erpressung eines Geständnisses eingesetzt ([BGE 148 IV 205](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-148-IV-205_2022.html)). Polizeiliche Videoüberwachung ohne STA-Anordnung und ZMGER-Genehmigung (BGE 145 IV 42). Verletzung des Teilnahmerechts nach Art. 147 StPO (BGE 143 IV 457).

**Relative Unverwertbarkeit (Abs. 2)**: GoPro-Aufnahme bei nicht schwerer Verkehrsregelverletzung ([BGE 147 IV 16](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-147-IV-16_2021.html)). Private Observationen ohne gesetzliche Grundlage (BGE 143 IV 387). AFV-Aufzeichnungen bei nicht schwerer Anlasstat (BGE 146 I 11).

**Verwertbar trotz Rechtswidrigkeit (Abs. 2, schwere Straftat bejaht)**: Video eines Hotelbetriebs bei Landfriedensbruch ([BGE 147 IV 9](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-147-IV-9_2021.html)).

**Ordnungsvorschriften (Abs. 3)**: iPhone-Durchsuchung ohne Befehl bei polizeilicher Anhaltung, konkrete Umstände ([BGE 139 IV 128](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-139-IV-128_2013.html)). Örtlich unzuständige Kantonspolizei bei Blutprobe (BGE 142 IV 23).

**Gültigkeitsvorschriften (Abs. 2)**: Fehlende schriftliche Bestätigung einer mündlichen Beschlagnahme ([BGE 151 IV 18](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-151-IV-18_2025.html)). Fehlende schriftliche Anordnung/Bestätigung einer Blutprobe (BGer 6B_307/2017).

**Fernwirkung (Abs. 4)**: Fehlender Nachweis hypothetisch rechtmässiger Erlangbarkeit nach PIN-Erfragung ([BGE 151 IV 73](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-151-IV-73_2025.html) E. 2.5.2). Geständnis nach BÜPF-Zufallsfund trotz Fernwirkung verwertbar (BGE 133 IV 329).

**Aktenbereinigung und Prozessuales (Abs. 5)**: Verbleib in Akten grundsätzlich kein irreparabler Nachteil (BGE 141 IV 289); Ausnahme bei kantonaler Entfernungsanordnung im Vorverfahren. Unzulässige Verwertbarkeits-Zweiteilung der Hauptverhandlung ([BGer 7B_1429/2025](https://entscheidsuche.ch/docs/CH_BGer/CH_BGer_007_7B-1429-2025_2026-08-05.html)).

## Literatur

- OnlineKommentar.ch, Art. 141 StPO (Donat/Flückiger)
- Botschaft zur Änderung der Strafprozessordnung (Art. 141 Abs. 4 n.F.), BBl 2019 6697
- SCHMID, Niklaus, Schweizerische Strafprozessordnung, Handkommentar, Art. 141
- HEER, Marc, in: Trechsel/Roth, Kommentar zur Schweizerischen Strafprozessordnung, Art. 141
- RUCKSTUHL, Niklaus, in: Basler Kommentar, Schweizerische Strafprozessordnung, 3. Aufl. 2023, Art. 158
- GODENZI, Gunhild, in: Kommentar zur Schweizerischen Strafprozessordnung StPO, Donatsch et al. (Hrsg.), 3. Aufl. 2020, Art. 158
- HUWILER/STUDER, «Jetzt noch für das Protokoll» – Informelles Erheben von Handyzugangsdaten der beschuldigten Person, forumpoenale 1/2022, S. 53 ff.
- GAUDERON, Ryan, L'investigation secrète: mesure de contrainte licite ou moyen d'instruction déloyal?, AJP 2020, S. 1438 ff.
- HEIMGARTNER, Stefan, in: Kommentar zur Schweizerischen Strafprozessordnung StPO, 3. Aufl. 2020, Art. 263
- BOMMER/GOLDSCHMID, in: Basler Kommentar, Schweizerische Strafprozessordnung, 3. Aufl. 2023, Art. 263
