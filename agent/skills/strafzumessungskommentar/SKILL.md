---
name: strafzumessungskommentar
description: >
  Ergänzt einen Glossagens-Kommentar zu einem Straftatbestand um einen empirischen
  Strafzumessungs-Praxiskommentar (`strafzumessung.md` im Page Bundle) nach dem Muster der
  Prototypen zu Art. 163–167 StGB auf strafzumessung.ch: Die strafzumessungsrelevanten Kriterien
  werden induktiv aus der publizierten Rechtsprechung entwickelt und mit belegten, am Dispositiv
  gespiegelten Strafwerten unterlegt. Workflows: /strafzumessung (Vollworkflow),
  /sz-recherche (nur Ledger), /sz-update (Nachführung), /sz-pruefen (Verifikation).
version: 1.0.0
author: Claude Code
license: MIT
tools:
  - mcp__fedlex-connector__get_article
  - mcp__fedlex-connector__list_amendments
  - mcp__fedlex-connector__search_by_title
  - mcp__entscheidsuche__search
  - mcp__entscheidsuche__search_by_case_number
  - mcp__entscheidsuche__fetch_document
metadata:
  hermes:
    tags: [Glossagens, Legal, Strafzumessung, Praxisauswertung, StGB]
---

# Strafzumessungs-Praxiskommentar

## Zweck

Für einen Straftatbestand wird eine eigene Seite im bestehenden Page Bundle angelegt:

```
content/kommentar/{gesetz}/art-{nr}/
├── _index.md            ← dogmatischer Kommentar (unverändert)
├── rechtsprechung.md    ← Entscheidsammlung (unverändert)
├── strafzumessung.md    ← DIESER Skill
└── strafzumessung-daten.json  ← Ledger, maschinenlesbar (nicht gerendert)
```

## Abgrenzung

| Skill | Frage |
|---|---|
| `gesetzeskommentar-workflows` | Was ist der Tatbestand? (dogmatisch, deduktiv, Lehre + Leitentscheide) |
| **dieser Skill** | Was kostet die Tat? (empirisch, induktiv, ausschliesslich aus belegten Strafwerten) |

Der Strafzumessungskommentar wiederholt die Dogmatik **nicht**. Er nimmt sie nur dort auf, wo sie
strafzumessungsrelevant ist — namentlich bei Einwänden, die den Schuldspruch insgesamt zu Fall
bringen (objektive Strafbarkeitsbedingungen, Abgrenzung zur Übertretung, Verjährung).

## Rollendefinition

Du wertest publizierte Entscheide aus und schreibst auf, **was die Gerichte tatsächlich tun** —
nicht, was sie tun sollten. Jede Aussage über ein Strafzumessungskriterium ist an einen
konkreten, verlinkten Entscheid gebunden. Wo die Praxis schweigt, schweigt der Kommentar.

Schweizerische Rechtschreibung, kein Eszett («Höchstmass», «Massstab»).

---

# Die zehn Grundregeln

Sie sind der eigentliche Inhalt dieses Skills; die Gliederung ist nur ihr Gefäss.

**R1 — Nur belegte Werte.** Jede Zahl im Kommentar stammt aus einem Urteilstext, den du im
Volltext gelesen hast. Keine Schätzung, keine Interpolation, keine Erfahrungswerte. Was nicht
beziffert ist, wird als «nicht beziffert» ausgewiesen.

**R2 — Gegenprobe am Dispositiv.** Jeder Strafwert wird gegen das Dispositiv desselben Urteils
gespiegelt: die Sanktion, die dort gegen dieselbe Person tatsächlich ausgesprochen wurde. Beide
Werte stehen nebeneinander in der Tabelle. Sie fallen systematisch auseinander — durch Asperation,
Zusatzstrafenbildung (Art. 49 Abs. 2 StGB) und vor allem durch das Verschlechterungsverbot
(Art. 391 Abs. 2 StPO). Ein Kommentar, der nur die Einzelstrafe nennt, täuscht.

**R3 — Einsatzstrafe ≠ Asperationszuschlag.** Zwei getrennte Tabellen, nie eine gemeinsame Spanne.
Der Zuschlag ist bereits um die Deckungsgleichheit mit dem Hauptdelikt gekürzt; er ist mit einer
isoliert bemessenen Einzelstrafe nicht vergleichbar. Diesen Satz im Kommentar ausdrücklich hinschreiben.

**R4 — Deliktsimmanenz prüfen.** Für jedes Merkmal fragen: Ist es bereits Tatbestandsmerkmal? Dann
darf es nach dem Doppelverwertungsverbot nicht straferhöhend wirken, und die Gerichte sagen das
regelmässig. Solche Merkmale gehören mit Richtung «—» ins Prüfraster, nicht unter «erhöhend».
Beispiel: der direkte Vorsatz bei Art. 164 StGB.

**R5 — Den Trichter offenlegen.** Der Abschnitt «Grundlage und Grenzen» nennt jede Stufe mit Zahl:
wie viele Entscheide die Norm zitieren, wie viele im Volltext ausgewertet wurden, wie viele einen
Schuldspruch enthalten, wie viele eine bezifferte Strafe, wie viele Werte nach Bereinigung
verbleiben. Ohne diese Zahlen ist die Auswertung nicht nachprüfbar und der Kommentar wertlos.

**R6 — Grenzen offenlegen.** Sprachraum (fast immer nur deutschsprachig), kantonale Schlagseite,
Publikationsbias (publiziert werden fast nur Berufungsurteile, häufig unter dem
Verschlechterungsverbot), Grösse der Basis. Der Satz «Die Befunde beschreiben eine Tendenz in den
ausgewerteten Entscheiden, nicht eine repräsentative Gesamtstatistik» steht in jedem Kommentar.

**R7 — Kein Tarif.** Die Tabellen sind ein **Plausibilitätstest**, kein Bemessungsraster: Wer eine
Strafe ausserhalb der für den benannten Verschuldensgrad belegten Spanne beantragt oder ausfällt,
trägt eine erhöhte Begründungslast (Kontrolle im Sinne von BGE 136 IV 55 E. 5.7). So formulieren —
nie als Empfehlung.

**R8 — Altrecht kennzeichnen.** Werte, die unter aufgehobenem Sanktionenrecht ergangen sind, werden
als solche markiert. Wichtigster Fall: Das Höchstmass der Geldstrafe betrug nach aArt. 34 Abs. 1
StGB 360 Tagessätze, seit dem 1. Januar 2018 beträgt es 180. Ältere Werte über 180 TS sind heute
nicht mehr aussprechbar — als Callout ausweisen, nicht kommentarlos in die Tabelle stellen.
Ebenso: Revisionen des Tatbestands selbst (Fedlex `list_amendments`).

**R9 — Links verbatim.** Jeder Entscheid wird auf entscheidsuche.ch verlinkt; die URL wird **nie**
konstruiert, sondern aus dem Feld `document_url` der MCP-Antwort übernommen. Pinpoint-Anker
`#consideration_{E-Nr}` nur bei HTML-Dokumenten (`is_pdf: false`) und nur, wenn die Erwägung dort
tatsächlich vorkommt. PDF-Entscheide ohne Anker. Rückfall: `https://mcp.opencaselaw.ch/entscheid/{id}`.

**R10 — Normtext aus Fedlex.** Deliktsbezeichnung, Wortlaut und Strafrahmen im Kopf des Kommentars
kommen aus `mcp__fedlex-connector__get_article`, nie aus dem Gedächtnis.

---

# TEIL A — WORKFLOWS

## Workflow 1: `/strafzumessung Art. {NR} {Gesetz}` — Vollworkflow

1. INIT (→ B.1)
2. RECHERCHETRICHTER (→ B.2)
3. VOLLTEXTAUSWERTUNG in den Ledger (→ B.3)
4. INDUKTION der Merkmale (→ B.4)
5. SCHREIBEN (→ Teil C, Vorlage in `references/vorlage.md`)
6. QUALITÄTSKONTROLLE (→ Teil D)
7. ABSCHLUSS — Frontmatter, Revisionseintrag, `make build-check`, Bericht

## Workflow 2: `/sz-recherche Art. {NR} {Gesetz}` — nur Ledger

Schritte 1–3. Ergebnis: `strafzumessung-daten.json` und eine Kurzauswertung im Chat
(Trichterzahlen, Zahl der Strafwerte, Einschätzung, ob die Basis für einen Kommentar trägt).
Der Kommentar wird nicht geschrieben.

## Workflow 3: `/sz-update Art. {NR} {Gesetz}` — Nachführung

Für eine bestehende Seite. Recherchetrichter nur ab dem bisherigen `Auswertungsstand`
(`decision_date_from`). Neue Werte in den Ledger, Tabellen ergänzen, Trichterzahlen und
Auswertungsstand hochzählen, betroffene Randnoten anpassen, neuer Revisionseintrag.
**Bestehende Werte nicht stillschweigend ändern** — wird ein früherer Wert korrigiert, gehört das
in die `note` des Revisionseintrags.

## Workflow 4: `/sz-pruefen Art. {NR} {Gesetz}` — Verifikation

Jeden Wert der Tabellen gegen den Urteilstext zurückprüfen (`fetch_document`, wörtliche Stelle
suchen). Ergebnisliste: bestätigt / abweichend / im Urteil nicht auffindbar. Befunde korrigieren.
Erst danach darf `mcp_verified: true` gesetzt werden.

---

# TEIL B — BASISOPERATIONEN

## B.1 INIT

1. Bundle prüfen: existiert `content/kommentar/{gesetz}/art-{nr}/_index.md`? Wenn nein — zuerst
   `gesetzeskommentar-workflows` (`/kommentar`); dieser Skill ergänzt nur.
2. Normtext und **Strafrahmen** via `mcp__fedlex-connector__get_article` holen; bei mehreren
   Ziffern/Absätzen mit je eigenem Rahmen alle notieren (Beispiel Art. 163 StGB: Ziff. 1 fünf
   Jahre, Ziff. 2 drei Jahre — sie werden im Kommentar getrennt geführt).
3. `mcp__fedlex-connector__list_amendments`: Wurde der Tatbestand im Auswertungszeitraum geändert?
   Falls ja, Stichdatum notieren (R8).
4. **Deliktsbezeichnung und ihre Varianten** sammeln — der Randtitel plus alle Schreibweisen, die
   in Urteilen vorkommen. Sie sind der Schlüssel des Trichters (Beispiel Art. 164 StGB:
   «Vermögensminderung» und «Vermögensverminderung»; Art. 167 StGB: «Bevorzugung eines
   Gläubigers» und «Gläubigerbevorzugung» — Letzteres liefert überwiegend Fehltreffer aus dem
   Steuererlass- und Betreibungsrecht).
5. Den bestehenden `_index.md` und `rechtsprechung.md` lesen — Doppelungen vermeiden, vorhandene
   Entscheide als Ausgangspunkt nehmen.

## B.2 RECHERCHETRICHTER

Ausschliesslich `mcp__entscheidsuche__*`, **direkt in der Hauptkonversation, keine parallelen
Subagenten**. Jede Stufe wird gezählt; die Zahlen wandern wörtlich in den Abschnitt «Grundlage und
Grenzen».

| Stufe | Query | Zweck |
|---|---|---|
| 1 Bestand | `"Art. 165 StGB"` | Wie oft wird die Norm überhaupt zitiert |
| 1b Varianten | `"Misswirtschaft"`, jede Schreibweise einzeln | Keine Variante verlieren |
| 2 Schuldspruch | `"im Sinne von Art. 165"` bzw. `"Misswirtschaft im Sinne von Art. 165"` | Der ertragreichste Filter: die Schuldspruchformel |
| 3 Strafzumessung | Stufe 2 `AND ("Einsatzstrafe" OR "Einzelstrafe" OR "asperiert" OR "Tatverschulden")` | Sachurteile mit begründeter Strafzumessung |
| 4 Trefferliste | Stufe 2/3 mit `size: 100` + `search_after` | Vollständige Liste, nicht nur Seite 1 |

Regeln:
- Zählung mit `size: 1` und dem `total` der Antwort; die Trefferliste separat paginieren.
- Die Schuldspruchformel wird **kantonal unterschiedlich** formuliert. Bringt Stufe 2 auffallend
  wenige oder nur Treffer eines Kantons, ist das eine Grenze der Auswertung (R6) — im Kommentar
  benennen, nicht kaschieren.
- Fremdsprachige Praxis: entweder mit `language_filter` einbeziehen und die französische/
  italienische Deliktsbezeichnung ergänzen, oder ausdrücklich ausschliessen und das unter
  «Grenzen» sagen. Beides ist zulässig — Schweigen nicht.
- Bei `/sz-update`: `decision_date_from` = bisheriger Auswertungsstand.

## B.3 VOLLTEXTAUSWERTUNG → Ledger

Jeden Treffer der Stufe 3 mit `mcp__entscheidsuche__fetch_document` im Volltext lesen. Ist
`text_truncated: true`, das Dokument über `document_url` nachziehen.

Pro Entscheid im Urteil suchen: die Strafzumessungserwägung zum fraglichen Tatbestand, die
wörtliche Verschuldensbezeichnung, den bezifferten Wert, das **Dispositiv** — und die Merkmale,
die das Gericht ausdrücklich nennt.

Ledger `strafzumessung-daten.json` (liegt im Bundle, wird von Hugo nicht gerendert):

```json
{
  "norm": "Art. 165 StGB",
  "auswertungsstand": "2026-08-29",
  "trichter": {"normzitat": 245, "schuldspruchformel": 70, "volltext_ausgewertet": 70,
               "schuldspruch": 51, "bezifferte_strafe": 12, "strafwerte_bereinigt": 12,
               "freispruch": 6, "einstellung_verjaehrung": 3},
  "werte": [{
    "entscheid": "OG ZH SB240416", "gericht": "Obergericht Zürich", "kanton": "ZH",
    "datum": "2025-09-16", "doc_id": "…", "document_url": "https://entscheidsuche.ch/docs/…",
    "is_pdf": false, "erwaegung": "5.3",
    "rolle": "einzelstrafe",
    "benannter_grad": "nicht mehr leicht",
    "wert": "10 Monate", "asperiert": "6 Monate",
    "ausgesprochen_dispositiv": "21 Mt. FS + 90 TS",
    "bezugsgroesse": {"art": "Verschleppungsdauer", "wert": "2015–2020"},
    "verschlechterungsverbot": false, "altrecht": false,
    "merkmale": [{"merkmal": "einschlägige Vorstrafe", "richtung": "erhoehend",
                  "zitat": "…wörtlich…"}],
    "zitat_wert": "…wörtliche Stelle, aus der der Wert stammt…"
  }],
  "ausgeschieden": [{"entscheid": "OG ZH SB230033", "grund": "Rückweisungsverfahren zu SB180264 — zählt als ein Fall"}]
}
```

**Bereinigung** (Stufe 5): Rückweisungspaare (dasselbe Verfahren vor und nach BGer-Rückweisung)
zählen als **ein** Fall; Parallelurteile gegen Mitbeschuldigte werden einzeln geführt, aber als
Parallelfall gekennzeichnet. Freisprüche und Einstellungen werden **gezählt**, nicht weggelassen —
bei manchen Tatbeständen ist die Freispruchquote der wichtigste Befund (so Art. 167 StGB).

## B.4 INDUKTION der Merkmale

Aus dem Ledger die Merkmale gruppieren und **nach belegtem Gewicht ordnen** — nicht nach
Lehrbuchsystematik. Leitfragen:

- Welche Grösse beziffern die Gerichte durchgehend? Das ist das dominierende Merkmal
  (Deliktsbetrag, Verschleppungsdauer, Menge, Dauer der Unterlassung).
- Trägt der Tatbestand die Einsatzstrafe, oder erscheint er fast nur als Asperationszuschlag?
  Diese Zweiteilung bestimmt den ganzen Aufbau.
- Gibt es eine bezifferte Asperationsregel (z. B. die «Drittelsregel» bei Art. 166 StGB)? Das ist
  regelmässig der praktisch verwertbarste Befund — als eigener Abschnitt mit «Befund»-Callout.
- Welche Merkmale sind deliktsimmanent (R4)?
- Was entlastet **nicht**? Nachträgliche Schuldentilgung, öffentlich-rechtliche Gläubiger,
  nachträgliche Rekonstruierbarkeit — diese Negativbefunde sind für die Praxis so wertvoll wie die
  positiven und gehören in einen eigenen Abschnitt oder mit Richtung «—» ins Prüfraster.
- Widersprechen sich Kantone? Dann beide Linien darstellen und die Konsequenz benennen (Beispiel:
  Aargauer Asperationsabschlag vs. Zürcher Doppelverwertungsverbot — beides zusammen wäre eine
  doppelte Entlastung).

**Schwelle:** Unter 20 im Volltext ausgewerteten Entscheiden oder unter 8 belegten Strafwerten
trägt kein Kommentar. Dann `/sz-recherche` melden, den Befund berichten und mit dem Benutzer
klären, ob die Seite mit ausdrücklich ausgewiesener schmaler Basis trotzdem entstehen soll.

---

# TEIL C — AUFBAU DES KOMMENTARS

Vollständige Vorlage mit Frontmatter: `references/vorlage.md`.
Ausgearbeitetes Muster: `references/muster-art-166-stgb.md`.

Feste Reihenfolge; die mittleren Blöcke werden nach Befundlage gewählt.

| # | Abschnitt | Pflicht |
|---|---|---|
| — | Kopf: Deliktsbezeichnung, Norm + Strafrahmen, Kennzahlen-Callout | ja |
| — | **Grundlage und Grenzen dieser Auswertung** | ja |
| A | **Einordnung: {charakterisierender Zusatz}** | ja |
| B | **Die strafzumessungsrelevanten Merkmale** (I., II., III. …) | ja |
| C ff. | variable Blöcke (siehe unten) | nach Befund |
| — | **Belegte Strafmasse** (Tabellen) | ja |
| — | **Prüfraster für die Praxis** | ja |
| — | **Ausgewertete Entscheide** | ja |

Variable Blöcke, je nach Befund und in dieser Reihenfolge:

- **Asperation und Deckungsgleichheit** — wenn der Tatbestand typischerweise neben einem
  schwereren Delikt steht (fast immer bei Wirtschaftsdelikten).
- **Was die Praxis nicht entlastet** — wenn genügend Negativbefunde vorliegen.
- **Wo der Tatbestand scheitert** — wenn die Freispruch-/Einstellungsquote auffällig ist.
- **Dogmatische Grenzen** — nur Einwände, die den Schuldspruch als Ganzes betreffen (objektive
  Strafbarkeitsbedingung, Abgrenzung zur Übertretung, Verjährung, Sonderdelikt/Art. 26 StGB).
- **Strafart, Vollzug, Verbindungsbusse** — wenn sich eine Schwelle zwischen Geld- und
  Freiheitsstrafe belegen lässt; hier auch der Altrechtsvorbehalt (R8).
- **Täterkomponente** — nur wenn beziffert (Vorstrafen, Verfahrensdauer Art. 5 StPO, Geständnis).
- **{Bezugsgrösse} und Strafmass: die Streubreite** — nur bei ≥ 10 Wertepaaren; Tabelle
  Betrag/Dauer → Strafe, aufsteigend, mit dem ausdrücklichen Befund, ob eine Linie erkennbar ist.

## Kopf

```
{{< callout type="info" >}}
**Auswertungsstand** 29.08.2026 · **Ausgewertete Entscheide** 70 ·
**Belegte Strafwerte** 12
{{< /callout >}}
```

Kein Hinweis auf KI-Erstellung, fehlende Verifikation oder «Prototyp»-Status: Die Plattform
deklariert beides global unter `/ueber/`, und `revisions` samt `agent_verified` halten es pro
Seite maschinenlesbar fest. Ein solcher Hinweis im Artikel selbst ist Redundanz — anders als bei
den Prototypen auf strafzumessung.ch, wo er die Rubrik als Ganzes betrifft. Was in den Artikel
gehört, sind die **inhaltlichen** Vorbehalte: der Trichter (R5) und der Abschnitt «Grenzen» (R6).

Darüber: H1 = Deliktsbezeichnung (nicht «Art. X»), darunter eine Zeile
`Art. 166 StGB — Freiheitsstrafe bis zu drei Jahren oder Geldstrafe`.

## Randnoten

Fortlaufend `**N 1**`, `**N 2**` … über den ganzen Kommentar; Tabellen und Callouts erhalten keine
Nummer. Querverweise als «(N 11)». Eine Randnote trägt einen Gedanken und mindestens einen
verlinkten Beleg.

## Zitierweise

- Kurzzitat im Fliesstext: `[OG ZH SB240125](https://entscheidsuche.ch/docs/…#consideration_5.2)`
  — Gericht, Kanton, Geschäftsnummer. BGE/BGer wie üblich: `BGE 131 IV 49`, `BGer 6B_157/2025 vom
  15.01.2026, E. 2.2.1`.
- Wörtliche Übernahmen aus Erwägungen als Blockzitat mit Attribution:

  ```
  > Vorliegend könne einzig noch Berücksichtigung finden, dass sich das durch die Unterlassung
  > der Buchführung geschützte Rechtsgut nicht vollumfänglich mit demjenigen der Misswirtschaft
  > decke.
  >
  > — [Obergericht Zürich SB180264 vom 21.04.2021](https://entscheidsuche.ch/docs/…)
  ```
- Verschuldensbezeichnungen immer **wörtlich** und in Anführungszeichen («noch leicht», «nicht mehr
  leicht») — sie sind der Anknüpfungspunkt der Kontrolle nach BGE 136 IV 55 E. 5.7.
- Abkürzungen einmal einführen: FS = Freiheitsstrafe, TS = Tagessätze Geldstrafe;
  «Strafeinheiten» ist die bernische Bezeichnung für die vor der Wahl der Strafart bemessene Grösse.

## Befund-Callouts

Verdichtete, praktisch verwertbare Erkenntnisse als eigener Kasten:

```
{{< callout type="default" >}}
**Befund** — Die Drittelsregel erlaubt es, aus einer hypothetischen Einzelstrafe den zu
erwartenden Zuschlag abzuschätzen — und umgekehrt einen ausgewiesenen Zuschlag auf seine
Plausibilität zu prüfen. Sie gilt nur beim engen zeitlichen und sachlichen Zusammenhang.
{{< /callout >}}
```

Altrechtsvorbehalte als `type="warning"`.

## Tabelle «Belegte Strafmasse»

Einleitungssatz nach R3, dann getrennt:

*Tabelle 1: {Norm} als Einsatzstrafdelikt — gespiegelt am Dispositiv*

| Entscheid | Datum | Benannter Grad | Einzel-/Einsatzstrafe | Ausgesprochen (Dispositiv) | Bemerkung |

*Tabelle 2: {Norm} als asperiertes Nebendelikt*

| Entscheid | Datum | Benannter Grad | Isolierte Einzelstrafe | Zuschlag | Hauptdelikt | Ausgesprochen (Dispositiv) |

Sortierung aufsteigend nach Strafhöhe. Nach jeder Tabelle eine Randnote, die die Spanne benennt,
die Ausreisser erklärt und sagt, was ausserhalb des belegten Rahmens liegt. Nicht Bezifferbares:
«—», nie leer.

Optional, wenn die Verschuldensbezeichnungen es hergeben — *Kontrolltabelle*
`Benannter Grad | Strafmass | Beobachtung`, eingeleitet mit dem Hinweis auf BGE 136 IV 55 E. 5.7.
Dazu gehört die Beobachtung, welcher Teil des Strafrahmens in der Praxis **leer** bleibt.

## Prüfraster für die Praxis

Abschliessende Tabelle, Merkmale in der Reihenfolge ihres belegten Gewichts:

| Merkmal | Richtung | Belegte Wirkung |

`Richtung` ist `erhöhend`, `mindernd` oder `—` (neutral/deliktsimmanent/kein Tatbestand).
`Belegte Wirkung` nennt einen konkreten Wert oder ein wörtliches Zitat plus Randnotenverweis —
niemals eine allgemeine Beschreibung.

## Ausgewertete Entscheide

Liste aller Entscheide, absteigend nach Datum, je mit Link und einer Zeile, was er beiträgt.
Leitentscheide (BGE) am Schluss. Diese Liste ist der Nachweis für R1.

---

# TEIL D — QUALITÄTSKONTROLLE

Vor dem Abschluss durchgehen:

- [ ] Jede Zahl im Text steht so im Ledger und im Urteilstext (Workflow 4).
- [ ] Jeder Entscheid ist verlinkt; jede URL stammt verbatim aus `document_url` (R9).
- [ ] Anker nur bei `is_pdf: false` und nur bei tatsächlich vorhandener Erwägung.
- [ ] Einsatzstrafen und Zuschläge sind getrennt; keine gemeinsame Spanne (R3).
- [ ] Jeder Strafwert hat seinen Dispositivwert (R2).
- [ ] Trichterzahlen vollständig und untereinander konsistent (R5).
- [ ] Abschnitt «Grenzen» nennt Sprachraum, Kantonsverteilung, Basisgrösse, Publikationsbias (R6).
- [ ] Kein Satz empfiehlt ein Strafmass; die Tabellen sind als Plausibilitätstest eingeführt (R7).
- [ ] Altrechtliche Werte gekennzeichnet (R8).
- [ ] Deliktsimmanente Merkmale stehen nicht unter «erhöhend» (R4).
- [ ] Verschuldensbezeichnungen wörtlich zitiert.
- [ ] Keine Eszett; schweizerische Rechtschreibung.
- [ ] Frontmatter vollständig, Revisionseintrag zuoberst, `mcp_verified` korrekt gesetzt.
- [ ] `make build-check` grün.

## Abschlussbericht

Trichterzahlen, Zahl der Strafwerte, Spanne der Einsatzstrafen, Spanne der Zuschläge, die drei
gewichtigsten Merkmale, die auffälligsten Negativbefunde, benannte Grenzen — und ausdrücklich:
was nicht belegt werden konnte.

---

# TEIL E — TECHNISCHE REFERENZ

## Frontmatter

```yaml
---
title: "Strafzumessung: {Deliktsbezeichnung} (Art. X {Gesetz})"
weight: 98          # zwischen Kommentar (Artikel-Weight) und rechtsprechung.md (99)
date: YYYY-MM-DD
lastmod: YYYY-MM-DD
description: "Empirische Auswertung der publizierten Praxis zur Strafzumessung nach Art. X …"
tags: ["Strafzumessung", "{Gesetz}", "{Deliktsbezeichnung}", "Praxisauswertung"]
agent_verified: false
auswertungsstand: YYYY-MM-DD
entscheide_ausgewertet: 70
strafwerte_belegt: 12
revisions:
  - date: YYYY-MM-DD
    by: "Claude Code"
    model: "claude-opus-5"
    mcp_verified: true
    note: "Erstauswertung: 70 Entscheide im Volltext, 12 belegte Strafwerte, gespiegelt am Dispositiv."
---
```

`mcp_verified: true` nur, wenn Normtext über Fedlex **und** sämtliche Entscheide über
entscheidsuche geprüft wurden. `agent_verified` bleibt `false`, bis die Seite verifiziert ist.

## Verlinkung im Artikel

`layouts/kommentar/list.html` blendet auf der Artikelseite eine Kachel für `strafzumessung` ein,
sobald die Seite existiert — es ist nichts von Hand zu verlinken.

## entscheidsuche — Aufrufe

| Zweck | Aufruf |
|---|---|
| Zählen | `search` mit `size: 1` → `total` |
| Trefferliste | `search` mit `size: 100`, dann `search_after` = `next_cursor` |
| Nachführung | `search` mit `decision_date_from` |
| Einzelner Entscheid | `search_by_case_number` → `document_url` verbatim |
| Volltext | `fetch_document` (bei `text_truncated: true` über `document_url` nachziehen) |
| Kantons- und Sprachverteilung | `search` mit `include_aggregations: true` |

Die Aggregation liefert die Zahlen für den Abschnitt «Grenzen» fertig: der Block `hierarchy` die
Kantons- und Gerichtsverteilung (Beispiel Art. 166 StGB: ZH 51 von 70 — daraus wird «stark
zürcherisch geprägt, rund zwei Drittel»), der Block `language` den Sprachraum. Die Antwort ist
gross, weil sie zusätzlich Datums-Buckets enthält: nur einmal pro Auswertung anfordern und nur
`hierarchy` und `language` auswerten.

Keine parallelen Subagenten. Die Auswertung läuft sequenziell in der Hauptkonversation;
bei sehr grossen Beständen den Trichter enger ziehen, nicht die Recherche verteilen.

## Fedlex

`get_article` (Wortlaut, Strafrahmen), `list_amendments` (Revisionen), `search_by_title`
(SR-Nummer unbekannt).
