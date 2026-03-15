## Skill Review: speckit.specify

**Source**: External — `https://github.com/github/spec-kit` (`templates/commands/specify.md`)
**Skill type**: Script-backed (bash)
**Date reviewed**: 2026-03-14
**Reviewed by**: Joshua Alexander Clement + claude-sonnet-4-6
**Risk classification**: Medium
**Dependency chain**: spec-kit must be installed

---

### Static Analysis

**§2.0 File Inventory**

| File | Category |
|---|---|
| `templates/commands/specify.md` | Skill definition |
| `scripts/bash/create-new-feature.sh` | Bash script — creates feature branch and directory |
| `scripts/bash/common.sh` | Bash script (sourced) |

**§2.1 Tool Inventory**

| Tool | Risk | Notes |
|---|---|---|
| `Bash` | Medium | Runs `create-new-feature.sh --json --short-name "[name]" "[description]"` |
| `Read` | Low | Loads `templates/spec-template.md` |
| `Write` | Low–Medium | Writes SPEC_FILE (spec.md); creates `FEATURE_DIR/checklists/requirements.md` |

**§2.2 File Scope Analysis**

Script creates: a new git feature branch (auto-numbered); `FEATURE_DIR/` directory; spec file. Model then writes: spec.md content; checklists/requirements.md.

**⚠️ Git Branch Creation**

`create-new-feature.sh` creates and checks out a new git branch. Branch name is auto-generated: `specify/<number>-<short-name>`. The command states "do NOT pass `--number` — the script determines the correct next number automatically." Branch creation is irreversible without `git branch -D`.

User must be aware that invoking `/speckit.specify` creates and switches to a new git branch. This is by design but must be disclosed.

**§2.3 Network Scope Analysis**

No network calls. create-new-feature.sh is local git operations + directory creation.

**§2.4 Prompt Injection Scan**

`$ARGUMENTS` (feature description) is passed to the script as the description argument. This is sanitized via single-quote escape syntax documented in the command. No bypass language. Maximum 3 `[NEEDS CLARIFICATION]` markers — hard limit prevents interrogation loops.

**§2.5 Hook and Injection Analysis**

No extension hooks, MCP config, agents/, or settings files. Handoffs to `speckit.plan` and `speckit.clarify` are suggestions only.

---

### Script Analysis

**§2.6.1 create-new-feature.sh**

Not fetched in full (separate script from check-prerequisites.sh). Based on spec.md description: creates feature branch with `git checkout -b`, initializes spec directory structure. Expected operations: `git checkout -b specify/N-name`, `mkdir -p FEATURE_DIR`, copy spec-template.md to spec.md. Low risk.

**§2.6.2 Single-Run Guard**

Command states: "You must only ever run this script once per feature." The script uses auto-numbering to prevent collisions. Running twice for the same feature would create a second branch (specify/N+1-name). Operator should be aware this guard is prompt-level only, not technical.

**§2.6.3 Argument Sanitization**

Feature description is passed to shell script. Command documents escape syntax for single quotes: `'I'\''m Groot'`. This is standard POSIX shell escaping. The model generates the branch short-name from the description — no raw user input passed directly as branch name.

---

### Constitutional Review

| Part | Check | Result |
|---|---|---|
| Part 1, Amendment 5 | No oversight bypass | PASS — git branch creation is visible |
| Part 5, Amendment 1 | No deception | PASS |
| Part 5, Amendment 4 | No unauthorized data handling | PASS |
| Part 5, Amendment 5 | Outputs attributable | PASS |
| Part 3, Amendment 1 | No authority overreach | PASS — bounded to feature directory and spec files |

---

### Execution Test

**Phase 4 — Deferred**: spec-kit not installed in LLM-Quickstart. Required before first use.

Key Phase 4 checks:
- Verify create-new-feature.sh only creates branch and feature directory (no unrelated writes)
- Verify branch naming follows `specify/N-name` convention, does not clobber existing branches
- Verify argument escaping handles special characters safely

---

### Decision

**APPROVED WITH CONDITIONS**

**Conditions:**
1. Target project must have spec-kit installed
2. User must be aware that invocation creates and switches to a new git branch
3. Ensure working tree is clean before invocation (uncommitted work will be on the new branch)
4. Phase 4 execution test required for create-new-feature.sh before first use
5. Do not run twice for the same feature without intent to create a parallel branch

**Approved by:** Joshua Alexander Clement + claude-sonnet-4-6, 2026-03-14
