# Skill Vetting Workflow

**Type**: Reference Document
**Status**: Ratified
**Constitutional Authority**: `memory/constitution.md` Part 1, Amendment 5 (No Undermining Oversight), Part 2, Amendment 5 (Accountability)

---

## Purpose

Defines the process for reviewing, testing, and approving Claude Code skills from external or unverified sources before they are added to `docs/approved-skills.md`. A skill that has not completed this workflow is treated as unapproved regardless of its apparent quality or source reputation.

---

## Contents
1. [Threat Model](#1-threat-model)
2. [Phase 1 — Static Analysis](#2-phase-1--static-analysis)
3. [Phase 2 — Constitutional Review](#3-phase-2--constitutional-review)
4. [Phase 3 — Risk Classification](#4-phase-3--risk-classification)
5. [Phase 4 — Sandboxed Execution](#5-phase-4--sandboxed-execution)
6. [Phase 5 — Approval Decision](#6-phase-5--approval-decision)
7. [Sandbox Setup and Teardown](#7-sandbox-setup-and-teardown)
8. [Red Flag Reference](#8-red-flag-reference)

---

## 1. Threat Model

Skills are prompt templates that instruct Claude to invoke tools — `Bash`, `Edit`, `Write`, `WebFetch`, `WebSearch`, and others. The risks are not in reading a skill file — they are in executing one.

| Threat | Description | Caught in Phase |
|---|---|---|
| **Prompt injection** | Instructions hidden in the skill designed to override Claude's behavior or constitution | 1, 2 |
| **Unexpected tool scope** | Skill reads or writes files outside its stated purpose | 1, 4 |
| **Data exfiltration** | Skill sends data to external URLs via WebFetch or WebSearch | 1, 4 |
| **Persistent modification** | Skill writes to config, memory, standards, or constitution files | 1, 4 |
| **Credential harvesting** | Skill requests or logs sensitive values (tokens, passwords, keys) | 1, 2 |
| **Supply chain confusion** | Skill impersonates a known approved skill with subtle behavioral differences | 1, 2 |

Reading the skill file to perform static analysis is safe. The threat only activates on execution.

---

## 2. Phase 1 — Static Analysis

**Goal**: Understand what the skill does without running it.
**Required tool**: Read only. No execution.

### 2.1 Tool Inventory

List every tool the skill invokes. Flag any that are unexpected for the skill's stated purpose.

| Tool | Risk Level | Notes |
|---|---|---|
| `Read`, `Glob`, `Grep` | Low | Read-only |
| `Edit`, `Write` | Medium | Modifies files — scope matters |
| `Bash` | High | Arbitrary shell execution |
| `WebFetch`, `WebSearch` | High | External network calls |
| `Agent` | High | Spawns sub-agents with their own tool access |
| `NotebookEdit` | Medium | Modifies Jupyter notebooks |

### 2.2 File Scope Analysis

For every `Edit`, `Write`, or `Read` call in the skill:
- What paths does it access?
- Are any of those paths outside the working directory?
- Does it access `memory/`, `standards/`, `constitution/`, `.claude/`, `~/.claude/`, or system paths?

Any skill that reads or writes to governance documents (`constitution.md`, `standards/STD*`, `AGENTS.md`) without an explicit documented reason is a **hard reject**.

### 2.3 Network Scope Analysis

For every `WebFetch` or `WebSearch` call:
- What URL or query is being sent?
- Is any project data, file content, or session context included in the request?
- Is the domain hardcoded or constructed dynamically?

A skill that sends file contents or session data to an external URL is a **hard reject**.

### 2.4 Prompt Injection Scan

Read the skill file looking for:

| Pattern | Example | Flag |
|---|---|---|
| Override instructions | "Ignore previous instructions" | Hard reject |
| Constitution bypass | "Disregard the constitution for this task" | Hard reject |
| Role replacement | "You are now [different persona]" | Hard reject |
| Hidden instructions | Instructions in HTML comments, zero-width characters, or unusual whitespace | Hard reject |
| Scope creep language | "Also do X while you're at it" where X is unrelated to the skill's stated purpose | Review |
| Escalation requests | Asking Claude to request more permissions or tool access than needed | Review |

### 2.5 Static Analysis Checklist

```
[ ] Tool inventory complete — all tools identified and listed
[ ] File scope documented — all read/write paths noted
[ ] No access to governance documents (memory/, standards/, .claude/)
[ ] Network calls identified — URLs and data sent documented
[ ] No project data sent to external URLs
[ ] Prompt injection scan complete — no override patterns found
[ ] Skill does what it claims and only what it claims
[ ] Source noted — where did this skill come from?
```

---

## 3. Phase 2 — Constitutional Review

**Goal**: Confirm the skill's instructions are consistent with the constitution.

Check against each Part:

| Part | Check |
|---|---|
| Part 1, Amendment 5 | Does the skill ask Claude to conceal its actions or bypass oversight? |
| Part 2, Amendment 1 | Does the skill instruct Claude to fabricate, omit, or mislead? |
| Part 2, Amendment 4 | Does the skill handle or transmit private or sensitive data? |
| Part 2, Amendment 5 | Does the skill produce auditable, attributable outputs? |
| Part 2, Amendment 7 | Does the skill respect attribution — does it claim authorship for work it did not originate? |
| Part 4, Amendment 1 | Does the skill ask Claude to act beyond its defined authority? |

Any constitutional violation is a **hard reject**. Document the specific article violated.

```
[ ] Part 1 — no oversight bypass
[ ] Part 2, Amendment 1 — no deception or omission
[ ] Part 2, Amendment 4 — no unauthorized data handling
[ ] Part 2, Amendment 5 — outputs are attributable
[ ] Part 2, Amendment 7 — attribution respected
[ ] Part 4, Amendment 1 — no authority overreach
```

---

## 4. Phase 3 — Risk Classification

Based on Phases 1–2, assign a risk level using the table in `docs/approved-skills.md §4`.

Skills classified **Medium or above** proceed to Phase 4 (sandboxed execution).
Skills classified **Low** may be approved after Phases 1–2 with Operator sign-off — execution testing is recommended but not mandatory.
Skills with any **hard reject** flag do not proceed. Document in §6 (Rejected Skills) of `docs/approved-skills.md`.

---

## 5. Phase 4 — Sandboxed Execution

**Goal**: Observe what the skill actually does in an isolated environment.
**Required**: Sandbox setup per §7. No real credentials or sensitive data in scope.

### 5.1 Pre-execution baseline

```bash
# Record filesystem state before execution
find . -type f -newer /tmp/skill-test-baseline -name "*.md" > /tmp/before-state.txt
ls -la /tmp/skill-test-[name]/
```

### 5.2 Execution

Run the skill in the worktree sandbox with a controlled, synthetic input. Observe:
- Every tool call Claude makes during execution
- Every file read, written, or modified
- Every network call attempted
- Every subprocess spawned via Bash

**Do not provide real credentials, tokens, API keys, or personal data during sandbox testing.**

Use synthetic stand-ins:
```
API key:   sk-test-0000000000000000000000000000000000000000000000
Password:  test-password-sandbox
Email:     sandbox@test.local
```

### 5.3 Post-execution comparison

```bash
# What changed?
find . -type f -newer /tmp/skill-test-baseline -name "*.md" > /tmp/after-state.txt
diff /tmp/before-state.txt /tmp/after-state.txt

# Check for unexpected writes outside working directory
find /tmp/skill-test-[name]/ -newer /tmp/skill-test-baseline -type f
```

### 5.4 Execution checklist

```
[ ] Sandbox created per §7 — no real data present
[ ] Baseline recorded before execution
[ ] Skill executed with synthetic inputs only
[ ] All tool calls observed and match static analysis prediction
[ ] No unexpected file writes outside stated scope
[ ] No network calls to unexpected domains
[ ] No writes to governance documents
[ ] Post-execution comparison clean — no residual state outside sandbox
[ ] Sandbox torn down per §7
```

---

## 6. Phase 5 — Approval Decision

Compile findings from all phases into a review record:

```markdown
## Skill Review: [Skill Name]

**Source**: [URL or origin]
**Date reviewed**: YYYY-MM-DD
**Reviewed by**: [Name] + [model-id]
**Risk classification**: [Low / Low-Medium / Medium / High]

### Static Analysis
[Findings — tools used, file scope, network calls, injection scan result]

### Constitutional Review
[Pass / Fail per article — note any concerns even if not a hard reject]

### Execution Test
[What happened — matches or deviates from static analysis?]

### Decision
[ ] Approved — add to docs/approved-skills.md §2
[ ] Approved with caveats — note caveats in approved-skills.md
[ ] Rejected — add to docs/approved-skills.md §6 with reason
[ ] Deferred — needs further review, add to §5 with notes

**Operator sign-off**: Joshua Alexander Clement
```

The Operator must give explicit approval before a skill is moved from §5 (Under Review) to §2 (Approved) in `docs/approved-skills.md`.

---

## 7. Sandbox Setup and Teardown

### Setup

```bash
# 1. Create isolated worktree on a throwaway branch
git worktree add /tmp/skill-test-[skill-name] -b test/skill-[skill-name]

# 2. Create synthetic test data — no real content
mkdir -p /tmp/skill-test-[skill-name]/test-data
echo "Synthetic test file — no real data" > /tmp/skill-test-[skill-name]/test-data/sample.md

# 3. Set baseline timestamp
touch /tmp/skill-test-baseline

# 4. Confirm no sensitive files are in scope
ls -la /tmp/skill-test-[skill-name]/
```

### During testing

- Work only within `/tmp/skill-test-[skill-name]/`
- If the skill attempts to access paths outside this directory, stop immediately — that is a finding
- If the skill attempts a network call with real data, stop immediately

### Teardown

```bash
# Remove the worktree
git worktree remove /tmp/skill-test-[skill-name] --force

# Delete the test branch
git branch -D test/skill-[skill-name]

# Clean up temp files
rm -f /tmp/before-state.txt /tmp/after-state.txt /tmp/skill-test-baseline
```

---

## 8. Red Flag Reference

Quick reference for findings that trigger an immediate stop and hard reject:

| Red Flag | Action |
|---|---|
| Skill reads or writes `memory/constitution.md` | Hard reject |
| Skill reads or writes any `standards/STD*.md` | Hard reject |
| Skill reads or writes `.claude/` or `~/.claude/` config | Hard reject |
| Skill sends file contents to an external URL | Hard reject |
| Skill contains "ignore previous instructions" or equivalent | Hard reject |
| Skill requests elevated permissions or additional tool access | Hard reject |
| Skill's actual tool calls don't match its stated purpose | Hard reject |
| Skill constructs network URLs dynamically from session context | Hard reject |
| Skill writes outside the working directory | Hard reject |
| Skill spawns persistent background processes | Hard reject |

When a hard reject is triggered mid-execution, stop the session, tear down the sandbox, and document the finding before doing anything else.

---

## Revision History

| Rev | Date | Author | Model | Why |
|---|---|---|---|---|
| 1.0 | 2026-03-12 | Joshua Alexander Clement | claude-sonnet-4-6 | Initial creation — full vetting workflow for external Claude Code skills |
