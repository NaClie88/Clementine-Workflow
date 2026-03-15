## Skill Review: speckit.clarify

**Source**: External — `https://github.com/github/spec-kit` (`templates/commands/clarify.md`)
**Skill type**: Script-backed (bash)
**Date reviewed**: 2026-03-14
**Reviewed by**: Joshua Alexander Clement + claude-sonnet-4-6
**Risk classification**: Medium
**Dependency chain**: spec-kit must be installed in target project

---

### Static Analysis

**§2.0 File Inventory**

| File | Category |
|---|---|
| `templates/commands/clarify.md` | Skill definition |
| `scripts/bash/check-prerequisites.sh` | Bash script (invoked with `--json --paths-only`) |
| `scripts/bash/common.sh` | Bash script (sourced) |

**§2.1 Tool Inventory**

| Tool | Risk | Notes |
|---|---|---|
| `Bash` | Low | Runs `check-prerequisites.sh --json --paths-only` |
| `Read` | Low | Loads spec.md once at start |
| `Write` | Medium | Overwrites spec.md after each accepted clarification answer (atomic) |

**§2.2 File Scope Analysis**

Reads: spec.md (FEATURE_SPEC). Writes: spec.md — overwrites the file after each answer to minimize context loss risk. Write scope is exactly one file: the active feature spec. No other files written. Handoff hint (`speckit.plan`) is a suggestion only; does not auto-invoke.

**§2.3 Network Scope Analysis**

No network calls.

**§2.4 Prompt Injection Scan**

`$ARGUMENTS` provides prioritization context but does not control file paths. No bypass language. The command explicitly prohibits speculative tech stack questions unless blocking. No injection vectors found.

**§2.5 Hook and Injection Analysis**

No hooks, MCP config, agents/ directory. Bash script is paths-only mode — no file validation, no write operations.

---

### Script Analysis

**§2.6.1 Shell Script**

`--paths-only` mode: resolves FEATURE_DIR, FEATURE_SPEC, IMPL_PLAN, TASKS paths and outputs them. No file validation, no writes. See speckit-analyze.md §2.6.1 for common.sh notes.

**§2.6.2 File Modification Bounds**

Modifies only FEATURE_SPEC (the active spec.md). Modification is incremental: appends to `## Clarifications` section and updates relevant sections in-place. The command explicitly states "if the clarification invalidates an earlier ambiguous statement, replace that statement instead of duplicating." Destructive replacement is possible but bounded to the spec file only.

**§2.6.3 Maximum Questions**

Hard-capped at 5 total questions per session. Prevents open-ended interrogation loops.

---

### Constitutional Review

| Part | Check | Result |
|---|---|---|
| Part 1, Amendment 5 | No oversight bypass | PASS |
| Part 5, Amendment 1 | No deception | PASS — each question shows recommended answer with rationale |
| Part 5, Amendment 4 | No unauthorized data handling | PASS — modifies only local spec file |
| Part 5, Amendment 5 | Outputs attributable | PASS |
| Part 3, Amendment 1 | No authority overreach | PASS — bounded to spec.md only |

---

### Risk Notes

The atomic-overwrite pattern (save after each clarification) means partially-completed sessions cannot be easily undone. Users should have git state clean before running. The command does not perform a git status check before writing.

---

### Execution Test

**Phase 4 — Deferred**: spec-kit not installed in LLM-Quickstart. Required before first use.

Verify: spec.md is the only file modified; clarification section is appended correctly; previous content is not destroyed.

---

### Decision

**APPROVED WITH CONDITIONS**

**Conditions:**
1. Target project must have spec-kit installed
2. Git working tree should be clean before invocation (no uncommitted changes to spec.md)
3. Phase 4 execution test required before first use
4. Maximum 5-question cap must be preserved in any adaptation

**Approved by:** Joshua Alexander Clement + claude-sonnet-4-6, 2026-03-14
