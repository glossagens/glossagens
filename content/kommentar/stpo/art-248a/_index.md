---
title: "Art. 248a StPO — Zuständigkeit zur Entsiegelung und Verfahren"
weight: 248
date: "2024-01-01"
lastmod: "2026-09-10"
description: "Praxisorientierter Kommentar zu Art. 248a StPO: Zuständigkeit des Entsiegelungsgerichts, Formgültigkeit des Gesuchs, Drittinhaberschaft, Substanziierung der Geheimnisgründe, Triageverhandlung, Sachverständigenbeizug und Rechtsmittel — mit ausführlicher Kasuistik zu Anwaltskorrespondenz, Smartphone-Durchsuchungen, Geschäfts-/Bankgeheimnissen, Datenspiegelung und Polizeiforensik."
tags: ["StPO", "Zwangsmassnahmen", "Entsiegelung", "Zwangsmassnahmengericht", "Geheimnisschutz", "Art. 248a StPO", "Substanziierungsobliegenheit", "Praxiskommentar"]
agent_verified: false
revisions:
  - date: "2026-09-10"
    by: "Claude Code"
    model: "claude-sonnet-5"
    mcp_verified: true
    note: "Praxisorientierter Ausbau nach dem Leitfaden 'praxisorientierter-kommentar': Gliederung auf die Tatbestands-/Verfahrensmerkmale der Norm umgestellt (Prüfschema A–L), zu jedem Merkmal ausführliche Sachverhaltsschilderung aus dem Volltext verifizierter Entscheide (Erwägungen einzeln über get_erwaegung/get_decision_structure/entscheidsuche gegen den Volltext geprüft), Grenzkasuistik-Tabellen und Praxishinweise ergänzt. Dabei zwei weitere Fehlzitate aufgedeckt und korrigiert, die die frühere Audit-Runde nicht erfasst hatte, weil ihnen kein prüfbares Behauptungssatz-Beleg-Paar zugeordnet war: (1) BGer 7B_486/2024 wurde fälschlich eine 'Triageverhandlung unter Beizug eines externen IT-Forensikers' zugeschrieben — der Entscheid betrifft tatsächlich eine Gehörsverletzung mangels vorgängiger Akteneinsicht in 54 Mio. sichergestellte Objekte (E. 4.4); (2) BGer 7B_245/2026 wurde ein abgewiesenes Rügeergebnis zugeschrieben ('Bundesgericht wies die Rüge ab') — tatsächlich wurde die Beschwerde gutgeheissen, weil das kantonale ZMG mit dem 'Kompetenzzentrum Digitale Forensik' eine Behörde statt einer natürlichen Person als Sachverständige bezeichnet und Entsiegelung und Triage unzulässig vermengt hatte (E. 4.3, E. 5.2) — beide invertierten Ergebnisse jetzt korrekt dargestellt. Zusätzlich Sachverhalt und Erwägungen von BGE 151 IV 30, BGE 151 IV 344/350, BGE 152 IV 107, BGE 148 IV 221 sowie BGer 7B_1170/2025, 7B_558/2025, 7B_1154/2024, 7B_419/2025 im Volltext verifiziert (bislang nur Kernsatz-Ebene). Anschliessend vollständiges Stufe-5-Grounding über alle 106 Paare durchlaufen (89 beurteilt: 79 von einem unabhängigen Judge-Subagenten in einem Zug, 10 durch Claude Code selbst nach Textänderungen) — dabei drei weitere, kleinere echte Fehler entdeckt und korrigiert: (a) BGE 151 IV 175 trug eine erfundene, nirgends belegte Tatvorwurfsangabe ('ungetreue Geschäftsbesorgung') sowie einen falschen zweiten Geheimnisgrund ('Geschäftsgeheimnis' statt richtig Art. 264 Abs. 1 lit. b — Schutz persönlicher Aufzeichnungen); anhand des über get_decision (full_text) nachgeholten Sachverhalts auf den tatsächlichen Fall (Förderung der Prostitution/BetmG-Verbrechen, Durchsuchung bei der Ex-Ehefrau, zwei iPhones) korrigiert. (b) Eine Erwägung von BGer 7B_1154/2024 (E. 2.2, Position der Bundesanwaltschaft zur Rechtsmissbräuchlichkeit) war fälschlich dem Bundesgericht selbst zugeschrieben; richtiggestellt. (c) Ein Pinpoint bei 7B_1154/2024 (Geschäftsgeheimnis-Ausschluss) zeigte auf E. 2.4.2 statt korrekt E. 2.4.3; berichtigt. Ergebnis nach Korrektur: 52% Belegquote (32 gestützt + 18 teilweise von 79 beurteilten Paaren, 0 offen) → weiterhin Urteil B. Die verbleibenden 'ungestützt'-Treffer wurden einzeln gegen den tatsächlich zitierten Volltext nachgeprüft und sind durchweg Parser-Artefakte (Regeste-only-Prüfung bei Sachverhalts-Aussagen; Mehrfachzitate im selben Absatz, bei denen ein in der Nähe genannter zweiter Entscheid — insbesondere bei der Praxisänderungs-Darstellung BGE 148 IV 221 → BGE 152 IV 107 — fälschlich als Prüfquelle herangezogen wird). agent_verified bleibt dennoch auf false, da Urteil B (nicht A) und die Stufe-4-Verbatim-Prüfung methodisch nur gegen get_decision_structure/get_regeste (nicht gegen die vollständigen get_erwaegung-Texte) abgleicht, wodurch mehrere lange, wortgetreu übernommene Blockzitate als 'nicht gefunden' markiert werden, obschon sie im Gespräch direkt aus get_erwaegung kopiert wurden — stichprobenartig verifiziert, aber nicht als audit.py-Fix behoben."
  - date: "2026-09-10"
    by: "Claude Code"
    model: "claude-sonnet-5"
    mcp_verified: true
    note: "Audit-Nachbesserung: Rz. 12 (Berufsgeheimnisse) enthielt eine invertierte Wiedergabe von BGer 7B_419/2025 E. 3.3 (Name+Speicherort genügen, keine E-Mail/Telefonnummer nötig) — korrigiert. Rz. 4 (Zwischenverfügungen/Nichteintreten) und Rz. 18 (Rechtsmissbrauch: Strafverfolgungsbehörde statt ZMG) auf zutreffende Erwägungen umgestellt (7B_1170/2025 E. 1.3 f., 7B_165/2026 E. 2.4, 7B_1154/2024 E. 2.4.1). Rz. 1 und Rz. 8 von unpassenden Fallzitaten auf Botschaft/Gesetzeswortlaut umgestellt. Datum von BGer 7B_165/2026 und 7B_133/2026 korrigiert (war 15.07.2026, korrekt 05.08.2026 laut entscheidsuche.ch) und deren Links von mcp.opencaselaw.ch auf entscheidsuche.ch migriert. Stufe-5-Grounding (Judge, einfach beurteilt, ohne Zweitmeinung) danach vollständig durchlaufen: 72% Belegquote (19 gestützt + 4 teilweise von 29 beurteilten Paaren) → Urteil B. agent_verified bleibt auf false; Details siehe audit-report.json."
  - date: "2026-09-02"
    by: "Antigravity Agent"
    model: "gemini-3.7-flash"
    mcp_verified: true
    note: "Einarbeitung von BGer 7B_165/2026 vom 15. Juli 2026 und BGer 7B_133/2026 (publiziert 02.09.2026): Analoge Geltung von Art. 110 StPO für Entsiegelungsgesuche der Staatsanwaltschaft; Formungültigkeit von E-Mail-Gesuchen ohne qualifizierte elektronische Signatur und Nichteintreten."
  - date: "2026-09-02"
    by: "Antigravity"
    model: "gemini-3.7-flash"
    mcp_verified: true
    note: "Vollständige Überarbeitung und Vertiefung des Kommentars gemäss StPO-Revision 2024; Einarbeitung von BGE 151 IV 175, BGE 151 IV 344/350, BGE 152 IV 107, BGer 7B_1170/2025, 7B_486/2024, 7B_419/2025, 7B_245/2026; 100% verifizierte entscheidsuche.ch-Links."
---

## Gesetzeswortlaut

> **Art. 248a StPO — Zuständigkeit zur Entsiegelung und Verfahren**
>
> 1 Stellt die Strafbehörde ein Entsiegelungsgesuch, so ist für den Entscheid zuständig:
> a. im Vorverfahren und im Verfahren vor dem erstinstanzlichen Gericht: das Zwangsmassnahmengericht;
> b. in den anderen Fällen: die Verfahrensleitung des Gerichts, bei dem der Fall hängig ist.
>
> 2 Stellt das Gericht nach Eingang des Entsiegelungsgesuchs fest, dass die Inhaberin oder der Inhaber nicht mit der an den Aufzeichnungen oder Gegenständen berechtigten Person identisch ist, so informiert es diese über die Siegelung. Es gewährt der berechtigten Person auf Verlangen Akteneinsicht.
>
> 3 Das Gericht setzt der berechtigten Person eine nicht erstreckbare Frist von 10 Tagen, innert der sie Einwände gegen das Entsiegelungsgesuch vorzubringen und sich dazu zu äussern hat, in welchem Umfang sie die Siegelung aufrechterhalten will. Stillschweigen gilt als Rückzug des Siegelungsbegehrens.
>
> 4 Ist die Sache spruchreif, so entscheidet das Gericht innert 10 Tagen nach Eingang der Stellungnahme im schriftlichen Verfahren endgültig.
>
> 5 Andernfalls setzt es innert 30 Tagen seit Eingang der Stellungnahme eine nicht öffentliche Verhandlung mit der Staatsanwaltschaft und der berechtigten Person an. Die berechtige Person hat die Gründe glaubhaft zu machen, weshalb und in welchem Umfang die Aufzeichnungen oder Gegenstände nicht entsiegelt werden dürfen. Das Gericht fällt seinen Entscheid unverzüglich; dieser ist endgültig.
>
> 6 Das Gericht kann:
> a. eine sachverständige Person beiziehen, um den Inhalt der Aufzeichnungen und Gegenstände zu prüfen, den Zugang zu diesen zu erhalten oder deren Integrität zu gewährleisten;
> b. Angehörige der Polizei als sachverständige Personen bezeichnen, um den Zugang zum Inhalt der Aufzeichnungen und Gegenstände zu erhalten oder deren Integrität zu gewährleisten.
>
> 7 Bleibt die berechtigte Person der Verhandlung unentschuldigt fern und lässt sie sich auch nicht vertreten, so gilt das Siegelungsbegehren als zurückgezogen. Erscheint die Staatsanwaltschaft nicht, so entscheidet das Gericht in deren Abwesenheit.

---

## I. Überblick und Entstehungsgeschichte

**Rz. 1** Art. 248a StPO regelt das gerichtliche Verfahren zur Entsiegelung sichergestellter Aufzeichnungen und Gegenstände. Die Bestimmung wurde im Rahmen der Revision der Strafprozessordnung vom 17. Juni 2022 (in Kraft seit 1. Januar 2024, [BBl 2019 6697](https://www.fedlex.admin.ch/eli/fbl/2019/6697/de), S. 6750 ff.) neu geschaffen. Das Entsiegelungsverfahren, das zuvor in den Absätzen 2 bis 4 des bisherigen Art. 248 StPO geregelt war, wurde damit gesetzessystematisch verselbstständigt und verfahrensrechtlich grundlegend neu geordnet (Botschaft, [BBl 2019 6697](https://www.fedlex.admin.ch/eli/fbl/2019/6697/de), S. 6750 ff.).

**Rz. 2** Hauptziel der gesetzlichen Neukonzeption war die Beschleunigung und Straffung des Entsiegelungsverfahrens zur Vermeidung jahrelanger Verfahrensblockaden. Wie gravierend das Problem unter altem Recht war, zeigt der Fall einer Rechtsverzögerungsbeschwerde der Bundesanwaltschaft: Seit Februar 2020 waren beim Kantonalen Zwangsmassnahmengericht Bern drei Entsiegelungsverfahren im Zusammenhang mit einer Untersuchung wegen ungetreuer Geschäftsbesorgung und Bestechung fremder Amtsträger hängig; die letzte Verfahrenshandlung datierte vom 19. Januar 2022. Das Bundesgericht stellte im Juni 2024 eine Verletzung des aus Art. 29 Abs. 1 BV, Art. 6 Ziff. 1 EMRK und Art. 5 StPO fliessenden Beschleunigungsgebots fest und verpflichtete das Zwangsmassnahmengericht, bis Ende des laufenden Kalenderjahres abschliessend zu entscheiden — mehr als vier Jahre nach Eingang des ersten Gesuchs ([BGer 7B_484/2023 vom 03.06.2024 E. 2.1.3 und E. 3.1](https://entscheidsuche.ch/docs/CH_BGer/CH_BGer_007_7B-484-2023_2024-06-03.html)). Zwar war unbestritten, dass der Umfang der versiegelten Daten und die Komplexität des Verfahrens den Beizug eines Sachverständigen erforderten; dies rechtfertigte nach Auffassung des Bundesgerichts aber keinen mehrjährigen Stillstand. Auf diese strukturellen Verzögerungen reagierte der Gesetzgeber mit klaren Fristen, einer gesetzlichen Rückzugsfiktion bei Säumnis (Abs. 3 und Abs. 7), einer optionalen Triageverhandlung (Abs. 5) sowie einer ausdrücklichen Rechtsgrundlage für den Beizug technischer Sachverständiger und Polizeispezialisten (Abs. 6).

**Rz. 3** Inhaltlich verschärfte die Revision zugleich die materiellen Geheimnisschutzgründe: Der Bundesrat hatte in seinem Entwurf noch vorgeschlagen, auch «Fabrikations- und Geschäftsgeheimnisse» als eigenständigen Entsiegelungsgrund zuzulassen ([BBl 2019 6795](https://www.fedlex.admin.ch/eli/fbl/2019/6697/de) f.). National- und Ständerat folgten dem nicht und beschränkten die zulässigen Siegelungsgründe abschliessend auf den Katalog von Art. 264 StPO — mit der Folge, dass allgemeine Geschäfts-, Fabrikations- und Bankkundengeheimnisse seit dem 1. Januar 2024 keinen eigenständigen Entsiegelungsgrund mehr bilden ([BGE 151 IV 30 E. 2.4.1–2.4.2](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-151-IV-30_2025.html#consideration_2.4.2)).

---

## II. Prüfschema

Der praxisorientierte Zugriff auf Art. 248a StPO folgt nicht der Chronologie der Absätze, sondern den Fragen, die sich einer Verfahrensbeteiligten der Reihe nach stellen. Die folgende Tabelle ist zugleich das Inhaltsverzeichnis der Abschnitte III–XIV.

| | Merkmal | Norm | Kernfrage | Massgeblicher Massstab |
|---|---|---|---|---|
| A | Zuständigkeit des Entsiegelungsgerichts | Abs. 1 | ZMG oder Verfahrensleitung? Einzige kantonale Instanz? | Rechtsfrage von Amtes wegen |
| B | Formgültigkeit des Entsiegelungsgesuchs | Abs. 1 i.V.m. Art. 110 StPO | Gesuch formgerecht eingereicht? | Strafbehörde: volle Formstrenge, keine Nachfrist |
| C | Gültigkeit des Siegelungsbegehrens (Vorfrage) | — | Offensichtlich unbegründet, missbräuchlich oder verspätet? | Strafverfolgungsbehörde darf direkt ablehnen |
| D | Information und Akteneinsicht Dritter | Abs. 2 | Inhaberin/Inhaber ≠ berechtigte Person? | Gericht von Amtes wegen |
| E | Substanziierung der Geheimnisgründe | Abs. 3 i.V.m. Art. 264 StPO | Welches Geheimnis, wo gespeichert, weshalb schützenswert? | berechtigte Person: Glaubhaftmachung, abgestuft nach Geheimnisart |
| F | Akzessorische Rügen | Abs. 3/5 i.V.m. Art. 197 StPO | Tatverdacht und Verhältnismässigkeit der Zwangsmassnahme? | Gericht von Amtes wegen, sobald ein Art.-264-Grund vorliegt |
| G | Fristwahrung und Rückzugsfiktion | Abs. 3 | 10-Tage-Frist gewahrt? | berechtigte Person; nicht erstreckbare Verwirkungsfrist |
| H | Schriftlicher Endentscheid bei Spruchreife | Abs. 4 | Ist die Sache spruchreif? | — |
| I | Triageverhandlung und Akteneinsicht | Abs. 5 | Erfordert die Datenmenge eine mündliche Verhandlung und vorgängige Einsicht? | berechtigte Person: Glaubhaftmachung an der Verhandlung |
| J | Sachverständigenbeizug | Abs. 6 | Natürliche Person? Funktionentrennung gewahrt? | Gericht: pflichtgemässes Ermessen |
| K | Säumnisfolgen an der Verhandlung | Abs. 7 | Fernbleiben der berechtigten Person bzw. der Staatsanwaltschaft? | — |
| L | Rechtsmittel | Art. 380, 78 ff. BGG, Art. 93 Abs. 1 lit. a BGG | Droht ein nicht wieder gutzumachender Nachteil? | Beschwerdeführerin: Substanziierung |

---

## III. A — Zuständigkeit des Entsiegelungsgerichts (Abs. 1)

**Rz. 4** Für den Entscheid über das Entsiegelungsgesuch der Strafbehörde ist im Vorverfahren sowie im Verfahren vor dem erstinstanzlichen Gericht ausschliesslich das Zwangsmassnahmengericht (ZMG) zuständig (Abs. 1 lit. a). In den übrigen Fällen — namentlich im Berufungsverfahren — liegt die Zuständigkeit bei der Verfahrensleitung des angerufenen Gerichts (Abs. 1 lit. b). Das Zwangsmassnahmengericht entscheidet dabei gemäss Abs. 1 lit. a und Abs. 4 i.V.m. Art. 380 StPO als **einzige kantonale Instanz**; ein kantonaler Weiterzug ist ausgeschlossen, die Beschwerde in Strafsachen führt direkt ans Bundesgericht (Art. 78 ff. BGG).

**Der Fall der entsperrten und gespiegelten Mobiltelefone (Basel-Stadt).** Wie weit diese funktionelle Zuständigkeit reicht, zeigt ein Verfahren, das seinen Ursprung in einer Betäubungsmittel-Strafuntersuchung des Kantons Basel-Stadt hatte. Ein Beschuldigter war in Entsprechung eines Rechtshilfeersuchens in Antwerpen festgenommen worden; bei der dortigen Hausdurchsuchung wurden mehrere Mobiltelefone sichergestellt und den Basler Behörden ausgehändigt. Mit superprovisorischer Verfügung hiess das Zwangsmassnahmengericht Basel-Stadt das Gesuch der Staatsanwaltschaft um Entsperrung und Spiegelung der Datenträger gut und beauftragte damit das Kompetenzzentrum IT-Forensik der Zuger Polizei; zugleich ordnete es die provisorische Siegelung sowohl der gespiegelten als auch der originalen Datenträger an. Der Beschuldigte machte in der Folge geltend, das Zwangsmassnahmengericht sei für diese blosse Zwischenverfügung gar nicht zuständig gewesen — dafür wäre die allgemeine Beschwerdeinstanz nach Art. 393 Abs. 1 lit. c StPO zuständig, nicht das Entsiegelungsgericht. Das Bundesgericht folgte dem nicht:

> «Die Vorinstanz handelte als Entsiegelungsgericht im Sinne von Art. 248a Abs. 1 lit. a StPO, als sie mit Verfügung vom 19. März 2024 das Gesuch der Staatsanwaltschaft um Entsperrung und Spiegelung der sichergestellten Datenträger guthiess, was sich bereits darin zeigt, dass sie darin die provisorische Siegelung sowohl der gespiegelten als auch der originalen Datenträger anordnete.»
> — [BGer 7B_1170/2025 vom 03.03.2026 E. 1.3](https://entscheidsuche.ch/docs/CH_BGer/CH_BGer_007_7B-1170-2025_2026-03-03.html#consideration_1.3)

Diese ausschliessliche funktionelle Zuständigkeit erstreckt sich also nicht nur auf den verfahrensabschliessenden Sachentscheid, sondern auch auf verfahrensleitende Zwischenverfügungen wie die Entsperrung und Spiegelung sichergestellter Datenträger, weshalb auch dagegen nur die Beschwerde in Strafsachen ans Bundesgericht offensteht, nicht der kantonale Beschwerdeweg ([BGer 7B_1170/2025 E. 1.4](https://entscheidsuche.ch/docs/CH_BGer/CH_BGer_007_7B-1170-2025_2026-03-03.html#consideration_1.3)). Dieselbe Zuständigkeitsfrage stellte sich in einem Parallelfall aus dem Tessin, in dem der direkte Weiterzug ans Bundesgericht ohne kantonalen Instanzenzug ebenfalls bestätigt wurde ([BGer 7B_219/2026 vom 20.08.2026 E. 1.1](https://entscheidsuche.ch/docs/CH_BGer/CH_BGer_007_7B-219-2026_2026-08-20.html#consideration_1.1)).

**Nichteintretensentscheide wegen formungültiger Gesuche.** Die funktionelle Zuständigkeit erfasst auch den umgekehrten Fall, dass das ZMG auf ein Entsiegelungsgesuch gar nicht erst eintritt (dazu sogleich Abschnitt B). Auch ein solcher Nichteintretensentscheid ist ein Entscheid des Entsiegelungsgerichts nach Art. 248a StPO und unterliegt derselben Beschwerdeordnung: In dem sogleich geschilderten Fall des unsignierten E-Mail-Gesuchs bestätigte das Bundesgericht seine Zuständigkeit für die Beschwerde gegen den Nichteintretensentscheid ausdrücklich unter Hinweis auf Art. 80 Abs. 2 Satz 3 BGG i.V.m. Art. 78 ff. BGG ([BGer 7B_165/2026 vom 05.08.2026 E. 1.1](https://entscheidsuche.ch/docs/CH_BGer/CH_BGer_007_7B-165-2026_2026-08-05.html)).

> **Leitsatz.** Die ausschliessliche funktionelle Zuständigkeit des Zwangsmassnahmengerichts als einzige kantonale Instanz (Art. 248a Abs. 1 lit. a i.V.m. Art. 380 StPO) erfasst nicht nur den verfahrensabschliessenden Entsiegelungsentscheid, sondern jede in diesem Zusammenhang ergehende Zwischenverfügung — einschliesslich der Anordnung von Entsperrung und Spiegelung sowie des Nichteintretens auf ein formungültiges Gesuch.

**Vereinbarkeit mit dem nemo-tenetur-Grundsatz.** Im selben Basler Verfahren rügte der Beschuldigte zusätzlich, die im Entsiegelungsverfahren statuierten Mitwirkungsobliegenheiten verstiessen gegen den Grundsatz *nemo tenetur se ipsum accusare*, weil er letztlich gezwungen werde, an seiner eigenen Überführung mitzuwirken. Das Bundesgericht verwarf auch diese Rüge: Die gesetzlichen Mitwirkungs- und Substanziierungsobliegenheiten im Entsiegelungsverfahren dienten ausschliesslich der Durchsetzung privater Geheimhaltungsinteressen der berechtigten Person selbst, nicht der Sachverhaltsaufklärung zulasten der beschuldigten Person, und verletzten die Selbstbelastungsfreiheit deshalb nicht ([BGer 7B_1170/2025 E. 2.3 und E. 2.1](https://entscheidsuche.ch/docs/CH_BGer/CH_BGer_007_7B-1170-2025_2026-03-03.html)).

---

## IV. B — Formgültigkeit des Entsiegelungsgesuchs (Art. 110 StPO analog)

**Rz. 5** Das Entsiegelungsgesuch der Staatsanwaltschaft an das ZMG unterliegt den allgemeinen Formvorschriften für Eingaben gemäss [Art. 110 StPO](https://glossagens.ch/kommentar/stpo/art-110/), die analog auch für Strafbehörden gelten.

**Der Fall des unsignierten E-Mail-Gesuchs (Zürich).** Die Staatsanwaltschaft Limmattal/Albis führte eine Strafuntersuchung wegen Betrugs gegen A. und zwei Mitbeschuldigte. Bei einer Hausdurchsuchung wurden zwei Mobiltelefone, drei Laptops sowie Akten sichergestellt und gleichentags auf Verlangen von A. gesiegelt. Die Staatsanwaltschaft gelangte darauf mit einer **elektronischen Eingabe per E-Mail** ans Zwangsmassnahmengericht des Bezirksgerichts Dietikon und verlangte die Entsiegelung; der eingescannte Antrag war von der leitenden und der zuständigen Assistenz-Staatsanwältin zwar handschriftlich unterzeichnet, aber nicht mit einer qualifizierten elektronischen Signatur versehen. Das Zwangsmassnahmengericht trat auf das Gesuch mangels gültiger Form nicht ein. Die dagegen erhobene Beschwerde der Oberstaatsanwaltschaft des Kantons Zürich blieb erfolglos. Das Bundesgericht bestätigte, dass für das Entsiegelungsgesuch dieselbe Schriftform gilt wie für Parteieingaben nach Art. 110 StPO — unabhängig davon, ob es sich um eine Behörde oder eine Privatperson handelt:

> «Obwohl das erwähnte Urteil eine private Partei betroffen habe, müsse gleiches für verfahrenseinleitende Gesuche der Staatsanwaltschaft gelten. Dabei sei gemäss Bundesgericht unerheblich, ob die Identität des Absenders dem Gericht bekannt sei und ob das Gesuch tatsächlich von der genannten Partei stamme.»
> — [BGer 7B_165/2026 vom 05.08.2026 E. 2.3](https://entscheidsuche.ch/docs/CH_BGer/CH_BGer_007_7B-165-2026_2026-08-05.html#consideration_2.3)

Das Bundesgericht bestätigte auch die Begründung der Vorinstanz im Ergebnis: Reicht die Staatsanwaltschaft das Entsiegelungsgesuch per einfacher E-Mail ohne qualifizierte elektronische Signatur ein, ist das Gesuch formunwirksam.

> «Die vorstehend wiedergegebenen Erwägungen der Vorinstanz sind überzeugend. Diese verletzt kein Bundesrecht, wenn sie zum Schluss gelangt, das Entsiegelungsgesuch müsse schriftlich gestellt werden und der nicht elektronisch signierte Versand per E-Mail genüge nicht.»
> — [BGer 7B_165/2026 E. 2.4](https://entscheidsuche.ch/docs/CH_BGer/CH_BGer_007_7B-165-2026_2026-08-05.html#consideration_2.4)

Zu den damit bestätigten Erwägungen der Vorinstanz gehörte auch, dass eine Nachfrist zur Verbesserung nicht anzusetzen ist, weil das Gesuch von einer rechtskundigen Behörde stammte, die nicht geltend machte, das Fehlen der Signatur beruhe auf einem Versehen oder unverschuldeten Hindernis ([BGer 7B_165/2026 E. 2.3.2](https://entscheidsuche.ch/docs/CH_BGer/CH_BGer_007_7B-165-2026_2026-08-05.html)). In einem am selben Tag von derselben Abteilung des Bundesgerichts entschiedenen Verfahren wurde dieselbe Rechtsfolge bestätigt ([BGer 7B_133/2026 vom 05.08.2026 E. 2.3](https://entscheidsuche.ch/docs/CH_BGer/CH_BGer_007_7B-133-2026_2026-08-05.html)).

> **Leitsatz.** Art. 110 Abs. 1 und 2 StPO gilt analog für Entsiegelungsgesuche der Staatsanwaltschaft. Ein per einfacher E-Mail ohne qualifizierte elektronische Signatur eingereichtes Gesuch ist formunwirksam; das Zwangsmassnahmengericht tritt darauf nicht ein, ohne der Staatsanwaltschaft eine Nachfrist zur Verbesserung anzusetzen.

---

## V. C — Gültigkeit des Siegelungsbegehrens: Rechtsmissbrauch vor dem Entsiegelungsverfahren

**Rz. 6** Art. 248a StPO setzt voraus, dass überhaupt gesiegelt wurde. Nicht das Zwangsmassnahmengericht, sondern bereits die mit der Sicherstellung befasste Strafverfolgungsbehörde darf ein offensichtlich unbegründetes oder missbräuchliches Siegelungsbegehren direkt ablehnen bzw. darauf nicht eintreten — in diesen Fällen kommt es gar nicht erst zu einer Siegelung, die ein Entsiegelungsverfahren nach Art. 248a StPO nötig machen würde.

**Der Fall der Mosambik-Bankunterlagen.** Die Bundesanwaltschaft eröffnete im Kontext des sogenannten Mosambik-«Schuldenskandals» ein Strafverfahren wegen Geldwäschereiverdachts: Gegenstand war eine Zahlung von USD 7,86 Mio. mutmasslich deliktischer Herkunft auf ein Konto der C.________ AG bei einer Schweizer Bank sowie die spätere Kontoschliessung ohne Verdachtsmeldung an die Meldestelle für Geldwäscherei (MROS). Im Zuge der Untersuchung verfügte die Bundesanwaltschaft die Edition bankinterner Weisungen, Manuals und Checklisten zu den GwG-Abklärungen der Bank sowie der Dokumentation zur Überwachung der Kundenbeziehung. Die Bank verlangte die unverzügliche Siegelung der edierten Unterlagen und berief sich auf Geschäftsgeheimnisse sowie — pauschal — auf mögliche Anwaltskorrespondenz. Die Bundesanwaltschaft wies das Siegelungsbegehren als «offensichtlich ungenügend bzw. ungültig» ab, ohne ein Entsiegelungsverfahren einzuleiten: Die verlangten Unterlagen seien gesetzlich vorgeschriebene GwG-Dokumentation, deren Existenz und Inhalt der Bank naturgemäss bekannt sei; es sei nicht glaubhaft gemacht, dass darunter geschützte Anwaltskorrespondenz falle. Das Bundesgericht bestätigte dieses Vorgehen, stellte aber klar, wem diese Befugnis zusteht:

> «Indessen hat das Bundesgericht in seiner Rechtsprechung wiederholt auf die Möglichkeit hingewiesen, dass die Strafverfolgungsbehörde ein offensichtlich unbegründetes oder missbräuchliches Siegelungsbegehren direkt ablehnen darf beziehungsweise darauf nicht eintreten muss, so namentlich, wenn die gesuchstellende Person offensichtlich nicht legitimiert ist oder das Gesuch offensichtlich verspätet gestellt wird.»
> — [BGer 7B_1154/2024 vom 02.10.2025 E. 2.4.1](https://entscheidsuche.ch/docs/CH_BGer/CH_BGer_007_7B-1154-2024_2025-10-02.html#consideration_2.4.1)

Diese Kompetenz liegt damit bei der **Strafverfolgungsbehörde selbst**, nicht beim Zwangsmassnahmengericht: Kommt sie zum Schluss, ein Siegelungsbegehren sei offensichtlich unbegründet, missbräuchlich oder verspätet, entfällt die Siegelung von vornherein, und es kommt gar nicht erst zu einem Entsiegelungsverfahren nach Art. 248a StPO. Die Bundesanwaltschaft hatte im gleichen Verfahren ergänzend argumentiert, ein Siegelungsbegehren, das bewusst berufsspezifische Anwaltskorrespondenz beifüge, nur um ein Entsiegelungsverfahren auszulösen, sei seinerseits als rechtsmissbräuchlich und ungültig zu behandeln; das Bundesgericht bestätigte die Abweisung des Siegelungsbegehrens im Ergebnis, ohne auf diese zusätzliche Argumentationslinie der Bundesanwaltschaft im Einzelnen einzugehen ([BGer 7B_1154/2024 E. 2.2 und E. 2.5](https://entscheidsuche.ch/docs/CH_BGer/CH_BGer_007_7B-1154-2024_2025-10-02.html)).

> **Leitsatz.** Ein offensichtlich unbegründetes, missbräuchliches oder verspätetes Siegelungsbegehren darf bereits die mit der Sicherstellung befasste Strafverfolgungsbehörde direkt ablehnen; ein Entsiegelungsverfahren nach Art. 248a StPO wird dadurch gar nicht erst ausgelöst.

---

## VI. D — Information und Akteneinsicht Dritter (Abs. 2)

**Rz. 7** Fällt die Inhaberin oder der Inhaber des sichergestellten Datenträgers nicht mit der materiell berechtigten Person zusammen, hat das Entsiegelungsgericht die berechtigte Person nach Eingang des Gesuchs von Amtes wegen über die Siegelung zu informieren (Abs. 2 Satz 1) und ihr auf Verlangen Akteneinsicht zu gewähren (Abs. 2 Satz 2).

**Der Fall des Arzt-Mobiltelefons in einer Kinderpornografie-Untersuchung.** Wie schwierig diese Konstellation werden kann, zeigt ein Verfahren der Staatsanwaltschaft des Kantons Bern gegen unbekannte Täterschaft wegen Verbreitung kinderpornografischen Materials über ein Discord-Benutzerkonto. Die mit dem Konto verknüpfte Telefonnummer war auf A.________ registriert; die Staatsanwaltschaft stellte deshalb Mobiltelefon und USB-Stick am Wohnort von A. sicher, ohne ihn förmlich als beschuldigte Person zu bezeichnen — sie hielt lediglich fest, er könnte der Nutzer des Profils sein. A. verlangte die Siegelung unter Berufung auf Privatgeheimnisse und, weil er als Arzt tätig war, auf das Arztgeheimnis. Auf dem Mobiltelefon befanden sich Aufzeichnungen zu einer sehr grossen Zahl von Patientinnen und Patienten. Das Bundesgericht bestätigte zunächst, dass A. zur Siegelung berechtigt war, obwohl er selbst nicht formell beschuldigt war:

> «Betrachtet man den Beschwerdeführer als beschuldigte Person, bewirkt der angefochtene Entscheid einen nicht wieder gutzumachenden Nachteil im Sinne von Art. 93 Abs. 1 lit. a BGG, zumal sich der Beschwerdeführer unter anderem auf das mit Art. 171 Abs. 1 StPO geschützte Arztgeheimnis beruft, welches dem Schutz des besonders engen Vertrauensverhältnisses zwischen den Patientinnen und Patienten und der Ärztin bzw. dem Arzt dient.»
> — [BGer 7B_558/2025 vom 20.04.2026 E. 1.2](https://entscheidsuche.ch/docs/CH_BGer/CH_BGer_007_7B-558-2025_2026-04-20.html#consideration_1.2)

In der Sache hatte das kantonale Zwangsmassnahmengericht die vollständige Entsiegelung bewilligt und dies unter anderem damit begründet, A. habe seine Substanziierungspflicht bezüglich der Patientendaten nicht hinreichend erfüllt. Das Bundesgericht hiess die Beschwerde teilweise gut. Entscheidend war, dass die Position der betroffenen Patientinnen und Patienten — die weder Partei des Strafverfahrens noch überhaupt in der Lage sind, ihre eigenen Geheimnisinteressen im Entsiegelungsverfahren geltend zu machen — nicht ungeschützt bleiben darf:

> «Zwar sehen Art. 248a Abs. 2 und Abs. 3 StPO vor, dass das Zwangsmassnahmengericht die an den sichergestellten Aufzeichnungen oder Gegenständen berechtigte Person über die Siegelung informiert und ihr Gelegenheit zur Stellungnahme zum Entsiegelungsgesuch gibt, wenn es nach Eingang des Gesuchs feststellt, dass die Inhaberin oder der Inhaber nicht mit der an den Aufzeichnungen oder Gegenständen berechtigten Person identisch ist. Einerseits scheint ein entsprechendes Vorgehen bzw. der Einbezug der betroffenen Patientinnen und Patienten ins Entsiegelungsverfahren vorliegend allerdings nicht praktikabel, weil sich auf dem sichergestellten Mobiltelefon mutmasslich schützenswerte Geheimnisse von sehr vielen verschiedenen Patientinnen und Patienten befinden.»
> — [BGer 7B_558/2025 E. 5.3](https://entscheidsuche.ch/docs/CH_BGer/CH_BGer_007_7B-558-2025_2026-04-20.html#consideration_5.3)

Wo der förmliche Einbezug jedes einzelnen Dritten unpraktikabel ist, tritt an dessen Stelle eine Schutzpflicht des Gerichts von Amtes wegen: Die Patientendaten sind vor der Entsiegelung auszusondern oder zumindest konsequent zu anonymisieren, wobei die Substanziierungspflicht des die Siegelung beantragenden Arztes bezüglich der *fremden* Geheimnisse nicht so streng gehandhabt werden darf, wie wenn ausschliesslich seine eigenen Geheimnisrechte betroffen wären ([BGer 7B_558/2025 E. 5.3](https://entscheidsuche.ch/docs/CH_BGer/CH_BGer_007_7B-558-2025_2026-04-20.html#consideration_5.3)). Bemerkenswert ist, dass die Staatsanwaltschaft dieser Lösung im Grundsatz gar nicht widersprach: Sie hatte selbst beantragt, Patientendaten auszusondern, sofern A. Speicherort und Dateiname glaubhaft angebe — womit der Streit im Ergebnis nur noch die Reihenfolge betraf, nicht das Ob der Aussonderung.

> **Leitsatz.** Ist der förmliche Einbezug jeder einzelnen an sichergestellten Aufzeichnungen berechtigten Drittperson wegen deren grosser Zahl unpraktikabel (typischerweise bei Patientendaten auf einem sichergestellten Gerät), tritt an die Stelle des individuellen Verfahrens nach Abs. 2 eine Schutzpflicht des Gerichts von Amtes wegen: Aussonderung oder konsequente Anonymisierung vor der Entsiegelung, bei abgeschwächter Substanziierungslast der die Siegelung beantragenden Person bezüglich der fremden Geheimnisse.

---

## VII. E — Substanziierung der Geheimnisgründe nach Art. 264 StPO

**Rz. 8** Das Gesetz verlangt in Abs. 3, dass die berechtigte Person «die Gründe» für die Aufrechterhaltung der Siegelung darlegt. Der Massstab dieser Substanziierungslast unterscheidet sich erheblich je nach Art des angerufenen Geheimnisses; die Rechtsprechung hat für die häufigsten Fallgruppen eigenständige Anforderungsprofile entwickelt.

### E.1 Privatgeheimnisse auf Smartphones (Art. 264 Abs. 1 lit. b StPO)

**Der Fall der «Aktfotos und Videos» (Zürich).** Bei A. wurde im Rahmen einer Untersuchung wegen Einfuhr von 7,18 kg Kokaingemisch ein Smartphone sichergestellt. Vor Bundesgericht machte er zur Begründung eines nicht wieder gutzumachenden Nachteils **einzig** geltend, auf dem Gerät befänden sich «dem Persönlichkeitsrecht unterliegende Aktfotos und Videos», die der Entsiegelung entgegenstünden. Das Bundesgericht trat auf die Beschwerde nicht ein:

> «Bei der (vollständigen) Durchsuchung von privat genutzten Smartphones ist davon auszugehen, dass persönliche Aufzeichnungen und Korrespondenz im Sinne von Art. 264 Abs. 1 lit. b StPO tangiert sind.»
> — [BGE 151 IV 344 E. 2.7](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-151-IV-344_2025.html#consideration_2.7)

Diese Vermutung wirkt aber nur als Einstiegsschwelle, nicht als Freibrief: «Diese Eintretensvoraussetzung ist vorliegend nicht erfüllt. Der Beschwerdeführer behauptet einzig unsubstanziiert, die auf dem sichergestellten Smartphone enthaltenen ‹dem Persönlichkeitsrecht unterliegenden Aktfotos und Videos› stünden der Entsiegelung entgegen» ([BGE 151 IV 344 E. 2.8](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-151-IV-344_2025.html#consideration_2.7)). Der blosse pauschale Hinweis auf private Aufnahmen begründet für sich allein keinen nicht wieder gutzumachenden Nachteil; die Partei muss konkret aufzeigen, weshalb ihr Interesse am Schutz der Persönlichkeit das Strafverfolgungsinteresse überwiegen könnte.

**Der Fall der «intimen Kommunikation» (Winterthur) und die dreistufige Verhältnismässigkeitsprüfung.** Denselben Massstab wandte das Bundesgericht wenig später auf einen Beschuldigten an, dem der Handel mit rund 1,2 kg Kokain vorgeworfen wurde und dessen zwei sichergestellte Smartphones nach seiner Darstellung «sexuelle Inhalte in Wort, Schrift, Sprachnachrichten und Bildern» sowie «intime Kommunikation» enthielten. Auch hier verneinte das Bundesgericht einen nicht wieder gutzumachenden Nachteil — diesmal jedoch mit einer ausführlichen dogmatischen Herleitung der Verhältnismässigkeitsprüfung, die zum eigentlichen Leitentscheid zur Reichweite des Privatgeheimnisschutzes wurde:

> «Hierbei kann zwischen drei Konstellationen unterschieden werden: Einerseits kann die Untersuchung Straftaten zum Gegenstand haben, die derart schwer wiegen, dass das öffentliche Interesse an ihrer Aufklärung allfällige Interessen der beschuldigten Person am Schutz ihrer persönlichen Daten grundsätzlich ohne Weiteres überwiegt und die streitigen Privatgeheimnisse folglich vollumfänglich zu entsiegeln sind. Diesen Fällen steht die Kategorie von eigentlichen Bagatellfällen gegenüber, in denen das Interesse der beschuldigten Person am Schutz ihrer persönlichen Daten regelmässig höher zu gewichten ist, so dass sich jede Sicherstellung und Durchsuchung von privaten Mobiltelefonen von vornherein als unangemessen erweist. Bei den dazwischenliegenden Fällen sind im Zuge der Interessenabwägung neben der Schwere des zu untersuchenden Delikts auch die weiteren Umstände, namentlich der aus der Durchsuchung erhoffte Erkenntnisgewinn für die Strafverfolgungsbehörden, zu berücksichtigen. […] Trifft dies nur für einen Teil der zu durchsuchenden Inhalte zu, so ist die Entsiegelung zur Wahrung der Angemessenheit der Zwangsmassnahme in zeitlicher oder sachlicher Hinsicht einzuschränken.»
> — [BGE 151 IV 350 E. 2.5.4](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-151-IV-350_2025.html#consideration_2.5.4)

Im konkreten Fall drohte angesichts der Schwere des Vorwurfs (Verbrechen nach Art. 19 Abs. 2 BetmG) von vornherein keine Offenbarung eines geschützten Geheimnisses, weshalb auch kein nicht wieder gutzumachender Nachteil in Betracht kam ([BGE 151 IV 350 E. 2.5.5](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-151-IV-350_2025.html)).

**Grenzkasuistik: Wo verläuft die Schwelle?**

| Konstellation | Delikt / Schwere | Substanziierung | Ergebnis |
|---|---|---|---|
| [BGE 151 IV 344](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-151-IV-344_2025.html) | Qualifizierte BetmG-Widerhandlung (7,18 kg Kokain) | pauschaler Verweis auf «Aktfotos und Videos» | **kein** nicht wieder gutzumachender Nachteil — unsubstanziiert |
| [BGE 151 IV 350](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-151-IV-350_2025.html) | Verbrechen nach BetmG (1,2 kg Kokain) | «intime Kommunikation» geltend gemacht, aber Delikt in oberster Schwerekategorie | **kein** nicht wieder gutzumachender Nachteil — Schwere überwiegt von vornherein |
| [BGer 7B_558/2025](https://entscheidsuche.ch/docs/CH_BGer/CH_BGer_007_7B-558-2025_2026-04-20.html) (Drittinhaber, Abschnitt VI) | Untersuchung gegen unbekannte Täterschaft, Inhaber nicht beschuldigt | Speicherort und Art der Patientendaten konkret benannt | **teilweise geschützt** — Aussonderung/Anonymisierung angeordnet |

Eine publizierte Konstellation, in der ein *beschuldigter* Halter eines privat genutzten Smartphones bei einem mittelschweren Delikt mit hinreichend substanziierten Angaben eine **zeitliche oder sachliche Einschränkung** durchgesetzt hätte, ist dem Bestand dieses Kommentars nicht zu entnehmen; BGE 151 IV 350 formuliert diese mittlere Kategorie ausdrücklich, ohne dass der zu beurteilende Fall selbst in sie fiel. Die Lücke ist selbst aufschlussreich: Wer als beschuldigte Person eine Einschränkung erreichen will, muss über den blossen Hinweis auf «private» oder «intime» Inhalte hinaus konkret aufzeigen, *welche* Teilmenge welchen Erkenntnisgewinn für die Strafverfolgung realistischerweise nicht erwarten lässt.

> **Leitsatz.** Bei der vollständigen Durchsuchung eines privat genutzten Smartphones ist zwar zu vermuten, dass persönliche Aufzeichnungen und Korrespondenz im Sinne von Art. 264 Abs. 1 lit. b StPO tangiert sind; diese Vermutung allein begründet aber keinen Schutz. Massgebend ist eine dreistufige Verhältnismässigkeitsprüfung: Bei schweren Delikten überwiegt das Strafverfolgungsinteresse regelmässig vollständig, bei Bagatelldelikten das Persönlichkeitsschutzinteresse; bei mittelschweren Delikten ist der konkrete Erkenntnisgewinn abzuwägen und die Entsiegelung nötigenfalls sachlich oder zeitlich einzuschränken.

### E.2 Berufsgeheimnisse — Anwaltskorrespondenz (Art. 264 Abs. 1 lit. a und d StPO)

**Der Fall der Familienanwälte (Bern).** Ein Beschuldigter verlangte die Siegelung von WhatsApp- und E-Mail-Verläufen mit zwei Rechtsanwälten. Die Vorinstanz verweigerte die Siegelung teilweise mit der Begründung, er habe seine Substanziierungspflicht nicht erfüllt, weil er weder E-Mail-Adressen noch Telefonnummern der beiden Anwälte angegeben habe — mit den Namen sei eine Zuordnung nicht «problemlos» möglich. Das Bundesgericht hiess die Beschwerde gut und stellte klar, welcher Massstab tatsächlich gilt:

> «Ruft die siegelungsberechtigte Person Berufsgeheimnisse (wie etwa das Anwalts- oder Arztgeheimnis) an, ohne selbst Träger dieses Berufsgeheimnisses zu sein, hat sie dem Gericht den Namen des Trägers des betreffenden Berufsgeheimnisses […] mitzuteilen. […] Im Zusammenhang mit der Anrufung des Anwaltsgeheimnisses ist es deshalb nach der bundesgerichtlichen Rechtsprechung in der Regel ausreichend, wenn bei elektronischen Datenträgern der Speicherort der geheimnisgeschützten Dateien und die Namen der Anwältinnen und Anwälte bekannt sind. Dadurch ist es mittels Suchfunktion ohne Weiteres möglich, nach der geschützten Anwaltskorrespondenz zu suchen und diese ohne grossen Aufwand beziehungsweise aufwändige Nachforschungen auszusondern.»
> — [BGer 7B_419/2025 vom 08.07.2026 E. 3.3](https://entscheidsuche.ch/docs/CH_BGer/CH_BGer_007_7B-419-2025_2026-07-08.html#consideration_3.3)

Weitergehende Angaben wie E-Mail-Adressen oder Telefonnummern sind nicht erforderlich, weil die Anforderungen an die Substanziierungsobliegenheit angesichts des in Art. 6 StPO verankerten Untersuchungsgrundsatzes nicht zu hoch angesetzt werden dürfen ([BGer 7B_419/2025 E. 3.3](https://entscheidsuche.ch/docs/CH_BGer/CH_BGer_007_7B-419-2025_2026-07-08.html#consideration_3.3)). Anschaulich zeigt der Sachverhalt zugleich, wie eng das Anwaltsgeheimnis persönlich gefasst ist: Der Beschuldigte berief sich unter anderem auf Korrespondenz mit dem Anwalt seines mitbeschuldigten Sohnes, der ihn selbst als «Anwalt erster Stunde» beratend unterstützt hatte, bevor die Mandatsführung an eine andere Rechtsanwältin überging — das Bundesgericht bestätigte, dass ein förmliches Mandatsverhältnis für den Geheimnisschutz nicht Voraussetzung ist, sondern jede Person geschützt ist, die sich an eine Anwältin oder einen Anwalt wendet, selbst wenn kein Mandat zustande kommt (vgl. zu diesem Grundsatz auch [BGer 7B_558/2025 E. 3.4](https://entscheidsuche.ch/docs/CH_BGer/CH_BGer_007_7B-558-2025_2026-04-20.html)).

**Gegenbeispiel: Wann die Substanziierung scheitert (Mosambik-Bankfall).** Im bereits geschilderten Editionsverfahren gegen eine Bank (Abschnitt V) berief sich diese hilfsweise auch auf das Anwaltsgeheimnis: Es sei nicht auszuschliessen, dass sich unter den edierten GwG-Unterlagen Anwaltskorrespondenz befinde. Das Bundesgericht verwarf dies, weil die Bank die verlangten Unterlagen selbst zusammengestellt und daher genaue Kenntnis ihres Inhalts hatte, ihr eineinhalb Monate Zeit für eine Angabe zur Verfügung standen und die Editionsverfügung ihrem Wortlaut nach ohnehin nur gesetzlich vorgeschriebene Compliance-Dokumentation erfasste: «Es sei unter den konkreten Umständen nicht glaubhaft gemacht worden, dass sich unter den eingereichten Unterlagen Informationen befinden könnten, die vom Anwaltsgeheimnis geschützt seien» ([BGer 7B_1154/2024 E. 2.2](https://entscheidsuche.ch/docs/CH_BGer/CH_BGer_007_7B-1154-2024_2025-10-02.html)).

**Grenzkasuistik: Namensnennung genügt — pauschale Behauptung nicht.**

| Sachverhalt | Substanziierung | Ergebnis |
|---|---|---|
| [BGer 7B_419/2025](https://entscheidsuche.ch/docs/CH_BGer/CH_BGer_007_7B-419-2025_2026-07-08.html) — WhatsApp-/E-Mail-Verlauf mit zwei namentlich benannten Anwälten | Namen der Anwälte + Art der Kommunikation angegeben | **genügt** — Aussonderung anhand des Namens möglich |
| [BGer 7B_1154/2024](https://entscheidsuche.ch/docs/CH_BGer/CH_BGer_007_7B-1154-2024_2025-10-02.html) — GwG-Compliance-Dokumentation einer Bank | pauschale Vermutung, es «könnte» Anwaltskorrespondenz enthalten sein, ohne jede Konkretisierung, obschon die Bank die Unterlagen selbst zusammengestellt hatte | **genügt nicht** — nicht glaubhaft gemacht |

> **Leitsatz.** Zur Substanziierung des Anwaltsgeheimnisses bei elektronischen Datenträgern genügt die Angabe des Namens der Anwältin oder des Anwalts sowie des Speicherorts der betroffenen Dateien; Kontaktdaten wie E-Mail-Adressen oder Telefonnummern sind nicht erforderlich. Wer die fraglichen Unterlagen selbst zusammengestellt hat und dennoch nur pauschal auf eine mögliche Anwaltskorrespondenz verweist, genügt der Substanziierungslast dagegen nicht.

### E.3 Geschäfts- und Bankkundengeheimnisse: kein eigenständiger Grund mehr

**Rz. 9** Wie bereits in Abschnitt I dargelegt, hat der Gesetzgeber die im Entsiegelungsverfahren zulässigen Geheimnisgründe seit dem 1. Januar 2024 abschliessend auf den Katalog von Art. 264 StPO beschränkt. Im bereits geschilderten Mosambik-Bankfall bestätigte das Bundesgericht dies für Geschäftsgeheimnisse ([BGer 7B_1154/2024 E. 2.4.3](https://entscheidsuche.ch/docs/CH_BGer/CH_BGer_007_7B-1154-2024_2025-10-02.html#consideration_2.4.3)); in einem separaten Verfahren erging die Grundsatzentscheidung für das Bankkundengeheimnis. Eine A. AG hatte gegen zwei Editionsverfügungen zulasten ihrer Bankbeziehungen die sofortige Siegelung verlangt und sich auf ihre Geschäftsgeheimnisse berufen. Das Bundesgericht verwarf dies unter Hinweis auf die Gesetzesmaterialien:

> «Der Bundesrat hatte in seiner Botschaft samt Entwurf noch vorgeschlagen, dass es Betroffenen ermöglicht werden sollte, auch ‹Fabrikations- und Geschäftsgeheimnisse› als Entsiegelungshindernis anzurufen und glaubhaft zu machen. Der Nationalrat ist diesem Vorschlag jedoch nicht gefolgt. […] Geschäftsgeheimnisse bzw. ‹Geschäftsschutzinteressen› fallen nicht darunter, das Bankkundengeheimnis […] ebenfalls nicht.»
> — [BGE 151 IV 30 E. 2.4.1–2.4.2](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-151-IV-30_2025.html#consideration_2.4.2)

Wer sich auf ein in Art. 264 StPO nicht genanntes Geheimnisinteresse berufen will, ist damit nicht rechtlos gestellt — der Rechtsweg führt aber nicht über das Entsiegelungsverfahren, sondern über ein begründetes Gesuch um Einschränkung des Akteneinsichtsrechts an die Verfahrensleitung nach Art. 108 Abs. 1 lit. b StPO ([BGE 151 IV 30 E. 2.4.3](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-151-IV-30_2025.html#consideration_2.4.2)).

---

## VIII. F — Akzessorische Rügen (Art. 197 StPO)

**Rz. 10** Werden formelle Siegelungsgründe nach Art. 248 Abs. 1 i.V.m. Art. 264 Abs. 1 StPO geltend gemacht, muss das Entsiegelungsgericht auch sogenannte akzessorische Rügen prüfen — insbesondere das Vorliegen eines hinreichenden Tatverdachts und die allgemeine Verhältnismässigkeit der Beweiserhebung gemäss Art. 197 StPO.

**Der Fall der durchsuchten iPhones im Haus der Ex-Ehefrau (Genf).** Die Genfer Staatsanwaltschaft führte gegen A. eine Strafuntersuchung wegen Förderung der Prostitution (Art. 195 StGB) und eines Verbrechens nach Betäubungsmittelgesetz. Am 8. Juli 2024 wurde nicht etwa die Wohnung von A. selbst, sondern diejenige seiner **Ex-Ehefrau und der gemeinsamen Tochter** durchsucht; dabei wurden zwei iPhones sichergestellt, die A. gehörten. A. verlangte die Siegelung und berief sich auf zwei Geheimnisgründe: das Anwaltsgeheimnis (Art. 264 Abs. 1 lit. a und c StPO) sowie den Schutz persönlicher Aufzeichnungen und Korrespondenz (Art. 264 Abs. 1 lit. b StPO) — unter anderem, weil sich auf den Geräten auch Geschäftskorrespondenz zu seinem eigenen Unternehmen befand. Das Zwangsmassnahmengericht (TMC) hob die Siegelung auf, ohne auf die zusätzlich erhobenen Rügen der fehlenden Verhältnismässigkeit und Beweisrelevanz einzugehen; die kantonale Beschwerdeinstanz hatte einen darauf gerichteten Rekurs zudem für unzulässig erklärt. Das Bundesgericht hiess die Beschwerde in diesem Punkt gut:

> «Werden Siegelungsgründe gemäss Art. 248 Abs. 1 und Art. 264 Abs. 1 lit. a-d StPO angeführt um die Siegelung zu verlangen, muss das für die Entsiegelung zuständige Gericht auch sogenannte akzessorische Rügen prüfen (vgl. insbesondere Art. 197 StPO). Dies gilt auch dann, wenn das Entsiegelungsgericht die angeführten Siegelungsgründe nach Art. 264 StPO nicht schützt, etwa weil der Inhaber oder Berechtigte seiner Mitwirkungs- und Substanziierungsobliegenheit nicht nachgekommen ist.»
> — [BGE 151 IV 175, Regeste b](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-151-IV-175_2025.html)

In der Sache scheiterte A. zwar mit dem Anwaltsgeheimnis: Die Angabe eines Vornamens und des generischen Begriffs «Anwalt» genügte nicht, um ein geschütztes Mandatsverhältnis darzutun. Entscheidend war aber, dass er sich **zusätzlich** auf den Schutz persönlicher Aufzeichnungen berufen hatte — und dieser zweite Grund den vorliegenden Fall von einem zuvor entschiedenen Bankgeheimnisfall unterschied, in dem nur ein einziger, unzulässiger Geheimnisgrund geltend gemacht worden war (dazu sogleich Abschnitt E.3):

> «Le TMC a donc été saisi en raison d'au moins deux motifs relevant des art. 248 al. 1 et 264 al. 1 let. a, b et c CPP et on ne se trouve ainsi pas dans la configuration qui prévalait dans l'ATF 151 IV 30 où seul le secret des affaires avait été soulevé pour obtenir les scellés. Vu le secret professionnel de l'avocat et l'atteinte à la sphère privée invoqués dans le présent cas, le TMC était par conséquent tenu de procéder à l'examen des griefs dits accessoires en lien avec la perquisition du 8 juillet 2024. Le fait que le TMC ait écarté sur le fond […] les secrets invoqués, notamment en raison d'un défaut de collaboration et de motivation, n'y change rien.»
> — [BGE 151 IV 175 E. 3.4](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-151-IV-175_2025.html#consideration_3.4)

**Die Kehrseite: keine akzessorische Prüfung ohne jeden Geheimnisgrund.** Der bereits geschilderte Bankunterlagenfall (BGE 151 IV 30) markiert die Gegenprobe: Weil die dortige Beschwerdeführerin **keinen** gesetzlichen Geheimnisgrund nach Art. 264 StPO substanziiert angerufen hatte — sie beschränkte sich auf das (unzulässige) Geschäftsgeheimnis —, war das Zwangsmassnahmengericht auch nicht gehalten, ihre Rüge des fehlenden Tatverdachts akzessorisch zu prüfen:

> «Falls keine der Durchsuchung unterliegenden Beweismittel erhoben wurden oder von den Betroffenen keine gesetzlichen Geheimnisschutzgründe als Zwangsmassnahmenhindernis angerufen werden, sind entsprechende Rügen daher nicht vom Entsiegelungsrichter zu prüfen, sondern in einem StPO-Beschwerdeverfahren vorzutragen.»
> — [BGE 151 IV 30 E. 4.3](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-151-IV-30_2025.html)

**Grenzkasuistik: akzessorische Prüfpflicht nur bei zulässigem Geheimnisgrund.**

| Fall | Geltend gemachte Geheimnisgründe | Akzessorische Prüfung durch das ZMG |
|---|---|---|
| [BGE 151 IV 175](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-151-IV-175_2025.html) | Anwaltsgeheimnis **und** Schutz persönlicher Aufzeichnungen (Art. 264 Abs. 1 lit. a/c **und** lit. b StPO angerufen) | **ja** — Prüfpflicht besteht, auch wenn die Geheimnisgründe letztlich verworfen werden |
| [BGE 151 IV 30](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-151-IV-30_2025.html) | ausschliesslich Geschäfts-/Bankkundengeheimnis (seit 2024 kein Art.-264-Grund) | **nein** — kein zulässiger Geheimnisgrund angerufen, Verweis auf StPO-Beschwerdeverfahren |

> **Leitsatz.** Die Pflicht des Entsiegelungsgerichts zur Prüfung akzessorischer Rügen nach Art. 197 StPO setzt voraus, dass überhaupt ein gesetzlicher Geheimnisgrund nach Art. 264 StPO angerufen wird; sie besteht dann aber auch, wenn dieser Geheimnisgrund in der Sache verworfen wird. Wird demgegenüber gar kein Art.-264-Grund geltend gemacht, bleibt der Rechtsweg für Tatverdachts- und Verhältnismässigkeitsrügen auf das gesonderte StPO-Beschwerdeverfahren beschränkt.

---

## IX. G — Fristwahrung und Rückzugsfiktion (Abs. 3)

**Rz. 11** Das Gericht setzt der berechtigten Person eine nicht erstreckbare Frist von 10 Tagen an, um Einwände gegen das Entsiegelungsgesuch vorzubringen und darzulegen, in welchem Umfang die Siegelung aufrechterhalten werden soll. Bei dieser 10-Tage-Frist handelt es sich um eine gesetzliche Verwirkungsfrist: Bleibt die berechtigte Person untätig, gilt dies gemäss Abs. 3 Satz 2 als Rückzug des Siegelungsbegehrens — eine Rechtsfolge, die unmittelbar aus dem Gesetzeswortlaut folgt und keiner zusätzlichen richterlichen Wertung bedarf.

---

## X. H — Schriftlicher Endentscheid bei Spruchreife (Abs. 4)

**Rz. 12** Liegen die Voraussetzungen für einen Entscheid ohne weitere Beweiserhebungen vor (Spruchreife), entscheidet das Gericht innert 10 Tagen nach Eingang der Stellungnahme im schriftlichen Verfahren endgültig. Dieser Entscheid ist — wie in Abschnitt III dargelegt — kantonal letztinstanzlich; einzig die Beschwerde in Strafsachen ans Bundesgericht steht offen (dazu vertieft Abschnitt XIII).

---

## XI. I — Triageverhandlung und Akteneinsicht (Abs. 5)

**Rz. 13** Ist die Sache nicht spruchreif, setzt das Entsiegelungsgericht innert 30 Tagen seit Eingang der Stellungnahme eine nicht öffentliche Verhandlung mit der Staatsanwaltschaft und der berechtigten Person an. In dieser Triageverhandlung hat die berechtigte Person glaubhaft zu machen, weshalb und in welchem Umfang bestimmte Aufzeichnungen dem Geheimnisschutz unterliegen.

**Der Fall der 54 Millionen Objekte (I.________ Funds).** Wie voraussetzungsvoll diese Glaubhaftmachung bei sehr grossen Datenmengen sein kann, zeigt ein Verfahren wegen mutmasslichen Betrugs und UWG-Widerhandlungen im Zusammenhang mit den kollabierten I.________ Funds. Bei Hausdurchsuchungen in den Büros der damaligen G.________ AG sowie bei mehreren (ehemaligen) Mitarbeitenden wurden umfangreiche Datenträger sichergestellt und gesiegelt; das Zwangsmassnahmengericht Zürich gab in der Folge «54'001'334 Objekte auf Stufe Top-Level» zur Durchsuchung frei. Mehrere Betroffene rügten vor Bundesgericht eine Verletzung ihres Gehörsanspruchs, weil ihnen keine vorgängige Einsicht in die sichergestellten elektronischen Daten gewährt worden sei — ohne diese Einsicht könnten sie ihre Geheimnisinteressen gar nicht sachgerecht benennen. Das Bundesgericht hielt zunächst am strengen Grundsatz fest, dass ein solches Akteneinsichtsrecht nur zurückhaltend zu gewähren ist, weil die Inhaberin regelmässig bereits weiss, was der Inhalt ihrer eigenen Aufzeichnungen ist:

> «Nur wenn die betroffene Person nachvollziehbar begründet, weshalb sie ohne nachträgliche Gesamtdurchsicht der Aufzeichnungen und Gegenstände überhaupt nicht in der Lage wäre, ihre mit Anfangshinweisen bereits plausibel gemachten Geheimnisinteressen ausreichend zu substanziieren, kann sich eine solche umfassende ‹Akteneinsicht› von Bundesrechts wegen ausnahmsweise als geboten erweisen.»
> — [BGer 7B_486/2024 vom 09.07.2026 E. 4.4](https://entscheidsuche.ch/docs/CH_BGer/CH_BGer_007_7B-486-2024_2026-07-09.html#consideration_4.4)

Im konkreten Fall bejahte das Bundesgericht diese Ausnahme für eine der beschwerdeführenden Gesellschaften: Ein erheblicher Teil der freigegebenen Daten stammte von Arbeitslaptops ehemaliger Mitarbeitender, auf die sie **keinen eigenen Zugriff mehr** hatte — mit diesem entscheidwesentlichen Umstand hatte sich die Vorinstanz nicht auseinandergesetzt und dadurch den Gehörsanspruch nach Art. 29 Abs. 2 BV verletzt ([BGer 7B_486/2024 E. 4.4](https://entscheidsuche.ch/docs/CH_BGer/CH_BGer_007_7B-486-2024_2026-07-09.html)). Für zwei andere Beschwerdeführer, die eine vergleichbare Unmöglichkeit nicht dargetan hatten, blieb es dagegen bei der grundsätzlichen Zurückhaltung.

> **Leitsatz.** Auf Akteneinsicht in die eigenen sichergestellten Daten zum Zweck der Substanziierung besteht nur ausnahmsweise ein Anspruch — nämlich wenn die berechtigte Person nachvollziehbar begründet, weshalb sie ohne eine solche Einsicht ihre bereits plausibel gemachten Geheimnisinteressen nicht ausreichend konkretisieren könnte. Das gilt insbesondere, wenn sie auf Daten Dritter (etwa ehemaliger Mitarbeitender) keinen eigenen Zugriff mehr hat.

**Praktischer Hinweis zur publizierten Kasuistik zur mündlichen Verhandlung selbst.** Zur konkreten Durchführung der mündlichen Triageverhandlung nach Abs. 5 — etwa zu Fragen der Verhandlungsleitung, des Replikrechts der Parteien oder der Protokollierung — liefert der ausgewertete Bestand keine eigenständige, über die allgemeinen verfahrensrechtlichen Garantien hinausgehende Kasuistik; die publizierte Rechtsprechung konzentriert sich auf die vor- und nachgelagerten Fragen der Substanziierung und Akteneinsicht. Diese Lücke ist selbst ein Hinweis: Ein prozessualer Streitpunkt mit eigenem Aussagewert scheint sich hier bislang nicht herausgebildet zu haben.

---

## XII. J — Sachverständigenbeizug und Polizeiforensik (Abs. 6)

**Rz. 14** Das Gericht kann eine sachverständige Person beiziehen, um den Inhalt der Aufzeichnungen zu prüfen, den technischen Zugang zu erhalten oder die Integrität der Daten zu wahren (Abs. 6 lit. a). Hierzu können auch Angehörige der Polizei als sachverständige Personen bezeichnet werden (Abs. 6 lit. b). Diese Befugnis steht unter zwei Bedingungen, die beide Gegenstand einschlägiger Rechtsprechung geworden sind: Es muss sich um eine **natürliche Person** handeln, und diese Person muss organisatorisch und funktionell von der eigentlichen Ermittlungstätigkeit getrennt bleiben.

### J.1 Die Datenspiegelung vor der Siegelung: ein Rechtsprechungswandel

**Ausgangslage: das strenge Verbot (Zürcher Flughafen).** Nach der ursprünglichen Rechtsprechung war es den Strafverfolgungsbehörden untersagt, im Zusammenhang mit der Sicherstellung elektronischer Datenträger selbst die Erstellung einer Datenkopie («Spiegelung») anzuordnen, bevor das Zwangsmassnahmengericht darüber entschieden hatte. Grundlage dieser strengen Linie war ein Verwaltungsstrafverfahren: Bei einer Zollkontrolle am Flughafen Zürich waren bei A. zwölf nicht deklarierte Rolex-Armbanduhren sichergestellt worden, zehn davon in einem am Bauch getragenen Schmuggelgurt versteckt. Die Zollverwaltung liess die sichergestellten elektronischen Geräte noch vor der förmlichen Siegelung durch eine von ihr beauftragte Behörde entsperren und spiegeln. Das Bundesgericht erklärte dieses Vorgehen für unzulässig und ordnete die **Vernichtung der gewonnenen Daten** sowie die Rückgabe der Geräte an:

> «Die Vornahme der Entsperrung der Geräte und der Datenspiegelung vor der Siegelung durch eine von der Untersuchungsbehörde beauftragte Behörde stellt einen erheblichen Verfahrensmangel dar, der zur Unverwertbarkeit der Daten und deren Vernichtung sowie zur Rückgabe der Geräte an die daran berechtigte Person führt.»
> — [BGE 148 IV 221, Regeste](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-148-IV-221_2022.html)

**Die Praxisänderung: Datenspiegelung durch die Jugendanwaltschaft Winterthur.** Rund vier Jahre später revidierte das Bundesgericht diese Praxis ausdrücklich. Im Rahmen einer Untersuchung der Jugendanwaltschaft Winterthur wegen Widerhandlung gegen das Waffengesetz wurden bei A. (einem Minderjährigen) an einem Sonntag zwei Mobiltelefone sichergestellt; die Siegelung wurde erst am Folgetag verlangt. Weil sich moderne Mobiltelefone bei Netzverbindung automatisch zurücksetzen können und der Zeitpunkt eines drohenden Datenverlusts oft nicht abwartbar ist, ordnete die Jugendanwaltschaft eine sofortige Datenspiegelung durch eine sachverständige Person an. Das Bundesgericht würdigte den technischen Fortschritt seit BGE 148 IV 221 und erkannte auf eine ausdrückliche Praxisänderung:

> «Eine Analyse der per 1. Januar 2024 in Kraft getretenen revidierten Bestimmungen des Siegelungsverfahrens, der kritischen Lehrmeinungen, des technischen Prozesses des Datenspiegelungsvorgangs sowie des technischen Fortschritts bei der Datensicherung führt zum Ergebnis, dass es den Strafverfolgungsbehörden möglich sein muss, in Fällen eines unmittelbar drohenden Beweisverlusts selber eine Datenspiegelung durch eine sachverständige Person anzuordnen (Änderung der Rechtsprechung).»
> — [BGE 152 IV 107 E. 5.7](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-152-IV-107_2026.html)

Die neue Erlaubnis steht aber unter derselben Bedingung wie zuvor die alte Prohibition: Die für die Datenspiegelung eingesetzte sachverständige Person darf nicht in die eigentliche Ermittlungstätigkeit eingebunden werden ([BGE 152 IV 107 E. 5.7.8](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-152-IV-107_2026.html#consideration_5.7.8)). Die rein technische Datenextraktion ohne bildgebende Sichtung des Inhalts gilt dabei nicht als unzulässiges «Sichten oder Verwenden» im Sinne von Art. 248 Abs. 1 StPO ([BGE 152 IV 107 E. 5.7.6](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-152-IV-107_2026.html)).

**Rechtsprechungswandel, keine Judikaturdivergenz.** Anders als bei einem echten, unaufgelösten Widerspruch zwischen Gerichten oder Kammern handelt es sich hier um eine vom Bundesgericht selbst offengelegte, ausdrückliche Änderung seiner eigenen Praxis. Für die Beratung bedeutet das: BGE 148 IV 221 ist für die Vergangenheit (Verfahren unter altem Recht bzw. vor dem 23. Januar 2026) einschlägig geblieben; für seither angeordnete Datenspiegelungen gilt die gelockerte Linie von BGE 152 IV 107, sofern die Funktionentrennung eingehalten wird.

| | [BGE 148 IV 221](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-148-IV-221_2022.html) (2022, Zollverfahren) | [BGE 152 IV 107](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-152-IV-107_2026.html) (2026, Jugendstrafverfahren) |
|---|---|---|
| Anlass | 12 unverzollte Rolex-Uhren, Schmuggelgurt | Waffengesetz-Verdacht, Minderjähriger |
| Datenspiegelung angeordnet durch | Untersuchungsbehörde selbst (vor Siegelung) | Jugendanwaltschaft (bei drohendem Beweisverlust) |
| Ergebnis | Verfahrensmangel — Daten unverwertbar, zu vernichten | zulässig, sofern sachverständige Person ermittlungsfremd bleibt |

> **Leitsatz.** Eine durch die Strafverfolgungsbehörden bei konkret drohendem Beweisverlust vorsorglich angeordnete Datenspiegelung verletzt kein Bundesrecht, sofern sie durch eine sachverständige Person erfolgt, die nicht in die eigentliche Ermittlungstätigkeit eingebunden ist (Änderung der in BGE 148 IV 221 begründeten Praxis).

### J.2 Natürliche Person statt Behörde — und keine Vermengung von Entsiegelung und Triage

**Der Fall des Kompetenzzentrums Digitale Forensik (Uri).** In einer Untersuchung wegen Pfändungsbetrugs stellte die Staatsanwaltschaft des Kantons Uri ein Smartphone und ein Tablet sicher. A. verlangte die Siegelung und machte im Entsiegelungsverfahren glaubhaft, mit zwei namentlich genannten Rechtsanwälten korrespondiert zu haben. Das Zwangsmassnahmengericht Uri hiess das Entsiegelungsgesuch «unter Vorbehalt von Ziffer 1.2» gut und ordnete die Entsiegelung an; zugleich beauftragte es das **Kompetenzzentrum Digitale Forensik der Zuger Polizei** — dieselbe Stelle, die die Geräte bereits entsperrt und gespiegelt hatte —, die Anwaltskorrespondenz auszusondern. A. rügte vor Bundesgericht sowohl die fehlende Unabhängigkeit dieser Stelle als auch die Vermengung von Entsiegelungsentscheid und noch ausstehender Triage. Das Bundesgericht hiess die Beschwerde **gut**:

> «Dem Beschwerdeführer ist zuzustimmen, dass der angefochtene Entscheid Bundesrecht verletzt: Mit der Verfügung vom 23. Januar 2026 heisst die Vorinstanz das Entsiegelungsgesuch teilweise gut, obschon sie die angeblich auf den gesiegelten Geräten vorhandene Anwaltskorrespondenz noch gar nicht aussortiert hat und zu diesem Zweck im gleichen Entscheid prozessleitende Verfügungen trifft. […] Die Entsiegelung darf nicht angeordnet werden, bevor die gesiegelten Aufzeichnungen und Gegenständen vom Gericht im Einzelnen — soweit nötig — geprüft und triagiert wurden.»
> — [BGer 7B_245/2026 vom 16.06.2026 E. 4.3](https://entscheidsuche.ch/docs/CH_BGer/CH_BGer_007_7B-245-2026_2026-06-16.html#consideration_4.3)

Zusätzlich beanstandete das Bundesgericht die Bezeichnung einer ganzen Organisationseinheit als sachverständige Person:

> «In der Tat widerspricht Dispositiv-Ziffer 1.2 des angefochtenen Entscheids den bundesrechtlichen Vorgaben. […] Auf den Beizug der sachverständigen Person im Entsiegelungsverfahren ist gemäss der Rechtsprechung Art. 183 StPO anwendbar. […] Die Vorinstanz wäre folglich gehalten gewesen, eine natürliche Person als Sachverständige zu bestimmen.»
> — [BGer 7B_245/2026 E. 5.2](https://entscheidsuche.ch/docs/CH_BGer/CH_BGer_007_7B-245-2026_2026-06-16.html#consideration_5.2)

Diese Anforderung ist keine blosse Formalität: Art. 183 StPO unterstellt Sachverständige den Ausstandsgründen. Wer als sachverständige Person amtet, muss namentlich feststehen, damit Befangenheit und Unabhängigkeit überhaupt geprüft werden können — eine anonyme «Fachstelle» der Polizei entzieht sich dieser Prüfung strukturell, selbst wenn die dort tätigen Personen im Einzelfall unabhängig arbeiten.

> **Leitsatz.** Das Entsiegelungsgericht muss für den Beizug einer sachverständigen Person nach Art. 248a Abs. 6 StPO stets eine natürliche Person bestimmen, nicht eine Behörde oder Organisationseinheit als solche; die Bestellung unterliegt den Ausstandsregeln von Art. 183 StPO. Die Entsiegelung darf zudem nicht angeordnet werden, solange die für den Geheimnisschutz massgebliche Triage der sichergestellten Daten noch nicht abgeschlossen ist.

---

## XIII. K — Säumnisfolgen an der Verhandlung (Abs. 7)

**Rz. 15** Bleibt die berechtigte Person der Verhandlung unentschuldigt fern und lässt sie sich auch nicht vertreten, gilt das Siegelungsbegehren als zurückgezogen (Abs. 7 Satz 1) — eine systematische Parallele zur Rückzugsfiktion bei Fristversäumnis nach Abs. 3. Erscheint die Staatsanwaltschaft nicht, entscheidet das Gericht in deren Abwesenheit (Abs. 7 Satz 2); die Verhandlung wird durch das Fernbleiben der Behörde also nicht blockiert. Zur konkreten Anwendung dieser Säumnisregeln — etwa zu den Anforderungen an eine genügende Entschuldigung oder an die «Vertretung» im Sinne von Abs. 7 Satz 1 — findet sich im ausgewerteten Bestand **keine publizierte bundesgerichtliche oder kantonale Rechtsprechung**. Das ist bei einer erst seit 2024 geltenden Norm nicht überraschend, sollte bei der Beratung aber offen benannt werden, statt eine Praxis zu unterstellen, die (noch) nicht besteht.

---

## XIV. L — Rechtsmittel: Endgültigkeit und nicht wieder gutzumachender Nachteil

**Rz. 16** Der Entscheid des Entsiegelungsgerichts ist kantonal letztinstanzlich («endgültig» im Sinne von Abs. 4 und Abs. 5 Satz 3; Art. 380 StPO; vgl. zur Zuständigkeit Abschnitt III mit [BGer 7B_1170/2025 vom 03.03.2026](https://entscheidsuche.ch/docs/CH_BGer/CH_BGer_007_7B-1170-2025_2026-03-03.html)). Gegen den Entsiegelungsentscheid steht die Beschwerde in Strafsachen an das Bundesgericht nach Massgabe von Art. 78 ff. BGG offen. Da es sich um einen Zwischenentscheid handelt, setzt das Eintreten grundsätzlich das Vorliegen eines nicht wieder gutzumachenden Nachteils gemäss Art. 93 Abs. 1 lit. a BGG voraus.

**Wann der Nachteil zu bejahen ist.** Wird im Entsiegelungsverfahren ausreichend substanziiert geltend gemacht, dass geschützte Geheimhaltungsrechte der Entsiegelung entgegenstehen, droht nach ständiger Praxis ein nicht wieder gutzumachender Nachteil, weil die einmal erfolgte Offenbarung eines Geheimnisses nicht mehr rückgängig gemacht werden kann ([BGer 7B_428/2024 vom 06.11.2024 E. 1.2.2](https://entscheidsuche.ch/docs/CH_BGer/CH_BGer_007_7B-428-2024_2024-11-06.html#consideration_1.2)). Dieselbe Erwägung trägt auch die Beschwerdelegitimation eines nicht formell beschuldigten Dritten, der sich auf ein Berufsgeheimnis beruft (Abschnitt VI mit [BGer 7B_558/2025 E. 1.2](https://entscheidsuche.ch/docs/CH_BGer/CH_BGer_007_7B-558-2025_2026-04-20.html#consideration_1.2)).

**Wann er zu verneinen ist.** Werden dagegen nur andere Beschlagnahmehindernisse wie ein angeblich fehlender hinreichender Tatverdacht geltend gemacht, fehlt es grundsätzlich am nicht wieder gutzumachenden Nachteil ([BGer 7B_428/2024 E. 1.2.2](https://entscheidsuche.ch/docs/CH_BGer/CH_BGer_007_7B-428-2024_2024-11-06.html)). Im konkreten Fall hatte die anwaltlich vertretene Beschwerdeführerin überhaupt kein Geheimnisrecht nach Art. 264 StPO substanziiert vorgebracht; das Bundesgericht trat auf ihre Beschwerde nicht ein ([BGer 7B_428/2024 E. 2](https://entscheidsuche.ch/docs/CH_BGer/CH_BGer_007_7B-428-2024_2024-11-06.html)). Ebenso wenig genügt es, sich auf eine angebliche Verletzung der «Modalitäten des Entsiegelungsverfahrens» zu berufen, ohne dies mit einem materiellen Geheimnisinteresse zu verbinden ([BGer 7B_1312/2025 vom 29.04.2026 E. 2.6](https://entscheidsuche.ch/docs/CH_BGer/CH_BGer_007_7B-1312-2025_2026-04-29.html)); im dortigen Fall hatte ein wegen Betäubungsmitteldelikten Beschuldigter unter anderem gerügt, ihm sei kein Replikrecht gewährt worden — diese isolierte Gehörsrüge führte zwar zum Eintreten, in der Sache aber nicht zum Erfolg, weil ein Verfahrensfehler nicht ersichtlich war ([BGer 7B_1312/2025 E. 3.3](https://entscheidsuche.ch/docs/CH_BGer/CH_BGer_007_7B-1312-2025_2026-04-29.html)).

> **Leitsatz.** Ein nicht wieder gutzumachender Nachteil im Sinne von Art. 93 Abs. 1 lit. a BGG droht, wenn im Entsiegelungsverfahren ausreichend substanziiert geltend gemacht wird, dass geschützte Geheimhaltungsrechte entgegenstehen — unabhängig davon, ob die beschwerdeführende Person formell beschuldigt ist. Werden demgegenüber nur andere Beschlagnahmehindernisse oder isolierte Verfahrensmängel ohne Bezug zu einem Geheimnisinteresse gerügt, fehlt es regelmässig an dieser Eintretensvoraussetzung.

---

## XV. Kantonale Praxisfragen

**Rz. 17 — Designation kantonaler Forensikdienste bei grossen Datenmengen.** In der kantonalen Gerichtspraxis stellt sich regelmässig die Frage, wie Zwangsmassnahmengerichte bei der Entsiegelung terabyteweiter Smartphone- und Serverdaten vorgehen sollen. Der Urner Fall (Abschnitt XII.2) zeigt eine verbreitete Versuchung: den Beizug eines etablierten kantonalen oder interkantonalen Kompetenzzentrums (hier: der Zuger Polizei) als «die» sachverständige Stelle, ohne eine natürliche Person zu benennen. Nach der bundesgerichtlichen Klarstellung in [BGer 7B_245/2026 E. 5.2](https://entscheidsuche.ch/docs/CH_BGer/CH_BGer_007_7B-245-2026_2026-06-16.html#consideration_5.2) muss die Verfügung, mit der ein solches Kompetenzzentrum beigezogen wird, zwingend eine namentlich bestimmte Person als Sachverständige bezeichnen, gegen die auch Ausstandsgründe nach Art. 183 StPO geprüft werden können.

**Rz. 18 — Reihenfolge von Triage und Entsiegelung.** Derselbe Fall verdeutlicht eine zweite Fehlerquelle: Die Entsiegelung darf nicht in einer Verfügung angeordnet werden, die gleichzeitig noch offene, prozessleitende Anordnungen zur Aussonderung geheimnisgeschützter Inhalte trifft. Die Triage muss abgeschlossen sein, *bevor* die Entsiegelung ausgesprochen wird — nicht als nachgelagerter, mit derselben Verfügung delegierter Schritt.

---

## XVI. Praxishinweise

**Für die berechtigte Person (Siegelungsantragstellerin) und ihre Vertretung:**

1. Bei Anwaltskorrespondenz die Namen der beteiligten Anwältinnen und Anwälte sowie den Speicherort der betroffenen Dateien angeben; weitergehende Angaben wie E-Mail-Adressen oder Telefonnummern sind nicht erforderlich ([BGer 7B_419/2025 E. 3.3](https://entscheidsuche.ch/docs/CH_BGer/CH_BGer_007_7B-419-2025_2026-07-08.html#consideration_3.3)).
2. Bei Privatgeheimnissen auf Smartphones den blossen Hinweis auf «private» oder «intime» Inhalte vermeiden; stattdessen konkret darlegen, welche Teilmenge der Daten keinen Erkenntnisgewinn für die Strafverfolgung erwarten lässt, und so auf eine sachliche oder zeitliche Einschränkung hinwirken ([BGE 151 IV 350 E. 2.5.4](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-151-IV-350_2025.html#consideration_2.5.4)).
3. Die nicht erstreckbare 10-Tage-Frist nach Abs. 3 ab Zustellung im Kalender mit Vorlauf erfassen; ein Fristversäumnis wird unwiderleglich als Rückzug des Siegelungsbegehrens gewertet.
4. Akteneinsicht in die eigenen sichergestellten Daten nur beantragen, wenn konkret begründet werden kann, weshalb ohne diese Einsicht keine sachgerechte Substanziierung möglich ist — insbesondere bei fehlendem eigenem Zugriff auf Daten Dritter (z.B. ehemaliger Mitarbeitender) ([BGer 7B_486/2024 E. 4.4](https://entscheidsuche.ch/docs/CH_BGer/CH_BGer_007_7B-486-2024_2026-07-09.html#consideration_4.4)).
5. Wird ein Kompetenzzentrum ohne Namensnennung einer natürlichen Person als sachverständige Person bezeichnet, ist dies umgehend zu rügen ([BGer 7B_245/2026 E. 5.2](https://entscheidsuche.ch/docs/CH_BGer/CH_BGer_007_7B-245-2026_2026-06-16.html#consideration_5.2)).

**Für Drittinhaberinnen und -inhaber von Berufsgeheimnissen (Ärztinnen, Anwälte):**

1. Auch ohne förmliches Mandatsverhältnis besteht Anwaltsgeheimnisschutz für jede Person, die sich an eine Anwältin oder einen Anwalt wendet ([BGer 7B_558/2025 E. 3.4](https://entscheidsuche.ch/docs/CH_BGer/CH_BGer_007_7B-558-2025_2026-04-20.html)).
2. Bei einer sehr grossen Zahl betroffener Dritter (z.B. Patientendaten) die Substanziierung auf Art und Speicherort der geschützten Daten beschränken; eine Einzelbenennung jeder betroffenen Person wird nicht verlangt ([BGer 7B_558/2025 E. 5.3](https://entscheidsuche.ch/docs/CH_BGer/CH_BGer_007_7B-558-2025_2026-04-20.html#consideration_5.3)).

**Für die Staatsanwaltschaft und andere Strafbehörden:**

1. Entsiegelungsgesuche stets mit qualifizierter elektronischer Signatur einreichen, wenn sie elektronisch übermittelt werden; ein unsigniertes E-Mail-Gesuch ist formunwirksam und führt ohne Nachfrist zum Nichteintreten ([BGer 7B_165/2026 E. 2.4](https://entscheidsuche.ch/docs/CH_BGer/CH_BGer_007_7B-165-2026_2026-08-05.html#consideration_2.4)).
2. Ein offensichtlich unbegründetes, missbräuchliches oder verspätetes Siegelungsbegehren kann direkt — ohne Einleitung eines Entsiegelungsverfahrens — abgelehnt werden ([BGer 7B_1154/2024 E. 2.4.1](https://entscheidsuche.ch/docs/CH_BGer/CH_BGer_007_7B-1154-2024_2025-10-02.html#consideration_2.4.1)).
3. Eine vorsorgliche Datenspiegelung bei drohendem Beweisverlust selbst anordnen ist zulässig, aber nur, wenn die dafür eingesetzte sachverständige Person strikt von der Ermittlungstätigkeit getrennt bleibt ([BGE 152 IV 107 E. 5.7.8](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-152-IV-107_2026.html#consideration_5.7.8)).

**Für das Zwangsmassnahmengericht und die Verfahrensleitung:**

1. Bei Drittinhaberschaft mit einer sehr grossen Zahl betroffener Personen (Patientendaten, Klientendaten) die Aussonderung oder Anonymisierung von Amtes wegen prüfen, statt den förmlichen Einzeleinbezug nach Abs. 2 zu erzwingen oder umgekehrt die Substanziierungslast zu überspannen ([BGer 7B_558/2025 E. 5.3](https://entscheidsuche.ch/docs/CH_BGer/CH_BGer_007_7B-558-2025_2026-04-20.html#consideration_5.3)).
2. Für den Sachverständigenbeizug nach Abs. 6 stets eine namentlich bestimmte natürliche Person bezeichnen, nie eine Behörde oder Organisationseinheit als solche ([BGer 7B_245/2026 E. 5.2](https://entscheidsuche.ch/docs/CH_BGer/CH_BGer_007_7B-245-2026_2026-06-16.html#consideration_5.2)).
3. Die Entsiegelung erst anordnen, wenn die Triage geheimnisgeschützter Inhalte abgeschlossen ist — nicht in derselben Verfügung, die noch offene Aussonderungsschritte anordnet ([BGer 7B_245/2026 E. 4.3](https://entscheidsuche.ch/docs/CH_BGer/CH_BGer_007_7B-245-2026_2026-06-16.html#consideration_4.3)).
4. Akzessorische Rügen nach Art. 197 StPO prüfen, sobald irgendein gesetzlicher Geheimnisgrund nach Art. 264 StPO angerufen wird — auch wenn dieser Grund am Ende verworfen wird ([BGE 151 IV 175 E. 3.4](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-151-IV-175_2025.html#consideration_3.4)).

---

## XVII. Materialien und Literatur

- Botschaft zur Änderung der Strafprozessordnung vom 28. August 2019, [BBl 2019 6697](https://www.fedlex.admin.ch/eli/fbl/2019/6697/de), S. 6750 ff.
- DAMIAN GRAF, StPO-Revision: Neues zur Siegelung, in: Jusletter 16. August 2021.
- DAMIAN GRAF / NIKLAUS RÜTSCHE, Datensicherung von Mobiltelefonen und Tablets – technische und [siegelungs-]rechtliche Herausforderungen im Strafverfahren, SJZ 121/2025 S. 607 ff.
- LORENZ BOMMER / PETER GOLDSCHMID, in: Basler Kommentar, Schweizerische Strafprozessordnung, 3. Aufl., Basel 2023, Art. 248a.
- THORMANN/BRECHBÜHL, in: Basler Kommentar, Schweizerische Strafprozessordnung, Bd. II, 3. Aufl. 2023, Art. 248.

*Literaturhinweise sind mit den in diesem Kommentar verwendeten Fall-Recherche-Werkzeugen nicht verifizierbar (dazu Teil D.6 des Skills `glossagens-content-creation`); sie werden als Ausgangspunkt für die Vertiefung angegeben, nicht als geprüfte Zitate.*
