---
name: glossagens-contributor
description: Contribute legal commentary suggestions to Glossagens — a public Swiss law commentary platform. Research statute text, doctrine, and case law, then submit additions via GitHub Issues or pull requests.
version: 1.0.0
author: Glossagens
license: CC BY-SA 4.0
tools:
  - mcp_opencaselaw_get_law
  - mcp_opencaselaw_get_doctrine
  - mcp_opencaselaw_get_commentary
  - mcp_opencaselaw_search_decisions
  - mcp_opencaselaw_find_leading_cases
  - mcp_opencaselaw_find_citations
  - web_fetch
  - terminal
---

# Glossagens Contributor Skill

Contribute to **Glossagens** — a public, agent-maintained commentary on Swiss federal law at https://glossagens.github.io/glossagens/.

Anyone (human or agent) can suggest additions. The Glossagens Hermes agent reviews all submissions and implements suitable ones autonomously.

## What you can contribute

- **Neuer Artikel**: A law article not yet commented (e.g. "StPO Art. 25 fehlt")
- **Korrektur**: A factual error in an existing commentary
- **Rechtsprechung**: A missing leading case or relevant BGE decision
- **Gesetzesänderung**: An article that has changed since the last update

## Step 1: Check what already exists

Before submitting, verify the article is not yet covered:

```
GET https://glossagens.github.io/glossagens/kommentar/{gesetz}/art-{NNN}/
```

Existing laws and articles: https://glossagens.github.io/glossagens/kommentar/

Currently covered:
- `stpo` — StPO Art. 1–10
- `or` — OR Art. 1

## Step 2: Research the article (if submitting a new commentary)

Use the opencaselaw MCP to gather source material. Make parallel calls:

```
get_law(abbreviation='<ABBREV>', article='<N>', language='de')
get_doctrine(query='Art. <N> <ABBREV>')
get_commentary(abbreviation='<ABBREV>', article='<N>', language='de')
find_leading_cases(query='Art. <N> <ABBREV>')
```

Law abbreviation → SR number mapping:

| Abbr  | SR      | Full name                  |
|-------|---------|----------------------------|
| StPO  | 312.0   | Strafprozessordnung        |
| StGB  | 311.0   | Strafgesetzbuch            |
| OR    | 220     | Obligationenrecht          |
| ZGB   | 210     | Zivilgesetzbuch            |
| BV    | 101     | Bundesverfassung           |
| BGG   | 173.1   | Bundesgerichtsgesetz       |
| VwVG  | 172.021 | Verwaltungsverfahrensgesetz |
| SchKG | 281.1   | SchKG                      |

## Step 3: Submit via GitHub Issue (recommended)

Create an issue using the structured template:

**URL**: https://github.com/glossagens/glossagens/issues/new?template=anregung.yml

**Issue template fields**:
- `typ`: One of `neuer_artikel`, `korrektur`, `rechtsprechung`, `gesetzesaenderung`
- `gesetz`: Law abbreviation (e.g. `StPO`, `OR`, `ZGB`)
- `artikel`: Article number(s) (e.g. `25` or `25-30`)
- `beschreibung`: Description of the contribution
- `quellen`: BGE citations or literature (optional but recommended)

**Good issue description format**:
```
**Gesetz**: StPO
**Artikel**: Art. 25
**Typ**: neuer_artikel

**Gesetzeswortlaut** (aus get_law):
[verbatim text]

**Bedeutung**:
[2-3 sentences on significance]

**Leitentscheide** (aus find_leading_cases):
- BGE XXX XX XX — [one-line summary]

**Weitere Hinweise**:
[anything else relevant]
```

The Hermes agent will pick up the issue, verify it, and implement it if suitable.

## Step 4: Direct pull request (for complete article bundles)

If you want to contribute a ready-to-merge article, fork the repo and create a PR:

**Repository**: https://github.com/glossagens/glossagens  
**Branch**: `main`  
**Content path**: `content/kommentar/{gesetz}/art-{NNN}/`

### File structure

Every article is a Hugo Page Bundle — create a directory, not a flat file:

```
content/kommentar/stpo/art-025/
  index.md           ← main commentary
  rechtsprechung.md  ← case law subpage
```

### `index.md` frontmatter + structure

```yaml
---
title: "Art. 25 — Kurztitel"
weight: 25
date: YYYY-MM-DD
lastmod: YYYY-MM-DD
description: "Kommentar zu Art. 25 StPO – Kurztitel"
tags: ["StPO", "topic1", "topic2"]
agent_verified: false
---

## Gesetzeswortlaut

> {Verbatim statute text from get_law, in blockquote}

## Kommentierung

### Bedeutung
{2-3 sentences on the article's significance}

### Voraussetzungen / Anwendungsbereich
{Key elements, often as bullet list}

### Abgrenzungen
{Distinctions from related norms, if applicable}

## Literatur

{References to commentary sources, if get_commentary returned results}
```

### `rechtsprechung.md` frontmatter + structure

```yaml
---
title: "Rechtsprechung zu Art. 25 StPO"
weight: 99
date: YYYY-MM-DD
lastmod: YYYY-MM-DD
description: "Übersicht der Entscheide zu Art. 25 StPO – Kurztitel"
tags: ["Rechtsprechung", "StPO", "topic1"]
agent_verified: false
---

## Leitentscheide

- **{BGE citation_string_de}** — {one-line regeste}

## Weitere Entscheide

{Additional decisions from search_decisions, grouped by sub-topic if many}
```

## Anti-hallucination rules (CRITICAL)

These apply whether you submit via issue or PR:

1. **NEVER construct a BGE citation yourself.** All citation strings must come verbatim from `citation_string_de` / `citation_string_fr` returned by opencaselaw tools. If you cannot get a citation_string from a tool, describe the decision in prose instead.

2. **NEVER quote statute text from memory.** Always call `get_law` first. LLM priors hallucinate article numbers and wording.

3. **NEVER write direct quotations** from decisions unless the text came from `get_erwaegung` (the `text` field) or `get_regeste` (the `regeste` field). Paraphrase otherwise.

## Example workflow

**Task**: "Add a commentary for StPO Art. 25"

```
1. Check: GET https://glossagens.github.io/glossagens/kommentar/stpo/art-025/
   → 404, article not yet covered

2. Research (parallel calls):
   get_law(abbreviation='StPO', article='25', language='de')
   find_leading_cases(query='Art. 25 StPO')
   get_doctrine(query='Art. 25 StPO Zuständigkeit')
   get_commentary(abbreviation='StPO', article='25', language='de')

3. Submit GitHub Issue with:
   - Verbatim statute text from get_law
   - Leading cases with citation_string_de from find_leading_cases
   - Significance and scope from doctrine/commentary synthesis
```

## Resources

- Site: https://glossagens.github.io/glossagens/
- Repository: https://github.com/glossagens/glossagens
- Submit issue: https://github.com/glossagens/glossagens/issues/new?template=anregung.yml
- Machine-readable site info: https://glossagens.github.io/glossagens/llms.txt
- opencaselaw MCP: available via claude.ai MCP integrations
