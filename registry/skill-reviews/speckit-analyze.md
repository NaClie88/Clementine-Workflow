## Skill Review: speckit.analyze

**Source**: External — `https://github.com/github/spec-kit` (`templates/commands/analyze.md`)
**Skill type**: Script-backed (bash)
**Date reviewed**: 2026-03-14
**Reviewed by**: Joshua Alexander Clement + claude-sonnet-4-6
**Risk classification**: Low
**Dependency chain**: spec-kit must be installed in target project

---

### Static Analysis

**§2.0 File Inventory**

| File | Category |
|---|---|
| `templates/commands/analyze.md` | Skill definition (deployed as `.claude/commands/speckit.analyze.md`) |
| `scripts/bash/check-prerequisites.sh` | Bash script (invoked via `{SCRIPT}`) |
| `scripts/bash/common.sh` | Bash script (sourced by check-prerequisites.sh) |

No CLAUDE.md, hooks.json, settings.json, MCP config, plugin.json, or agents/ directory.

**§2.1 Tool Inventory**

| Tool | Risk | Notes |
|---|---|---|
| `Bash` | Low | Runs `check-prerequisites.sh --json --require-tasks --include-tasks` |
| `Read` | Low | Loads spec.md, plan.md, tasks.md, `/memory/constitution.md` for analysis |

**§2.2 File Scope Analysis**

**STRICTLY READ-ONLY** — explicitly stated in the command's operating constraints. Reads: spec.md, plan.md, tasks.md, constitution. Writes: **none**. Output is to stdout only. No user-controlled path construction.

**§2.3 Network Scope Analysis**

No network calls in bash script or prompt. check-prerequisites.sh reads local git repo state and file paths. No external endpoints.

**§2.4 Prompt Injection Scan**

No override instructions, constitution bypass, role replacement, or hidden instructions. Constitution authority reinforced: "non-negotiable within this analysis scope." No injection vectors found.

**§2.5 Hook and Injection Analysis**

No hooks.json, settings.json, CLAUDE.md, MCP config, agents/ directory. check-prerequisites.sh sources common.sh (local, no network). No injection vectors.

---

### Script Analysis

**§2.6.1 Shell Script — check-prerequisites.sh**

| Operation | Detail |
|---|---|
| `source "$SCRIPT_DIR/common.sh"` | Sources local sibling script — must be installed alongside |
| `get_feature_paths` | Reads git branch (`git rev-parse`), derives FEATURE_DIR from branch name |
| `check_feature_branch` | Validates current branch matches expected feature branch pattern |
| File stat checks | `[[ -f "$IMPL_PLAN" ]]`, `[[ -d "$FEATURE_DIR" ]]` — read-only |
| JSON output | `jq` or `printf` — stdout only |

No writes, no network calls, no subshells with user input, no `eval`.

**§2.6.2 Path Mismatch — Constitution Location**

The command loads `/memory/constitution.md` for constitutional validation. In LLM-Quickstart, the constitution is at `memory/constitution.md` (relative to repo root). Path resolves identically if invoked from repo root. **No issue.**

**§2.6.3 spec-kit Compatibility Prerequisite**

`check-prerequisites.sh` requires spec-kit's git-branch naming convention (`.specify/specs/<number>-<name>/`) and the `common.sh` library. This command **cannot function** in a project that does not have spec-kit installed and configured. Will fail at `{SCRIPT}` step with a clear error.

---

### Constitutional Review

| Part | Check | Result |
|---|---|---|
| Part 1, Amendment 5 | No oversight bypass | PASS — read-only, output only |
| Part 5, Amendment 1 | No deception | PASS |
| Part 5, Amendment 4 | No unauthorized data handling | PASS — no external transmission |
| Part 5, Amendment 5 | Outputs attributable | PASS |
| Part 3, Amendment 1 | No authority overreach | PASS — explicitly instructs to offer remediation only, not apply it |

---

### Execution Test

**Phase 4 — Deferred**: `check-prerequisites.sh` is not installed in LLM-Quickstart (spec-kit not installed). Phase 4 execution test **required before first use in a spec-kit-enabled project**.

When running in a spec-kit project:
- Verify `check-prerequisites.sh` makes no network calls (strace or equivalent)
- Verify no files are created by the analysis run
- Confirm script exits non-zero if required artifacts are missing (safe fail)

---

### Decision

**APPROVED WITH CONDITIONS** — added to `docs/approved-skills.md` §2.

**Conditions:**
1. Target project must have spec-kit installed (scripts/bash/ present, feature branch convention active)
2. Phase 4 execution test required before first use in a spec-kit-enabled project
3. Read-only constraint must be preserved in any adaptation of this command
4. In LLM-Quickstart: will fail at script step (no spec-kit installed) — this is the safe/expected behavior

**Approved by:** Joshua Alexander Clement + claude-sonnet-4-6, 2026-03-14
