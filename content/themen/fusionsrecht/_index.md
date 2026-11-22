---
title: "Grundzüge des Fusionsrechts: Fusion, Spaltung, Umwandlung und Vermögensübertragung"
date: 2026-11-22
lastmod: 2026-11-22
description: "Systematische Einführung in das schweizerische Fusionsgesetz (FusG): Numerus clausus der Umstrukturierungen, Fusion, Spaltung, Umwandlung, Vermögensübertragung, Gesellschafter-, Gläubiger- und Arbeitnehmerschutz sowie steuer- und kartellrechtliche Schnittstellen."
tags: ["Fusionsrecht", "FusG", "Fusion", "Spaltung", "Umwandlung", "Vermögensübertragung", "Umstrukturierung", "Gesellschaftsrecht", "Universalsukzession", "Überprüfungsklage"]
typ: grundlage
kurz: "Das Fusionsgesetz stellt Unternehmen, Vereinen, Stiftungen und weiteren Rechtsträgern vier abschliessend geregelte Instrumente zur Verfügung, um ihre rechtliche Struktur anzupassen: Fusion, Spaltung, Umwandlung und Vermögensübertragung. Kernvorteil gegenüber einer Einzelübertragung von Vermögenswerten ist die Universalsukzession: Aktiven, Passiven und Verträge gehen mit dem Handelsregistereintrag von Gesetzes wegen als Ganzes oder gemäss Inventar auf den übernehmenden Rechtsträger über. Zum Ausgleich schützt das Gesetz Minderheitsgesellschafter, Gläubiger und Arbeitnehmende durch Kontinuitätsregeln, Sicherstellungsansprüche und besondere Klagen."
sachgebiete: [schuldrecht.gesellschaft, schuldrecht.arbeit, steuern.einkommen_vermoegen]
normen:
  - { gesetz: fusg, art: art-001 }
  - { gesetz: fusg, art: art-003 }
  - { gesetz: fusg, art: art-007 }
  - { gesetz: fusg, art: art-018 }
  - { gesetz: fusg, art: art-022 }
  - { gesetz: fusg, art: art-023 }
  - { gesetz: fusg, art: art-029 }
  - { gesetz: fusg, art: art-053 }
  - { gesetz: fusg, art: art-069 }
  - { gesetz: fusg, art: art-073 }
  - { gesetz: fusg, art: art-103 }
  - { gesetz: fusg, art: art-105 }
  - { gesetz: fusg, art: art-106 }
  - { gesetz: fusg, art: art-108 }
  - { gesetz: or, art: art-333 }
  - { gesetz: dbg, art: art-019 }
  - { gesetz: dbg, art: art-061 }
  - { gesetz: sthg, art: art-024 }
  - { gesetz: kg, art: art-009 }
stichworte: ["Fusionsgesetz", "FusG", "Fusion", "Absorptionsfusion", "Kombinationsfusion", "erleichterte Fusion", "Spaltung", "Aufspaltung", "Abspaltung", "Umwandlung", "Vermögensübertragung", "Universalsukzession", "Kontinuitätsprinzip", "Überprüfungsklage", "Gläubigerschutz", "Arbeitnehmerschutz", "Umstrukturierung"]
revisions:
  - date: 2026-11-22
    by: "Antigravity"
    model: "gemini-4-neon"
    note: "Erstfassung nach Skill glossagens-themen (Typ grundlage). Normtexte Art. 1, 3, 29, 53 und 69 FusG per {{< wortlaut >}} (scripts/wortlaut.py); alle übrigen zitierten Bestimmungen aus FusG, OR, DBG, StHG, KG und IPRG über fedlex-connector geprüft. Zwölf Leitentscheide als Volltext-HTML von entscheidsuche.ch geladen und Anker sowie wörtliche Zitate (bei französischsprachigen Entscheiden ausschliesslich aus der deutschen Regeste bzw. als Paraphrase) abgeglichen; Curia Vista auf parlament.ch geprüft."
---

## Überblick {#ueberblick}

Das Bundesgesetz über Fusion, Spaltung, Umwandlung und Vermögensübertragung (Fusionsgesetz, FusG; SR 221.301) vom 3. Oktober 2003, in Kraft seit 1. Juli 2004, ordnet die zivilrechtlichen Möglichkeiten zur Strukturanpassung von Unternehmen, Vereinen, Stiftungen und bestimmten weiteren Rechtsträgern in einem eigenen Spezialgesetz. Bis zum Inkrafttreten des FusG waren lediglich die Fusion von Aktiengesellschaften und Genossenschaften rudimentär im Obligationenrecht geregelt (aArt. 748 f. OR). Das Bundesgericht bezeichnet das Fusionsgesetz deshalb als Anwendungsfall einer *Dekodifikation*: Inhaltlich gehört das Fusionsrecht zum Gesellschaftsrecht, wurde seines Umfangs wegen aber in ein eigenständiges Gesetz ausgelagert ([BGE 151 III 212](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_005_BGE-151-III-212_2025.html#consideration_2.4.3) E. 2.4.3).

Das Gesetz stellt vier Transaktionsformen bereit, die sich nach Rechtsfolge für die beteiligten Rechtsträger und nach dem Schicksal von Vermögen und Mitgliedschaft unterscheiden:

| Transaktionsform | Kernvorgang | Schicksal des übertragenden Rechtsträgers | Vermögensübergang | Mitgliedschaftliche Kontinuität |
|---|---|---|---|---|
| **Fusion** (Art. 3–28 FusG) | Zusammenschluss zweier oder mehrerer Rechtsträger durch Absorption oder Kombination | Auflösung ohne Liquidation, Löschung im Handelsregister | Gesamt-Universalsukzession aller Aktiven und Passiven (Art. 22 Abs. 1 FusG) | Grundsatz der Kontinuität (Art. 7 FusG); Wahlrecht oder Abfindung möglich (Art. 8 FusG) |
| **Spaltung** (Art. 29–52 FusG) | Aufspaltung auf mindestens zwei oder Abspaltung auf mindestens einen anderen Rechtsträger | Bei Aufspaltung: Auflösung ohne Liquidation; bei Abspaltung: Fortbestand | Partielle Universalsukzession gemäss Inventar (Art. 52 FusG) | Kontinuität bei symmetrischer oder asymmetrischer Spaltung (Art. 31 FusG) |
| **Umwandlung** (Art. 53–68 FusG) | Wechsel des Rechtskleids eines Rechtsträgers (z. B. GmbH in AG) | Identität wahrender Fortbestand in neuer Rechtsform | Kein Vermögensübergang (Rechtsträger bleibt identisch) | Grundsatz der Kontinuität der Anteils- und Mitgliedschaftsrechte (Art. 56 FusG) |
| **Vermögensübertragung** (Art. 69–77 FusG) | Übertragung eines Vermögens oder eines Teilvermögens auf einen anderen Rechtsträger | Fortbestand (keine Auflösung kraft Transaktion) | Partielle Universalsukzession gemäss Inventar (Art. 73 Abs. 2 FusG) | Keine mitgliedschaftliche Beteiligung (reine Vermögenstransaktion mit oder ohne Gegenleistung) |

## Rechtsgrundlagen und Systematik {#rechtsgrundlagen}

### Geltungsbereich und erfasste Rechtsträger {#geltungsbereich}

{{< wortlaut gesetz="fusg" art="art-001" >}}

Das FusG erfasst gemäss Art. 2 lit. a FusG Gesellschaften (Kapitalgesellschaften, Kollektiv- und Kommanditgesellschaften, Vereine und Genossenschaften), Stiftungen, im Handelsregister eingetragene Einzelunternehmen, Kommanditgesellschaften für kollektive Kapitalanlagen, Investmentgesellschaften mit variablem Kapital (SICAV) sowie Institute des öffentlichen Rechts. Für einzelne Kategorien sieht das Gesetz Sonderregeln vor, namentlich für Stiftungen (Art. 78–87 FusG), für Vorsorgeeinrichtungen (Art. 88–98 FusG) und für Institute des öffentlichen Rechts (Art. 99–101 FusG).

### Numerus clausus der Umstrukturierungen {#numerus-clausus}

Im Unterschied zum früheren Recht, unter dem das Bundesgericht vereinzelt gesetzlich nicht vorgesehene Fusionen und Umwandlungen zugelassen hatte, gilt unter dem FusG ein strenger *Numerus clausus*: «Das Gesetz sieht einen Numerus clausus zulässiger Umstrukturierungen und insbesondere einen Numerus clausus zulässiger Fusionen vor» ([BGE 148 III 362](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_005_BGE-148-III-362_2022.html#consideration_6.1) E. 6.1). Das FusG ordnet die zulässigen Strukturanpassungen abschliessend und knüpft sie an die jeweiligen Rechtsformen (Art. 4, Art. 30, Art. 54 FusG). Was nicht ausdrücklich als Fusion, Spaltung oder Umwandlung zugelassen ist, bleibt unzulässig und ist nicht im Handelsregister eintragungsfähig.

Diese Schranke greift auch bei Beteiligung öffentlich-rechtlicher Körperschaften oder Anstalten. In [BGE 132 III 470](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_005_BGE-132-III-470_2006.html#consideration_3.3) E. 3.3 hielt das Bundesgericht fest, dass die «Grundordnung der privatrechtlichen Gesellschaftsformen, die auf einem Numerus clausus der Formen und den Grundsätzen des Formenzwangs und der Formenfixierung beruht», eine Gleichsetzung der SBB als spezialgesetzlicher Aktiengesellschaft des öffentlichen Rechts mit einer privatrechtlichen AG ausschliesst. Da Art. 99 Abs. 1 FusG lediglich die Übernahme eines Instituts des öffentlichen Rechts durch einen privatrechtlichen Rechtsträger vorsieht, nicht aber den umgekehrten Vorgang, durfte die SBB ihre Tochtergesellschaft (Etzelwerk AG) nicht durch Absorptionsfusion übernehmen; für den umgekehrten Weg verweist Art. 99 Abs. 2 FusG auf die Vermögensübertragung (E. 4.2, E. 5.2).

Die Rechtsprechung wendet den *Numerus clausus* auch bei Verfahrensvereinfachungen konsequent an: In [BGE 148 III 362](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_005_BGE-148-III-362_2022.html#consideration_6.4) E. 6.4 stellte das Bundesgericht klar, dass eine erleichterte Schwesternfusion nach Art. 23 Abs. 1 lit. b FusG voraussetzt, dass der übergeordnete Rechtsträger bzw. die Personengruppe sämtliche stimmberechtigten Anteile *direkt* besitzt. Indirekte Beteiligungen über eine Zwischengesellschaft genügen nicht – «Ein solcher Formalismus ist nicht Selbstzweck, sondern steht im Dienste von Rechtsklarheit, Rechtssicherheit und Transparenz. Genau dies soll das Fusionsgesetz gewährleisten» ([BGE 148 III 362](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_005_BGE-148-III-362_2022.html#consideration_6.2) E. 6.2).

## Grundprinzipien des Fusionsgesetzes {#grundprinzipien}

Das Fusionsgesetz baut auf vier tragenden Strukturprinzipien auf:

1. **Universalsukzession (Gesamtnachfolge) und partielle Universalsukzession**: Bei der Fusion gehen mit der Eintragung ins Handelsregister sämtliche Aktiven und Passiven der übertragenden Gesellschaft von Gesetzes wegen auf die übernehmende Gesellschaft über (Art. 22 Abs. 1 FusG). Einzelne Abtretungen (Zessionen), Schuldübernahmen oder Grundbuchverfügungen sind vor der Eintragung nicht nötig; Eigentum, Forderungen und Verpflichtungen wechseln *uno actu*. Bei Spaltung (Art. 52 FusG) und Vermögensübertragung (Art. 73 Abs. 2 FusG) tritt eine *partielle Universalsukzession* ein: Es gehen genau jene Aktiven und Passiven von Gesetzes wegen über, die im Inventar des Spaltungs- oder Übertragungsvertrags bezeichnet sind. Wie das Bundesgericht betont, bezieht sich das Wort *partiell* «nur auf den Umfang der Universalsukzession, nicht auf deren Rechtswirkungen» ([BGE 152 II 375](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_004_BGE-152-II-375_2026.html#consideration_2.1.4) E. 2.1.4).
2. **Kontinuität der Anteils- und Mitgliedschaftsrechte**: Wer vor der Umstrukturierung Gesellschafter der übertragenden Gesellschaft war, soll diese Stellung wert- und einflussmässig an der übernehmenden Gesellschaft behalten (Art. 7 Abs. 1, Art. 31 Abs. 1, Art. 56 Abs. 1 FusG). Ausnahmsweise lässt das Gesetz bei Fusionen eine Abfindung zu (Art. 8 FusG), knüpft den Ausschluss von Minderheiten aber an ein hohes Quorum (90 % der stimmberechtigten Gesellschafter, Art. 18 Abs. 5 FusG) und an die gerichtliche Überprüfungsklage nach Art. 105 FusG.
3. **Schutz von Gläubigern und Arbeitnehmenden**: Weil bei der Fusion, Spaltung und Vermögensübertragung Vermögen ohne Zustimmung der einzelnen Gläubiger verschoben wird, sichert das Gesetz deren Position durch Schuldenrufe, Sicherstellungsansprüche und subsidiäre bzw. solidarische Haftung der beteiligten Rechtsträger. Für Arbeitnehmende verweist das FusG durchgehend auf Art. 333 OR (automatischer Übergang der Arbeitsverhältnisse) und Art. 333a OR (Informations- und Konsultationspflicht).
4. **Transparenz und KMU-Erleichterungen**: Grundsätzlich verlangen Fusion, Spaltung und Umwandlung schriftliche Transaktionsverträge oder -pläne, einen erläuternden Bericht des obersten Leitungsorgans, die Prüfung durch eine zugelassene Revisionsexpertin oder einen zugelassenen Revisionsexperten sowie ein 30-tägiges Einsichtsrecht der Gesellschafter vor der Beschlussfassung. Kleine und mittlere Unternehmen (KMU) im Sinne von Art. 2 lit. e FusG können mit Zustimmung *aller* Gesellschafterinnen und Gesellschafter auf Bericht, Prüfung und Einsichtsrecht verzichten (Art. 14 Abs. 2, Art. 15 Abs. 2, Art. 16 Abs. 2 FusG; analog für Spaltung und Umwandlung).

## Die vier Transaktionsformen {#transaktionsformen}

### Fusion (Art. 3–28 FusG) {#fusion}

{{< wortlaut gesetz="fusg" art="art-003" >}}

Das Gesetz unterscheidet zwei Fusionsarten: Bei der **Absorptionsfusion** (Art. 3 Abs. 1 lit. a FusG) übernimmt eine bestehende Gesellschaft eine oder mehrere andere Gesellschaften; bei der **Kombinationsfusion** (Art. 3 Abs. 1 lit. b FusG) schliessen sich zwei oder mehrere Gesellschaften zu einer neuen Gesellschaft zusammen. In beiden Fällen werden die übertragenden Gesellschaften aufgelöst und im Handelsregister gelöscht (Art. 3 Abs. 2, Art. 21 Abs. 3 FusG).

Der Ablauf einer ordentlichen Fusion gliedert sich in folgende Schritte:

1. **Abschluss des Fusionsvertrags** durch die obersten Leitungs- oder Verwaltungsorgane (Art. 12 f. FusG) samt aktuellem Bilanzstichtag; liegt der Stichtag mehr als sechs Monate zurück oder sind wichtige Änderungen eingetreten, ist ein Zwischenabschluss erforderlich (Art. 11 Abs. 1 FusG).
2. **Fusionsbericht und Prüfung** durch eine zugelassene Revisionsexpertin oder einen zugelassenen Revisionsexperten (Art. 14 f. FusG), vorbehältlich eines KMU-Verzichts sämtlicher Gesellschafter.
3. **Einsichtsrecht und Konsultation**: Während 30 Tagen vor dem Fusionsbeschluss können die Gesellschafter die Unterlagen einsehen (Art. 16 FusG); die Arbeitnehmervertretung ist rechtzeitig vor der Beschlussfassung zu informieren und gegebenenfalls zu konsultieren (Art. 28 FusG i.V.m. Art. 333a OR).
4. **Fusionsbeschluss und öffentliche Beurkundung**: Die Generalversammlung beschliesst die Fusion mit qualifiziertem Mehr — bei der AG und Kommandit-AG mit mindestens zwei Dritteln der vertretenen Aktienstimmen und der absoluten Mehrheit des vertretenen Aktiennennwerts (Art. 18 Abs. 1 lit. a FusG), bei der Abfindungsfusion mit Zustimmung von mindestens 90 % der stimmberechtigten Gesellschafter der übertragenden Gesellschaft (Art. 18 Abs. 5 FusG). Der Beschluss bedarf der öffentlichen Beurkundung (Art. 20 Abs. 1 FusG).
5. **Eintragung ins Handelsregister**: Mit dem Eintrag wird die Fusion rechtswirksam und bewirkt die Universalsukzession nach Art. 22 Abs. 1 FusG.

Für verbundene Kapitalgesellschaften (Mutter-Tochter-Fusion bei 100 % direktem Anteilsbesitz oder Schwesternfusion unter demselben direkten Alleineigentümer nach Art. 23 Abs. 1 FusG; sowie bei mindestens 90 % Beteiligung nach Art. 23 Abs. 2 FusG) erlaubt Art. 24 FusG eine **erleichterte Fusion**: Fusionsbericht, Prüfung, Einsichtsrecht und – bei 100 % – sogar der Generalversammlungsbeschluss entfallen.

Die Universalsukzession nach Art. 22 Abs. 1 FusG erfasst das gesamte Zivilvermögen und grundsätzlich auch zivilprozessuale Parteirollen (Art. 83 ZPO). Im Strafprozess stösst sie jedoch an Grenzen: Nach [BGE 140 IV 162](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-140-IV-162_2014.html#consideration_4.4) E. 4.4 «führt die privatrechtliche Universalsukzession aufgrund von Art. 22 Abs. 1 FusG nicht (per se) zur Parteistellung der übernehmenden Gesellschaft im Strafprozess», da eine Fusion primär auf einem rechtsgeschäftlichen Akt und nicht auf gesetzlicher Subrogation im Sinne von Art. 121 Abs. 2 StPO beruht (E. 4.9.5).

### Spaltung (Art. 29–52 FusG) {#spaltung}

{{< wortlaut gesetz="fusg" art="art-029" >}}

Die Spaltung ist das Gegenstück zur Fusion und kennt zwei Grundformen: Bei der **Aufspaltung** (Art. 29 lit. a FusG) teilt eine Gesellschaft ihr gesamtes Vermögen auf mindestens zwei andere Gesellschaften auf und wird aufgelöst; bei der **Abspaltung** (Art. 29 lit. b FusG) überträgt sie nur Teile ihres Vermögens auf eine oder mehrere andere Gesellschaften und besteht selbst fort. In beiden Fällen erhalten die Gesellschafter der übertragenden Gesellschaft Anteile an den übernehmenden Gesellschaften (Art. 31 FusG) — entweder im bisherigen Verhältnis (*symmetrische Spaltung*) oder abweichend davon (*asymmetrische Spaltung*, Art. 31 Abs. 2 lit. b FusG, wofür nach Art. 43 Abs. 2 FusG die Zustimmung von mindestens 90 % der stimmberechtigten Gesellschafter erforderlich ist).

Zentrales Dokument ist der Spaltungsvertrag (bei Übernahme durch bestehende Gesellschaften) bzw. der Spaltungsplan (bei Neugründung, Art. 36 FusG), der ein genaues **Inventar** der zu übertragenden Aktiven und Passiven enthält (Art. 37 lit. b FusG). Lässt sich ein Gegenstand des Aktivvermögens nicht zuordnen, steht er bei der Aufspaltung allen übernehmenden Gesellschaften nach dem Verhältnis des zugefallenen Nettovermögens zu und verbleibt bei der Abspaltung bei der übertragenden Gesellschaft (Art. 38 Abs. 1 FusG). Für nicht zugeordnete Passiven haften alle an der Spaltung beteiligten Gesellschaften solidarisch (Art. 38 Abs. 3 FusG).

Im Unterschied zur Fusion findet der **Gläubigerschutz vor dem Spaltungsbeschluss** statt (Art. 45 f. FusG). Während hängiger Verfahren folgt bei der Abspaltung die prozessuale Parteistellung nach [BGE 152 II 375](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_004_BGE-152-II-375_2026.html#consideration_2.1.4) E. 2.1.4 im Grundsatz dem inventarisierten Streitgegenstand; betrifft eine behördliche Anordnung (wie eine FINMA-Liquidationsverfügung) das Gesamtvermögen, tritt die abgespaltene Gesellschaft von Gesetzes wegen als weitere Partei in das Verfahren ein (E. 2.2).

### Umwandlung (Art. 53–68 FusG) {#umwandlung}

{{< wortlaut gesetz="fusg" art="art-053" >}}

Bei der Umwandlung wechselt ein Rechtsträger lediglich sein rechtliches Kleid, ohne seine wirtschaftliche oder rechtliche Identität zu verlieren. Es findet weder eine Liquidation noch eine Vermögensübertragung statt; alle Verträge, Arbeitsverhältnisse und Schulden laufen am selben Rechtssubjekt weiter. Zulässig sind die in Art. 54 FusG aufgezählten Rechtsformwechsel (z. B. von einer GmbH in eine AG, von einer Kollektiv- oder Kommanditgesellschaft in eine Kapitalgesellschaft oder Genossenschaft, oder von einem Verein in eine Kapitalgesellschaft oder Genossenschaft).

Das Verfahren entspricht im Grundsatz jenem von Fusion und Spaltung: Umwandlungsplan (Art. 59 f. FusG), gegebenenfalls Zwischenabschluss nach der Sechsmonatsfrist (Art. 58 Abs. 1 FusG), Umwandlungsbericht und Prüfung (Art. 61 f. FusG, mit KMU-Verzichtsmöglichkeit), 30-tägiges Einsichtsrecht (Art. 63 FusG), öffentlich beurkundeter Umwandlungsbeschluss mit qualifiziertem Mehr (Art. 64 f. FusG) und konstitutive Handelsregistereintragung (Art. 67 FusG). Die Gesellschafter behalten grundsätzlich gleichwertige Anteile (Art. 56 FusG).

### Vermögensübertragung (Art. 69–77 FusG) {#vermoegensuebertragung}

{{< wortlaut gesetz="fusg" art="art-069" >}}

Die Vermögensübertragung ist das flexible Auffanginstrument des FusG: Jeder im Handelsregister eingetragene Rechtsträger (auch Einzelunternehmen, Stiftungen oder Institute des öffentlichen Rechts) kann Vermögen oder Teilvermögen durch schriftlichen Vertrag samt Inventar auf einen anderen Rechtsträger übertragen (Art. 69 f. FusG). Werden Grundstücke mitübertragen, bedürfen die entsprechenden Vertragsteile einer einzigen öffentlichen Beurkundung am Sitz des übertragenden Rechtsträgers (Art. 70 Abs. 2 FusG).

Anders als bei Fusion, Spaltung und Umwandlung beschliesst allein das oberste Leitungs- oder Verwaltungsorgan über den Vertrag (Art. 70 Abs. 1 FusG); ein Generalversammlungsbeschluss ist gesetzlich nicht vorgesehen (vorbehältlich einer Information im Anhang zur Jahresrechnung nach Art. 74 FusG oder faktischer Zweckänderungen nach allgemeinem Gesellschaftsrecht). Mit dem Handelsregistereintrag gehen die im Inventar aufgeführten Aktiven und Passiven per partieller Universalsukzession auf den übernehmenden Rechtsträger über (Art. 73 Abs. 2 FusG).

Gerade weil nicht das gesamte Unternehmen untergeht, löst die Vermögensübertragung eines Teilvermögens auch öffentlich-rechtliche Rechtsnachfolgen aus, soweit das Spezialgesetz daran anknüpft: In [BGE 146 II 73](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_004_BGE-146-II-73_2020.html#consideration_2.3.3) E. 2.3.3 bestätigte das Bundesgericht im Anschluss an Art. 69 ff. FusG, dass die Übertragung eines Teilbetriebs (Taxibetrieb mit Fahrzeugen und Bewilligung) nach Art. 16 Abs. 2 MWSTG eine *partielle mehrwertsteuerliche Steuernachfolge* für die mit diesem Teilvermögen zusammenhängenden Steuerschulden bewirken kann.

## Schutzmechanismen und Rechtsbehelfe {#schutzmechanismen}

### Gesellschafterschutz und Überprüfungsklage {#ueberpruefungsklage}

Verletzt eine Fusion, Spaltung oder Umwandlung die Vorgaben zur Wahrung der Anteils- oder Mitgliedschaftsrechte oder ist eine Abfindung nicht angemessen, steht jeder betroffenen Gesellschafterin und jedem betroffenen Gesellschafter innerhalb von **zwei Monaten** nach Veröffentlichung des Transaktionsbeschlusses die **Überprüfungsklage** nach Art. 105 Abs. 1 FusG offen. Diese Klage bremst die Transaktion nicht (keine Registersperre), sondern «dient der wirtschaftlichen Korrektur einer Verletzung des Prinzips der Kontinuität der Mitgliedschaft» ([BGE 135 III 603](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_005_BGE-135-III-603_2009.html#consideration_2.1.2) E. 2.1.2). Das Urteil wirkt *erga omnes* für alle Gesellschafter in gleicher Rechtsstellung (Art. 105 Abs. 2 FusG).

Zur Ausgestaltung dieser Klage hat das Bundesgericht mehrere Leitlinien präzisiert:

- **Sachliche Zuständigkeit**: Da das FusG materiell Gesellschaftsrecht bildet, fällt die Überprüfungsklage nach Art. 105 Abs. 1 FusG unter die Streitigkeiten aus dem Recht der Handelsgesellschaften im Sinne von Art. 6 Abs. 4 lit. b ZPO und damit – bei Erreichen der kantonalen Streitwertgrenze – in die Zuständigkeit des Handelsgerichts ([BGE 151 III 212](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_005_BGE-151-III-212_2025.html#consideration_2.4.3) E. 2.4.3–2.4.4).
- **Edition des Bewertungsgutachtens**: Die klagende Partei trägt die Beweislast für die Unangemessenheit und darf alle Beweismittel heranziehen. In [BGE 134 III 255](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_005_BGE-134-III-255_2008.html#consideration_2.3) E. 2.3–2.4 stellte das Bundesgericht klar, dass sich aus Art. 14 und 16 FusG kein generelles Geheimhaltungsprivileg für den Unternehmensbewertungsbericht ableiten lässt; die Gesellschaft muss ihn im Prozess grundsätzlich offenlegen, vorbehältlich substantiiert dargetaner Geschäftsgeheimnisse (E. 2.5).
- **Kostenprivileg und seine Grenzen**: Nach Art. 105 Abs. 3 FusG trägt grundsätzlich der übernehmende Rechtsträger die Verfahrenskosten, sofern nicht besondere Umstände eine Kostenauflage an die Kläger rechtfertigen. Dieses Privileg schützt indes nicht, wer Aktien erst nach Bekanntgabe der Abfindung erwirbt, da er «wirtschaftlich betrachtet nur das Recht auf die Abfindung und nicht eine Gesellschafterstellung erwirbt, welche ihm durch die Fusion entzogen werden könnte» ([BGE 135 III 603](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_005_BGE-135-III-603_2009.html#consideration_2.4) E. 2.4). Ebenso greift Art. 105 Abs. 3 FusG vor Bundesgericht nur eingeschränkt, wenn der Kläger ein erhebliches eigenes finanzielles Interesse verfolgt ([BGE 137 III 577](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_005_BGE-137-III-577_2011.html#consideration_8.4) E. 8.4).

Bei schwerwiegenden Gesetzesverletzungen ermöglicht Art. 106 Abs. 1 FusG Gesellschaftern, die nicht zugestimmt haben, innerhalb von **zwei Monaten** nach der Veröffentlichung im SHAB die **Anfechtungsklage**; kann ein Mangel behoben werden, räumt das Gericht zunächst eine Frist zur Heilung ein (Art. 107 Abs. 1 FusG). Zudem haften mitwirkende Personen und Prüfer für absichtliche oder fahrlässige Pflichtverletzungen nach Art. 108 FusG (vgl. im Aktienrecht [Art. 754 OR](/kommentar/or/art-754/)).

### Gläubigerschutz {#glaeubigerschutz}

Je nach Transaktionsform greift der Gläubigerschutz zu einem anderen Zeitpunkt:

- **Fusion**: Nachgelagerter Gläubigerschutz. Die beteiligten Gesellschaften rufen ihre Gläubiger nach Rechtswirksamkeit dreimal im SHAB auf (verzichtbar bei Bestätigung durch eine zugelassene Revisionsexpertin oder einen zugelassenen Revisionsexperten); Gläubiger können innerhalb von **drei Monaten** Sicherstellung verlangen, sofern die Erfüllung ihrer Forderung durch die Fusion gefährdet ist (Art. 25 FusG). Persönliche Haftungen von Gesellschaftern der übertragenden Gesellschaft bestehen für vorbestehende Schulden fort (Art. 26 FusG).
- **Spaltung**: Vorgelagerter Gläubigerschutz. Alle beteiligten Gesellschaften müssen ihre Gläubiger vor dem Spaltungsbeschluss dreimal im SHAB auffordern, innert **zwei Monaten** Sicherstellung zu verlangen (Art. 45 f. FusG). Nach Vollzug haften die übrigen beteiligten Gesellschaften für Forderungen, die von der primär zugewiesenen Gesellschaft nicht befriedigt werden, **subsidiär solidarisch** (Art. 47 FusG).
- **Vermögensübertragung**: Die bisherigen Schuldner haften für vor der Übertragung begründete Schulden während **dreier Jahre** solidarisch mit dem neuen Schuldner (Art. 75 Abs. 1 FusG); entfällt diese Solidarhaftung vorzeitig oder wird eine Gefährdung nachgewiesen, besteht Anspruch auf Sicherstellung (Art. 75 Abs. 3 FusG).
- **Umwandlung**: Weil das Haftungssubstrat unverändert bleibt, bedarf es grundsätzlich keines besonderen Gläubigerschutzes; einzig bisherige persönliche Gesellschafterhaftungen dauern für Altverbindlichkeiten fort (Art. 68 Abs. 1 FusG).

### Arbeitnehmerschutz {#arbeitnehmerschutz}

Für alle Strukturänderungen mit Rechtsträgerwechsel (Fusion, Spaltung, Vermögensübertragung) verweist das FusG auf Art. 333 OR und Art. 333a OR (Art. 27 f., Art. 49 f., Art. 76 f. FusG). Danach gehen sämtliche betroffenen Arbeitsverhältnisse im Zeitpunkt des Vollzugs mit allen Rechten und Pflichten von Gesetzes wegen auf den übernehmenden Rechtsträger über, sofern die Arbeitnehmerin oder der Arbeitnehmer den Übergang nicht ablehnt; der bisherige und der neue Arbeitgeber haften zudem solidarisch für fällige Forderungen (Art. 333 Abs. 1 und 3 OR).

In [BGE 132 III 32](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_005_BGE-132-III-32_2006.html#consideration_4.2) E. 4.1–4.2 bestätigte das Bundesgericht für die Aufteilung einer Gesellschaft (Spaltung), dass der gesetzliche Übergang nach Art. 333 Abs. 1 OR zwingend ist und weder durch Vereinbarung zwischen altem und neuem Arbeitgeber noch durch einen konzerninternen Personalverleihvertrag umgangen werden kann (E. 5); die solidarische Haftung nach Art. 333 Abs. 3 OR erfasst auch Leistungen aus einem vom früheren Arbeitgeber errichteten Sozialplan (E. 6.2). Werden die Konsultationspflichten nach Art. 333a OR vor dem Transaktionsbeschluss missachtet, kann die Arbeitnehmervertretung eine gerichtliche **Registersperre** verlangen (Art. 28 Abs. 3 FusG; ebenso bei Spaltung und Vermögensübertragung).

## Abgrenzungen und Schnittstellen {#abgrenzungen}

### Steuerrechtliche Umstrukturierungsneutralität {#steuerrecht}

Zivilrechtliche Zulässigkeit nach dem FusG und steuerliche Neutralität fallen nicht automatisch zusammen. Während das FusG Umstrukturierungen weitgehend zulässt, knüpfen Art. 19 DBG (Personenunternehmungen), Art. 61 DBG (juristische Personen) und Art. 24 Abs. 3 und 3quater StHG die steuerneutrale Übertragung stiller Reserven an eigenständige Voraussetzungen: Fortbestand der Steuerpflicht in der Schweiz, Übernahme der bisherigen Gewinnsteuer- bzw. Einkommenssteuerwerte sowie – insbesondere bei der Einbringung einer Personenunternehmung in eine juristische Person und bei der Spaltung – das **Betriebserfordernis** (Übertragung eines Betriebs oder Teilbetriebs).

In [BGE 142 II 283](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_004_BGE-142-II-283_2016.html#consideration_3.2) E. 3.2 hielt das Bundesgericht fest, als Betrieb im Sinne des steuerlichen Umstrukturierungsrechts gelte «jeder organisatorisch-technische Komplex von Vermögenswerten, der im Hinblick auf die unternehmerische Leistungserbringung eine relativ unabhängige, organische Einheit bildet». Blosses Geschäftsvermögen – im konkreten Fall einige Stockwerkeigentumseinheiten und Tiefgaragenplätze einer Kollektivgesellschaft ohne fortgesetzte eigene Leistungserbringung – genügt dem Betriebserfordernis von Art. 19 Abs. 1 lit. b DBG nicht und löst bei der Vermögensübertragung auf eine AG die Besteuerung der stillen Reserven aus (E. 4.2–4.3).

Für kantonale und kommunale **Handänderungsabgaben** enthält Art. 103 FusG ein direkt anwendbares bundesrechtliches Erhebungsverbot bei Umstrukturierungen im Sinne von Art. 8 Abs. 3 und Art. 24 Abs. 3 und 3quater StHG (unter Vorbehalt kostendeckender Gebühren). Wie das Bundesgericht in [BGE 138 II 557](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_004_BGE-138-II-557_2012.html#consideration_4.2) E. 4.2 festhielt, bedarf Art. 103 FusG keiner kantonalen Konkretisierung, und das kantonale Recht darf nicht davon abweichen; eine konzerninterne Vermögensübertragung ist selbst dann von der Handänderungssteuer befreit, wenn die übernehmende Einheit eine steuerbefreite Vorsorgestiftung ist (E. 7.5).

### Kartellrecht und internationales Privatrecht {#kartellrecht-iprg}

Erreicht ein Zusammenschluss (Fusion oder Übernahme der Kontrolle) die Umsatzschwellen des Art. 9 KG (weltweit mindestens 2 Milliarden Franken oder auf die Schweiz entfallend mindestens 500 Millionen Franken, sowie mindestens zwei beteiligte Unternehmen mit je mindestens 100 Millionen Franken Umsatz in der Schweiz) oder betrifft er eine bereits rechtskräftig festgestellte marktbeherrschende Stellung, ist das Vorhaben vor dem Vollzug der Wettbewerbskommission zu melden (Art. 9 Abs. 1 und 4 KG). Die zivilrechtliche Wirksamkeit von Fusion und Vermögensübertragung steht ausdrücklich unter dem Vorbehalt von Art. 34 KG (Art. 22 Abs. 1 und Art. 73 Abs. 2 FusG).

Für **grenzüberschreitende Umstrukturierungen** verweist das FusG auf das IPRG: Die Art. 163a–164b IPRG regeln Immigrations- und Emigrationsfusionen (z. B. Übernahme einer ausländischen Gesellschaft durch eine schweizerische Gesellschaft nach Art. 163a IPRG) sowie grenzüberschreitende Spaltungen und Vermögensübertragungen, sofern auch das beteiligte ausländische Gesellschaftsstatut die Transaktion zulässt.

## Praxishinweise {#praxishinweise}

- **Rechtsform-Check vor der Strukturwahl**: Prüfen Sie anhand von Art. 4, 30 und 54 FusG zuerst, ob die gewünschte Transaktion zwischen den beteiligten Rechtsformen zulässig ist. Scheitert eine Fusion oder Umwandlung am *Numerus clausus* (etwa bei Beteiligung öffentlich-rechtlicher Institute oder bestimmter Stiftungen), steht häufig die **Vermögensübertragung** (Art. 69 ff. FusG) als Ersatzinstrument offen.
- **Direkte Beteiligung für erleichterte Fusionen**: Soll konzernintern nach Art. 23 Abs. 1 FusG ohne Generalversammlungsbeschluss, Fusionsbericht und Revisionsexpertenprüfung fusioniert werden, müssen alle Stimmrechte *unmittelbar* gehalten werden; Zwischenholdings versperren den Weg über Art. 23 Abs. 1 lit. b FusG ([BGE 148 III 362](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_005_BGE-148-III-362_2022.html#consideration_6.4)).
- **Inventar und Prozessrisiken bei Spaltung und Vermögensübertragung**: Das Inventar (Art. 37 lit. b, Art. 71 Abs. 1 lit. b FusG) entscheidet nicht nur über den Vermögensübergang, sondern bei der Abspaltung auch über laufende Gerichts- und Verwaltungsverfahren. Passiven, Eventualverbindlichkeiten und Streitgegenstände sind eindeutig zuzuordnen.
- **Bilanzstichtag und KMU-Verzicht frühzeitig planen**: Liegt der letzte Bilanzstichtag bei Vertragsabschluss über sechs Monate zurück, wird ein Zwischenabschluss fällig (Art. 11, 35, 58 FusG). Ein KMU-Verzicht auf Bericht, Prüfung und Einsichtsrecht erfordert die nachweisliche Zustimmung *sämtlicher* Gesellschafterinnen und Gesellschafter.
- **Arbeitsrechtliche Konsultation vor dem Beschluss**: Unterbleibt die rechtzeitige Information und Konsultation nach Art. 333a OR, droht bei Fusion, Spaltung und Vermögensübertragung eine gerichtliche Registersperre durch die Arbeitnehmervertretung (Art. 28 Abs. 3 FusG).
- **Steuer- und Kartellprüfung parallel führen**: Ein zivilrechtlich gültiger Vollzug garantiert keine Steuerneutralität. Insbesondere bei Einbringung von Einzelunternehmen oder Personengesellschaften sowie bei Spaltungen ist das Betriebserfordernis (Art. 19 Abs. 1 lit. b, Art. 61 Abs. 1 lit. b DBG) vorab – idealerweise mittels Steuerruling – abzuklären.

## Leitentscheide {#leitentscheide}

| Entscheid | Gegenstand | Bedeutung |
|---|---|---|
| [BGE 132 III 470](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_005_BGE-132-III-470_2006.html) | Numerus clausus; Institute des öffentlichen Rechts | Spezialgesetzliche AG des öffentlichen Rechts (SBB) darf keine privatrechtliche AG durch Absorptionsfusion übernehmen (Art. 2 lit. d, Art. 99 FusG). |
| [BGE 148 III 362](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_005_BGE-148-III-362_2022.html) | Erleichterte Schwesternfusion | Art. 23 Abs. 1 lit. b FusG verlangt direkten Besitz aller stimmberechtigten Anteile; indirekte Beteiligungen genügen nicht. |
| [BGE 140 IV 162](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-140-IV-162_2014.html) | Universalsukzession im Strafprozess | Privatrechtliche Gesamtnachfolge nach Art. 22 Abs. 1 FusG verschafft der übernehmenden AG keine Privatklägerstellung nach Art. 121 Abs. 2 StPO. |
| [BGE 152 II 375](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_004_BGE-152-II-375_2026.html) | Abspaltung und Parteistellung | Bei der Abspaltung (Art. 29 lit. b FusG) folgt die Parteistellung in hängigen Verfahren dem inventarisierten Vermögenswert bzw. bei umfassender Liquidation beiden Gesellschaften. |
| [BGE 146 II 73](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_004_BGE-146-II-73_2020.html) | Vermögensübertragung eines Teilvermögens | Übertragung eines Teilbetriebs nach Art. 69 ff. FusG führt zur partiellen Universalsukzession und kann partielle MWST-Steuernachfolge auslösen. |
| [BGE 135 III 603](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_005_BGE-135-III-603_2009.html) | Überprüfungsklage (Art. 105 FusG) | Klage dient der wirtschaftlichen Korrektur verletzter Kontinuität; kein Kostenprivileg nach Art. 105 Abs. 3 FusG bei Aktienkauf in Kenntnis der Abfindung. |
| [BGE 134 III 255](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_005_BGE-134-III-255_2008.html) | Edition des Bewertungsberichts | Im Verfahren nach Art. 105 FusG ist die Offenlegung des Unternehmensbewertungsberichts zulässig; kein generelles Geschäftsgeheimnis. |
| [BGE 137 III 577](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_005_BGE-137-III-577_2011.html) | Prozesskosten vor Bundesgericht | Kostenprivileg von Art. 105 Abs. 3 FusG greift vor Bundesgericht bei erheblichem eigenem finanziellem Interesse des Klägers nicht. |
| [BGE 151 III 212](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_005_BGE-151-III-212_2025.html) | Zuständigkeit des Handelsgerichts | Überprüfungsklage nach Art. 105 Abs. 1 FusG ist gesellschaftsrechtliche Streitigkeit nach Art. 6 Abs. 4 lit. b ZPO. |
| [BGE 132 III 32](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_005_BGE-132-III-32_2006.html) | Arbeitnehmerschutz bei Spaltung | Übergang der Arbeitsverhältnisse nach Art. 333 OR ist zwingend und umfasst in der Solidarhaftung auch Sozialplanansprüche. |
| [BGE 138 II 557](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_004_BGE-138-II-557_2012.html) | Handänderungssteuerverbot | Art. 103 FusG ist direkt anwendbares Bundesrecht und verbietet kantonale Handänderungssteuern auch bei konzerninterner Übertragung an eine Vorsorgestiftung. |
| [BGE 142 II 283](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_004_BGE-142-II-283_2016.html) | Steuerliches Betriebserfordernis | Steuerneutrale Umstrukturierung einer Personenunternehmung in eine juristische Person (Art. 19 Abs. 1 lit. b DBG) setzt einen echten Betrieb oder Teilbetrieb voraus. |
