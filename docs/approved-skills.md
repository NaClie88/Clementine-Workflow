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
| *(none currently)* | — | — | — |

> Skills from unverified external sources (community repos, third-party collections) must be reviewed against the constitution before being added here. The source being popular or widely used is not sufficient justification.

---

## 6. Rejected Skills

Skills that were reviewed and not approved, with the reason:

| Skill | Reason Rejected | Date | Reviewed By |
|---|---|---|---|
| *(none currently)* | — | — | — |

---

## Revision History

| Rev | Date | Author | Model | Why |
|---|---|---|---|---|
| 1.0 | 2026-03-12 | Joshua Alexander Clement | claude-sonnet-4-6 | Initial creation — approved skills registry seeded with confirmed Claude Code skills |
