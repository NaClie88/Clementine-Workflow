## Skill Review: speckit.tasks

**Source**: External — `https://github.com/github/spec-kit` (`templates/commands/tasks.md`)
**Skill type**: Script-backed (bash) + extension hook system
**Date reviewed**: 2026-03-14
**Reviewed by**: Joshua Alexander Clement + claude-sonnet-4-6
**Risk classification**: Medium
**Dependency chain**: spec-kit must be installed; plan.md must exist

---

### Static Analysis

**§2.0 File Inventory**

| File | Category |
|---|---|
| `templates/commands/tasks.md` | Skill definition |
| `scripts/bash/check-prerequisites.sh` | Bash script (invoked with `--json`) |
| `scripts/bash/common.sh` | Bash script (sourced) |
| `.specify/extensions.yml` | Optional — hook configuration |

**§2.1 Tool Inventory**

| Tool | Risk | Notes |
|---|---|---|
| `Bash` | Low | Runs `check-prerequisites.sh --json` |
| `Read` | Low | Loads plan.md, spec.md, optionally data-model.md, contracts/, research.md |
| `Write` | Low–Medium | Writes `FEATURE_DIR/tasks.md` |

**§2.2 File Scope Analysis**

Reads from FEATURE_DIR (plan.md, spec.md, optional files). Writes: tasks.md to FEATURE_DIR. Bounded write scope. Handoffs to `speckit.analyze` and `speckit.implement` are suggestions only; not auto-invoked.

**§2.3 Network Scope Analysis**

No network calls.

**§2.4 Prompt Injection Scan**

`$ARGUMENTS` provides optional context. No path control via user input. No bypass language. Checklist format validation (required checkbox/ID/label/path pattern) is explicit and enforced.

**§2.5 Hook and Injection Analysis**

⚠️ **Extension Hook System** — same concern as speckit.implement

Reads `.specify/extensions.yml` for `hooks.before_tasks` and `hooks.after_tasks`. Mandatory hooks with `optional: false` trigger `EXECUTE_COMMAND: {command}` auto-execution without separate user confirmation.

Since `.specify/extensions.yml` does not exist in LLM-Quickstart, hook processing is silently skipped. In spec-kit projects where extensions.yml is present, user must review hooks before invocation.

---

### Script Analysis

**§2.6.1 Shell Script**

Standard `check-prerequisites.sh --json` — resolves paths, validates plan.md exists. No writes. See speckit-analyze.md §2.6.1.

---

### Constitutional Review

| Part | Check | Result |
|---|---|---|
| Part 1, Amendment 5 | No oversight bypass | **CAUTION** — extension hook auto-execution if extensions.yml present |
| Part 5, Amendment 1 | No deception | PASS |
| Part 5, Amendment 4 | No unauthorized data handling | PASS |
| Part 5, Amendment 5 | Outputs attributable | PASS |
| Part 3, Amendment 1 | No authority overreach | PASS — bounded to tasks.md in FEATURE_DIR |

---

### Execution Test

**Phase 4 — Deferred**: spec-kit not installed in LLM-Quickstart.

Key Phase 4 checks:
- Verify tasks.md is the only file written
- Verify extension hook path silently skips when extensions.yml absent
- Verify task format validation (checkbox/ID/story/path) is applied

---

### Decision

**APPROVED WITH CONDITIONS**

**Conditions:**
1. Target project must have spec-kit installed
2. **Review `.specify/extensions.yml` before invocation** if it exists — mandatory hooks auto-execute
3. Phase 4 execution test required before first use
4. tasks.md is the only expected output; warn if any other files are written
5. In LLM-Quickstart: will fail at script step — expected behavior

**Approved by:** Joshua Alexander Clement + claude-sonnet-4-6, 2026-03-14
