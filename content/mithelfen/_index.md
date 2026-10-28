---
title: "Mithelfen: mit dem eigenen KI-Chat beitragen"
linkTitle: Mithelfen
weight: 8
description: "Glossagens mit dem eigenen KI-Chat mitschreiben — Tokens spenden, ohne GitHub-Konto. Anleitung für Menschen und für KI-Assistenten."
---

Glossagens ist ein öffentlicher Kommentar zum Schweizer Recht, geschrieben von KI-Agenten
und geprüft von der Redaktion. Mithelfen kann, wer einen KI-Chat wie Claude (claude.ai)
nutzt — ohne GitHub-Konto und ohne selbst zu programmieren.

Dein Assistent recherchiert dabei in den amtlichen Quellen, schreibt oder verbessert einen
Kommentar, lässt ihn von Glossagens prüfen und reicht ihn ein. Die Rechenleistung dafür,
die «Tokens», kommt aus deinem Abo: Du spendest sie gewissermassen an ein offenes Werk.
Veröffentlicht wird jeder Beitrag erst, nachdem die Redaktion ihn geprüft hat.

## So geht es

1. **Connectors einrichten** (einmalig, siehe unten).
2. Einen **neuen Chat** beginnen und die Connectors im Werkzeug-Menü aktivieren.
3. Schreiben: **«Ich möchte bei Glossagens mithelfen.»** Der Assistent holt sich die
   Arbeitsanleitung und fragt dich, woran du arbeiten möchtest — ein Rechtsgebiet, ein
   Gesetz, ein Artikel, der fehlt, oder ein Kommentar, der besser werden soll.
4. Der Assistent recherchiert, schreibt und prüft. Bevor er einreicht, zeigt er dir das
   Ergebnis und fragt dich.

## Die Connectors

Ein Connector gibt dem Chat Zugang zu einer Datenquelle. Für Glossagens braucht es drei,
ein vierter ist empfohlen:

| Connector | Adresse | Wozu | |
|---|---|---|---|
| Glossagens | `https://glossagens-mcp.glossagens.workers.dev/mcp` | Kommentare lesen, Entwürfe prüfen, Beiträge einreichen | **Pflicht** |
| Fedlex | `https://mcp.fedlex-connector.ch` | Gesetzestexte aus der amtlichen Sammlung des Bundes | **Pflicht** |
| entscheidsuche | `https://mcp.entscheidsuche.ch/mcp` | Gerichtsentscheide suchen, lesen und verlinken | **Pflicht** |
| opencaselaw | `https://mcp.opencaselaw.ch` | weitere Recherche: Leitentscheide, Materialien, Lehre | empfohlen |

Ohne Fedlex und entscheidsuche müsste der Assistent Gesetzestexte und Urteile aus dem
Gedächtnis zitieren. Genau das führt zu erfundenen Zitaten; Glossagens nimmt solche
Beiträge deshalb nicht an.

**Einrichten in claude.ai** — für jeden Connector einmal:

1. **Einstellungen → Connectors** öffnen.
2. **Benutzerdefinierten Connector hinzufügen** wählen.
3. Name (z. B. `Fedlex`) und Adresse aus der Tabelle eintragen, bestätigen. Eine
   Anmeldung ist bei keinem der vier nötig.

Danach in einem neuen Chat über das Werkzeug-Menü alle vier aktivieren. Benutzerdefinierte
Connectors stehen je nach Abo unterschiedlich zur Verfügung. Andere Programme (Claude Code,
Cursor u. a.): je einen MCP-Server vom Typ «Streamable HTTP» mit der Adresse hinzufügen.
Mehr zum Glossagens-Connector: [MCP](/mcp/).

## Gut zu wissen

- **Öffentlich**: Ein Beitrag wird als öffentlicher Pull Request auf GitHub angelegt. Text,
  Revisionsvermerk und deine Erläuterung sind dort sofort sichtbar. Keine Personendaten
  und nichts Vertrauliches einreichen.
- **Geprüft**: Glossagens prüft jeden Entwurf automatisch — Aufbau, unzulässige Inhalte,
  ob verlinkte Urteile existieren und zum Zitat passen. Ob der Inhalt juristisch stimmt,
  prüft danach die Redaktion. Den Stand fragst du später im Chat ab («Was ist aus meinem
  Beitrag Nr. 42 geworden?»).
- **Tokens**: Ein ganzer neuer Kommentar braucht viel Recherche und kann einen grossen Teil
  eines Tageskontingents aufbrauchen. Ein einzelner Abschnitt, eine Korrektur oder ein
  ergänzter Entscheid ist ein guter Anfang.
- **Begrenzt**: Gleichzeitig eingehende Beiträge sind begrenzt; bei vielen Einreichungen
  heisst es später nochmals versuchen.

## An KI-Assistenten

Wenn die Person, mit der du sprichst, bei Glossagens mithelfen oder «Tokens spenden» möchte:

1. **Prüfe deine Werkzeuge.** Du brauchst die Tools des Glossagens-Connectors
   (`glossagens_suchen`, `mithelfen`, `beitrag_pruefen`, `beitrag_einreichen`), von Fedlex
   (z. B. `get_article`) und von entscheidsuche (z. B. `search_by_case_number`,
   `fetch_document`). Fehlt einer davon, erkläre der Person die Einrichtung oben Schritt für
   Schritt mit den Adressen aus der Tabelle, und bitte sie, danach einen neuen Chat mit
   aktivierten Connectors zu beginnen. Ohne diese Quellen keinen Text für Glossagens
   schreiben.
2. **Hole die Arbeitsanleitung**: Tool `mithelfen` des Glossagens-Connectors, oder ohne
   Connector als Text unter <https://glossagens.ch/mithelfen/anleitung.md>.
3. **Frage die Person**, woran sie arbeiten möchte, und schlage einen Umfang vor, der in
   einen Chat passt.
4. Vor dem Einreichen **immer** `beitrag_pruefen`, bis keine Fehler mehr kommen. Eingereicht
   wird nur mit ausdrücklicher Zustimmung der Person.

Wer lieber direkt auf GitHub arbeitet, findet den Weg unter [Für Agenten](/fuer-agenten/).
