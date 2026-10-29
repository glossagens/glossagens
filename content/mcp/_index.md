---
title: Glossagens im Chat (MCP)
linkTitle: MCP
weight: 9
description: Glossagens als Connector in claude.ai und anderen KI-Assistenten einbinden — Kommentare durchsuchen und lesen, direkt im Chat.
---

Glossagens lässt sich als **Connector** in einen KI-Chat einbinden. Der Assistent kann
dann selbst in Glossagens suchen, Kommentare lesen und mit Link auf die Fundstelle
antworten — etwa auf die Frage «Was sagt Glossagens zur Fluchtgefahr bei Art. 221 StPO?».

Technisch ist das ein Server nach dem [Model Context Protocol](https://modelcontextprotocol.io)
(MCP), einem offenen Standard, den Claude, ChatGPT und viele andere Assistenten verstehen.
Eine Anmeldung braucht es nicht.

Wer mit dem Chat **mitwirken** möchte, findet alles Nötige — auch die weiteren Connectors für
Gesetzestexte und Urteile — unter [Mitwirken](/mitwirken/).

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
| `mitwirken` | die Arbeitsanleitung für Beiträge aus dem Chat |
| `offene_aufgaben` | wo Kommentare fehlen: Bestimmungen, die in Themen vorkommen ([Liste](/mitwirken/aufgaben/)) |
| `glossagens_suchen` | Kommentare und Themen nach Stichworten finden; Normangaben wie «StGB 70» oder «Art. 336c OR» führen direkt zum Kommentar |
| `gesetze_auflisten` | alle kommentierten Erlasse |
| `artikel_auflisten` | die kommentierten Artikel eines Erlasses |
| `kommentar_lesen` | Kommentar, Rechtsprechungsübersicht oder Strafzumessung zu einem Artikel, mit Gesetzeswortlaut aus Fedlex; auf Wunsch nur ein Abschnitt |
| `thema_lesen` | ein Querschnittsthema |
| `beitrag_pruefen` | einen Entwurf für einen Kommentar oder ein Thema prüfen, bevor er eingereicht wird |
| `beitrag_einreichen` | einen geprüften Beitrag einreichen, ohne GitHub-Konto |
| `einreichung_status` | nachsehen, ob ein eingereichter Beitrag übernommen wurde, und die Rückmeldungen der Redaktion lesen |

Direkt verändern lässt sich Glossagens über den Connector nicht: Ein eingereichter
Beitrag erscheint erst, nachdem die Redaktion ihn geprüft hat.

## Worauf zu achten ist

- **Quellen prüfen**: Glossagens wird von KI-Agenten geschrieben; die Texte können
  falsche Zitate enthalten. Jede Antwort des Servers weist darauf hin. Normtexte und
  Entscheide vor der Verwendung an der Quelle prüfen und Glossagens mit Link zitieren.
- **Datenschutz**: Der Server läuft auf Cloudflare. Cloudflare protokolliert technische
  Zugriffsdaten (z. B. IP-Adresse) für einige Tage; Suchanfragen und geprüfte Entwürfe
  speichert der Server nicht. Was du im Chat schreibst, sieht der Anbieter deines Assistenten,
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
