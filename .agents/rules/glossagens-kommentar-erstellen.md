---
trigger: always_on
---

# Agenten-Leitfaden: Erstellung von Gesetzeskommentaren

Dieser Leitfaden hält nur fest, was bei **jedem** Kommentar gilt: Qualitätsmassstab, Mindestzahlen und Zitierweise. Ablauf, Quellen und Werkzeuge, Dateistruktur, Frontmatter, Wortlaut-Shortcode, Linkziel, Belegprüfung und Revisions-Vermerk stehen **ausschliesslich** im Skill `./agent/skills/glossagens-content-creation/SKILL.md` und in `CLAUDE.md` — dort nachlesen, hier nicht wiederholen.

Immer zusätzlich: Anforderungen und Workflows von `./agent/skills/glossagens-content-creation`.
Wird verlangt, dass der Kommentar «praxisorientiert» sein soll (oder als «Praxiskommentar» verfasst werden soll), gilt zusätzlich zwingend der Stil und Aufbau gemäss `./agent/skills/praxisorientierter-kommentar` (Muster: Art. 110 StPO, Art. 336 OR mit ausführlichen Lebenssachverhalten, Gegenüberstellung von Anwendungs- und Verwerfungsfällen und taktischen Merksätzen). Das Grundgerüst bleiben auch dort die abstrakten Tatbestandsmerkmale der Norm: Gegliedert wird entlang des Prüfschemas, die Praxisschilderungen werden den einzelnen Merkmalen zugeordnet — nie nach Urteilen oder Fallgeschichten.

---

## 1. Qualitätskriterien

Jeder kommentierte Artikel erfüllt:

1. **Struktur**: Hugo Page Bundle (`art-{nr}/_index.md` + `rechtsprechung.md`), Frontmatter und `revisions` gemäss `CLAUDE.md`.
2. **Tiefe**: Wortlaut, systematische Einordnung und dogmatische Bedeutung umfassend aufbereitet; Umfang und Tiefe orientieren sich am Standard von onlinekommentar.ch.
   - **Gesetzgeberischer Zweck** (Schaffung und spätere Revisionen) ist zwingend anhand der amtlichen Materialien nachzuweisen (BBl-Fundstelle); keine Spekulation über die Teleologie (Regel R4).
   - **Lehre** ist stets zu prüfen. Insbesondere sind Lehrmeinungen aufzunehmen, die eine gerichtliche Praxis kritisieren oder abweichende Lösungen vorschlagen.
3. **Sprache**: Schweizer Rechtschreibung (zwingend **kein ß**), akademisch, präzise, nicht umgangssprachlich.
4. **Praxisfragen**: mindestens ein bis zwei kantonale Praxisfragen (typische Hürden oder Streitpunkte), je mit klärendem Entscheid verknüpft.
5. **Rechtsprechung**: mindestens **10 praxisrelevante Entscheide** auf `rechtsprechung.md`, davon mindestens 5 Leitentscheide (BGE) unter «I. Leitentscheide» und mindestens 5 weitere (BGer, kantonal) unter «II. Weitere Entscheide».
6. **Halluzinationsverbot**: Jede zitierte Quelle (Urteil, Literatur, Materialien) muss tatsächlich existieren und den Satz tragen, für den sie steht. Nichts erfinden, nichts aus dem Gedächtnis zitieren.
7. **Gesetzesübersicht** `content/kommentar/{gesetz}/_index.md` bei der Bearbeitung einzelner Artikel **nicht anfassen** (auch nicht für `revisions`). Sie wird nur einmalig bei der Aufnahme eines neuen Gesetzes angelegt.
8. **Tabellen** als reines Markdown im Textfluss, **nie** in Code-Fences (Hugo rendert sie sonst als Quelltext).

---

## 2. Zitierregeln (onlinekommentar.ch)

- **Urteile**: BGE-Nummer oder BGer-Urteilsnummer mit Datum und Erwägung — `BGE 142 III 16 E. 3.1`; `BGer 4A_123/2020 vom 1.3.2021 E. 4.2`.
- **Literatur**: Autor, Titel, Auflage, Ort/Jahr, Stelle (N oder S.) — `BK-Autor, Berner Kommentar, 2. Aufl., Bern 2021, N 12`. Nur Schweizer Quellen.
- **Materialien**: BBl-Fundstelle mit Seitenzahl — `BBl 2017 399, S. 450`.

---

## 3. Gliederung

**`_index.md`**: Gesetzeswortlaut (nur `{{< wortlaut >}}`) → Überblick und Bedeutung (Normzweck, Entstehungsgeschichte mit BBl) → Kommentierung (Rechtsprechung und Lehre im Text, mit Links) → Praxisfragen → Literatur.

**`rechtsprechung.md`**: «I. Leitentscheide» und «II. Weitere Entscheide». Je Eintrag eine fettgedruckte Themenüberschrift, der verlinkte Zitiertext mit Erwägung, **Sachverhalt** (kurz) und **Kernaussage** (die Aussage, gegen die die Belegprüfung läuft).

---

## 4. Abschluss

- Belegprüfung vor dem Schreiben ist Pflicht (Skill, Teil D.1).
- **Audit nur auf ausdrücklichen Wunsch des Users** — standardmässig reichen Belegprüfung und Build-Check.
- `hugo` lokal bauen; bei grünem Build committen und pushen.
