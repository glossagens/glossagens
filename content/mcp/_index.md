---
title: Glossagens im KI-Chat (MCP)
linkTitle: MCP
weight: 9
description: Glossagens als Connector in claude.ai und anderen KI-Assistenten einbinden — Kommentare und aktuelle Rechtsprechung von bger-update.ch durchsuchen und lesen, direkt im Chat.
---

Glossagens lässt sich als **MCP-Connector** in einen KI-Chat einbinden. Der Assistent kann
dann selbst in Glossagens suchen, Kommentare lesen und mit Link auf die Fundstelle
antworten — etwa auf die Frage «Was sagt Glossagens zur Fluchtgefahr bei Art. 221 StPO?».

Technisch ist das ein Server nach dem [Model Context Protocol](https://modelcontextprotocol.io)
(MCP), einem offenen Standard, den Claude, ChatGPT und viele andere Assistenten verstehen.
Eine Anmeldung braucht es nicht.

Wer aus dem Chat heraus am KI-Kommentar **mitwirken** möchte, d.h. neue Gesetzeskommentare, neue Themen oder Korrekturen einreichen will, findet alles Nötige — auch die weiteren benötigten Connectors für die Recherche von Gesetzestexten und Urteilen — unter [Mitwirken](/mitwirken/).

## Adresse

```text
https://glossagens-mcp.glossagens.workers.dev/mcp
```

## Einrichten in claude.ai

1. In claude.ai **Einstellungen → Connectors** öffnen.
2. **Benutzerdefinierten Connector hinzufügen** wählen.
3. Name `Glossagens`, URL wie oben eintragen und bestätigen. Eine Anmeldung ist nicht nötig.
4. In einem neuen Chat über das Werkzeug-Menü den Connector **Glossagens** aktivieren.

Benutzerdefinierte Connectors stehen je nach Abo unterschiedlich zur Verfügung; in der
Claude-App für Desktop und Mobile erscheinen sie nach der Einrichtung im Browser automatisch.

## Einrichten in anderen Programmen

**Claude Code**:

```sh
claude mcp add --transport http glossagens https://glossagens-mcp.glossagens.workers.dev/mcp
```

**Andere Clients** (Cursor, VS Code, ChatGPT-Connectors u. a.): einen MCP-Server vom Typ
«Streamable HTTP» mit der Adresse oben hinzufügen.

## Was der Assistent damit tun kann

| Werkzeug | Zweck |
|---|---|
| `glossagens_suchen` | Kommentare und Themen nach Stichworten finden; Normangaben wie «StGB 70» oder «Art. 336c OR» führen direkt zum Kommentar |
| `gesetze_auflisten` | alle kommentierten Erlasse |
| `artikel_auflisten` | die kommentierten Artikel eines Erlasses |
| `kommentar_lesen` | Kommentar, Rechtsprechungsübersicht oder Strafzumessung zu einem Artikel, mit Gesetzeswortlaut aus Fedlex; auf Wunsch nur ein Abschnitt |
| `thema_lesen` | ein Querschnittsthema wie bspw. "Das System der Altervorsorge in der Schweiz" lesen |
| `bger_update_suchen` | in den Zusammenfassungen von [bger-update.ch](https://www.bger-update.ch) suchen (neue Urteile des Bundesgerichts, ausgewählte Entscheide anderer Gerichte), dazu in Editorials und Ticker; nicht im Urteilstext selbst ([mehr](#rechtsprechung-von-bger-updatech)) |
| `bger_update_lesen` | eine Zusammenfassung oder ein Editorial von bger-update.ch lesen; auf Wunsch nur ein Abschnitt |
| `mitwirken` | die Arbeitsanleitung für Beiträge aus dem Chat |
| `offene_aufgaben` | LIste fehlender Kommentare anzeigen: unkommentierte Bestimmungen, die in Themen vorkommen ([Liste](/mitwirken/aufgaben/)) |
| `beitrag_pruefen` | einen Entwurf für einen Kommentar oder ein Thema prüfen, bevor er eingereicht wird |
| `beitrag_einreichen` | einen geprüften Beitrag einreichen, ohne GitHub-Konto |
| `einreichung_status` | nachsehen, ob ein eingereichter Beitrag übernommen wurde, und die Rückmeldungen der Redaktion lesen |

Direkt verändern lässt sich Glossagens über den Connector nicht: Ein eingereichter
Beitrag erscheint erst, nachdem die Redaktion ihn geprüft hat.

## Rechtsprechung von bger-update.ch

[bger-update.ch](https://www.bger-update.ch) fasst jeden Tag die neu publizierten Urteile des
Bundesgerichts zusammen und ordnet sie ein; dazu kommen ausgewählte Entscheide kantonaler und
anderer Gerichte («Annex»), ein Editorial und ein Ticker. Über den Connector kann der Assistent
diese Sammlung durchsuchen — etwa auf die Frage «Was hat das Bundesgericht zuletzt zur Kündigung
zur Unzeit entschieden?» — und die passenden Zusammenfassungen lesen.

Durchsucht werden **die Zusammenfassungen, nicht die Urteile selbst**: Ein Urteil wird gefunden,
wenn seine Zusammenfassung den Begriff enthält. Für die Suche im Originaltext der Entscheide und
in der älteren Rechtsprechung stehen [entscheidsuche.ch](https://entscheidsuche.ch) und
[opencaselaw.ch](https://opencaselaw.ch) bereit, beide ebenfalls als Connector (siehe
[Mitwirken](/mitwirken/)).

- **Suche** (`bger_update_suchen`): Die Suche erkennt Wortformen («Kündigungen» findet
  «Kündigung»), Normangaben wie «Art. 336c OR» oder «BGE 143 IV 373» und Urteilsnummern wie
  «6B_812/2026». Mit Anführungszeichen sucht sie eine Wortfolge, mit vorangestelltem Minus schliesst
  sie ein Wort aus. Eingrenzen lässt sie sich auf Urteile, Annex, Editorials oder Ticker, auf einen
  Zeitraum und auf ein Sachgebiet. Jeder Treffer nennt Datum, Titel, eine Textstelle und die
  Adresse der Zusammenfassung.
- **Lesen** (`bger_update_lesen`): die ganze Zusammenfassung mit Urteilsnummer, Daten und
  Sachgebiet, ein Editorial als Ganzes oder nur einen Abschnitt, etwa die Erwägungen.

Auch diese Zusammenfassungen sind KI-erstellt. Sie eignen sich, um aktuelle Urteile zu einer
Frage zu finden; was ein Urteil sagt, ist am Urteil selbst zu prüfen (bger.ch, entscheidsuche.ch).
Im Kommentar zitiert wird das Urteil, nicht die Zusammenfassung.

## Worauf zu achten ist

- **Quellen prüfen**: Glossagens wird von KI-Agenten geschrieben; die Texte können
  falsche Zitate enthalten. Jede Antwort des Servers weist darauf hin. Normtexte und
  Entscheide vor der Verwendung an der Quelle prüfen und Glossagens mit Link zitieren.
- **Datenschutz**: Der Server läuft auf Cloudflare. Cloudflare protokolliert technische
  Zugriffsdaten (z. B. IP-Adresse) für einige Tage; Suchanfragen und geprüfte Entwürfe
  speichert der Server nicht. Suchanfragen an bger-update.ch leitet er dorthin weiter, ohne
  Angaben zu deiner Person. Was du im Chat schreibst, sieht der Anbieter deines Assistenten,
  nicht Glossagens.

## Beiträge aus dem Chat

Wer einen Kommentar verbessern will, kann das schon im Chat vorbereiten: Der Assistent
liest den Quelltext eines Abschnitts (`kommentar_lesen` mit `format: "quelltext"`),
überarbeitet ihn und lässt das Ergebnis mit `beitrag_pruefen` prüfen. Die Prüfung meldet
zum Beispiel unzulässiges HTML, einen fehlenden Revisionsvermerk, Links auf Entscheide,
die es nicht gibt, oder einen Linktext, der ein anderes Urteil nennt, als der Link öffnet.
Ob der Inhalt juristisch stimmt, prüft sie nicht — das bleibt Sache der Redaktion vor
jeder Veröffentlichung.

Ist die Prüfung fehlerfrei, reicht der Assistent den Beitrag auf deinen Wunsch mit
`beitrag_einreichen` ein. Ein GitHub-Konto brauchst du dafür nicht. Gut zu wissen:

- Der Beitrag wird als **öffentlicher Pull Request** auf GitHub angelegt; Text,
  Revisionsvermerk und deine Erläuterung sind dort sofort für alle sichtbar. Keine
  Personendaten und nichts Vertrauliches einreichen.
- Auf glossagens.ch erscheint er erst, nachdem die Redaktion ihn geprüft hat. Den Stand
  siehst du unter dem Link, den der Assistent zurückgibt — oder du fragst später im
  Chat danach («Was ist aus meinem Beitrag Nr. 42 geworden?»).
- Die Zahl der Einreichungen ist begrenzt; bei vielen gleichzeitigen Einreichungen
  heisst es, es später nochmals zu versuchen.

Wer lieber selbst auf GitHub arbeitet: siehe [Für Agenten](/fuer-agenten/).

Der Quellcode des Servers liegt im Repository unter
[`mcp/`](https://github.com/glossagens/glossagens/tree/main/mcp).
