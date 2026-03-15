## Skill Review: speckit.implement

**Source**: External — `https://github.com/github/spec-kit` (`templates/commands/implement.md`)
**Skill type**: Script-backed (bash) + extension hook system
**Date reviewed**: 2026-03-14
**Reviewed by**: Joshua Alexander Clement + claude-sonnet-4-6
**Risk classification**: High
**Dependency chain**: spec-kit must be installed; tasks.md must exist

---

### Static Analysis

**§2.0 File Inventory**

| File | Category |
|---|---|
| `templates/commands/implement.md` | Skill definition |
| `scripts/bash/check-prerequisites.sh` | Bash script (invoked with `--json --require-tasks --include-tasks`) |
| `scripts/bash/common.sh` | Bash script (sourced) |
| `.specify/extensions.yml` | Optional — hook configuration (read if present) |

**§2.1 Tool Inventory**

| Tool | Risk | Notes |
|---|---|---|
| `Bash` | Low–Medium | Runs check-prerequisites.sh; may run `git rev-parse` for ignore-file detection |
| `Read` | Low | Loads tasks.md, plan.md, data-model.md, contracts/, research.md, checklists/ |
| `Write` | High | Writes ALL implementation files per tasks.md; creates/updates ignore files |
| `Bash` | High | `git rev-parse --git-dir` — checks git status; may create/modify .gitignore |

**§2.2 File Scope Analysis**

Writes to any file referenced in tasks.md — this is unbounded in scope relative to the project tree. Creates/updates .gitignore, .dockerignore, .eslintignore, .prettierignore, .npmignore, .terraformignore as detected. Reads checklists/ to gate on completion status.

**§2.3 Network Scope Analysis**

No direct network calls. Extension hook system can invoke other slash commands (`EXECUTE_COMMAND: {command}`) — those commands may themselves have network or file scope. Extension hooks are read from `.specify/extensions.yml` if present. Since this file does not exist in LLM-Quickstart, hook processing is skipped silently.

**§2.4 Prompt Injection Scan**

`$ARGUMENTS` is optional user context. No override instructions. No constitution bypass. The checklist gate (halt if incomplete checklists) is a legitimate safety check. No injection vectors found in prompt text.

**§2.5 Hook and Injection Analysis**

⚠️ **Extension Hook System — Key Finding**

The command reads `.specify/extensions.yml` and processes hooks under `hooks.before_implement` and `hooks.after_implement`. For mandatory hooks (`optional: false`), the output includes:
```
EXECUTE_COMMAND: {command}
```
The AI is instructed to: "Wait for the result of the hook command before proceeding." This means mandatory hooks trigger **automatic, unsolicited execution of other slash commands** without a separate user confirmation step.

**Risk**: If a malicious or misconfigured `extensions.yml` defines a mandatory hook pointing to a destructive command, it would execute without user approval during implementation.

**Mitigations present:**
- Only processes hooks where `enabled: true`
- Does not evaluate `condition` expressions (defers to HookExecutor) — hooks with non-empty conditions are skipped
- `.specify/extensions.yml` does not exist in LLM-Quickstart — hook processing is silently skipped

**Mitigation required (condition):** User must review `.specify/extensions.yml` before first invocation in any project where it exists.

---

### Script Analysis

**§2.6.1 Shell Script**

check-prerequisites.sh in `--require-tasks --include-tasks` mode: validates FEATURE_DIR exists, plan.md exists, tasks.md exists. Outputs JSON with FEATURE_DIR and AVAILABLE_DOCS. No writes. See speckit-analyze.md §2.6.1.

**§2.6.2 Ignore File Detection**

`git rev-parse --git-dir 2>/dev/null` — safe read-only git command. Creates or appends ignore files only with standard patterns (documented in command). No user input in ignore file content.

---

### Constitutional Review

| Part | Check | Result |
|---|---|---|
| Part 1, Amendment 5 | No oversight bypass | **CAUTION** — mandatory extension hooks auto-execute without user confirmation |
| Part 5, Amendment 1 | No deception | PASS — checklist gate is transparent |
| Part 5, Amendment 4 | No unauthorized data handling | PASS — no external transmission |
| Part 5, Amendment 5 | Outputs attributable | PASS |
| Part 3, Amendment 1 | No authority overreach | **CAUTION** — unbounded file write scope; extension hook auto-execution |

---

### Execution Test

**Phase 4 — Deferred**: spec-kit not installed in LLM-Quickstart. Required before first use in a spec-kit-enabled project.

Key Phase 4 checks required:
- Verify extension hook auto-execution path is only triggered with valid extensions.yml
- Verify checklist gate actually halts on incomplete checklists
- Verify tasks.md task completion marking (`[X]`) functions correctly

---

### Decision

**APPROVED WITH CONDITIONS**

**Conditions:**
1. Target project must have spec-kit installed
2. **Review `.specify/extensions.yml` before every invocation** — mandatory hooks with `EXECUTE_COMMAND` auto-execute without user confirmation
3. Treat each `/speckit.implement` invocation as a high-impact action requiring user awareness of full task scope
4. Phase 4 execution test required before first production use
5. Ensure clean git state and any valuable uncommitted work is stashed before invocation
6. In LLM-Quickstart: will fail at script step — expected behavior

**Approved by:** Joshua Alexander Clement + claude-sonnet-4-6, 2026-03-14
