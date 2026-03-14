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
4. [cs-onboard](#4-cs-onboard)
5. [google-workspace-cli](#5-google-workspace-cli)
6. [ms365-tenant-manager](#6-ms365-tenant-manager)
7. [atlassian-suite](#7-atlassian-suite) (atlassian-admin, atlassian-templates, confluence-expert, jira-expert)

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

## 4. cs-onboard

**Source**: github.com/alirezarezvani/claude-skills `c-level-advisor/cs-onboard/SKILL.md`
**Rejected**: 2026-03-12
**Reason for rejection**: Explicitly writes to `~/.claude/company-context.md` — user's global Claude config directory. The skill's own documentation confirms: "After the interview, generate `~/.claude/company-context.md`" and "Do not move it." This is the setup wizard for the entire `context-engine` ecosystem (also rejected).

### What It Does

A first-run onboarding wizard for the c-level advisor suite. When a new user activates the c-suite skill set for the first time, `cs-onboard` runs an interactive interview to gather company information, then generates the `company-context.md` file that all other c-level advisor skills depend on.

**Key behaviours**:
- Runs a structured interview across the same 7 dimensions as `context-engine`: Company, Product, Market, Competition, Metrics, Voice, Team
- Prompts for each dimension in sequence with guided follow-up questions
- After the interview, generates and writes the context file to disk
- Optionally integrates with LinkedIn, Crunchbase, and Google News to pre-populate competitive intelligence before writing
- Designed as a one-time setup — instructs user not to move the generated file

**Relationship to other rejected skills**: `cs-onboard` is the initializer; `context-engine` is the runtime update layer. Neither is useful without the other. Both were rejected for the same `~/.claude/` path violation.

### What a Compliant Version Would Need

The interview and generation concept is entirely sound. The only violation is where the file is written.

| cs-onboard behaviour | Compliant approach |
|---|---|
| Structured interview across 7 dimensions | Carry over as-is. |
| Write to `~/.claude/company-context.md` | **Change**: Write to `memory/company-context.md` (project-relative). |
| Pre-population from LinkedIn/Crunchbase/Google News | Permitted — external reads for enrichment. No data exfiltrated. |
| "Do not move it" instruction | Replace with correct path instruction. |

A compliant `cs-onboard` is essentially `/ctx init` — the subcommand already added to the approved `/ctx` skill. The init subcommand runs an interview and writes to `memory/company-context.md` with Operator confirmation.

### Build Priority

**Already covered** — the `/ctx init` subcommand in the approved `ctx` skill covers this design intent. No separate build needed.

---

## 5. google-workspace-cli

**Source**: github.com/alirezarezvani/claude-skills `engineering-team/google-workspace-cli/SKILL.md`
**Rejected**: 2026-03-13
**Reason for rejection**: `gws_recipe_runner.py` uses `subprocess.run(cmd, shell=True)` — live shell execution with Google OAuth credentials active in the Claude session. Additional scripts run `gcloud` subprocesses directly. Direct live execution with no review buffer between Claude output and Google Workspace changes.

### What It Does

A CLI wrapper for Google Workspace administration using the `gws` tool. Covers Gmail, Drive, Calendar, Meet, Chat, Contacts, Groups, Users, and Shared Drives.

**Key behaviours**:
- `gws_recipe_runner.py` — executes `gws` CLI commands directly via `shell=True`
- `gws_doctor.py` — checks gws installation and auth status (subprocess)
- `workspace_audit.py` — audits workspace configuration (subprocess for gcloud)
- `auth_setup_guide.py` — guides OAuth setup, runs `gcloud auth` commands

**The problem**: `shell=True` with live OAuth means a Claude session error, hallucination, or bad prompt produces an immediate Workspace change with no review step.

### What the Compliant `/gws` Skill Needs

| google-workspace-cli behaviour | Compliant approach |
|---|---|
| Execute `gws` commands directly in Claude session | Generate a `registry/pending-ops/gws/YYYY-MM-DD-HH-MM.sh` script for Operator review |
| `shell=True` subprocess | No subprocess in Claude session at all — output is a reviewed shell script |
| Live OAuth during session | Credentials only needed when Operator runs the reviewed script |
| Doctor/audit tools | Permitted read-only — these can remain as-is (no writes, no live auth) |

**Sync mechanism**: Operator reviews the generated `.sh` file, then runs it manually. One script per session batch. The gws CLI itself is unchanged — only when it fires changes.

### Build Priority

**High** — Google Workspace is a common admin target. The compliant version is structurally simple: replace subprocess execution with file generation. The `gws` CLI and recipe logic carry over entirely.

> **Prerequisite gate — do not build until all of the following are established:**
> 1. Operator has identified the specific Google Workspace tenant and admin scope required
> 2. Data flow is defined: what data enters the session, what the generated script touches, and what stays local
> 3. OAuth credential management approach is vetted — credentials must not appear in session context or generated files
> 4. A specific integration need exists that native Claude cannot meet without the `gws` CLI
>
> Check this file (§5) before starting. The design intent is ready; the operator context is the gate.

---

## 6. ms365-tenant-manager

**Source**: github.com/alirezarezvani/claude-skills `engineering-team/ms365-tenant-manager/SKILL.md`
**Rejected**: 2026-03-13
**Reason for rejection**: SKILL.md describes PowerShell subprocess execution for live M365 admin operations with credentials passed via environment variables. Direct execution in Claude session means no review buffer between generated PowerShell and M365 tenant changes.

### What It Does

Microsoft 365 tenant administration via PowerShell automation. Covers user lifecycle (create, disable, offboard), Teams management, SharePoint sites, Exchange policies, conditional access, and compliance.

**Key behaviours**:
- Generates PowerShell commands for M365 Graph API and Exchange Online
- Executes via subprocess with credentials from env vars
- Covers high-privilege operations: user provisioning, license assignment, MFA policy, conditional access rules

**The problem**: High-privilege operations (conditional access, MFA policy, bulk user changes) executing directly in a Claude session with no mandatory review step before they land in the tenant.

### What the Compliant `/m365` Skill Needs

| ms365-tenant-manager behaviour | Compliant approach |
|---|---|
| Execute PowerShell in Claude session | Generate `registry/pending-ops/m365/YYYY-MM-DD-HH-MM.ps1` for Operator review |
| Credentials via env vars during session | Credentials only needed when Operator runs the reviewed `.ps1` |
| Direct high-privilege ops | All high-privilege ops (conditional access, MFA, bulk) require explicit Operator review before execution |
| Audit and reporting commands (read-only) | Permitted as-is — read-only Graph API calls are low risk |

**Sync mechanism**: Operator reviews the generated `.ps1` file, then runs it in a PowerShell session with M365 credentials. One script per Claude session batch.

### Build Priority

**Medium** — M365 admin is high-privilege territory. The compliant version is straightforward (file generation instead of subprocess execution) but the script templates need careful review given the privilege level of the operations.

> **Prerequisite gate — do not build until all of the following are established:**
> 1. Operator has identified the specific M365 tenant and the admin roles/operations required
> 2. Data flow is defined: session scope, what the generated `.ps1` touches, and what credential store is used
> 3. PowerShell credential management is vetted — credentials must not appear in session context or generated scripts in plaintext
> 4. High-privilege operation categories (conditional access, MFA, bulk user changes) have explicit Operator-approved scope limits documented
> 5. A specific integration need exists that native Claude cannot meet
>
> Check this file (§6) before starting. The design intent is ready; the operator context is the gate.

---

## 7. atlassian-suite

This entry covers four skills rejected for the same architectural reason and replaced by a single compliant `/atlassian` skill.

**Skills covered**:
- `project-management/atlassian-admin` — user provisioning, permission changes via Atlassian REST API
- `project-management/atlassian-templates` — Confluence page creation from templates via MCP
- `project-management/confluence-expert` — full Confluence management including delete operations via MCP
- `project-management/jira-expert` — Jira project/issue management including bulk operations via MCP

**Rejected**: 2026-03-13
**Reason for rejection**: All four skills write to external Atlassian SaaS services (Confluence, Jira) via live MCP connections during the Claude session. No review buffer between Claude output and external changes. `confluence-expert` additionally exposes `delete_page` and `delete_space` operations — irreversible actions with no staging step.

### What They Do Collectively

| Skill | Operations |
|---|---|
| `atlassian-admin` | Create/disable users, assign groups, manage permissions, audit access |
| `atlassian-templates` | Create Confluence pages from templates; `confluence_create_page`, `confluence_update_page` |
| `confluence-expert` | Full space/page lifecycle: `create_space`, `create_page`, `update_page`, `delete_page` |
| `jira-expert` | `create_project`, `create_issue`, `update_issue`, `transition_issue`, bulk ops |

**The problem**: Four separate skills with overlapping Atlassian scope, all writing live via MCP. `delete_page` is irreversible. Bulk Jira operations can affect hundreds of issues in one call. No mandatory review step.

### What the Compliant `/atlassian` Skill Needs

One unified skill covering all four domains with a local-first staging architecture:

| atlassian-suite behaviour | Compliant approach |
|---|---|
| Live MCP writes during Claude session | Stage operations as structured JSON in `registry/pending-ops/atlassian/` |
| `delete_page` / `delete_space` live | Staged as a delete request — requires explicit second confirmation at sync time |
| Bulk Jira operations live | Staged as a bulk spec — Operator reviews scope before sync |
| User provisioning live | Staged as a provisioning request — reviewed before any account changes |
| Read operations (get_pages, get_issues, search) | Permitted live — reads are low risk and needed for context |

**Staging format**: Each Claude session produces a timestamped JSON file in `registry/pending-ops/atlassian/YYYY-MM-DD-HH-MM-ops.json`. The file lists operations in sequence with type, target, payload, and a `requires_confirmation` flag for destructive ops.

**Sync mechanism**: `scripts/atlassian-sync.py` reads the staging directory, presents a summary of pending operations, prompts for confirmation on any destructive ops, then executes via Atlassian REST API using credentials from env vars. Processed files are moved to `registry/processed/atlassian/`.

**MCP**: The existing Atlassian MCP can remain for read operations. Write operations go through the staging path only.

### Build Priority

**High** — Atlassian is the most commonly used project management stack in this skill set. Four skills collapse into one. The compliant version adds a staging layer but preserves all the useful functionality. The Python sync script is the main build artifact beyond the SKILL.md itself.

> **Prerequisite gate — do not build until all of the following are established:**
> 1. Operator has identified the specific Atlassian Cloud instance and the projects/spaces in scope
> 2. Data flow is defined: what enters the session, what is staged, what the sync script touches
> 3. Atlassian API token management is vetted — tokens must not appear in session context or staged JSON files
> 4. Destructive operations (`delete_page`, `delete_space`, bulk Jira transitions) have explicit Operator-approved scope limits documented before the sync script is built
> 5. A specific integration need exists that cannot be met by the Atlassian web UI or existing CLI tools
>
> Check this file (§7) before starting. The design intent is ready; the operator context is the gate.

---

## Revision History

| Rev | Date | Author | Model | Why |
|---|---|---|---|---|
| 1.0 | 2026-03-12 | Joshua Alexander Clement | claude-sonnet-4-6 | Initial creation — design intents for 3 hard-rejected c-level and engineering-team skills |
| 1.1 | 2026-03-12 | Joshua Alexander Clement | claude-sonnet-4-6 | Added cs-onboard (§4) — context-engine ecosystem setup wizard; already covered by `/ctx init` |
| 1.2 | 2026-03-13 | Joshua Alexander Clement | claude-sonnet-4-6 | Added §5 google-workspace-cli, §6 ms365-tenant-manager, §7 atlassian-suite (4 skills) — all rejected for direct live writes to external services; replaced by compliant local-first `/gws`, `/m365`, `/atlassian` skills |
| 1.3 | 2026-03-13 | Joshua Alexander Clement | claude-sonnet-4-6 | Added prerequisite gate blocks to §5, §6, §7 — build is deferred until Operator establishes target service, data flow, credential management, and scope limits for each integration |
