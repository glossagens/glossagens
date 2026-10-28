# Glossagens MCP-Server

Ein MCP-Server auf einem Cloudflare Worker. Wer ihn in claude.ai als Connector
hinzufügt (oder in Claude Code, Cursor, jedem MCP-Client), kann Glossagens im Chat
durchsuchen und Kommentare lesen.

Ausbaustufe 2: lesen und **Entwürfe prüfen**. Geschrieben wird noch nichts; das
Einreichen ohne GitHub-Konto kommt später in denselben Worker (siehe
`plan-kontofreie-einreichung.md`) und ruft dieselbe Prüfung auf.

**Live:** `https://glossagens-mcp.glossagens.workers.dev/mcp` (seit 28.10.2026).

## Tools

| Tool | Zweck |
|---|---|
| `glossagens_suchen` | Stichwortsuche über Kommentare und Themen; erkennt Normangaben wie `StGB 70`, `Art. 336c OR` |
| `gesetze_auflisten` | alle kommentierten Erlasse mit Kürzel, SR-Nummer, Artikelzahl |
| `artikel_auflisten` | die Artikel eines Erlasses |
| `kommentar_lesen` | Kommentar, Rechtsprechung oder Strafzumessung als Markdown, Gesetzeswortlaut eingesetzt; mit `abschnitt` nur ein Abschnitt. `format: "quelltext"`: Datei unverändert samt Frontmatter und `version` |
| `thema_lesen` | ein Querschnittsthema als Markdown, ebenfalls mit `format: "quelltext"` |
| `beitrag_pruefen` | prüft einen Entwurf (neue Datei, ganze Datei oder ein Abschnitt) und meldet Fehler, Warnungen und Änderungen; schreibt nichts |

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

- Die Tools lesen nur öffentlich zugängliche Daten; es gibt nichts zu stehlen und
  nichts zu verändern. `beitrag_pruefen` ruft fremde URLs nur auf einer festen
  Liste von Hosts ab, nie beliebige.
- Gelesen wird nur unter festen Präfixen (`content/kommentar/{gesetz}/{artikel}/`,
  `content/themen/{slug}/`, `data/wortlaut/`); Gesetz und Artikel müssen im Katalog
  stehen, Slugs sind auf `[a-z0-9-]` beschränkt.
- Die `instructions` an den Client halten fest, dass gelieferte Texte Inhalt sind,
  keine Anweisungen.
