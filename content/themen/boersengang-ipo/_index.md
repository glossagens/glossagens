---
title: "Börsengang (IPO) nach Schweizer Recht"
date: 2026-11-22
lastmod: 2026-11-22
description: "Wie ein Börsengang (Initial Public Offering) nach Schweizer Recht abläuft: gesellschaftsrechtliche Vorbereitung und Kapitalerhöhung (OR), Prospektpflicht und Prüfstelle (FIDLEG), Platzierung und Preisstabilisierung (FinfraG/FinfraV), Kotierung an der Börse (SIX/BX Swiss), Prospekthaftung, Folgepflichten und Emissionsabgabe."
tags: ["IPO", "Börsengang", "Kotierung", "Kapitalmarktrecht", "Aktienrecht", "Prospektpflicht", "Prospekthaftung", "FIDLEG", "FinfraG", "SIX Swiss Exchange", "Emissionsabgabe"]
typ: verfahren
kurz: "Bei einem Börsengang (IPO) öffnet sich eine Aktiengesellschaft dem breiten Publikum und lässt ihre Aktien zum Handel an einer Schweizer Börse (meist SIX Swiss Exchange oder BX Swiss) zulassen. Rechtlich greifen drei Ebenen ineinander: die gesellschaftsrechtliche Vorbereitung samt Kapitalerhöhung und Bezugsrechtsentzug nach Obligationenrecht (OR), die Erstellung und vorgängige Genehmigung eines Emissionsprospekts nach dem Finanzdienstleistungsgesetz (FIDLEG) sowie das Kotierungsverfahren nach dem Finanzmarktinfrastrukturgesetz (FinfraG) und den Reglementen der Börse. Mit dem ersten Handelstag untersteht die Gesellschaft dauerhaften kapitalmarkt- und aktienrechtlichen Folgepflichten."
sachgebiete: [schuldrecht.gesellschaft, wirtschaftsaufsicht]
normen:
  - { gesetz: or, art: art-650 }
  - { gesetz: or, art: art-652b }
  - { gesetz: or, art: art-653s }
  - { gesetz: or, art: art-659 }
  - { gesetz: or, art: art-685d }
  - { gesetz: or, art: art-704 }
  - { gesetz: or, art: art-716a }
  - { gesetz: or, art: art-732 }
  - { gesetz: or, art: art-754 }
  - { gesetz: stg, art: art-005 }
  - { gesetz: stg, art: art-006 }
  - { gesetz: stg, art: art-008 }
stichworte: ["IPO", "Initial Public Offering", "Börsengang", "Kotierung", "Prospektpflicht", "Prospekthaftung", "FIDLEG", "FinfraG", "SIX Swiss Exchange", "BX Swiss", "Bookbuilding", "Greenshoe", "Emissionskonsortium", "Kapitalerhöhung", "Bezugsrecht", "Emissionsabgabe", "Ad-hoc-Publizität", "Angebotspflicht"]
revisions:
  - date: 2026-11-22
    by: "Antigravity"
    model: "gemini-4-neon"
    note: "Erstfassung nach Skill glossagens-themen (Typ verfahren). Normtexte aus OR, FIDLEG, FinfraG, FinfraV, BEG und StG über Fedlex-MCP geprüft; Art. 652b OR und Art. 5 StG per {{< wortlaut >}} eingebunden. Leitentscheide (BGE 121 III 219, 130 II 530, 131 III 306, 132 III 715, 137 II 371, 137 III 37, 149 II 462) gegen die Volltexte auf entscheidsuche.ch verifiziert; SIX-Kotierungsvoraussetzungen gemäss Kotierungsreglement (KR) geprüft; pruefen.py und build-check.sh bestanden."
---

## Überblick {#ueberblick}

Ein *Initial Public Offering* (IPO, Börsengang) ist das erstmalige öffentliche Angebot von Beteiligungspapieren einer Gesellschaft, verbunden mit deren Zulassung zum Handel an einer Börse (Kotierung). Wirtschaftlich dient der Börsengang der Eigenkapitalfinanzierung des Unternehmens oder dem teilweisen oder vollständigen Ausstieg bisheriger Eigentümer. Rechtlich handelt es sich um einen mehrstufigen Vorgang an der Schnittstelle von Gesellschaftsrecht, Kapitalmarktrecht und börslicher Selbstregulierung.

In der Praxis treten drei Grundformen auf:

- **Primary Offering**: Die Gesellschaft gibt im Rahmen einer Kapitalerhöhung neue Aktien aus und nimmt den Emissionserlös selbst ein.
- **Secondary Offering**: Bestehende Aktionäre veräussern bereits existierende Aktien an das Publikum; der Gesellschaft fliesst kein neues Kapital zu.
- **Kombiniertes Angebot**: Neue Aktien aus einer Kapitalerhöhung werden zusammen mit bestehenden Aktien platziert (in der Schweiz der Regelfall bei grösseren Börsengängen).

Abzugrenzen ist der klassische IPO vom *Direct Listing*, bei dem bereits bestehende Aktien ohne vorgängiges öffentliches Platzierungsangebot und ohne Emissionskonsortium direkt zum Börsenhandel zugelassen werden, sowie vom Börsengang über eine *Special Purpose Acquisition Company* (SPAC), bei dem zunächst ein Akquisitionsvehikel kotiert wird, das später mit dem Zielunternehmen fusioniert.

## Rechtsgrundlagen {#rechtsgrundlagen}

Das Schweizer IPO-Recht ist nicht in einem einzelnen Gesetz kodifiziert, sondern verteilt sich auf Bundesgesetze, Ausführungsverordnungen und das Reglementswerk des jeweiligen Handelsplatzes:

| Ebene | Erlass | Regelungsgegenstand beim IPO |
|---|---|---|
| Gesellschaftsrecht | Obligationenrecht (OR, SR 220) | Kapitalerhöhung, Kapitalband, Bezugsrechtsentzug, Vinkulierung, Vergütungsordnung für Publikumsgesellschaften, Wertrechte |
| Effektenrecht | Bucheffektengesetz (BEG, SR 957.1) | Entstehung und Übertragung von Bucheffekten über Verwahrungsstellen |
| Kapitalmarktrecht (Primärmarkt) | Finanzdienstleistungsgesetz (FIDLEG, SR 950.1) und FIDLEV | Prospektpflicht, Prospektinhalt, Ex-ante-Prüfung durch die Prüfstelle, Werbung, Prospekthaftung |
| Kapitalmarktrecht (Sekundärmarkt) | Finanzmarktinfrastrukturgesetz (FinfraG, SR 958.1) und FinfraV | Handelsplätze, börsliche Selbstregulierung, Offenlegung bedeutender Beteiligungen, Übernahmerecht, Insider- und Marktmanipulationsverbot, Preisstabilisierung |
| Börsliche Selbstregulierung | Kotierungsreglement (KR) und Richtlinien (SIX Exchange Regulation / BX Swiss) | Materielle Kotierungsvoraussetzungen, Kotierungsverfahren, Ad-hoc-Publizität, Management-Transaktionen |
| Steuerrecht | Bundesgesetz über die Stempelabgaben (StG, SR 641.10) | Emissionsabgabe (1 % auf entgeltlicher Begründung von Beteiligungsrechten), Umsatzabgabe |

## Das Verfahren im Überblick {#verfahren-ueberblick}

Ein Börsengang dauert von den ersten gesellschaftsrechtlichen Vorbereitungen bis zum ersten Handelstag typischerweise vier bis neun Monate. Die nachfolgende Übersicht fasst die fünf Kernphasen zusammen:

| Phase | Zuständige Organe / Stellen | Zentrale Rechtsgrundlagen | Typische Dauer / Frist |
|---|---|---|---|
| 1. Vorbereitung und *IPO-Readiness* | Verwaltungsrat, Revisionsstelle, Rechtsberater, Konsortialbanken | Art. 704, 716a, 732 ff. OR; KR SIX/BX | 2–4 Monate |
| 2. Prospekterstellung und Prüfung | Emittent, Banken, Prüfstelle (SIX Exchange Regulation AG / BX Swiss AG) | Art. 35–57 FIDLEG | Prüfung: bis zu 20 Kalendertage bei neuen Emittenten (Art. 53 Abs. 5 FIDLEG) |
| 3. Kotierungsgesuch | Emittent über anerkannten Vertreter, Zulassungsstelle der Börse | Art. 35 FinfraG; KR SIX/BX | Gesuchseinreichung i. d. R. mind. 20 Börsentage vor dem ersten Handelstag |
| 4. *Bookbuilding*, Kapitalerhöhung und Zuteilung | Generalversammlung, Verwaltungsrat, Handelsregisteramt, Konsortialbanken | Art. 650, 652b, 653s OR; Art. 64 Abs. 2 FIDLEG | Angebotsfrist: Prospekt mind. 6 Arbeitstage vor Angebotsende verfügbar; HR-Eintragung vor Handel |
| 5. Erster Handelstag und Stabilisierung | Börse, Stabilisierungsmanager (Wertpapierhaus), Emittent | Art. 659 OR; Art. 143 FinfraG, Art. 126 FinfraV | Stabilisierungsperiode: längstens 30 Tage nach Platzierung (Art. 126 lit. a FinfraV) |

## Gesellschaftsrechtliche Vorbereitung und Strukturierung {#vorbereitung}

### Umwandlung, Statutenanpassung und Corporate Governance {#vorbereitung-governance}

Nur eine Aktiengesellschaft (oder Kommanditaktiengesellschaft) kann ihre Beteiligungspapiere an einer Schweizer Börse kotieren lassen. Gesellschaften in anderer Rechtsform (z. B. GmbH) müssen vorab nach dem Fusionsgesetz umgewandelt werden. Der Verwaltungsrat leitet das IPO-Projekt im Rahmen seiner unübertragbaren Oberleitungs- und Finanzplanungskompetenz ([Art. 716a OR](/kommentar/or/art-716a/)).

Regelmässig sind die Statuten mit qualifiziertem Mehr der Generalversammlung (Art. 704 Abs. 1 OR) an die Anforderungen einer Publikumsgesellschaft anzupassen:

- **Übertragbarkeit der Aktien (Vinkulierung)**: Bei börsenkotierten Namenaktien darf die Gesellschaft einen Erwerber nach Art. 685d Abs. 1 OR nur ablehnen, wenn die Statuten eine prozentmässige Begrenzung vorsehen und diese überschritten wird, oder wenn der Erwerber auf Verlangen keine Erklärung abgibt, die Aktien im eigenen Namen und auf eigene Rechnung zu erwerben (Art. 685d Abs. 2 OR). Weitergehende statutarische Vinkulierungsbestimmungen (wie bei privaten Gesellschaften zulässig) sind vor der Kotierung aufzuheben.
- **Vergütungsordnung und Unabhängigkeit**: Mit der Kotierung greifen die Bestimmungen über Vergütungen bei Gesellschaften, deren Aktien an einer Börse kotiert sind (Art. 732 ff. OR): Die Generalversammlung stimmt jährlich verbindlich über die Gesamtbeträge der Vergütungen des Verwaltungsrats, der Geschäftsleitung und des Beirats ab; die Statuten müssen die Grundsätze der Vergütungen, Zusatzbeträge, Kreditgrenzen und die maximale Anzahl zulässiger externer Mandate regeln.
- **Wertrechte und Bucheffekten**: Für den börslichen Handel werden die Aktien regelmässig als einfache Wertrechte nach Art. 973c OR ausgestaltet oder als Globalurkunde hinterlegt und durch Eintragung im Hauptregister einer zentralen Verwahrungsstelle (in der Schweiz SIX SIS AG) sowie Gutschrift auf Effektenkonten als Bucheffekten nach Art. 3 und Art. 6 BEG geschaffen.

### Kapitalerhöhung und Bezugsrechtsentzug {#vorbereitung-kapitalerhoehung}

Um neue Aktien für das *Primary Offering* zu schaffen, stehen nach dem seit 1. Januar 2023 geltenden Aktienrecht zwei Wege offen:

1. **Ordentliche Kapitalerhöhung (Art. 650 OR)**: Die Generalversammlung beschliesst mit öffentlicher Urkunde den Nennbetrag (oder maximalen Nennbetrag) sowie die weiteren Angaben nach Art. 650 Abs. 2 OR und ermächtigt den Verwaltungsrat häufig zur Festsetzung des endgültigen Ausgabebetrags nach Abschluss des *Bookbuildings*. Die Kapitalerhöhung muss innerhalb von sechs Monaten beim Handelsregisteramt zur Eintragung angemeldet werden (Art. 650 Abs. 3 OR).
2. **Kapitalband (Art. 653s OR)**: Alternativ kann die Generalversammlung in den Statuten ein Kapitalband einführen (qualifiziertes Mehr nach Art. 704 Abs. 1 Ziff. 5 OR) und den Verwaltungsrat ermächtigen, das Aktienkapital während längstens fünf Jahren innerhalb einer Bandbreite von bis zu plus 50 Prozent des im Handelsregister eingetragenen Kapitals zu erhöhen. Das Kapitalband ersetzt seit 2023 die frühere genehmigte Kapitalerhöhung.

Sollen die neuen Aktien beim IPO nicht den bisherigen Aktionären, sondern neuen öffentlichen Investoren zugeteilt werden, muss das gesetzliche Bezugsrecht der Altaktionäre eingeschränkt oder aufgehoben werden:

{{< wortlaut gesetz="or" art="art-652b" >}}

Der Beschluss über die Einschränkung oder Aufhebung des Bezugsrechts bedarf des qualifizierten Mehrs der Generalversammlung (Art. 704 Abs. 1 Ziff. 4 OR) und eines wichtigen Grundes im Sinne von Art. 652b Abs. 2 OR. Das Bundesgericht hat bereits in [BGE 121 III 219](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_005_BGE-121-III-219_1995-04-25.html#consideration_3.) E. 3 klargestellt, dass die Aufzählung im Gesetz «nicht abschliessend, sondern lediglich exemplifikatorisch» ist; die Interessenabwägung bei bestimmten Finanzierungssituationen vermag einen Bezugsrechtsentzug zu rechtfertigen, namentlich wenn damit «eine Kotierung der Aktien an ausländischen Börsen» oder eine gezielte Aktienplatzierung zur Verbreiterung des Aktionariats verbunden ist. Gemäss Art. 652b Abs. 4 OR darf zudem weder durch den Entzug des Bezugsrechts noch durch die Festsetzung des Ausgabebetrags jemand in unsachlicher Weise begünstigt oder benachteiligt werden.

## Prospektpflicht, Prospektprüfung und Werbung {#prospekt}

### Anwendungsbereich und Ausnahmen {#prospekt-pflicht}

Wer in der Schweiz ein öffentliches Angebot zum Erwerb von Effekten unterbreitet oder um Zulassung von Effekten zum Handel auf einem Handelsplatz nach Art. 26 lit. a FinfraG ersucht, hat vorgängig einen Prospekt zu veröffentlichen (Art. 35 Abs. 1 FIDLEG). Beim klassischen IPO greifen beide Tatbestände kumulativ.

Die Ausnahmen von der Prospektpflicht nach der Art des Angebots (Art. 36 Abs. 1 FIDLEG — etwa Angebote ausschliesslich an professionelle Kunden, an weniger als 500 Anlegerinnen und Anleger, mit einer Mindeststückelung oder Mindestanlagesumme von 100 000 Franken oder einem Gesamtwert unter 8 Millionen Franken innert 12 Monaten) gelten beim regulären IPO mit Publikumsangebot und Kotierung nicht, da die Zulassung zum Handel an einer Börse ihrerseits eine eigenständige Prospektpflicht auslöst.

### Inhalt, Sprache und Zusammenfassung {#prospekt-inhalt}

Der Prospekt enthält gemäss Art. 40 Abs. 1 FIDLEG die für einen Anlageentscheid wesentlichen Angaben zum Emittenten (Organe, letzte Jahres- oder Halbjahresrechnung, Geschäftslage, Perspektiven, Risiken und Rechtsstreitigkeiten), zu den Effekten (Rechte, Pflichten, Risiken) und zum Angebot (Art der Platzierung, geschätzter Nettoerlös). Er kann in einer Amtssprache des Bundes oder in Englisch abgefasst werden (Art. 40 Abs. 2 FIDLEG), was bei internationalen Transaktionen der Standard ist.

Können der endgültige Emissionskurs und das Emissionsvolumen bei Prospektveröffentlichung vor dem *Bookbuilding* noch nicht genannt werden, muss der Prospekt den höchstmöglichen Emissionskurs (oder die Preisspanne) sowie die Kriterien zur Ermittlung des Volumens nennen; die endgültigen Angaben sind anschliessend bei der Prüfstelle zu hinterlegen und zu veröffentlichen (Art. 40 Abs. 4 FIDLEG). Dem Prospekt ist eine leicht verständliche Zusammenfassung voranzustellen (Art. 40 Abs. 3 und Art. 43 FIDLEG).

### Ex-ante-Prüfung, Veröffentlichung und Nachtragspflicht {#prospekt-pruefung}

Seit dem Inkrafttreten des FIDLEG am 1. Januar 2020 unterliegen Emissions- und Kotierungsprospekte für Beteiligungspapiere zwingend einer vorgängigen (Ex-ante-)Prüfung durch eine von der FINMA zugelassene Prüfstelle (Art. 51 Abs. 1 FIDLEG; in der Schweiz sind die Prüfstellen der SIX Exchange Regulation AG und der BX Swiss AG zugelassen). Die Prüfstelle prüft den Prospekt auf Vollständigkeit, Kohärenz und Verständlichkeit — nicht jedoch auf dessen wirtschaftliche Richtigkeit oder Werthaltigkeit.

Das Prüfverfahren richtet sich nach dem Verwaltungsverfahrensgesetz (Art. 53 Abs. 1 FIDLEG). Bei neuen Emittenten — also im Regelfall eines IPO — beträgt die Prüfungsfrist 20 Kalendertage ab Eingang (Art. 53 Abs. 5 FIDLEG; bei bereits kotierten Emittenten 10 Kalendertage nach Art. 53 Abs. 3 und 4 FIDLEG). Erfolgt innert Frist kein Entscheid, gilt dies ausdrücklich nicht als Genehmigung (Art. 53 Abs. 6 FIDLEG).

Nach Genehmigung ist der Prospekt bei der Prüfstelle zu hinterlegen und spätestens mit Beginn des öffentlichen Angebots oder der Zulassung zum Handel zu veröffentlichen (Art. 64 Abs. 1 FIDLEG). Soll erstmals eine Gattung von Beteiligungspapieren zum Handel zugelassen werden, muss der Prospekt mindestens sechs Arbeitstage vor dem Ende des Angebots zur Verfügung gestellt werden (Art. 64 Abs. 2 FIDLEG). Treten zwischen Genehmigung und Angebotsende beziehungsweise Handelsaufnahme neue Tatsachen ein, die die Bewertung der Effekten wesentlich beeinflussen könnten, ist umgehend ein Nachtrag einzureichen (Art. 56 Abs. 1 und 2 FIDLEG). Die Prüfstelle entscheidet darüber innert höchstens sieben Kalendertagen; während eines öffentlichen Angebots verlängert sich die Angebotsfrist so, dass sie frühestens zwei Tage nach Veröffentlichung des Nachtrags endet, wobei Zeichner ihre Zusagen zurückziehen können (Art. 56 Abs. 3 und 5 FIDLEG).

Werbung für die angebotenen Aktien muss als solche klar erkennbar sein, auf den Prospekt sowie dessen Bezugsstelle hinweisen und inhaltlich mit dem Prospekt übereinstimmen (Art. 68 FIDLEG).

## Übernahme, Bookbuilding und Preisstabilisierung {#platzierung}

### Emissionskonsortium und Underwriting-Vertrag {#platzierung-konsortium}

Die Platzierung der Aktien begleitet regelmässig ein Bankenkonsortium unter Führung eines oder mehrerer *Global Coordinators* bzw. *Lead Managers*. Im *Underwriting Agreement* zwischen Emittent, gegebenenfalls verkaufenden Altaktionären und dem Konsortium wird üblicherweise eine feste Übernahme (*Firm Commitment Underwriting*) vereinbart: Die Konsortialbanken zeichnen die neuen Aktien (bzw. übernehmen die bestehenden Aktien) gegen eine Übernahmekommission und verpflichten sich, diese am Markt zu platzieren. Seltener — insbesondere bei kleineren Emissionen — erfolgt eine blosse Platzierung auf Kommissionsbasis (*Best Efforts*).

Zum Schutz des nachbörslichen Kurses verpflichten sich die Gesellschaft, die Mitglieder von Verwaltungsrat und Geschäftsleitung sowie wesentliche Altaktionäre regelmässig zu einer Veräusserungssperre (*Lock-up*) von meist sechs bis zwölf Monaten ab dem ersten Handelstag.

### Bookbuilding, Greenshoe und Preisstabilisierung {#platzierung-stabilisierung}

Die Preisfindung erfolgt bei Schweizer IPOs nahezu durchwegs im *Bookbuilding*-Verfahren: Auf Basis einer im Prospekt veröffentlichten Preisspanne sammeln die Konsortialbanken unverbindliche Zeichnungsaufträge institutioneller Investoren (*Orderbook*), um nach Ablauf der Zeichnungsfrist gemeinsam mit dem Emittenten den endgültigen Emissionspreis festzusetzen.

Um Kursschwankungen in den ersten Handelswochen abzufedern, wird den Konsortialbanken regelmässig eine Mehrzuteilungsoption (*Greenshoe* bzw. *Over-Allotment Option*) von typischerweise bis zu 15 Prozent des Basisangebots eingeräumt. Die Banken teilen zunächst mehr Aktien zu, als im Basisangebot vorgesehen sind, und decken diese Überzuteilung entweder durch Käufe am offenen Markt (bei sinkendem Kurs unter den Emissionspreis) oder durch Ausübung der Mehrzuteilungsoption (bei steigendem Kurs).

Rechtlich greift hier eine wichtige kapitalmarktrechtliche Ausnahme: Künstliche Eingriffe in Angebot, Nachfrage oder Kurs sind nach Art. 143 Abs. 1 FinfraG grundsätzlich als Marktmanipulation verboten. Art. 126 FinfraV erklärt Effektengeschäfte zur Preisstabilisierung nach einer öffentlichen Platzierung jedoch ausdrücklich für zulässig, sofern fünf kumulative Voraussetzungen erfüllt sind:

1. Die Stabilisierungsgeschäfte werden innerhalb von 30 Tagen nach der öffentlichen Platzierung getätigt (Art. 126 lit. a FinfraV).
2. Sie erfolgen höchstens zum Emissionspreis (Art. 126 lit. b FinfraV).
3. Die maximale Stabilisierungsdauer und das zuständige Wertpapierhaus werden vor Handelsaufnahme veröffentlicht (Art. 126 lit. c FinfraV).
4. Die Geschäfte werden dem Handelsplatz innert fünf Handelstagen gemeldet und vom Emittenten innert fünf Handelstagen nach Ablauf der 30-Tage-Frist veröffentlicht (Art. 126 lit. d FinfraV).
5. Die Ausübung einer Mehrzuteilungsoption wird innert fünf Handelstagen öffentlich bekanntgegeben (Art. 126 lit. e FinfraV).

Erwirbt im Rahmen von Stabilisierungs- oder Rückkaufprogrammen die Gesellschaft selbst eigene Aktien, ist die aktienrechtliche Grenze von Art. 659 OR (frei verwendbares Eigenkapital in Höhe des Anschaffungswerts und Beschränkung auf grundsätzlich 10 Prozent des Aktienkapitals) einzuhalten.

## Kotierungsverfahren an der Börse {#kotierung}

### Börsliche Selbstregulierung und Handelsplätze {#kotierung-selbstregulierung}

Nach Art. 27 und Art. 35 FinfraG regeln die Schweizer Börsen — namentlich die **SIX Swiss Exchange** und die **BX Swiss** — die Zulassung von Effekten zum Handel im Rahmen der von der FINMA genehmigten Selbstregulierung selbst. Das Bundesgericht hat diese Struktur in [BGE 137 III 37](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_005_BGE-137-III-37_2011.html#consideration_2.2.1) E. 2.2.1 (noch zum früheren Art. 8 BEHG) dahin charakterisiert, dass die reglementarischen Vorschriften des Kotierungsreglements «einen wichtigen Teil der börslichen Selbstregulierung» bilden.

### Materielle Kotierungsvoraussetzungen und Verfahren {#kotierung-voraussetzungen}

Die Einzelheiten richten sich nach dem Kotierungsreglement (KR) des gewählten Handelsplatzes und des jeweiligen Marktsegments. Für das ordentliche Hauptsegment der SIX Swiss Exchange (*International Reporting Standard* oder *Swiss Reporting Standard*) gelten nach dem KR namentlich folgende Eckwerte:

- **Bestandesdauer**: Der Emittent muss in der Regel während mindestens drei Jahren als Unternehmen bestanden und entsprechende Jahresabschlüsse vorgelegt haben (Ausnahmen für junge Wachstumsunternehmen oder das KMU-Segment *Sparks* sind in den jeweiligen Zusatzreglementen geregelt).
- **Eigenkapital**: Das ausgewiesene (bzw. konsolidierte) Eigenkapital muss am ersten Handelstag mindestens CHF 2,5 Millionen betragen.
- **Streubesitz (Free Float)**: Mindestens 20 Prozent der ausstehenden Beteiligungspapiere derselben Kategorie müssen sich im Publikum befinden und eine Marktkapitalisierung von mindestens CHF 25 Millionen erreichen.
- **Rechnungslegung und Revision**: Anwendung eines anerkannten Rechnungslegungsstandards (IFRS, US GAAP oder Swiss GAAP FER je nach Segment) sowie Prüfung durch ein staatlich beaufsichtigtes Revisionsunternehmen im Sinne von Art. 7 und Art. 8 RAG (Art. 35 Abs. 2 lit. d FinfraG).

Das Kotierungsgesuch wird durch einen bei der Börse anerkannten Vertreter (in der Praxis eine spezialisierte Anwaltskanzlei oder Bank) eingereicht, üblicherweise mindestens 20 Börsentage vor dem geplanten ersten Handelstag. Nach Prüfung durch die Zulassungsstelle (bei SIX: SIX Exchange Regulation AG) ergeht der Kotierungsentscheid unter Vorbehalt der erfolgreichen Platzierung und Handelsregistereintragung neuer Aktien.

### Rechtsschutz bei Verweigerung der Zulassung {#kotierung-rechtsmittel}

Wird die Kotierung verweigert (oder später widerrufen), muss die Börse nach Art. 37 Abs. 1 FinfraG eine unabhängige Beschwerdeinstanz vorsehen. Erst nach Durchführung dieses börseninternen Beschwerdeverfahrens steht die Klage beim Zivilgericht offen (Art. 37 Abs. 4 FinfraG). Wie das Bundesgericht in [BGE 137 III 37](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_005_BGE-137-III-37_2011.html#consideration_2.2.2) E. 2.2.2 entschieden hat, ist dieser gesetzlich vorgezeichnete Rechtsweg zwingend und kann durch eine blosse Reglementsbestimmung nicht durch ein Schiedsgericht ersetzt werden.

## Haftung und strafrechtliche Risiken {#haftung}

### Prospekthaftung (Art. 69 FIDLEG) {#haftung-prospekt}

Mit dem Inkrafttreten des FIDLEG wurde die Prospekthaftung aus dem Aktienrecht (aArt. 752 OR) in Art. 69 FIDLEG überführt. Wer in Prospekten, im Basisinformationsblatt oder in ähnlichen Mitteilungen unrichtige, irreführende oder den gesetzlichen Anforderungen nicht entsprechende Angaben macht, ohne dabei die erforderliche Sorgfalt anzuwenden, haftet dem Erwerber eines Finanzinstruments für den dadurch verursachten Schaden (Art. 69 Abs. 1 FIDLEG). Eingeschränkt ist die Haftung für die Zusammenfassung (Haftung nur, wenn sie zusammen mit dem übrigen Prospekt gelesen irreführend, unrichtig oder widersprüchlich ist, Art. 69 Abs. 2 FIDLEG) sowie für zukunftsgerichtete Aussagen über wesentliche Perspektiven (Haftung nur wider besseres Wissen oder ohne Hinweis auf die Ungewissheit, Art. 69 Abs. 3 FIDLEG).

Die Rechtsprechung zu aArt. 752 OR bleibt für die Grundfragen der Aktivlegitimation und der Kausalität wegweisend:

- **Aktivlegitimation**: Nach [BGE 131 III 306](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_005_BGE-131-III-306_2005.html#consideration_2.1) E. 2.1 ist «nicht nur der Zeichner während der Angebotsfrist, sondern auch der spätere Käufer klageberechtigt, sofern […] die Angaben im Prospekt kausal für seinen Kaufentschluss waren». Auch wer die Titel erst am Sekundärmarkt nach dem ersten Handelstag erwirbt, kann somit Ansprüche geltend machen, solange der Prospekt für seinen Erwerb mitbestimmend war.
- **Kausalität und Beweismass**: In [BGE 132 III 715](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_005_BGE-132-III-715_2006.html#consideration_3.2.1) E. 3.2.1 hielt das Bundesgericht fest, dass wegen der typischen Beweisnot des Anlegers «das Beweismass der überwiegenden Wahrscheinlichkeit für den Nachweis des Kausalzusammenhangs ausreicht und kein strikter Beweis verlangt werden kann». Beim Erstkäufer innerhalb der Zeichnungsfrist ist regelmässig davon auszugehen, dass die Prospektangaben für den Kaufentschluss direkt kausal waren; beim späteren Sekundärmarktkäufer sinkt diese Vermutung mit zunehmender Zeitspanne.

Neben der spezialgesetzlichen Prospekthaftung kann gegenüber den Organen der Gesellschaft die allgemeine aktienrechtliche Verantwortlichkeit nach [Art. 754 OR](/kommentar/or/art-754/) greifen, wobei bei einem durch die Gesellschaft erlittenen Schaden im Konkurs die besondere Klageordnung nach Art. 757 OR zu beachten ist (BGE 131 III 306 E. 3).

### Strafrechtliche Risiken {#haftung-strafrecht}

Wer vorsätzlich im Prospekt falsche Angaben macht oder wesentliche Tatsachen verschweigt oder den Prospekt nicht spätestens mit Beginn des öffentlichen Angebots veröffentlicht, wird nach Art. 90 Abs. 1 FIDLEG mit Busse bis zu 500 000 Franken bestraft. Darüber hinaus kommen bei unwahren Angaben gegenüber dem Handelsregister oder in beurkundeten Kapitalerhöhungsakten Urkundendelikte (Art. 251, 253 StGB) sowie nach der Handelsaufnahme die Straftatbestände des Ausnützens von Insiderinformationen (Art. 154 FinfraG) und der Kursmanipulation (Art. 155 FinfraG) in Betracht — Letztere sehen bei Vermögensvorteilen über einer Million Franken Freiheitsstrafen bis zu fünf Jahren vor.

## Folgepflichten nach dem Börsengang {#folgepflichten}

Mit dem ersten Handelstag wechselt das Unternehmen vom geschlossenen Kreis einer privaten Gesellschaft in das Regime der Publikumsgesellschaft. Die wichtigsten laufenden Pflichten sind:

- **Periodische Berichterstattung**: Veröffentlichung geprüfter Jahres- und ungeprüfter Halbjahresberichte nach dem gewählten Rechnungslegungsstandard sowie eines Corporate-Governance-Berichts und eines Vergütungsberichts.
- **Ad-hoc-Publizität**: Unverzügliche Bekanntgabe potenziell kursrelevanter Tatsachen, die im Tätigkeitsbereich des Emittenten eingetreten sind und nicht öffentlich bekannt sind (gemäss KR SIX/BX).
- **Management-Transaktionen**: Meldung von Käufen und Verkäufen von Beteiligungspapieren des Emittenten durch Mitglieder des Verwaltungsrats und der Geschäftsleitung an den Emittenten und durch diesen an die Börse.
- **Offenlegung bedeutender Beteiligungen**: Nach Art. 120 Abs. 1 FinfraG muss jedermann, der Aktien einer in der Schweiz kotierten Gesellschaft erwirbt oder veräussert und dabei die Schwellenwerte von 3, 5, 10, 15, 20, 25, 33⅓, 50 oder 66⅔ Prozent der Stimmrechte erreicht, über- oder unterschreitet, dies der Gesellschaft und der Börse melden. Nach Art. 120 Abs. 4 lit. a FinfraG löst bereits die erstmalige Kotierung selbst die Meldepflicht für bestehende Grossaktionäre aus. Wie das Bundesgericht in [BGE 137 II 371](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_004_BGE-137-II-371_2011.html#consideration_5.1) E. 5.1 zur Vorgängernorm (Art. 20 aBEHG) erläutert hat, erfasst die Pflicht sowohl direkte als auch indirekte Erwerbe und Handlungen in gemeinsamer Absprache.
- **Öffentliches Übernahmerecht und Angebotspflicht**: Überschreitet ein Aktionär oder eine gemeinsam handelnde Gruppe nach der Kotierung den Grenzwert von 33⅓ Prozent der Stimmrechte, entsteht die Pflicht, ein öffentliches Übernahmeangebot für alle kotierten Beteiligungspapiere zu unterbreiten (Art. 135 Abs. 1 FinfraG; zur historischen Ausgestaltung der Angebotspflicht vgl. [BGE 130 II 530](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_004_BGE-130-II-530_2004.html#consideration_5.1.1) E. 5.1.1). Gesellschaften können diese Schwelle vor der Kotierung in den Statuten auf bis zu 49 Prozent anheben (*Opting-up*, Art. 135 Abs. 1 Satz 2 FinfraG) oder die Angebotspflicht vor der Kotierung ganz ausschliessen (*Opting-out*, Art. 125 Abs. 3 FinfraG).
- **Insider- und Marktmanipulationsverbot**: Ab Zulassung zum Handel gelten die verwaltungsrechtlichen Verbote des Ausnützens von Insiderinformationen (Art. 142 FinfraG) und der Marktmanipulation (Art. 143 FinfraG) neben den entsprechenden Strafnormen.

## Kosten und Steuern {#kosten-steuern}

### Emissionsabgabe {#kosten-emissionsabgabe}

Werden beim IPO im Rahmen einer Kapitalerhöhung (*Primary Offering*) neue Beteiligungsrechte begründet, fällt grundsätzlich die eidgenössische Emissionsabgabe an:

{{< wortlaut gesetz="stg" art="art-005" >}}

Die Abgabe beträgt nach [Art. 8 Abs. 1 lit. a StG](/kommentar/stg/art-008/#abs-1-lit-a--begründung-und-erhöhung-von-beteiligungsrechten) 1 Prozent und bemisst sich vom gesamten Betrag, der der Gesellschaft als Gegenleistung für die neuen Aktien zufliesst — also einschliesslich eines allfälligen Agios (Emissionsaufgeld), mindestens aber vom Nennwert (vgl. zur Behandlung von Agio und Verrechnungsliberierung auch [BGE 149 II 462](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_004_BGE-149-II-462_2023.html#consideration_3.1) E. 3.1 f.). Bei einer Kapitalerhöhung gilt zwar ein einmaliger Freibetrag von 1 Million Franken (Art. 6 Abs. 1 lit. h StG); dieser ist bei wachstumsstarken Unternehmen allerdings häufig bereits durch frühere Finanzierungsrunden ausgeschöpft.

Demgegenüber löst der blosse Verkauf bereits bestehender Aktien durch Altaktionäre (*Secondary Offering*) keine Emissionsabgabe aus, da keine neuen Beteiligungsrechte geschaffen werden. Bei Transaktionen unter Mitwirkung eines Effektenhändlers (z. B. einer Schweizer Bank) ist indes die Umsatzabgabe auf der Übertragung entgeltlicher Urkunden zu prüfen, wobei für bestimmte Primärmarktvorgänge Befreiungstatbestände nach StG bestehen.

### Transaktions- und Konsortialkosten {#kosten-transaktion}

Zu den direkten Transaktionskosten zählen die Konsortialkommissionen der Banken (üblicherweise ein prozentualer Abschlag auf dem Bruttoemissionserlös), die Gebühren der Prüfstelle für die Prospektgenehmigung, die Kotierungsgebühren der Börse, Kosten für Rechtsberatung, Wirtschaftsprüfung und öffentliche Beurkundung sowie laufende Kosten für Investor Relations und die fortlaufende Börsenkotierung.

## Praxishinweise {#praxishinweise}

- **Für Verwaltungsrat und Geschäftsleitung**: Beginnen Sie mit der *IPO-Readiness* mindestens sechs Monate vor dem angepeilten Handelsstart. Klären Sie frühzeitig, ob die Statuten vor der Kotierung ein *Opting-out* oder *Opting-up* (Art. 125 Abs. 3, Art. 135 Abs. 1 FinfraG) vorsehen sollen, da eine nachträgliche Einführung nach der Kotierung der aktienrechtlichen Anfechtungskontrolle (Art. 706 OR) unterliegt. Richten Sie interne Insider-Listen und Sperrfristen (*Blackout Periods*) bereits vor dem ersten Handelstag ein.
- **Für Emissionsbanken und Berater**: Planen Sie für die Prospektprüfung bei neuen Emittenten die gesetzliche Frist von 20 Kalendertagen (Art. 53 Abs. 5 FIDLEG) zuzüglich allfälliger Nachbesserungsrunden fest in den Zeitplan ein und stellen Sie sicher, dass der Prospekt bei Erstkotierung mindestens sechs Arbeitstage vor Angebotsende verfügbar ist (Art. 64 Abs. 2 FIDLEG). Dokumentieren Sie bei Preisstabilisierungsmassnahmen lückenlos die Einhaltung der 30-Tage-Frist, der Preisobergrenze sowie der fünftägigen Melde- und Publikationspflichten nach Art. 126 FinfraV.
- **Für Anlegerinnen und Anleger**: Stützen Sie eine Zeichnungsentscheidung nicht allein auf die Prospektzusammenfassung oder Marketingunterlagen — die Haftung für die Zusammenfassung ist nach Art. 69 Abs. 2 FIDLEG eingeschränkt, und für zukunftsgerichtete Prognosen wird nur bei Arglist oder fehlendem Risikohinweis gehaftet (Art. 69 Abs. 3 FIDLEG). Beachten Sie zudem bei eigenen Aktienkäufen nach der Kotierung die Meldeschwelle von 3 Prozent der Stimmrechte (Art. 120 FinfraG).

## Leitentscheide {#leitentscheide}

| Entscheid | Gegenstand | Bedeutung |
|---|---|---|
| [BGE 121 III 219](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_005_BGE-121-III-219_1995-04-25.html#consideration_3.) E. 3 | Bezugsrechtsentzug (Art. 652b OR) | Aufzählung wichtiger Gründe ist nicht abschliessend; Kotierung und gezielte Aktienplatzierung können den Entzug des Bezugsrechts rechtfertigen. |
| [BGE 137 III 37](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_005_BGE-137-III-37_2011.html#consideration_2.2.1) E. 2.2 | Börsliche Selbstregulierung und Rechtsweg | Kotierungsreglement ist Teil der börslichen Selbstregulierung; der gesetzliche Rechtsweg über die Beschwerdeinstanz zum Zivilgericht kann nicht durch Reglement ersetzt werden. |
| [BGE 131 III 306](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_005_BGE-131-III-306_2005.html#consideration_2.1) E. 2.1 | Prospekthaftung: Aktivlegitimation | Nicht nur Erstzeichner, sondern auch spätere Käufer am Sekundärmarkt sind klageberechtigt, sofern die Prospektangaben kausal für den Kaufentschluss waren. |
| [BGE 132 III 715](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_005_BGE-132-III-715_2006.html#consideration_3.2.1) E. 3.2.1 | Prospekthaftung: Beweismass der Kausalität | Für den Kausalzusammenhang zwischen falschen Prospektangaben und Kaufentschluss genügt das Beweismass der überwiegenden Wahrscheinlichkeit. |
| [BGE 137 II 371](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_004_BGE-137-II-371_2011.html#consideration_5.1) E. 5.1 | Offenlegung von Beteiligungen | Konkretisierung der Meldepflicht bei Erreichen, Über- oder Unterschreiten der Stimmrechtsschwellen einschliesslich indirekter Erwerbe und gemeinsamen Handelns. |
| [BGE 130 II 530](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_004_BGE-130-II-530_2004.html#consideration_5.1.1) E. 5.1 | Angebotspflicht im Übernahmerecht | Grundsätze zur Pflicht zur Unterbreitung eines öffentlichen Übernahmeangebots bei Überschreiten der Kontrollschwelle (heute Art. 135 FinfraG). |
| [BGE 149 II 462](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_004_BGE-149-II-462_2023.html#consideration_3.1) E. 3.1 | Emissionsabgabe und Agio (Art. 5, 8 StG) | Behandlung von Agio und Verrechnungsliberierung bei Kapitalerhöhungen im Stempelabgaberecht. |
