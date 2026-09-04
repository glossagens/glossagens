---
name: praxisorientierter-kommentar
description: >-
  Standard für den Stil, Aufbau und die Kasuistik eines praxisorientierten Gesetzeskommentars bei Glossagens nach den Referenzmustern Art. 110 StPO und Art. 336 OR. Gilt immer dann, wenn ein Kommentar ausdrücklich als «praxisorientiert» angefordert oder ausgebaut werden soll. Kern: Sehr umfangreiche, plastische Beschreibungen der tatsächlichen Lebenssachverhalte aus publizierten Gerichtsurteilen — sowohl Fälle, in denen die Bestimmung angewandt wurde, als auch Fälle, in denen deren Anwendbarkeit verworfen wurde —, Schwellenwert-Gegenüberstellungen, Kasuistiktabellen, schonungslose Offenlegung echter Judikaturwidersprüche (ohne Scheinharmonisierung), prozessuale Klippen und taktische Merksätze.
version: 1.1.0
author: Antigravity Agent
tools:
  - mcp__fedlex-connector__get_article
  - mcp__fedlex-connector__get_law_text
  - mcp__fedlex-connector__search_by_title
  - mcp__fedlex-connector__list_amendments
  - mcp__entscheidsuche__search_by_case_number
  - mcp__entscheidsuche__search
  - mcp__entscheidsuche__fetch_document
metadata:
  glossagens:
    category: legal-commentary-style
    benchmarks: ["content/kommentar/stpo/art-110/_index.md", "content/kommentar/or/art-336/_index.md"]
---

# Leitfaden: Praxisorientierter Gesetzeskommentar

Dieser Skill definiert den massgebenden **Stil**, den **inhaltlichen Aufbau** und die **Kasuistik** für alle Glossagens-Kommentare, die **praxisorientiert** verfasst oder zu einem Praxiskommentar ausgebaut werden sollen.

---

## 1. Geltungsbereich und Zweck

Wann immer der Benutzer vorgibt:
- *«schreibe/erstelle den Kommentar praxisorientiert»*
- *«baue Art. X zu einem Praxiskommentar aus»*
- *«im Stil von Art. 110 StPO oder Art. 336 OR»*

gilt **dieser Skill als zwingende Stilleitlinie** ergänzend zu den allgemeinen Workflows von `glossagens-content-creation`.

### Abgrenzung zu Standardkommentaren

| Dimension | Akademischer / Konventioneller Kommentar | Praxisorientierter Kommentar (DIESER SKILL) |
|---|---|---|
| **Erkenntnisquelle** | Abstrakt-deduktiv aus Doktrin, Systematik und Gesetzestext | Konkret-induktiv aus tatsächlichen Lebenssachverhalten der Gerichtspraxis |
| **Urteilsdarstellung** | Schlagwort-Zitat: *«Das Bundesgericht bejahte Missbräuchlichkeit (BGE 131 III 535)»* | **Umfangreiche Sachverhaltserzählung**: Wer, was, welche Vorwürfe, welches Kündigungsschreiben, welche Entlastungsmomente, warum gekippt? |
| **Normgrenzen** | Aufzählung von Tatbestandsmerkmalen | **Zweiseitige Grenzkasuistik**: Ausführliche Gegenüberstellung von Fällen, in denen die Norm *angewandt* wurde, und Grenzfällen, in denen sie *verworfen* wurde |
| **Widersprüche** | Scheinharmonisierung («hängt vom Einzelfall ab», feine Sachverhaltsnuancen erfunden) | **Echte Brüche benennen**: Divergenzen zwischen Gerichten/Kammern offen als unvereinbar herausarbeiten |
| **Prozessrealität** | Fokus auf materiellrechtliche Auslegungsfragen | Fokus auf Beweislast, Fristen, Verwirkung, Versehensnachweis, Prozessfallen |
| **Orientierungshilfe** | Abstrakte Lehrmeinungsstreitigkeiten | **Taktische Merksätze** (`> **Merksatz.**`) und Handlungsanweisungen für Parteien und Behörden |
| **Textelement** | Fliessender Prosa-Kommentar | Dichte Kasuistik, Gegenüberstellungstabellen, wörtliche Kernzitate |

---

## 2. Die beiden Referenzmuster (Benchmarks)

Vor dem Verfassen eines praxisorientierten Kommentars sind die beiden Vorzeigekommentare im Repository zu konsultieren:

1. **Art. 110 StPO** (`content/kommentar/stpo/art-110/_index.md`):
   - *Thema*: Formstrenge vs. überspitzter Formalismus bei Eingaben.
   - *Praxis-Stil*: Ausführliche Schilderung realer Gerichtsentscheide (Telefax eines in Deutschland Inhaftierten am Freitagabend; USB-Stick bei Revision; Eingabe mit eingescannter Signatur; E-Mail-Entsiegelungsgesuch der Staatsanwaltschaft; Kasuistik ungebührlicher Rechtsschriften mit Gegenüberstellung extremer Beleidigungen vs. noch zulässiger harter Kritik).
2. **Art. 336 OR** (`content/kommentar/or/art-336/_index.md`):
   - *Thema*: Missbräuchliche Kündigung, verpönte Motive und ungeschriebene Tatbestände.
   - *Praxis-Stil*: Narrative Lebenssachverhalte (WhatsApp-Story eines Seilbahnmitarbeiters mit NS-Pass-Vergleich; Bankvize als Sündenbock nach Millionenveruntreuung eines Dritten; Verdachtskündigung nach anonymer Ombudsfrauen-Meldung und Reichweite von StPO-Garantien; Covid-19-Impfobligatorium bei Flight Attendants; Tabellenvergleich zwischen geschützter und ungeschützter Alterskündigung: 60 J./37 Dienstjahre VR-Präsident vs. 58 J./32 Dienstjahre Sachbearbeiter).

---

## 3. Die 7 Grundregeln des praxisorientierten Stils

### Regel 1: Narrative Sachverhaltsschilderung («Storytelling aus den Akten»)

Abstrakte Rechtsregeln sind für die Praxis wertlos, wenn nicht klar ist, auf welche Lebenssachverhalte sie zutreffen. Jeder ausgewertete Entscheid wird mit seinem **konkreten Lebenssachverhalt** eingeführt.

#### Was in die Sachverhaltsschilderung gehört:
1. **Die Akteure**: Funktion, Branche, Dienstjahre, Alter, Hierarchiestufe, Rollen (z.B. *«Ein seit 2011 fest angestellter Seilbahn- und Rodelbahnangestellter...»*, *«Ein selbst als Rechtsanwalt tätiger Beschuldigter...»*, *«Die Staatsanwaltschaft Limmattal/Albis...»*).
2. **Der konkrete Konflikt / das Verhalten**: Exakte Zitate der beanstandeten Aussagen, exakter Übermittlungsweg, genaue Daten, Fristen und Zeitabstände (z.B. *«vier Arbeitstage nach der Veröffentlichung»*, *«am Freitagabend um 18.26 Uhr per Telefax»*).
3. **Das Vorgehen der Gegenseite / Behörde**: Wurde verwarnt? Wurde eine Nachfrist gesetzt? Wie begründete das erstinstanzliche Gericht sein Nichteintreten oder seine Abweisung?
4. **Die Weichenstellung des Obergerichts / Bundesgerichts**: Warum genau kippte der Fall? Welche Erwägung gab den Ausschlag?

#### Negativ-Beispiel (abstrakt, verboten):
> Eine Kündigung wegen Äusserungen im privaten Umfeld kann zulässig sein, wenn betriebliche Interessen berührt sind (BGer 4A_368/2023). Auch bei Krankheit ist eine Kündigung nach Fristablauf meist nicht missbräuchlich.

#### Positiv-Beispiel (praxisorientiert, verbindlich):
> **Meinungsäusserung: die WhatsApp-Story eines Seilbahnangestellten**  
> Ein seit 2011 fest angestellter Seilbahn- und Rodelbahnangestellter veröffentlichte Anfang September 2021 auf seinem privaten Mobiltelefon eine dreiteilige WhatsApp-«Story». Im dritten Teil zeigte er das Bild eines «Gesundheitspasses» aus der nationalsozialistischen Zeit samt Hakenkreuz mit der Bemerkung: «Die Geschichte wiederholt sich und wir, die das vorausgesehen hatten, sind die Verschwörungstheoretiker. Leider nicht, kann man dazu sagen.» Der Vorgesetzte schrieb ihm per WhatsApp, extreme Statusmeldungen mit NS-Bezug im Unternehmen nicht zu tolerieren. Am 15. September 2021 kündigte die Arbeitgeberin — sechs Tage bzw. vier Arbeitstage nach der Veröffentlichung — und nannte die Story sowie frühere Verwarnungen (Maskenpflichtmissachtung, Befahren einer gesperrten Piste).  
> **Erster Schritt: Die Äusserung ist geschützt.** Das Kantonsgericht hielt fest, der Vergleich des Corona-Zertifikats mit dem NS-Gesundheitspass sei zwar geschmacklos und schockierend, überschreite aber den Rahmen von Art. 16 Abs. 2 BV nicht ([SG KG BO.2024.11-K3 E. III/4b](https://entscheidsuche.ch/docs/SG_Gerichte/SG_KG_002_BO-2024-11-K3_2024-12-27.pdf)).  
> **Zweiter Schritt: Die Klage scheitert trotzdem.** Weil der Kläger zuvor bereits wegen Sicherheitsverstössen verwarnt worden war, zeigte die Story, dass er Massnahmen bewusst missachtete. Er konnte nicht nachweisen, dass die Kündigung *ohne* die früheren Verwarnungen allein wegen der Äusserung erfolgt wäre ([E. III/5d](https://entscheidsuche.ch/docs/SG_Gerichte/SG_KG_002_BO-2024-11-K3_2024-12-27.pdf)).

---

### Regel 2: Zweiseitige Grenzkasuistik — Angewandt vs. Verworfen

Praktiker lesen einen Kommentar, um die **Grenze des rechtlich Möglichen** auszuloten. Daher müssen zu jedem Streitpunkt zwingend beide Richtungen mit ausführlichen Sachverhalten dargestellt werden:

1. **Anwendungsfälle (Tatbestand bejaht / Klage geschützt / Rechtsfolge ausgelöst)**:
   - Sachverhalte, in denen die Gerichte die Hürde als genommen ansahen.
2. **Verwerfungsfälle (Tatbestand verneint / Anwendbarkeit verworfen / Rechtsfolge verweigert)**:
   - Sachverhalte, in denen eine Partei die Norm anrief, das Gericht aber abwies (weil Schwelle nicht erreicht, Gegenausnahme griff, Kausalität fehlte oder ein Rechtfertigungsgrund vorlag).

#### Der didaktische Zweck:
Durch die Gegenüberstellung von *«Gerade noch geschützt / missbräuchlich / ungebührlich»* und *«Noch zulässig / verworfen»* wird der Schwellenwert der Gerichte greifbar.

---

### Regel 3: Echte Judikaturwidersprüche offenlegen (Verbot der Scheinharmonisierung)

Juristische Urteile stehen nicht immer in eleganter Harmonie zueinander; sie können zueinander in **echtem, unauflösbarem Widerspruch** stehen:
- zwischen verschiedenen Abteilungen oder Kammern desselben Gerichts (z.B. I. öffentlich-rechtliche vs. strafrechtliche Kammer des BGer; verschiedene Zivilkammern eines Obergerichts),
- zwischen der kantonalen Gerichtspraxis (Obergerichte / Kantonsgerichte) und dem Bundesgericht,
- oder im Zeitablauf bei schleichenden oder uneinheitlich vollzogenen Praxisänderungen.

#### Das Verbot der Scheinharmonisierung:
Es ist ein schwerer methodischer Fehler, solche Brüche in der Judikatur **künstlich weg-zuharmonisieren**, indem man behauptet, die Entscheide liessen sich durch vermeintliche Nuancen im Sachverhalt (z.B. minimale Altersunterschiede, Branchenbesonderheiten oder kantonale Herkunft) widerspruchsfrei erklären, obwohl die Gerichte in Wahrheit gegensätzliche rechtliche Massstäbe oder Wertungen angewandt haben.

> **Grundsatz:** Wo Gerichte bei im Kern vergleichbaren Sachverhalten unvereinbare Massstäbe anlegen, wird dieser Widerspruch **offen, präzise und ungeschönt beim Namen genannt** — anstatt ihn mit Scheindifferenzierungen zu übertünchen.

#### Wie Widersprüche darzustellen sind:
1. **Den Konflikt klar benennen**: Explizite Abschnitte wie *«Uneinheitliche Praxis / Judikaturdivergenz»*, *«Gespaltener Massstab»* oder *«Widerspruch zwischen Bundesgericht und kantonaler Praxis»*.
2. **Die unvereinbaren Linien konfrontieren**: Sachverhalte beider Entscheide schildern und zeigen, warum die jeweiligen Begründungen sachlich nicht zusammenpassen.
3. **Keine Scheinerklärungen konstruieren**: Keine Randtatsachen als Erklärung vorschieben, die das Gericht selbst gar nicht als tragend gewertet hat.
4. **Prozessuale Taktik herausarbeiten**:
   - Für die Rechtsmittelpraxis: Ein offener Widerspruch ist der stärkste Hebel, um eine Rechtsfrage von grundsätzlicher Bedeutung zu begründen, eine Plenar- oder Fünferbesetzung (z.B. Art. 23 BGG) zu verlangen oder eine Praxisänderung anzuregen.
   - Für das Instanzgericht: Parteien können gezielt die für sie günstigere Linie unter Hinweis auf die Divergenz einfordern.

---

### Regel 4: Strukturierte Kasuistik- und Kriterientabellen

Wo mehrere Entscheide denselben Tatbestand konkretisieren, fasst eine **Vergleichstabelle** die Sachverhaltskerne und Ergebnisse zusammen.

#### Muster A: Grenzziehungs-Tabelle (z.B. aus Art. 110 StPO)
```markdown
| Sachverhalt / Formulierung | Beurteilung | Entscheid |
|---|---|---|
| Der Bezirksgerichtspräsident sei «womöglich ein schwules Arschloch», «allenfalls ein Rechtsverdreher» | ungebührlich; Relativierungen ändern nichts | [BGer 6B_1272/2017 E. 3.2](https://entscheidsuche.ch/docs/CH_BGer/CH_BGer_006_6B-1272-2017_2018-02-23.html) |
| Vorwurf an zwei Bundesanwälte, sie hätten Gerichte vorsätzlich getäuscht («pour tromper sciemment et volontairement les juges») — ohne jeden Anhaltspunkt | **noch nicht** ungebührlich; unbegründete Kritik bleibt geschützt, solange sachbezogen | [BStGer BB.2020.288 E. 5.3](https://entscheidsuche.ch/docs/CH_BSTG/CH_BSTG_001_BB-2020-288_2021-02-15.pdf) |
```

#### Muster B: Fallvergleichs-Tabelle zweier Leitentscheide (z.B. aus Art. 336 OR)
```markdown
| Kriterium | [BGer 4A_44/2021](https://entscheidsuche.ch/docs/CH_BGer/CH_BGer_004_4A-44-2021_2021-06-02.html) — **nicht** missbräuchlich | [AG OG ZOR.2025.11](https://entscheidsuche.ch/docs/AG_Gerichte/AG_OG_001_ZOR-2025-11_2025-09-01.pdf) — **missbräuchlich** |
|---|---|---|
| Alter / Dienstjahre | 60 Jahre / 37 Jahre | 58 Jahre / 32 Jahre |
| Hierarchiestufe | VR-Mitglied und CEO, Familienmitglied, hoher Lohn | Sachbearbeiter ohne Führung, Normalgehalt |
| Weiterbeschäftigung | faktisch ausgeschlossen | konkret möglich (Stelle per 1.1. neu besetzt) |
| Ergebnis | Kündigung geschützt | Vier Monatslöhne Pönale zugesprochen |
```

---

### Regel 5: Harte Prozessrealität statt Elfenbeinturm

Praxiskommentare sparen nicht an den prozessualen Klippen, an denen Verfahren in der Praxis scheitern. Sie arbeiten systematisch heraus:

1. **Beweislast und Beweismass**:
   - Wer muss was beweisen? Reicht Glaubhaftmachen oder gilt das Regelbeweismass der vollen Überzeugung?
   - Wie weist man innere Tatsachen nach (z.B. Kündigungsmotiv, Vorsatz, Rechtsmissbrauch)?
2. **Formstrenge und Fristenfalle**:
   - Welche Mängel sind mit Nachfrist heilbar (blosses Versehen) und welche führen zum sofortigen Rechtsverlust (bewusst gewählter Übermittlungsweg, Telefax, unvollständige elektronische Eingabe)?
   - Geltung für Behörden: Trifft Staatsanwaltschaft oder Verwaltung dieselbe Formstrenge wie Private?
3. **Substanziierung und Rügeobliegenheiten**:
   - Welche Tatsachen müssen bereits in der Ersteingabe detailliert dargelegt werden?
   - Was gilt als unzulässiges Nachschieben von Gründen?

---

### Regel 6: Taktische Merksätze («Merksatz.»)

Jeder Hauptabschnitt schliesst mit einem hervorgehobenen Merksatz oder mit Handlungsanweisungen für die Prozessparteien ab.

#### Format für Einzelmerksätze:
```markdown
> **Merksatz.** Alter und Dienstjahre allein tragen keine Klage. Sie erhöhen den Massstab, an dem die Art und Weise gemessen wird — und dieser Massstab wird umso strenger, je weiter unten in der Hierarchie der Arbeitnehmer steht und je konkreter eine Weiterbeschäftigung möglich gewesen wäre.
```

#### Format für Rollen-Merksätze:
```markdown
#### Die Merksätze für die Praxis
- **Für die Klagepartei / Verteidigung**: Der Angriff auf eine [...] geht ins Leere, wenn [...]. Wer sich auf [...] berufen will, muss zwingend nachweisen, dass [...].
- **Für die Beklagte / Staatsanwaltschaft**: Wer als Behörde [...] verlangt, muss [...]. Bei Kündigungen schützt eine lückenlos dokumentierte Vorgeschichte vor [...].
```

---

### Regel 7: Absolutes Grounding & wörtliche Schlüsselerwägungen

Praxiskommentare enthalten niemals erfundene Urteilssachverhalte oder spekulative Sachverhaltsdetails.
- **Volltextrecherche**: Jeder geschilderte Sachverhalt stammt aus einem Urteil, das über `entscheidsuche.ch` oder `mcp.opencaselaw.ch` im Volltext gesichtet wurde.
- **Wörtliche Zitate**: Die entscheidende Begründung des Gerichts wird als Blockzitat (`> «...»`) verbatim übernommen.
- **Exakte Verlinkung**: Verlinkung auf `entscheidsuche.ch` (bzw. opencaselaw-Fallback), bei BGE-Entscheiden wenn möglich mit Erwägungsanker (`#consideration_X.Y`).

---

## 4. Gliederung und Umfang im Page Bundle

Ein praxisorientierter Kommentar wird als vollwertiges Page Bundle angelegt:

```text
content/kommentar/{gesetz}/art-{nr}/
├── _index.md            ← Hauptkommentar mit detaillierter Kasuistik (Branch Bundle)
└── rechtsprechung.md    ← Rechtsprechungsübersicht (mind. 10 strukturierte Entscheide)
```

### Aufbau des Hauptkommentars (`_index.md`)

1. **Frontmatter**:
   - `description`: Erwähnt explizit die Ausrichtung als Praxiskommentar und die wichtigsten Fallgruppen/Kasuistiken.
   - `tags`: Umfasst spezifische Sachverhalts- und Kasuistik-Schlagworte.
   - `revisions`: Vollständiger Nachweis der ausgewerteten Volltexte und Verifikationen.
2. **Gesetzeswortlaut**:
   - Verbatim nach Fedlex, gegliedert nach Absätzen, mit historischem Gesetzesstand.
   - Bei komplexen Normen: Eine vorangestellte Übersichtstabelle («Die Tatbestände auf einen Blick»).
3. **Überblick und Bedeutung**:
   - 1–2 Absätze zur praktischen Tragweite und den typischen Stolpersteinen in der Praxis.
   - **Prüfschema / Schichten-Tabelle**: Übersicht über die logische Prüfungsreihenfolge und wer die Beweislast trägt.
   - Zentrale Leitentscheide im wörtlichen Zitat.
4. **Kommentierung (Abschnitte A, B, C...)**:
   - Gliederung nach Absätzen oder Kernproblemen.
   - Jeder Abschnitt enthält:
     - Dogmatische Grundlinie (prägnant).
     - **Ausführliche Sachverhalte konkreter Urteile** (siehe Regel 1).
     - **Gegenüberstellung angewandter vs. verworfener Fälle** (siehe Regel 2).
     - **Offenlegung echter Judikaturwidersprüche ohne Scheinharmonisierung** (siehe Regel 3).
     - **Kasuistik- oder Vergleichstabelle** (siehe Regel 4).
     - **Taktische Merksätze** (siehe Regel 6).
5. **Kantonale Praxisfragen**:
   - Mindestens 1–2 konkrete Streitpunkte oder Verfahrensdivergenzen kantonaler Gerichte (z.B. Obergerichte ZH, BE, SG, AG, LU).

---

## 5. Qualitäts-Checkliste für den praxisorientierten Kommentar

Vor dem Commit ist der geschriebene Text gegen folgende Punkte zu prüfen:

- [ ] **Sachverhaltstiefe**: Werden die Urteile als reale Geschichten mit Berufsbezeichnungen, Dienstjahren, Verhaltensweisen, Datumsangaben und Parteivorbringen geschildert (keine Einzeiler-Zitate)?
- [ ] **Doppelte Kasuistik**: Sind zu den Hauptstreitpunkten sowohl Fälle enthalten, in denen das Gericht die Norm angewandt hat, als auch Fälle, in denen es die Anwendung verworfen hat?
- [ ] **Widersprüche offengelegt**: Wurden echte Judikaturdivergenzen und Widersprüche zwischen Gerichten, Kammern oder im Zeitablauf klar benannt, anstatt sie künstlich über feine Sachverhaltsunterschiede wegzuerklären?
- [ ] **Tabellarische Vergleiche**: Gibt es mindestens eine strukturierte Tabelle, die Grenzfälle oder gegensätzliche Gerichtsentscheide nebeneinanderstellt?
- [ ] **Prozessuale Klippen**: Werden Beweislast, Fristen, Verwirkung, Versehensnachweis oder Substanziierungsobliegenheiten explizit thematisiert?
- [ ] **Merksätze vorhanden**: Enthalten die massgebenden Abschnitte prägnante `> **Merksatz.**`-Blöcke oder Rollen-Merksätze für Anwälte/Behörden?
- [ ] **Volltext-Verifikation**: Ist jeder Sachverhalt und jedes wörtliche Zitat gegen das Originalurteil auf `entscheidsuche.ch` abgeglichen (keine Halluzinationen)?
- [ ] **Schweizer Rechtschreibung**: Durchgehend kein Eszett («ss»), korrekte Schweizer Rechtsterminologie.
