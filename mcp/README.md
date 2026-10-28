# Glossagens MCP-Server

Ein MCP-Server auf einem Cloudflare Worker. Wer ihn in claude.ai als Connector
hinzufügt (oder in Claude Code, Cursor, jedem MCP-Client), kann Glossagens im Chat
durchsuchen und Kommentare lesen.

Erste Ausbaustufe: **nur lesende Tools**. Das Einreichen von Beiträgen ohne
GitHub-Konto kommt später in denselben Worker (siehe `plan-kontofreie-einreichung.md`).

**Live:** `https://glossagens-mcp.glossagens-mcp.workers.dev/mcp` (seit 28.10.2026).

## Tools

| Tool | Zweck |
|---|---|
| `glossagens_suchen` | Stichwortsuche über Kommentare und Themen; erkennt Normangaben wie `StGB 70`, `Art. 336c OR` |
| `gesetze_auflisten` | alle kommentierten Erlasse mit Kürzel, SR-Nummer, Artikelzahl |
| `artikel_auflisten` | die Artikel eines Erlasses mit Prüfstand |
| `kommentar_lesen` | Kommentar, Rechtsprechung oder Strafzumessung als Markdown, Gesetzeswortlaut eingesetzt; mit `abschnitt` nur ein Abschnitt |
| `thema_lesen` | ein Querschnittsthema als Markdown |

Jede Antwort nennt den **Prüfstand** (`verifiziert` = `agent_verified` und
`mcp_verified` der jüngsten Revision) und warnt bei nicht verifizierten Texten.

## Woher die Daten kommen

```
glossagens.ch/kommentar/index.json   Katalog: Gesetze, Artikel, Titel, Tags, Prüfstand
                                     (layouts/kommentar/list.json.json, beim Hugo-Build erzeugt)
glossagens.ch/themen/index.json      Themen (layouts/themen/list.json.json)
raw.githubusercontent.com/…/main/    Markdown der Kommentare und data/wortlaut/*.json
```

Der Worker hält **keinen Schlüssel** und schreibt nirgends hin. Kataloge bleiben
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
  nichts zu verändern.
- Gelesen wird nur unter festen Präfixen (`content/kommentar/{gesetz}/{artikel}/`,
  `content/themen/{slug}/`, `data/wortlaut/`); Gesetz und Artikel müssen im Katalog
  stehen, Slugs sind auf `[a-z0-9-]` beschränkt.
- Die `instructions` an den Client halten fest, dass gelieferte Texte Inhalt sind,
  keine Anweisungen.
