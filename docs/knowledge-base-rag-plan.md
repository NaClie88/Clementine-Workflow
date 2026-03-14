# Knowledge Base RAG System — Plan

**Type**: Plan Document
**Status**: Approved — pending implementation
**Constitutional Authority**: `memory/constitution.md` Part 7, Amendment 6 (Architecture Decision Records), Part 6, Amendment 1 (Integration Architecture)

---

## End Goal

Build a RAG (Retrieval-Augmented Generation) knowledge base that can be embedded in any new project and queried by a project agent at session start. The agent retrieves only the principles relevant to the current project context — rather than receiving the entire knowledge base — and uses them to guide development toward the strongest possible product from day one.

The system must be both agent-readable (semantic query) and human-readable (browsable UI).

---

## Architecture Decisions (ratified in session 2026-03-14)

| Decision | Choice | Rationale |
|---|---|---|
| Storage model | Embedded in project repo | Self-contained, portable, no external service dependency |
| Local tool | LanceDB | File-based (Arrow columnar), no server process, same Python API as self-hosted. Approved: D01 |
| Self-hosted path | LanceDB server | Same client API as local — migration is a connection string change |
| Cloud path | LanceDB Cloud | Same client API as local and self-hosted — migration is a connection string change |
| Embedding model | `sentence-transformers/all-MiniLM-L6-v2` | Small, fast, CPU-only, no API key required |
| Source of truth | Per-entry markdown files with YAML frontmatter | Git-native, human-readable, agent-readable, diffable |
| Human UI (now) | Obsidian | Reads frontmatter natively, renders graph of `related:` links, zero infrastructure |
| Human UI (later) | MkDocs or Docusaurus | Static site from the same markdown files, web-accessible |
| Deployment model | Local → self-hosted → cloud | In that order, no wasted work between phases |

---

## Deployment Phases

### Phase 1 — Local (current target)
- LanceDB stores as files on disk (`knowledge-base/db/lance/`)
- `embed.py` rebuilds the index from source files
- `query.py` CLI for human testing
- Agent query skill (vetted through Phase 1–4 workflow)
- Human UI: Obsidian pointed at `knowledge-base/entries/`

### Phase 2 — Self-hosted
- Run LanceDB server pointed at `./db/lance/` — same data, server-accessible
- Client connection string changes from local path to `http://localhost:8080`
- Everything else identical
- Human UI: MkDocs static site on the same files

### Phase 3 — Cloud
- Connect LanceDB client to LanceDB Cloud (or pgvector if Postgres is already the app datastore)
- Connection string change only — no code rewrite required
- Human UI: deployed MkDocs or a purpose-built filter UI

---

## Repository Structure

```
knowledge-base/
  entries/                    ← source of truth (git-versioned)
    security/
    privacy/
    architecture/
    methodology/
    database/
    distributed-systems/
    ux/
    systems-thinking/
    functional-programming/
    ml-ai/
    ethics/
    performance/
    organisation/
    documentation/
  db/
    lance/                    ← derived artifact (gitignored, rebuilt from entries/)
  scripts/
    embed.py                  ← indexes all entries into LanceDB
    query.py                  ← CLI query tool for human testing
  schema.yaml                 ← required frontmatter fields and allowed values
  README.md                   ← how to use the knowledge base
```

The `db/` directory is gitignored. It is rebuilt by running `embed.py`. It is never the source of truth.

---

## Entry Schema (`schema.yaml`)

Every entry file must include this frontmatter. Fields marked `required` will be validated by `embed.py` — entries missing required fields will not be indexed and will log a warning.

```yaml
# Required fields
id: string                    # kebab-case, globally unique (e.g. least-privilege)
title: string                 # human-readable name
domain: enum                  # see Domain Catalogue below
sub-domain: string            # free text, more specific grouping within domain

# Classification
applies-to: list[enum]        # backend | frontend | infrastructure | cloud | mobile
                              # data | ml | all
complexity: enum              # low | medium | high  (complexity to implement correctly)
maturity: enum                # established | emerging | theoretical

# Provenance
theorist: string              # primary author/originator (or "multiple" if collective)
year: integer                 # year the concept was named/published (approximate is fine)

# Relationships
related: list[id]             # IDs of related entries — drives graph view in Obsidian

# Discovery
tags: list[string]            # free-form tags for search and filtering
```

### Allowed `domain` values

```
security              privacy               architecture
methodology           database              distributed-systems
ux                    systems-thinking      functional-programming
coding-practices      ml-ai                 ethics
performance           organisation          documentation
```

---

## RAG Pipeline

```
INDEXING  (run embed.py once, then on each content update)
──────────────────────────────────────────────────────────
  entries/*.md
      │
      ▼
  embed.py
  - reads each file
  - extracts frontmatter metadata
  - embeds body text using all-MiniLM-L6-v2
  - stores vector + metadata in LanceDB
      │
      ▼
  db/lance/  (local Arrow files)


RETRIEVAL  (agent runs query skill at session start or on demand)
──────────────────────────────────────────────────────────────────
  Agent receives project context:
  "Building a healthcare API with E2EE messaging and Postgres backend"
      │
      ▼
  query skill
  - embeds the context string
  - similarity search in LanceDB
  - optional pre-filter on domain/applies-to metadata
  - returns top-K entries (default: 10)
      │
      ▼
  Agent receives ~3,000 tokens of relevant principles
  (not ~80,000 tokens of the entire knowledge base)
      │
      ▼
  Agent uses principles to guide development decisions  ← Augmented Generation
```

---

## Implementation Steps

### Step 1 — Define and ratify `schema.yaml`
Write the frontmatter schema file. Review allowed values for `domain` and `applies-to`. This is the decision that cannot easily be changed after 500 entries exist — get it right first.

**Output:** `knowledge-base/schema.yaml`

### Step 2 — Migrate existing content to per-entry files
Restructure `docs/dev-philosophy-reference.md` (107 entries) into individual files under `knowledge-base/entries/`. Each entry gets the schema frontmatter added.

This is the bulk of the migration work. The content already exists — this is restructuring, not rewriting.

**Output:** 107 individual `.md` files in `knowledge-base/entries/`

### Step 3 — Write `embed.py`
Python script that:
- Walks `knowledge-base/entries/` recursively
- Parses YAML frontmatter from each file
- Validates required fields against `schema.yaml` (logs warnings for missing fields, does not crash)
- Embeds the body text using `sentence-transformers/all-MiniLM-L6-v2`
- Upserts into LanceDB (idempotent — safe to re-run on update)
- Prints a summary: N entries indexed, M warnings

**Output:** `knowledge-base/scripts/embed.py`

### Step 4 — Write `query.py`
CLI tool that:
- Accepts a query string as argument
- Optional flags: `--domain security`, `--applies-to backend`, `--top-k 10`
- Embeds the query, searches LanceDB, returns formatted results
- Supports both human-readable output and `--json` for machine consumption
- Exits with code 0 on success, 1 on failure

```bash
python query.py "designing authentication for a healthcare app" --domain security --top-k 8
```

**Output:** `knowledge-base/scripts/query.py`

### Step 5 — Vet and approve the query skill
The query script becomes an agent skill. It goes through the full vetting workflow (Phases 1–4) documented in `docs/skill-vetting-workflow.md`.

Phase 4 Docker sandbox: `--network none` is acceptable (no network needed — local LanceDB only).

**Output:** Entry in `docs/approved-skills.md`

### Step 6 — Add Tier 1 domain entries
With the infrastructure in place, continue adding entries from the domain catalogue. Priority order (most foundational first):

1. Database & Data Theory (8 entries)
2. Distributed Systems Theory (7 entries)
3. Systems Thinking (10 entries)
4. Functional Programming Principles (5 entries)
5. UI/UX Theory (11 entries)

---

## Domain Catalogue — Full Scope

This is the complete list of domains identified for future content. Domains are grouped by implementation tier.

### Tier 1 — Add to current knowledge base (same abstraction level as existing content)

**Database & Data Theory**
Relational theory (Codd's rules, normalisation 1NF→BCNF), CAP theorem, PACELC extension, ACID vs BASE, data modelling paradigms (relational/document/graph/columnar/time-series), dimensional modelling (Kimball vs Inmon), schema evolution philosophy, data mesh, data contracts.

**Distributed Systems Theory**
Fallacies of Distributed Computing (Deutsch), Two Generals / Byzantine Generals problems, Lamport clocks / vector clocks, Saga pattern, CRDTs, Circuit Breaker, Bulkhead pattern.

**UI/UX Theory**
User-Centered Design (Norman/ISO 9241), cognitive load theory, affordance theory (Gibson/Norman), Gestalt principles, Fitts's Law, Hick's Law, Nielsen's 10 Usability Heuristics, progressive disclosure, design thinking, Jobs to be Done, dark patterns taxonomy.

**Systems Thinking**
Cynefin framework (Snowden), feedback loops (Meadows), Theory of Constraints (Goldratt), Conway's Law, Goodhart's Law, Hyrum's Law, Gall's Law, Postel's Robustness Principle, Little's Law, second-order thinking.

**Functional Programming Principles**
Immutability and pure functions, referential transparency, function composition, algebraic data types (making invalid states unrepresentable), Unix philosophy (do one thing well, composable tools, text as universal interface).

### Tier 2 — Future separate documents (right level, different audience)

**ML/AI Engineering Philosophy** → `knowledge-base/entries/ml-ai/`
Bias-variance tradeoff, no free lunch theorem, data-centric vs model-centric AI, distributional shift/concept drift, FATE framework (fairness/accountability/transparency/explainability), AI alignment, the Bitter Lesson, MLOps philosophy, calibration, interpretability vs explainability.

**Software Ethics** → `knowledge-base/entries/ethics/`
ACM Code of Ethics, algorithmic fairness theories (disparate impact, individual fairness, counterfactual fairness), value-sensitive design, green software/carbon-aware computing, free software vs open source philosophy (Stallman vs Raymond), license philosophy (copyleft vs permissive), attention economy ethics.

**Organisational & Team Design** → `knowledge-base/entries/organisation/`
Team Topologies (stream-aligned/platform/enabling/complicated-subsystem), Dunbar's number, psychological safety (Edmondson), autonomy/mastery/purpose (Pink), Wardley Mapping, T-shaped skills philosophy.

### Tier 3 — Sections within existing domains (not separate documents)

Performance Engineering (deeper): Amdahl's Law, Universal Scalability Law, queueing theory, memory hierarchy theory, performance budgets.

Documentation Theory: Divio documentation system (tutorials/how-tos/reference/explanation), docs-as-code, living documentation.

Cryptography (deeper): PKI design philosophy, Certificate Transparency, post-quantum migration philosophy.

Information Theory Fundamentals: Shannon entropy, type theory as proof system, the Halting Problem, formal verification.

---

## Content Already Produced (migration source)

`docs/dev-philosophy-reference.md` — 107 entries, 2,537 lines.

This file is the migration source for Step 2. Its sections map to knowledge-base domains as follows:

| Existing section | Target domain folder |
|---|---|
| 1.1 Design Principles | `entries/architecture/` |
| 1.2 Architectural Philosophies | `entries/architecture/` |
| 1.3 Development Methodologies | `entries/methodology/` |
| 1.4 Operational Philosophies | `entries/methodology/` |
| 2. Coding Best Practices | `entries/coding-practices/` |
| 3.1 Foundational Privacy Theories | `entries/privacy/` |
| 3.2 Regulatory Frameworks | `entries/privacy/` |
| 3.3 Technical Privacy Approaches | `entries/privacy/` |
| 4.1 Foundational Security Principles | `entries/security/` |
| 4.2 Threat Modelling Methodologies | `entries/security/` |
| 4.3 Industry Frameworks & Standards | `entries/security/` |
| 4.4 Secure Development Practices | `entries/security/` |
| 4.5 Privacy & Security Architecture Patterns | `entries/security/` + `entries/privacy/` |

`docs/dev-philosophy-reference.md` is **not deleted** after migration. It becomes a generated artifact — rebuilt from the entry files if needed — or archived as a snapshot. The per-entry files are the new source of truth.

---

## Dependencies

```
Python 3.11+
lancedb==0.29.2
sentence-transformers==5.3.0
python-frontmatter==1.1.0
pyyaml==6.0.3
```

All approved per STD09 §2.4 (Decision record: D01). No GPU required. Runs on the same machine that runs Claude Code.

---

## What This Is Not

- This is not a documentation site (that is Obsidian/MkDocs — a separate concern)
- This is not a general-purpose database (it is a read-mostly knowledge index)
- This is not a replacement for the constitution or standards documents (those govern behaviour; this provides knowledge)
- This is not a web service (it is an embedded tool until Phase 2)

---

## Revision History

| Rev | Date | Author | Why |
|---|---|---|---|
| 1.0 | 2026-03-14 | Joshua Alexander Clement | Initial plan — architecture decisions made in session. Written before context compaction. |
| 1.1 | 2026-03-14 | Joshua Alexander Clement | Updated ChromaDB → LanceDB throughout following STD09 §4 approval process (D01). |

Assisted-By: Anthropic Claude Sonnet 4.6 (claude-sonnet-4-6)
