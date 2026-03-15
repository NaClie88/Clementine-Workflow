## Skill Review: speckit.taskstoissues

**Source**: External — `https://github.com/github/spec-kit` (`templates/commands/taskstoissues.md`)
**Skill type**: MCP-backed (`github/github-mcp-server/issue_write`) + script-backed (bash)
**Date reviewed**: 2026-03-14
**Reviewed by**: Joshua Alexander Clement + claude-sonnet-4-6
**Risk classification**: High
**Dependency chain**: spec-kit installed; `github/github-mcp-server` MCP configured; tasks.md must exist

---

### Static Analysis

**§2.0 File Inventory**

| File | Category |
|---|---|
| `templates/commands/taskstoissues.md` | Skill definition |
| `scripts/bash/check-prerequisites.sh` | Bash script (invoked with `--json --require-tasks --include-tasks`) |
| `scripts/bash/common.sh` | Bash script (sourced) |
| `github/github-mcp-server` | MCP server (external, not local) |

**§2.1 Tool Inventory**

| Tool | Risk | Notes |
|---|---|---|
| `Bash` | Low | Runs `check-prerequisites.sh --json --require-tasks --include-tasks` |
| `Bash` | Low | `git config --get remote.origin.url` — read-only git operation |
| `github/github-mcp-server/issue_write` | **High** | Creates GitHub issues — external, visible, not easily reversible |

**§2.2 File Scope Analysis**

Reads: tasks.md. No local file writes. All output is external: GitHub issues.

**§2.3 Network Scope Analysis**

**External action**: Creates GitHub issues in the repository matching the git remote URL. Each task becomes a GitHub issue. This is:
- **External to the local system** — affects shared GitHub state
- **Visible to all collaborators and watchers**
- **Not easily reversible** (issues must be individually closed/deleted; deletion requires separate API call or manual action)

**§2.4 Prompt Injection Scan**

Two `[!CAUTION]` blocks are explicit safety guardrails:
1. "ONLY PROCEED TO NEXT STEPS IF THE REMOTE IS A GITHUB URL"
2. "UNDER NO CIRCUMSTANCES EVER CREATE ISSUES IN REPOSITORIES THAT DO NOT MATCH THE REMOTE URL"

These are **prompt-level instructions** — they do not provide technical enforcement. A manipulated `tasks.md` containing issue creation directives could potentially influence behavior, though the command's explicit [!CAUTION] framing makes this a red flag trigger.

**§2.5 Hook and Injection Analysis**

No extension hooks in taskstoissues. Bash script is local. MCP server `github/github-mcp-server` handles the external action.

---

### Script Analysis

**§2.6.1 Shell Script**

check-prerequisites.sh in `--require-tasks --include-tasks` mode. See speckit-analyze.md §2.6.1. No writes. Validates tasks.md exists.

**§2.6.2 MCP Tool: github/github-mcp-server/issue_write**

| Concern | Assessment |
|---|---|
| External action | Yes — creates issues on GitHub |
| Reversibility | Low — issues persist until closed/deleted; notifications sent to watchers |
| Scope creep risk | High if remote URL check bypassed |
| Cross-repo risk | Addressed by [!CAUTION] blocks (prompt-level only) |
| Issue count | Not shown to user before creation — no "create N issues?" confirmation step |

**Missing safeguard**: The command does not include a step to summarize and confirm the number of issues to be created before invoking `issue_write`. A tasks.md with 50 tasks would create 50 GitHub issues without a single user confirmation step (beyond the initial `/speckit.taskstoissues` invocation).

---

### Constitutional Review

| Part | Check | Result |
|---|---|---|
| Part 1, Amendment 5 | No oversight bypass | **CAUTION** — creates external visible actions without pre-creation count confirmation |
| Part 5, Amendment 1 | No deception | PASS — [!CAUTION] blocks are explicit |
| Part 5, Amendment 4 | No unauthorized data handling | PASS — data goes to intended repo only |
| Part 5, Amendment 5 | Outputs attributable | PASS — issues attributed to authenticated user |
| Part 3, Amendment 1 | No authority overreach | **CAUTION** — external action on shared system |

---

### Execution Test

**Phase 4 — Deferred**: github-mcp-server not confirmed as configured; spec-kit not installed.

Prerequisite before first use:
- Confirm `github/github-mcp-server` is configured and authenticated in this environment
- Test with a private/test repository first before use on any production repo
- Verify remote URL check actually gates execution (not just printed warning)

---

### Decision

**APPROVED WITH CONDITIONS** — highest-risk command in the spec-kit suite. Treat as a high-impact, potentially-irreversible action.

**Conditions:**
1. `github/github-mcp-server` MCP server must be configured and authenticated
2. **Before each use: confirm issue count with user** — summarize task list and ask "Create N issues in [repo]?" before invoking `issue_write`
3. Remote URL must be verified to match intended repository before any issue creation
4. Only invoke in projects where the git remote is explicitly the intended target repo
5. Not for use in shared/organization repos without explicit authorization from the repo owner
6. Target project must have spec-kit installed (for check-prerequisites.sh)
7. Phase 4 test in a disposable repository required before first production use

**Note on missing safeguard**: The spec-kit command does not include a pre-creation count confirmation step. This must be enforced at the skill invocation level (condition 2 above) by the operator adapting this command to their context.

**Approved by:** Joshua Alexander Clement + claude-sonnet-4-6, 2026-03-14
