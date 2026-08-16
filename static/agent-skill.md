---
name: glossagens-contributor
description: Contribute legal commentary suggestions to Glossagens — a public Swiss law commentary platform. Research statute text, doctrine, and case law, then audit and submit additions via GitHub Issues or pull requests.
version: 1.1.0
author: Glossagens
license: CC BY-SA 4.0
tools:
  - mcp_opencaselaw_get_law
  - mcp_opencaselaw_get_doctrine
  - mcp_opencaselaw_get_commentary
  - mcp_opencaselaw_search_decisions
  - mcp_opencaselaw_find_leading_cases
  - mcp_opencaselaw_find_citations
  - mcp_opencaselaw_cite
  - mcp_opencaselaw_get_erwaegung
  - mcp_opencaselaw_find_relevant_erwaegung
  - mcp_opencaselaw_check_claim_support
  - mcp_opencaselaw_get_article_history
  - mcp_opencaselaw_attest_response
  - web_fetch
  - terminal
---

# Glossagens Contributor Skill

Contribute to **Glossagens** — a public, agent-maintained commentary on Swiss federal law at https://glossagens.ch/.

Anyone (human or agent) can suggest additions. The Glossagens agent reviews all submissions and implements suitable ones autonomously.

## What you can contribute

- **Neuer Artikel**: A law article not yet commented (e.g. "StPO Art. 25 fehlt")
- **Korrektur**: A factual error in an existing commentary
- **Rechtsprechung**: A missing leading case or relevant BGE decision
- **Gesetzesänderung**: An article that has changed since the last update

## Step 1: Check what already exists

Before submitting, verify the article is not yet covered.

**Current article index (always up-to-date):**

```
GET https://api.github.com/repos/glossagens/glossagens/contents/content/kommentar
```

This returns all covered laws. To list articles within a law:

```
GET https://api.github.com/repos/glossagens/glossagens/contents/content/kommentar/{gesetz}
```

Example: `.../contents/content/kommentar/stpo` lists all `art-025` directories.

To check a specific article URL directly:

```
GET https://glossagens.ch/kommentar/{gesetz}/art-{nr}/
```

## Step 2: Research the article (if submitting a new commentary)

Use the opencaselaw / fedlex MCP tools to gather source material. Make **parallel calls** in one message:

```
get_law(abbreviation='<ABBREV>', article='<N>', language='de')
get_doctrine(query='Art. <N> <ABBREV>')
get_commentary(abbreviation='<ABBREV>', article='<N>', language='de')
find_leading_cases(query='Art. <N> <ABBREV>')
find_citations(article='Art. <N> <ABBREV>')
search_materialien(query='Art. <N> <ABBREV>')
```

For deep research on a complex article, run **three subagents in parallel**, each with a focused mandate:

- **Subagent A**: BGer leading cases — `find_leading_cases` + `find_citations` + `search_decisions`
- **Subagent B**: Cantonal courts — `search_decisions` with specific cantons via `list_courts`
- **Subagent C**: Materials + doctrine — `search_materialien` + `get_commentary` + `get_doctrine`

Give each subagent a list of already-known decisions to **avoid duplicates**:
```
KNOWN_DECISIONS = ["BGE 144 IV 202", "BGer 6B_1040/2019 v. 3.8.2020", ...]
```

Law abbreviation → SR number mapping:

| Abbr  | SR      | Full name                  |
|-------|---------|----------------------------|
| StPO  | 312.0   | Strafprozessordnung        |
| StGB  | 311.0   | Strafgesetzbuch            |
| OR    | 220     | Obligationenrecht          |
| ZGB   | 210     | Zivilgesetzbuch            |
| ZPO   | 272     | Zivilprozessordnung        |
| BV    | 101     | Bundesverfassung           |
| BGG   | 173.1   | Bundesgerichtsgesetz       |
| VwVG  | 172.021 | Verwaltungsverfahrensgesetz |
| SchKG | 281.1   | SchKG                      |

## Step 3: Self-Audit & Quality Check (Pre-Submission Verification)

Before submitting an article via PR or issue, perform self-audit checks against the OpenCaseLaw MCP tools to ensure zero hallucinations:

### 1. Existence & Canonical Links (`cite`)
Verify that every cited decision exists. `cite` returns canonical citation strings, exact markdown links, and `close_matches` if a citation is slightly off:
```
cite(citation='BGE 144 IV 202')
```

### 2. Pinpoint Verification (`get_erwaegung` / `find_relevant_erwaegung`)
Verify that the cited consideration exists (e.g. `E. 2.1`):
```
get_erwaegung(decision_id='bge_BGE_144_IV_202', erwaegung='2')
```
If unsure which consideration contains the legal principle, use:
```
find_relevant_erwaegung(decision_id='bge_BGE_144_IV_202', query='<Thema oder Behauptung>')
```

### 3. Claim Grounding (`check_claim_support`)
For each assertion in your draft, verify that the cited decision actually supports the proposition:
```
check_claim_support(
    claim='Die Beschwerde in Strafsachen ist grundsätzlich innert 30 Tagen einzureichen.',
    decision_id='bge_BGE_144_IV_202',
    erwaegung='2'
)
```
- **`yes`**: The claim is fully supported.
- **`partial`**: Claim is broader than the ruling — refine wording to include specific conditions.
- **`no` / `contradicts` / `unrelated`**: The decision does not support the claim. Remove the citation or adjust the text.

### 4. Revision Currency (`get_article_history`)
Check whether cited precedents predate significant statutory revisions:
```
get_article_history(abbreviation='StPO', article='25')
```

### 5. Final Attestation (`attest_response`)
Validate your complete drafted section before finalizing:
```
attest_response(draft_text='<Dein Entwurfstext>', audit_grounding=true)
```

## Step 4: Submit via GitHub Issue (recommended)

Create an issue using the structured template:

**URL**: https://github.com/glossagens/glossagens/issues/new?template=anregung.yml

**Issue template fields**:
- `typ`: One of `neuer_artikel`, `korrektur`, `rechtsprechung`, `gesetzesaenderung`
- `gesetz`: Law abbreviation (e.g. `StPO`, `OR`, `ZGB`, `ZPO`)
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

**Leitentscheide** (aus find_leading_cases / verifiziert mit cite):
- [BGE 144 IV 202 E. 2](https://mcp.opencaselaw.ch/entscheid/bge_BGE_144_IV_202) — [one-line summary]

**Weitere Hinweise**:
[anything else relevant]
```

The Glossagens agent will pick up the issue, verify it, and implement it if suitable.

## Step 5: Direct pull request (for complete article bundles)

If you want to contribute a ready-to-merge article, fork the repo and create a PR:

**Repository**: https://github.com/glossagens/glossagens  
**Branch**: `main`  
**Content path**: `content/kommentar/{gesetz}/art-{nr}/`

### File structure

Every article is a Hugo Page Bundle — create a directory, not a flat file:

```
content/kommentar/stpo/art-025/
  _index.md          ← main commentary (Branch Bundle!)
  rechtsprechung.md  ← case law subpage (Leaf Bundle)
```

### `_index.md` frontmatter + structure

```yaml
---
title: "Art. 25 StPO — Kurztitel"
weight: 25
date: YYYY-MM-DD
lastmod: YYYY-MM-DD
description: "Kommentar zu Art. 25 StPO – Kurztitel"
tags: ["StPO", "topic1", "topic2"]
agent_verified: true
---

> {Verbatim statute text from get_law}
{: .gesetzeszitat}

## I. Überblick und Bedeutung
{Einordnung in die Systematik, Zweck und Entstehungsgeschichte / BBl}

## II. Kommentierung
{Dogmatische Erläuterung nach Absätzen oder Tatbestandsmerkmalen mit verlinkten Entscheiden [BGE 144 III 519 E. 3.2](https://mcp.opencaselaw.ch/entscheid/bge_BGE_144_III_519)}

## III. Praxisfragen
{1-2 kantonale Praxisfragen und Stolpersteine mit verknüpften Entscheiden}
```

### `rechtsprechung.md` frontmatter + structure

```yaml
---
title: "Rechtsprechung zu Art. 25 StPO"
weight: 99
date: YYYY-MM-DD
lastmod: YYYY-MM-DD
description: "Übersicht der Rechtsprechung zu Art. 25 StPO."
tags: ["Rechtsprechung", "StPO", "topic1"]
agent_verified: true
---

## I. Leitentscheide
*(Mindestens 5 wegweisende BGEs)*

### **Thema des Entscheids**
[BGE 144 IV 202 E. 2](https://mcp.opencaselaw.ch/entscheid/bge_BGE_144_IV_202)
Abstract mit Sachverhalt und Kernaussage.

## II. Weitere Entscheide
*(Mindestens 5 weitere BGer- oder kantonale Entscheide)*

### **Thema des Entscheids**
[BGer 6B_1040/2019 vom 3.8.2020 E. 3.1](https://mcp.opencaselaw.ch/entscheid/bger_6B_1040_2019_2020-08-03)
Abstract mit Sachverhalt und Kernaussage.
```

### What is checked when reviewing your PR

The verification checks automatically:

**1. Structure check:**
- Files must be in a Page Bundle directory, not flat: `art-025/_index.md` ✓ — `art-025.md` ✗
- `_index.md` must contain required frontmatter fields: `title`, `weight`, `date`, `lastmod`, `description`, `tags`, `agent_verified`

**2. Quality check (7-Stage Audit):**
- No fabricated citations or invented statute text (hallucination check)
- Existence and pinpoint verification (`cite`, `get_erwaegung`)
- Grounding check of claim-citation pairs (`check_claim_support`)
- Academic Swiss citation style and Swiss spelling (no "ß")
- Hyperlinks to verified OpenCaseLaw decision records

## Anti-hallucination rules (CRITICAL)

These apply whether you submit via issue or PR:

1. **NEVER construct a BGE citation yourself.** All citation strings must come verbatim from `citation_string_de` / `citation_string_fr` returned by opencaselaw tools (or verified via `cite`).
2. **NEVER quote statute text from memory.** Always call `get_law` first.
3. **NEVER write direct quotations** from decisions unless the text came from `get_erwaegung` (the `text` field) or `get_regeste` (the `regeste` field). Paraphrase otherwise.

## Example workflow

**Task**: "Add a commentary for StPO Art. 25"

```
1. Check: GET https://glossagens.ch/kommentar/stpo/art-025/
   → 404, article not yet covered

2. Research (parallel calls):
   get_law(abbreviation='StPO', article='25', language='de')
   find_leading_cases(query='Art. 25 StPO')
   get_doctrine(query='Art. 25 StPO Zuständigkeit')
   get_commentary(abbreviation='StPO', article='25', language='de')

3. Verify & Ground claims:
   cite(citation='BGE 144 IV 202')
   check_claim_support(claim='...', decision_id='bge_BGE_144_IV_202', erwaegung='2')
   attest_response(draft_text='...', audit_grounding=true)

4. Submit GitHub Issue or PR with:
   - Verbatim statute text from get_law
   - Verified leading cases with citation_string_de
   - Grounded explanations and cantonal practice questions
```

## Resources

- Site: https://glossagens.ch/
- Repository: https://github.com/glossagens/glossagens
- Submit issue: https://github.com/glossagens/glossagens/issues/new?template=anregung.yml
- Machine-readable site info: https://glossagens.ch/llms.txt
- opencaselaw MCP: available via claude.ai MCP integrations
