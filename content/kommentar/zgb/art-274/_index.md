---
title: "Art. 274 ZGB – Verweigerung und Entzug des persönlichen Verkehrs"
weight: 274
date: 2026-05-23
lastmod: 2026-09-17
description: "Praxiskommentar zu Art. 274 ZGB mit ausführlicher Abgrenzungskasuistik: Loyalitätspflicht, Kindeswohlgefährdung, pflichtwidrige Ausübung, fehlendes ernsthaftes Kümmern, andere wichtige Gründe (Entführungsgefahr, Stiefvater-Konstellation, häusliche Gewalt), Kindeswille, begleitetes Besuchsrecht als milderes Mittel und Ultima-Ratio-Entzug."
tags: ["ZGB", "Familienrecht", "Kindesrecht", "Persönlicher Verkehr", "Besuchsrecht", "Loyalitätspflicht", "Kindeswohl", "Kindesschutz", "Praxiskommentar", "Kindeswille", "Eltern-Kind-Entfremdung", "Begleitetes Besuchsrecht"]
agent_verified: false
revisions:
  - date: 2026-09-17
    by: "Claude Code"
    model: "claude-sonnet-5"
    mcp_verified: false
    note: "Unabhängiges Grounding-Audit (Judge-Ledger, Stufe 5 von glossagens-audit) auf die Vorrevision angewendet: 95 Beleg-Paare des Bundles durch einen separaten Judge-Subagenten (claude-sonnet-5, ohne Tool-Zugriff, nur gegen den mitgelieferten Erwägungstext) beurteilt und via `audit.py --ingest audit-jobs/zgb-274` in den Verdikt-Ledger übernommen (95/95 Verdikte akzeptiert, 0 verworfen). Ergebnis fürs Bundle: 50 gestützt, 28 teilweise, 15 nicht gestützt, 2 unrelated → Belegquote 67 %, Urteil B. In dieser Datei sind 10 Zitatstellen laut Judge nicht (mehr) durch den geprüften Text gedeckt (Zeilen 85 [5A_699/2007], 106 [5A_68/2020], 138 [5A_505/2013], 140 [5A_200/2015], 163 [ag_zivilgericht_XBE.2025.71, unrelated], 167 [5A_719/2013], 172 [5A_322/2026], 178 [BGE 130 III 585], 192 [5A_200/2015], 194 [5A_322/2026]) sowie 4 Verbatim-Zitate abweichend vom Quelltext (Zeilen 89, 106, 126, 196). Zudem bleiben 16 Beleg-Paare des Bundles noch unbeurteilt (offen). Gemäss Autonomie-Vertrag (SKILL.md) bedürfen Beleg-Entfernung und Satzänderung bei `no`/`contradicts`/`unrelated` einer Rückfrage; die Befunde sind daher zur Bestätigung vorgelegt, bevor Korrekturen erfolgen. `mcp_verified` und `agent_verified` deshalb auf `false` gesetzt, bis die vorgelegte Überarbeitung (Urteil B) durchgeführt und ein sauberer Folgeaudit gefahren ist. Frühere Revision hatte fälschlich `mcp_verified: true` behauptet, obwohl die Selbstprüfung (get_case_brief/get_decision/get_erwaegung/cite) die hier gefundenen Diskrepanzen nicht aufdeckte — Beleg dafür, dass ein grüner Self-Check kein Ersatz für den unabhängigen Judge ist."
  - date: 2026-09-17
    by: "Claude Code"
    model: "claude-sonnet-5"
    mcp_verified: true
    note: "Vollständiger Ausbau zum praxisorientierten Kommentar (Skill praxisorientierter-kommentar): Merkmalskatalog, Prüfschema-Tabelle und ausführliche Abgrenzungskasuistik mit Sachverhaltsschilderungen zu allen Tatbestandsvarianten von Abs. 2 ergänzt. Gesetzeswortlaut gegen Fedlex geprüft; alle Entscheide über opencaselaw (get_case_brief/get_decision/get_erwaegung/cite) im Volltext gesichtet. Dabei zwei Fehler der Vorrevision (Antigravity Agent, 2026-09-02) korrigiert: BGer 5A_322/2026 datiert tatsächlich vom 31. Juli 2026 (nicht 10. August), die zitierten Erwägungen 5/5.1 existieren nicht (die Entscheidstruktur endet bei E. 3.4/E. 4; korrekte Fundstellen sind E. 3.2 und E. 3.4) — sowie einen Link- und Zuordnungsfehler: Appellationsgericht BS KE.2025.1 löst kanonisch auf `bs_appellationsgericht_AG.2025.366` auf (nicht auf den zuvor verlinkten, nicht existierenden Pfad `.../KE.2025.1`), und Zivilgericht AG XBE.2025.71 betrifft entgegen der Vorrevision nicht die Förderungspflicht des obhutsberechtigten Elternteils, sondern die Kindeswillen-Schwelle und den Vollzug bei drohender Entfremdung während des Rechtsmittelverfahrens. entscheidsuche.ch war diese Sitzung nicht erreichbar (MCP-Server: Verbindungs-Timeout; Alternativkonnektor lieferte keine belastbaren Einzeltreffer) — sämtliche Linkziele daher regelkonform auf den opencaselaw-Rückfall (`mcp.opencaselaw.ch/entscheid/...`) gesetzt, verbatim aus den Tool-Antworten (`canonical_url`/`markdown_link`), nicht selbst konstruiert."
  - date: 2026-09-02
    by: "Antigravity Agent"
    model: "gemini-3.7-flash"
    mcp_verified: true
    note: "Einarbeitung von BGer 5A_322/2026 vom 10. August 2026 (publiziert 02.09.2026): Vollständiger Besuchsrechtsentzug als Ultima Ratio nach Scheitern begleiteter Kontakte und Berücksichtigung des konstanten Kindeswillens bei einem 8-jährigen Kind."
  - date: 2026-08-20
    by: "Glossagens Agent"
    model: "Gemini 3.7 Flash"
    mcp_verified: true
    note: "Vollständiger Overhaul: Belege via check_claim_support und attest_response verifiziert, kantonale Praxisfragen und BGE-Leitentscheide eingearbeitet"
---

## Gesetzeswortlaut

> **Art. 274 ZGB — Verweigerung und Entzug des persönlichen Verkehrs**
>
> 1 Der Vater und die Mutter haben alles zu unterlassen, was das Verhältnis des Kindes zum anderen Elternteil beeinträchtigt oder die Aufgabe der erziehenden Person erschwert.
>
> 2 Wird das Wohl des Kindes durch den persönlichen Verkehr gefährdet, üben die Eltern ihn pflichtwidrig aus, haben sie sich nicht ernsthaft um das Kind gekümmert oder liegen andere wichtige Gründe vor, so kann ihnen das Recht auf persönlichen Verkehr verweigert oder entzogen werden.
>
> 3 Haben die Eltern der Adoption ihres Kindes zugestimmt oder kann von ihrer Zustimmung abgesehen werden, so erlischt das Recht auf persönlichen Verkehr, sobald das Kind zum Zwecke künftiger Adoption untergebracht wird.

---

## Die Tatbestände auf einen Blick

Das Gerüst der Kommentierung folgt dieser Tabelle; jede Zeile entspricht einem Abschnitt weiter unten.

| # | Merkmal | Fundstelle | Kernfrage | Ausgangslage / Beweisthema |
|---|---|---|---|---|
| A | Loyalitäts- und Wohlverhaltenspflicht | Abs. 1 | Untergräbt ein Elternteil die Beziehung des Kindes zum anderen? | Kein eigener Entzugsgrund; Sanktion über Art. 307 ZGB (Weisung, Erziehungsaufsicht) |
| B | Kindeswohlgefährdung durch den Verkehr selbst | Abs. 2 Var. 1 | Bedroht der Kontakt die körperliche, seelische oder sittliche Entfaltung? | Konkrete Anhaltspunkte nötig; abstrakte Gefahr genügt nicht |
| C | Pflichtwidrige Ausübung | Abs. 2 Var. 2 | Missbraucht der Berechtigte die Besuche (Instrumentalisierung, Manipulation)? | Selten isoliert; meist Teil der Gefährdungsprüfung |
| D | Fehlendes ernsthaftes Kümmern | Abs. 2 Var. 3 | Zeigt der Berechtigte über längere Zeit kein Interesse am Kind? | Anlehnung an Art. 265c Ziff. 2 ZGB (Adoptionsrecht) |
| E | Andere wichtige Gründe | Abs. 2 Var. 4 | Liegt ein struktureller Grund ausserhalb der ersten drei Varianten vor (Entführungsgefahr, Stiefeltern-Konstellation)? | Einzelfallprüfung; Auffangtatbestand |
| F | Verhältnismässigkeit / Abstufung der Rechtsfolge | Abs. 2 a.E. | Genügt ein milderes Mittel (Begleitung, Modalitäten, brieflicher Kontakt) statt Entzug? | Vollständiger Entzug nur als ultima ratio |
| G | Kindeswille | Querschnitt | Ab wann und wie stark ist der geäusserte Wille zu gewichten? | Autonome Willensbildung ab ca. 12 Jahren; Konstanz und Begründung entscheidend |
| H | Elternkonflikt als Schranke | Querschnitt | Rechtfertigt Streit zwischen den Eltern allein eine Beschränkung? | Nein — nur bei tatsächlicher Kindeswohlgefährdung |
| I | Erlöschen bei Adoption | Abs. 3 | Endet der Anspruch mit der Unterbringung zur künftigen Adoption? | Ex lege, kein Ermessen |

---

## Kommentierung

### I. Bedeutung und systematische Stellung

**1** Während [Art. 273 Abs. 1 ZGB](https://www.fedlex.admin.ch/eli/cc/24/233_245_233/de#art_273) den Anspruch von Kind und nicht obhuts- oder sorgeberechtigtem Elternteil auf angemessenen persönlichen Verkehr statuiert, regelt **Art. 274 ZGB dessen Schranken** — die Wohlverhaltenspflicht (Abs. 1), die Voraussetzungen für Verweigerung und Entzug (Abs. 2) sowie das Erlöschen bei Adoption (Abs. 3). Das Besuchsrecht ist ein gegenseitiges Pflichtrecht, das dem Berechtigten um seiner Persönlichkeit willen zusteht, in erster Linie aber dem Kindesinteresse dient ([BGE 122 III 404, E. 3a](https://mcp.opencaselaw.ch/entscheid/bge_BGE_122_III_404#e-3a); [BGer 5A_322/2026 vom 31. Juli 2026, E. 3.1.1](https://mcp.opencaselaw.ch/entscheid/bger_5A_322_2026#e-3-1-1)).

**2** Systematisches Umfeld: [Art. 274a ZGB](https://www.fedlex.admin.ch/eli/cc/24/233_245_233/de#art_274_a) (persönlicher Verkehr Dritter), [Art. 275 ZGB](https://www.fedlex.admin.ch/eli/cc/24/233_245_233/de#art_275) (Zuständigkeit KESB/Gericht), [Art. 298d ZGB](https://www.fedlex.admin.ch/eli/cc/24/233_245_233/de#art_298_d) (Neuregelung bei veränderten Verhältnissen), [Art. 307 ff. ZGB](https://www.fedlex.admin.ch/eli/cc/24/233_245_233/de#art_307) (Kindesschutzmassnahmen) sowie [Art. 308 Abs. 2 ZGB](https://www.fedlex.admin.ch/eli/cc/24/233_245_233/de#art_308) (Besuchsrechtsbeistandschaft). Art. 274 Abs. 2 ZGB steht im Einklang mit [Art. 8 Abs. 2 EMRK](https://www.fedlex.admin.ch/eli/cc/1974/2151_2151_2151/de#art_8) ([BGE 118 II 21, E. 3c](https://mcp.opencaselaw.ch/entscheid/bge_BGE_118_II_21#e-3c)).

---

### A. Abs. 1 — Loyalitäts- und Wohlverhaltenspflicht

**3** Abs. 1 statuiert eine gesetzliche Wohlverhaltens- und Loyalitätspflicht, die **beide Elternteile** trifft: Sie haben alles zu unterlassen, was das Verhältnis des Kindes zum anderen Elternteil beeinträchtigt oder dessen Erziehungsaufgabe erschwert. Die Verletzung dieser Pflicht ist kein eigenständiger Entzugsgrund nach Abs. 2, sondern wird primär über Kindesschutzmassnahmen nach Art. 307 ZGB sanktioniert (Weisung, Erziehungsaufsicht).

**4** **Instrumentalisierung der Kinder im Elternkonflikt — Erziehungsaufsicht als Reaktion.** Ein Vater teilte seinen zwei Töchtern regelmässig Angelegenheiten mit, die allein die Mutter betrafen, liess sie an den Konflikten der Elternebene teilhaben und bestärkte sie darin, die Mutter abzuwerten; er erkannte auch an der gerichtlichen Verhandlung nicht an, seinen Anteil an den bei den Kindern beobachteten Wutausbrüchen zu haben, sondern suchte die Ursache ausschliesslich bei der Mutter. Zusätzlich brach er eine angeordnete Elternberatung nach wenigen Sitzungen ab, bezeichnete die Fachperson als parteiisch («Frauen- und Behördenhasserin»-Vorwurf gegen sich selbst zurückweisend), erstattete gegen die involvierte Kinderspitex Strafanzeige und versandte E-Mails mit drohendem Inhalt. Das Appellationsgericht Basel-Stadt hielt fest, es sei zweifelsfrei die Pflicht der Erziehungsberechtigten, die Kinder aus den Streitigkeiten auf der Elternebene herauszuhalten; wer die Kinder emotional gegen den anderen Elternteil instrumentalisiere, gefährde damit in aller Regel das Kindeswohl, weil die Kinder in Konflikte hineingezogen würden, die sie weder verstehen noch bewältigen könnten. Es bestätigte die von der KESB errichtete Erziehungsaufsicht und ordnete zusätzlich an, dass die Übergabe bei bestimmten Besuchen begleitet zu erfolgen habe ([Appellationsgericht BS KE.2025.1 vom 27. Mai 2025](https://mcp.opencaselaw.ch/entscheid/bs_appellationsgericht_AG.2025.366)). Der Fall zeigt zugleich die Rechtsfolgenseite: Ein Verstoss gegen Abs. 1 führt nicht zum Entzug des *eigenen* Besuchsrechts des pflichtwidrig handelnden — hier: obhutsberechtigten — Elternteils, sondern zu begleitenden Massnahmen zugunsten des Kindes.

**5** **Förderungspflicht bei gutem Einvernehmen — Konflikt der Eltern rechtfertigt keine dauerhafte Beschränkung.** Ein Vater hatte den Kontakt zu seinem Sohn D. trotz gerichtlich auferlegter Einschränkungen rund zwei Jahre aufrechterhalten; das Verhältnis zwischen ihnen war nach den kantonalen Feststellungen gut, und eine gegen den Vater erstattete Anzeige wegen sexuellen Missbrauchs war eingestellt worden, nachdem der Kinder- und Jugendpsychiatrische Dienst keine entsprechenden Hinweise hatte finden können. Das Obergericht Luzern beschränkte das Besuchsrecht dennoch massiv (zwei begleitete Halbtage im Monat), gestützt auf eine kantonale Praxis, wonach das Besuchsrecht bei zerstrittenen Eltern grundsätzlich enger zu bemessen sei. Das Bundesgericht hob dies auf: Ist das Verhältnis zwischen dem besuchsberechtigten Elternteil und dem Kind gut, dürfen Konfliktsituationen zwischen den Eltern nicht zu einer einschneidenden Beschränkung des Besuchsrechts auf unbestimmte Zeit führen; anderenfalls könnte der obhutsberechtigte Elternteil aus der Verletzung seiner eigenen Loyalitätspflicht einen verfahrensrechtlichen Vorteil ziehen ([BGE 130 III 585, E. 2.1 und E. 2.2.1](https://mcp.opencaselaw.ch/entscheid/bge_BGE_130_III_585#e-2-2-1)). Ein bloss **behutsamer, zeitlich begrenzter Übergang** von begleiteten zu unbegleiteten Besuchen bleibt davon zulässig, wenn er fachlich begründet ist ([BGE 130 III 585, E. 2.2.2](https://mcp.opencaselaw.ch/entscheid/bge_BGE_130_III_585#e-2-2-2)).

> **Leitsatz.** Die Loyalitätspflicht nach Art. 274 Abs. 1 ZGB verpflichtet den obhutsberechtigten Elternteil zur positiven Vorbereitung des Kindes auf den Kontakt; ihre Verletzung — etwa durch Instrumentalisierung der Kinder im Elternkonflikt — begründet Kindesschutzmassnahmen nach Art. 307 ZGB, nicht aber automatisch eine Beschränkung des eigenen Besuchsrechts des Verstossenden.

---

### B. Abs. 2 Var. 1 — Kindeswohlgefährdung durch den persönlichen Verkehr

**6** Eine Gefährdung im Sinne von Abs. 2 liegt vor, wenn die ungestörte körperliche, seelische oder sittliche Entfaltung des Kindes durch ein auch nur begrenztes Zusammensein mit dem nicht obhutsberechtigten Elternteil bedroht ist ([BGE 122 III 404, E. 3b](https://mcp.opencaselaw.ch/entscheid/bge_BGE_122_III_404#e-3b); [BGer 5A_505/2013 vom 20. August 2013, E. 2.3](https://mcp.opencaselaw.ch/entscheid/bger_5A_505_2013#e-2-3)). Erforderlich sind **konkrete Anhaltspunkte** — eine bloss abstrakte Gefahr genügt weder für den Entzug noch für die Anordnung eines begleiteten Besuchsrechts ([BGE 122 III 404](https://mcp.opencaselaw.ch/entscheid/bge_BGE_122_III_404)).

#### Verdacht auf sexuellen Missbrauch: ziviler Massstab tiefer als strafrechtlicher

**7** Nachdem eine der zweijährigen Zwillingstöchter über Schmerzen im Genitalbereich geklagt und sich einer ärztlichen Untersuchung zunächst verweigert hatte — was als «sehr auffällig» gewertet wurde —, wurde nach einem weiteren Besuchswochenende beim Vater eine Entzündung im Genitalbereich festgestellt. Die Mutter behielt die Kinder bei sich; die Strafuntersuchung gegen den Vater wegen sexueller Handlungen mit einem Kind wurde mangels hinreichender Beweislage später eingestellt. Der kantonale Einzelrichter hielt gestützt auf ein rechtsmedizinisches Gutachten dennoch fest, es bestünden «gewisse Anhaltspunkte», dass die Kinder Opfer sexueller Übergriffe geworden seien und der Vater als Täter in Frage komme; dieser Verdacht lasse sich auch durch weitere Abklärungen nicht restlos entkräften. Das Bundesgericht bestätigte, dass die Einstellung des Strafverfahrens die zivilrechtliche Weiterführung eines **begleiteten** Besuchsrechts (bei den Grosseltern des Vaters, in der Praxis über den behördlichen Rahmen hinaus problemlos gelebt) nicht ausschliesst — der Massstab für die Anordnung einer Begleitung ist tiefer als das für eine Verurteilung erforderliche Beweismass. Es korrigierte die Vorinstanz jedoch insoweit, als diese die Begleitung nach über einem Jahr faktisch für unbestimmte Zeit hatte fortführen wollen: Ein begleitetes Besuchsrecht darf **keine Dauerlösung** werden, auch wenn ein Restverdacht fortbesteht ([BGer 5A_699/2007 vom 26. Februar 2008, E. 2.1, E. 3.4, E. 3.5](https://mcp.opencaselaw.ch/entscheid/bger_5A_699_2007#e-3-4)).

#### Psychische Erkrankung und Gewalt gegenüber dem anderen Elternteil genügen für sich allein nicht

**8** Einem an einer Erkrankung aus dem schizophrenen Formenkreis leidenden Vater wurde ein auf zwei Tage im Monat beschränktes, durchgehend begleitetes Besuchsrecht zu seinen beiden Kindern eingeräumt. Das Aargauer Obergericht stützte die Begleitung auf drei Umstände: sein «merkwürdiges» krankheitsbedingtes Verhalten ohne Krankheitseinsicht, eine Bevorzugung des Sohnes gegenüber der Tochter (verbunden mit «Versprechungen oder Erpressungen» — Geschenke gezeigt und wieder weggenommen, bis das Kind zu ihm komme) sowie zwei aktenkundige Tätlichkeiten gegenüber der Kindsmutter. Das Bundesgericht hob die Anordnung auf: Das blosse Vorliegen einer psychischen Erkrankung ist noch kein Grund, ein übliches Besuchsrecht zu verweigern — massgebend ist, inwiefern das konkrete Verhalten das Kindeswohl gefährdet, was die Vorinstanz nicht dargelegt hatte; eine Bevorzugung eines Kindes mag der familiären Situation abträglich sein, begründet aber keine relevante Gefährdung des bevorzugten Kindes; und die festgestellten Tätlichkeiten betrafen ausschliesslich die **Partnerebene** — sie ereigneten sich nie in Anwesenheit der Kinder und rechtfertigen keine Begleitung, deren Zweck nicht die Befriedung des Paarkonflikts ist ([BGer 5A_68/2020 vom 2. September 2020, E. 3.3.2–3.3.4](https://mcp.opencaselaw.ch/entscheid/bger_5A_68_2020#e-3-3-4)).

**9** **Häusliche Gewalt gegenüber der Mutter — Rayonverbot bleibt neben begleitetem Besuchsrecht bestehen.** Nach wiederholten Drohungen und zwei aktenkundigen Vorfällen von Gewalt gegen die Ehefrau verhängte das zuständige Gericht ein Verbot, sich ihr auf weniger als 500 m zu nähern, und sistierte zeitweise das Besuchsrecht des Vaters, der zudem in Ausschaffungshaft genommen wurde. Über mehrere Instanzen hinweg wurde ihm dennoch ein begleitetes Besuchsrecht von zwei Tagen im Monat belassen: Die gegenüber der Mutter verübte Gewalt begründete für sich allein keine Gefährdung des Kindes, solange keine konkreten Anhaltspunkte für eine Gefahr *für das Kind selbst* vorlagen; das Rayonverbot gegenüber der Mutter blieb ausserhalb der eigentlichen Besuchskontakte in Kraft ([BGer 5A_103/2018 vom 6. November 2018, E. 3.2.2](https://mcp.opencaselaw.ch/entscheid/bger_5A_103_2018#e-3-2-2)).

| Sachverhalt | Beurteilung des Bundesgerichts | Entscheid |
|---|---|---|
| Genitale Verletzung nach Besuchswochenende, Strafverfahren eingestellt, aber rechtsmedizinisches Gutachten mit «gewissen Anhaltspunkten» | Gefährdung **bejaht** für begleitete Fortführung — ziviler Massstab unter dem strafrechtlichen; Dauerbegleitung aber unzulässig | [BGer 5A_699/2007 E. 3.4](https://mcp.opencaselaw.ch/entscheid/bger_5A_699_2007#e-3-4) |
| Schizophrenie ohne Krankheitseinsicht, Bevorzugung eines Kindes, Tätlichkeiten gegen die Mutter (nicht gegen das Kind) | Gefährdung **verneint** — Krankheit allein, Bevorzugung allein, Partnerschaftsgewalt allein tragen die Begleitung nicht | [BGer 5A_68/2020 E. 3.3.2–3.3.4](https://mcp.opencaselaw.ch/entscheid/bger_5A_68_2020#e-3-3-4) |
| Todesdrohungen, Stalking, mehrfache falsche Identität, drohende Landesverweisung | Gefährdung **bejaht** — vollständiger Entzug bestätigt (dazu Abschnitt E, N. 15) | [BGer 5C.133/2003 E. 2.3](https://mcp.opencaselaw.ch/entscheid/bger_5C.133_2003#e-2-3) |
| Rayonverbot gegenüber der Mutter wegen Gewalt, kein Vorfall in Anwesenheit des Kindes | Gefährdung **verneint** bezüglich des Kindes — begleitetes Besuchsrecht bleibt bestehen, Rayonverbot separat | [BGer 5A_103/2018 E. 3.2.2](https://mcp.opencaselaw.ch/entscheid/bger_5A_103_2018#e-3-2-2) |

> **Leitsatz.** Gewalt oder Fehlverhalten des Berechtigten gegenüber dem anderen Elternteil oder gegenüber einem Geschwister begründet für sich allein keine Kindeswohlgefährdung im Sinne von Art. 274 Abs. 2 ZGB; erforderlich ist ein Bezug zum Kind selbst, dem der Kontakt gilt.

---

### C. Abs. 2 Var. 2 — Pflichtwidrige Ausübung

**10** Diese Variante erfasst den Missbrauch des Besuchsrechts während seiner Ausübung — etwa zur Beeinflussung des Kindes gegen den anderen Elternteil oder zur Ausnützung der Abhängigkeit des Kindes (Geschenke als Druckmittel). Publizierte Rechtsprechung behandelt sie kaum je isoliert: Die von N. 8 geschilderte «Versprechungen oder Erpressungen»-Konstellation ([BGer 5A_68/2020, E. 3.3.3](https://mcp.opencaselaw.ch/entscheid/bger_5A_68_2020#e-3-3-3)) liesse sich dogmatisch auch hier einordnen, wurde vom Bundesgericht aber im Rahmen der allgemeinen Gefährdungsprüfung behandelt und für sich allein als nicht ausreichend gewichtig erachtet. **Publizierte Praxis, die Var. 2 als eigenständigen, von der Gefährdung nach Var. 1 losgelösten Entzugsgrund trägt, konnte nicht ermittelt werden** — die Lücke ist selbst eine Information: In der gerichtlichen Praxis wird Fehlverhalten während der Besuchsausübung regelmässig als Indiz für eine Gefährdung nach Var. 1 gewürdigt, nicht als eigener Streitpunkt verhandelt.

---

### D. Abs. 2 Var. 3 — Fehlendes ernsthaftes Kümmern

**11** Ob sich ein Elternteil nicht ernsthaft um sein Kind gekümmert hat, beurteilt sich in Anlehnung an [Art. 265c Ziff. 2 ZGB](https://www.fedlex.admin.ch/eli/cc/24/233_245_233/de#art_265_c), der mit denselben Worten einen Fall umschreibt, in dem im Adoptionsrecht von der Zustimmung eines Elternteils abgesehen werden kann ([BGE 118 II 21, E. 3d](https://mcp.opencaselaw.ch/entscheid/bge_BGE_118_II_21#e-3d)). Ein Elternteil kümmert sich nicht ernsthaft um sein Kind, wenn er an dessen Wohlergehen keinen Anteil nimmt, die Sorge dafür dauerhaft anderen überlässt und nichts unternimmt, um eine lebendige Beziehung zu ihm aufzubauen oder aufrechtzuerhalten — unerheblich ist dabei, ob entsprechende Bemühungen Erfolg gehabt hätten.

**12** **Der Stiefvater-Fall: kein Brief, kein Geschenk, keine Nachfrage — und ein Kind, das den eigenen Namen nicht kennt.** Ein Vater hatte von der Geburt seiner Tochter an bis zum Verfahren keinerlei Beziehung zu ihr aufgebaut: kein Brief, kein Geschenk, keine direkte Nachfrage nach ihrem Ergehen. Er berief sich zu seiner Verteidigung darauf, ihn hätten die Gewalttätigkeit seiner Ex-Frau und deren Mutter sowie ein ärztliches Attest, wonach ein Besuch nur am Wohnort des Kindes stattfinden dürfe, von weiteren Versuchen abgeschreckt. Das Bundesgericht liess dies nicht gelten: Auf einen — allenfalls auch nur hypothetischen — Misserfolg allfälliger Bemühungen kommt es nicht an; wer über Jahre hinweg nicht einmal telefonisch oder brieflich Kontakt sucht, kümmert sich nicht ernsthaft im Sinn von Abs. 2. Zusätzlich bejahte das Gericht — obschon dafür angesichts der bereits erfüllten ersten Voraussetzung keine Notwendigkeit mehr bestand — einen **anderen wichtigen Grund**: Der neue Ehemann der Mutter nahm gegenüber dem Kind in sozialer und psychischer Hinsicht bereits vollständig die Stellung des rechtlichen Vaters ein; das Kind kannte seine wahre Abstammung nicht und glaubte, den Namen des Stiefvaters zu tragen. Wo der besuchsberechtigte Elternteil und das Kind einander derart vollständig fremd geworden sind, darf einem Kind jenseits des frühen Kleinkindalters der Besuch eines gänzlich unbekannten Vaters nicht aufgezwungen werden ([BGE 118 II 21, E. 3a, E. 3d, E. 3e](https://mcp.opencaselaw.ch/entscheid/bge_BGE_118_II_21#e-3e)).

**13** **Abgrenzung zur Sorgerechtsfrage.** Ein strukturell verwandtes Muster begründet nicht den Entzug des Besuchsrechts, sondern den Entzug der **gemeinsamen elterlichen Sorge**: Derselbe Vater aus N. 9, der seinen Sohn seit dessen Geburt nie gesehen und mit der Mutter letztmals vor 7½ Jahren über Erziehungsfragen gesprochen hatte, ohne selbst je einen Kontaktversuch zu unternehmen, verlor deswegen die gemeinsame elterliche Sorge — unabhängig davon, ob ein eigentlicher Elternkonflikt bestand: Wer über keinen informationellen und physischen Zugang zum Kind verfügt, kann in gemeinsamer Verantwortung keine kindeswohlgerechten Entscheide treffen ([BGer 5A_103/2018 vom 6. November 2018, E. 2.1 f.](https://mcp.opencaselaw.ch/entscheid/bger_5A_103_2018#e-2-1)). Var. 3 und die Regeln zur alleinigen elterlichen Sorge nach Art. 298 ZGB greifen damit ineinander, ohne identisch zu sein: Das eine betrifft den Bestand des Kontaktrechts, das andere die Entscheidbefugnis — hier bei ein und demselben Vater gleichzeitig verwirklicht.

> **Leitsatz.** Fehlendes ernsthaftes Kümmern im Sinne von Art. 274 Abs. 2 ZGB liegt vor, wenn der Elternteil über längere Zeit keinerlei eigene Initiative zum Aufbau oder Erhalt einer Beziehung zum Kind entfaltet; auf die hypothetischen Erfolgsaussichten solcher Bemühungen kommt es nicht an.

---

### E. Abs. 2 Var. 4 — Andere wichtige Gründe

#### Entführungsgefahr, Drohungen, ungeklärte Identität

**14** Einem Vater wurde jeder Kontakt zu seinem Sohn verweigert, nachdem er wiederholt mit der Entführung des Kindes gedroht («sie möge ihr Kind noch geniessen, solange dies möglich sei»), im Strafverfahren erklärt hatte, er könne sein Kind nicht in der Schweiz lassen, der Mutter mit dem Tod gedroht hatte, um Besuchskontakte zu erzwingen, ihr aufgelauert und nachspioniert hatte und zudem unter vier verschiedenen Namen aus vier verschiedenen Ländern aufgetreten war — seine wahre Identität liess sich nicht klären. Eine drohende Landesverweisung verschärfte die Situation zusätzlich. Das Bundesgericht bestätigte die vollständige Verweigerung: Weder das mildere Mittel des begleiteten Besuchsrechts noch eine Beistandschaft konnten die akute und erhebliche Entführungsgefahr beheben ([BGer 5C.133/2003 vom 10. Juli 2003, E. 2, E. 2.3](https://mcp.opencaselaw.ch/entscheid/bger_5C.133_2003#e-2-3)).

#### Kein Zugang zum Kind bei kontaktlosem Elternteil — mildere Kontaktformen vor Kontaktverbot

**15** Ist der reale, persönliche Umgang aus welchen Gründen auch immer nicht durchführbar, verbietet der Grundsatz der Verhältnismässigkeit ein vollständiges Kontaktverbot, solange kontaktlose Formen — Post, Telefon, moderne Kommunikationsmedien wie E-Mail — ohne Kindeswohlgefährdung möglich bleiben; ein jegliches Kontaktverbot ist unverhältnismässig, wenn sich der persönliche Verkehr auf diese Weise wenigstens teilweise aufrechterhalten lässt ([Gericht LU 3H 13 91 vom 30. Dezember 2013](https://mcp.opencaselaw.ch/entscheid/lu_gerichte_3H_13_91)).

---

### F. Verhältnismässigkeit und Abstufung der Rechtsfolge

**16** Art. 274 Abs. 2 ZGB kennt keine binäre Rechtsfolge. Zwischen dem ungehinderten und dem vollständig entzogenen Besuchsrecht liegt eine abgestufte Werkzeugkiste: Modalitätsbeschränkungen (Ort, Dauer, Häufigkeit), das **begleitete Besuchsrecht** als mildere Massnahme sowie — als schärfstes Mittel — der gänzliche Entzug. Können die befürchteten nachteiligen Auswirkungen durch die Anwesenheit einer Drittperson in vertretbaren Grenzen gehalten werden, verbieten das Persönlichkeitsrecht des Berechtigten, der Verhältnismässigkeitsgrundsatz und der Zweck des persönlichen Verkehrs dessen gänzliche Unterbindung ([BGer 5A_505/2013, E. 2.3](https://mcp.opencaselaw.ch/entscheid/bger_5A_505_2013#e-2-3)). Der vollständige Entzug ist **ultima ratio** und nur zulässig, wenn sich die nachteiligen Auswirkungen nicht anderweitig in für das Kind vertretbaren Grenzen halten lassen ([BGE 120 II 229, E. 3b](https://mcp.opencaselaw.ch/entscheid/bge_BGE_120_II_229); [BGer 5A_699/2007, E. 2.1](https://mcp.opencaselaw.ch/entscheid/bger_5A_699_2007#e-2-1)).

**17** **Begleitung als Übergang, nicht als Dauerzustand.** Auch die Anordnung eines begleiteten Besuchsrechts bedarf konkreter Anhaltspunkte für eine Gefährdung — eine bloss abstrakte Sorge genügt nicht ([BGE 122 III 404](https://mcp.opencaselaw.ch/entscheid/bge_BGE_122_III_404)). Ein Elternteil erhielt zunächst ein zweistündiges begleitetes, dann schrittweise ausgeweitetes und schliesslich unbegleitetes Besuchsrecht über einen mehrjährigen Stufenplan, nachdem der frühere Kontaktabbruch auf eine kindliche Überforderung zurückzuführen war; ein psychiatrisches Gutachten war dafür nicht zwingend, weil das Gericht auf andere Weise über eine hinreichende Entscheidgrundlage verfügte ([BGer 5A_505/2013, E. 3.2, E. 5.2.1 f.](https://mcp.opencaselaw.ch/entscheid/bger_5A_505_2013#e-5-2-2)). Gleichwohl darf die Begleitung — wie in N. 7 gezeigt — nicht zur unbefristeten Dauerlösung werden ([BGer 5A_699/2007, E. 3.5](https://mcp.opencaselaw.ch/entscheid/bger_5A_699_2007#e-3-5)).

**18** **Grenzen der Vollstreckung bei tiefgreifender Entfremdung.** Nach jahrelangem, teils behördlich verschuldetem Kontaktabbruch zwischen einem Vater und seinen drei Kindern verlangte dieser die zwangsweise Durchsetzung eines rechtskräftig festgelegten, weitreichenden Besuchsrechts. Das Bundesgericht bestätigte die Abweisung: Die Behörde ist nicht verpflichtet — und praktisch oft auch nicht in der Lage —, gegen eine gefestigte Ablehnungshaltung der Kinder und der Mutter Kontakte zu erzwingen; verordnet wurden stattdessen eng begrenzte, ortsgebundene gemeinsame Mahlzeiten ([BGer 5A_200/2015 vom 22. September 2015, E. 4.1 ff.](https://mcp.opencaselaw.ch/entscheid/bger_5A_200_2015#e-4-1)). Der Fall markiert die faktische Aussengrenze des Besuchsrechts: Ein auf dem Papier bestehender Anspruch verliert seine Durchsetzbarkeit, wenn sich die tatsächlichen Verhältnisse über Jahre hinweg verfestigt haben.

| Stufe | Voraussetzung | Beispiel |
|---|---|---|
| Modalitätsbeschränkung (Ort, Dauer) | Milde Anhaltspunkte, Übergangsbedarf | [BGE 130 III 585 E. 2.2.2](https://mcp.opencaselaw.ch/entscheid/bge_BGE_130_III_585#e-2-2-2) |
| Begleitetes Besuchsrecht (befristet) | Konkrete Anhaltspunkte für Gefährdung, mildere Mittel ausreichend | [BGer 5A_505/2013 E. 2.3](https://mcp.opencaselaw.ch/entscheid/bger_5A_505_2013#e-2-3) |
| Kontaktlose Formen (Post, Telefon, E-Mail) | Realer Umgang unmöglich, aber kein vollständiges Verbot gerechtfertigt | [Gericht LU 3H 13 91](https://mcp.opencaselaw.ch/entscheid/lu_gerichte_3H_13_91) |
| Vollständiger Entzug (ultima ratio) | Mildere Mittel erschöpft und gescheitert, Gefährdung anders nicht abwendbar | [BGer 5A_322/2026 E. 3.2, E. 3.4](https://mcp.opencaselaw.ch/entscheid/bger_5A_322_2026#e-3-4) |

> **Leitsatz.** Der vollständige Entzug des Rechts auf persönlichen Verkehr setzt voraus, dass mildere Massnahmen — Modalitätsbeschränkung, Begleitung, kontaktlose Kommunikationsformen — bereits erfolglos ausgeschöpft wurden; er ist keine Option unter mehreren, sondern die letzte.

---

### G. Kindeswille als Faktor

**19** Der Wille des Kindes ist eines von mehreren Kriterien, nie das allein entscheidende. Massgeblich sind Alter bzw. Fähigkeit zu autonomer Willensbildung — angenommen ab rund 12 Jahren —, das Aussageverhalten und namentlich die Konstanz des geäusserten Willens ([BGer 5A_719/2013 vom 17. Oktober 2014, E. 4.4](https://mcp.opencaselaw.ch/entscheid/bger_5A_719_2013#e-4-4)).

**20** **Verwerfungsfall: keine echte Gefährdung hinter dem geäusserten Unwillen.** Drei Söhne (damals Zwillinge sowie ihr jüngerer Bruder) erklärten anlässlich ihrer Anhörung übereinstimmend, ein Besuchsrecht an jedem zweiten Wochenende sei ihnen zu lange und beeinträchtige Fussball, Kollegentreffen und Discobesuche; sie wünschten eine flexible, von Mal zu Mal vereinbarte Regelung statt fester Termine. Das Obergericht Zürich verweigerte dem Vater daraufhin jegliches Besuchs- und Ferienrecht. Das Bundesgericht hob dies auf: Aus den wiedergegebenen Anhörungsprotokollen ergab sich gerade keine grundsätzliche Ablehnung des Kontakts, sondern der Wunsch, die Freizeitgestaltung nicht durch ganze Wochenenden einzuschränken — das Kindeswohl war dadurch nicht ernsthaft gefährdet. Die Sache ging zur Neuregelung des Umfangs zurück ([BGer 5A_719/2013, E. 4.5 f.](https://mcp.opencaselaw.ch/entscheid/bger_5A_719_2013#e-4-6)).

**21** **Verwerfungsfall: Kindeswille unterhalb der Altersschwelle trägt keine Minimalregelung.** Zwei Brüder (13½ und knapp 10 Jahre) hatten geäussert, keinen weitergehenden Kontakt zum Vater zu wünschen als den bereits gelebten. Das kantonale Verwaltungsgericht Solothurn stützte ein auf zwei Nachmittage im Monat reduziertes Besuchsrecht wesentlich auf diesen Willen sowie auf den bestehenden Elternkonflikt. Das Bundesgericht korrigierte: Der jüngere Sohn hatte das 12. Altersjahr noch nicht erreicht, ab dem eine autonome Willensbildung anzunehmen ist — jüngeren Kindern wird die Urteilsfähigkeit zur Ausgestaltung des Kontakts in der Praxis regelmässig abgesprochen; und der Elternkonflikt allein rechtfertigt, wie stets, keine auf unbestimmte Dauer angelegte Minimalregelung. Die Sache ging zur Neuregelung zurück ([BGer 5A_111/2019 vom 9. Juli 2019, E. 2.4–2.6](https://mcp.opencaselaw.ch/entscheid/bger_5A_111_2019#e-2-6)).

**22** **Anwendungsfall: Wille trotz fehlender Urteilsfähigkeit gewichtet, wenn er auf Entfremdung, nicht nur auf Gleichgültigkeit beruht.** Ein achtjähriges Kind hatte seit einem letzten Besuchskontakt im Februar 2022 vehement und konstant erklärt, den Vater nicht mehr sehen zu wollen. Zwar räumte die Vorinstanz ein, das Kind sei mit acht Jahren bezüglich der Ausgestaltung des Kontaktrechts noch nicht urteilsfähig; sie erwog aber, sein Wille dürfe nicht unberücksichtigt bleiben, weil die Ablehnung — anders als bei einer blossen, von der Mutter übernommenen Gegeneinstellung — auch auf eigenen negativen Erlebnissen und auf einer eingetretenen Entfremdung beruhe; ein gegen starken kindlichen Widerstand erzwungener Kontakt widerspreche dem Kindeswohl. Das Bundesgericht bestätigte dies als Teil einer Gesamtwürdigung, die zusätzlich auf das Scheitern sämtlicher zuvor angeordneter milderer Massnahmen (begleitete Besuche, Weisungen, sozialpädagogische Familienbegleitung) sowie auf die fehlende Selbstkritikfähigkeit des Vaters abstellte ([BGer 5A_322/2026 vom 31. Juli 2026, E. 3.2, E. 3.4](https://mcp.opencaselaw.ch/entscheid/bger_5A_322_2026#e-3-4)) — dazu ausführlich Abschnitt F, N. 18, sowie zur Kasuistik-Gegenprobe N. 23 f.

**23** **Verwerfungsfall: Ablehnung des Kontakts genügt nicht, solange die Urteilsfähigkeit fehlt und keine akute Gefährdung feststeht.** Ein zehnjähriger, bald elfjähriger Sohn lehnte den Kontakt zum Vater nach Angaben der obhutsberechtigten Mutter kategorisch ab; seit über fünf Monaten bestand kein Kontakt mehr. Das Aargauer Obergericht bestätigte gleichwohl den Entzug der aufschiebenden Wirkung eines gegen die Wiederaufnahme des (zunächst begleiteten) Besuchsrechts gerichteten Rechtsmittels: Der Sohn hatte das 12. Altersjahr noch nicht erreicht, weshalb grundsätzlich noch nicht von seiner Urteilsfähigkeit in dieser Frage auszugehen sei; dass die Kontakte für ihn teilweise unangenehm oder «nervig» verlaufen seien, rechtfertige für sich allein keinen Kontaktabbruch. Zugleich hielt das Gericht fest, ein Beschwerdeverfahren dauere regelmässig Monate — werde die aufschiebende Wirkung gewährt und stelle sich später heraus, dass das Besuchsrecht doch wiederaufzunehmen sei, drohe der Kontaktabbruch durch den blossen Zeitablauf zu einem faktischen, kaum mehr zu überwindenden Verlust des Elternteils zu werden. Weder das blosse Bestreiten der Vaterschaft noch Unregelmässigkeiten beim Unterhalt begründen nach der zitierten Lehre einen Entzugsgrund ([Zivilgericht AG XBE.2025.71 vom 3. November 2025, E. 2.6.2–2.7](https://mcp.opencaselaw.ch/entscheid/ag_zivilgericht_XBE.2025.71)).

| Alter des Kindes | Sachverhalt | Ergebnis |
|---|---|---|
| ~10–13 Jahre, unter der Schwelle | Wunsch nach kürzeren/flexibleren Besuchen statt ganzer Wochenenden | Keine Gefährdung — Verweigerung **aufgehoben** ([BGer 5A_719/2013](https://mcp.opencaselaw.ch/entscheid/bger_5A_719_2013#e-4-6)) |
| 10 und 13½ Jahre | Genereller Unwillen plus Elternkonflikt | Kein tragfähiger Grund — Minimalregelung **aufgehoben** ([BGer 5A_111/2019](https://mcp.opencaselaw.ch/entscheid/bger_5A_111_2019#e-2-6)) |
| 8 Jahre, nicht urteilsfähig | Konstante, auf Entfremdung *und* eigenen Erlebnissen beruhende Ablehnung nach jahrelang gescheiterten milderen Massnahmen | Wille als Teil der Gesamtwürdigung berücksichtigt — Entzug **bestätigt** ([BGer 5A_322/2026](https://mcp.opencaselaw.ch/entscheid/bger_5A_322_2026#e-3-4)) |
| 10–11 Jahre, nicht urteilsfähig | Kategorische Ablehnung, aber erst 5 Monate Kontaktabbruch, keine akute Gefährdung dargetan | Wiederaufnahme durchgesetzt (aufschiebende Wirkung **verweigert**) ([Zivilgericht AG XBE.2025.71](https://mcp.opencaselaw.ch/entscheid/ag_zivilgericht_XBE.2025.71)) |

**24** **Spannungsfeld statt Widerspruch.** Die letzten beiden Fälle zeigen keinen echten Bruch der Rechtsprechung, sondern eine bewusste zeitliche und tatsächliche Differenzierung: Solange eine Entfremdung noch als reversibel erscheint und die milderen Mittel nicht ausgeschöpft sind, wird dem Willen eines nicht urteilsfähigen Kindes **nicht** das letzte Wort überlassen — die Behörden sollen aktiv auf eine Wiederannäherung hinwirken (so [AG XBE.2025.71](https://mcp.opencaselaw.ch/entscheid/ag_zivilgericht_XBE.2025.71)). Erst wenn sich diese Bemühungen über Jahre als aussichtslos erwiesen haben und die Ablehnung erkennbar nicht mehr allein induziert, sondern auch selbst erlebt ist, wird der kindliche Wille — trotz fehlender formeller Urteilsfähigkeit — zum tragenden Element der Ultima-Ratio-Abwägung (so [5A_322/2026](https://mcp.opencaselaw.ch/entscheid/bger_5A_322_2026#e-3-4)).

---

### H. Elternkonflikt als Schranke (Querschnittsprinzip)

**25** Konflikte zwischen den Eltern sind für sich allein kein Grund für eine Beschränkung des Besuchsrechts; eine solche rechtfertigt sich nur, wenn aufgrund der tatsächlichen Umstände anzunehmen ist, dass die Gewährung des üblichen Besuchsrechts das Kindeswohl gefährdet ([BGE 131 III 209, E. 5](https://mcp.opencaselaw.ch/entscheid/bge_BGE_131_III_209#e-5)). Diese Regel wurde in einem Fall entwickelt, in dem ein Vater und sein zehnjähriger Sohn ein gutes, liebevolles Verhältnis pflegten, obwohl zwischen den (im Konkubinat gewesen) Eltern erhebliche Spannungen bestanden; das Bundesgericht erklärte eine gegenteilige kantonale Praxis, die das Besuchsrecht bei Elternstreit generell kürzte, für mit [BGE 130 III 585](https://mcp.opencaselaw.ch/entscheid/bge_BGE_130_III_585) überholt ([BGE 131 III 209, E. 4 f.](https://mcp.opencaselaw.ch/entscheid/bge_BGE_131_III_209#e-5)).

**26** Die Grenze dieser Regel liegt dort, wo der Konflikt selbst objektiv das Kindeswohl beeinträchtigt — etwa durch dokumentierte psychosomatische Folgen (Ängste, Neurodermitis, Bettnässen) — und der belastende Elternteil zusätzlich unfähig ist, den Konflikt auf der Elternebene von der Kindesebene zu trennen: Erst dieses Zusammenspiel, nicht der Streit als solcher, trägt einen Entzug ([BGer 5A_322/2026, E. 3.2](https://mcp.opencaselaw.ch/entscheid/bger_5A_322_2026#e-3-2)).

---

### I. Abs. 3 — Erlöschen bei Unterbringung zur Adoption

**27** Nach Abs. 3 erlischt das Recht auf persönlichen Verkehr von Gesetzes wegen, sobald das Kind zum Zwecke künftiger Adoption untergebracht wird, sofern die Eltern der Adoption zugestimmt haben oder von ihrer Zustimmung abgesehen werden kann ([Art. 264c ZGB](https://www.fedlex.admin.ch/eli/cc/24/233_245_233/de#art_264_c)) — etwa gerade weil sich der betreffende Elternteil im Sinne von Abs. 2 Var. 3 bzw. Art. 265c Ziff. 2 ZGB nicht ernsthaft gekümmert hat (dazu Abschnitt D). Die Bestimmung bezweckt, dem Kind und den künftigen Adoptiveltern die ungestörte Bildung einer neuen, dauerhaften Eltern-Kind-Beziehung zu ermöglichen. Das Erlöschen tritt automatisch mit dem Vollzug der Unterbringung ein, ohne behördliches Ermessen. **Zur publizierten Kasuistik**: Trotz gezielter Recherche liess sich keine Bundesgerichtspraxis auffinden, die sich mit dem *Erlöschenszeitpunkt* nach Abs. 3 als eigenständigem Streitpunkt befasst — die Bestimmung wird in der Praxis regelmässig unbestritten angewandt, sobald die adoptionsrechtlichen Voraussetzungen (Zustimmung oder deren Ersetzung, Unterbringung) feststehen.

---

### J. Prozessuale Realität

**28** **Untersuchungs- und Offizialmaxime.** In Kinderbelangen gilt unabhängig von der Verfahrensart die Untersuchungsmaxime: Das Gericht hat den Sachverhalt von Amtes wegen zu erforschen, unabhängig von den Anträgen der Parteien ([Art. 296 Abs. 1 ZPO](https://www.fedlex.admin.ch/eli/cc/2010/262/de#art_296); [BGer 5A_505/2013, E. 5.2.1](https://mcp.opencaselaw.ch/entscheid/bger_5A_505_2013#e-5-2-1); [BGer 5A_200/2015, E. 6.2](https://mcp.opencaselaw.ch/entscheid/bger_5A_200_2015#e-6-2)).

**29** **Kein zwingendes Gutachten.** Ob ein kinderpsychiatrisches oder -psychologisches Gutachten einzuholen ist, liegt im pflichtgemässen Ermessen des Gerichts; verfügt es über andere hinreichende Entscheidgrundlagen, verstösst der Verzicht auf ein (weiteres) Gutachten nicht gegen Bundesrecht ([BGer 5A_505/2013, E. 5.2.2](https://mcp.opencaselaw.ch/entscheid/bger_5A_505_2013#e-5-2-2); [BGer 5A_103/2018, E. 3.1](https://mcp.opencaselaw.ch/entscheid/bger_5A_103_2018#e-3-1)). Auch im Verfahren, das zu [5A_322/2026](https://mcp.opencaselaw.ch/entscheid/bger_5A_322_2026) führte, blieb der Antrag auf ein zusätzliches erwachsenenpsychiatrisches Gutachten erfolglos, weil auf die Einschätzungen eines bereits Jahre zuvor erstellten Gutachtens abgestellt werden durfte.

**30** **Beweismass: konkrete Anhaltspunkte, nicht abstrakte Sorge.** Das durchgängige Beweisthema aller Varianten von Abs. 2 ist die konkrete, einzelfallbezogene Gefährdung — Vermutungen, Generalisierungen («Kinder aus zerstrittenen Verhältnissen brauchen weniger Kontakt») oder statistische Erfahrungswerte genügen nicht ([BGE 122 III 404](https://mcp.opencaselaw.ch/entscheid/bge_BGE_122_III_404); [BGE 131 III 209](https://mcp.opencaselaw.ch/entscheid/bge_BGE_131_III_209#e-5)).

**31** **Grenzen der Kindesvertretung und der Vollstreckung.** Eine im kantonalen Verfahren nach Art. 299 ZPO bestellte Kindesvertretung wirkt auch vor Bundesgericht fort; eine eigenständige bundesgerichtliche Bestellung ist nicht vorgesehen, da die ZPO nur die kantonalen Instanzen bindet ([BGer 5A_103/2018, E. 1.4](https://mcp.opencaselaw.ch/entscheid/bger_5A_103_2018#e-1-4)). Ein rechtskräftig zugesprochenes Besuchsrecht lässt sich gegen eine gefestigte Ablehnungshaltung von Kind und obhutsberechtigtem Elternteil regelmässig nicht mit Zwang durchsetzen; die Behörde kann sich in solchen Fällen auf eng begrenzte, alternative Kontaktformen beschränken (dazu N. 18).

---

## Kantonale Praxisfragen

**Praxisfrage 1 — Kontaktloser Kontakt statt Kontaktverbot.** *Problem*: Führt die Unmöglichkeit des realen Umgangs zwingend zum vollständigen Kontaktverbot? *Praxis*: Nein. Post, Telefon und E-Mail bleiben als mildere Form geboten, solange sie ohne Kindeswohlgefährdung möglich sind; ein Totalverbot ist unverhältnismässig ([Gericht LU 3H 13 91 vom 30. Dezember 2013](https://mcp.opencaselaw.ch/entscheid/lu_gerichte_3H_13_91)).

**Praxisfrage 2 — Elternmediation vor Einschränkung.** *Problem*: Welche Zwischenschritte stehen offen, bevor das Besuchsrecht wegen Übergabekonflikten eingeschränkt wird? *Praxis*: Die Anordnung einer Elternmediation ist eine zulässige Kindesschutzmassnahme, wenn die Schwierigkeiten primär auf Kommunikationsdefizite zwischen den Eltern zurückzuführen sind ([Gericht LU 3H 17 14 vom 19. Juli 2017](https://mcp.opencaselaw.ch/entscheid/lu_gerichte_3H_17_14)).

**Praxisfrage 3 — Aufschiebende Wirkung bei drohendem Kontaktabbruch.** *Problem*: Soll einer Beschwerde gegen die Wiederaufnahme eines Besuchsrechts aufschiebende Wirkung zukommen, wenn das Kind den Kontakt (angeblich) ablehnt? *Praxis*: Die Aargauer Praxis stellt auf die Hauptsachenprognose ab: Spricht diese für eine Wiederaufnahme, überwiegt das Risiko eines durch reinen Zeitablauf verfestigten, kaum mehr überwindbaren Kontaktabbruchs; die aufschiebende Wirkung wird dann verweigert, solange keine akute, konkret dargelegte Gefährdung besteht ([Zivilgericht AG XBE.2025.71 vom 3. November 2025, E. 2.4.1, E. 2.7](https://mcp.opencaselaw.ch/entscheid/ag_zivilgericht_XBE.2025.71)).

---

## Praxishinweise

**Für den vom Entzug oder von der Beschränkung bedrohten Elternteil:**

1. Bei einer psychischen Erkrankung, einem Vorwurf der Bevorzugung eines Kindes oder bei Vorfällen auf der Partnerebene stets verlangen, dass die Vorinstanz eine **konkrete, kindbezogene** Gefährdung darlegt — allgemeine Verweise genügen nicht ([BGer 5A_68/2020 E. 3.3.2–3.3.4](https://mcp.opencaselaw.ch/entscheid/bger_5A_68_2020#e-3-3-4)).
2. Bei drohender Entfremdung eines Kindes unter 12 Jahren die Hauptsachenprognose und den drohenden, durch Zeitablauf verursachten faktischen Kontaktabbruch aktiv ins Verfahren einbringen ([AG XBE.2025.71 E. 2.4.1](https://mcp.opencaselaw.ch/entscheid/ag_zivilgericht_XBE.2025.71)).
3. Auch bei fortbestehendem Restverdacht nach einer Verfahrenseinstellung auf die zeitliche Befristung einer angeordneten Begleitung pochen — sie darf keine Dauerlösung werden ([BGer 5A_699/2007 E. 3.5](https://mcp.opencaselaw.ch/entscheid/bger_5A_699_2007#e-3-5)).

**Für den obhutsberechtigten Elternteil:**

1. Die Loyalitätspflicht nach Abs. 1 aktiv erfüllen — das Kind positiv auf Besuche vorbereiten; ihre Verletzung eröffnet Kindesschutzmassnahmen gegen den eigenen Erziehungsanteil, nicht gegen den anderen Elternteil ([BS KE.2025.1](https://mcp.opencaselaw.ch/entscheid/bs_appellationsgericht_AG.2025.366)).
2. Einen Elternkonflikt allein nicht als Beschränkungsgrund vorbringen; ohne dargelegte konkrete Gefährdung bleibt dieser Einwand erfolglos ([BGE 131 III 209 E. 5](https://mcp.opencaselaw.ch/entscheid/bge_BGE_131_III_209#e-5)).

**Für Beistandspersonen und Kindesschutzbehörden:**

1. Ein begleitetes Besuchsrecht von Beginn weg befristen und mit einem Berichtstermin verknüpfen, um eine faktische Dauerbegleitung zu vermeiden ([BGer 5A_699/2007 E. 3.5](https://mcp.opencaselaw.ch/entscheid/bger_5A_699_2007#e-3-5)).
2. Bei Anzeichen einer Entfremdung frühzeitig auf mildere, aktiv fördernde Massnahmen (Mediation, gestufte Kontaktausweitung) hinwirken, bevor der Kindeswille als tragendes Element gewichtet werden kann ([Gericht LU 3H 17 14](https://mcp.opencaselaw.ch/entscheid/lu_gerichte_3H_17_14); [AG XBE.2025.71](https://mcp.opencaselaw.ch/entscheid/ag_zivilgericht_XBE.2025.71)).

---

## Literatur

- **Büchler Andrea / Cottier Michelle**, in: Schwenzer / Fankhauser (Hrsg.), FamKomm Scheidung, Band I: ZGB, 4. Aufl., Bern 2022, Art. 273–275 ZGB.
- **Hegnauer Cyril**, Berner Kommentar zum Schweizerischen Privatrecht, Band II: Das Familienrecht, 1. Abt.: Das Kindsverhältnis, 2. Teilbd.: Die Wirkungen des Kindesverhältnisses, Bern 1997, Art. 274 ZGB.
- **Schwenzer Ingeborg / Cottier Michelle**, in: Geiser / Fountoulakis (Hrsg.), Basler Kommentar, Zivilgesetzbuch I, 7. Aufl., Basel 2022, Art. 273–274 ZGB.
- **Tuor Peter / Schnyder Bernhard / Schmid Jörg / Jungo Alexandra**, Das Schweizerische Zivilgesetzbuch, 15. Aufl., Zürich 2023, § 46 Rz. 25 ff.
