# Themen-Kandidaten aus bger-update.ch

Arbeitsliste für den Bereich `/themen/`. Jeder Agent und jeder Mensch kann ein Thema übernehmen.

**Stand**: 24.10.2026 · **Quelle**: bger-update.ch, Wochensicht Straf-, öffentliches, Zivil- und
Sozialversicherungsrecht (Publikationen 19.–23.10.2026, 152 Urteile) und Annex «Erwähnenswerte
Urteile kantonaler und eidgenössischer Gerichte» (erfasst 17.–24.10.2026, 38 Entscheide).

---

## So wird ein Thema übernommen

1. **Reservieren**: In der Zeile `Status` des Themas `offen` ersetzen durch
   `in Arbeit — {wer}, {Modell}, {Datum}` und das gleich committen und pushen. So arbeiten nicht
   zwei Agenten am selben Thema. Ein Thema, das seit mehr als 7 Tagen `in Arbeit` steht und noch
   keinen Commit in `content/themen/{slug}/` hat, darf neu reserviert werden.
2. **Erstellen**: nach dem Skill `agent/skills/glossagens-themen/` (Recherche, Aufbau je Typ,
   Prüfung mit `pruefen.py`). Massstab ist `content/themen/pragmatischer-methodenpluralismus/`.
   Frontmatter und Regeln: CLAUDE.md, Abschnitt «Themen».
3. **Abschliessen**: `Status` auf `erledigt — content/themen/{slug}/ ({Commit})` setzen.

**Was diese Liste ist — und was nicht**

- Die **Eckpunkte** sind ein Gerüst, keine Belege. Sie stützen sich auf die **KI-generierten**
  Ticker und Zusammenfassungen von bger-update («keine Gewähr»). Jede Aussage ist am
  Originalentscheid zu prüfen; Entscheide über entscheidsuche (`search_by_case_number`) holen und
  verlinken, Normtexte nur über Fedlex bzw. `{{< wortlaut >}}`.
- Die genannten **BGE** stammen aus diesen Zusammenfassungen und sind **unverifiziert**. Nicht
  ungeprüft übernehmen (siehe `project_fabricated_citations` in den Memories:
  Falschzitate kommen vor).
- Ein Anlassentscheid macht noch kein Thema. Wie bei den Kommentaren gilt **breite Recherche**:
  die ganze Rechtsprechungslinie, nicht nur das Urteil der Woche.
- **Abgrenzung**: Ein Thema verdichtet Fragen, die sich aus **mehreren** Normen beantworten, und
  verweist auf die Kommentare. Was nur einen Artikel betrifft, gehört in den Kommentar — siehe
  Abschnitt «Kommentar-Nachträge» am Ende.

**Zeichen bei den Normen**: ✓ Kommentar vorhanden (in `normen` eintragen und auf die passende
Überschrift verlinken) · ○ noch kein Kommentar (in `normen` zulässig, erscheint als Lücke).

**Kennzeichen der Entscheide**: **Publ.** = zur Publikation vorgesehen · **5er** = Fünferbesetzung ·
**G** = Gutheissung · **tG** = teilweise Gutheissung · **A** = Abweisung · **Annex** = Entscheid eines
anderen Gerichts aus dem Annex.

## Übersicht

| Nr. | Thema | Typ | Priorität | Status |
|---|---|---|---|---|
| 1 | Bettelverbote und umwandelbare Bussen | `grundlage` | hoch | in Arbeit — Hermes Agent, glm-5.2, 24.10.2026 |
| 2 | Haftgründe und Ersatzmassnahmen im Strafverfahren | `verfahren` | hoch | erledigt — content/themen/haftgruende-und-ersatzmassnahmen/ (9c918263) |
| 3 | Altersfeststellung und Datenberichtigung im ZEMIS/SYMIC | `verfahren` | hoch | offen |
| 4 | Fernhaltung straffälliger Ausländerinnen und Ausländer | `rechtsfolgen` | hoch | offen |
| 5 | Replikrecht und Akteneinsicht | `grundlage` | hoch | in Arbeit — Antigravity, gemini-3.8-flash, 24.10.2026 |
| 6 | Auszonung oder Nichteinzonung | `grundlage` | mittel | offen |
| 7 | Beweisverwertungsverbote im Strafprozess | `grundlage` | mittel | offen |
| 8 | Siegelung und Entsiegelung | `verfahren` | mittel | offen |
| 9 | Informationsaustausch zwischen Kindesschutz und Strafverfolgung | `rechtsfolgen` | mittel | offen |
| 10 | Erwerbsobliegenheit und hypothetisches Einkommen im Unterhaltsrecht | `rechtsfolgen` | mittel | offen |
| 11 | Einkommensvergleich bei der Invaliditätsbemessung | `grundlage` | mittel | offen |
| 12 | Bauen ausserhalb der Bauzone: Zonenkonformität und Bestandesschutz | `grundlage` | mittel | offen |
| 13 | Asylunwürdigkeit und Flüchtlingseigenschaft | `rechtsfolgen` | mittel | offen |
| 14 | Ausländerrechtliche Administrativhaft | `verfahren` | mittel | offen |
| 15 | Nachvertragliches Konkurrenzverbot | `rechtsfolgen` | niedrig | offen |
| 16 | Anklagegrundsatz und rechtliche Würdigung | `grundlage` | niedrig | offen |
| 17 | Weltrechtspflege: Völkerrechtsverbrechen vor Schweizer Gerichten | `grundlage` | niedrig | offen |
| 18 | Mantelhandel im Steuerrecht | `grundlage` | niedrig | offen |

Priorität: **hoch** = mehrere Urteile derselben Woche oder Publikation/Fünferbesetzung, und das
Thema berührt mehr als ein Hauptgebiet; **mittel** = klarer Querschnitt mit aktuellem Anlass;
**niedrig** = Anlass schmal oder Normen weitgehend unkommentiert.

---

## 1. Bettelverbote und umwandelbare Bussen {#bettelverbote}

- **Status**: erledigt — content/themen/bettelverbote-und-umwandelbare-bussen/
- **Slug**: `bettelverbote-und-umwandelbare-bussen`
- **Typ**: `grundlage` (alternativ als zweiter Schritt ein `kantonsvergleich` der kantonalen Bettelverbote)
- **Sachgebiete**: `grundrechte`, `strafrecht.strafzumessung`, `strafprozess.strafbefehl`
- **Normen**: BV 7 ✓, BV 10 ✓, BV 36 ✓, EMRK 8 ✓, StGB 106 ✓, StPO 410 ✓ — kantonal Art. 11A LPG/GE (nicht im Bestand)
- **Anlass**: sieben Urteile in einer Woche, alle Genf, alle zum selben Muster
  - [6B_453/2025](https://bger-update.ch/zusammenfassung/34663/) G · [6B_452/2025](https://bger-update.ch/zusammenfassung/34662/) G · [6B_445/2025](https://bger-update.ch/zusammenfassung/34661/) G · [6B_281/2025](https://bger-update.ch/zusammenfassung/34659/) G · [6B_239/2025](https://bger-update.ch/zusammenfassung/34658/) G · [6B_29/2025](https://bger-update.ch/zusammenfassung/34660/) tG
  - [6B_131/2025](https://bger-update.ch/zusammenfassung/34657/) A — Revision von über 100 Strafbefehlen (Faksimile-Stempel)
- **Eckpunkte**
  - Betteln liegt im Schutzbereich der persönlichen Freiheit (BV 10 Abs. 2) und des Privatlebens (EMRK 8); Massstab für Einschränkungen ist BV 36, mit Bezug zur Menschenwürde (BV 7).
  - Rechtsprechungslinie laut Zusammenfassungen: abstrakte Normenkontrolle Basel-Stadt (BGE 149 I 248), konkrete Anwendung Genf (BGE 152 I 38 und fünf Parallelurteile vom 19.03.2025), jetzt die Serie vom 17.09.2026 — **alle drei Stufen verifizieren**.
  - Kern: Eine in Ersatzfreiheitsstrafe umwandelbare Busse gegen strukturell Mittellose ist nur *ultima ratio* nach einer dokumentierten **administrativen Kaskade** (polizeiliche Wegweisung, formelle Verwarnung, Information über Norminhalt und Umwandlungsfolge in einer verständlichen Sprache).
  - Frühere Verurteilungen und Strafanzeigen ersetzen die Kaskade nicht; Vorstrafen unter dem alten, umfassenden Verbot informieren nicht über das neue, ortsbezogene (6B_281/2025).
  - Tatbestand «unmittelbare Nähe» von Eingängen: Distanzangaben im Polizeiprotokoll (unter 2 m genügt, «unter 10 m» im Zweifel nicht).
  - Art. 106 Abs. 2 StGB (schuldhafte Nichtzahlung) ist kein taugliches Korrektiv der Unverhältnismässigkeit.
  - Prozessuale Seite: Mangel nicht heilbar → Freispruch; Faksimile-Stempel auf Strafbefehlen ist Formmangel, weder Nichtigkeit noch Revisionsgrund nach Art. 410 Abs. 1 lit. a StPO (6B_131/2025).
- **Offen für die Recherche**: Haben andere Kantone (Basel-Stadt, Waadt, Lausanne, Zürich) seit BGE 149 I 248 nachgezogen? EGMR *Lacatus c. Suisse* (2021) als Ausgangspunkt prüfen.

## 2. Haftgründe und Ersatzmassnahmen im Strafverfahren {#haftgruende}

- **Status**: erledigt — content/themen/haftgruende-und-ersatzmassnahmen/ (9c918263)
- **Slug**: `haftgruende-und-ersatzmassnahmen`
- **Typ**: `verfahren` (Anordnung → Haftprüfung → Haftentlassung, je mit Haftgrund und Ersatzmassnahme)
- **Sachgebiete**: `strafprozess.haft`, `strafprozess.verteidigung`, `grundrechte`
- **Normen**: StPO 221 ✓, 222 ✓, 225 ✓, 226 ✓, 227 ✓, 228 ✓, 236 ✓, 237 ✓, 130 ✓ · BV 31 ✓ · EMRK 3 ✓, 5 ✓
- **Anlass**
  - [7B_1283/2026](https://bger-update.ch/zusammenfassung/34697/) G — Unmittelbarkeit bei qualifizierter Wiederholungsgefahr entfällt nach über einem Jahr deliktfrei in Freiheit
  - [7B_1249/2026](https://bger-update.ch/zusammenfassung/34566/) tG — kurze Messerdrohung: Schwelle der Anlasstat und Eskalationsprognose (Art. 221 Abs. 1bis lit. a/b)
  - [7B_1311/2026](https://bger-update.ch/zusammenfassung/34698/) tG — Abhängigkeit von Behördenunterstützung wirkt verankernd, keine «ausgeprägte» Fluchtgefahr; Ersatzmassnahmen zwingend prüfen
  - [7B_1235/2026](https://bger-update.ch/zusammenfassung/34696/) A — drohendes Erlöschen des Schutzstatus S als Fluchtreiz; ausgeprägte Fluchtgefahr schliesst Ersatzmassnahmen regelmässig aus
  - [7B_1056/2026](https://bger-update.ch/zusammenfassung/34682/) G — Widerruf des vorzeitigen Massnahmenvollzugs (Art. 236) ist eigene, zu begründende Verfügung; notwendige Verteidigung (Art. 130) auch bei Haft-Nebenentscheiden
  - [7B_1240/2026](https://bger-update.ch/zusammenfassung/34691/) A — dringender Tatverdacht trotz grenzüberschreitender Überwachung (Brücke zu Thema 7)
  - [7B_1149/2026](https://bger-update.ch/zusammenfassung/34607/) A — Krankheit und Haftbedingungen (EMRK 3): medizinische Versorgung als Mittel-, nicht Erfolgspflicht
  - [6B_902/2025](https://bger-update.ch/zusammenfassung/34629/) A — Haftbedingungs-Rügen nach letztinstanzlichem Haftentscheid im Sachurteil gesperrt
- **Eckpunkte**
  - Gliederung nach Haftgrund: Fluchtgefahr (Gesamtwürdigung; Staatsangehörigkeit und fehlende Bindungen allein genügen nicht), Kollusionsgefahr, Wiederholungsgefahr, qualifizierte Wiederholungsgefahr nach Art. 221 Abs. 1bis StPO (seit 2024: Anlasstat, «unmittelbare» und «ernsthafte» Gefahr, Gutachtenbedarf).
  - Stufung der Fluchtgefahr («moderat» vs. «ausgeprägt») als Weiche für Ersatzmassnahmen (Art. 237).
  - Verfahrensgarantien: Begründungspflicht, notwendige Verteidigung, Haftbedingungen und deren Rügeweg (Haftbeschwerde, nicht Sachurteil).
  - Tabelle «Phase · Behörde · Frist · Rechtsmittel» für Anordnung (Art. 224–226), Haftverlängerung (Art. 227), Haftentlassungsgesuch (Art. 228), Sicherheitshaft (Art. 229–233).
- **Abgrenzung**: Die Artikelkommentare zu Art. 221 und 237 StPO bestehen bereits; das Thema bündelt den Ablauf und verweist dorthin, statt die Haftgründe neu zu kommentieren. Die neuen Präzisierungen gehören **zusätzlich** in den Kommentar zu Art. 221 StPO (siehe Nachträge).

## 3. Altersfeststellung und Datenberichtigung im ZEMIS/SYMIC {#symic}

- **Status**: offen
- **Slug**: `altersfeststellung-und-datenberichtigung-symic`
- **Typ**: `verfahren`
- **Sachgebiete**: `auslaenderrecht.asyl`, `auslaenderrecht.einreise`, `verwaltungsverfahren`, `grundrechte`
- **Normen**: VwVG 63 ✓, 65 ✓, VwVG 25a ✓ · DSG 41 ✓ · AsylG ○ (Art. 17 Abs. 3bis prüfen) · BGG ○
- **Anlass** (drei Urteile in Fünferbesetzung, eines zur Publikation vorgesehen)
  - [1C_764/2025](https://bger-update.ch/zusammenfassung/34575/) A **Publ. 5er** — BGE 144 II 56 (kein Kostenvorschuss für unbegleitete Minderjährige) gilt nur im Asylverfahren, nicht bei der SYMIC-Berichtigung
  - [1C_747/2025](https://bger-update.ch/zusammenfassung/34572/) A **5er** — gleiche Frage; Beweismass bei der Datenberichtigung: überwiegende Wahrscheinlichkeit, nicht asylrechtliche Glaubhaftmachung
  - [1C_639/2025](https://bger-update.ch/zusammenfassung/34574/) G **5er** — BVGer muss Aussichtslosigkeit auf den Zeitpunkt des Gesuchs beurteilen; inkonsistente Parallelpraxis gerügt
  - Annex: [BVGer F-6766/2026](https://bger-update.ch/weitere/2720/) — strittige Änderung des Geburtsdatums braucht eine anfechtbare Verfügung; faktische Mutation ersetzt sie nicht
- **Eckpunkte**
  - Ablauf: Altersabklärung im Asylverfahren → Eintrag im ZEMIS/SYMIC → Berichtigungsbegehren → Verfügung des SEM (Anspruch darauf, Rechtsverweigerungsbeschwerde) → BVGer → BGer (Beschwerde in öffentlich-rechtlichen Angelegenheiten, Datenschutz).
  - Zwei Verfahren, zwei Massstäbe: asylrechtliche Minderjährigkeit vs. datenschutzrechtliche Richtigkeit.
  - Kosten: Kostenvorschuss, unentgeltliche Rechtspflege, massgeblicher Beurteilungszeitpunkt der Erfolgsaussichten.
  - Folgen des eingetragenen Alters (Unterbringung, Vertretung, Dublin, Schule).
- **Offen**: Welche Rechtsgrundlage nennt das BGer für den Berichtigungsanspruch genau (DSG 41 oder Spezialnorm im AIG/AsylG/ZEMIS-Verordnung)? Erst am Volltext festlegen, dann `normen` setzen.

## 4. Fernhaltung straffälliger Ausländerinnen und Ausländer {#fernhaltung}

- **Status**: offen
- **Slug**: `fernhaltung-straffaelliger-auslaender`
- **Typ**: `rechtsfolgen` (strafrechtliche Landesverweisung · ausländerrechtlicher Widerruf und Einreiseverbot · Vollzug und Non-Refoulement)
- **Sachgebiete**: `strafrecht.landesverweisung`, `auslaenderrecht.bewilligung`, `auslaenderrecht.einreise`, `auslaenderrecht.fza`, `grundrechte`
- **Normen**: StGB 66a ✓, 66abis ✓, 66d ✓ · AIG 63 ✓, 67 ✓ · BV 25 ✓ · EMRK 3 ✓, 8 ✓
- **Anlass**
  - [6B_736/2025](https://bger-update.ch/zusammenfassung/34563/) G — Härtefall bejaht, aber keine Interessenabwägung und keine Prüfung von EMRK 3 → Kassation
  - [6B_268/2026](https://bger-update.ch/zusammenfassung/34593/) A — Landesverweisung bei Betäubungsmittelverbrechen trotz Geburt in der Schweiz
  - [6B_294/2026](https://bger-update.ch/zusammenfassung/34670/) tG **5er** — Landesverweisung eines in der Schweiz Geborenen bestätigt
  - [2C_141/2026](https://bger-update.ch/zusammenfassung/34628/) A — Einreiseverbot und SIS-Ausschreibung trotz Ehe mit EU-Bürgerin (Art. 5 Anhang I FZA)
  - [2C_513/2025](https://bger-update.ch/zusammenfassung/34584/) Nichteintreten **5er** — Wegweisung einer trans Person nach Brasilien: Anforderungen an den Nachweis des Refoulement-Risikos
- **Eckpunkte**
  - Drei Schienen nebeneinander: Strafgericht (obligatorische/fakultative Landesverweisung, Härtefallklausel Art. 66a Abs. 2), Migrationsbehörde (Widerruf, Nichtverlängerung, Einreiseverbot), Vollzug (Art. 66d StGB, Art. 25 Abs. 2/3 BV, EMRK 3).
  - Prüfprogramm der Härtefallklausel: schwerer persönlicher Härtefall → Interessenabwägung → völkerrechtliche Garantien; fehlt ein Schritt, wird kassiert.
  - FZA-Schranke: «tatsächliche, gegenwärtige und hinreichend schwere» Gefährdung der öffentlichen Ordnung.
  - Non-Refoulement für Angehörige sexueller Minderheiten: allgemeiner Lagebericht genügt nicht ohne Bezug auf systematische Verfolgung und fehlenden Staatsschutz.
  - Verhältnis der Schienen: Dualismusverbot (Art. 63 Abs. 3 AIG) — Migrationsbehörde darf nicht nachholen, was das Strafgericht verworfen hat.

## 5. Replikrecht und Akteneinsicht {#replikrecht}

- **Status**: in Arbeit — Antigravity, gemini-3.8-flash, 24.10.2026
- **Slug**: `replikrecht-und-akteneinsicht`
- **Typ**: `grundlage`
- **Sachgebiete**: `grundrechte`, `bundesrechtspflege`, `verwaltungsverfahren`
- **Normen**: BV 29 ✓ · EMRK 6 ✓ · VwVG 26 ✓, 29 ✓, 30 ✓ · BGG 108 ✓, BGG 102 ○ · StPO 107 ✓
- **Anlass**
  - Annex: [EGMR, B.K. gegen die Schweiz, Nr. 24268/21 und 55351/21](https://bger-update.ch/weitere/3034/) vom 22.10.2026 — Verletzung von Art. 6 EMRK: Das Bundesgericht stützte sich im vereinfachten Verfahren (Art. 108 BGG) auf von Amtes wegen eingeholte Auskünfte, ohne sie dem Beschwerdeführer zur Stellungnahme zu unterbreiten
  - [1C_396/2026](https://bger-update.ch/zusammenfassung/34581/) G — unbehandeltes Akteneinsichtsgesuch führt ohne Rücksicht auf den Ausgang zur Aufhebung
  - [7B_1056/2026](https://bger-update.ch/zusammenfassung/34682/) G — fehlende Begründung als Gehörsverletzung
- **Eckpunkte**
  - Herleitung: formelle Natur des Gehörsanspruchs vs. Rechtsprechung «kein Selbstzweck»; wo das BGer die formelle Natur beibehält (Akteneinsicht, Replik).
  - EGMR-Fallreihe gegen die Schweiz zum Replikrecht (laut Annex: *Nideröst-Huber*, *F.R.*, *Ziegler*, *Kessler* — einzeln verifizieren) und die Antwort der Schweizer Praxis (unbedingtes Replikrecht).
  - Neu: Pflicht gilt auch für Informationen, die das Gericht selbst einholt, und im vereinfachten Verfahren.
  - Heilung im Rechtsmittelverfahren: Voraussetzungen und Grenzen.
- **Offen**: Revision nach Art. 122 BGG infolge des EGMR-Urteils? Reaktion des BGer verfolgen.

## 6. Auszonung oder Nichteinzonung {#auszonung}

- **Status**: offen
- **Slug**: `auszonung-oder-nichteinzonung`
- **Typ**: `grundlage`
- **Sachgebiete**: `enteignung`, `raumplanung.nutzungsplanung`
- **Normen**: BV 26 ✓ · RPG 5 ✓, RPG 15 ○, RPG 21 ○
- **Anlass**
  - [1C_681/2025](https://bger-update.ch/zusammenfassung/34624/) A — rechtswidriger Weiler von 1981: qualitative Kriterien (isolierte Lage, landwirtschaftlicher Charakter) begründen die RPG-Widrigkeit auch ohne Bedarfsrechnung → Nichteinzonung, keine Entschädigung
  - [1C_571/2025](https://bger-update.ch/zusammenfassung/34591/) G — Plan von 1986/1991 ohne Bedarfserhebung, unverändert aus Vor-RPG-Plan übernommen: keine Vermutung der RPG-Konformität
- **Eckpunkte**
  - Weichenstellung: Auszonung (Eingriff in eine RPG-konforme Bauzone → materielle Enteignung möglich) vs. Nichteinzonung (keine Entschädigung).
  - Kriterien der RPG-Konformität älterer Pläne: quantitativ (Bedarf 15 Jahre) und qualitativ (Lage, Erschliessung, Charakter).
  - Voraussetzungen der materiellen Enteignung (besonders schwerer Eingriff, Sonderopfer) und Verfahren.
  - Aktualität: Rückzonungen nach RPG-Revision 2014 in vielen Kantonen.

## 7. Beweisverwertungsverbote im Strafprozess {#verwertungsverbote}

- **Status**: offen
- **Slug**: `beweisverwertungsverbote-im-strafprozess`
- **Typ**: `grundlage`
- **Sachgebiete**: `strafprozess.zwangsmassnahmen`, `strafprozess.erledigung`, `grundrechte`
- **Normen**: StPO 140 ✓, 141 ✓, 147 ✓, 158 ✓, 177 ✓, 215 ✓, 269 ✓ · EMRK 6 ✓, 8 ✓ · BV 8 ✓
- **Anlass**
  - [6B_344/2025](https://bger-update.ch/zusammenfassung/34655/) A — die Verwertbarkeit nach Art. 141 Abs. 2 StPO erwächst mit dem Rückweisungsentscheid in Rechtskraft
  - [6B_677/2024](https://bger-update.ch/zusammenfassung/34588/) A — relatives Verwertungsverbot (Art. 177 Abs. 3): das Opfer muss sein Zeugnisverweigerungsrecht selbst ausüben
  - [6B_153/2026](https://bger-update.ch/zusammenfassung/34602/) A **5er** — Identitätskontrolle ohne Verdacht (Schlafen auf Parkbank), Racial Profiling: daraus erlangte Beweise unverwertbar; kantonales Polizeirecht umgeht Art. 215 StPO nicht
  - [7B_1240/2026](https://bger-update.ch/zusammenfassung/34691/) A — grenzüberschreitende verdeckte Überwachung: nachträgliche Genehmigung des ausländischen Staates
  - Annex: [TC NE ARMP.2026.87](https://bger-update.ch/weitere/3032/) — Verletzung des Teilnahmerechts (Art. 147 Abs. 4) führt zur Unverwertbarkeit zulasten der abwesenden Partei, nicht zur Entfernung aus den Akten
- **Eckpunkte**
  - System: absolute (Art. 140, 141 Abs. 1) vs. relative Verbote (Art. 141 Abs. 2, Interessenabwägung, «schwere Straftat»), Ordnungsvorschriften (Abs. 3), Fernwirkung (Abs. 4).
  - Wer kann sich auf ein Verbot berufen, und wann (Rechtskraft, Rückweisung, Revision)?
  - Polizeiliche Vorermittlung: Abgrenzung kantonales Polizeirecht / StPO; Diskriminierungsverbot als Verwertungsschranke.
  - Beweise aus dem Ausland: Territorialitätsprinzip, Rechtshilfe, nachträgliche Genehmigung.

## 8. Siegelung und Entsiegelung {#entsiegelung}

- **Status**: offen
- **Slug**: `siegelung-und-entsiegelung`
- **Typ**: `verfahren`
- **Sachgebiete**: `strafprozess.zwangsmassnahmen`
- **Normen**: StPO 197 ✓, 246 ✓, 248 ✓, 248a ✓, 264 ✓ · BGFA ○ (Anwaltsgeheimnis Art. 13) · StGB 321 ○
- **Anlass**
  - [7B_815/2026](https://bger-update.ch/zusammenfassung/34642/) tG — Substanziierung je nach Geheimnisart: beim Anwaltsgeheimnis genügen Anwaltsnamen und E-Mail-Adressen; beim Arztgeheimnis auf Privatgeräten höhere Hürden
  - [7B_925/2025](https://bger-update.ch/zusammenfassung/34559/) G — Entsiegelung eines Smartphones (Klimaaktivismus): das Zwangsmassnahmengericht muss zeitlichen und sachlichen Umfang und die Triage festlegen
- **Eckpunkte**: Ablauf Siegelungsbegehren → Entsiegelungsgesuch (Frist) → Triage → Entscheid → Beschwerde ans BGer; Neuerungen seit 01.01.2024 (Art. 248a); Substanziierungsobliegenheit; Smartphones als Sonderfall (Datenmenge, Verhältnismässigkeit, Zeitraum).
- **Abgrenzung**: Prüfen, ob die Kommentare zu Art. 248 und 248a StPO den Ablauf schon tragen; dann schmaler halten und vor allem verweisen.

## 9. Informationsaustausch zwischen Kindesschutz und Strafverfolgung {#kindesschutz-strafverfolgung}

- **Status**: offen
- **Slug**: `kindesschutz-und-strafverfolgung`
- **Typ**: `rechtsfolgen`
- **Sachgebiete**: `familienrecht.kinder`, `familienrecht.erwachsenenschutz`, `strafprozess`
- **Normen**: ZGB 314 ✓, ZGB 314e ○, 443 ○, 448 ○, 451 ○, 453 ○ · StGB 320 ○, 321 ○, 364 ○ · StPO 147 ✓, 302 ○
- **Anlass**
  - Annex: [TC NE ARMP.2026.87](https://bger-update.ch/weitere/3032/) — laut Annex erstmals zu Art. 453 ZGB: Ein Beistand darf seinen Bericht der Staatsanwaltschaft ohne Entbindung vom Amtsgeheimnis weitergeben, wenn häusliche Gewalt eine ernsthafte Gefahr begründet
  - bger-update stellt dazu selbst die offene Frage «Art. 453 ZGB: Rechtfertigung für Informationsaustausch zwischen Kindesschutz und Strafverfolgung?» (Annotation auf der Startseite)
- **Eckpunkte**: Melderechte und Meldepflichten (ZGB 314c–314e, 443), Amts- und Berufsgeheimnis (StGB 320/321) und deren Rechtfertigung (StGB 14, ZGB 453), Verwertbarkeit im Strafverfahren, Rückfluss von der Staatsanwaltschaft zur KESB, Rollen von Beistand, KESB, Schule und Ärzteschaft.
- **Hinweis**: Normenlage ist mehrheitlich unkommentiert; das Thema zeigt die Lücken und kann die Kommentare zu ZGB 453 und StGB 320 anstossen.

## 10. Erwerbsobliegenheit und hypothetisches Einkommen im Unterhaltsrecht {#hypothetisches-einkommen}

- **Status**: offen
- **Slug**: `hypothetisches-einkommen-im-unterhaltsrecht`
- **Typ**: `rechtsfolgen`
- **Sachgebiete**: `familienrecht.unterhalt`, `familienrecht.ehe`
- **Normen**: ZGB 125 ○, 163 ✓, 176 ✓, 276 ✓, 285 ✓
- **Anlass**
  - [5A_254/2026](https://bger-update.ch/zusammenfassung/34608/) tG — Abweichen vom Schulstufenmodell muss konkret begründet werden; Eheschutzstadium allein rechtfertigt keine reduzierte Erwerbsobliegenheit
  - Annex: [OGer SO ZKBER.2025.67](https://bger-update.ch/weitere/1475/) — freiwilliger Wegzug ins Ausland: Schweizer Einkommen bleibt hypothetisch anrechenbar
- **Eckpunkte**: zweistufige Prüfung (Zumutbarkeit, tatsächliche Möglichkeit), Schulstufenmodell, Übergangsfrist, freiwillige Einkommensverminderung, Gesundheit und Auslandwegzug, Verhältnis Ehegatten-/Kindesunterhalt, Bezug zur einstufig-konkreten Methode.

## 11. Einkommensvergleich bei der Invaliditätsbemessung {#einkommensvergleich}

- **Status**: offen
- **Slug**: `einkommensvergleich-invaliditaetsbemessung`
- **Typ**: `grundlage`
- **Sachgebiete**: `iv.rente`, `iv.revision`, `uv.rente_ie`
- **Normen**: ATSG 16 ✓, ATSG 17 ✓, ATSG 43 ✓ · IVG 28 ✓, 28a ✓ · IVV 25, 26, 26bis (Verordnung, nicht im Bestand)
- **Anlass**
  - [8C_288/2026](https://bger-update.ch/zusammenfassung/34669/) G — Doppelzählungsverbot beim Valideneinkommen: enthält der Stundenlohn eine Ferienentschädigung, sind die Ferientage vom Arbeitsbudget abzuziehen
  - [9C_518/2025](https://bger-update.ch/zusammenfassung/34576/) tG — Neuanmeldung: Prüfung der wesentlichen Änderung; keine Abweichung vom Gutachten ohne medizinische Grundlage
  - [9C_501/2025](https://bger-update.ch/zusammenfassung/34551/) A — Schmerzangaben ohne objektives Korrelat
  - Annex: [VersGer SG IV 2025/272](https://bger-update.ch/weitere/3021/) — Frühinvalidität (Art. 26 Abs. 6 IVV seit 2022) und berufsberaterische Abklärung der Verwertbarkeit
- **Eckpunkte**: Valideneinkommen (tatsächliches, Tabellenlohn, Frühinvalidität), Invalideneinkommen (LSE, Abzug, Parallelisierung seit 2022), Rundung und Bagatellgrenzen, Beweiswürdigung medizinischer Gutachten (Indikatorenprüfung), Revision und Neuanmeldung.

## 12. Bauen ausserhalb der Bauzone: Zonenkonformität und Bestandesschutz {#ausserhalb-bauzone}

- **Status**: offen
- **Slug**: `bauen-ausserhalb-der-bauzone`
- **Typ**: `grundlage`
- **Sachgebiete**: `raumplanung.ausserhalb_bauzone`, `raumplanung.baubewilligung`, `baeuerliches_bodenrecht`
- **Normen**: RPG 16a ○, 22 ✓, 24 ✓, 24a ✓, 24b ✓, 24bis ✓, 24c ✓, 24d ✓ · BGBB ○ · DBG 18 ○
- **Anlass**
  - Annex: [VGer ZH VB.2025.00331](https://bger-update.ch/weitere/3113/) — Kindertagesstätte im Wohnhaus in der Landwirtschaftszone ist gewerbliche Nutzung, keine «teilweise Änderung» nach Art. 24c RPG
  - Annex: [VGer GR VR1 2026 31](https://bger-update.ch/weitere/327/) — Winterdienst mit landwirtschaftlichen Traktoren hebt deren Zonenkonformität nicht auf (Art. 16a RPG, im Vergaberecht)
  - [9C_577/2025](https://bger-update.ch/zusammenfassung/34656/) A — eisenbahnrechtliche Plangenehmigung entzieht einem Grundstück das landwirtschaftliche Steuerprivileg
- **Eckpunkte**: Trennungsgrundsatz; zonenkonform (Art. 16a) vs. Ausnahme (Art. 24 ff.); Bestandesschutz und «teilweise Änderung» (Art. 24c); Zweckänderung; Folgen im Steuer- und Bodenrecht.
- **Abgrenzung**: Die Art. 24–24d RPG sind kommentiert — das Thema ordnet sie ins System ein und verweist auf die Stellen.

## 13. Asylunwürdigkeit und Flüchtlingseigenschaft {#asylunwuerdigkeit}

- **Status**: offen
- **Slug**: `asylunwuerdigkeit-und-fluechtlingseigenschaft`
- **Typ**: `rechtsfolgen`
- **Sachgebiete**: `auslaenderrecht.asyl`
- **Normen**: AsylG 3 ✓, 53 ○, 54 ○, 59 ○, 64 ○ · AIG 83 ✓ · EMRK 3 ✓
- **Anlass**: Annex: [BVGer D-2663/2024](https://bger-update.ch/weitere/3024/) — Asylunwürdigkeit eines myanmarischen Ex-Offiziers nach Art. 53 lit. a AsylG: individueller Tatbeitrag statt pauschaler Armeezugehörigkeit; Grenzen des Befehlsnotstands. bger-update stellt dazu die Frage «Asylunwürdig, aber Flüchtling: was ändert sich im Alltag gegenüber dem vollen Asylstatus?»
- **Eckpunkte**: Unterschied Flüchtlingseigenschaft / Asyl; Ausschlussgründe (Art. 53, 54 AsylG, Art. 1F FK); Rechtsfolge vorläufige Aufnahme als Flüchtling — Aufenthalt, Familiennachzug, Reisen, Erwerb, Sozialhilfe im Vergleich zum Asyl (Tabelle).

## 14. Ausländerrechtliche Administrativhaft {#administrativhaft}

- **Status**: offen
- **Slug**: `auslaenderrechtliche-administrativhaft`
- **Typ**: `verfahren`
- **Sachgebiete**: `auslaenderrecht.zwangsmassnahmen`
- **Normen**: AIG 75 ✓, 76 ✓, 76a ○, 78 ○, 79 ○, 80 ○, 81 ○ · BV 31 ✓ · EMRK 5 ✓
- **Anlass**
  - Annex: [VGer ZH VB.2026.00610](https://bger-update.ch/weitere/3053/) — Angst vor der Rückkehr begründet keine Untertauchensgefahr; fremdes Reisedokument ist keine Identitätsverweigerung, wenn die Person unter wahrer Identität kooperiert
  - Annex: [VGer BE 100 2026 161](https://bger-update.ch/weitere/1818/) — Dublin-Haft im Regionalgefängnis: zulässige Übergangsfrist bei unplanbarer Inhaftierung vor dem Wochenende
- **Eckpunkte**: Haftarten (Vorbereitungs-, Ausschaffungs-, Dublin-, Durchsetzungshaft), Haftgründe, richterliche Prüfung (96 Stunden), Beschleunigungsgebot, Höchstdauer, Haftbedingungen (Trennungsgebot), Rechtsmittel.
- **Verwandt**: Thema 2 (strafprozessuale Haft) — Unterschiede in einer Tabelle gegenüberstellen.

## 15. Nachvertragliches Konkurrenzverbot {#konkurrenzverbot}

- **Status**: offen
- **Slug**: `nachvertragliches-konkurrenzverbot`
- **Typ**: `rechtsfolgen`
- **Sachgebiete**: `schuldrecht.arbeit`
- **Normen**: OR 340 ✓, 340a ○, 340b ○, 340c ○
- **Anlass**: Annex: [Cour de justice GE ACJC/1664/2026](https://bger-update.ch/weitere/2383/) — Treuhänder mit Kundenkontakt: Einblick bejaht, Verbot scheitert am nicht substanziierten drohenden Schaden; dazu fristlose Entlassung ohne Beweis der Vorwürfe ungerechtfertigt (Verweis aufs Thema [ungerechtfertigte Kündigung](content/themen/ungerechtfertigte-kuendigung/))
- **Eckpunkte**: Voraussetzungen (Handlungsfähigkeit, Schriftform, Einblick, erhebliche Schädigungsmöglichkeit), Kundenbeziehung mit persönlichem Gepräge, Beschränkung (Ort, Zeit, Gegenstand), Wegfall (Art. 340c), Konventionalstrafe und Realexekution, Beweislast.

## 16. Anklagegrundsatz und rechtliche Würdigung {#anklagegrundsatz}

- **Status**: offen
- **Slug**: `anklagegrundsatz-und-rechtliche-wuerdigung`
- **Typ**: `grundlage`
- **Sachgebiete**: `strafprozess.erledigung`, `strafrecht.vermoegen`
- **Normen**: StPO 9 ✓, 158 ✓, 325 ✓, 333 ✓, 344 ✓, 350 ✓ · EMRK 6 ✓ · StGB 158 ✓
- **Anlass**
  - [6B_962/2024](https://bger-update.ch/zusammenfassung/34652/) G — Einpersonen-AG: ob Aktienkapital und gebundene Reserven angetastet sind, ist rechtliche Würdigung, nicht Anklageinhalt
  - [6B_178/2026](https://bger-update.ch/zusammenfassung/34565/) tG — falsches Datum verletzt den Anklagegrundsatz nicht, wenn Ort und Tatmodus bestimmbar bleiben
  - [6B_268/2026](https://bger-update.ch/zusammenfassung/34593/) A — Tatvorhalt (Art. 158) in der Schlusseinvernahme nachholbar
- **Eckpunkte**: Umgrenzungs- und Informationsfunktion; Sachverhalt vs. rechtliche Würdigung; Änderung und Erweiterung (Art. 333), abweichende Würdigung (Art. 344); typische Mängel und Folgen.
- **Hinweis**: niedrige Priorität, weil die Kommentare zu Art. 9 und 325 StPO den Kern schon tragen dürften — zuerst prüfen, ob das Thema mehr leistet als ein Verweis.

## 17. Weltrechtspflege: Völkerrechtsverbrechen vor Schweizer Gerichten {#weltrechtspflege}

- **Status**: offen
- **Slug**: `weltrechtspflege`
- **Typ**: `grundlage`
- **Sachgebiete**: `strafrecht.leib_leben`, `rechtshilfe_straf`
- **Normen**: StGB 3 ○, 6 ○, 7 ○, 264 ff. ○ · StPO 23 ○, 24 ○ · EMRK 6 ✓
- **Anlass**: [6B_41/2025](https://bger-update.ch/zusammenfassung/34625/) A **5er** — Gehilfenschaft eines ehemaligen Polizeichefs von Guatemala an mehrfachem Mord (Gefängnis El Boquerón 2006); Verfahren über 14 Jahre mit EGMR-Entscheid und Revision; Bindung an Rückweisungsentscheide, reformatio in peius
- **Eckpunkte**: Anknüpfungen (Territorialität, Personalität, stellvertretende Strafrechtspflege, Weltrechtsprinzip), Voraussetzung Anwesenheit, Zuständigkeit Bundesanwaltschaft, bekannte Verfahren (vorher verifizieren).

## 18. Mantelhandel im Steuerrecht {#mantelhandel}

- **Status**: offen
- **Slug**: `mantelhandel-im-steuerrecht`
- **Typ**: `grundlage`
- **Sachgebiete**: `steuern.vst_stempel`, `steuern.einkommen_vermoegen`
- **Normen**: StG 5 ○, StG 8 ✓ · VStG 4 ○ · DBG 20 ✓, DBG 67 ○
- **Anlass**: [9C_232/2026](https://bger-update.ch/zusammenfassung/34590/) A **5er** — Emissionsabgabe beim Mantelhandel (Art. 5 Abs. 2 lit. b StG) mindestens auf dem Nennwert, auch bei Verlustvorträgen; teleologische Reduktion verworfen
- **Eckpunkte**: Begriff des Mantelhandels (wirtschaftliche Liquidation, Handwechsel), Folgen in Stempel-, Verrechnungs- und Gewinnsteuer (Verlustverrechnung), Steuerumgehung als Hintergrund.

---

## Kommentar-Nachträge (kein Thema) {#kommentar-nachtraege}

Diese Entscheide betreffen im Kern **einen** Artikel. Sie gehören in den bestehenden Kommentar bzw.
in dessen `rechtsprechung.md` (Revisionseintrag nicht vergessen) oder sind Anlass für einen neuen.

| Entscheid | Norm | Kommentar | Aussage laut bger-update |
|---|---|---|---|
| [7B_1283/2026](https://bger-update.ch/zusammenfassung/34697/), [7B_1249/2026](https://bger-update.ch/zusammenfassung/34566/) | Art. 221 Abs. 1bis StPO | ✓ | Unmittelbarkeit und Eskalationsprognose der qualifizierten Wiederholungsgefahr |
| [7B_1056/2026](https://bger-update.ch/zusammenfassung/34682/) | Art. 130, 236 StPO | ✓ | notwendige Verteidigung bei Haft-Nebenentscheiden; Widerruf des vorzeitigen Massnahmenvollzugs |
| [7B_129/2026](https://bger-update.ch/zusammenfassung/34589/), [7B_890/2026](https://bger-update.ch/zusammenfassung/34568/) | Art. 56 lit. f StPO | ✓ | Befangenheit der Staatsanwaltschaft: ungeschickte Äusserungen genügen nicht; Kumulation von Verfahrensfehlern kann genügen |
| [6B_840/2025](https://bger-update.ch/zusammenfassung/34651/) | Art. 115, 118 StPO | ✓ | Schadloshaltung durch die Täterin beseitigt die Geschädigtenstellung |
| [7B_861/2025](https://bger-update.ch/zusammenfassung/34556/) | Art. 255 Abs. 1bis StPO | ✓ | neues DNA-Profil trotz bestehendem, solange keine Löschfrist läuft |
| [1C_131/2026](https://bger-update.ch/zusammenfassung/34580/) | Ermächtigungsverfahren (kantonal / Art. 7 Abs. 2 lit. b StPO) | ✓ Art. 7 | in dubio pro duriore verlangt genügende Sachverhaltsabklärung |
| [6B_294/2026](https://bger-update.ch/zusammenfassung/34670/) **5er** | Art. 49 Abs. 2 StGB | ✓ | Strafzumessung bei teilweiser retrospektiver Konkurrenz |
| [6B_939/2025](https://bger-update.ch/zusammenfassung/34671/), [6B_373/2026](https://bger-update.ch/zusammenfassung/34558/) | Art. 42, 43 StGB | ✓ | Prognose beim teilbedingten Vollzug; Verhältnis zum Geld und fehlende Einsicht als Kriterien |
| [6B_741/2025](https://bger-update.ch/zusammenfassung/34554/) | Art. 67 Abs. 4bis StGB | ✓ Art. 67 | Strafhöhe allein bestimmt den besonders leichten Fall nicht |
| [6B_266/2026](https://bger-update.ch/zusammenfassung/34553/) | Art. 125 StGB | ✓ | Garantenstellung des Vorgesetzten bei selbst geschaffener Betriebsgefahr |
| [4A_290/2026](https://bger-update.ch/zusammenfassung/34548/) | Art. 4, 6 VVG | ○ | «körperliche» Erkrankung im Fragebogen erfasst keine psychischen Störungen |
| [4A_545/2025](https://bger-update.ch/zusammenfassung/34549/) | Art. 398 OR | ✓ | Conto vendita: Auftragsrecht statt Hinterlegung |
| [4A_93/2026](https://bger-update.ch/zusammenfassung/34586/) | Art. 398 Abs. 2 OR | ✓ | Sorgfalt der Treuhänderin bei MWST-Beratung: konkreter Einzelfall statt abstrakter Information |
| [4A_58/2026](https://bger-update.ch/zusammenfassung/34620/) | Art. 321c OR | ✓ | Überstunden ex aequo et bono schätzen, wenn beide Beweismittel unbrauchbar |
| [4A_340/2026](https://bger-update.ch/zusammenfassung/34547/) | Art. 208 ZPO / Art. 271 OR | ○ / ✓ | «definitiv» im Schlichtungsvergleich beendet das Mietverhältnis |
| [4A_316/2025](https://bger-update.ch/zusammenfassung/34626/) **5er** | Art. 259d, 288 OR | ○ | Verweigerung der Weinbau-Acquits als Sachmangel; Schadenssubstanziierung |
| [5A_165/2026](https://bger-update.ch/zusammenfassung/34587/) | Art. 274a ZGB | ✓ | Besuchsrecht der sozialen Mutter in der Regenbogenfamilie |
| [5A_987/2026](https://bger-update.ch/zusammenfassung/34567/) | Art. 13 HKÜ | ○ | Kindeswille bei Retardierung und Manipulation |
| Annex [AG HSU.2026.22](https://bger-update.ch/weitere/2924/) | Art. 16 ZGB | ✓ | relative Urteilsfähigkeit bei der Ausübung von Aktienstimmrechten |
| [8C_109/2026](https://bger-update.ch/zusammenfassung/34571/) | Art. 17, 30 AVIG | ✓ | Stellensuche während der Kündigungsfrist, nicht rein arithmetisch |
| [8C_313/2026](https://bger-update.ch/zusammenfassung/34573/) | Art. 52 ATSG | ✓ | keine Nachfrist für anwaltlich unbegründete Einsprache |
| Annex [VD 854](https://bger-update.ch/weitere/2722/) | Art. 14 AVIG | ✓ | Ende des Konkubinats ist kein Befreiungsgrund |
| [9C_494/2025](https://bger-update.ch/zusammenfassung/34622/) | Art. 30 MWSTG | ○ | Umsatzschlüssel bei gemischten Holdinggesellschaften ungeeignet |
| Annex [BVGer A-2934/2026](https://bger-update.ch/weitere/2934/) | Art. 20 MWSTG | ✓ | Aussenauftritt entscheidet über Stellvertretung |
| [9C_666/2025](https://bger-update.ch/zusammenfassung/34555/) | Art. 13 StHG / Art. 265 SchKG | ○ | Konkursverlustschein-Schulden nur bei Aussicht auf neues Vermögen abziehbar |
| Annex [BVGer A-4467/2025](https://bger-update.ch/weitere/2987/) | Art. 5, 6 DSG | ✓ Art. 6 | biometrische Stimmabdrücke: ausdrückliche Einwilligung, kein Opt-out |
| Annex [GE ACJC/1613/2026](https://bger-update.ch/weitere/2892/) | Art. 272 SchKG | ✓ | Glaubhaftmachung arrestierbarer Werte mit WhatsApp und E-Mail |
| Annex [GE DCSO/663/2026](https://bger-update.ch/weitere/928/) | Art. 41 Abs. 1bis SchKG | ○ | beneficium excussionis realis endet am Plafond der Bankgarantie |
| Annex [BVGer A-2637/2026](https://bger-update.ch/weitere/2994/) | Art. 21 Abs. 2 Ziff. 11 MWSTG | ○ | Bildungsleistungen nach dem konkreten Kursprogramm |
| Annex [VGer ZH VB.2025.00214](https://bger-update.ch/weitere/3110/), [OGer SO VWBES.2025.317](https://bger-update.ch/weitere/2789/) | Art. 8, 28b WG | ○ (WG nicht im Bestand) | ausländische Vorstrafen nach Schweizer Qualifikation; Sammlerbegriff |

Die Zuordnung zu Normen und die Angabe ✓/○ beruhen auf den Tickern und dem Stand von
`content/kommentar/` am 24.10.2026; Absatz- und Literaangaben am Volltext prüfen.
