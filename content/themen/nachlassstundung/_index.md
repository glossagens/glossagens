---
title: "Ablauf der Nachlassstundung"
date: 2026-11-27
lastmod: 2026-11-27
description: "Ablauf der Nachlassstundung nach Art. 293–336 SchKG: Einleitung, provisorische und stille Stundung, definitive Stundung und Verlängerung, Wirkungen auf Gläubigerrechte und Dauerschuldverhältnisse, Unternehmensverkauf nach Art. 298 Abs. 2 SchKG, Inventar, Schuldenruf, Gläubigerversammlung, Ausstieg durch Sanierung, Nachlassvertrag oder Konkurs sowie Rechtsmittelweg und Kosten."
tags: ["SchKG", "Nachlassstundung", "Nachlassverfahren", "Sanierung", "Sachwalter", "Nachlassvertrag", "Gläubigerversammlung", "Konkurs", "Schuldenbereinigung"]
typ: verfahren
kurz: "Die Nachlassstundung verschafft einem zahlungsunfähigen oder überschuldeten Unternehmen eine gerichtliche Atempause: Während der Stundung dürfen Gläubiger grundsätzlich nicht betreiben, und laufende Zivilprozesse stehen still. Das Verfahren läuft zwingend in zwei Stufen ab — zuerst eine rasch bewilligte provisorische Stundung (höchstens vier, verlängerbar auf acht Monate) zur Prüfung der Sanierungschancen, dann die definitive Stundung (vier bis sechs, verlängerbar auf bis zu 24 Monate). Sie endet entweder mit der erfolgreichen Sanierung ohne Nachlassvertrag, mit der Bestätigung eines Nachlassvertrages oder — bei Scheitern — mit der Konkurseröffnung von Amtes wegen."
sachgebiete: [schkg.konkurs]
normen:
  - { gesetz: schkg, art: art-173a }
  - { gesetz: schkg, art: art-293 }
  - { gesetz: schkg, art: art-293a }
  - { gesetz: schkg, art: art-293b }
  - { gesetz: schkg, art: art-293c }
  - { gesetz: schkg, art: art-293d }
  - { gesetz: schkg, art: art-294 }
  - { gesetz: schkg, art: art-295 }
  - { gesetz: schkg, art: art-295a }
  - { gesetz: schkg, art: art-295b }
  - { gesetz: schkg, art: art-295c }
  - { gesetz: schkg, art: art-296 }
  - { gesetz: schkg, art: art-296a }
  - { gesetz: schkg, art: art-296b }
  - { gesetz: schkg, art: art-297 }
  - { gesetz: schkg, art: art-297a }
  - { gesetz: schkg, art: art-298 }
  - { gesetz: schkg, art: art-299 }
  - { gesetz: schkg, art: art-300 }
  - { gesetz: schkg, art: art-301 }
  - { gesetz: schkg, art: art-302 }
  - { gesetz: schkg, art: art-304 }
  - { gesetz: schkg, art: art-305 }
  - { gesetz: schkg, art: art-306 }
  - { gesetz: schkg, art: art-307 }
  - { gesetz: schkg, art: art-308 }
  - { gesetz: schkg, art: art-309 }
  - { gesetz: schkg, art: art-310 }
  - { gesetz: schkg, art: art-314 }
  - { gesetz: schkg, art: art-317 }
  - { gesetz: schkg, art: art-333 }
  - { gesetz: schkg, art: art-334 }
  - { gesetz: zpo, art: art-251 }
  - { gesetz: or, art: art-725b }
stichworte: ["Nachlassstundung", "provisorische Nachlassstundung", "definitive Nachlassstundung", "stille Nachlassstundung", "Sachwalter", "Gläubigerausschuss", "Nachlassvertrag", "Dividendenvergleich", "Nachlassvertrag mit Vermögensabtretung", "Sanierung", "Pre-pack", "Schuldenruf", "Gläubigerversammlung", "einvernehmliche private Schuldenbereinigung"]
revisions:
  - date: 2026-11-27
    by: "Antigravity Agent"
    model: "gemini-4-neon"
    note: "Erstfassung nach Skill glossagens-themen (Typ verfahren). Normtexte Art. 293a und Art. 294 SchKG per {{< wortlaut >}} (scripts/wortlaut.py, Fedlex-Konsolidierung Stand 1.1.2026); Elfter Titel SchKG, Art. 173a SchKG, Art. 54–55 GebV SchKG, Art. 251 ZPO, Art. 725b OR und Art. 74 BGG über Fedlex-MCP geprüft. 9 BGE und 2 BGer-Urteile im Volltext von entscheidsuche.ch geladen; Erwägungsnummern, Anker, Dispositive und wörtliche Zitate (nur aus deutschsprachigen Entscheiden; französischsprachige sinngemäss wiedergegeben) gegen den Volltext abgeglichen. Curia Vista zu Geschäft 25.019 geprüft (Stand 27.11.2026)."
---

## Überblick {#ueberblick}

Die **Nachlassstundung** (Art. 293–304 SchKG) ist das zentrale gerichtliche Sanierungs- und Restrukturierungsinstrument des schweizerischen Insolvenzrechts. Sie schützt den Schuldner vor Einzelzwangsvollstreckungen und Gerichtsprozessen, damit er unter Aufsicht eines Sachwalters entweder sein Unternehmen ohne Nachlassvertrag sanieren oder mit den Gläubigern einen **Nachlassvertrag** (Dividendenvergleich oder Liquidationsvergleich) abschliessen kann.

Mit der am 1. Januar 2014 in Kraft getretenen Revision des Sanierungsrechts (AS 2013 4111; BBl 2010 6455) hat der Gesetzgeber das Nachlassverfahren neu geordnet und den Zugang spürbar erleichtert. Seither gilt zwingend ein **zweistufiger Ablauf**: Jedes Nachlassverfahren beginnt mit einer rasch und niederschwellig bewilligten **provisorischen Stundung** (Art. 293a SchKG), die auch als reine Sanierungsstundung genutzt werden kann; erst in einem zweiten Schritt prüft das Nachlassgericht die Voraussetzungen für die **definitive Stundung** (Art. 294 SchKG). Zudem wurde mit der Aktienrechtsrevision per 1. Januar 2023 der frühere aktienrechtliche Konkursaufschub aufgehoben — überschuldete Gesellschaften nutzen seither ausschliesslich die Nachlassstundung (vgl. Art. 725b Abs. 3 OR i.V.m. Art. 173a SchKG). Für den allgemeinen Gesamtzusammenhang des Vollstreckungsrechts siehe das Thema [Schuldbetreibungs- und Konkursrecht im Überblick](/themen/schuldbetreibungs-und-konkursrecht/).

## Überblick über die Phasen {#phasen}

| Phase | Zuständige Behörde / Organ | Frist / Dauer | Rechtsmittel |
|---|---|---|---|
| **1. Einleitung** (Art. 293 SchKG) | Nachlassgericht (summarisches Verfahren, Art. 251 lit. a ZPO) | unverzügliche Prüfung | bei Abweisung mit Konkurs: Beschwerde nach ZPO (zehn Tage, Art. 321 Abs. 2 ZPO) |
| **2. Provisorische Stundung** (Art. 293a–293d SchKG) | Nachlassgericht; provisorischer Sachwalter | höchstens vier Monate, verlängerbar um höchstens vier Monate (total acht Monate) | Bewilligung und Sachwalterernennung nicht anfechtbar (Art. 293d SchKG) |
| **3. Definitive Stundung** (Art. 294–296 SchKG) | Nachlassgericht; Sachwalter; fakultativ Gläubigerausschuss | vier bis sechs Monate, verlängerbar auf zwölf, in besonders komplexen Fällen auf höchstens 24 Monate (Art. 295b SchKG) | Beschwerde nach ZPO durch Schuldner und Gläubiger; keine aufschiebende Wirkung gegen Bewilligung (Art. 295c SchKG) |
| **4. Stundungsverfahren** (Art. 299–304 SchKG) | Sachwalter (unter Aufsicht des Nachlassgerichts bzw. Gläubigerausschusses) | Schuldenruf: ein Monat (Art. 300 SchKG); Einberufung Gläubigerversammlung: mind. ein Monat vorher, Akteneinsicht 20 Tage (Art. 301 SchKG) | Aufsichtsbeschwerde nach Art. 17–19 SchKG (Art. 295 Abs. 4 SchKG); Neuschätzung Pfand innert zehn Tagen beim Nachlassgericht (Art. 299 Abs. 3 SchKG) |
| **5. Beendigung** (Art. 296a, 296b, 305–310 SchKG) | Nachlassgericht | vor Ablauf der Stundung (Art. 296a, 304 SchKG) | Beschwerde nach ZPO (Art. 296a Abs. 3, Art. 307 SchKG); gegen Bestätigungsentscheid mit aufschiebender Wirkung (Art. 307 Abs. 2 SchKG) |

## Phase 1: Einleitung des Nachlassverfahrens {#einleitung}

Das Nachlassverfahren wird nach Art. 293 SchKG auf drei Wegen beim örtlich zuständigen Nachlassgericht (am Betreibungsort gemäss Art. 46 SchKG) im summarischen Verfahren (Art. 251 lit. a ZPO) eingeleitet:

1. **Gesuch des Schuldners** (Art. 293 lit. a SchKG): Dies ist der Regelfall. Dem Gesuch sind eine aktuelle Bilanz, eine Erfolgsrechnung und eine Liquiditätsplanung (oder entsprechende Unterlagen zur derzeitigen und künftigen Vermögens-, Ertrags- oder Einkommenslage) sowie ein **provisorischer Sanierungsplan** beizulegen. Ein fertiger Entwurf eines Nachlassvertrags ist in diesem Stadium nicht erforderlich.
2. **Gesuch eines Gläubigers** (Art. 293 lit. b SchKG): Antragsberechtigt ist jeder Gläubiger, der berechtigt wäre, ein Konkursbegehren zu stellen (sei es nach vorgängiger Betreibung oder ohne solche nach [Art. 190 SchKG](/kommentar/schkg/art-190/)).
3. **Überweisung durch das Konkursgericht** (Art. 293 lit. c i.V.m. Art. 173a Abs. 2 SchKG): Bestehen in einem hängigen Konkursverfahren — etwa nach einer Überschuldungsanzeige des Verwaltungsrats gemäss Art. 725b Abs. 3 OR — Anhaltspunkte für eine unmittelbare Sanierung oder das Zustandekommen eines Nachlassvertrags, kann das Konkursgericht den Entscheid über den Konkurs von Amtes wegen aussetzen und die Akten dem Nachlassgericht überweisen. Hat der Schuldner oder ein Gläubiger bereits ein Stundungsgesuch eingereicht, kann das Konkursgericht den Konkursentscheid ebenfalls aussetzen (Art. 173a Abs. 1 SchKG).

## Phase 2: Provisorische Nachlassstundung {#provisorische-stundung}

Nach Eingang des Gesuchs prüft das Nachlassgericht zunächst zwingend die **provisorische Stundung**:

{{< wortlaut gesetz="schkg" art="art-293a" >}}

### Niederschwellige Bewilligung und Dauer {#provisorische-bewilligung}

Die provisorische Stundung dient als rasche Orientierungs- und Prüfphase. Nach der Rechtsprechung des Bundesgerichts gilt ein bewusst tiefer Massstab: «An die Bewilligung der provisorischen Stundung sind keine hohen Anforderungen zu stellen» ([BGE 147 III 226](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_005_BGE-147-III-226_2021.html#consideration_3.1.3) E. 3.1.3). «Nur in aussichtslosen bzw. hoffnungslosen Fällen soll das Nachlassgericht keine provisorische Stundung bewilligen, wobei zur Beurteilung ein Ermessen besteht» (a.a.O.).

Die Dauer beträgt zunächst höchstens **vier Monate** und kann auf Antrag des Sachwalters — oder, wenn kein solcher eingesetzt wurde, des Schuldners — in begründeten Fällen um höchstens **vier weitere Monate** auf insgesamt acht Monate verlängert werden (Art. 293a Abs. 2 SchKG). Zur näheren Prüfung der Sanierungs- oder Bestätigungsaussichten setzt das Nachlassgericht in der Regel einen oder mehrere **provisorische Sachwalter** ein; nur in begründeten Fällen kann es davon absehen (Art. 293b SchKG).

### Stille provisorische Stundung {#stille-stundung}

Grundsätzlich entfaltet die provisorische Stundung die gleichen Wirkungen wie die definitive (Art. 293c Abs. 1 SchKG) und wird öffentlich bekannt gemacht (Art. 296 SchKG). In begründeten Fällen kann das Nachlassgericht jedoch auf Antrag bis zur Beendigung der provisorischen Stundung auf die öffentliche Bekanntmachung verzichten, sofern der Schutz Dritter gewährleistet ist (Art. 293c Abs. 2 SchKG — sogenannte **stille Nachlassstundung**). Sie erlaubt es einem Unternehmen, Sanierungsverhandlungen oder einen Betriebsverkauf ohne unmittelbaren Reputationsverlust vorzubereiten. In diesem Fall gelten vier gesetzliche Besonderheiten:

- Die Mitteilung an Betreibungs-, Handelsregister- und Grundbuchamt unterbleibt (lit. a).
- Gegen den Schuldner können Betreibungen noch eingeleitet, nicht aber fortgesetzt werden (lit. b).
- Die Unwirksamkeit von Vorausabtretungen künftiger Forderungen ([Art. 297 Abs. 4 SchKG](/kommentar/schkg/art-297/)) tritt erst ein, wenn die provisorische Stundung dem Zessionar mitgeteilt wird (lit. c).
- Die Einsetzung eines provisorischen Sachwalters ist zwingend (lit. d).

### Verweigerung und vorzeitiger Widerruf {#provisorische-verweigerung}

Besteht **offensichtlich keine Aussicht** auf Sanierung oder Bestätigung eines Nachlassvertrags, eröffnet das Nachlassgericht von Amtes wegen den Konkurs (Art. 293a Abs. 3 SchKG). Diese Konkursfolge greift jedoch nicht ausnahmslos: «Wird die provisorische Nachlassstundung hingegen zu früh (unnötig bzw. ohne Sanierungsbedarf) oder gar rechtsmissbräuchlich beantragt, kann sich die amtswegige Konkurseröffnung nicht auslösen» ([BGer 5A_898/2024](https://entscheidsuche.ch/docs/CH_BGer/CH_BGer_005_5A-898-2024_2025-05-19.html) vom 19. Mai 2025 E. 1.2). Dasselbe gilt, wenn sich das Gesuch mangels eingereichter Unterlagen nicht beurteilen lässt; das Gericht weist das Gesuch dann ab, ohne den Konkurs zu eröffnen (a.a.O.).

Auch nach bereits bewilligter provisorischer Stundung kann ein vorzeitiger Abbruch mit Konkurseröffnung geboten sein: «Die Offensichtlichkeit der fehlenden Aussicht kann sich auch erst zu einem späteren Zeitpunkt nach der Bewilligung der provisorischen Nachlassstundung, aber vor deren Ablauf, ergeben.» ([BGer 5A_660/2025](https://entscheidsuche.ch/docs/CH_BGer/CH_BGer_005_5A-660-2025_2025-11-05.html) vom 5. November 2025 E. 2.1.4). Massgeblich bleibt dabei der strengere Massstab der Offensichtlichkeit (Art. 293a Abs. 3 bzw. Art. 296b lit. b SchKG) und nicht Art. 294 Abs. 3 SchKG, der erst bei Ablauf der provisorischen Stundung greift (a.a.O.).

## Phase 3: Definitive Nachlassstundung {#definitive-stundung}

Vor Ablauf der provisorischen Stundung entscheidet das Nachlassgericht von Amtes wegen über den Übergang in die **definitive Nachlassstundung**:

{{< wortlaut gesetz="schkg" art="art-294" >}}

### Verhandlung, Prognose und Publikation {#definitive-bewilligung}

Im Gegensatz zur provisorischen Phase genügt nun nicht mehr das blosse Fehlen offensichtlicher Aussichtslosigkeit: Erforderlich ist positiv eine **Aussicht auf Sanierung oder Bestätigung eines Nachlassvertrages**, d. h. ein Gelingen der Sanierung darf erwartet werden oder ein Nachlassvertrag hat realistische Chancen (BGE 147 III 226 E. 3.1.3). Vorgängig lädt das Nachlassgericht den Schuldner und einen allfälligen antragstellenden Gläubiger zu einer Verhandlung vor; der provisorische Sachwalter erstattet mündlich oder schriftlich Bericht, und weitere Gläubiger können angehört werden (Art. 294 Abs. 2 SchKG).

Die Bewilligung der definitiven Stundung wird stets **öffentlich bekannt gemacht** (eine stille definitive Stundung kennt das Gesetz nicht) und unverzüglich dem Betreibungs-, dem Handelsregister- und dem Grundbuchamt mitgeteilt; im Grundbuch ist die Nachlassstundung spätestens zwei Tage nach Bewilligung anzumerken (Art. 296 SchKG).

### Organe: Sachwalter und Gläubigerausschuss {#organe}

Mit der definitiven Stundung ernennt das Nachlassgericht einen oder mehrere **Sachwalter** (Art. 295 Abs. 1 SchKG). Der Sachwalter überwacht die Geschäftsführung des Schuldners, erstellt Inventar und Pfandschätzung, führt den Schuldenruf durch, entwirft bei Bedarf den Nachlassvertrag, leitet die Gläubigerversammlung und erstattet dem Gericht Zwischen- und Schlussberichte (Art. 295 Abs. 2 SchKG). Seine Geschäftsführung untersteht sinngemäss der Aufsichtsbeschwerde nach [Art. 17](/kommentar/schkg/art-017/)–19 SchKG (Art. 295 Abs. 4 SchKG).

Wo es die Umstände erfordern — typischerweise bei grösseren oder komplexen Unternehmenssanierungen —, setzt das Nachlassgericht zudem einen **Gläubigerausschuss** ein, in dem verschiedene Gläubigerkategorien angemessen vertreten sein müssen (Art. 295a Abs. 1 SchKG). Der Gläubigerausschuss beaufsichtigt den Sachwalter, kann ihm Empfehlungen erteilen und erteilt anstelle des Nachlassgerichts die Ermächtigung zu zustimmungsbedürftigen Geschäften nach Art. 298 Abs. 2 SchKG (Art. 295a Abs. 2 und 3 SchKG).

### Verlängerung der definitiven Stundung {#verlaengerung}

Die definitive Stundung wird zunächst für **vier bis sechs Monate** bewilligt (Art. 294 Abs. 1 SchKG). Sie kann nach Art. 295b Abs. 1 SchKG auf **zwölf Monate** und in besonders komplexen Fällen auf **höchstens 24 Monate** verlängert werden.

Bei der Antragsberechtigung unterscheidet das Bundesgericht scharf nach der Sechsmonatsgrenze ([BGE 150 III 137](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_005_BGE-150-III-137_2024.html#consideration_3.6.2) E. 3.6.2):

- **Bis sechs Monate**: Wurde zunächst eine kürzere Stundung (z. B. vier Monate) bewilligt, gilt Art. 294 SchKG: «Ist die Dauer der definitiven Stundung von sechs Monaten noch nicht ausgeschöpft, so können Antragssteller zur Verlängerung der Schuldner und gegebenenfalls der Gläubiger sein; der Sachwalter muss den Antrag nicht selber stellen» (BGE 150 III 137 E. 3.6.2).
- **Über sechs Monate hinaus**: Sobald die definitive Stundung über sechs Monate hinaus verlängert werden soll, greift Art. 295b Abs. 1 SchKG, und **ausschliesslich der Sachwalter** ist antragsberechtigt — nicht der Schuldner und nicht ein Gläubiger (BGE 150 III 137 E. 3.5.2 und 3.6.2). Im entschiedenen Fall beantragte eine Konzerngesellschaft selbst die Verlängerung über sechs Monate hinaus, nachdem die Sachwalter keinen Antrag gestellt hatten; das Bundesgericht bestätigte die daraufhin von Amtes wegen erfolgte Konkurseröffnung ([BGE 150 III 137](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_005_BGE-150-III-137_2024.html#consideration_4.) E. 4).

Soll die Stundung über **zwölf Monate** hinaus verlängert werden, muss der Sachwalter zudem eine **ausserordentliche Gläubigerversammlung** einberufen, die vor Ablauf des neunten Monats seit Bewilligung der definitiven Stundung stattzufinden hat; die Gläubiger können dort einen Gläubigerausschuss einsetzen oder abberufen sowie einen neuen Sachwalter bestimmen (Art. 295b Abs. 2 und 3 SchKG).

## Wirkungen während der Stundung {#wirkungen}

Die Wirkungen der Nachlassstundung treten bereits mit der Bewilligung der provisorischen Stundung ein (Art. 293c Abs. 1 SchKG, unter Vorbehalt der stillen Stundung nach Abs. 2).

### Wirkungen auf Gläubigerrechte {#wirkungen-glaeubiger}

[Art. 297 SchKG](/kommentar/schkg/art-297/) schirmt den Schuldner umfassend vor dem Zugriff der Gläubiger ab (Einzelheiten im Artikelkommentar):

- **Betreibungs- und Arrestverbot** (Abs. 1–3): Gegen den Schuldner kann grundsätzlich keine Betreibung eingeleitet oder fortgesetzt werden; ausgenommen ist die Betreibung auf Pfandverwertung für grundpfandgesicherte Forderungen, wobei die Verwertung des Grundpfandes gesperrt bleibt. Für Nachlassforderungen sind Arreste und andere Sicherungsmassnahmen ausgeschlossen.
- **Unwirksamkeit von Vorausabtretungen** (Abs. 4): Vor der Stundung vereinbarte Globalzessionen erfassen keine Forderungen, die erst nach der Stundungsbewilligung entstehen — die laufenden Debitorenzahlungen verbleiben dem Betrieb.
- **Ex-lege-Sistierung von Gerichtsverfahren** (Abs. 5): Zivilprozesse und Verwaltungsverfahren über Nachlassforderungen werden, ausser in dringlichen Fällen, sistiert. Wie das Bundesgericht klargestellt hat, liegt darin kein richterliches Ermessen: «Vielmehr tritt die Sistierung mit der Bewilligung der Nachlassstundung von Gesetzes wegen ein. Die entsprechende Verfügung des Gerichts ist bloss deklaratorischer Natur» ([BGE 151 III 516](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_005_BGE-151-III-516_2025.html#consideration_1.5.2) E. 1.5.2). Erfasst sind jedoch nur Verfahren über **Nachlassforderungen** (Geldforderungen). Ein mietrechtliches Ausweisungsverfahren nach aufgelöstem Geschäftsmietvertrag stützt sich auf den Realanspruch aus Art. 267 Abs. 1 OR und wird durch die Nachlassstundung nicht sistiert ([BGE 143 III 173](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_005_BGE-143-III-173_2017.html#consideration_6.) E. 6).
- **Fristen-, Zinsen- und Verrechnungsregeln** (Abs. 6–8): Verjährungs- und Verwirkungsfristen stehen still; für nicht pfandgesicherte Forderungen hört der Zinsenlauf auf, sofern der Nachlassvertrag nichts anderes bestimmt; für die Verrechnung gelten die Schranken von [Art. 213](/kommentar/schkg/art-213/) und [Art. 214 SchKG](/kommentar/schkg/art-214/) analog. Zudem verlängern sich die Fristen der paulianischen Anfechtung um die Dauer der Stundung ([Art. 288a SchKG](/kommentar/schkg/art-288a/)).

### Dauerschuldverhältnisse {#dauerschuldverhaeltnisse}

Nach Art. 297a SchKG kann der Schuldner mit Zustimmung des Sachwalters ein **Dauerschuldverhältnis** (z. B. einen langfristigen Miet- oder Leasingvertrag) jederzeit auf einen beliebigen Zeitpunkt kündigen, sofern andernfalls der Sanierungszweck vereitelt würde. Die Gegenpartei hat Anspruch auf Entschädigung, doch bildet diese blosse **Nachlassforderung** (die der Dividende unterliegt). Vorbehalten bleiben die besonderen Bestimmungen über die Auflösung von Arbeitsverträgen. Umgekehrt vermittelt Art. 297a SchKG dem Schuldner keinen Anspruch darauf, einen Dritten zur Fortführung eines bereits gekündigten Dauerschuldverhältnisses zu zwingen ([BGE 143 III 173](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_005_BGE-143-III-173_2017.html#consideration_7.) E. 7).

### Verfügungsbefugnis und Unternehmensverkauf (Pre-pack) {#verfuegungsbefugnis}

Anders als im Konkurs behält der Schuldner während der Nachlassstundung grundsätzlich die **Verfügungsbefugnis** und führt seine Geschäftstätigkeit unter Aufsicht des Sachwalters weiter (Art. 298 Abs. 1 SchKG). Das Nachlassgericht kann jedoch einzelne Handlungen der Mitwirkung des Sachwalters unterstellen oder diesem die Geschäftsführung übertragen.

Strenger geregelt sind ausserordentliche Dispositionen: Ohne **Ermächtigung des Nachlassgerichts oder des Gläubigerausschusses** können während der Stundung keine Teile des **Anlagevermögens** veräussert oder belastet, keine Pfänder bestellt, keine Bürgschaften eingegangen und keine unentgeltlichen Verfügungen getroffen werden (Art. 298 Abs. 2 SchKG; Rechte gutgläubiger Dritter bleiben nach Abs. 3 vorbehalten). «Ohne die Ermächtigung ist das Rechtsgeschäft zwar zivilrechtlich gültig, aber zwangsvollstreckungsrechtlich unbeachtlich» ([BGE 147 III 226](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_005_BGE-147-III-226_2021.html#consideration_4.3.1) E. 4.3.1).

In der Praxis ist Art. 298 Abs. 2 SchKG die Grundlage für übertragende Sanierungen — den Verkauf einzelner Betriebsteile oder des gesamten Unternehmens an eine Auffanggesellschaft, oft schon während der (allenfalls stillen) provisorischen Stundung (sogenannter *Pre-pack*). Das Bundesgericht hat dazu zwei wegweisende Schranken für Rechtsmittel gezogen:

- **Keine Beschwerde der Gläubiger**: «Ein Gläubiger ist zum Antrag auf Veräusserung von Anlagevermögen nach Art. 298 Abs. 2 SchKG nicht berechtigt, und das Verfahren richtet sich nicht gegen die Gläubiger» ([BGE 147 III 226](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_005_BGE-147-III-226_2021.html#consideration_4.3.4) E. 4.3.4). Gläubiger können gegen den Ermächtigungsentscheid keine ZPO-Beschwerde führen; beschwerdelegitimiert ist nur der Schuldner, wenn seinem Antrag nicht entsprochen wird (a.a.O. E. 4.3.3).
- **Keine Beschwerde der Gesellschafter**: Mit [BGE 152 III 398](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_005_BGE-152-III-398_2026.html#consideration_3.2.1) E. 3.2.1 und 3.2.2.8 übertrug das Bundesgericht diese Linie auf Anteilsinhaber: Auch der Minderheitsgesellschafter einer GmbH (im entschiedenen Fall mit 48 % Stammanteil) kann die gerichtliche Ermächtigung zur Betriebsveräusserung nicht mit Beschwerde anfechten. «Der Grund liegt darin, dass Gegenstand der gerichtlichen Genehmigung eine Rechtshandlung des Schuldners ist, währenddem die Gläubiger nur mittelbar tangiert sind, indem der Deckungsgrad ihrer Forderung beeinflusst werden kann.» (a.a.O. E. 3.2.1). Vorbehalten bleibt einzig die jederzeit von Amtes wegen zu beachtende **Nichtigkeit** bei besonders schweren, offensichtlichen Mängeln ([BGE 152 III 398](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_005_BGE-152-III-398_2026.html#consideration_3.3.1) E. 3.3.1).

Verstösst der Schuldner gegen Art. 298 SchKG oder Weisungen des Sachwalters, kann das Nachlassgericht ihm auf Anzeige des Sachwalters die Verfügungsbefugnis entziehen oder von Amtes wegen den Konkurs eröffnen (Art. 298 Abs. 4, Art. 296b lit. c SchKG).

## Phase 4: Durchführung des Stundungsverfahrens {#durchfuehrung}

Soll die Stundung in einen Nachlassvertrag münden, durchläuft der Sachwalter fünf geordnete Verfahrensschritte:

1. **Inventar und Pfandschätzung** (Art. 299 SchKG): Sofort nach seiner Ernennung nimmt der Sachwalter ein Inventar über sämtliche Vermögensbestandteile auf und schätzt sie. Die Verfügung über die Pfandschätzung legt er zur Einsicht auf und teilt sie Pfandgläubigern und Schuldner vor der Gläubigerversammlung schriftlich mit; jeder Beteiligte kann innert **zehn Tagen** beim Nachlassgericht gegen Kostenvorschuss eine Neuschätzung verlangen (Abs. 3).
2. **Schuldenruf** (Art. 300 SchKG): Der Sachwalter fordert die Gläubiger durch öffentliche Bekanntmachung (und uneingeschriebenen Brief an bekannte Gläubiger) auf, ihre Forderungen innert **eines Monats** einzugeben — mit der Androhung, dass sie bei Unterlassung an den Verhandlungen über den Nachlassvertrag nicht stimmberechtigt sind. Danach holt er die Erklärung des Schuldners über die eingegebenen Forderungen ein (Abs. 2).
3. **Einberufung der Gläubigerversammlung** (Art. 301 SchKG): Sobald der Entwurf des Nachlassvertrags steht, beruft der Sachwalter die Gläubigerversammlung durch öffentliche Bekanntmachung mindestens **einen Monat** im Voraus ein (sowie per Brief an bekannte Gläubiger), mit dem Hinweis auf die **20-tägige Akteneinsicht** vor der Versammlung.
4. **Gläubigerversammlung und Rechte gegen Mitverpflichtete** (Art. 302–303 SchKG): Der Sachwalter leitet die Versammlung und erstattet Bericht über die Vermögens-, Ertrags- oder Einkommenslage; der Schuldner hat beizuwohnen und Aufschluss zu geben. Der Entwurf des Nachlassvertrags wird den Gläubigern zur unterschriftlichen Genehmigung vorgelegt (Zustimmungen können noch bis zum Bestätigungsentscheid eingehen, Art. 305 Abs. 1 SchKG). Gläubiger, die nicht zustimmen, wahren ihre Rechte gegen Mitschuldner und Bürgen ohne Weiteres; wer zustimmt, muss diesen mindestens **zehn Tage** vor der Versammlung Ort und Zeit mitteilen und die Abtretung der Forderung gegen Zahlung anbieten (Art. 303 SchKG).
5. **Sachwalterbericht und Bestätigungsverhandlung** (Art. 304 SchKG): Vor Ablauf der Stundung unterbreitet der Sachwalter dem Nachlassgericht alle Akten samt Bericht über die eingegangenen Zustimmungen und seiner Empfehlung zur Bestätigung oder Ablehnung. Ort und Zeit der Bestätigungsverhandlung werden öffentlich bekannt gemacht, damit Gläubiger dort Einwendungen anbringen können.

## Phase 5: Ausstieg und Beendigung {#beendigung}

Eine Nachlassstundung endet auf genau einem von drei Wegen:

### 1. Erfolgreiche Sanierung ohne Nachlassvertrag {#aufhebung-sanierung}

Gelingt die Sanierung vor Ablauf der Stundung (etwa durch Kapitalerhöhung, Forderungsverzichte einzelner Hauptgläubiger oder Verkauf von Betriebsteilen), hebt das Nachlassgericht die Nachlassstundung nach einer Verhandlung und dem Bericht des Sachwalters **von Amtes wegen auf** (Art. 296a Abs. 1 und 2 SchKG). Die Aufhebung wird wie die Bewilligung öffentlich bekannt gemacht und den Ämtern mitgeteilt; die Wirkungen der Stundung enden *ex nunc* (BGE 147 III 226 E. 3.2.2).

### 2. Bestätigung eines Nachlassvertrages {#nachlassvertrag}

Der Nachlassvertrag ist nach Art. 305 Abs. 1 SchKG angenommen, wenn ihm bis zum Bestätigungsentscheid zustimmt:

- die **Mehrheit der Gläubiger**, die zugleich mindestens **zwei Drittel** des Gesamtbetrags der Forderungen vertreten; oder
- **ein Viertel der Gläubiger**, die mindestens **drei Viertel** des Gesamtbetrags der Forderungen vertreten.

Privilegierte Gläubiger (erste und zweite Klasse nach Art. 219 Abs. 4 SchKG) sowie Ehegatte bzw. eingetragene Partnerin oder Partner zählen weder nach Köpfen noch nach Forderungsbetrag mit; pfandgesicherte Forderungen zählen nur für den ungedeckten Teil (Art. 305 Abs. 2 SchKG). Über die Mitzählung bestrittener oder bedingter Forderungen für das Quorum entscheidet das Nachlassgericht, ohne dem materiellen Prozess vorzugreifen (Art. 305 Abs. 3 SchKG; [BGE 142 III 705](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_005_BGE-142-III-705_2016.html#consideration_3.1) E. 3.1).

Das Nachlassgericht bestätigt den angenommenen Vertrag nach Art. 306 Abs. 1 SchKG nur, wenn drei kumulative Voraussetzungen erfüllt sind:

1. Die angebotenen Leistungen stehen im richtigen Verhältnis zu den Möglichkeiten des Schuldners (Ziff. 1).
2. Die vollständige Befriedigung der angemeldeten privilegierten Gläubiger sowie die Erfüllung der während der Stundung **mit Zustimmung des Sachwalters** eingegangenen Verbindlichkeiten (Masseverbindlichkeiten) sind hinlänglich sichergestellt, sofern nicht ausdrücklich verzichtet wurde (Ziff. 2).
3. Beim **ordentlichen Nachlassvertrag** leisten die **Anteilsinhaber** einen angemessenen Sanierungsbeitrag (Ziff. 3).

Mit der Vollstreckbarkeit des Bestätigungsentscheids fallen die Wirkungen der Stundung dahin (Art. 308 Abs. 2 SchKG) sowie alle vor der Stundung eingeleiteten Betreibungen mit Ausnahme der Pfandverwertungsbetreibungen (Art. 311 SchKG). Der bestätigte Vertrag bindet sämtliche Gläubiger von **Nachlassforderungen**, also Forderungen, die vor der Stundungsbewilligung oder danach ohne Zustimmung des Sachwalters entstanden sind — ausgenommen pfandgedeckte Forderungen (Art. 310 Abs. 1 SchKG). Nebenversprechen zur Bevorzugung einzelner Gläubiger sind nichtig (Art. 312 SchKG).

Das Gesetz kennt zwei Grundformen:

- **Ordentlicher Nachlassvertrag** (Art. 314–316 SchKG): Meist als **Dividendenvergleich** (Teilerlass gegen Zahlung einer Quote, allenfalls ganz oder teilweise in Beteiligungsrechten, Art. 314 Abs. 1bis SchKG) oder Stundungsvergleich. Für bestrittene Forderungen setzt das Nachlassgericht eine 20-tägige Klagefrist zur Sicherstellung der Dividende (Art. 315 SchKG). Ein eingesetzter Vollzieher (Art. 314 Abs. 2 SchKG) kann jedoch im Streitfall nicht per Verfügung nach Art. 17 SchKG entscheiden, ob eine Forderung als Masseverbindlichkeit oder als Nachlassforderung gilt: «Im Weiteren fehlt es an der Kompetenz der Aufsichtsbehörde, im Streitfall darüber zu entscheiden, ob eine Forderung gemäss Art. 310 Abs. 1 SchKG seit Bekanntmachung der Stundung "mit Zustimmung des Sachwalters" eingegangen worden sei» ([BGE 144 III 247](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_005_BGE-144-III-247_2018.html#consideration_2.3.2) E. 2.3.2); zuständig ist das Zivilgericht bzw. die in der Sache zuständige Instanz.
- **Nachlassvertrag mit Vermögensabtretung** (Liquidationsvergleich, Art. 317–331 SchKG): Der Schuldner tritt sein Vermögen den Gläubigern zur geordneten Verwertung durch Liquidatoren (unter Aufsicht eines Gläubigerausschusses) oder einem Dritten ab. Mit der Vollstreckbarkeit erlöschen das Verfügungsrecht des Schuldners und die Zeichnungsbefugnis der bisherigen Organe; im Handelsregister erhält die Firma den Zusatz *in Nachlassliquidation* (Art. 319 SchKG). Die Liquidatoren erstellen ohne neuen Schuldenruf einen Kollokationsplan (Art. 321 SchKG), verwerten die Aktiven (Art. 322–325 SchKG), können paulianische Anfechtungsansprüche geltend machen (Art. 331 SchKG) und verteilen den Erlös nach Verteilungsliste (Art. 326–329 SchKG).

### 3. Scheitern und Konkurseröffnung von Amtes wegen {#konkurseroeffnung}

Scheitert das Verfahren, eröffnet das Nachlassgericht **von Amtes wegen den Konkurs** — sowohl bei offensichtlicher Aussichtslosigkeit während der provisorischen Stundung (Art. 293a Abs. 3 SchKG), bei Verweigerung der definitiven Stundung (Art. 294 Abs. 3 SchKG), beim vorzeitigen Abbruch wegen Gefährdung des Vermögens, offensichtlicher Aussichtslosigkeit oder Zuwiderhandlung gegen Art. 298 SchKG bzw. Sachwalterweisungen (Art. 296b SchKG), bei ungenutztem Auslaufen der definitiven Stundung ohne Verlängerungsantrag des Sachwalters ([BGE 150 III 137](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_005_BGE-150-III-137_2024.html#consideration_4.) E. 4) als auch bei Ablehnung des Nachlassvertrages (Art. 309 SchKG).

Wird die definitive Stundung erst durch die Rechtsmittelinstanz aufgehoben und der Konkurs eröffnet, wirkt die Konkurseröffnung ***ex nunc*** per Datum des Beschwerdeentscheids: «Dies legt nahe, dass die Aufhebung der Nachlassstundung - nicht nur bei Gelingen der Sanierung vor Ablauf der Stundung ( Art. 296a Abs. 1 SchKG ), sondern auch beim von Amtes wegen zu eröffnenden Konkurs - ex nunc wirkt» ([BGE 147 III 226](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_005_BGE-147-III-226_2021.html#consideration_3.2.2) E. 3.2.2). Während der Stundung mit Zustimmung des Sachwalters eingegangene Verbindlichkeiten bleiben im nachfolgenden Konkurs **Masseverbindlichkeiten** (Art. 310 Abs. 2 SchKG).

## Abgrenzung: Einvernehmliche private Schuldenbereinigung {#private-schuldenbereinigung}

Für **natürliche Personen**, die nicht der Konkursbetreibung unterliegen, steht neben dem ordentlichen Nachlassverfahren die **einvernehmliche private Schuldenbereinigung** offen (Art. 333–336 SchKG). Das Nachlassgericht gewährt eine Stundung von höchstens **drei Monaten** (verlängerbar auf höchstens **sechs Monate**) und ernennt einen Sachwalter, der mit den Gläubigern über einen Bereinigungsvorschlag verhandelt (Art. 334 und 335 SchKG). Anders als beim gerichtlichen Nachlassvertrag besteht **kein Mehrheitszwang**: Jeder Gläubiger muss zustimmen. Während dieser Stundung bleibt die Betreibung für periodische familienrechtliche Unterhalts- und Unterstützungsbeiträge zulässig (Art. 334 Abs. 3 SchKG). Folgt dennoch ein ordentliches Nachlassverfahren, wird die bisherige Stundungsdauer angerechnet (Art. 336 SchKG).

## Rechtsmittelweg {#rechtsmittelweg}

Das Rechtsmittelsystem der Nachlassstundung ist stark ausdifferenziert, weil Verzögerungen durch Rechtsmittel den Sanierungserfolg vereiteln können:

| Entscheid | Kantonales Rechtsmittel | Aufschiebende Wirkung | Bundesgericht (BGG) |
|---|---|---|---|
| **Bewilligung provisorische Stundung / Ernennung prov. Sachwalter** (Art. 293d SchKG) | **nicht anfechtbar** (Ausnahme: Kostenvorschuss oder Ausstandsgründe gegen Sachwalter, BGE 141 III 188 E. 4.3 f.) | – | ausgeschlossen (Art. 293d SchKG, BGE 141 III 188 E. 4.2) |
| **Verweigerung provisorische Stundung mit Konkurseröffnung** (Art. 293a Abs. 3 SchKG) | Beschwerde nach ZPO (zehn Tage, Art. 321 Abs. 2 ZPO) | auf Antrag (Art. 325 Abs. 2 ZPO) | Beschwerde in Zivilsachen ohne Streitwertgrenze (Art. 74 Abs. 2 lit. d BGG), **volle Rechtsprüfung** nach Art. 95 BGG (BGE 142 III 364 E. 2.3 f.) |
| **Verweigerung provisorische Stundung ohne Konkurseröffnung** | Beschwerde nach ZPO (zehn Tage) | auf Antrag | Beschwerde in Zivilsachen ohne Streitwertgrenze, aber **nur Verfassungsrügen** nach Art. 98 BGG (BGer 5A_898/2024 E. 1.2) |
| **Definitive Stundung / Verlängerung / Abbruch** (Art. 295c, 296b SchKG) | Beschwerde nach ZPO durch Schuldner und Gläubiger (zehn Tage) | **ausgeschlossen** gegen Bewilligung (Art. 295c Abs. 2 SchKG) | Beschwerde in Zivilsachen ohne Streitwertgrenze (Art. 74 Abs. 2 lit. d BGG) |
| **Ermächtigung Anlagevermögen** (Art. 298 Abs. 2 SchKG) | Beschwerde nach ZPO **nur durch Schuldner** bei Abweisung; keine Legitimation von Gläubigern oder Gesellschaftern (BGE 147 III 226; BGE 152 III 398) | auf Antrag | wie kantonal (nur Schuldner bzw. Nichtigkeit) |
| **Aufhebung bei Sanierung** (Art. 296a Abs. 3 SchKG) | Beschwerde nach ZPO (zehn Tage) | auf Antrag | Beschwerde in Zivilsachen ohne Streitwertgrenze (Art. 74 Abs. 2 lit. d BGG) |
| **Bestätigung / Ablehnung Nachlassvertrag** (Art. 307 SchKG) | Beschwerde nach ZPO (zehn Tage) | **von Gesetzes wegen** (Art. 307 Abs. 2 SchKG) | Beschwerde in Zivilsachen ohne Streitwertgrenze (Art. 74 Abs. 2 lit. d BGG) |
| **Geschäftsführung des Sachwalters** (Art. 295 Abs. 4 SchKG) | Beschwerde an kantonale Aufsichtsbehörde (zehn Tage, Art. 17 SchKG) | auf Antrag (Art. 36 SchKG) | Beschwerde in Zivilsachen ohne Streitwertgrenze (Art. 74 Abs. 2 lit. c BGG) |

Im Einzelnen hat das Bundesgericht wichtige Abgrenzungen geklärt:

- **Art. 293d SchKG schliesst jedes Rechtsmittel aus**: Weder die kantonale Beschwerde noch die Beschwerde an das Bundesgericht stehen gegen die Bewilligung der provisorischen Stundung oder die Einsetzung des provisorischen Sachwalters offen ([BGE 141 III 188](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_005_BGE-141-III-188_2015.html#consideration_4.2) E. 4.2). Hingegen können Nebenanordnungen ausserhalb der gesetzlichen Aufzählung — etwa die Auferlegung des Kostenvorschusses — mit Beschwerde nach Art. 319 ff. ZPO (analog Art. 295c Abs. 1 SchKG) angefochten werden ([BGE 141 III 188](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_005_BGE-141-III-188_2015.html#consideration_4.4) E. 4.4).
- **Kognition vor Bundesgericht**: Verweigert das Gericht die provisorische Stundung und eröffnet gleichzeitig den Konkurs (Art. 293a Abs. 3 SchKG), liegt keine vorsorgliche Massnahme im Sinne von Art. 98 BGG vor; das Bundesgericht prüft Rechtsverletzungen frei nach Art. 95 BGG ([BGE 142 III 364](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_005_BGE-142-III-364_2016.html#consideration_2.3) E. 2.3 und 2.4). Wird das Gesuch hingegen ohne Konkurseröffnung abgewiesen (etwa mangels Unterlagen oder fehlendem Sanierungsbedarf), handelt es sich um eine vorsorgliche Massnahme, sodass vor Bundesgericht nur die Verletzung verfassungsmässiger Rechte gerügt werden kann ([BGer 5A_898/2024](https://entscheidsuche.ch/docs/CH_BGer/CH_BGer_005_5A-898-2024_2025-05-19.html) E. 1.2).
- **Rechtsmittel gegen Bestätigungsentscheid nicht verpassen**: Auch privilegierte Gläubiger müssen einen mangelhaften Bestätigungsentscheid rechtzeitig nach Art. 307 Abs. 1 SchKG anfechten. In [BGE 142 III 705](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_005_BGE-142-III-705_2016.html#consideration_4.2) E. 4.2 hatte eine Sachwalterin eine rechtzeitig eingegebene, privilegierte AHV-Beitragsforderung eigenmächtig nur teilweise aufgenommen; die Ausgleichskasse blieb untätig. «Den Entscheid des Nachlassgerichts hätte die Ausgleichskasse mit Beschwerde an das Obergericht des Kantons Thurgau weiterziehen müssen.» (a.a.O.). Weil der Bestätigungsentscheid unangefochten in Rechtskraft erwuchs, wurde der Nachlassvertrag auch für den nicht berücksichtigten Teil der privilegierten Forderung verbindlich.

## Kosten {#kosten}

Die gerichtlichen Kosten richten sich nach der Gebührenverordnung zum SchKG (GebV SchKG, SR 281.35):

- **Gerichtsgebühr**: Für Entscheide des Nachlassgerichts beträgt die Gebühr **200 bis 2500 Franken**; in besonderen Fällen kann das Nachlassgericht sie bis auf **5000 Franken** erhöhen (Art. 54 GebV SchKG).
- **Honorar der Organe**: Das Nachlassgericht setzt das Honorar des Sachwalters (sowie bei einem Liquidationsvergleich das Honorar der Liquidatoren und der Mitglieder des Gläubigerausschusses) **pauschal** fest; massgebend sind Schwierigkeit und Bedeutung der Sache, Umfang der Bemühungen, Zeitaufwand und Auslagen (Art. 55 Abs. 1 und 3 GebV SchKG).
- **Kostenvorschuss**: In der Praxis verlangt das Nachlassgericht regelmässig bereits zu Beginn der provisorischen Stundung einen angemessenen Vorschuss für die Gerichtskosten und das Honorar des provisorischen Sachwalters. Streitigkeiten über Höhe oder Kostentragung des Vorschusses unterliegen der Beschwerde nach Art. 319 ff. ZPO, nicht der Aufsichtsbeschwerde nach Art. 17 SchKG (BGE 141 III 188 E. 4.4).

## Stand der Gesetzgebung {#stand-der-gesetzgebung}

Mit der Vorlage [25.019 — Bundesgesetz über Schuldbetreibung und Konkurs (Sanierungsverfahren für natürliche Personen)](https://www.parlament.ch/de/ratsbetrieb/suche-curia-vista/geschaeft?AffairId=20250019) hat das Parlament am **19. Juni 2026** in den Schlussabstimmungen eine umfassende Revision des SchKG für überschuldete Privatpersonen verabschiedet (BBl 2026 1768; Stand 27. November 2026). Die Referendumsfrist lief am 8. Oktober 2026 ungenutzt ab; der Zeitpunkt des Inkrafttretens ist durch den Bundesrat noch nicht bestimmt. Für natürliche Personen soll die Revision zusätzlich zur einvernehmlichen privaten Schuldenbereinigung ein **vereinfachtes Nachlassverfahren** (mit Mehrheitsentscheid der Gläubiger) sowie ein **Sanierungskonkursverfahren** mit mehrjähriger Abschöpfung und anschliessender Restschuldbefreiung einführen. Das ordentliche Nachlassverfahren für Unternehmen (Art. 293–332 SchKG) bleibt in seinem grundlegenden Ablauf davon unberührt.

## Praxishinweise {#praxishinweise}

- **Für Verwaltungsräte und Geschäftsleitungen — frühzeitig planen, vollständig dokumentieren:** Reichen Sie das Stundungsgesuch ein, solange noch Liquidität für den laufenden Betrieb und den Sachwaltervorschuss vorhanden ist. Fehlen Bilanz, Liquiditätsplanung oder provisorischer Sanierungsplan (Art. 293 lit. a SchKG), droht die Abweisung oder die sofortige Konkurseröffnung. Prüfen Sie bei drohendem Reputationsschaden gezielt den Antrag auf eine **stille provisorische Stundung** (Art. 293c Abs. 2 SchKG).
- **Für Schuldner während der definitiven Stundung — Frist und Sachwalterantrag im Blick behalten:** Soll die definitive Stundung über sechs Monate hinaus verlängert werden, kann ausschliesslich der Sachwalter den Antrag stellen (Art. 295b Abs. 1 SchKG; BGE 150 III 137). Klären Sie die Haltung des Sachwalters rechtzeitig vor Fristablauf — ein eigener Verlängerungsantrag des Schuldners verhindert die Konkurseröffnung nicht.
- **Für Schuldner bei Vermögensverkäufen — immer Ermächtigung einholen:** Veräusserungen von Anlagevermögen oder Betriebsteilen ohne vorgängige Ermächtigung des Nachlassgerichts oder Gläubigerausschusses sind zwangsvollstreckungsrechtlich unbeachtlich (Art. 298 Abs. 2 SchKG) und können zum sofortigen Konkurs nach Art. 296b lit. c SchKG führen.
- **Für Gläubiger — Schuldenruf und Bestätigungsverhandlung aktiv wahrnehmen:** Geben Sie Forderungen innert der einmonatigen Frist des Schuldenrufs (Art. 300 SchKG) vollständig und belegt ein, um das Stimmrecht zu sichern. Kontrollieren Sie den Vertragsentwurf während der 20-tägigen Auflagefrist (Art. 301 SchKG) — auch als privilegierter Gläubiger: Werden Sie zu Unrecht gekürzt oder übergangen, müssen Sie den Bestätigungsentscheid innert zehn Tagen nach Art. 307 Abs. 1 SchKG anfechten (BGE 142 III 705).
- **Für Lieferanten und Vermieter — Zustimmung des Sachwalters schriftlich verlangen:** Neue Lieferungen oder Leistungen während der Stundung geniessen nur dann das Privileg einer **Masseverbindlichkeit** (Art. 310 Abs. 2 SchKG), wenn der Sachwalter zugestimmt hat. Bei einem bereits gekündigten Mietverhältnis bleibt die Ausweisungsklage trotz Nachlassstundung zulässig (BGE 143 III 173).
- **Für Gläubiger mit Bürgen oder Mitschuldnern — Zehn-Tage-Frist beachten:** Stimmen Sie einem Nachlassvertrag nur zu, wenn Sie zuvor Mitschuldner und Bürgen mindestens zehn Tage vor der Gläubigerversammlung informiert und ihnen die Abtretung gegen Zahlung angeboten haben (Art. 303 Abs. 2 SchKG); andernfalls verlieren Sie Ihre Rechte gegen diese.

## Leitentscheide {#leitentscheide}

| Entscheid | Gegenstand | Bedeutung |
|---|---|---|
| [BGE 141 III 188](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_005_BGE-141-III-188_2015.html#consideration_4.2) | Beschwerde gegen provisorische Nachlassstundung und Kostenvorschuss | Art. 293d SchKG schliesst kantonale und bundesgerichtliche Rechtsmittel gegen Bewilligung und Sachwalterernennung aus; Kostenvorschuss nach Art. 319 ff. ZPO anfechtbar |
| [BGE 142 III 364](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_005_BGE-142-III-364_2016.html#consideration_2.3) | Verweigerung der provisorischen Stundung mit Konkurseröffnung | Keine vorsorgliche Massnahme nach Art. 98 BGG; volle bundesgerichtliche Rechtsprüfung nach Art. 95 BGG |
| [BGE 142 III 705](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_005_BGE-142-III-705_2016.html#consideration_4.2) | Vom Sachwalter gekürzte privilegierte AHV-Forderung | Rechtskräftiger Bestätigungsentscheid bindet auch privilegierte Gläubiger, wenn diese keine Beschwerde nach Art. 307 Abs. 1 SchKG erheben |
| [BGE 143 III 173](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_005_BGE-143-III-173_2017.html#consideration_6.) | Ausweisungsklage gegen Mieterin in Nachlassstundung | Rückgabeanspruch nach Art. 267 Abs. 1 OR ist keine Nachlassforderung; keine Sistierung nach Art. 297 Abs. 5 SchKG; kein Fortführungsanspruch aus Art. 297a SchKG |
| [BGE 144 III 247](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_005_BGE-144-III-247_2018.html#consideration_2.3.2) | Kompetenzen des Vollziehers beim ordentlichen Nachlassvertrag | Streit über Entstehungszeitpunkt oder Zustimmung des Sachwalters (Art. 310 Abs. 1 SchKG) entscheidet das Zivilgericht, nicht der Vollzieher oder die Aufsichtsbehörde |
| [BGE 147 III 226](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_005_BGE-147-III-226_2021.html#consideration_3.1.3) | Unternehmensverkauf während stiller provisorischer Stundung; Verweigerung definitiver Stundung | Tiefere Hürde für provisorische Stundung (E. 3.1.3); *ex nunc*-Konkurseröffnung durch Rechtsmittelinstanz (E. 3.2.2); keine Gläubigerbeschwerde gegen Ermächtigung nach Art. 298 Abs. 2 SchKG (E. 4.3.3 f.) |
| [BGE 150 III 137](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_005_BGE-150-III-137_2024.html#consideration_3.6.2) | Verlängerung der definitiven Stundung über sechs Monate hinaus | Ausschliessliche Antragsberechtigung des Sachwalters nach Art. 295b Abs. 1 SchKG; ohne rechtzeitigen Antrag folgt der Konkurs von Amtes wegen |
| [BGE 151 III 516](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_005_BGE-151-III-516_2025.html#consideration_1.5.2) | Sistierung eines Zivilprozesses während Nachlassstundung | Sistierung nach Art. 297 Abs. 5 SchKG tritt *ex lege* ein; gerichtliche Verfügung ist bloss deklaratorisch |
| [BGE 152 III 398](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_005_BGE-152-III-398_2026.html#consideration_3.2.1) | Betriebsveräusserung während provisorischer Stundung (GmbH-Gesellschafter) | Auch Gesellschafter können die Ermächtigung nach Art. 298 Abs. 2 SchKG nicht mit Beschwerde anfechten; vorbehalten bleibt nur Nichtigkeit |
