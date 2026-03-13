# Approved Claude Code Skills Registry

**Type**: Reference Document
**Status**: Ratified
**Constitutional Authority**: `memory/constitution.md` Part 2, Amendment 5 (Accountability), Governance (Operator declaration)

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

Skills that have been identified but not yet fully reviewed or approved:

| Skill | Source | Status | Notes |
|---|---|---|---|
| `review` | github.com/alirezarezvani/claude-skills `.claude/commands/review.md` | Under Review — Phase 1 complete | Good pre-push lint/audit concept. Installs 4 unapproved packages (yamllint, check-jsonschema, safety, markdown-link-check). Hardcoded paths are repo-specific and need rewriting. Needs STD09 approvals before execution test. |
| `security-scan` | github.com/alirezarezvani/claude-skills `.claude/commands/security-scan.md` | Under Review — Phase 1 complete | Secret scanning + CVE audit concept is valuable. Requires gitleaks (brew) and safety (pip) — both need STD09 approval. Makes external network calls to PyPI CVE database. |
| `update-docs` | github.com/alirezarezvani/claude-skills `.claude/commands/update-docs.md` | Deferred | Entirely hardcoded to source repo structure. Runs 3 unaudited Python scripts. No value to this project as-is. Revisit only if a general docs-sync skill is needed. |
| `git/clean` | github.com/alirezarezvani/claude-skills `.claude/commands/git/clean.md` | Under Review — Phase 1 complete | Branch cleanup skill. Clean static analysis — no injection, no external calls, confirms before remote deletes. Minor adaptation needed: protected branch list (remove dev, gh-pages; keep main only). |
| `git/pr` | github.com/alirezarezvani/claude-skills `.claude/commands/git/pr.md` | Under Review — Phase 1 complete | PR creation via gh CLI. Concept is solid. Needs CI gate dependency removed and adapted to STD04 review criteria. |
| `c-level-advisor/board-meeting` | github.com/alirezarezvani/claude-skills `c-level-advisor/board-meeting/SKILL.md` | Under Review — Phase 1 complete | 6-phase multi-agent board deliberation. Reads `memory/company-context.md` and writes to `memory/board-meetings/` (project-level relative paths — not `~/.claude/`). No external network calls, no injection patterns. Medium risk due to autonomous memory writes. Needs adaptation to match deployment's memory structure before Phase 4. |
| `c-level-advisor/competitive-intel` | github.com/alirezarezvani/claude-skills `c-level-advisor/competitive-intel/SKILL.md` | Under Review — Phase 1 complete | External intelligence gathering via WebSearch. Queries Crunchbase, LinkedIn, G2/Capterra, Ad Libraries. No project data exfiltrated — searches only. No local file writes, no governance access. Medium risk due to external calls. Clean injection scan. |
| `c-level-advisor/founder-coach` | github.com/alirezarezvani/claude-skills `c-level-advisor/founder-coach/SKILL.md` | Under Review — Phase 1 complete | Pure coaching framework. No file I/O, no network calls, no governance access. Uses inline templates only. Clean injection scan. Low risk — Operator approval needed to move to §2. |
| `c-level-advisor/change-management` | github.com/alirezarezvani/claude-skills `c-level-advisor/change-management/SKILL.md` | Under Review — Phase 1 complete | ADKAR-based change playbook. No file I/O, no network calls, no governance access. Pure framework skill. Clean injection scan. Low risk — Operator approval needed to move to §2. |
| `c-level-advisor/culture-architect` | github.com/alirezarezvani/claude-skills `c-level-advisor/culture-architect/SKILL.md` | Under Review — Phase 1 complete | Culture health assessment and values framework. No file I/O, no network calls, no governance access. Pure framework skill. Clean injection scan. Low risk — Operator approval needed to move to §2. |
| `c-level-advisor/internal-narrative` | github.com/alirezarezvani/claude-skills `c-level-advisor/internal-narrative/SKILL.md` | Under Review — Phase 1 complete | Internal communications strategy framework. No file I/O, no network calls, no governance access. Includes contradiction detection to prevent narrative injection. Clean injection scan. Low risk — Operator approval needed to move to §2. |
| `marketing-skill/ai-seo` | github.com/alirezarezvani/claude-skills `marketing-skill/ai-seo/SKILL.md` | Under Review — Phase 1 complete | AI-era SEO strategy framework. No file I/O, no network calls, no injection patterns. Pure prompt framework. Low risk — Operator approval needed to move to §2. |
| `marketing-skill/brand-guidelines` | github.com/alirezarezvani/claude-skills `marketing-skill/brand-guidelines/SKILL.md` | Under Review — Phase 1 complete | Brand identity framework. Conditionally reads `.claude/product-marketing-context.md` (project-relative path, read-only, not `~/.claude/`). No network calls, no injection. Low risk — Operator approval needed. |
| `marketing-skill/content-creator` | github.com/alirezarezvani/claude-skills `marketing-skill/content-creator/SKILL.md` | Under Review — Phase 1 complete | Deprecated routing wrapper. No file I/O, no network calls, no injection. Minimal attack surface. Low risk — Operator approval needed. |
| `marketing-skill/marketing-ideas` | github.com/alirezarezvani/claude-skills `marketing-skill/marketing-ideas/SKILL.md` | Under Review — Phase 1 complete | Idea generation framework. Conditionally reads `.claude/product-marketing-context.md` (project-relative, read-only). No network calls, no injection. Low risk — Operator approval needed. |
| `marketing-skill/marketing-psychology` | github.com/alirezarezvani/claude-skills `marketing-skill/marketing-psychology/SKILL.md` | Under Review — Phase 1 complete | Mental models and behavioral frameworks. Conditionally reads `marketing-context.md`. No network calls, no injection. Low risk — Operator approval needed. |
| `marketing-skill/marketing-strategy-pmm` | github.com/alirezarezvani/claude-skills `marketing-skill/marketing-strategy-pmm/SKILL.md` | Under Review — Phase 1 complete | Product marketing strategy framework. No file I/O, no network calls, no injection. Low risk — Operator approval needed. |
| `marketing-skill/paywall-upgrade-cro` | github.com/alirezarezvani/claude-skills `marketing-skill/paywall-upgrade-cro/SKILL.md` | Under Review — Phase 1 complete | Paywall conversion optimization framework. Conditionally reads `.claude/product-marketing-context.md` (project-relative, read-only). No network calls, no injection. Low risk — Operator approval needed. |
| `marketing-skill/popup-cro` | github.com/alirezarezvani/claude-skills `marketing-skill/popup-cro/SKILL.md` | Under Review — Phase 1 complete | Popup conversion optimization framework. Conditionally reads `.claude/product-marketing-context.md` (project-relative, read-only). No network calls, no injection. Low risk — Operator approval needed. |
| `marketing-skill/social-content` | github.com/alirezarezvani/claude-skills `marketing-skill/social-content/SKILL.md` | Under Review — Phase 1 complete | Social media content framework. Conditionally reads `.claude/product-marketing-context.md` (project-relative, read-only). No network calls, no injection. Low risk — Operator approval needed. |
| `engineering-team/email-template-builder` | github.com/alirezarezvani/claude-skills `engineering-team/email-template-builder/SKILL.md` | Under Review — Phase 1 complete | React Email template generation assistant. Outputs code for transactional email systems (welcome, invoice, verification). No file I/O, no network calls, no injection. Low risk — Operator approval needed. |
| `engineering-team/stripe-integration-expert` | github.com/alirezarezvani/claude-skills `engineering-team/stripe-integration-expert/SKILL.md` | Under Review — Phase 1 complete | Stripe billing integration reference skill. Outputs code patterns for subscriptions, webhooks, customer portal. No file I/O, no network calls, no injection. Low risk — Operator approval needed. |
| `engineering-team/playwright-pro` | github.com/alirezarezvani/claude-skills `engineering-team/playwright-pro/SKILL.md` | Under Review — Phase 1 pending | Testing automation suite with PostToolUse (Write/Edit) and SessionStart hooks. Also includes MCP integrations (BrowserStack, TestRail) and TypeScript MCP servers. Hook scope and shell scripts need full Phase 1 review before classification. Not pure-prompt. |

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

---

## Revision History

| Rev | Date | Author | Model | Why |
|---|---|---|---|---|
| 1.0 | 2026-03-12 | Joshua Alexander Clement | claude-sonnet-4-6 | Initial creation — approved skills registry seeded with confirmed Claude Code skills |
| 1.1 | 2026-03-12 | Joshua Alexander Clement | claude-sonnet-4-6 | Phase 1 static analysis of 7 skills from alirezarezvani/claude-skills — 2 rejected, 4 under review, 1 deferred |
| 1.2 | 2026-03-12 | Joshua Alexander Clement | claude-sonnet-4-6 | Phase 1 static analysis of 8 c-level-advisor skills — 2 hard rejected (context-engine, chief-of-staff: ~/.claude/ writes), 6 under review (board-meeting, competitive-intel, founder-coach, change-management, culture-architect, internal-narrative) |
| 1.3 | 2026-03-12 | Joshua Alexander Clement | claude-sonnet-4-6 | Phase 1 static analysis of 9 marketing-skill pure-prompt skills (all pass), 2 engineering-team pure-prompt skills (email-template-builder, stripe-integration-expert: both pass), 1 engineering-team hard reject (self-improving-agent: governance writes + persistent hook), 1 engineering-team pending full Phase 1 (playwright-pro: hooks + MCP) |
