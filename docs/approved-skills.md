# Approved Claude Code Skills Registry

**Type**: Reference Document
**Status**: Ratified
**Constitutional Authority**: `memory/constitution.md` Part 5, Amendment 5 (Accountability), Governance (Operator declaration)

---

## Purpose

Defines which Claude Code skills (slash commands) are approved for use in sessions on this system. The default answer to "can I use this skill?" is **no** — until it has been reviewed and added to this registry.

Skills are invocable slash commands (`/skill-name`) that trigger pre-defined agent behaviours. They range from low-risk utilities (formatting commits) to high-risk automation (recurring loops, code modification). This registry ensures skills are understood before they are used and that their behaviour is consistent with this system's constitution and standards.

---

## Contents
1. [The Rule](#1-the-rule)
2. [Approved Skills](#2-approved-skills)
3. [Approval Process](#3-approval-process)
4. [Risk Classification](#4-risk-classification)
5. [Skills Under Review](#5-skills-under-review)
6. [Rejected Skills](#6-rejected-skills)

---

## 1. The Rule

**Use only what is listed in §2. Do not invoke unapproved skills.**

Before invoking any skill:
1. Check §2 — if it is listed and approved, use it.
2. If it is not listed — stop. Review it per §3 before use.

An unapproved skill is not necessarily unsafe — it is unknown. The review process exists to understand it before it touches this system.

---

## 2. Approved Skills

### Core Skills

| Skill | Invocation | Risk | What It Does | Caveats | Approved | Date |
|---|---|---|---|---|---|---|
| Commit | `/commit` | Low | Stages and commits changes with a correctly formatted commit message following STD03 | Reviews diff before committing — verify staged files are correct first | Joshua Alexander Clement | 2026-03-12 |
| Simplify | `/simplify` | Low–Medium | Reviews recently changed code for reuse, quality, and efficiency — then fixes issues found | Makes edits to code; review its changes before accepting | Joshua Alexander Clement | 2026-03-12 |
| Review PR | `/review-pr [number]` | Low | Reviews a GitHub pull request — checks for issues, consistency, and quality | Read-only analysis; no changes made | Joshua Alexander Clement | 2026-03-12 |
| Claude API | `/claude-api` | Low | Assists with building applications using the Anthropic SDK or Claude API | Triggers when code imports `@anthropic-ai/sdk` or similar; does not invoke external APIs itself | Joshua Alexander Clement | 2026-03-12 |
| Keybindings Help | `/keybindings-help` | Low | Configures Claude Code keyboard shortcuts and keybindings in `~/.claude/keybindings.json` | Writes to local config file | Joshua Alexander Clement | 2026-03-12 |

### Automation Skills

| Skill | Invocation | Risk | What It Does | Caveats | Approved | Date |
|---|---|---|---|---|---|---|
| Loop | `/loop [interval] [command]` | High | Runs a prompt or slash command on a recurring interval (default 10 min) | **Persistent automation** — runs until explicitly stopped. Use only for well-defined, bounded tasks. Never loop destructive or write operations without a stop condition. | Joshua Alexander Clement | 2026-03-12 |

### Testing Skills

| Skill | Invocation | Risk | What It Does | Caveats | Approved | Date |
|---|---|---|---|---|---|---|
| Playwright Pro | `/pw:init` `/pw:generate` `/pw:review` `/pw:fix` `/pw:migrate` `/pw:coverage` `/pw:report` `/pw:testrail` `/pw:browserstack` | Low–Medium | Production Playwright testing toolkit. Generates, reviews, fixes, and migrates E2E tests. 55 templates, 3 agents (test-architect, test-debugger, migration-planner). Auto-lints test files on every Write/Edit via hook. Optional TestRail and BrowserStack MCP integrations (fully reviewed). | **Hooks auto-fire**: `validate-test.sh` runs on every Write/Edit to spec files (4-pattern linter, prints warnings only). `detect-playwright.sh` runs at session start (prints hint if playwright.config found, read-only). **Pre-granted**: `Bash(npx playwright*)` and `Bash(npx tsx*)` without per-use confirmation. **MCP servers**: TestRail (read/write test cases and results) and BrowserStack (read builds/sessions, mark pass/fail) — both require explicit env var configuration and fail fast if not set. Neither runs without your credentials. | Joshua Alexander Clement | 2026-03-13 |

### Anthropic Official Skills (github.com/anthropics/skills)

Skills published by Anthropic at the canonical skills repository. Semi-trusted source — same full Phase 1–5 workflow applies; benefit of doubt on ambiguous intent given source credibility. Production document skills (docx, pptx, pdf, xlsx) have effective Phase 4 coverage via production use in Claude.ai.

#### Pure-Prompt Skills

| Skill | Invocation | Risk | What It Does | Caveats | Approved | Date |
|---|---|---|---|---|---|---|
| Algorithmic Art | `/algorithmic-art` | Low | Generates creative algorithmic art using SVG, CSS, and JavaScript canvas. Outputs code artifacts only. | No file I/O, no network, no shell. | Joshua Alexander Clement | 2026-03-13 |
| Brand Guidelines | `/brand-guidelines` | Low | Brand identity framework — tone, color, typography, visual language. | No file I/O, no network, no shell. Note: distinct from alirezarezvani brand-guidelines. | Joshua Alexander Clement | 2026-03-13 |
| Canvas Design | `/canvas-design` | Low | Designs layouts and UI components using HTML5 canvas and CSS. Outputs code artifacts. | No file I/O, no network, no shell. | Joshua Alexander Clement | 2026-03-13 |
| Claude API | `/claude-api` (Anthropic version) | Low | Anthropic SDK integration guidance — patterns, streaming, tool use, caching. | Triggers on Anthropic SDK imports. Coexists with locally written `/claude-api`; overlapping trigger domains — Anthropic version is more detailed. | Joshua Alexander Clement | 2026-03-13 |
| Doc Coauthoring | `/doc-coauthoring` | Low | Collaborative document drafting — structure, audience, clarity, iteration. | Pure prompt, no file I/O. | Joshua Alexander Clement | 2026-03-13 |
| Frontend Design | `/frontend-design` | Low | Frontend component and layout design assistant (React, CSS, accessibility). | No file I/O, no network, no shell. | Joshua Alexander Clement | 2026-03-13 |
| Internal Comms | `/internal-comms` | Low | Internal communication drafting — announcements, memos, policy rollouts. | Pure prompt, no file I/O. | Joshua Alexander Clement | 2026-03-13 |
| Theme Factory | `/theme-factory` | Low | CSS and design system theme generation — tokens, variables, color palettes. | No file I/O, no network, no shell. | Joshua Alexander Clement | 2026-03-13 |

#### Document Processing Skills

| Skill | Invocation | Risk | What It Does | Caveats | Approved | Date |
|---|---|---|---|---|---|---|
| DOCX | `/docx` | Low–Medium | Creates and edits Microsoft Word documents using LibreOffice via subprocess. Production Anthropic skill (powers Claude.ai document editing). | **LibreOffice required** (`libreoffice` in PATH). SKILL.md contains a C LD_PRELOAD shim for AF_UNIX socket restrictions in container/sandbox environments — shim is inert on standard Linux desktops. All file I/O is project-local. | Joshua Alexander Clement | 2026-03-13 |
| PPTX | `/pptx` | Low–Medium | Creates and edits PowerPoint presentations via LibreOffice subprocess. Same architecture as /docx. | **LibreOffice required.** Same LD_PRELOAD shim note as /docx. | Joshua Alexander Clement | 2026-03-13 |
| PDF | `/pdf` | Low–Medium | PDF reading (pypdf, pdfplumber) and generation (reportlab). Extracts text/tables, creates new PDFs. | Packages: pypdf (APPROVED), pdfplumber (APPROVED), reportlab (APPROVED WITH CONDITIONS — output to project-local path only). | Joshua Alexander Clement | 2026-03-13 |
| XLSX | `/xlsx` | Low–Medium | Excel spreadsheet read and write via openpyxl. Cells, formulas, charts. | Packages: openpyxl (APPROVED WITH CONDITIONS — output to project-local path only). | Joshua Alexander Clement | 2026-03-13 |

#### Tooling Skills

| Skill | Invocation | Risk | What It Does | Caveats | Approved | Date |
|---|---|---|---|---|---|---|
| MCP Builder | `/mcp-builder` | Low–Medium | Scaffolds MCP server projects and evaluates them using an agent loop. `evaluation.py` calls Anthropic API directly via SDK. | **Developer tool only.** `evaluation.py` requires `ANTHROPIC_API_KEY` — will fail fast without it. Not intended for production session use. Packages: anthropic (APPROVED WITH CONDITIONS). | Joshua Alexander Clement | 2026-03-13 |
| Skill Creator | `/skill-creator` | Low–Medium | Creates, evaluates, and iterates on Claude Code skill descriptions using `claude -p` subprocesses. During eval runs, temporarily writes command files to `[project-root]/.claude/commands/` — cleaned up in `finally` block. | **Temp file caveat**: eval creates `.claude/commands/<skill>-skill-<uuid>.md` for the duration of each test run (cleaned up on exit, including errors). Files are project-scoped, not user-scoped. Log files written if `--log-dir` specified. | Joshua Alexander Clement | 2026-03-13 |
| Slack GIF Creator | `/slack-gif-creator` | Low–Medium | Generates animated GIFs for Slack using imageio + ffmpeg. All output is local. | Packages: imageio (APPROVED), imageio-ffmpeg (APPROVED WITH CONDITIONS — fixed local paths only; do not pass user-controlled strings as ffmpeg input URI), pillow (APPROVED WITH CONDITIONS), numpy (APPROVED). **ffmpeg binary ships with imageio-ffmpeg** (~70MB). | Joshua Alexander Clement | 2026-03-13 |
| Webapp Testing | `/webapp-testing` | Low–Medium | End-to-end web application testing using Playwright. | Same conditions as `/pw:*` (playwright-pro, already approved). Playwright already in package registry (Tier 3, APPROVED WITH CONDITIONS). | Joshua Alexander Clement | 2026-03-13 |
| Web Artifacts Builder | `/web-artifacts-builder` | Low–Medium | Scaffolds single-file React/Vite/Tailwind web artifact projects. `init-artifact.sh` extracts a bundled `shadcn-components.tar.gz` archive and runs `npm install`. `bundle-artifact.sh` runs Parcel bundler to produce a single `bundle.html`. | **npm install on init** — reaches npmjs.com. Archive (`shadcn-components.tar.gz`) is bundled by Anthropic. Parcel runs as subprocess. All output is project-local. | Joshua Alexander Clement | 2026-03-13 |

---

### Custom Skills (Internally Written)

Skills written for this system and vetted against the full workflow. Source is this project, not an external repository.

| Skill | Invocation | Risk | What It Does | Caveats | Approved | Date |
|---|---|---|---|---|---|---|
| Company Context | `/ctx [load\|status\|update\|init]` | Low | Manages persistent company knowledge base at `memory/company-context.md`. Load, review, update, or initialise structured company context. | Reads and writes `memory/company-context.md` — all writes require explicit Operator confirmation | Joshua Alexander Clement | 2026-03-12 |
| Chief of Staff | `/chief-of-staff [route\|log]` | Low–Medium | Routes strategic questions to the appropriate c-level advisor roles. Presents a routing plan for Operator approval before activating any advisors. Logs ratified decisions to `registry/decisions/`. | Invokes advisor sub-agents — all activations gated by Operator confirmation of the routing plan. Requires `memory/company-context.md` (run `/ctx init` first). | Joshua Alexander Clement | 2026-03-12 |
| Memory Curator | `/curate [review\|promote\|confirm\|extract\|status]` | Low | Curates auto-memory (`MEMORY.md`) into durable project knowledge. Reviews for promotion candidates, runs a consequence check, outputs formatted text for manual application to `CLAUDE.md`. Never writes to governance files directly. | All promotions require manual Operator action — `/curate promote` outputs text to paste; `/curate confirm` marks the entry done. `/curate extract` stages skill templates to `skills/` (not `.claude/`) for vetting. | Joshua Alexander Clement | 2026-03-12 |

---

## 3. Approval Process

When a skill is encountered that is not in §2:

1. **Stop.** Do not invoke it.
2. **Research it.** What does it do? What permissions does it require? What does it write, read, or call?
3. **Classify the risk** per §4.
4. **Add it to §5** (Skills Under Review) with your findings.
5. **Get explicit approval** from the Operator before moving it to §2.
6. **Document the approval** — who approved it, on what date, and with what caveats.

### What counts as approval

| Counts | Does not count |
|---|---|
| Explicit "yes, approve it" from the Operator | Silence or assumption |
| Written confirmation in the session | "I guess it's probably fine" |

---

## 4. Risk Classification

| Level | Description | Examples |
|---|---|---|
| **Low** | Read-only or produces output for human review; no autonomous writes or external calls | `/review-pr`, `/keybindings-help` |
| **Low–Medium** | Writes to files but changes are reviewable before accepting | `/simplify`, `/commit` |
| **Medium** | Calls external services or modifies multiple files autonomously | Skills that push to remotes, open PRs |
| **High** | Persistent automation, recurring execution, or irreversible actions | `/loop` |
| **Unclassified** | Not yet reviewed — treat as High until assessed | Any skill not in this registry |

High-risk skills require a defined stop condition and explicit per-use authorization. Do not invoke a High-risk skill open-endedly.

---

## 5. Skills Under Review

Skills that have been identified but not yet fully reviewed or approved.

**Dependency chain note:** When a skill is listed with `Depends On`, approving it requires the dependency to be approved (or substituted with a compliant equivalent) first. A dependency that is rejected blocks approval of the dependent skill as-is.

**Script-backed skills note:** Phase 1 (static analysis) is now complete for all 125 script-backed skills. Cross-cutting findings from broad sweep: no `~/.claude/` writes, no `CLAUDE.md` writes, no hooks in any script-backed skill. All non-stdlib package imports in Python scripts were found to be inside template string literals (generated code output), not runtime dependencies. The only runtime non-stdlib package is PyYAML, used with `yaml.safe_load()` and guarded with `try/except ImportError` throughout. No hard reject triggers found in any script-backed skill.

> **Group B individual sign-offs (2026-03-13):** All 18 flagged skills (marked `Phase 1 complete (FLAG)`) have been individually reviewed through Phase 1–3 with full script reads. Decisions are recorded in each skill's row below. All 18 approved (8 with caveats, 10 clean). Reviewed by: Joshua Alexander Clement + claude-sonnet-4-6.

> **Group D bulk approval (2026-03-13):** All skills in §5 marked **"Phase 1 complete"** without a FLAG designation have been reviewed through Phase 1–3 and are approved for use under standard conditions: project-local file I/O only, no external network calls, no governance file access, no `~/.claude/` writes. These are stdlib-only Python analytics tools or pure-prompt skills with low risk profiles consistent with the cross-cutting Phase 1 findings above. Individual caveats are noted in each skill's Notes column where applicable. Approved by: Joshua Alexander Clement + claude-sonnet-4-6.

---

### Pure-Prompt Skills (Initial Review Batch)

| Skill | Source | Status | Depends On | Notes |
|---|---|---|---|---|
| `review` | alirezarezvani/claude-skills `.claude/commands/review.md` | Phase 1 complete | — | Good pre-push lint/audit concept. Installs 4 unapproved packages (yamllint, check-jsonschema, safety, markdown-link-check). Hardcoded paths are repo-specific and need rewriting. Needs package registry entries before Phase 4. |
| `security-scan` | alirezarezvani/claude-skills `.claude/commands/security-scan.md` | Phase 1 complete | — | Secret scanning + CVE audit concept. Requires gitleaks (brew) and safety (pip) — both need package registry entries. Makes external network calls to PyPI CVE database. |
| `update-docs` | alirezarezvani/claude-skills `.claude/commands/update-docs.md` | Deferred | — | Entirely hardcoded to source repo structure. Runs 3 unaudited Python scripts. No value to this project as-is. |
| `git/clean` | alirezarezvani/claude-skills `.claude/commands/git/clean.md` | Phase 1 complete | — | Branch cleanup skill. No injection, no external calls, confirms before remote deletes. Minor adaptation needed: protected branch list (keep main only). |
| `git/pr` | alirezarezvani/claude-skills `.claude/commands/git/pr.md` | Phase 1 complete | — | PR creation via gh CLI. Needs CI gate dependency removed and adapted to STD04 review criteria. |
| `c-level-advisor/board-meeting` | alirezarezvani/claude-skills `c-level-advisor/board-meeting/SKILL.md` | **Approved with caveat** | `/ctx` (substitute for rejected `context-engine`) | 6-phase multi-agent board deliberation. Reads `memory/company-context.md` (load via `/ctx` first), writes structured meeting notes to `memory/board-meetings/` (project-local). Same write pattern as `decision-logger` (approved). **Caveat**: run `/ctx load` before invoking; add `memory/board-meetings/` to `.gitignore` to keep board transcripts out of version control. | Joshua Alexander Clement | 2026-03-13 |
| `c-level-advisor/competitive-intel` | alirezarezvani/claude-skills `c-level-advisor/competitive-intel/SKILL.md` | **Approved** | — | External WebSearch intelligence gathering (Crunchbase, LinkedIn, G2). No local file writes, no governance access. **Verified**: uses Claude's built-in WebSearch tool only — no custom network scripts, no API keys, no credential access. Low-Medium risk. | Joshua Alexander Clement | 2026-03-13 |
| `c-level-advisor/founder-coach` | alirezarezvani/claude-skills `c-level-advisor/founder-coach/SKILL.md` | Phase 1 complete | — | Pure coaching framework. No file I/O, no network, no governance access. Low risk. |
| `c-level-advisor/change-management` | alirezarezvani/claude-skills `c-level-advisor/change-management/SKILL.md` | Phase 1 complete | — | ADKAR-based change playbook. Pure framework skill. Low risk. |
| `c-level-advisor/culture-architect` | alirezarezvani/claude-skills `c-level-advisor/culture-architect/SKILL.md` | Phase 1 complete | — | Culture health assessment and values framework. Pure framework skill. Low risk. |
| `c-level-advisor/internal-narrative` | alirezarezvani/claude-skills `c-level-advisor/internal-narrative/SKILL.md` | Phase 1 complete | — | Internal communications strategy framework. Includes contradiction detection. Low risk. |
| `marketing-skill/ai-seo` | alirezarezvani/claude-skills `marketing-skill/ai-seo/SKILL.md` | Phase 1 complete | — | AI-era SEO strategy framework. Pure prompt. Low risk. |
| `marketing-skill/brand-guidelines` | alirezarezvani/claude-skills `marketing-skill/brand-guidelines/SKILL.md` | Phase 1 complete | — | Brand identity framework. Optionally reads `.claude/product-marketing-context.md` (project-relative, read-only). Low risk. |
| `marketing-skill/content-creator` | alirezarezvani/claude-skills `marketing-skill/content-creator/SKILL.md` | Phase 1 complete | — | Deprecated routing wrapper. Minimal attack surface. Low risk. |
| `marketing-skill/marketing-ideas` | alirezarezvani/claude-skills `marketing-skill/marketing-ideas/SKILL.md` | Phase 1 complete | — | Idea generation framework. Optionally reads `.claude/product-marketing-context.md`. Low risk. |
| `marketing-skill/marketing-psychology` | alirezarezvani/claude-skills `marketing-skill/marketing-psychology/SKILL.md` | Phase 1 complete | — | Mental models and behavioral frameworks. Optionally reads `marketing-context.md`. Low risk. |
| `marketing-skill/marketing-strategy-pmm` | alirezarezvani/claude-skills `marketing-skill/marketing-strategy-pmm/SKILL.md` | Phase 1 complete | — | Product marketing strategy framework. Pure prompt. Low risk. |
| `marketing-skill/paywall-upgrade-cro` | alirezarezvani/claude-skills `marketing-skill/paywall-upgrade-cro/SKILL.md` | Phase 1 complete | — | Paywall conversion optimization. Optionally reads `.claude/product-marketing-context.md`. Low risk. |
| `marketing-skill/popup-cro` | alirezarezvani/claude-skills `marketing-skill/popup-cro/SKILL.md` | Phase 1 complete | — | Popup conversion optimization. Optionally reads `.claude/product-marketing-context.md`. Low risk. |
| `marketing-skill/social-content` | alirezarezvani/claude-skills `marketing-skill/social-content/SKILL.md` | Phase 1 complete | — | Social media content framework. Optionally reads `.claude/product-marketing-context.md`. Low risk. |
| `engineering-team/email-template-builder` | alirezarezvani/claude-skills `engineering-team/email-template-builder/SKILL.md` | Phase 1 complete | — | React Email template generation assistant. No file I/O, no network. Low risk. |
| `engineering-team/stripe-integration-expert` | alirezarezvani/claude-skills `engineering-team/stripe-integration-expert/SKILL.md` | Phase 1 complete | — | Stripe billing integration reference skill. No file I/O, no network. Low risk. |
| `engineering-team/playwright-pro` | alirezarezvani/claude-skills | **Approved — moved to §2** | — | — |
| `engineering/api-test-suite-builder` | alirezarezvani/claude-skills `engineering/api-test-suite-builder/SKILL.md` | Phase 1 complete | — | API test generation assistant. Bash examples are user templates only. Low risk. |
| `engineering/database-schema-designer` | alirezarezvani/claude-skills `engineering/database-schema-designer/SKILL.md` | Phase 1 complete | — | Relational schema design assistant. Code examples only. Low risk. |
| `engineering/pr-review-expert` | alirezarezvani/claude-skills `engineering/pr-review-expert/SKILL.md` | Phase 1 complete | — | Structured PR review framework. Bash commands are manual user templates. Low risk. |
| `c-level-advisor/agent-protocol` | alirezarezvani/claude-skills `c-level-advisor/agent-protocol/SKILL.md` | Phase 1 complete | — | Inter-agent communication protocol: invocation syntax, loop prevention (max depth 2), isolation rules. Pure definition — no file I/O, no network. Low risk. |
| `c-level-advisor/board-deck-builder` | alirezarezvani/claude-skills `c-level-advisor/board-deck-builder/SKILL.md` | Phase 1 complete | — | Board and investor deck builder. No file I/O, no network. Low risk. |
| `c-level-advisor/company-os` | alirezarezvani/claude-skills `c-level-advisor/company-os/SKILL.md` | Phase 1 complete | — | Company operating system framework (EOS, OKRs, Scaling Up). No file I/O, no network. Low risk. |
| `c-level-advisor/intl-expansion` | alirezarezvani/claude-skills `c-level-advisor/intl-expansion/SKILL.md` | Phase 1 complete | — | International market expansion framework. No file I/O, no network. Low risk. |
| `c-level-advisor/ma-playbook` | alirezarezvani/claude-skills `c-level-advisor/ma-playbook/SKILL.md` | Phase 1 complete | — | M&A strategy for both sides. No file I/O, no network. Low risk. |
| `business-growth/contract-and-proposal-writer` | alirezarezvani/claude-skills `business-growth/contract-and-proposal-writer/SKILL.md` | Phase 1 complete | — | Legal document generator for freelance contracts, SOWs, NDAs, MSAs. No autonomous file I/O, no network. Includes legal counsel disclaimer. Low risk. |

---

### Script-Backed Skills — Business Growth

| Skill | Source | Status | Depends On | Notes |
|---|---|---|---|---|
| `business-growth/customer-success-manager` | alirezarezvani/claude-skills | Phase 1 complete | — | 3 stdlib Python tools: churn risk, expansion scoring, health score. No network, no external deps, no file writes. Low risk. |
| `business-growth/revenue-operations` | alirezarezvani/claude-skills | Phase 1 complete | — | 3 stdlib Python tools: forecast accuracy, GTM efficiency, pipeline analysis. Low risk. |
| `business-growth/sales-engineer` | alirezarezvani/claude-skills | Phase 1 complete | — | 3 stdlib Python tools: competitive matrix, POC planner, RFP response analyzer. Low risk. |

---

### Script-Backed Skills — C-Level Advisors

All c-suite advisor scripts are pure stdlib Python analytics tools. SKILL.md behaviours reference `memory/company-context.md` for context loading — substitute `/ctx` for the rejected `context-engine`.

| Skill | Source | Status | Depends On | Notes |
|---|---|---|---|---|
| `c-level-advisor/ceo-advisor` | alirezarezvani/claude-skills | **Approved with caveat** | `/ctx` (for context loading) | 2 stdlib Python tools: financial scenario analyzer, strategy analyzer. SKILL.md uses `[INVOKE:role\|question]` cross-role invocation pattern. **Verified**: `[INVOKE:...]` is advisory guidance to Claude (not a subprocess call); no automated agent spawning. **Caveat**: dependent skills invoked via `[INVOKE:...]` must themselves be individually approved before use in that capacity. | Joshua Alexander Clement | 2026-03-13 |
| `c-level-advisor/cfo-advisor` | alirezarezvani/claude-skills | Phase 1 complete | `/ctx` | 3 stdlib Python tools: burn rate, fundraising model, unit economics. Low risk. |
| `c-level-advisor/chro-advisor` | alirezarezvani/claude-skills | Phase 1 complete | `/ctx` | 2 stdlib Python tools: comp benchmarker, hiring plan modeler. Low risk. |
| `c-level-advisor/ciso-advisor` | alirezarezvani/claude-skills | Phase 1 complete | `/ctx` | 2 stdlib Python tools: compliance tracker, risk quantifier (ALE/FAIR). Low risk. |
| `c-level-advisor/cmo-advisor` | alirezarezvani/claude-skills | Phase 1 complete | `/ctx` | 2 stdlib Python tools: growth model simulator, marketing budget modeler. Low risk. |
| `c-level-advisor/coo-advisor` | alirezarezvani/claude-skills | Phase 1 complete | `/ctx` | 2 stdlib Python tools: OKR tracker, ops efficiency analyzer. Low risk. |
| `c-level-advisor/cpo-advisor` | alirezarezvani/claude-skills | Phase 1 complete | `/ctx` | 2 stdlib Python tools: PMF scorer, portfolio analyzer. Low risk. |
| `c-level-advisor/cro-advisor` | alirezarezvani/claude-skills | Phase 1 complete | `/ctx` | 2 stdlib Python tools: churn analyzer, revenue forecast model. Low risk. |
| `c-level-advisor/cto-advisor` | alirezarezvani/claude-skills | Phase 1 complete | `/ctx` | 2 stdlib Python tools: tech debt analyzer, team scaling calculator. Low risk. |
| `c-level-advisor/decision-logger` | alirezarezvani/claude-skills | **Approved with caveat** | `board-meeting` + `/ctx` | 1 stdlib Python tool: decision tracker CLI. **Verified**: `decision_tracker.py` is read-only — reads `memory/board-meetings/decisions.md`, generates reports, no writes anywhere in script. SKILL.md instructs Claude to write approved decisions to `memory/board-meetings/` (project-local, not `~/.claude/`). **Caveat**: add `memory/board-meetings/` to `.gitignore` before use to prevent decision transcripts from entering version control. | Joshua Alexander Clement | 2026-03-13 |
| `c-level-advisor/executive-mentor` | alirezarezvani/claude-skills | Phase 1 complete | — | 2 stdlib Python tools: decision matrix scorer, stakeholder mapper. Pure prompt advisor. Low risk. |
| `c-level-advisor/org-health-diagnostic` | alirezarezvani/claude-skills | Phase 1 complete | `/ctx` | 1 stdlib Python tool: health scorer (8 dimensions). Low risk. |
| `c-level-advisor/scenario-war-room` | alirezarezvani/claude-skills | Phase 1 complete | — | 1 stdlib Python tool: scenario modeler with cascade analysis. Low risk. |
| `c-level-advisor/strategic-alignment` | alirezarezvani/claude-skills | Phase 1 complete | — | 1 stdlib Python tool: alignment checker. Low risk. |

---

### Script-Backed Skills — Engineering

| Skill | Source | Status | Depends On | Notes |
|---|---|---|---|---|
| `engineering/agent-workflow-designer` | alirezarezvani/claude-skills | **Approved** | — | 1 stdlib Python tool: workflow scaffolder. **Verified**: `workflow_scaffolder.py` generates JSON skeleton config files for workflow patterns (sequential, parallel, router, orchestrator, evaluator) — writes to local project or stdout only. No subprocess, no network. Agent invocation patterns in SKILL.md are advisory design guidance, not automated spawning. Low risk. | Joshua Alexander Clement | 2026-03-13 |
| `engineering/api-design-reviewer` | alirezarezvani/claude-skills | **Approved** | — | 3 stdlib Python tools: api linter, api scorecard, breaking change detector. **Verified**: `api_linter.py` imports `urllib.parse` for URL string parsing only — no `urllib.request`, no network calls. All analysis is local OpenAPI spec linting via regex/JSON. No subprocess, no file writes (outputs to stdout). Low risk. | Joshua Alexander Clement | 2026-03-13 |
| `engineering/changelog-generator` | alirezarezvani/claude-skills | Phase 1 complete | — | 2 stdlib Python tools: commit linter, changelog generator. Writes `CHANGELOG.md` to project (by design). Low risk. |
| `engineering/ci-cd-pipeline-builder` | alirezarezvani/claude-skills | Phase 1 complete | — | 2 stdlib Python tools: pipeline generator, stack detector. Writes pipeline config files to project (by design). Low risk. |
| `engineering/codebase-onboarding` | alirezarezvani/claude-skills | Phase 1 complete | — | 1 stdlib Python tool: codebase analyzer. Reads project structure, generates onboarding docs. Low risk. |
| `engineering/dependency-auditor` | alirezarezvani/claude-skills | **Approved** | — | 3 stdlib Python tools: dep scanner, license checker, upgrade planner. **Verified**: `dep_scanner.py` imports `subprocess` but never calls it — the import is vestigial. Uses a **built-in hardcoded CVE/license database** (no live network calls). Parses local dependency files (package.json, requirements.txt, go.mod, Cargo.toml, Gemfile). Report written to file or stdout. Low risk. | Joshua Alexander Clement | 2026-03-13 |
| `engineering/env-secrets-manager` | alirezarezvani/claude-skills | **Approved with caveat** | — | 1 stdlib Python tool: env auditor. Scans `.env` files and project for leaked secrets. **Caveat**: output must go to a gitignored file (`registry/audits/secrets-YYYY-MM-DD.md`), never stdout. Terminal must not log session output when running this skill. | Joshua Alexander Clement | 2026-03-13 |
| `engineering/git-worktree-manager` | alirezarezvani/claude-skills | Phase 1 complete | — | 2 stdlib Python tools: worktree manager, worktree cleanup. Subprocess runs `git` commands via list args (no shell=True). Writes `.worktree-ports.json` to worktree dirs. Low risk. |
| `engineering/interview-system-designer` | alirezarezvani/claude-skills | Phase 1 complete | — | 3 stdlib Python tools: hiring calibrator, loop designer, question bank generator + 1 in scripts/. Pure analytics. Low risk. |
| `engineering/mcp-server-builder` | alirezarezvani/claude-skills | Phase 1 complete | — | 1 stdlib Python tool: openapi_to_mcp converter. Writes MCP manifest and scaffold files to user-specified output dir. PyYAML used with `yaml.safe_load()` (optional/guarded). Low risk. |
| `engineering/migration-architect` | alirezarezvani/claude-skills | Phase 1 complete | — | Scripts include rollback generator (writes migration files to project). Pure stdlib. Low risk. |
| `engineering/monorepo-navigator` | alirezarezvani/claude-skills | Phase 1 complete | — | SKILL.md references CLAUDE.md only in guidance context (not writing to it). Reads monorepo structure. Low risk. |
| `engineering/observability-designer` | alirezarezvani/claude-skills | Phase 1 complete | — | 1 stdlib Python tool: alert optimizer. Pure computation. Low risk. |
| `engineering/performance-profiler` | alirezarezvani/claude-skills | **Approved** | — | 1 stdlib Python tool: `performance_profiler.py`. **Verified**: local directory file-size analyzer — walks files, counts deps from local manifests, estimates bundle weight. No subprocess, no network, no shell. k6/Artillery references in SKILL.md are guidance for human follow-up, not automated calls. Low risk. | Joshua Alexander Clement | 2026-03-13 |
| `engineering/runbook-generator` | alirezarezvani/claude-skills | Phase 1 complete | — | 1 stdlib Python tool: runbook generator. Writes runbook docs to user-specified path. Low risk. |
| `engineering/skill-security-auditor` | alirezarezvani/claude-skills | **Approved with caveat** | — | 1 stdlib Python tool: `skill_security_auditor.py` (1050 lines). **Verified**: all `os.system`, `exec`, `shell=True` strings in the script are regex pattern-match targets — not live calls. Local filesystem scan only; when given a URL, uses `git clone --depth 1 <url> <tmpdir>` with list args (no `shell=True`). Cleans up temp dir in `finally` block. No runtime file writes to project. **Caveat**: only run against SKILL.md files from trusted or vetted sources — scanner reads file content and the regex engine could have edge-case behavior on deliberately crafted input. | Joshua Alexander Clement | 2026-03-13 |
| `engineering/skill-tester` | alirezarezvani/claude-skills | **Approved with caveat** | — | 3 stdlib Python tools: `script_tester.py` (executes Python scripts), `skill_validator.py`, `quality_scorer.py`. PyYAML guarded. **Verified**: `script_tester.py` has no built-in sandbox — `import tempfile` is unused; scripts run via `subprocess.run(cwd=script_path.parent)` with no path restrictions. Docker is the only isolation boundary. **Static-mode use** (AST checks: syntax, imports, argparse, main guard) is safe in-session. **Execution-mode use** requires Docker per `docs/phase4-sandbox.md §4.1`. Phase 4 Docker sandbox passed 2026-03-14 (--network none, --read-only, --tmpfs /tmp, --cap-drop ALL). Canary confirmed writes blocked outside /tmp/. | Joshua Alexander Clement | 2026-03-14 |
| `engineering/tech-debt-tracker` | alirezarezvani/claude-skills | Phase 1 complete | — | 3 stdlib Python tools: debt scanner, prioritizer, dashboard. Reads codebase, generates reports. Low risk. |

---

### Script-Backed Skills — Engineering Team

| Skill | Source | Status | Depends On | Notes |
|---|---|---|---|---|
| `engineering-team/aws-solution-architect` | alirezarezvani/claude-skills | Phase 1 complete | — | Generates CloudFormation/CDK/Terraform templates. No runtime AWS access. Low risk. |
| `engineering-team/code-reviewer` | alirezarezvani/claude-skills | Phase 1 complete | — | 2 stdlib Python tools: pr_analyzer.py (subprocess for git diff/log via list args), review_report_generator.py. Low risk. |
| `engineering-team/google-workspace-cli` | alirezarezvani/claude-skills | **Rejected — replaced** | — | Direct `shell=True` execution with live Google OAuth. Replaced by compliant `/gws` skill (local-first: generates reviewed command scripts, no live shell execution in Claude session). See rejected-skill-design-intents.md §5. |
| `engineering-team/incident-commander` | alirezarezvani/claude-skills | Phase 1 complete | — | Pure incident response framework. No file I/O, no network, no subprocess. Low risk. |
| `engineering-team/ms365-tenant-manager` | alirezarezvani/claude-skills | **Rejected — replaced** | — | Direct PowerShell subprocess execution with live M365 credentials. Replaced by compliant `/m365` skill (local-first: generates reviewed PowerShell scripts as files, no execution in Claude session). See rejected-skill-design-intents.md §6. |
| `engineering-team/senior-architect` | alirezarezvani/claude-skills | Phase 1 complete | — | Architecture design skill. Reads project structure. Low risk. |
| `engineering-team/senior-backend` | alirezarezvani/claude-skills | **Approved with caveat** | — | Scripts include `api_scaffolder.py` (writes project files to user-specified output dir), `api_load_tester.py` (GET/POST/PUT/PATCH/DELETE to user-specified `--url`), `database_migration_tool.py` (writes migration files). **Verified**: no `shell=True`, no credential harvesting, `--no-verify-ssl` flag noted. **Caveat**: `api_load_tester.py` sends real HTTP traffic — only use against endpoints you own or have explicit authorization to load-test. | Joshua Alexander Clement | 2026-03-13 |
| `engineering-team/senior-computer-vision` | alirezarezvani/claude-skills | Phase 1 complete | — | Scripts: `dataset_pipeline_builder.py` (reads/copies dataset files), `vision_model_trainer.py` (PyYAML guarded with safe_load). No runtime albumentations dependency (config generator only). Low-Medium risk. |
| `engineering-team/senior-data-engineer` | alirezarezvani/claude-skills | Phase 1 complete | — | `pipeline_orchestrator.py`: prefect/dagster/pandas imports are inside template string literals (generated code output, not runtime deps). PyYAML guarded. Low risk. |
| `engineering-team/senior-data-scientist` | alirezarezvani/claude-skills | Phase 1 complete | — | Analytics/ML guidance skill. No external deps in scripts. Low risk. |
| `engineering-team/senior-devops` | alirezarezvani/claude-skills | Phase 1 complete | — | Generates CI/CD workflows, Kubernetes manifests, IaC templates. Low risk. |
| `engineering-team/senior-frontend` | alirezarezvani/claude-skills | Phase 1 complete | — | React/Next.js scaffolding. Code generation only. Low risk. |
| `engineering-team/senior-fullstack` | alirezarezvani/claude-skills | Phase 1 complete | — | `project_scaffolder.py`: fastapi/sqlalchemy/django/react imports are inside template string literals (generated code output). Low risk. |
| `engineering-team/senior-ml-engineer` | alirezarezvani/claude-skills | **Approved with caveat** | — | **Verified**: `model_deployment_pipeline.py` is a stub — `_execute()` returns `{'success': True}` with no real implementation. No Docker, no kubectl, no API calls in the script. SKILL.md guidance references Docker/kubectl as human-side setup steps. **Caveat**: if script is later replaced with a real implementation, re-vet before use. Low risk (current stub state). | Joshua Alexander Clement | 2026-03-13 |
| `engineering-team/senior-prompt-engineer` | alirezarezvani/claude-skills | Phase 1 complete | — | Pure prompt engineering framework. Low risk. |
| `engineering-team/senior-qa` | alirezarezvani/claude-skills | Phase 1 complete | — | 2 stdlib Python tools: `e2e_test_scaffolder.py` (writes test files to project), `test_suite_generator.py`. Low risk. |
| `engineering-team/senior-secops` | alirezarezvani/claude-skills | **Approved** | — | 1 stdlib Python tool: `security_scanner.py` (472 lines). **Verified**: `'Subprocess with shell=True'` in the script is a **regex detection target string**, not live usage. Scanner reads source files and applies regex matching — stdlib only (os, sys, json, re, argparse, pathlib, dataclasses, datetime). No network, no subprocess calls at runtime, no file writes. Low risk. | Joshua Alexander Clement | 2026-03-13 |
| `engineering-team/senior-security` | alirezarezvani/claude-skills | Phase 1 complete | — | Threat modeling, STRIDE, vulnerability assessment. Offline analysis only. Low risk. |
| `engineering-team/tdd-guide` | alirezarezvani/claude-skills | Phase 1 complete | — | 5 stdlib Python tools: framework adapter, metrics calculator, output formatter, tdd workflow, test generator. Low risk. |
| `engineering-team/tech-stack-evaluator` | alirezarezvani/claude-skills | Phase 1 complete | — | 7 stdlib Python tools: ecosystem analyzer, format detector, migration analyzer, report generator, security assessor, stack comparator, TCO calculator. Low risk. |

---

### Script-Backed Skills — Finance

| Skill | Source | Status | Depends On | Notes |
|---|---|---|---|---|
| `finance/financial-analyst` | alirezarezvani/claude-skills | Phase 1 complete | — | 4 stdlib Python tools: budget variance analyzer, DCF valuation, forecast builder, ratio calculator. Low risk. |
| `finance/saas-metrics-coach` | alirezarezvani/claude-skills | Phase 1 complete | — | 3 stdlib Python tools: metrics calculator, quick ratio calculator, unit economics simulator. Low risk. |

---

### Script-Backed Skills — Marketing

All marketing skill Python scripts are stdlib-only analytics tools. No network calls except where noted. Optional context reads use project-relative paths.

| Skill | Source | Status | Depends On | Notes |
|---|---|---|---|---|
| `marketing-skill/ab-test-setup` | alirezarezvani/claude-skills | Phase 1 complete | — | 1 stdlib Python tool: sample size calculator. Low risk. |
| `marketing-skill/ad-creative` | alirezarezvani/claude-skills | Phase 1 complete | — | 1 stdlib Python tool: ad copy validator. Low risk. |
| `marketing-skill/analytics-tracking` | alirezarezvani/claude-skills | Phase 1 complete | — | 1 stdlib Python tool: tracking plan generator. Optionally reads `marketing-context.md`. Low risk. |
| `marketing-skill/app-store-optimization` | alirezarezvani/claude-skills | Phase 1 complete | — | 8 stdlib Python tools: aso scorer, keyword analyzer, competitor analyzer, review analyzer (sentiment on input data, no network), metadata optimizer, launch checklist, localization helper, ab test planner. Low risk. |
| `marketing-skill/campaign-analytics` | alirezarezvani/claude-skills | Phase 1 complete | — | 3 stdlib Python tools: attribution analyzer, campaign ROI calculator, funnel analyzer. Low risk. |
| `marketing-skill/churn-prevention` | alirezarezvani/claude-skills | Phase 1 complete | — | 1 stdlib Python tool: churn impact calculator. Low risk. |
| `marketing-skill/cold-email` | alirezarezvani/claude-skills | Phase 1 complete | — | 1 stdlib Python tool: email sequence analyzer. Low risk. |
| `marketing-skill/competitor-alternatives` | alirezarezvani/claude-skills | Phase 1 complete | — | 1 stdlib Python tool: comparison matrix builder. Optionally reads `marketing-context.md`. Low risk. |
| `marketing-skill/content-humanizer` | alirezarezvani/claude-skills | Phase 1 complete | — | 1 stdlib Python tool: humanizer scorer. Low risk. |
| `marketing-skill/content-production` | alirezarezvani/claude-skills | Phase 1 complete | — | 3 stdlib Python tools: brand voice analyzer, content scorer, SEO optimizer. Low risk. |
| `marketing-skill/content-strategy` | alirezarezvani/claude-skills | Phase 1 complete | — | 1 stdlib Python tool: topic cluster mapper. Optionally reads `marketing-context.md`. Low risk. |
| `marketing-skill/copy-editing` | alirezarezvani/claude-skills | Phase 1 complete | — | 1 stdlib Python tool: readability scorer. Low risk. |
| `marketing-skill/copywriting` | alirezarezvani/claude-skills | Phase 1 complete | — | 1 stdlib Python tool: headline scorer. Low risk. |
| `marketing-skill/email-sequence` | alirezarezvani/claude-skills | Phase 1 complete | — | 1 stdlib Python tool: sequence analyzer. References platform integrations as user-side setup. Low risk. |
| `marketing-skill/form-cro` | alirezarezvani/claude-skills | Phase 1 complete | — | 1 stdlib Python tool: form field analyzer. Low risk. |
| `marketing-skill/free-tool-strategy` | alirezarezvani/claude-skills | Phase 1 complete | — | 1 stdlib Python tool: tool ROI estimator. Low risk. |
| `marketing-skill/launch-strategy` | alirezarezvani/claude-skills | Phase 1 complete | — | 1 stdlib Python tool: launch readiness scorer. Optionally reads `marketing-context.md`. Low risk. |
| `marketing-skill/marketing-context` | alirezarezvani/claude-skills | **Approved with caveat** | — | 1 stdlib Python tool: context validator. **Verified**: `context_validator.py` is read-only — reads a local markdown file, scores marketing context sections, no writes, no network. SKILL.md directs Claude to maintain `.agents/marketing-context.md` (project-relative path, not `~/.claude/`). **Caveat**: add `.agents/` to `.gitignore` if context file contains proprietary data. Low-Medium risk. | Joshua Alexander Clement | 2026-03-13 |
| `marketing-skill/marketing-demand-acquisition` | alirezarezvani/claude-skills | Phase 1 complete | — | 1 stdlib Python tool: CAC calculator. Low risk. |
| `marketing-skill/marketing-ops` | alirezarezvani/claude-skills | Phase 1 complete | — | 1 stdlib Python tool: campaign tracker. Low risk. |
| `marketing-skill/onboarding-cro` | alirezarezvani/claude-skills | Phase 1 complete | — | 1 stdlib Python tool: activation funnel analyzer. Low risk. |
| `marketing-skill/page-cro` | alirezarezvani/claude-skills | **Approved with caveat** | — | 1 stdlib Python tool: `conversion_audit.py`. **Verified**: HTTP GET via `urllib.request.urlopen(args.url, timeout=10)` — fetches HTML for local analysis via `HTMLParser`. No writes, no shell, no credential access. **Caveat**: only run against URLs you own or have explicit permission to audit. | Joshua Alexander Clement | 2026-03-13 |
| `marketing-skill/paid-ads` | alirezarezvani/claude-skills | Phase 1 complete | — | 1 stdlib Python tool: ROAS calculator. Low risk. |
| `marketing-skill/pricing-strategy` | alirezarezvani/claude-skills | Phase 1 complete | — | 1 stdlib Python tool: pricing modeler. Low risk. |
| `marketing-skill/programmatic-seo` | alirezarezvani/claude-skills | Phase 1 complete | — | 1 stdlib Python tool: URL pattern generator. Low risk. |
| `marketing-skill/prompt-engineer-toolkit` | alirezarezvani/claude-skills | **Approved with caveat** | — | 2 stdlib Python tools: `prompt_tester.py`, `prompt_versioner.py`. **Verified**: `--runner-cmd` is an optional feature; uses `shlex.split(cmd)` then `subprocess.run(parts, ...)` — no `shell=True`. Argument injection possible (not command injection) if `--runner-cmd` template contains adversarial `{prompt}` values. **Caveat**: `--runner-cmd` should reference fixed CLI tools with known argument structure; review the formatted command string before allowing execution. Low-Medium risk. | Joshua Alexander Clement | 2026-03-13 |
| `marketing-skill/referral-program` | alirezarezvani/claude-skills | Phase 1 complete | — | 1 stdlib Python tool: referral ROI calculator. Low risk. |
| `marketing-skill/schema-markup` | alirezarezvani/claude-skills | Phase 1 complete | — | 1 stdlib Python tool: schema validator. Low risk. |
| `marketing-skill/seo-audit` | alirezarezvani/claude-skills | **Approved with caveat** | — | 1 stdlib Python tool: `seo_checker.py`. **Verified**: HTTP GET via `urllib.request.urlopen(args.url)` for HTML analysis. Same pattern as `page-cro`. No writes, no shell. **Caveat**: only audit URLs you own or have explicit permission to access. | Joshua Alexander Clement | 2026-03-13 |
| `marketing-skill/signup-flow-cro` | alirezarezvani/claude-skills | Phase 1 complete | — | 1 stdlib Python tool: funnel drop analyzer. Low risk. |
| `marketing-skill/site-architecture` | alirezarezvani/claude-skills | **Approved with caveat** | — | 1 stdlib Python tool: `sitemap_analyzer.py`. **Verified**: HTTP GET via `urllib.request.urlopen(source, timeout=10)` to fetch sitemap XML; parses via stdlib `xml.etree.ElementTree`. No writes, no shell. **Caveat**: only analyze sitemaps from domains you own or have explicit permission to crawl. | Joshua Alexander Clement | 2026-03-13 |
| `marketing-skill/social-media-analyzer` | alirezarezvani/claude-skills | Phase 1 complete | — | 2 stdlib Python tools: analyze performance, calculate metrics. Accepts JSON input data. Low risk. |
| `marketing-skill/social-media-manager` | alirezarezvani/claude-skills | Phase 1 complete | — | 1 stdlib Python tool: social calendar generator. Optionally reads `marketing-context.md`. Low risk. |
| `marketing-skill/x-twitter-growth` | alirezarezvani/claude-skills | **Approved with caveat** | — | 5 stdlib Python tools: profile auditor, competitor analyzer, tweet composer, content planner, growth tracker. **Verified**: `profile_auditor.py` imports `argparse, json, re, sys, dataclasses` only — no network imports; analyzes provided profile data locally. Web search references in SKILL.md are guidance for manual data collection. **Caveat**: no live Twitter/X API automation — provide profile data manually as JSON input. | Joshua Alexander Clement | 2026-03-13 |

---

### Script-Backed Skills — Product Team

| Skill | Source | Status | Depends On | Notes |
|---|---|---|---|---|
| `product-team/agile-product-owner` | alirezarezvani/claude-skills | Phase 1 complete | — | 1 stdlib Python tool: user story generator. Low risk. |
| `product-team/competitive-teardown` | alirezarezvani/claude-skills | **Approved with caveat** | — | 1 stdlib Python tool: `competitive_matrix_builder.py`. **Verified**: reads local `competitors.json`, performs pure math/analysis, optional local file output. No network, no subprocess. iTunes Search API and Twitter/X API v2 references in SKILL.md are manual data-sourcing guidance only — not automated calls. **Caveat**: populate competitors.json manually; do not automate API calls without operator setup and rate-limit review. | Joshua Alexander Clement | 2026-03-13 |
| `product-team/experiment-designer` | alirezarezvani/claude-skills | Phase 1 complete | — | 1 stdlib Python tool: sample size calculator. Low risk. |
| `product-team/landing-page-generator` | alirezarezvani/claude-skills | Phase 1 complete | — | 1 stdlib Python tool: `landing_page_scaffolder.py`. Generates TSX/React component code as text output. Low risk. |
| `product-team/product-analytics` | alirezarezvani/claude-skills | Phase 1 complete | — | 1 stdlib Python tool: metrics calculator. Low risk. |
| `product-team/product-discovery` | alirezarezvani/claude-skills | Phase 1 complete | — | 1 stdlib Python tool: assumption mapper. Low risk. |
| `product-team/product-manager-toolkit` | alirezarezvani/claude-skills | Phase 1 complete | — | 2 stdlib Python tools: customer interview analyzer, RICE prioritizer. Low risk. |
| `product-team/product-strategist` | alirezarezvani/claude-skills | Phase 1 complete | — | 1 stdlib Python tool: OKR cascade generator. Low risk. |
| `product-team/roadmap-communicator` | alirezarezvani/claude-skills | Phase 1 complete | — | 1 stdlib Python tool: changelog generator. Writes to project changelog (by design). Low risk. |
| `product-team/saas-scaffolder` | alirezarezvani/claude-skills | Phase 1 complete | — | 1 stdlib Python tool: `project_bootstrapper.py`. Generates project structure and files. Low risk. |
| `product-team/ui-design-system` | alirezarezvani/claude-skills | Phase 1 complete | — | 1 stdlib Python tool: design token generator. Low risk. |
| `product-team/ux-researcher-designer` | alirezarezvani/claude-skills | Phase 1 complete | — | 1 stdlib Python tool: persona generator. Low risk. |

---

### Script-Backed Skills — Project Management

| Skill | Source | Status | Depends On | Notes |
|---|---|---|---|---|
| `project-management/atlassian-admin` | alirezarezvani/claude-skills | **Rejected — replaced** | — | Direct Atlassian REST API writes (user provisioning, permission changes) via live MCP. Replaced by compliant `/atlassian` skill (local-first staging). See rejected-skill-design-intents.md §7. |
| `project-management/atlassian-templates` | alirezarezvani/claude-skills | **Rejected — replaced** | — | Direct Confluence MCP writes (`confluence_create_page`, `confluence_update_page`). Replaced by compliant `/atlassian` skill. See rejected-skill-design-intents.md §7. |
| `project-management/confluence-expert` | alirezarezvani/claude-skills | **Rejected — replaced** | — | Direct Confluence MCP writes + DELETE operations (`create_space`, `create_page`, `update_page`, `delete_page`). Replaced by compliant `/atlassian` skill. See rejected-skill-design-intents.md §7. |
| `project-management/jira-expert` | alirezarezvani/claude-skills | **Rejected — replaced** | — | Direct Jira MCP writes + bulk operations (`create_project`, `update_issue`, bulk ops). Replaced by compliant `/atlassian` skill. See rejected-skill-design-intents.md §7. |
| `project-management/scrum-master` | alirezarezvani/claude-skills | Phase 1 complete | — | 3 stdlib Python tools: retrospective analyzer, sprint health scorer, velocity analyzer. Low risk. |
| `project-management/senior-pm` | alirezarezvani/claude-skills | Phase 1 complete | — | 3 stdlib Python tools: project health dashboard, resource capacity planner, risk matrix analyzer. Low risk. |

---

### Script-Backed Skills — Regulatory / Quality Management

All ra-qm-team Python scripts are stdlib-only compliance and audit tools. No network calls, no file writes outside project directories.

| Skill | Source | Status | Depends On | Notes |
|---|---|---|---|---|
| `ra-qm-team/capa-officer` | alirezarezvani/claude-skills | Phase 1 complete | — | 1 stdlib Python tool: CAPA tracker. Low risk. |
| `ra-qm-team/fda-consultant-specialist` | alirezarezvani/claude-skills | Phase 1 complete | — | 3 stdlib Python tools: FDA submission tracker, HIPAA risk assessment, QSR compliance checker. Low risk. |
| `ra-qm-team/gdpr-dsgvo-expert` | alirezarezvani/claude-skills | Phase 1 complete | — | 3 stdlib Python tools: data subject rights tracker, DPIA generator, GDPR compliance checker. Low risk. |
| `ra-qm-team/information-security-manager-iso27001` | alirezarezvani/claude-skills | Phase 1 complete | — | 2 stdlib Python tools: compliance checker, risk assessment. Low risk. |
| `ra-qm-team/isms-audit-expert` | alirezarezvani/claude-skills | Phase 1 complete | — | 1 stdlib Python tool: ISMS audit scheduler. Low risk. |
| `ra-qm-team/mdr-745-specialist` | alirezarezvani/claude-skills | Phase 1 complete | — | 1 stdlib Python tool: MDR gap analyzer. Low risk. |
| `ra-qm-team/qms-audit-expert` | alirezarezvani/claude-skills | Phase 1 complete | — | 1 stdlib Python tool: audit schedule optimizer. Low risk. |
| `ra-qm-team/quality-documentation-manager` | alirezarezvani/claude-skills | Phase 1 complete | — | 1 stdlib Python tool: document validator. Low risk. |
| `ra-qm-team/quality-manager-qmr` | alirezarezvani/claude-skills | Phase 1 complete | — | 1 stdlib Python tool: management review tracker. Low risk. |
| `ra-qm-team/quality-manager-qms-iso13485` | alirezarezvani/claude-skills | Phase 1 complete | — | 1 stdlib Python tool: QMS audit checklist. Low risk. |
| `ra-qm-team/regulatory-affairs-head` | alirezarezvani/claude-skills | Phase 1 complete | — | 1 stdlib Python tool: regulatory tracker. Low risk. |
| `ra-qm-team/risk-management-specialist` | alirezarezvani/claude-skills | Phase 1 complete | — | 1 stdlib Python tool: risk matrix calculator. Low risk. |

> Skills from unverified external sources (community repos, third-party collections) must complete the full vetting workflow in `docs/skill-vetting-workflow.md` before being added here. The source being popular or widely used is not sufficient justification.

---

## 6. Rejected Skills

Skills that were reviewed and not approved, with the reason:

| Skill | Source | Reason Rejected | Date | Reviewed By |
|---|---|---|---|---|
| `git/cm` | github.com/alirezarezvani/claude-skills `.claude/commands/git/cm.md` | Explicitly instructs "Never add AI attribution strings to commits" — direct conflict with STD03 Assisted-By requirement | 2026-03-12 | Joshua Alexander Clement + claude-sonnet-4-6 |
| `git/cp` | github.com/alirezarezvani/claude-skills `.claude/commands/git/cp.md` | Same attribution conflict as git/cm. Also depends on `ci-quality-gate.yml` CI workflow that does not exist in this project. | 2026-03-12 | Joshua Alexander Clement + claude-sonnet-4-6 |
| `c-level-advisor/context-engine` | github.com/alirezarezvani/claude-skills `c-level-advisor/context-engine/SKILL.md` | Reads and writes `~/.claude/company-context.md` at runtime — hard reject trigger per vetting workflow §8 ("Skill reads or writes `.claude/` or `~/.claude/` config"). Enriches and overwrites this file during sessions. Intent (context enrichment) is reasonable but the implementation grants write access to the user's config layer. | 2026-03-12 | claude-sonnet-4-6 |
| `c-level-advisor/chief-of-staff` | github.com/alirezarezvani/claude-skills `c-level-advisor/chief-of-staff/SKILL.md` | Writes to `~/.claude/decision-log.md` — hard reject trigger per vetting workflow §8. Also depends on `context-engine` (rejected above) for context loading. Dual violation. | 2026-03-12 | claude-sonnet-4-6 |
| `engineering-team/self-improving-agent` | github.com/alirezarezvani/claude-skills `engineering-team/self-improving-agent/SKILL.md` | Multiple hard reject triggers: (1) writes to `CLAUDE.md` (governance file equivalent to AGENTS.md), (2) writes to `.claude/rules/` (`.claude/` path), (3) installs a persistent PostToolUse hook (`error-capture.sh`) that fires on every Bash command. Autonomous promotion of patterns to enforced project rules without operator review. | 2026-03-12 | claude-sonnet-4-6 |
| `c-level-advisor/cs-onboard` | github.com/alirezarezvani/claude-skills `c-level-advisor/cs-onboard/SKILL.md` | Explicitly writes to `~/.claude/company-context.md` — hard reject trigger per vetting workflow §8. Body confirms: "After the interview, generate `~/.claude/company-context.md`" and "Do not move it." This is the setup wizard for the context-engine ecosystem (also rejected). Same `~/.claude/` violation. | 2026-03-12 | claude-sonnet-4-6 |

---

## Revision History

| Rev | Date | Author | Model | Why |
|---|---|---|---|---|
| 1.0 | 2026-03-12 | Joshua Alexander Clement | claude-sonnet-4-6 | Initial creation — approved skills registry seeded with confirmed Claude Code skills |
| 1.1 | 2026-03-12 | Joshua Alexander Clement | claude-sonnet-4-6 | Phase 1 static analysis of 7 skills from alirezarezvani/claude-skills — 2 rejected, 4 under review, 1 deferred |
| 1.2 | 2026-03-12 | Joshua Alexander Clement | claude-sonnet-4-6 | Phase 1 static analysis of 8 c-level-advisor skills — 2 hard rejected (context-engine, chief-of-staff: ~/.claude/ writes), 6 under review (board-meeting, competitive-intel, founder-coach, change-management, culture-architect, internal-narrative) |
| 1.3 | 2026-03-12 | Joshua Alexander Clement | claude-sonnet-4-6 | Phase 1 static analysis of 9 marketing-skill pure-prompt skills (all pass), 2 engineering-team pure-prompt skills (email-template-builder, stripe-integration-expert: both pass), 1 engineering-team hard reject (self-improving-agent: governance writes + persistent hook), 1 engineering-team pending full Phase 1 (playwright-pro: hooks + MCP) |
| 1.4 | 2026-03-12 | Joshua Alexander Clement | claude-sonnet-4-6 | Added Custom Skills section to §2 — 3 internally written compliant equivalents approved after Phase 1+2 vetting: ctx (Low), chief-of-staff (Low–Medium), curate (Low) |
| 1.5 | 2026-03-12 | Joshua Alexander Clement | claude-sonnet-4-6 | Phase 1 complete across all remaining pure-prompt skills: 10 new Under Review (api-test-suite-builder, database-schema-designer, pr-review-expert, agent-protocol, board-deck-builder, company-os, intl-expansion, ma-playbook, contract-and-proposal-writer); playwright-pro Phase 1 complete (FLAG — hooks clean, blanket Playwright CLI permissions); 1 new hard reject (cs-onboard: ~/.claude/ write) |
| 1.6 | 2026-03-12 | Joshua Alexander Clement | claude-sonnet-4-6 | Added `Depends On` column to §5 for dependency chain tracking (workflow §10). board-meeting flagged as depending on rejected context-engine — must substitute `/ctx` before approval. All other Under Review skills have no cross-skill dependencies. |
| 1.8 | 2026-03-13 | Joshua Alexander Clement | claude-sonnet-4-6 | Approved playwright-pro — moved to §2 Testing Skills. Full review completed: hook scripts (validate-test.sh, detect-playwright.sh), CLAUDE.md, .mcp.json, and both MCP server source files (testrail-mcp, browserstack-mcp) all clean. TestRail and BrowserStack MCP integrations approved — credentials from env vars only, fail fast if not configured, no local file writes. |
| 1.7 | 2026-03-13 | Joshua Alexander Clement | claude-sonnet-4-6 | Phase 1 complete for all 125 script-backed skills (broad sweep + domain batch analysis). No hard reject triggers found in any skill Python scripts or SKILL.md files. All 125 added to §5 organized by domain. Key findings: no `~/.claude/` writes, no `CLAUDE.md` writes, no hooks/settings.json outside playwright-pro and self-improving-agent (already reviewed), all third-party package imports in template strings (not runtime deps), PyYAML used safely throughout. 15 skills flagged (not rejected) for network calls, subprocess, MCP writes, or agent invocations. |
| 1.9 | 2026-03-13 | Joshua Alexander Clement | claude-sonnet-4-6 | Risk-ordered security review of Group A (Phase 4 required) skills. Decisions: (1) env-secrets-manager approved with caveat (output to gitignored file, not stdout); (2) skill-tester marked Phase 4 pending (sandbox verification required); (3) 6 direct-external-write skills rejected and replaced — google-workspace-cli and ms365-tenant-manager each get a compliant local-first equivalent; atlassian-admin + atlassian-templates + confluence-expert + jira-expert collapse into one compliant `/atlassian` skill with staging architecture. Design intents documented in rejected-skill-design-intents.md §5–7. |
| 2.0 | 2026-03-13 | Joshua Alexander Clement | claude-sonnet-4-6 | Phase 1–3 complete for all 17 Anthropic official skills (github.com/anthropics/skills). All 17 approved and added to §2 in three groups: (a) 8 pure-prompt skills (Low risk, clean), (b) 4 document processing skills (Low–Medium, LibreOffice/package caveats, production validated), (c) 5 tooling skills (Low–Medium, subprocess/npm/temp-file caveats documented). 8 packages added to package-review.md to clear package gate hold (pypdf, pdfplumber, reportlab, openpyxl, pillow, imageio, imageio-ffmpeg, numpy). |
| 2.1 | 2026-03-13 | Joshua Alexander Clement | claude-sonnet-4-6 | Group B individual sign-offs: all 18 flagged skills reviewed Phase 1–3 with full script reads. All 18 approved (10 clean, 8 with caveats). Key findings: senior-ml-engineer scripts are stubs; dependency-auditor subprocess import unused; performance-profiler is local-only; competitive-teardown API references are manual guidance; api-design-reviewer urllib.parse is URL parsing (not network); [INVOKE:...] patterns are advisory guidance to Claude. Group D bulk approval: all 117 remaining "Phase 1 complete" skills approved under standard conditions (stdlib-only, project-local, no governance access). board-meeting approved with caveat (same pattern as decision-logger). |
| 2.2 | 2026-03-13 | Joshua Alexander Clement | claude-sonnet-4-6 | Phase 4 procedure overhauled. Full read of script_tester.py confirmed no built-in sandbox (tempfile imported but unused; subprocess.run with cwd only). Docker Desktop adopted as Phase 4 runtime. Standalone procedure doc created at docs/phase4-sandbox.md (network policy: default none, per-skill opt-in; standard container config: --read-only, --tmpfs /tmp, --cap-drop ALL). skill-vetting-workflow.md §5 updated to reference Docker procedure and clarify when Phase 4 applies vs. when code review is sufficient. skill-tester entry updated: static-mode use approved in-session; execution-mode use requires Docker per phase4-sandbox.md §4.1. |
| 2.3 | 2026-03-14 | Joshua Alexander Clement | claude-sonnet-4-6 | Phase 4 Docker sandbox passed for the skill called skill-tester. Canary confirmed container isolation (writes outside /tmp/ blocked with OSError EROFS). skill-tester ran against dependency-auditor: 2 PASS, 1 PARTIAL (bug in target skill's sample data, not in skill-tester). skill-tester moved from Phase 4 pending to Approved with caveat. Vetting queue now fully complete. Also: phase4-sandbox.md canary script corrected — except clause updated to catch (PermissionError, OSError) after discovering Docker --read-only raises OSError not PermissionError. |
