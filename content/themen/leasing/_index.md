---
title: "Leasing im schweizerischen Recht"
date: 2026-10-24
lastmod: 2026-10-24
description: "Begriff, Erscheinungsformen und dogmatische Einordnung des Leasingvertrags im schweizerischen Recht: Innominatkontrakt sui generis, Dreiparteienverhältnis, Risikoverteilung, zwingender Konsumentenschutz nach KKG sowie sachen-, betreibungs- und strafrechtliche Aspekte."
tags: ["Leasing", "Finanzierungsleasing", "Operating Leasing", "Innominatvertrag", "Konsumkreditgesetz", "KKG", "Mietrecht", "Sicherungseigentum"]
typ: grundlage
kurz: "Beim Leasing überlässt der Leasinggeber dem Leasingnehmer ein Investitions- oder Konsumgut gegen periodische Raten zum Gebrauch, während das volle Erhaltungs- und Sachrisiko regelmässig auf den Leasingnehmer übertragen wird. Das schweizerische Recht regelt das Leasing nicht als eigenständigen Nominatkontrakt im OR, sondern stuft es als Innominatvertrag (Gebrauchsüberlassungsvertrag sui generis mit Elementen aus Miete, Kauf und Darlehen) ein. Für das private Konsumgüterleasing gelten die zwingenden Schutzbestimmungen des Konsumkreditgesetzes (KKG), insbesondere Schriftform, Kreditfähigkeitsprüfung und vorzeitiges Kündigungsrecht."
sachgebiete: [schuldrecht.miete, schuldrecht.darlehen, schuldrecht.kauf]
normen:
  - { gesetz: or, art: art-019 }
  - { gesetz: or, art: art-164 }
  - { gesetz: or, art: art-184 }
  - { gesetz: or, art: art-253 }
  - { gesetz: or, art: art-312 }
  - { gesetz: or, art: art-107 }
  - { gesetz: zgb, art: art-641 }
  - { gesetz: schkg, art: art-093 }
  - { gesetz: schkg, art: art-242 }
  - { gesetz: stgb, art: art-138 }
stichworte: ["Leasing", "Finanzierungsleasing", "Operating Leasing", "Innominatvertrag", "Konsumgüterleasing", "Investitionsgüterleasing", "Konsumkreditgesetz", "KKG", "Amortisationstabelle", "Restwert", "Freizeichnung", "Dreiecksverhältnis"]
agent_verified: true
revisions:
  - date: 2026-10-24
    by: "Antigravity"
    model: "gemini-3.8-flash"
    mcp_verified: true
    note: "Erstfassung nach Skill glossagens-themen (Typ grundlage). Normtexte OR per {{< wortlaut >}} aus der Fedlex-Konsolidierung (scripts/wortlaut.py). Alle 12 Entscheide als Volltext von entscheidsuche.ch geladen; Erwägungsnummern, Anker und jedes wörtliche Zitat gegen den Volltext abgeglichen (pruefen.py)."
---

## Überblick {#ueberblick}

Das Leasing (aus dem Englischen *to lease* = mieten, pachten) ist eine der bedeutendsten modernen Formen der Absatz- und Investitionsfinanzierung in der Schweiz. Ob Fahrzeugflotten von Unternehmen, industrielle Produktionsmaschinen, Spital- und IT-Infrastruktur oder Personenwagen für Privatpersonen: Das Leasing ermöglicht die wirtschaftliche Nutzung eines Guts, ohne dass der Nutzer beim Erwerb den vollen Kaufpreis aus eigenen Mitteln aufbringen muss.

Der wirtschaftliche Kern des Leasings liegt in der **Trennung von rechtlichem Eigentum und wirtschaftlicher Nutzung**:
- Das **rechtliche Eigentum** verbleibt bei der Leasinggesellschaft (Leasinggeber) und dient dieser als primäre Kreditsicherheit.
- Die **wirtschaftliche Nutzung**, aber auch die **Sach- und Preisgefahr** (Unterhalt, Reparaturen, Gefahr des zufälligen Untergangs oder der Beschädigung) werden auf den Nutzer (Leasingnehmer) überwälzt.

Im schweizerischen Obligationenrecht (OR) sucht man ein eigenes «Leasingrecht» vergebens. Der Gesetzgeber hat das Leasing weder bei der Kodifikation des OR noch bei späteren Teilrevisionen als eigenständigen Nominatvertrag geregelt. Das Leasing beruht vielmehr auf der verfassungs- und zivilrechtlichen Vertragsfreiheit (Art. 19 Abs. 1 OR) und wird von Lehre und Rechtsprechung einhellig als **Innominatvertrag** qualifiziert. Wo Private als Konsumenten bewegliche Sachen leasen, greift zum Schutz vor Überschuldung das zwingende Bundesgesetz über den Konsumkredit (KKG).

| Dimension | Ausprägung beim Finanzierungsleasing | Klassische Miete (Art. 253 OR) | Kauf auf Abzahlung / Kreditkauf |
|---|---|---|---|
| **Vertragstypus** | Innominatvertrag (Gebrauchsüberlassung sui generis) | Gesetzlicher Nominatvertrag (Art. 253 ff. OR) | Gesetzlicher Nominatvertrag (Art. 184 / Art. 214 OR) |
| **Zivilrechtliches Eigentum** | Bleibt beim Leasinggeber (zur Kreditsicherung) | Bleibt beim Vermieter | Geht auf den Käufer über (sofern kein Eigentumsvorbehalt) |
| **Wirtschaftliche Stellung** | Leasingnehmer trägt Risiko und Ertrag (Quasi-Eigentümer) | Vermieter trägt Investitions- und Marktrisiko | Käufer ist Voll- und Sachberechtigter |
| **Sach- und Erhaltungsgefahr** | Vollständig beim Leasingnehmer (Unterhalt, Versicherung) | Beim Vermieter (Art. 256 Abs. 1 OR) | Beim Käufer (Art. 185 OR) |
| **Entgelt** | Zins und Amortisation des Anschaffungswerts | Reine Gegenleistung für Gebrauchsüberlassung | Kaufpreisabzahlung plus Finanzierungszins |
| **Gesetzliche Schranken** | Konsumkreditgesetz (KKG) bei Privatgebrauch; Art. 19/20 OR | Zwingendes Mietrecht (Art. 253 ff. OR) | KKG bei Konsumkrediten; ZGB/SchKG |

## Begriff und Rechtsgrundlage {#begriff-und-rechtsgrundlage}

Da das OR den Leasingvertrag nicht eigens kodifiziert hat, gründet die Rechtsfigur unmittelbar auf dem Grundsatz der Vertragsfreiheit:

{{< wortlaut gesetz="or" art="art-019" >}}

Gestützt auf Art. 19 Abs. 1 OR können die Vertragsparteien den Inhalt eines Vertrags innerhalb der Schranken des Gesetzes beliebig gestalten. Sie sind nicht an die gesetzlich geregelten Vertragstypen (wie Kauf, Miete, Pacht, Darlehen oder Auftrag) gebunden. Grenzen setzen allein die zwingenden Vorschriften des Gesetzes, die öffentliche Ordnung, die guten Sitten und das Persönlichkeitsrecht (Art. 19 Abs. 2 und [Art. 20 Abs. 1 OR](/kommentar/or/art-020/)).

Das schweizerische Recht kennt zwei Grundformen atypischer Verträge:
1. **Gemischte Verträge**: Vereinbarungen, die Elemente verschiedener gesetzlicher Vertragstypen in sich vereinigen (z. B. Miete und Kauf).
2. **Verträge sui generis**: Verträge mit einem völlig eigenständigen, im Gesetz nicht vorgezeichneten Leistungsinhalt.

Das Leasing weist Merkmale beider Konstruktionen auf: Es verbindet mietrechtliche Elemente der Gebrauchsüberlassung (Art. 253 OR) mit kaufrechtlichen Aspekten der Beschaffung und des allfälligen späteren Eigentumserwerbs (Art. 184 OR) sowie kreditrechtlichen Komponenten der Vorfinanzierung und Amortisation (Art. 312 OR).

## Die Formel des Bundesgerichts und Begriffsmerkmale {#formel}

Das Bundesgericht hat die typische Grundstruktur und das Wesen des Leasingvertrags in ständiger Rechtsprechung präzisiert:

> «Ein Leasingvertrag in seiner typischen Grundstruktur besteht darin, dass die eine Partei (Leasinggeber) der anderen (Leasingnehmer) auf eine fest bestimmte Zeit ein wirtschaftliches Gut (Leasingobjekt) zur freien Verwendung und Nutzung überlässt, wobei das volle Erhaltungsrisiko in der Regel auf den Leasingnehmer übertragen wird.»
>
> — [Urteil 4A_404/2008 vom 18. Dezember 2008](https://entscheidsuche.ch/docs/CH_BGer/CH_BGer_004_4A-404-2008_2008-12-18.html) E. 4.1.1

Das Entgelt wird in Teilleistungen entrichtet (sogenannter *Leasingzins* bzw. Leasingraten). Die kapitalisierten Raten ergeben einen Betrag, der dem auf das Vertragsende verzinsten Verkehrswert im Zeitpunkt des Vertragsschlusses entspricht (Vollamortisation) oder zusammen mit einem kalkulierten Restwert die Gesamtkosten deckt (Teilamortisation).

Aus der Rechtsprechung ergeben sich vier kumulative Wesensmerkmale des Finanzierungsleasings:

1. **Gebrauchsüberlassung auf feste Dauer**: Das Leasingobjekt wird dem Leasingnehmer für eine feste, während der Grundvertragsdauer ordentlich unkündbare Frist überlassen (typischerweise drei bis fünf Jahre bei Fahrzeugen und Investitionsgütern), die sich an der voraussichtlichen wirtschaftlichen Nutzungsdauer orientiert.
2. **Finanzierungs- und Amortisationsfunktion**: Der Leasingzins stellt nicht bloss ein Nutzungsentgelt dar, sondern amortisiert das vom Leasinggeber für die Anschaffung eingesetzte Kapital zuzüglich Verzinsung, Gemeinkosten und Gewinnmarge ([BGE 118 II 150](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_004_BGE-118-II-150_1992-04-30.html#consideration_4.) E. 4b).
3. **Risikoverlagerung auf den Nutzer**: Im Gegensatz zum klassischen Mietvertrag, bei dem der Vermieter die Sache in gebrauchsfähigem Zustand zu erhalten hat (Art. 256 Abs. 1 OR), übernimmt der Leasingnehmer sämtliche mit der Sache verbundenen Risiken und Lasten (Wartung, Reparaturen, Versicherung, Gefahr des zufälligen Untergangs oder der Beschädigung).
4. **Mehrere Optionen am Vertragsende**: Nach Ablauf der festen Vertragsdauer stehen dem Leasingnehmer regelmässig verschiedene Optionen offen: die Rückgabe der Sache, die Verlängerung des Vertrags, der Abschluss eines neuen Leasingvertrags über ein moderneres Nachfolgeobjekt oder der Kauf der Sache zu einem vorausbestimmten oder noch zu vereinbarenden Restwert ([BGE 118 II 150](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_004_BGE-118-II-150_1992-04-30.html#consideration_4.) E. 4b).

## Typologie und Erscheinungsformen {#erscheinungsformen}

In der Praxis treten unterschiedliche Erscheinungsformen des Leasings auf, die sich in ihrer Rechtsnatur und Risikoverteilung wesentlich voneinander unterscheiden:

### Finanzierungsleasing vs. Operating Leasing {#finanzierungs-vs-operating-leasing}

Das Bundesgericht hebt hervor:

> «Die wichtigste Erscheinungsform des Leasings ist das Finanzierungsleasing, vorab das Mobilienleasing. Bei diesem ist eine rechtliche Dreiecksbeziehung charakteristisch.»
>
> — [Urteil 4A_404/2008](https://entscheidsuche.ch/docs/CH_BGer/CH_BGer_004_4A-404-2008_2008-12-18.html) E. 4.1.1

- **Finanzierungsleasing (*Finance Lease*)**: Feste unkündbare Grunddauer, Amortisation der Anschaffungskosten über die Leasingraten, vollständige Abwälzung der Sach- und Preisgefahr auf den Leasingnehmer. Die Finanzierungs- und Kreditfunktion steht im Vordergrund.
- **Operating-Leasing (*Operatives Leasing*)**: Kurzfristige, jederzeit oder mit kurzen Fristen kündbare Gebrauchsüberlassung. Das Amortisations-, Erhaltungs- und Verwertungsrisiko verbleibt beim Leasinggeber. Das Operating-Leasing steht dem gesetzlichen Mietvertrag (Art. 253 ff. OR) so nahe, dass die mietrechtlichen Normen weitgehend unmittelbar anwendbar sind ([BGE 113 II 168](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_004_BGE-113-II-168_1987-05-20.html#consideration_2.) E. 2: «häufig wird ohnehin aus Werbegründen ein gewöhnlicher Mietvertrag als Leasing bezeichnet»).

### Konsumgüter- vs. Investitionsgüterleasing {#konsum-vs-investitionsgueter}

Die Unterscheidung richtet sich nach dem **Verwendungszweck des Leasingobjekts** ([BGE 118 II 150](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_004_BGE-118-II-150_1992-04-30.html#consideration_4.) E. 4a):
- **Investitionsgüter**: Güter, die im Geschäftsbetrieb eines Unternehmens für gewerbliche Zwecke eingesetzt werden, massgebend ist, ob «mit ihnen Geld verdient werden kann und soll» (BGE 118 II 150 E. 4a; BGE 103 II 118). Hier herrscht weitgehende Vertragsfreiheit.
- **Konsumgüter**: Güter, die dem privaten, nicht geschäftlichen Gebrauch natürlicher Personen dienen (z. B. das private Pendler- oder Familienfahrzeug). Beim Konsumgüterleasing schützt das Gesetz den Leasingnehmer als schwächere Partei durch die zwingenden Vorschriften des Konsumkreditgesetzes (KKG).

### Direktes vs. indirektes Leasing {#direktes-vs-indirektes-leasing}

- **Direktes Leasing (Herstellerleasing)**: Der Hersteller oder Lieferant schliesst den Leasingvertrag unmittelbar mit dem Kunden ab (Zweiparteienverhältnis).
- **Indirektes Leasing**: Das klassische Dreiparteienverhältnis zwischen Lieferant, Leasinggesellschaft und Leasingnehmer. Die Leasinggesellschaft tritt rein als Finanziererin auf.

### Immobilienleasing {#immobilienleasing}

Beim gewerblichen Immobilienleasing erwirbt die Leasinggesellschaft ein Grundstück oder errichtet darauf eine Betriebsliegenschaft nach den Vorgaben des Leasingnehmers, um sie diesem langfristig (oft 15 bis 25 Jahre) gegen Leasingzins zu überlassen. Das Bundesgericht hielt in [BGE 132 III 549](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_005_BGE-132-III-549_2006.html#consideration_2.1.2) E. 2.1.2 fest:

> «Der Immobilien-Leasingvertrag ist kein Vertrag auf Eigentumsübertragung, welcher gemäss Art. 216 Abs. 1 OR und Art. 657 Abs. 1 ZGB der öffentlichen Beurkundung bedürfte»
>
> «Der Leasingvertrag beinhaltet das Recht auf die Nutzung und den Gebrauch des Leasingobjektes während der Leasingdauer gegen Bezahlung eines Leasingzinses durch den Leasingnehmer.»

Ein Formzwang der öffentlichen Beurkundung besteht beim Immobilienleasing nur insoweit, als dem Leasingnehmer ein verbindliches Kaufsrecht im Sinne von Art. 216 Abs. 2 OR eingeräumt wird (BGE 132 III 549 E. 2.1.2).

## Dogmatische Einordnung: Innominatvertrag sui generis {#dogmatische-einordnung}

Das Bundesgericht hat die Zuordnung des Finanzierungsleasings in Leitentscheid [BGE 118 II 150](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_004_BGE-118-II-150_1992-04-30.html#consideration_4.) E. 4b grundlegend geklärt:

> «Der Finanzierungsleasingvertrag lässt sich keinem herkömmlichen Vertragstypus des schweizerischen Rechts zuordnen. Es handelt sich um einen Innominatvertrag»

In der juristischen Lehre wurden historisch drei Hauptansätze vertreten:
1. **Gebrauchsüberlassungsvertrag sui generis** (herrschende Meinung und kantonale Praxis, bestätigt in BGE 118 II 150 E. 6b): Im Vordergrund steht die Gebrauchsüberlassung auf Zeit. Weil dem Leasinggeber keine Veräusserungsabsicht unterstellt werden kann, handelt es sich um keinen Kaufvertrag.
2. **Gemischter Vertrag mit miet-, kauf- und darlehensrechtlichen Elementen** (u.a. Urteil 4A_404/2008 E. 4.1.2): Wegen der Verteilung von Zins und Amortisation weist der Vertrag Kreditcharakter auf, während die Nutzungsüberlassung mietrechtlichen Grundsätzen folgt.
3. **Veräusserungsvertrag auf Abzahlung** (Minderheitsmeinung): Teilweise wurde postuliert, das wirtschaftliche Eigentum stehe so stark im Vordergrund, dass Abzahlungsrecht anzuwenden sei. Das Bundesgericht verwarf eine generelle Gleichstellung mit Veräusserungsverträgen namentlich dann, wenn am Vertragsende keine automatische Eigentumsübertragung vereinbart ist (BGE 118 II 150 E. 6c; [BGE 119 II 236](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_004_BGE-119-II-236_1993-05-25.html#consideration_4.) E. 4).

Massgebend ist die Konstruktion des **Sicherungseigentums**: Der Vertrag räumt dem Leasingnehmer
> «wirtschaftlich die Stellung eines Eigentümers des Leasingobjektes einräumt, jedoch der Leasinggesellschaft das rechtliche Eigentum am Leasingobjekt zur Sicherung ihrer Forderung belässt»
>
> — BGE 118 II 150 E. 6c

Da das rechtliche Eigentum dem Leasinggeber zur Sicherung zusteht, behält er bei Vertragsstörungen und Insolvenz die sachenrechtliche Rechtsstellung des Eigentümers.

## Das Dreiecksverhältnis und die Gewährleistungsstruktur {#dreiecksverhaeltnis}

Das indirekte Finanzierungsleasing beruht auf einer zweistufigen Vertragsbeziehung zwischen drei Akteuren:

```text
       ┌──────────────── Kaufvertrag (Art. 184 OR) ──────────────┐
       │                                                         │
       ▼                                                         │
┌───────────────┐                                         ┌──────────────┐
│ Leasinggeber  │                                         │  Lieferant   │
│ (Finanzierer) │                                         │  (Händler)   │
└───────┬───────┘                                         └──────┬───────┘
        │                                                        │
        │ Leasingvertrag (Innominatvertrag)                      │ Direkte
        │ samt Abtretung der Gewährleistungsrechte               │ Ablieferung
        ▼ (Art. 164 OR)                                          ▼
┌────────────────────────────────────────────────────────────────┐
│                         Leasingnehmer                          │
│                            (Kunde)                             │
└────────────────────────────────────────────────────────────────┘
```

In diesem Gefüge hielt das Bundesgericht fest:
> «die Leasinggesellschaft (Leasinggeber, crédit-bailleur) erwirbt auf eigene Kosten gemäss den Anweisungen ihres Kunden (Leasingnehmer) das zu finanzierende Objekt beim Lieferanten. Dieser ist am Leasingvertrag nicht direkt als Vertragspartei beteiligt.»
>
> — BGE 118 II 150 E. 4b; [Urteil 4C.204/2003 vom 5. März 2004](https://entscheidsuche.ch/docs/CH_BGer/CH_BGer_004_4C-204-2003_2004-03-05.html) E. 2.2.1

### Die Freizeichnungsklausel und die Abtretungskonstruktion {#freizeichnung}

Die Verlagerung der Risiken führt zu einer spezifischen vertraglichen Regelung der Sachgewährleistung:
1. **Ausschluss der Haftung des Leasinggebers (Freizeichnung)**: Der Leasinggeber schliesst in den allgemeinen Geschäftsbedingungen (AGB/AVB) jede mietrechtliche Mängelhaftung (Art. 258 ff. OR) oder kaufrechtliche Gewährleistung (Art. 197 ff. OR) vollständig aus. Da der Leasinggeber die Sache selbst nie physisch prüft oder nutzt, ist dieser Ausschluss im Rahmen von Art. 199 und Art. 100 Abs. 1 OR zulässig, soweit keine absichtliche Täuschung vorliegt.
2. **Abtretung der Gewährleistungsansprüche (Art. 164 OR)**: Zum Ausgleich tritt der Leasinggeber seine kaufrechtlichen Gewährleistungsansprüche gegen den Lieferanten (Nachbesserung, Minderung, Ersatzlieferung) an den Leasingnehmer ab. Der Leasingnehmer rügt Mängel direkt beim Lieferanten und setzt die Ansprüche im eigenen Namen durch.
3. **Schicksal der Wandelung (Vertragsrücktritt)**: Heikler ist die Wandelung (Rückabwicklung des Kaufs). Das Wandelungsrecht greift unmittelbar in das Eigentum des Leasinggebers ein. In der Regel bedarf die Wandelung der Zustimmung des Leasinggebers; wird der Kaufvertrag rückabgewickelt, entfällt die Geschäftsgrundlage des Leasingvertrags, was zur Abrechnung und Rückerstattung der Amortisationsleistungen führt.

## Zwingendes Konsumentenschutzrecht: Das Konsumkreditgesetz (KKG) {#konsumkreditgesetz}

Wird ein Leasingvertrag von einer Privatperson zu Zwecken abgeschlossen, die nicht ihrer beruflichen oder gewerblichen Tätigkeit zugerechnet werden können, greift das Konsumkreditgesetz (KKG; SR 221.214.1).

### Geltungsbereich nach Art. 1 Abs. 2 lit. a KKG {#kkg-geltungsbereich}

Das KKG unterstellt Verträge über das Leasing beweglicher Sachen, die dem privaten Gebrauch dienen, zwingend dem Konsumkreditrecht, wenn vereinbart ist, dass:
- die vereinbarten Leasingraten bei vorzeitiger Auflösung des Vertrags nachträglich erhöht werden (Art. 8 Abs. 1 KKG); oder
- die Sache am Ende ohne zusätzliche Zahlung oder gegen Zahlung eines vorausbestimmten Betrags in das Eigentum des Konsumenten übergeht.

Praktisch alle im Schweizer Privatkundengeschäft verwendeten Autoleasingverträge fallen unter diesen Tatbestand.

### Zwingende Schutzvorschriften des KKG {#kkg-vorschriften}

Das KKG schützt Konsumenten durch strenge Form- und Verhaltenspflichten:

1. **Qualifizierte Schriftform (Art. 9 und Art. 11 KKG)**: Der Vertrag bedarf zu seiner Gültigkeit der Schriftform (oder qualifizierten elektronischen Signatur) und muss zwingend enthalten: Beschreibung des Objekts, Barkaufpreis, Anzahlung, Anzahl, Höhe und Fälligkeit der Raten, den effektiven Jahreszins, Verpflichtung zum Abschluss einer Kaskoversicherung sowie eine **Amortisationstabelle**.
2. **Kreditfähigkeitsprüfung und IKO-Meldepflicht (Art. 28 ff. KKG)**: Der Leasinggeber ist gesetzlich verpflichtet, vor Vertragsschluss die Kreditfähigkeit des Konsumenten zu prüfen. Ein Konsument gilt als kreditfähig, wenn er die Leasingraten bezahlen kann, ohne den betreibungsrechtlichen Notbedarf anzugreifen (Art. 28 Abs. 2 KKG). Der Vertrag muss der Informationsstelle für Konsumkredit (IKO) gemeldet werden. Bei schwerwiegender Verletzung dieser Prüfpflicht verliert die Leasinggesellschaft die Kreditsumme samt Zinsen und Kosten (Art. 32 KKG).
3. **14-tägiges Widerrufsrecht (Art. 16 KKG)**: Der Leasingnehmer kann den Vertrag innert 14 Tagen seit Erhalt der Vertragskopie schriftlich widerrufen.
4. **Zwingendes Kündigungsrecht (Art. 17 KKG)**: Der Leasingnehmer hat das unabdingbare Recht, den Leasingvertrag mit einer Frist von mindestens 30 Tagen auf das Ende einer dreimonatigen Leasingdauer vorzeitig zu kündigen.
5. **Amortisationstabelle und Kündigungsnachforderung**: Bei vorzeitiger Kündigung darf der Leasinggeber eine Nachzahlung nur verlangen, wenn diese auf einer im Vertrag enthaltenen und nach anerkannten Grundsätzen erstellten Tabelle beruht (Art. 11 Abs. 2 lit. g, Art. 17 Abs. 2 KKG). Die Nachforderung stellt den Ausgleich für die stärkere Entwertung des Objekts in der Anfangsphase dar und verstösst nicht gegen das Entschädigungsverbot von Art. 266k OR ([Urteil 4A_404/2008](https://entscheidsuche.ch/docs/CH_BGer/CH_BGer_004_4A-404-2008_2008-12-18.html) E. 3).
6. **Lauterkeitsrechtliche Preisbekanntgabe**: Bei der Werbung für Konsumleasingverträge gelten die Vorschriften des Lauterkeitsrechts (Art. 17 UWG) und der Preisbekanntgabeverordnung (PBV). Das Bundesgericht hielt in [BGE 145 IV 233](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-145-IV-233_2019.html#consideration_2.) E. 2 fest:
   > «Die Bekanntgabepflicht gilt nicht nur für das Angebot von Waren zum Kauf an Konsumenten, sondern auch für kaufähnliche Rechtsgeschäfte wie Leasingverträge»

## Beendigung und Leistungsstörungen {#beendigung-und-leistungsstoerungen}

### Ordentliche Beendigung {#ordentliche-beendigung}

Mit Ablauf der vereinbarten Dauer endet das Vertragsverhältnis. Dem Leasingnehmer stehen die vertraglich vereinbarten Optionen zur Verfügung:
- **Rückgabe**: Rückgabe des Leasingobjekts in vertragsgemässem Zustand. Entsteht eine Differenz zwischen dem vertraglich vereinbarten kalkulierten Restwert und dem tatsächlichen Marktwert (z. B. wegen übermässiger Abnützung oder Mehrkilometern), hat der Leasingnehmer diesen Minderwert auszugleichen.
- **Kauf / Eigentumserwerb**: Sofern vereinbart, kann der Leasingnehmer das Objekt zum Restwert erwerben.
- **Verlängerung**: Fortführung des Vertrags zu neu berechneten Leasingraten.

### Zahlungsverzug und vorzeitige Auflösung aus wichtigem Grund {#zahlungsverzug}

Gerät der Leasingnehmer mit den Leasingraten in Verzug, richtet sich das Vorgehen nach allgemeinem Schuldrecht:
- **Verzug nach Art. 107 ff. OR**: Der Leasinggeber kann nach Mahnung und Ansetzung einer angemessenen Nachfrist gemäss [Art. 107 OR](/kommentar/or/art-107/) vom Vertrag zurücktreten oder Schadenersatz wegen Nichterfüllung verlangen.
- **Schadensabrechnung (positives Erfüllungsinteresse)**: Bei vorzeitiger Kündigung wegen Verschuldens des Leasingnehmers kann der Leasinggeber verlangen, so gestellt zu werden, wie wenn der Vertrag bis zum ordentlichen Ende erfüllt worden wäre. Die Abrechnung setzt sich zusammen aus:
  - den bis zur Vertragsauflösung fälligen Leasingraten;
  - den künftigen, noch nicht fälligen Leasingraten (abgezinst auf den Barwert);
  - dem kalkulierten Restwert am Vertragsende;
  - abzüglich des Erlöses aus der Verwertung bzw. des aktuellen Marktwerts des zurückgenommenen Leasingobjekts.
- **Konventionalstrafen und richterliche Herabsetzung**: Vertragsklauseln, die bei Verzug pauschalierte Entschädigungen oder Strafzahlungen vorsehen, unterliegen als Konventionalstrafen der zwingenden richterlichen Herabsetzung nach Art. 163 Abs. 3 OR, wenn sie übermässig hoch sind und zu einer ungerechtfertigten Überentschädigung des Leasinggebers führen.
- **Rückabwicklung bei Nichtigkeit**: Erweist sich ein Konsumgüter-Leasingvertrag als nichtig (etwa wegen Verletzung zwingender Konsumkreditvorschriften), erfolgt die Abwicklung nach den Grundsätzen des faktischen Vertragsverhältnisses ([BGE 110 II 244](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_004_BGE-110-II-244_1984-09-05.html#consideration_2.) E. 2a):
  > «Erweist sich ein Auto-Leasing-Vertrag nach seiner Erfüllung im Hinblick auf Art. 226a ff. OR als nichtig, so schuldet der Benutzer des Autos dem Vermieter oder Verkäufer nebst der Rückgabe des Fahrzeugs eine angemessene Entschädigung für die Benutzung oder Vermietung.»

## Sachen-, betreibungs- und strafrechtliche Dimensionen {#weitere-rechtsgebiete}

Die Trennung von rechtlichem Eigentum und tatsächlichem Besitz erzeugt wesentliche Schnittstellen zu anderen Rechtsgebieten:

### Konkurs des Leasingnehmers und Aussonderung (Art. 242 SchKG) {#konkurs-aussonderung}

Fällt der Leasingnehmer in Konkurs, stellt sich die Frage, wem das Leasinggut zusteht:
- Da die Leasinggesellschaft Eigentümerin der Sache geblieben ist (Art. 641 ZGB), fällt das Leasingobjekt nicht in die Konkursmasse des Leasingnehmers.
- Der Leasinggeber kann das Objekt gestützt auf Art. 242 SchKG aus der Masse aussondern lassen ([BGE 110 III 87](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_005_BGE-110-III-87_1984-06-01.html#consideration_1.) E. 1; BGE 118 II 150 E. 5).
- Voraussetzung ist der strikte Nachweis des Eigentumserwerbs vom Lieferanten. War der Leasingnehmer vor Abschluss des Leasingvertrags bereits selbst Eigentümer geworden (z. B. bei mangelhaft konstruierten *Sale-and-lease-back*-Transaktionen), scheitert die Aussonderung am Verbot der besitzlosen Mobiliarhypothek gemäss Art. 717 ZGB ([BGE 119 II 236](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_004_BGE-119-II-236_1993-05-25.html#consideration_5.) E. 5).

### Betreibungsrechtliches Existenzminimum (Art. 93 SchKG) {#existenzminimum}

Bei einer Lohnpfändung des Leasingnehmers nach Art. 93 SchKG stellt sich die Frage, ob die monatlichen Leasingraten im Notbedarf anzurechnen sind:
- Das Bundesgericht stellte in [BGE 140 III 337](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_005_BGE-140-III-337_2014.html#consideration_5.) E. 5.2 klar:
  > «Nach der Rechtsprechung des Bundesgerichts, die sich auf die Richtlinien der Konferenz stützt, sind Leasingraten für ein Auto mit Kompetenzcharakter sowohl beim betreibungsrechtlichen Existenzminimum als auch in der prozessualen Bedarfsberechnung zu berücksichtigen»
- Begründung des Bundesgerichts:
  > «Vielmehr handelt es sich bei den Leasingraten für ein Kompetenzgut wirtschaftlich gesehen um zeitlich gestaffelte Anschaffungskosten von nicht pfändbarem Vermögen im Sinne von Art. 92 Abs. 1 oder Art. 93 Abs. 1 SchKG»
- Dient das Fahrzeug hingegen reinen Freizeit- oder Bequemlichkeitszwecken, werden die Leasingraten bei der Notbedarfsberechnung nicht berücksichtigt.

### Strafrechtliche Veruntreuung (Art. 138 Ziff. 1 StGB) {#veruntreuung}

Unterschlägt, veräussert oder verpfändet der Leasingnehmer das geleaste Gut eigenmächtig, macht er sich der Veruntreuung nach Art. 138 Ziff. 1 Abs. 1 StGB schuldig:
- Nach [BGE 143 IV 297](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-143-IV-297_2017.html#consideration_1.4) E. 1.3 gilt als anvertraut:
  > «Als anvertraut gilt, was jemand mit der Verpflichtung empfängt, es in bestimmter Weise im Interesse des Treugebers zu verwenden, insbesondere es zu verwahren, zu verwalten oder einem anderen abzuliefern»
- In E. 1.4 präzisierte das Gericht:
  > «Bei der Verfügungsmacht handelt es sich um ein faktisches (nicht rechtliches) Verhältnis»
- Der Leasingnehmer hat das Fahrzeug mit der klaren Werterhaltungspflicht empfangen; ein Weiterverkauf an gutgläubige Dritte erfüllt den Tatbestand der Veruntreuung.

### Beschlagnahme und Einziehung («Via sicura») {#beschlagnahme}

Wird ein geleastes Motorfahrzeug für ein qualifiziert grobes Verkehrsdelikt (Raserdelikt im Sinne von Art. 90 Abs. 3 und 4 SVG) verwendet, kann das Fahrzeug gemäss Art. 90a SVG und Art. 263 StPO beschlagnahmt und eingezogen werden. Das Bundesgericht entschied in [BGE 140 IV 133](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-140-IV-133_2014.html#consideration_4.) E. 4, dass eine Einziehungsbeschlagnahme auch bei Fahrzeugen im Dritteigentum der Leasinggesellschaft zulässig ist, wenn die Massnahme erforderlich ist, um den Lenker von weiteren schweren Delikten abzuhalten.

## Abgrenzungen zu verwandten Vertragstypen {#abgrenzungen}

Zur Verdeutlichung der rechtlichen Natur des Leasings dient die Abgrenzung zu gesetzlichen Nominatkontrakten:

| Abgrenzungskriterium | Finanzierungsleasing | Miete (Art. 253 OR) | Kauf auf Abzahlung (Art. 214 OR) | Darlehen (Art. 312 OR) |
|---|---|---|---|---|
| **Eigentumsstellung** | Zivilrechtlich beim Leasinggeber, wirtschaftlich beim Nutzer | Beim Vermieter | Geht auf den Käufer über | Geld/Sache geht zu Eigentum an Borgenden |
| **Sach- und Erhaltungsrisiko** | Vollständig auf Leasingnehmer überwälzt | Bleibt beim Vermieter (Art. 256 Abs. 1 OR) | Beim Käufer (Gefahrübergang Art. 185 OR) | Beim Borgenden |
| **Entgeltstruktur** | Amortisation des Anschaffungspreises + Zins | Nutzungsentschädigung (Mietzins) | Tilgung des Kaufpreises | Zins (Rückerstattung des Kapitals) |
| **Kündbarkeit während Grunddauer** | Ordentlich ausgeschlossen (ausser KKG Art. 17) | Je nach Vereinbarung ordentlich kündbar | Keine Kündigung (Vertrag auf Eigentumsübergang) | Rückzahlung nach Kündigungsfrist |
| **Gewährleistung** | Freizeichnung gegen Abtretung der Händlerrechte | Vermieter haftet direkt für Mängel | Verkäufer haftet für Mängel | Keine Sachgewährleistung |

## Würdigung {#wuerdigung}

Das Institut des Leasings verdankt seine weltweite und schweizerische Verbreitung seiner hohen ökonomischen Zweckmässigkeit:

1. **Wirtschaftliche Vorzüge**:
   - *Liquiditätsschonung*: Investitionen können getätigt werden, ohne Eigenkapital zu binden oder klassische Bankkredite zu beanspruchen (*Pay-as-you-earn*-Effekt: Die Raten werden aus den laufenden Erträgen der genutzten Maschine erwirtschaftet).
   - *Steuerliche Behandlung*: Im geschäftlichen Verkehr stellen die Leasingraten für Investitionsgüter regelmässig voll abzugsfähigen Betriebsaufwand dar.
   - *Flexibilität*: Leasingnehmer können ihren Maschinen- oder Fahrzeugpark laufend auf dem neuesten technischen Stand halten.

2. **Rechtliche und praktische Risiken**:
   - *Gesamtkostenbelastung*: Über die Gesamtdauer gerechnet ist das Leasing in der Regel teurer als ein Barkauf oder ein günstiger Bankkredit, da die Leasinggesellschaft Risikoprämien, Refinanzierungszinsen und Verwaltungskosten einkalkuliert.
   - *Gefahrtragung ohne Eigentum*: Der Leasingnehmer trägt alle Risiken eines Eigentümers (Vollkaskopflicht, Unterhaltspflicht, Wertverlustrisiko), ist aber sachenrechtlich blosser Besitzer. Bei Beschädigung oder Totalschaden droht eine Finanzierungslücke (*GAP*), wenn die Versicherungsleistung unter dem Buchrestwert liegt.
   - *Überschuldungsgefahr*: Bei Privatpersonen besteht das Risiko, durch scheinbar tragbare monatliche Raten finanzielle Verpflichtungen einzugehen, die bei unvorhergesehenen Lebensereignissen (Jobverlust, Scheidung) nicht mehr bedient werden können. Hier erfüllt das KKG eine unverzichtbare Schutzfunktion.

## Praxishinweise {#praxishinweise}

- **Geltungsbereich des KKG sorgfältig prüfen**: Dient das Leasingobjekt auch nur teilweise gewerblichen Zwecken, ist im Vertrag genau zu dokumentieren, ob ein Konsum- oder ein Investitionsgüterleasing vorliegt. Fehlt die Konsumenteneigenschaft, greifen die Schutzvorschriften des KKG (insbesondere das Widerrufsrecht und das zwingende Kündigungsrecht nach Art. 17 KKG) nicht.
- **Amortisationstabelle vor Unterzeichnung analysieren**: Die im Leasingvertrag enthaltene Tabelle (Art. 11 Abs. 2 lit. g KKG) legt fest, welche Nachzahlung bei vorzeitiger Kündigung fällig wird. Konsumenten sollten vorab prüfen, ob sie bei einer Kündigung nach einem oder zwei Jahren die degressive Nachforderung finanziell tragen können.
- **Restwertrisiko vertraglich klären (offenes vs. geschlossenes Leasing)**: Beim *geschlossenen Leasingvertrag* trägt die Leasinggesellschaft das Verwertungsrisiko bei vertragsgemässer Rückgabe. Beim *offenen Vertrag* hat der Leasingnehmer für die Differenz aufzukommen, wenn das Fahrzeug bei Vertragsende auf dem Occasionsmarkt weniger erlöst als der kalkulierte Restwert.
- **Mängel unverzüglich direkt beim Lieferanten rügen**: Da die Leasinggesellschaft ihre Gewährleistung wirksam ausschliesst und die Ansprüche an den Kunden abtritt, muss der Leasingnehmer Mängel sofort nach Entdeckung gemäss den kaufrechtlichen Prüf- und Rügeobliegenheiten (Art. 201 OR) gegenüber dem Lieferanten rügen. Versäumt er die Rüge, verliert er die Gewährleistungsansprüche, bleibt aber zur Zahlung der vollen Leasingraten verpflichtet.
- **GAP-Versicherung abschliessen**: Bei Fahrzeugen empfiehlt sich der Einschluss einer Differenzkaskoversicherung (GAP-Deckung). Bei Diebstahl oder Totalschaden zahlt die herkömmliche Vollkaskoversicherung nur den aktuellen Zeitwert; die GAP-Deckung schliesst die Lücke zum vertraglich geschuldeten Restwert der Leasinggesellschaft.
- **Aussonderung im Konkursfall unverzüglich anmelden**: Im Falle des Konkurses des Leasingnehmers hat die Leasinggesellschaft ihren Aussonderungsanspruch nach Art. 242 SchKG unter Vorlage des Leasingvertrags und des Kaufbelegs beim Konkursamt unverzüglich anzumelden, um zu verhindern, dass das Gut als Bestandteil der Konkursmasse versteigert wird.

## Leitentscheide {#leitentscheide}

| Entscheid | Gegenstand | Bedeutung für das Leasingrecht |
|---|---|---|
| [BGE 118 II 150](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_004_BGE-118-II-150_1992-04-30.html#consideration_4.) E. 4b, 6c | Nutzfahrzeugleasing / Konkurs | Grundlegende Qualifikation als Innominatvertrag sui generis; Begründung des Sicherungseigentums; Dreiparteienverhältnis |
| [Urteil 4A_404/2008](https://entscheidsuche.ch/docs/CH_BGer/CH_BGer_004_4A-404-2008_2008-12-18.html) E. 4.1 | Konsumgüterleasing / Kündigung | Typische Grundstruktur des Leasings; Verhältnis von Art. 266k OR zu Art. 17 KKG; Zulässigkeit von Amortisationstabellen |
| [BGE 132 III 549](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_005_BGE-132-III-549_2006.html#consideration_2.1) E. 2.1 | Immobilienleasing / Formvorschrift | Keine öffentliche Beurkundung für den Gesamtvertrag nach Art. 216 Abs. 1 OR erforderlich; Formzwang nur für ein separates Kaufsrecht |
| [BGE 119 II 236](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_004_BGE-119-II-236_1993-05-25.html#consideration_4.) E. 4, 5 | Finanzierungsleasing / Vindikation | Phasenmodell des Finanzierungsleasings; Eigentumserwerb und Grenzen der Aussonderung bei fehlerhaftem Besitzübergang |
| [BGE 110 II 244](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_004_BGE-110-II-244_1984-09-05.html#consideration_2.) E. 2a | Auto-Leasing / Nichtigkeit | Rückabwicklung nichtiger Verträge; Nutzungsentschädigung nach den Grundsätzen des faktischen Vertragsverhältnisses |
| [BGE 113 II 168](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_004_BGE-113-II-168_1987-05-20.html#consideration_2.) E. 2 | Abgrenzung Miete / Leasing | Wirtschaftliche Betrachtungsweise; Werbebezeichnung «Leasing» bei blossem Mietvertrag |
| [BGE 140 III 337](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_005_BGE-140-III-337_2014.html#consideration_5.) E. 5.2 | Lohnpfändung / Notbedarf | Leasingraten für ein Fahrzeug mit Kompetenzcharakter (Art. 92/93 SchKG) sind im betreibungsrechtlichen Existenzminimum anzurechnen |
| [BGE 143 IV 297](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-143-IV-297_2017.html#consideration_1.4) E. 1.4 | Veruntreuung / Art. 138 StGB | Veruntreuung bei Weiterverkauf eines Leasingfahrzeugs; Anvertrautsein und faktische Verfügungsmacht |
| [BGE 145 IV 233](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-145-IV-233_2019.html#consideration_2.) E. 2 | Lauterkeitsrecht / Werbung | Preisbekanntgabepflicht (Art. 17 UWG / PBV) gilt auch für kaufähnliche Rechtsgeschäfte wie Leasingverträge |
| [BGE 140 IV 133](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_006_BGE-140-IV-133_2014.html#consideration_4.) E. 4 | Beschlagnahme «Via sicura» | Zulässigkeit der Einziehungsbeschlagnahme eines Leasingfahrzeugs trotz Dritteigentums der Leasinggesellschaft |
| [BGE 110 III 87](https://entscheidsuche.ch/docs/CH_BGE/CH_BGE_005_BGE-110-III-87_1984-06-01.html#consideration_1.) E. 1 | Konkurs / Massevermögen | Gewahrsamsverhältnisse und Sicherung von Leasingobjekten bei Konkurseröffnung über den Leasingnehmer |
| [Urteil 4C.204/2003](https://entscheidsuche.ch/docs/CH_BGer/CH_BGer_004_4C-204-2003_2004-03-05.html) E. 2.2.1 | Finanzierungsleasing / Garantie | Dreiparteienverhältnis; Qualifikation und Durchsetzbarkeit von Erfüllungsgarantien Dritter für Leasingverbindlichkeiten |

## Literatur {#literatur}

In der Rechtsprechung zum Leasingrecht ausdrücklich herangezogen (u.a. BGE 118 II 150 E. 4, BGE 119 II 236 E. 4, BGE 132 III 549 E. 1, Urteil 4A_404/2008 E. 4.1):

- Amstutz/Schluep, Basler Kommentar, Einleitung vor Art. 184 ff. OR, N. 81 ff.
- Giger Hans, Der Leasingvertrag. Systematische Darstellung unter besonderer Berücksichtigung des Finanzierungsleasing, Bern 1977.
- Giger Hans, Berner Kommentar, Der Konsumkredit, N. 185 und N. 322.
- Giovanoli Mario, Le contrat de leasing et le droit suisse, in: Journal des Tribunaux (JdT) 1981 I, S. 39 ff.
- Giovanoli Mario, Leasing (crédit-bail), Schweizerische Juristische Kartothek (SJK), Karte Nr. 363.
- Hausheer Heinz, Finanzierungs-Leasing beweglicher Investitionsgüter, in: Zeitschrift des Bernischen Juristenvereins (ZbJV) 106 (1970), S. 217 ff.
- Hess Markus, Immobilien-Leasing in der Schweiz, Diss. Zürich 1989.
- Krummenacher Peter, Konsumentenleasing, 2007.
- Lüssi Paul, Das Leasing-Geschäft, Diss. Zürich 1966.
- Rinderknecht Thomas, Leasing von Mobilien, Diss. Zürich 1984.
- Schubiger August, Der Leasing-Vertrag nach Schweizerischem Privatrecht, Diss. Freiburg 1970.
- Stauder Bernd, Le contrat de «finance-équipement-leasing», Dixième journée juridique, MPFDG Nr. 10, Genf 1970, S. 30 ff.
- Stöcklin Marcus, Der Leasingvertrag als Mittel der Umgehung zwingenden Rechts, Diss. Basel 1985.

Die Literaturangaben folgen den Nachweisen in den Leitentscheiden des Bundesgerichts.
