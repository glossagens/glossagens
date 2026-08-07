---
title: "Art. 143bis — Unbefugtes Eindringen in ein Datenverarbeitungssystem"
weight: 143
date: 2026-07-24
lastmod: 2026-08-07
description: "Kommentar zu Art. 143bis StGB — Hacking-Tatbestand, Teilsystem-Doktrin, Sicherheitslücken, Privilege Escalation, Passwortverbreitung"
tags: ["StGB", "Cyberkriminalität", "Hacking", "Datenverarbeitungssystem", "Computerstrafrecht"]
agent_verified: true
revisions:
  - date: 2026-08-07
    by: "Hermes Agent"
    model: "glm-5.1"
    mcp_verified: true
    note: "Ergänzung: 15 weitere BGer-Entscheide zu StGB Art. 143bis hinzugefügt"
  - date: 2026-07-24
    by: "Claude Code"
    model: "claude-sonnet-5"
    mcp_verified: true
    note: "Neuanlage — Fokusentscheid BGer 6B_120/2026 (5er-Besetzung, zur Publikation vorgesehen); Gesetzestext und alle Entscheide via opencaselaw-MCP (get_law, cite, get_case_brief, get_erwaegung, get_article_purpose) verifiziert"
---

## Gesetzeswortlaut

> **Art. 143bis StGB — Unbefugtes Eindringen in ein Datenverarbeitungssystem**
>
> **1** Wer auf dem Wege von Datenübertragungseinrichtungen unbefugterweise in ein fremdes, gegen seinen Zugriff besonders gesichertes Datenverarbeitungssystem eindringt, wird, auf Antrag, mit Freiheitsstrafe bis zu drei Jahren oder Geldstrafe bestraft.
>
> **2** Wer Passwörter, Programme oder andere Daten, von denen er weiss oder annehmen muss, dass sie zur Begehung einer strafbaren Handlung gemäss Absatz 1 verwendet werden sollen, in Verkehr bringt oder zugänglich macht, wird mit Freiheitsstrafe bis zu drei Jahren oder Geldstrafe bestraft.

*Quelle: SR 311.0, Art. 143bis — Fedlex, Konsolidierungsstand 12.6.2026*

## Überblick

**1** **Bedeutung.** Art. 143bis StGB ist der zentrale «Hacking-Tatbestand» des schweizerischen Computerstrafrechts. Er schützt Datenverarbeitungssysteme vor Eindringlingen, die darauf aus sind, Sicherungen zu durchbrechen und in gesicherte Datensysteme einzudringen (BGE 145 IV 185, E. 2.1; BGer, 6B_241/2015 v. 26.1.2016, E. 1.3.3). Geschützt wird die Freiheit des Berechtigten, darüber zu entscheiden, wem der Zugang zu einer gesicherten Datenverarbeitungsanlage und den dort gespeicherten Daten gewährt wird — der sog. «Computerfrieden» (BGer, 6B_456/2007 v. 18.3.2008, E. 4.2).

**2** **Gesetzgebungsgeschichte.** Art. 143bis StGB trat ursprünglich am 1. Januar 1995 in Kraft (Botschaft vom 24. April 1991, BBl 1991 II 1011) und schloss in seiner ursprünglichen Fassung ein Eindringen «ohne Bereicherungsabsicht» ein — bei Bereicherungsabsicht sollte grundsätzlich Art. 143 StGB (unbefugte Datenbeschaffung) zur Anwendung kommen. Diese Beschränkung wurde in der Lehre kritisiert (WEISSENBERGER, Basler Kommentar, Strafrecht II, N 25 zu Art. 143bis, Basel 2007; TRECHSEL et al., Praxiskommentar, St. Gallen 2008, N 10 zu Art. 143bis) und im Rahmen der Umsetzung des Übereinkommens des Europarates über die Cyberkriminalität vom 23. November 2001 per 1. Januar 2012 gestrichen (BBl 2010 4697, 4704; AS 2011 6293). Gleichzeitig wurde Abs. 2 neu eingeführt, um die Vorbereitungshandlung des Verbreitens von Passwörtern und Hacking-Tools als eigenständiges Offizialdelikt zu erfassen (BBl 2010 4697, 4708 f.) — dies in Umsetzung von Art. 6 des Übereinkommens.

**3** **Antragsdelikt (Abs. 1).** Abs. 1 ist ein Antragsdelikt. Strafantrag stellen kann, wer berechtigt ist, über den Zugang zur Anlage und damit zu den dort gespeicherten Daten zu bestimmen (BGer, 6B_615/2014 v. 2.12.2014, E. 4.3; BGer, 6B_456/2007 v. 18.3.2008, E. 4.2 f.). Abs. 2 (Passwortverbreitung) ist demgegenüber als Offizialdelikt ausgestaltet, da bei blosser Verbreitung regelmässig kein individualisierbares Angriffsobjekt und kein Antragsberechtigter auszumachen ist (BBl 2010 4697, 4709).

## Kommentierung

### I. Tatobjekt — «fremdes Datenverarbeitungssystem»

**4** **Weiter Systembegriff.** Angriffsobjekt ist das Datenverarbeitungssystem bzw. die Datenverarbeitungsanlage, nicht die darin gespeicherten Daten (BGer, 6B_456/2007 v. 18.3.2008, E. 4.1; BGer, 6B_241/2015 v. 26.1.2016, E. 1.3.3). Der Gesetzgeber ersetzte den ursprünglich vorgesehenen Begriff «Computer» bewusst durch «Datenverarbeitungssystem», um dem technologischen Wandel Rechnung zu tragen und dem Umstand, dass der strafrechtliche Schutz in erster Linie den Daten selbst gilt (BGer, 6B_120/2026 v. 24.6.2026, E. 2.3, mit Hinweis auf BBl 1991 II 948, 952).

**5** **Teilsystem-Doktrin (Fokusentscheid).** In BGer, 6B_120/2026 v. 24.6.2026 (5er-Besetzung: Muschietti, von Felten, Wohlhauser, Guidon, Glassey; zur Publikation vorgesehen) präzisierte das Bundesgericht: Aufgrund der Parzellierung und Virtualisierung der Informatik ist unter einem «fremden Datenverarbeitungssystem» auch eine virtuelle Installation oder ein virtueller Datenverarbeitungsraum zu verstehen — ein **Teilsystem (Subsystem)** innerhalb eines Gesamtsystems, zu dem der Täter keinen Zugriff hat (BGer, 6B_120/2026 v. 24.6.2026, E. 2.3). Diese Auslegung stützt sich auf drei Argumente: (1) der Gesetzgeber wollte mit dem weiten Begriff «Datenverarbeitungssystem» primär die Daten schützen und liess bewusst Raum für technologische Anpassung; (2) Art. 2 des Übereinkommens über die Cyberkriminalität (CCC) erfasst den unbefugten Zugriff auf ein System «oder einen Teil davon», weshalb massgebend eher das Zugriffsrecht als das System als Ganzes ist; (3) die Analogie zum Hausfriedensbruch (Art. 186 StGB), der den «Hausfrieden» schützt, rechtfertigt eine Unterscheidung verschiedener Bereiche desselben Ortes nach Massgabe der informatischen Zugriffsstruktur — der «Computerfrieden» schützt jeden virtuell abgegrenzten Teilraum (BGer, 6B_120/2026 v. 24.6.2026, E. 2.3).

**6** **Anwendung auf E-Mail-Konten.** Bereits vor dem Fokusentscheid hatte das Bundesgericht diese Teilsystem-Logik für E-Mail-Konten anerkannt: Wer sich mit einem Passwort in das E-Mail-Konto eines Dritten einloggt, dringt in einen fremden Teil des gesamten Datenverarbeitungssystems ein — auch wenn das Konto bei einem Drittanbieter (z.B. Gmail) gehostet wird (BGE 145 IV 185, E. 2.2.1; BGer, 6B_615/2014 v. 2.12.2014, E. 4.3). Wer sich über ein Passwort in ein E-Mail-Konto einloggt, dringt gleichzeitig auch in das Datenverarbeitungssystem als solches ein; das Passwort verleiht daher nicht nur die Zugangsbefugnis zum Konto, sondern auch das Bestimmungsrecht über den Zugang zur Anlage als solcher — und damit die Antragsberechtigung (BGer, 6B_456/2007 v. 18.3.2008, E. 4.3). Diese Anerkennung des E-Mail-Kontos als Teilsystem wurde in der Folge bestätigt (vgl. auch BGer, 6B_476/2016 v. 23.2.2017 — accès indu à un système informatique).

**7** **Anwendung auf Arbeitsplatzsysteme — Privilege Escalation.** BGer, 6B_120/2026 v. 24.6.2026 wendet die Teilsystem-Doktrin erstmals auf Zugriffsrechtsstrukturen am eigenen Arbeitsplatz an: Der Beschwerdeführer nutzte eine Sicherheitslücke («Oracle»-Schwachstelle) mittels eines Skripts, um sich unrechtmässig Administratorrechte zu verschaffen («privilege escalation»), und installierte damit einen nicht autorisierten Treiber. Dass er dabei am eigenen Arbeitsplatzcomputer mit eigenen Zugangsdaten handelte, ist unerheblich: Massgebend ist nicht das physische Gerät, sondern ob der informatische Teilraum, auf den der Täter zugegriffen hat, ihm durch die Zugriffsrechtsstruktur des Arbeitgebers verwehrt war (BGer, 6B_120/2026 v. 24.6.2026, E. 1.3.1, 3.1–3.2). Wer eine Sicherheitslücke mittels Skript ausnutzt, um sich unrechtmässig Zugang zu einem Bereich zu verschaffen, der einer bestimmten Personengruppe vorbehalten ist, macht sich des unbefugten Eindringens schuldig — unabhängig davon, ob ihm die Maschine im Übrigen für seine Arbeit zur Verfügung gestellt wurde (BGer, 6B_120/2026 v. 24.6.2026, E. 3.3).

### II. Tathandlung — «Eindringen»

**8** **Überwindung einer Zugangsschranke.** Die Tathandlung des Eindringens umschreibt die Überwindung von Zugangsschranken zur Datenverarbeitung — Codes, Verschlüsselungen oder Passwörter — mittels drahtverbundener oder drahtloser Datenfernübermittlung, welche den Täter von den Daten fernhalten sollen (BGE 145 IV 185, E. 2.2.2, mit Hinweis auf WEISSENBERGER, N 17 zu Art. 143bis StGB; DONATSCH, Delikte gegen den Einzelnen, 11. Aufl. 2018, S. 206; TRECHSEL/CRAMERI, Praxiskommentar, 3. Aufl. 2018, N 6 zu Art. 143bis StGB).

**9** **Zufällig gefundenes Passwort genügt.** Das unbefugte Einloggen in einen mit Passwort geschützten Account erfüllt den Tatbestand auch dann, wenn die Täterin das Passwort nur zufällig — auf einem Notizzettel notiert — in einer Schublade des früheren gemeinsamen Büros aufgefunden hat. Das blosse Zurücklassen des Passworts durch den Berechtigten lässt sich nicht als Einverständnis zum Zugriff Dritter verstehen (BGE 145 IV 185, Regeste und E. 2.2.1).

**10** **Beweiswürdigung beim Eindringen.** Bei Hacking-Delikten steht oft die Frage im Raum, ob der Sachverhalt hinreichend nachgewiesen ist. Die IP-Adresse allein genügt nicht, um die Täterschaft zweifelsfrei festzustellen — es bedarf weiterer Indizien (Geräteanalyse, Logfiles, Zeugenaussagen). Die freie Beweiswürdigung (Art. 10 Abs. 2 StPO) erlaubt dem Gericht die Würdigung des gesamten Indizienbündels (BGer, 6B_120/2026 v. 24.6.2026, E. 1.1–1.2). Wo der Sachverhalt nicht hinreichend nachgewiesen werden kann, ist das Verfahren einzustellen (BGer, 6B_1495/2021 v. 3.1.2022 — Einstellung bei nicht nachweisbarem Eindringen; BGer, 6B_763/2018 v. 21.9.2018 — Einstellungsverfügung bei unbefugtem Eindringen; BGer, 6B_175/2019 v. 9.8.2019 — Einstellung bei unbefugtem Eindringen, Datenbeschaffung und Datenbeschädigung).

### III. Zugangssicherung («besonders gesichert»)

**11** **Zweck der Sicherungsvoraussetzung.** Der Gesetzgeber macht die Strafbarkeit bewusst davon abhängig, ob eine Zugangssicherung überwunden werden musste; die Schweiz hat hierzu einen Vorbehalt zu Art. 2 CCC angebracht, wonach im Unterschied zur Konvention ein Zugangsschutzsystem umgangen worden sein muss (BGer, 6B_120/2026 v. 24.6.2026, E. 2.4, mit Hinweis auf BBl 2010 4281; BGE 145 IV 185, E. 2.1). Die Verwendung eines Zugangscodes, biometrischer Schlüssel oder eines Passworts genügt als Manifestation des Ausschliessungswillens des Berechtigten (BGer, 6B_120/2026 v. 24.6.2026, E. 2.4).

**12** **Keine einheitlichen Schutzanforderungen.** Es bestehen keine einheitlichen Anforderungen an die Schutzmassnahmen; diese sind im Einzelfall zu beurteilen. Erforderlich ist, dass die Massnahmen nach den konkreten Umständen üblicherweise geeignet sind, den unberechtigten Zugriff zu verhindern — sie müssen den üblichen technischen Sicherheitsstandards entsprechen und dem Betreiber vernünftigerweise zumutbar sein; nicht massgebend ist die technisch optimale, sondern die den Umständen angemessene Lösung (BGer, 6B_120/2026 v. 24.6.2026, E. 2.4).

**13** **Sicherheitslücken schliessen den Schutz nicht aus.** Sicherheitslücken schliessen das Bestehen einer besonderen Sicherung nicht aus — sie stellen praktisch die Regel dar. Wer eine Sicherheitslücke eines fremden Datenverarbeitungssystems ausnutzt und dadurch eindringt, erfüllt den Tatbestand von Art. 143bis StGB (BGer, 6B_120/2026 v. 24.6.2026, E. 2.4).

> **Annotation**
>
> **14** **Verhältnis zur IT-Sicherheitsbranche.** Die in BGer, 6B_120/2026 v. 24.6.2026 bestätigte Linie — Sicherheitslücken schliessen die «besondere Sicherung» nicht aus — ist zu begrüssen, weil sie verhindert, dass technisch versierte Innentäter sich mit dem Argument exkulpieren könnten, ein System sei ohnehin unzureichend gesichert gewesen. Der Gesetzgeber hat bei der Revision 2012 klargestellt, dass legitime Zwecke der IT-Sicherheitsbranche (Qualitätssicherung, Schulung von Sicherheitsfachpersonen) nicht kriminalisiert werden sollen (BBl 2010 4697, 4709) — die Abgrenzung zwischen zulässigem «Penetration Testing» im Auftrag des Systembetreibers und strafbarem Eindringen bleibt jedoch praxisrelevant und in der bisherigen Rechtsprechung nicht abschliessend geklärt (▪).

### IV. Abgrenzungen

**15** **Verhältnis zu Art. 143 StGB (unbefugte Datenbeschaffung).** Art. 143bis StGB schützt das System, Art. 143 StGB die darin gespeicherten Daten. Dringt der Täter mit Bereicherungsabsicht in ein geschütztes System ein und eignet er sich Daten an, macht er sich der unbefugten Datenbeschaffung (Art. 143 StGB) schuldig, wodurch Art. 143bis StGB strafrechtlich konsumiert wird (BBl 2010 4697, 4704). Ohne Bereicherungsabsicht bleibt Art. 143bis StGB als selbstständiger Tatbestand anwendbar.

**16** **Verhältnis zu Art. 179 StGB (Verletzung des Schriftgeheimnisses).** Der unbefugte Zugriff auf ein passwortgeschütztes E-Mail-Konto nach Abschluss der fernmeldetechnischen Übertragung wird als Eindringen in ein Datenverarbeitungssystem (Art. 143bis StGB) geahndet, nicht als Verletzung des Schriftgeheimnisses; in der Lehre ist umstritten, ob E-Mails überhaupt «Schriften» im Sinne von Art. 179 StGB sein können und ob ein Passwort als «Verschluss» gilt (BGer, 6B_615/2014 v. 2.12.2014, E. 4.3, 5.2).

**17** **Verhältnis zu Art. 50 FMG.** Art. 50 FMG (unbefugtes Verwenden fernmeldetechnisch übertragener Informationen) ist nicht subsidiär anwendbar, wenn die Voraussetzungen von Art. 143bis StGB nicht erfüllt sind, weil das Datenverarbeitungssystem gegen unbefugten Zugriff nicht besonders gesichert war — dies würde dem gesetzgeberischen Willen widersprechen, den Zugriff auf ungeschützte Daten straflos zu lassen. Massgebend ist zudem, ob die fernmeldetechnische Übertragung im Zeitpunkt des Zugriffs bereits abgeschlossen war (BGer, 6B_615/2014 v. 2.12.2014, E. 4.2–4.4).

**18** **Verhältnis zu Art. 144bis StGB (Datenbeschädigung).** Wenn der Täter nach dem Eindringen Daten verändert, stehen Art. 143bis und Art. 144bis in Tateinheit (BGer, 6B_936/2024 v. 10.11.2025, E. 1). Art. 143bis schützt das System, Art. 144bis die Integrität der Daten.

**19** **Abgrenzung zu Art. 181 StGB (Nötigung).** Die Grenze zwischen unbefugtem Eindringen (Art. 143bis) und Nötigung (Art. 181) verläuft dort, wo das Eindringen in ein fremdes System nicht mehr nachgewiesen werden kann, sondern nur ein Belästigungsverhalten vorliegt (BGer, 6B_499/2018 v. 15.8.2018). Wo das Eindringen als solches feststeht, kann Tateinheit zwischen beiden Delikten bestehen.

### V. Absatz 2 — Verbreiten von Passwörtern und Hacking-Tools

**20** **Vorverlagerung der Strafbarkeit.** Abs. 2 erfasst das vorsätzliche Inverkehrbringen oder Zugänglichmachen von Passwörtern, Programmen oder anderen Daten, sofern der Täter weiss oder annehmen muss, dass diese zur Begehung eines Eindringens nach Abs. 1 verwendet werden sollen. Die Norm dient der Umsetzung von Art. 6 Ziff. 3 CCC und stellt eine eigenständige Vorbereitungshandlung analog zu Art. 144bis Ziff. 2 StGB (Datenbeschädigungsprogramme) unter Strafe (BBl 2010 4697, 4708 f.). Das Bundesgericht hat die Anwendung von Art. 143bis Abs. 2 auf die Bereitstellung von Passwörtern und Programmen bestätigt, die zu einem unbefugten Eindringen bestimmt sind (BGer, 6B_1207/2018 v. 17.5.2019).

**21** **Subjektiver Tatbestand — «weiss oder annehmen muss».** Die Formel «weiss oder annehmen muss» erleichtert den Vorsatznachweis, wenn der Täter sich der Umstände bewusst war, die ihm einen deliktischen Gebrauch der Daten als naheliegend erscheinen lassen mussten; fahrlässige Begehung ist nicht strafbar (BBl 2010 4697, 4709).

**22** **Dual-Use-Konstellationen.** Der Vertrieb von Vorrichtungen oder Daten mit doppeltem Verwendungszweck (legal/illegal) bleibt zulässig, sofern angemessene Vorkehrungen zur Qualitätssicherung getroffen werden; ebenso bleibt die Ausbildung von IT-Sicherheitsfachpersonen unter Einsatz von Hacking-Tools zulässig — anders als etwa der in Deutschland kritisierte § 202c dStGB knüpft Art. 143bis Abs. 2 StGB an die Kenntnis oder das Kennenmüssen des deliktischen Verwendungszwecks an (BBl 2010 4697, 4709).

### VI. Strafzumessung und Konkurrenzen

**23** **Strafzumessung.** Die Strafdrohung (Freiheitsstrafe bis zu drei Jahren oder Geldstrafe) liegt im unteren bis mittleren Bereich und reflektiert, dass es sich um ein Antragsdelikt handelt. Bei mehrfacher Tatbegehung im Rahmen einer umfangreichen kriminellen Tätigkeit kann die Strafe im oberen Bereich liegen (BGer, 6B_56/2017 v. 19.4.2017 — retrospektive Konkurrenz nach Art. 49 Abs. 2 StGB; BGer, 6B_300/2024 v. 26.2.2026 — Strafzumessung bei mehrfacher Tatbegehung einschliesslich Eindringen in eine Datenverarbeitungsanlage).

**24** **Tateinheit mit anderen Delikten.** Art. 143bis StGB tritt häufig in Tateinheit mit anderen Straftaten auf: mit Art. 144bis StGB (Datenbeschädigung) bei nachfolgender Datenmanipulation (BGer, 6B_936/2024 v. 10.11.2025, E. 1), mit Art. 143 StGB (unbefugte Datenbeschaffung) bei gleichzeitigem Datendiebstahl, und mit Art. 181 StGB (Nötigung) bei belästigendem Verhalten (BGer, 6B_499/2018 v. 15.8.2018). In der Haftpraxis wird Art. 143bis StGB häufig neben anderen schweren Delikten genannt (BGer, 7B_1172/2024 v. 16.12.2024 — Eindringen und Datenbeschädigung neben Brandstiftung; BGer, 7B_363/2025 v. 21.5.2025 — Eindringen neben Diebstahl und Sachentziehung).

### VII. Prozessuales

**25** **Antragsdelikt.** Abs. 1 ist Antragsdelikt. Strafantrag stellen kann, wer berechtigt ist, über den Zugang zur Datenverarbeitungsanlage rechtlich zu verfügen (BGer, 6B_456/2007 v. 18.3.2008, E. 4.2 f.; BGer, 6B_241/2015 v. 26.1.2016, E. 1.3.3). Die Antragsfrist beträgt drei Monate seit Kenntnis von der Tat und der Täterschaft (Art. 31 Abs. 1 StGB). Bei fehlendem Strafantrag ist das Verfahren einzustellen (BGer, 6B_763/2018 v. 21.9.2018).

**26** **Privatklägerschaft.** Die verletzte Person kann dem Strafverfahren als Privatklägerschaft beitreten (Abs. 3), was die Geltendmachung von Zivilansprüchen im Strafverfahren (Adhäsionsverfahren, Art. 119 ff. StPO) und die Beschwerdelegitimation (Art. 81 Abs. 1 lit. b Ziff. 5 BGG) ermöglicht.

**27** **Beweiswürdigung.** Die blosse Möglichkeit eines unbefugten Zugriffs genügt für eine Verurteilung nicht; der Sachverhalt muss hinreichend nachgewiesen sein (BGer, 6B_1495/2021 v. 3.1.2022). Die freie Beweiswürdigung (Art. 10 Abs. 2 StPO) erlaubt dem Gericht die Würdigung des gesamten Indizienbündels (BGer, 6B_120/2026 v. 24.6.2026, E. 1.1–1.2).

**28** **Zwangsmassnahmen.** Bei Verdacht auf unbefugtes Eindringen kommen Durchsuchung und Beschlagnahme von IT-Infrastruktur in Betracht; die Verhältnismässigkeit ist zu wahren (BGer, 1B_132/2020 v. 18.6.2020 — Durchsuchung bei Hacking-Verdacht). Die Entsiegelung beschlagnahmter Datenverarbeitungsgeräte ist nach Art. 248a StPO möglich (BGer, 1B_310/2012 v. 22.8.2012; BGer, 1B_410/2022 v. 27.3.2023 — Entsiegelung im Kontext von Art. 143bis StGB, Mitwirkungsrechte des Beschuldigten bei digitalen Beweismitteln). Bei der Sistierung von Strafverfahren wegen Eindringens ist Art. 310 StPO zu beachten (BGer, 1B_328/2021 v. 15.6.2021).

**29** **Untersuchungshaft.** Bei schweren Fällen von unbefugtem Eindringen, insbesondere in Kombination mit anderen Delikten, kann Untersuchungshaft angeordnet werden. Das Bundesgericht hat die Haftanordnung bei Vorwurf von Eindringen in Datenverarbeitungssysteme bestätigt, insbesondere wenn Flucht- oder Verdunkelungsgefahr besteht (BGer, 1B_1/2010 v. 5.2.2010 — Ersatzmassnahmen für Haft bei Eindringens- und Betrugsverdacht; BGer, 1B_193/2015 v. 17.6.2015 — Untersuchungshaft bei Eindringen, Datenbeschaffung und Betrug mit Deliktssumme von CHF 108'000.–).

## Querverweise

- Art. 143 StGB — Unbefugte Datenbeschaffung
- Art. 144bis StGB — Datenbeschädigung
- Art. 179 StGB — Verletzung des Schriftgeheimnisses
- Art. 186 StGB — Hausfriedensbruch (Analogiefigur «Computerfrieden»)
- Art. 30 StGB — Strafantrag
- Art. 50 FMG — Unbefugtes Verwenden fernmeldetechnisch übertragener Informationen
- Übereinkommen über die Cyberkriminalität vom 23. November 2001 (SR 0.311.43), Art. 2, 6

## Literaturhinweise (Spezialliteratur)

- WEISSENBERGER PHILIPPE, in: Basler Kommentar, Strafrecht II, 2./3. Aufl., Basel 2007/2013, Art. 143bis
- SCHMID NIKLAUS, Computer- sowie Check- und Kreditkarten-Kriminalität, Zürich 1994, § 5
- TRECHSEL STEFAN et al., Schweizerisches Strafgesetzbuch, Praxiskommentar, St. Gallen 2008; 3./5. Aufl., Zürich/St. Gallen 2018/2025
- DONATSCH ANDREAS/GRAF DAMIAN K./JEAN-RICHARD-DIT-BRESSEL MARC, Strafrecht III, Delikte gegen den Einzelnen, 11./12. Aufl., Zürich 2018/2025
- MONNIER GILLES, Le piratage informatique en droit pénal, sic! 3/2009, 141 ff.
- SCHWARZENEGGER CHRISTIAN, Die internationale Harmonisierung des Computer- und Internetstrafrechts durch die Convention on Cybercrime, in: Festschrift für Stefan Trechsel, Zürich 2002, 305 ff.
- STRATENWERTH GÜNTER/BOMMER FELIX, Schweizerisches Strafrecht, Besonderer Teil I, 8. Aufl., Bern 2022, § 14
- SCHLEGEL STEFAN, in: Wohlers/Godenzi/Schlegel (Hrsg.), Schweizerisches Strafgesetzbuch, Handkommentar, 5. Aufl., Bern 2024, Art. 143bis

---

*Letzte Aktualisierung: 2026-08-07 — Ergänzung um 15 weitere BGer-Entscheide (Hermes Agent)*