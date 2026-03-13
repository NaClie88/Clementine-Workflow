# Rejected Skill Design Intents

**Type**: Reference Document
**Status**: Active
**Purpose**: Design intent summaries for hard-rejected external skills — reference for building compliant equivalents.

When a skill is rejected for implementation violations rather than concept flaws, its design intent is documented here so the Operator can evaluate whether a standards-compliant version is worth building.

---

## Contents
1. [context-engine](#1-context-engine)
2. [chief-of-staff](#2-chief-of-staff)
3. [self-improving-agent](#3-self-improving-agent)

---

## 1. context-engine

**Source**: github.com/alirezarezvani/claude-skills `c-level-advisor/context-engine/SKILL.md`
**Rejected**: 2026-03-12
**Reason for rejection**: Reads and writes `~/.claude/company-context.md` — user's global Claude config directory used as persistent storage.

### What It Does

A persistent company knowledge base that enriches Claude's context during conversations. Instead of manually re-explaining your company in every session, `context-engine` maintains a structured profile with named dimensions:

| Dimension | What it captures |
|---|---|
| Company | Mission, stage, founding year, team size |
| Product | Core offering, key features, differentiators |
| Market | Target customer, ICP, key segments |
| Competition | Named competitors, positioning relative to each |
| Metrics | Key business KPIs and current values |
| Voice | Tone, communication style, brand personality |
| Team | Key roles, reporting lines, decision makers |

**Key behaviours**:
- Loads the context file at the start of any c-suite advisor session
- Detects stale context (>90 days since last update) and prompts for a refresh
- During conversations, detects when new information warrants a context update (e.g., a new competitor is mentioned) and offers to add it
- Enforces privacy/anonymization rules before any external API calls

### What a Compliant Version Would Need

- Store context in a **project-relative path** — `memory/company-context.md` rather than `~/.claude/company-context.md`
- Context enrichment must be **explicit, not autonomous** — present a proposed update and require Operator confirmation before writing
- Staleness detection can remain — prompt only, no automatic changes
- Privacy rules remain valuable and carry over as-is

### Build Priority

**High** — nearly every c-level and marketing skill in the reviewed set conditionally reads a company context file. A compliant version unlocks the rest of the c-level advisor ecosystem.

---

## 2. chief-of-staff

**Source**: github.com/alirezarezvani/claude-skills `c-level-advisor/chief-of-staff/SKILL.md`
**Rejected**: 2026-03-12
**Reason for rejection**: (1) Writes to `~/.claude/decision-log.md`. (2) Depends on `context-engine` (also rejected) for all context loading.

### What It Does

An orchestration layer for the c-level advisor ecosystem. Routes strategic questions to the right specialist role, manages conversation state across multiple advisor activations, and tracks decisions over time.

**Key behaviours**:
- **Topic detection** — classifies the strategic question and selects which advisor roles to activate (e.g., market expansion → CEO, CMO, CFO, CRO, COO)
- **Routing** — invokes specialist skills using a structured `[INVOKE:role|question]` syntax
- **Loop prevention** — enforces max depth 2, blocks A→B→A circular routing
- **Decision log** — records decisions with date and rationale for continuity across sessions
- **Synthesis** — summarizes multi-advisor outputs into a single unified recommendation

### What a Compliant Version Would Need

- Decision log stored in **`registry/` or `memory/`** (project-relative), not `~/.claude/`
- Context loading from **`memory/company-context.md`** (compliant context-engine equivalent), not `~/.claude/`
- Routing and synthesis logic carries over as-is — no inherent violations there
- Loop prevention logic is sound and reusable

### Dependency Note

Chief-of-staff is only useful once `context-engine` (§1 above) has a compliant equivalent. Build context-engine first.

### Build Priority

**Medium** — useful orchestration layer but only activates its full value once the c-level advisor ecosystem is otherwise functional. Build after context-engine.

---

## 3. self-improving-agent

**Source**: github.com/alirezarezvani/claude-skills `engineering-team/self-improving-agent/SKILL.md`
**Rejected**: 2026-03-12
**Reason for rejection**: (1) `/si:promote` writes to `CLAUDE.md` (governance instruction file) and `.claude/rules/` (`.claude/` config path). (2) `error-capture.sh` is a persistent PostToolUse shell hook that fires on every Bash command without Operator control.

### What It Does

A meta-skill that curates Claude Code's auto-memory (`MEMORY.md`) into durable project knowledge. Claude's auto-memory accumulates observations about a project over time — coding patterns, debugging solutions, preferences. The self-improving agent adds an editorial layer on top.

**Key behaviours**:

| Command | What it does |
|---|---|
| `/si:review` | Analyze `MEMORY.md` — identify promotion candidates, stale entries, consolidation opportunities |
| `/si:promote` | Graduate a pattern from `MEMORY.md` → `CLAUDE.md` or `.claude/rules/` (writes governance files) |
| `/si:extract` | Turn a proven debugging solution into a reusable skill file |
| `/si:status` | Memory health dashboard — line counts, topic distribution, capacity warnings |
| `/si:remember` | Explicitly save knowledge to auto-memory |
| `error-capture.sh` | PostToolUse hook — fires on every Bash error and prompts `/si:remember` |

**Why the concept is valuable**: Auto-memory fills up with raw, unstructured observations. Without curation, useful patterns get buried. The agent's core insight is that there is a meaningful difference between a rough note in memory and an enforced rule in `CLAUDE.md` — and someone (or something) needs to manage that promotion process deliberately.

### What a Compliant Version Would Need

The concept is sound. The violations are in the implementation, not the idea.

| Self-improving behaviour | Compliant approach |
|---|---|
| `/si:review` — read-only MEMORY.md analysis | Carry over as-is. Read-only. No changes needed. |
| `/si:promote` — write to CLAUDE.md / .claude/rules/ | **Change**: Output a formatted block of text the Operator pastes manually. Never write directly. |
| `/si:extract` — write a new skill file | **Permitted** if written to a project-scoped `skills/` directory, not `.claude/`. |
| `/si:status` — memory health dashboard | Carry over as-is. Read-only. No changes needed. |
| `/si:remember` — write to MEMORY.md | Permitted. MEMORY.md is the auto-memory file, not a governance document. |
| `error-capture.sh` — PostToolUse hook | **Remove**. Replace with an explicit user-invoked `/si:remember` after an error. The hook fires without Operator control. |

### Build Priority

**Medium** — genuinely useful for managing project memory discipline. The compliant version is primarily a constraint: promote outputs as text for the Operator to apply, never write to governance files directly.

---

## Revision History

| Rev | Date | Author | Model | Why |
|---|---|---|---|---|
| 1.0 | 2026-03-12 | Joshua Alexander Clement | claude-sonnet-4-6 | Initial creation — design intents for 3 hard-rejected c-level and engineering-team skills |
