# Knowledge Base

A RAG (Retrieval-Augmented Generation) knowledge base of software engineering principles, embedded in this project and queryable by agents at session start.

## Structure

```
knowledge-base/
  entries/          ← source of truth (git-versioned markdown + YAML frontmatter)
  db/chroma/        ← derived artifact (gitignored, rebuilt from entries/)
  scripts/
    embed.py        ← index all entries into ChromaDB
    query.py        ← CLI query tool for human testing and agent use
  schema.yaml       ← required frontmatter fields and allowed values
  README.md         ← this file
```

## Quick Start

**Index entries into ChromaDB:**
```bash
python knowledge-base/scripts/embed.py
```

**Query the knowledge base:**
```bash
python knowledge-base/scripts/query.py "designing authentication for a healthcare app" --domain security --top-k 8
```

**JSON output (for agent consumption):**
```bash
python knowledge-base/scripts/query.py "event-driven microservices" --json --top-k 10
```

## Entry Format

Every entry is a markdown file with YAML frontmatter. Required fields: `id`, `title`, `domain`, `sub-domain`. See `schema.yaml` for full field definitions and allowed values.

```markdown
---
id: least-privilege
title: "Principle of Least Privilege"
domain: security
sub-domain: access control
applies-to: [backend, infrastructure, all]
complexity: low
maturity: established
theorist: "Jerome Saltzer, Michael Schroeder"
year: 1975
related: [zero-trust, defence-in-depth, need-to-know]
tags: [access-control, permissions, iam]
---

## Definition
...

## Example
...

## Strengths
...

## Weaknesses
...

## Mitigation
...
```

## Human UI

Point Obsidian at `knowledge-base/entries/` to browse entries with frontmatter properties panel and graph view of `related:` links.

## Plan

Full architecture decisions, deployment phases, and implementation steps: `docs/knowledge-base-rag-plan.md`
