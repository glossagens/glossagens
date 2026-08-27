---
name: glossagens-audit
description: >
  Auditiert Glossagens-Kommentarartikel auf Belegtheit: prüft jedes Paar (Behauptungssatz, Beleg) — Gesetzeswortlaut,
  Existenz der Zitate, Pinpoints, wörtliche Zitate, ob der Entscheid die Behauptung wirklich trägt, und Aktualität.
  Fakten kommen aus den kostenfreien opencaselaw-Lookups, das Grounding-Urteil von Judge-Subagenten des jeweiligen
  Agenten (Claude Code, Antigravity, Hermes) — die LLM-Tools von opencaselaw werden nicht mehr aufgerufen.
  Bietet den Workflow /audit ({gesetz} | {gesetz} art-{nr}): wendet mechanisch belegbare Korrekturen automatisch an
  und legt alles Inhaltliche zur Bestätigung vor.
version: 2.0.0
author: Claude Code
license: MIT
tools:
  - Bash
  - Read
  - Edit
  - Task
metadata:
  hermes:
    tags: [Glossagens, Legal, Audit, Verification, QualityControl, AntiHallucination]
---

# Glossagens Audit — Belegtheit von Kommentarartikeln

## Zweck

`/lint` prüft den **Gesetzeswortlaut**. `/audit` prüft den **Belegapparat**: existieren die
zitierten Entscheide, stimmen die Fundstellen, und tragen sie die Aussagen, für die sie
angeführt werden.

Die Prüfeinheit ist das **Paar (Behauptungssatz, Beleg)** — nicht das Zitat allein. Ein
Entscheid, der thematisch passt, die konkrete Rechtsfolge aber nicht stützt, ist der Fehler,
der einem Praktiker vor Gericht schadet; nur die Prüfung gegen den tatsächlichen Satz
findet ihn.

## Geltungsbereich

Nur dieses Repo. Artikel liegen als Page Bundles:

```
content/kommentar/{gesetz}/art-{nr}/
├── _index.md            ← Fliesstext-Belege in Markdown-Links
└── rechtsprechung.md    ← Entscheidblöcke, zwei Bauformen im Bestand
```

Der Parser deckt sechs Zitierlagen ab — im Bestand kommen alle sechs vor:

| Lage | Beispiel | Behauptungssatz |
|---|---|---|
| Fliesstext, verlinkt | `… nicht darauf beschränkt ist ([BGE …](url)).` | Satz vor dem Link |
| Fliesstext, unverlinkt | `… bedürfen einer gesetzlichen Grundlage (BGE 146 I 49 E. 4.2).` | Satz vor dem Beleg |
| OCL-Zeile | `#### 2. BGE 135 I 187, E. 4.1` … `- **OCL**: [id](url)` | `**Kernaussage**` im Block |
| Link/Beleg in Überschrift | `### [BGE 146 IV 231](url) (13.7.2020)` | Feld im Block, sonst erster Absatz |
| Bold-Lead-Absatz | `**BGE 148 I 19** — Leitentscheid zu …` | Satz **nach** dem Beleg |
| Tabellenzeile | `\| BGE 126 I 68 \| 2000 \| Kernsatz … \|` | längste Zelle ohne den Beleg |

**Unverlinkte Zitierungen sind der Regelfall, nicht die Ausnahme.** Vor der Erweiterung
auf `CITE_PLAIN` sah der Parser nur Markdown-Links und meldete für neun von 26
BV-Artikeln «0 Paare» — ein Freispruch aus Blindheit. Über den BV-Bestand stieg die Zahl
der Prüfpaare von rund 370 auf 1358.

Als Behauptungssatz eines Entscheidblocks gilt das erste vorhandene Feld in der Rangfolge
`Kernaussage`/`Kernsatz` → `Regeste` → `Entscheid` → `Bedeutung`. `Sachverhalt` und
`Rechtsfrage` zählen bewusst nicht: das eine ist Tatsachenschilderung, das andere eine
Frage. Fehlt jedes Feld, greift der erste substanzielle Absatz des Blocks.

Wird ein Beleg dennoch keinem brauchbaren Satz zugeordnet, meldet Stufe 5
`claim_nicht_extrahierbar` — ein Parser-, kein Inhaltsbefund. Solche Fälle nie als
ungestützt werten.

### Audit-Protokolle sind vom Parsing ausgenommen

Ein überarbeiteter Artikel dokumentiert die ausgebauten Falschzitate namentlich. Alles ab
einer Überschrift `Entfernte Entscheide` / `Entfernte Belege` / `Nicht übernommen` /
`Audit-Protokoll` wird deshalb nicht als Beleg gelesen. Ohne diese Ausnahme meldet der
nächste Lauf genau die Referenzen wieder, die der letzte ausgebaut hat — die Transparenz
über eine Korrektur würde als Fehler gezählt. Neue Protokollüberschriften in dieses
Muster aufnehmen, nicht die Dokumentation weglassen.

**Ausgebaute Referenzen gehören ausschliesslich in diesen Abschnitt.** Wer sie zusätzlich
im Fliesstext nennt («die angeführten Entscheide BGE X und BGE Y stützten das nicht»),
erzeugt dort neue Paare, die Stufe 5 prompt als `unrelated` meldet — der eigene
Ehrlichkeitsvermerk drückt die Belegquote. Im Fliesstext auf das Protokoll verweisen,
die Nummern dort führen. Bei BV Art. 9 kostete das drei Paare und neun Prozentpunkte.

---

## KOSTENREGEL GEGENÜBER OPENCASELAW (verbindlich)

opencaselaw ist ein nichtkommerzielles Projekt und stellt den Bestand gratis
bereit. Ein Teil seiner Tools ruft im Hintergrund Claude auf und kostet den
Betreiber laut seiner Fair-Use-Richtlinie **$0.05–$0.50 pro Aufruf**. Für diese
Tools gilt ein Kontingent von 200 Aufrufen pro Tag und IP.

**Dieser Skill hat das überzogen.** Am 23.08.2026 hat der Betreiber den Client
`glossagens-audit/1.0` per IP gesperrt; im nginx-Regelwerk von opencaselaw steht
als Grund: *«4,229 verify_claim attempts in one day against a 200/day quota,
retry loop with no backoff»*. Seither antwortet der Server auf **alle** Anfragen
dieser IP mit 403 — auch auf die kostenlosen.

Daraus die Regeln, ausnahmslos:

| Tool | erlaubt? |
|---|---|
| `cite`, `get_law`, `get_erwaegung`, `get_regeste`, `get_decision`, `get_decision_structure`, `get_article_history` | ✅ frei — SQLite-Lookups, laut Fair-Use-Richtlinie ausdrücklich ungedrosselt |
| `check_claim_support`, `attest_response`, `reflect` | ⛔ **nie** — LLM-Aufruf beim Betreiber; `audit.py` blockt sie im Code |
| `search_decisions`, `search_laws`, `find_relevant_erwaegung`, `find_leading_cases`, übrige `search_*` | ⚠️ nur wenn ein Lookup die Antwort nicht liefert — Query-Parse, Expansion und Rerank sind serverseitig kleine LLM-Aufrufe |

Wer eine Referenz kennt, schlägt sie nach (`cite`), statt sie zu suchen. Wer
eine Erwägungsnummer sucht, holt die Struktur (`get_decision_structure`), statt
`find_relevant_erwaegung` zu rufen.

`audit.py` setzt das technisch durch: die drei LLM-Tools sind hart gesperrt,
Requests laufen mit fester Taktbremse (`GLOSSAGENS_AUDIT_RPS`, Vorgabe 4/s), und
bei 403 oder 429 bricht der Lauf ab, statt zu wiederholen.

---

## AUTONOMIE-VERTRAG (verbindlich)

**Modus: «Prüfen + mechanisch belegbare Fixes».**

| Aktion | Ohne Rückfrage? |
|--------|-----------------|
| Audit ausführen, Bericht erstellen | ✅ ja |
| Ungültigen Pinpoint entfernen (Zitat bleibt) | ✅ ja |
| Wörtliches Zitat durch Verbatim aus `get_erwaegung` ersetzen | ✅ ja |
| Referenz korrigieren, wenn `close_matches` **eindeutig** ist | ✅ ja |
| Gesetzeswortlaut aus `get_law` ersetzen | ✅ ja |
| `lastmod` + `revisions`-Eintrag setzen | ✅ ja (Pflicht) |
| Beleg entfernen bei `supports: no/contradicts/unrelated` | ⛔ Bestätigung |
| Satz umschreiben oder streichen | ⛔ Bestätigung |
| Artikel neu aufbauen oder löschen | ⛔ Bestätigung |
| `agent_verified` / `mcp_verified` auf `true` setzen | ⛔ nur wenn das Audit sauber ist |

**Kernregel:** Ein Satz, dessen Beleg wegfällt, wird **nie stillschweigend gelöscht**. Sonst
verschwindet die richtige Aussage mit dem falschen Beleg. Er wird markiert und vorgelegt.

---

## ANTI-HALLUZINATIONS-REGELN

1. Keine Zitierung selbst konstruieren. Ersatzzitate stammen wörtlich aus `citation_string_de`
   bzw. `markdown_link` einer `cite`-Antwort.
2. Keinen Pinpoint raten. Ohne `get_erwaegung`-Bestätigung wird er entfernt, nicht ersetzt.
   Ein Ersatz kommt aus `get_decision_structure` — dort stehen die tatsächlich
   vorhandenen Erwägungsnummern —, nie aus einer Schätzung und nicht aus
   `find_relevant_erwaegung` (Suchtool, siehe Kostenregel).
3. Gesetzeswortlaut nie aus dem Gedächtnis — nur aus `get_law`, mit Konsolidierungsdatum.
4. `supports: unrelated` bei hoher Konfidenz ist ein **Befund**, keine Messungenauigkeit.
5. Literaturzitate sind mit den Fall-Tools **nicht** verifizierbar → Status
   `nicht_verifizierbar`, niemals `korrekt`.

---

# WORKFLOW: `/audit`

## Aufrufformen

- `/audit {gesetz} art-{nr}` — ein Bundle (z. B. `/audit bv art-045`)
- `/audit {gesetz}` — alle Bundles eines Gesetzes
- `/audit` ohne Argument → nachfragen

## Schritt 1 — Mechanische Stufen 0–6

```bash
python3 agent/skills/glossagens-audit/audit.py content/kommentar/{gesetz}/art-{nr}
python3 agent/skills/glossagens-audit/audit.py content/kommentar/{gesetz} --all
```

Das Skript schreibt `audit-report.json` und gibt pro Artikel eine Kopfzeile aus.
Es cacht MCP-Antworten unter `~/.cache/glossagens-audit/`; Re-Runs kosten nichts.

Das Skript ruft **kein** LLM auf — weder bei opencaselaw noch sonstwo. Stufe 5
urteilt nicht selbst, sondern schlägt im **Verdikt-Ledger** nach
(`agent/skills/glossagens-audit/verdicts/ledger.jsonl`, im Repo versioniert).
Ein Paar ohne Verdikt erscheint als `offen`. **Offen ist kein Freispruch**: solche
Paare bleiben aus der Belegquote heraus, damit ein nicht gefälltes Urteil nie wie
ein bestandenes aussieht. Die Kopfzeile weist sie separat aus (`offen=n`).

Der Ledger enthält 11 728 Verdikte aus der Zeit, als Stufe 5 noch über
`check_claim_support` lief (Sonnet-4.6, bezahlt von opencaselaw). Sie bleiben
gültig und dienen zugleich als Vergleichsmassstab für neue Judge-Modelle.

Das Urteil ist nicht deterministisch: derselbe Fall liefert mal `no`, mal
`contradicts`. Die Belegquote schwankt zwischen zwei Läufen um ein bis zwei
Prozentpunkte — das ist der Judge, nicht der Harness. Für die Urteilsgrenzen
(A ≥ 80 %, B ≥ 50 %) heisst das: knappe Fälle nicht auf den Punkt genau lesen.

Zwei Cache-Fallen, beide im Skript entschärft, beim Ändern nicht wieder aufreissen:
`PARSER_VERSION` ist Teil des Cache-Keys (sonst liefert der Cache Ergebnisse der alten
Auswertung — bei Änderungen am Antwort-Parsing hochzählen), und Fehlantworten werden
**nicht** gecacht (sonst friert ein transienter Netzfehler als Dauerbefund ein).

| Stufe | Tool | Prüft |
|---|---|---|
| 0 Inventar | — | Bundle parsen: Wortlaut, Paare, Verbatim-Zitate ≥30 Zeichen |
| 1 Wortlaut | `get_law` | zitierter Gesetzestext absatzweise gegen Fedlex |
| 2 Existenz | `cite` | existiert die Referenz? sonst `close_matches` |
| 3 Pinpoint | `get_erwaegung` | existiert E. X.Y? |
| 4 Verbatim | `get_regeste`, `get_decision_structure` | wörtliche Zitate exakt im Quelltext |
| 5 Grounding | Judge-Subagent über den Ledger | trägt der Entscheid den Behauptungssatz? |
| 6 Aktualität | `get_article_history` | Belege vor der letzten Revision; einschlägige Entscheide, die fehlen |

**Gating:** Stufe 5 läuft nur auf Paaren, die 2–4 überlebt haben. Für ein
halluziniertes Zitat wird weder ein Prüftext geholt noch ein Judge bemüht.

> Der MCP wird per HTTP-JSON-RPC angesprochen, nicht über die MCP-Client-Tools:
> batchbar, cachebar und mit fester Taktbremse.
> Antworten kommen als SSE; JSON-Antworten tragen
> einen angehängten Hinweis-Footer, `get_law` antwortet ganz als Markdown — beides
> behandelt `Mcp._parse`.

## Schritt 1b — Offene Paare beurteilen lassen (Stufe 5)

```bash
# 1. Jobs ausgeben — holt den Prüftext über die kostenfreien Lookups
python3 agent/skills/glossagens-audit/audit.py content/kommentar/{gesetz}/art-{nr} --emit-jobs
#    → audit-jobs/{gesetz}-{nr}/jobs.jsonl

# 2. Urteilen lassen (siehe unten) → audit-jobs/{gesetz}-{nr}/verdicts-*.jsonl

# 3. Verdikte prüfen und in den Ledger schreiben
python3 agent/skills/glossagens-audit/audit.py --ingest audit-jobs/{gesetz}-{nr}
```

Ein Job ist **selbsttragend**: `claim`, `decision_id`, `pinpoint` und der `text`,
gegen den zu urteilen ist. Der Judge braucht damit keinerlei Werkzeuge — und darf
auch keine benutzen. Genau deshalb trägt dasselbe Verfahren für jeden Agenten:
Claude Code verteilt die Jobs auf Task-Subagenten, Antigravity auf sein eigenes
Fan-out, Hermes schickt sie einzeln durch `generate()`; keiner von ihnen braucht
für Stufe 5 einen MCP-Zugang.

**Als Claude Code:** Jobs in Scheiben zu 10–15 aufteilen, pro Scheibe ein
Subagent mit genau diesem Auftrag:

> Lies `agent/skills/glossagens-audit/judge-prompt.md` und beurteile die Zeilen
> {a}–{b} von `audit-jobs/{gesetz}-{nr}/jobs.jsonl`. Benutze **keine** Werkzeuge
> ausser Read und Write; urteile ausschliesslich über den mitgelieferten `text`.
> Schreibe eine JSON-Zeile pro Job nach
> `audit-jobs/{gesetz}-{nr}/verdicts-{scheibe}.jsonl`.

`--ingest` prüft jede Zeile mechanisch: Enum, Wertebereich, `job_id`, und ob die
Exzerpte **wörtlich** im Prüftext stehen. Verworfene Zeilen werden mit Grund
gemeldet und gelten als nicht geurteilt — nie als Befund gegen den Kommentar.
Ein Judge, der Exzerpte erfindet, fällt hier auf; der opencaselaw-Server hat
diese Bedingung nur im Prompt verlangt und nie nachgeprüft.

**Ein `no`/`contradicts`/`unrelated`, das zum Ausbau eines Belegs führt, braucht
die Bestätigung eines zweiten Modells.** Das sind wenige Paare pro Artikel; der
Schaden eines falschen Ausbaus — eine richtige Aussage verliert ihren Beleg —
wiegt schwerer als der Aufwand einer zweiten Meinung. `yes` bleibt einstimmig.

## Schritt 2 — Befunde klassifizieren

| Befund | Quelle | Aktion |
|--------|--------|--------|
| Wortlaut abweichend | Stufe 1 | ersetzen (sicher) |
| Referenz existiert nicht, `close_matches` eindeutig | Stufe 2 | korrigieren (sicher) |
| Referenz existiert nicht, kein Match | Stufe 2 | markieren, vorlegen |
| Pinpoint fehlt | Stufe 3 | entfernen (sicher) |
| Verbatim abweichend | Stufe 4 | ersetzen (sicher) |
| `partial` | Stufe 5 | Aussage abschwächen — vorlegen |
| `no` / `contradicts` / `unrelated` | Stufe 5 | Beleg raus — vorlegen |
| Beleg vor letzter Revision | Stufe 6 | prüfen, ob noch aussagekräftig — vorlegen |
| Einschlägige Entscheide nicht zitiert | Stufe 6 | Ergänzung vorschlagen |

**Eine `close_matches`-Korrektur ist nur dann «sicher», wenn `match_reason` die Identität
belegt** (z. B. `queried_page_within_this_decision` bei identischem Band). Ein blosser
Nachbartreffer auf derselben Seite ist es nicht — der wird vorgelegt.

### Gesamturteil

Belegquote = `(yes + 0.5 × partial) / beurteilte Paare`. `partial` zählt halb: die Aussage
ist tragfähig, aber zu weit gefasst. Nicht beurteilte Paare
(`nicht_verifizierbar`, `claim_nicht_extrahierbar`) bleiben aus dem Nenner — das Skript
rechnet das in `zusammenfassung.belegquote_prozent` / `urteil` aus.

| Belegquote | Urteil |
|---|---|
| ≥ 80 % | A — punktuelle Fixes |
| 50–79 % | B — Überarbeitung vorlegen |
| < 50 % | C — Neuaufbau vorlegen; Einzelfixes lohnen nicht |

Bei C **keine** Einzelkorrekturen anwenden. Wer in einem durchgehend unbelegten Artikel
Pinpoints repariert, erzeugt den Anschein von Sorgfalt, ohne die Substanz zu verbessern.

## Schritt 3 — Sichere Fixes anwenden

Nur die als sicher markierten. Danach in **jeder** geänderten Datei:

```yaml
lastmod: {heute}
revisions:
  - date: {heute}
    by: "Claude Code"
    model: "{exakte Modell-ID}"
    mcp_verified: true
    note: "Audit: Belege gegen opencaselaw-MCP geprüft; {kurz was}"
```

`mcp_verified: true` ist hier zulässig, weil jeder Fix aus einer MCP-Antwort stammt.
`agent_verified: true` nur, wenn das Audit **ohne** offene Befunde durchläuft.

## Schritt 4 — Schlussattest: derselbe Lauf auf dem korrigierten Text

```bash
python3 agent/skills/glossagens-audit/audit.py content/kommentar/{gesetz}/art-{nr} --emit-jobs
```

Das frühere `attest_response` braucht keinen Ersatz. Es war serverseitig zu neun
Zehnteln dasselbe, was die Stufen 0–4 hier ohnehin tun — Zitate parsen, Existenz,
Pinpoints, Verbatim —, plus derselbe Grounding-Judge. Ein zweiter Lauf über den
korrigierten Text leistet dasselbe und ist schärfer, weil er den ganzen Artikel
prüft und nicht nur den Abschnitt, den man ihm vorlegt.

Neue und geänderte Sätze erzeugen neue `job_id`s und sind damit automatisch
`offen`; sie durchlaufen Schritt 1b erneut. Bestanden ist das Attest, wenn kein
Paar mehr `offen` ist und keine Befunde offenstehen. Entfällt bei Urteil C —
dort gibt es keinen korrigierten Text.

## Schritt 5 — Bericht

```
AUDIT-BERICHT: {GESETZ} Art. {NR}   (Fedlex-Stand {Datum})
──────────────────────────────────────────────
Wortlaut:        {status}
Belegpaare:      {n} geprüft
  gestützt:      {n}     teilweise: {n}
  ungestützt:    {n}  ({no}/{contradicts}/{unrelated})
  offen:         {n}  (kein Verdikt — bleibt aus der Quote)
  Judge:         {Modelle}
Referenzen:      {n} geprüft, {n} nicht existent
Pinpoints:       {n} fehlerhaft
Verbatim:        {n} abweichend
Aktualität:      {n} Belege vor letzter Revision
                 {n} einschlägige Entscheide nicht zitiert

Gesamturteil: {A|B|C} — {Quote} gestützt

Sichere Fixes angewendet: {Liste}
Zur Bestätigung:          {Liste mit Fundstelle und Grund}
Nicht verifizierbar:      {Liste + Grund}
```

Commit/Push nur auf Verlangen — direkter Commit auf `main` löst Auto-Deploy aus.

---

## Grenzen — im Bericht ausweisen, nicht kaschieren

- **Literaturzitate.** Die Fall-Tools decken sie nicht ab; `search_scholarship` /
  `find_scholarship_citing_statute` erreichen die OA-Bestände, der klassische
  Kommentarapparat (BSK, ZK, Stämpfli) liegt grösstenteils ausserhalb.
- **Botschaften.** `BBl`-Fundstellen prüft dieses Audit nicht; dafür `search_botschaft`.
- **Juristische Richtigkeit.** Geprüft wird Belegtheit, nicht Qualität. Ein durchgehend
  belegter Kommentar kann dogmatisch schief sein.
- **Aktualität — der gefährlichste blinde Fleck.** Das Grounding-Urteil beantwortet
  «sagt der Entscheid das?», nicht «gilt das noch?». Bei BV Art. 13 stand BGE 137 V 334
  korrekt zitiert und mit zutreffender Wiedergabe im Text — und war trotzdem falsch:
  die Aussage zur gemischten Methode der Invaliditätsbemessung ist durch das
  EGMR-Urteil *Di Trizio gegen die Schweiz* (2016) überholt. Stufe 6 findet das nur,
  wenn eine Gesetzesrevision dazwischenliegt; eine Praxisänderung durch EGMR oder
  Bundesgericht sieht sie nicht. Bei Leitentscheiden, die älter als rund zehn Jahre
  sind und eine Grundrechtsfrage entscheiden, deshalb zusätzlich nach einer
  Praxisänderung suchen — hier ist `search_decisions` trotz Kostenregel richtig,
  weil kein Lookup die Frage beantwortet (mit dem Sachthema + «Praxisänderung»
  bzw. dem EGMR-Fallnamen). Ein `yes` ist kein Aktualitätsnachweis.
- **Nur Bundesentscheide** haben strukturierte Erwägungen; bei kantonalen greift Stufe 3
  nicht.

## Referenzläufe (2026-08-11)

| | BV Art. 45 | StPO Art. 429 | BV Art. 5 vorher | BV Art. 5 nachher |
|---|---|---|---|---|
| Paare | 20 | 31 | 28 | 31 |
| Referenzen nicht existent | 12 von 16 | 0 von 13 | 6 von 12 | 0 |
| Pinpoint-Fehler | 3 | 3 | 3 | 0 |
| Grounding | 7× `unrelated` | 22× `yes`, 8× `partial`, 1× `contradicts` | 0× `yes`, 7× `unrelated` | 28× `yes`, 3× `partial` |
| Belegquote | **0 % — C** | **84 % — A** | **12 % — C** | **95 % — A** |

BV Art. 5 zeigt, wie ein C-Artikel zu sanieren ist: Belegapparat verwerfen, Aussagen
behalten, für jede Aussage einen Beleg suchen und **vor** dem Schreiben einzeln
durch einen Judge prüfen lassen. Die dabei wiederkehrende Beobachtung: ein `partial` heisst
meist, dass die Paraphrase einen Qualifikator des Gerichts weggelassen hat
(«in Anbetracht der Schwere der Grundrechtseinschränkung», «verfassungsmässiges
*Individual*recht»). Wörtlich zitieren macht daraus ein `yes`.

Ebenso wiederkehrend: eine Regeste verweist auf «(E. 4)», aber die Erwägung existiert nur
als `4.1`/`4.2.1`. `cite` akzeptiert den Abschnittsverweis trotzdem — erst
`get_erwaegung` deckt auf, dass der Pinpoint ins Leere zeigt. Den echten Pinpoint
liefert die Erwägungsliste aus `get_decision_structure`, nie eine Schätzung.

Art. 45 und Art. 429 trugen beide `mcp_verified: true`. Zwei Lehren:

1. **Stufe 5 ist nicht weglassbar.** Die vier existierenden BV-45-Entscheide bestehen
   Stufe 2 anstandslos — und behandeln SchKG, Dividendenbesteuerung, vorsorgliche
   Massnahmen im Immaterialgüterrecht und Einbürgerungen. Ohne Grounding sähe der Artikel
   nach vier sauberen Belegen aus.
2. **Der Parser entscheidet über die Befundqualität.** Vor dem Fix für die Zitierlage
   «Link in Überschrift» meldete StPO 429 11/31 gestützt und 9 `unrelated` — fast alles
   Artefakte falsch zugeordneter Behauptungssätze. Ein neues Layout im Bestand erzeugt
   Falschalarme, keine stillen Lücken; bei auffällig vielen `unrelated` in **einer** Datei
   zuerst die Zitierlage prüfen, nicht den Kommentar verurteilen.
