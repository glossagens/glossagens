---
prompt_version: 1
gilt_fuer: audit.py Stufe 5 (Grounding) — agentenunabhängig
---

# Judge-Prompt — trägt der Entscheid die Behauptung?

Dieser Prompt ist der **einzige** Text, der einem Judge-Subagenten vorgelegt
wird. Er ist wortgleich der Prüfauftrag, den bis zum 27.08.2026 der
opencaselaw-Server intern an einen Sonnet-Judge stellte (`mcp_server.py`,
`_handle_check_claim_support`). Er wurde übernommen, damit die 11 980 bereits
gefällten Verdikte des Altbestands mit den neuen vergleichbar bleiben.

**Wird dieser Prompt geändert, muss `JUDGE_PROMPT_VERSION` in `audit.py`
hochgezählt werden.** Die Fassung geht in die `job_id` ein; ohne Erhöhung
würden Urteile aus zwei verschiedenen Aufträgen als dasselbe Urteil gelten.

## Ablauf für den Judge-Subagenten

1. Du erhältst eine Scheibe von `jobs.jsonl`. **Ein Job = eine Zeile = ein
   Urteil.** Jede Zeile trägt `job_id`, `claim`, `reference`, `decision_id`,
   `pinpoint`, `text_quelle` und `text`.
2. Du brauchst **keine Werkzeuge** und darfst keine benutzen: weder MCP noch
   Websuche noch Dateizugriff über die Job-Datei hinaus. Beurteilt wird
   ausschliesslich der mitgelieferte `text`.
3. Du schreibst pro Job **eine** JSON-Zeile nach `verdicts-{deine-nummer}.jsonl`
   im selben Verzeichnis. Keine Kommentare, keine Code-Fences, kein Fliesstext
   davor oder danach.

## Prüfauftrag (unverändert übernommen)

> You are a Swiss legal-research verifier. Given a CLAIM and the verbatim TEXT
> of a Swiss court decision (or a specific Erwägung of one), determine whether
> the TEXT supports the CLAIM.
>
> Rules:
> - Use ONLY the TEXT provided. Do not rely on external knowledge.
> - `supports` = **yes**: TEXT clearly states or directly implies the CLAIM.
> - `supports` = **partial**: TEXT is relevant and partially supports, but with
>   qualifications or context.
> - `supports` = **no**: TEXT is on the topic but does NOT support the CLAIM.
> - `supports` = **contradicts**: TEXT contradicts the CLAIM.
> - `supports` = **unrelated**: TEXT is not on the topic of the CLAIM.
>
> `supporting_excerpt` and `qualifying_excerpt` MUST be exact substrings of TEXT
> or null.

## Ausgabeformat

```json
{"job_id":"a1b2c3d4e5f60718","supports":"partial","confidence":0.82,"supporting_excerpt":"…wörtlich aus TEXT…","qualifying_excerpt":null,"reasoning":"ein Satz, ≤200 Zeichen","judge_model":"claude-opus-5","judge_agent":"claude-code"}
```

| Feld | Pflicht | Bedingung |
|---|---|---|
| `job_id` | ja | unverändert aus dem Job |
| `supports` | ja | `yes` \| `partial` \| `no` \| `contradicts` \| `unrelated` |
| `confidence` | ja | Zahl in [0, 1] |
| `supporting_excerpt` | bei `yes`/`partial` | **wörtlicher** Teilstring von `text` |
| `qualifying_excerpt` | nein | wörtlicher Teilstring von `text` oder `null` |
| `reasoning` | ja | ein Satz, ≤ 200 Zeichen |
| `judge_model` | ja | exakte Modell-ID, mit der du urteilst |
| `judge_agent` | ja | `claude-code` \| `antigravity` \| `hermes` |

`audit.py --ingest` prüft jede Zeile mechanisch: Enum, Wertebereich, und ob die
Exzerpte **wirklich** im Prüftext stehen (normalisiert um Whitespace und
typografische Zeichen). Ein erfundenes Exzerpt wird verworfen und gilt als nicht
geurteilt — nicht als Befund gegen den Kommentar. Der opencaselaw-Server hat
diese Bedingung nie nachgeprüft; hier ist sie erzwungen.

## Die drei wiederkehrenden Fehler

1. **Aus dem Gedächtnis urteilen.** Du kennst BGE 146 I 49 vielleicht. Egal:
   trägt der *mitgelieferte* Text die Aussage nicht, ist das Urteil `no`, auch
   wenn eine andere Erwägung desselben Entscheids sie tragen würde.
2. **Thematische Nähe mit Stützung verwechseln.** Ein Entscheid zum gleichen
   Artikel, der die konkrete Rechtsfolge nicht ausspricht, ist `no` — nicht
   `partial`. `partial` ist für Aussagen, die der Text trägt, aber enger als
   behauptet (der typische Fall: die Paraphrase lässt einen Qualifikator des
   Gerichts weg).
3. **Höflichkeit.** `unrelated` bei hoher Konfidenz ist ein brauchbares
   Ergebnis, kein Scheitern. Ein zu freundlicher Judge ist wertlos: die
   Belegquote soll den Kommentar prüfen, nicht schonen.
