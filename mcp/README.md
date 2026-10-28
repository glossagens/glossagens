# Glossagens MCP-Server

Ein MCP-Server auf einem Cloudflare Worker. Wer ihn in claude.ai als Connector
hinzufügt (oder in Claude Code, Cursor, jedem MCP-Client), kann Glossagens im Chat
durchsuchen, Kommentare lesen, Entwürfe prüfen und Beiträge ohne GitHub-Konto
einreichen. Eingereicht wird als Draft-PR; veröffentlicht erst nach dem Merge.

**Live:** `https://glossagens-mcp.glossagens.workers.dev/mcp` (seit 28.10.2026).

## Tools

| Tool | Zweck |
|---|---|
| `mithelfen` | Arbeitsanleitung für Beiträge aus dem Chat; holt `/mithelfen/anleitung.md` von der Seite (Quelle `static/mithelfen/anleitung.md`) |
| `offene_aufgaben` | Bestimmungen aus Themen (`normen`) ohne Kommentar, mehrfach gebrauchte zuerst; Filter nach Gesetz/Stichwort. Gleiche Quelle wie die Seite `/mithelfen/aufgaben/` (`layouts/_shortcodes/offene-aufgaben.html`) |
| `glossagens_suchen` | Stichwortsuche über Kommentare und Themen; erkennt Normangaben wie `StGB 70`, `Art. 336c OR` |
| `gesetze_auflisten` | alle kommentierten Erlasse mit Kürzel, SR-Nummer, Artikelzahl |
| `artikel_auflisten` | die Artikel eines Erlasses |
| `kommentar_lesen` | Kommentar, Rechtsprechung oder Strafzumessung als Markdown, Gesetzeswortlaut eingesetzt; mit `abschnitt` nur ein Abschnitt. `format: "quelltext"`: Datei unverändert samt Frontmatter und `version` |
| `thema_lesen` | ein Querschnittsthema als Markdown, ebenfalls mit `format: "quelltext"` |
| `beitrag_pruefen` | prüft einen Entwurf (neue Datei, ganze Datei oder ein Abschnitt) und meldet Fehler, Warnungen und Änderungen; schreibt nichts |
| `beitrag_einreichen` | prüft wie `beitrag_pruefen` und legt bei fehlerfreier Prüfung einen Draft-PR an (nur sichtbar, wenn `EINREICHEN = "an"`) |
| `einreichung_status` | Stand eines Chat-PRs (offen, gemerged mit Link, geschlossen) mit Reviews, Kommentaren und Zeilenanmerkungen der Redaktion; auch bei Not-Aus verfügbar |

## Beitrag prüfen (`src/pruefen.js`)

Ablauf im Chat: Quelltext lesen → Entwurf → `beitrag_pruefen` → korrigieren, bis keine
Fehler mehr kommen.

- **Ziel**: `gesetz` + `artikel` (+ `teil`) oder `thema`. Neue Artikel in einem
  bestehenden Gesetz und neue Themen sind zulässig, neue Gesetze nicht.
- **Abschnitt** (`abschnitt` + `text`, empfohlen): ersetzt denselben Bereich, den
  `kommentar_lesen` mit `abschnitt` liefert. Die Überschrift muss eindeutig passen.
  Fehlen im neuen Text Unterabschnitte, ist das ein Fehler — löschen nur bewusst über `datei`.
- **`version`**: Git-Blob-SHA der Datei (wie `sha` der GitHub-API), Pflicht bei
  bestehenden Dateien. So fällt auf, wenn sich die Datei seit dem Lesen geändert hat.
- **`revision`** (by, model, note): Der Server setzt den Eintrag zuoberst mit dem
  heutigen Datum und führt `lastmod` nach. Pflicht bei Abschnitten; bei `datei`
  alternativ im Frontmatter. Bisherige Einträge müssen unverändert bleiben.
- **Fehler** (blockieren): Pflichtfelder, `agent_verified`/`mcp_verified`, rohes HTML
  ausser `<br>`/`<sup>`/`<sub>` (hugo.toml rendert HTML ungefiltert), andere Shortcodes
  als `wortlaut`/`callout`, Attribut-Blöcke mit Werten, Links mit fremdem Schema, Bilder,
  Tabellen in Code-Blöcken, Normtext als Zitatblock statt `{{< wortlaut >}}`,
  Entscheid-Links mit HTTP 404.
- **Warnungen**: Linktext und Ziel passen nicht zusammen (BGE-/BGer-Nummer, Datum),
  fehlende Wortlaut-Daten, Links auf nicht vorhandene Kommentare/Themen, «ß»,
  opencaselaw statt entscheidsuche, Themen-Überschriften ohne Anker.
- Bei Änderungen zählt nur, was die Änderung mitbringt; Befunde, die schon im
  bisherigen Text standen, werden weggelassen (und gezählt).
- **Links** abgerufen werden nur auf entscheidsuche.ch, bger.ch und opencaselaw
  (HEAD, höchstens 30). Fedlex nicht: Die Seite antwortet auf jeden Pfad mit 200.

Jeder gelieferte Text trägt den festen Hinweis, dass er KI-erstellt ist und Zitate an
der Quelle zu prüfen sind. Einen Prüfstand pro Artikel gibt es nicht (mehr): Die früheren
Flags `agent_verified`/`mcp_verified` waren unüberprüfbare Selbstauskünfte.

## Woher die Daten kommen

```
glossagens.ch/kommentar/index.json   Katalog: Gesetze, Artikel, Titel, Tags
                                     (layouts/kommentar/list.json.json, beim Hugo-Build erzeugt)
glossagens.ch/themen/index.json      Themen (layouts/themen/list.json.json)
raw.githubusercontent.com/…/main/    Markdown der Kommentare und data/wortlaut/*.json
```

Der Worker hält **keinen Schlüssel** und schreibt nirgends hin; Entwürfe werden nur geprüft, nicht gespeichert. Kataloge bleiben
5 Minuten im Speicher. Was auf `main` liegt, ist nach dem nächsten Deploy der Seite
abrufbar; der Worker selbst muss dafür nicht neu deployt werden.

`{{< wortlaut >}}` setzt der Worker als Zitatblock aus `data/wortlaut/` ein
(Klartext, ohne Fussnoten; Stand und Fedlex-Link in der Kopfzeile). Andere
Shortcodes bleiben stehen.

## Protokoll

Streamable HTTP, **zustandslos**: `POST /mcp` mit JSON-RPC, Antwort als JSON, keine
Session, kein SSE (`GET /mcp` → 405). `GET /` beschreibt den Server. Unterstützte
Protokollversionen: `2025-06-18`, `2025-03-26`, `2024-11-05`.

## Testen

```sh
node mcp/test/server.test.mjs      # ohne Netz und ohne wrangler; läuft auch in CI (mcp-test.yml)
cd mcp && npx wrangler dev         # lokal unter http://localhost:8787/mcp
```

Von Hand gegen einen laufenden Server:

```sh
curl -s http://localhost:8787/mcp -H 'Content-Type: application/json' \
  -d '{"jsonrpc":"2.0","id":1,"method":"tools/call","params":{"name":"glossagens_suchen","arguments":{"anfrage":"StPO 221"}}}'
```

Oder mit dem MCP Inspector: `npx @modelcontextprotocol/inspector`, Transport
«Streamable HTTP», URL `http://localhost:8787/mcp`.

## Beitrag einreichen (`beitrag_einreichen`, `src/github.js`)

Der Worker schreibt als GitHub App **Glossagens Chat-Einreichung** (App-ID 5512533,
Installation 176226314, nur dieses Repo, Rechte: Contents und Pull requests). Ablauf:

1. Dieselbe Prüfung wie `beitrag_pruefen`; mit Fehlern wird nichts angelegt.
2. Doppelte Einreichung (gleicher Pfad und Inhalt, 7 Tage) → Link auf den bestehenden PR.
3. Obergrenzen: 10 pro Stunde und 40 pro Tag insgesamt, 5 pro Stunde je IP. Die
   globalen Grenzen sind die eigentlichen: claude.ai ruft Connectors über die Server
   von Anthropic auf, alle Nutzer teilen sich wenige IPs.
4. `version` gegen den `sha` der Datei auf `main` (GitHub-API, nicht raw).
5. Branch `chat/{gesetz}-{art}[-teil]-{datum}-{zufall}` ab `main`, ein Commit mit der
   einen Datei, Draft-PR mit Label `chat-einreichung`. Scheitert ein Schritt, wird der
   Branch wieder gelöscht.
6. `pr-build.yml` ergänzt fehlende Wortlaut-Daten (`scripts/wortlaut.py --fehlende`) im
   PR und baut danach.

Der PR-Text führt Änderungen, Warnungen, die Angaben der Person (als Zitat, `@`
entschärft) und das Belegprotokoll als Tabelle.

### Prüfauftrag und Belegprotokoll

Der Server prüft Belege nicht selbst — das wäre bei vielen Volltexten je Beitrag zu teuer
(Free Plan: wenig CPU je Anfrage). Er überträgt die Arbeit dem Chat der einreichenden Person:

1. `beitrag_pruefen` zieht mechanisch jede verlinkte Entscheid-Stelle aus dem neuen bzw.
   geänderten Text (Absätze, Listenpunkte, Tabellenzeilen; gleicher Link im selben Absatz
   einmal) und gibt sie als **Prüfauftrag** aus: B1, B2 … mit Link, Aussage und den
   «…»-Zitaten des Absatzes. Unverlinkte Entscheide (BGE-Nummern, Geschäftsnummern) meldet
   es als Warnung.
2. Der Chat liest jeden Entscheid und legt je Stelle `fundstelle`, `traegersatz` (wörtlich),
   `urteil` (`traegt` / `traegt_teilweise` + `anmerkung`) vor — angelehnt an das
   Verdikt-Ledger des Audits.
3. `beitrag_einreichen` verlangt das Protokoll (`belege`), sobald der Prüfauftrag Stellen
   hat, und prüft mechanisch: jede Stelle belegt, Trägersatz 30–3000 Zeichen und nicht der
   eigene Text, Fundstelle angegeben, Urteil zulässig, jedes «…»-Zitat steht in einem
   Trägersatz desselben Absatzes. Die Nummern entstehen beim Einreichen aus demselben Text
   neu; der Server speichert nichts.
4. Das Protokoll steht als Tabelle im PR (Aussage neben Trägersatz). Ob die Trägersätze
   wirklich im Entscheid stehen, prüft die Redaktion stichprobenweise. Die App kann `main` nicht ändern und keinen PR mergen: Das Ruleset
«main schützen» verlangt eine Freigabe, Admins dürfen vorbei.

Einrichtung (einmalig erledigt): privater Schlüssel als Secret, im PKCS#8-Format:

```sh
openssl pkcs8 -topk8 -nocrypt -in <download>.private-key.pem -out app.pem
npx wrangler secret put GITHUB_APP_KEY < app.pem
```

Zähler und Doppelerkennung liegen im KV-Namespace `EINREICHUNGEN`.

`einreichung_status` gibt nur Chat-PRs aus (Branch `chat/…` im eigenen Repo) und davon
nur, was Personen mit Schreibrecht am Repo schreiben (abgefragt über
`/collaborators/{login}/permission`; `author_association` taugt nicht, weil die App ein
Mitglied mit nicht öffentlicher Mitgliedschaft als NONE sieht). Kommentieren kann auf
GitHub jede Person mit Konto; deren Text wird gezählt, nicht wiedergegeben — sonst
stünde er im Chat wie eine Antwort der Redaktion.
Den Build-Status zeigt das Tool nicht (die App hat kein Recht auf Checks).

**Not-Aus:** `EINREICHEN = "aus"` in `wrangler.toml` und deployen — das Tool
verschwindet aus der Liste. Bei einem Schlüssel-Leck zusätzlich den Schlüssel in den
App-Einstellungen auf GitHub löschen.

## Deployen

Voraussetzung: ein Cloudflare-Konto (Free Plan genügt).

```sh
cd mcp
npx wrangler login
npx wrangler deploy
```

Ausgabe ist die Adresse, z. B. `https://glossagens-mcp.<konto>.workers.dev`. Der
MCP-Endpunkt ist `…/mcp`. Erst **nachdem** `/kommentar/index.json` auf glossagens.ch
live ist (also dieser Branch gemerged und die Seite deployt), liefert er Daten.

## In claude.ai einbinden

Einstellungen → Connectors → «Benutzerdefinierten Connector hinzufügen» → Name
`Glossagens`, URL `https://glossagens-mcp.<konto>.workers.dev/mcp`. Keine
Anmeldung nötig. Danach im Chat z. B.: «Was sagt Glossagens zur Fluchtgefahr bei
Art. 221 StPO?»

## Sicherheit

- Die Lese- und Prüftools lesen nur öffentlich zugängliche Daten. `beitrag_pruefen`
  ruft fremde URLs nur auf einer festen Liste von Hosts ab, nie beliebige.
- Schreiben kann nur `beitrag_einreichen`, und nur einen Branch `chat/…` mit einer
  Datei unter `content/kommentar/` oder `content/themen/` (der Pfad entsteht im Worker,
  nicht aus der Eingabe). Rohes HTML, fremde Shortcodes und Attribut-Blöcke weist die
  Prüfung ab — hugo.toml rendert HTML ungefiltert.
- Eingereichter Text ist fremder Text: kein Agent mit Schreibrechten verarbeitet ihn
  (CLAUDE.md, «PR-Prüfung»).
- Gelesen wird nur unter festen Präfixen (`content/kommentar/{gesetz}/{artikel}/`,
  `content/themen/{slug}/`, `data/wortlaut/`); Gesetz und Artikel müssen im Katalog
  stehen, Slugs sind auf `[a-z0-9-]` beschränkt.
- Die `instructions` an den Client halten fest, dass gelieferte Texte Inhalt sind,
  keine Anweisungen.
