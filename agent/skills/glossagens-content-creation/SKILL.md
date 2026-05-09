---
name: glossagens-content-creation
description: Create legal commentary articles for the Glossagens Hugo site — fetch statute text, doctrine, and leading cases, then write Hugo markdown with proper frontmatter.
version: 1.0.0
author: Hermes Agent
tools:
  - mcp_opencaselaw_get_law
  - mcp_opencaselaw_get_doctrine
  - mcp_opencaselaw_get_commentary
  - mcp_opencaselaw_search_decisions
  - mcp_opencaselaw_find_leading_cases
  - write_file
  - terminal
---

# Glossagens Content Creation

Create legal commentary articles for the Glossagens Hugo site at `/opt/glossagens/`.

## Workflow

### 1. Create the law index page

Each law gets its own directory under `content/kommentar/` and an `_index.md`:
- German abbreviation as directory name, lowercase: `stpo/`, `or/`, `zgb/`, `stgb/`
- `_index.md` with frontmatter: title, linkTitle, weight, description
- Brief introduction to the law (3-5 sentences: purpose, scope, structure)

### 2. Fetch statute text + doctrine for each article

For each article, make **parallel calls**:
- `get_law(abbreviation='<LAW>', article='<N>', language='de')` — verbatim statute text
- `get_doctrine(query='Art. <N> <ABBREV>')` — leading cases + commentary
- `get_commentary(abbreviation='<ABBREV>', article='<N>', language='de')` — OnlineKommentar commentary (if available)

### 3. Write article markdown

File naming: `art-001.md`, `art-002.md`, etc. (zero-padded to 3 digits)

**Frontmatter template:**
```yaml
---
title: "Art. {N} — {Kurztitel}"
weight: {N}
date: {YYYY-MM-DD}
lastmod: {YYYY-MM-DD}
description: "Kommentar zu Art. {N} {ABBREV} – {Kurztitel}"
tags: ["{ABBREV}", "{topic1}", "{topic2}"]
agent_verified: true
---
```

**Content structure (German):**
```markdown
## Gesetzeswortlaut

> {Verbatim statute text from get_law, in blockquote}

## Kommentierung

### Bedeutung
{2-3 sentences on the article's significance}

### Voraussetzungen / Anwendungsbereich
{Key elements, often as bullet list}

### Abgrenzungen
{Distinctions from related norms, if applicable}

{For complex norms: a summary table with columns like Voraussetzung | Erläuterung}

## Leitentscheide

{For each leading case from get_doctrine:}
- **{BGE citation}** — {one-line regeste/rule summary}. {Link if available}

## Literatur

{References to commentary sources, if get_commentary returned results}
```

### 4. Verify Hugo build

```bash
cd /opt/glossagens && hugo --minify 2>&1 | tail -5
```

Fix any build errors before committing.

### 5. Commit and push to GitHub

```bash
cd /opt/glossagens
git add content/kommentar/<law>/
git commit -m "feat: <ABBREV>-Kommentar Art. X–Y hinzugefügt"
git push origin main
```

**Git auth setup** (if not yet configured):
```bash
cd /opt/glossagens
git config user.email "agent@glossagens.ch"
git config user.name "Glossagens Agent"
# Use gh CLI for auth (token stored in .env):
source .env && echo "$GITHUB_TOKEN" | gh auth login --with-token
git remote set-url origin "https://$(gh auth token)@github.com/glossagens/glossagens.git"
```

**If push is rejected** (remote has new commits):
```bash
git stash
git pull --rebase origin main
git stash pop
git push origin main
```

## Law abbreviation → SR number mapping

| Abbr | SR | Directory | Full name |
|------|-----|-----------|------------|
| StPO | 312.0 | `stpo` | Strafprozessordnung |
| StGB | 311.0 | `stgb` | Strafgesetzbuch |
| OR | 220 | `or` | Obligationenrecht |
| ZGB | 210 | `zgb` | Zivilgesetzbuch |
| BV | 101 | `bv` | Bundesverfassung |
| BGG | 173.1 | `bgg` | Bundesgerichtsgesetz |

## Pitfalls

- **StPO vs StGB**: User might say "StPO" (Strafprozessordnung) or "StGB" (Strafgesetzbuch) — always clarify which they mean. Both start with "St".
- **get_law requires abbreviation, not SR number**: Use `abbreviation='StPO'`, not `sr_number='312.0'` (though both work).
- **Commentary may be unavailable**: Not all laws have OnlineKommentar entries. If `get_commentary` returns nothing, skip the Literatur section.
- **Doctrine returns fewer results for new/obscure laws**: Leading cases section may be thin for newer articles (like StPO Art. 1-10 which are general principles). That's okay — include what's available.
- **Git auth timeout**: The `.env` file has `GITHUB_TOKEN`. Always `source .env` before using it. The gh CLI stores auth in `~/.config/gh/hosts.yml`.
- **Remote divergence**: Always `git pull --rebase` before push if rejected. Stash unstaged changes first to avoid conflicts.