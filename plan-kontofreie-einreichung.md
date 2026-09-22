# Plan: kontofreie Einreichung

**Stand 22.09.2026 — Entwurf, nicht in Betrieb.** Der Code liegt vollständig auf dem
Branch `feature/kontofreie-einreichung` (ein Commit, `0a4bfaa`, nicht gepusht). Auf
`main` ist nichts davon vorhanden. Diese Notiz hält fest, worum es ging, was entschieden
wurde und was zum Einschalten fehlt.

```sh
git switch feature/kontofreie-einreichung     # anschauen
git branch -D feature/kontofreie-einreichung  # verwerfen
```

## Das Problem

Wer heute beitragen will, braucht ein GitHub-Konto. Für einen Pull Request ist das
unvermeidlich: Jeder Push trägt eine authentifizierte Identität, anonyme PRs gibt es
nicht. Das trifft nicht nur Menschen, sondern vor allem **fremde Agenten** — und die
sind der eigentliche Adressat: Sie sollen `/agent-skill.md` lesen, den Kommentar **mit
ihrer eigenen Rechenleistung** verfassen und das fertige Ergebnis abliefern. Der
Schreibaufwand läge damit bei ihnen, hier bliebe die Verifikation.

Die Hürde lässt sich nur verschieben, nicht abschaffen: Irgendjemand muss den
GitHub-Schlüssel halten. Die Idee ist, dass das eine kleine Vermittlerstelle tut, die
vor GitHub steht, statt jeder Beitragende einzeln.

## Die Entscheidungen

| Frage | Entscheid | Warum |
|---|---|---|
| Wo läuft die Gegenstelle? | Cloudflare Worker | GitHub Pages ist statisch und kann nichts entgegennehmen. Der Hetzner-Dienst ist ein Nous-Hermes-Agent und nicht dafür gedacht, öffentlichen Traffic zu bedienen. Der Worker läuft auch ohne Cloudflare-DNS auf einer `*.workers.dev`-Adresse, an glossagens.ch ändert sich nichts. |
| Issue oder Pull Request? | beides, zwei Pfade | `POST /einreichung` für blosse Anregungen (→ Issue, mündet in die bestehende Queue), `POST /beitrag` für fertige Page Bundles (→ ein Commit, Branch, Pull Request). |
| Wer merged? | niemand automatisch | Der Worker kennt keinen Merge-Aufruf. Er legt Branch und PR an, `pr-build.yml` baut, entschieden wird redaktionell. |
| Darf ein Beitrag `agent_verified: true` setzen? | **nein**, Abweisung mit 422 | Die Selbstauskunft eines fremden Modells ist nicht nachprüfbar; Antigravity und Hermes trugen `mcp_verified: true` über fabrizierten Belegen. Das Siegel setzt die Redaktion nach dem Audit. |
| Was prüft der Worker? | nur die Struktur | Inhaltliche Prüfung bleibt beim Audit. Der PR-Text sagt das ausdrücklich, damit ein grüner Build nicht als Qualitätsnachweis gelesen wird. |

## Was auf dem Branch liegt

| Datei | Zweck |
|---|---|
| `worker/src/index.js` | die Vermittlerstelle, beide Pfade |
| `worker/test/worker.test.mjs` | 34 Prüfungen, ohne Netz und ohne wrangler: `node worker/test/worker.test.mjs` |
| `worker/wrangler.toml`, `worker/README.md` | Konfiguration und Einrichtung |
| `layouts/_shortcodes/einreichungsformular.html` | das Webformular, eingebunden in `content/einreichung/_index.md` |
| `.github/workflows/pr-build.yml` | baut jeden PR mit der Version aus `.hugo-version` |
| `hugo.toml` | `[params.einreichung]` — leerer `endpoint` = Formular aus |
| `static/llms.txt`, `content/fuer-agenten/`, `static/agent-skill.md` | der Weg dort beschrieben, wo fremde Agenten nachschauen |
| `CLAUDE.md` | Kanal C dokumentiert; `verify-pr.yml` im Dateibaum durch `pr-build.yml` ersetzt (die Datei existierte nie) |

## Die Schnittstelle

```http
POST {basis}/beitrag
Content-Type: application/json

{
  "gesetz": "stpo",
  "artikel": "art-025",
  "urheber": "Agentenname / Modell-ID",
  "dateien": { "_index.md": "…", "rechtsprechung.md": "…" }
}
→ { "ok": true, "pr_url": "…", "pr_number": 42, "branch": "beitrag-stpo-art-025-…" }
```

Abweisung mit `422` und einer Liste konkreter Befunde unter `befunde`; ein abgewiesener
Versuch verbraucht kein Kontingent, damit ein Agent nachbessern kann. Geprüft werden:
Page-Bundle-Pfad und die vier erlaubten Dateinamen, dreistellig genullte Artikelnummer,
bei Neuanlage `_index.md` **und** `rechtsprechung.md`, die acht Pflichtfelder, der
Revisions-Vermerk, `agent_verified: false`, kein `ß`, keine Tabellen in
```` ```markdown ````-Blöcken. Grenzen: 150 000 Zeichen je Datei, 400 000 je Bundle,
2 Beiträge pro Stunde und 5 pro Tag; Anregungen 5/h und 10/Tag, gesamt 100/Tag.

Beide Pfade beschreiben sich per `GET` selbst, ein Agent findet das Schema also ohne
Dokumentation.

## Zum Einschalten fehlt

1. **`main` schützen** — Settings → Branches → Add rule für `main`:
   *Require a pull request before merging*. Das ist die eigentliche Sicherung, nicht
   der Token-Scope: Für `/beitrag` braucht der Schlüssel zwangsläufig Schreibrechte,
   und `deploy.yml` veröffentlicht alles auf `main` sofort. **Vorher nicht deployen.**
2. **Token erzeugen** — fine-grained PAT, nur dieses Repo, Permissions: Issues
   (read/write), Contents (read/write), Pull requests (read/write). Idealerweise unter
   einem eigenen Bot-Konto, damit die maschinelle Herkunft sichtbar ist.
3. **Turnstile-Widget anlegen** (Cloudflare → Turnstile, Domain glossagens.ch) — ergibt
   Site Key (öffentlich, in `hugo.toml`) und Secret Key (Worker-Secret).
4. **Deployen** — `cd worker && npx wrangler kv namespace create RATELIMIT`, die id in
   `wrangler.toml` eintragen, `wrangler secret put GITHUB_TOKEN | TURNSTILE_SECRET |
   IP_SALT`, dann `npx wrangler deploy`.
5. **URL eintragen** — an zwei Stellen: `params.einreichung.endpoint` in `hugo.toml`
   (schaltet das Formular) und `static/llms.txt`, Abschnitt „Weg 0", wo der Platzhalter
   `TODO-NACH-WORKER-DEPLOY-EINTRAGEN` steht (dort suchen Agenten).
6. **Testen** — `curl` gegen `GET /beitrag` und `GET /einreichung`, dann eine
   Testeinreichung; das erzeugte Issue bzw. den PR wieder schliessen.

Ausführlich in `worker/README.md` auf dem Branch.

## Offene Punkte

- **Branch-Namen**: Der Worker benennt `beitrag-stgb-art-011-<zeit>`, im Repo besteht
  schon das Muster `beitrag/stgb-art-011`. Angleichung wäre eine Zeile in
  `pullRequestAnlegen`.
- **Kosten/Grenzen**: Free Tier reicht (100 000 Anfragen/Tag, KV 1 000 Schreibvorgänge/Tag).
  Offen ist die CPU-Grenze von 10 ms pro Aufruf — das Base64-Kodieren eines grossen
  Bundles könnte sie streifen. Falls ja, hilft der 5-$-Plan (30 s) oder eine kleinere
  Obergrenze je Datei.
- **Menge**: Ob 5 Beiträge pro Tag und Absender zu viel oder zu wenig sind, zeigt erst
  der Betrieb. Wenn die Prüfung fremder Beiträge mehr Zeit kostet, als das Schreiben
  spart, ist die Zahl zu hoch.
- **Die eigentliche Frage bleibt offen**: Ob Beiträge fremder Agenten das Niveau
  halten, entscheidet nicht diese Mechanik, sondern das Audit dahinter. Der Worker
  senkt nur die Hürde — er erhöht damit auch die Menge dessen, was geprüft werden muss.
