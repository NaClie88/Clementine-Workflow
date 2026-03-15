## Skill Review: speckit.constitution

**Source**: External — `https://github.com/github/spec-kit` (`templates/commands/constitution.md`)
**Skill type**: Pure-prompt (no scripts)
**Date reviewed**: 2026-03-14
**Reviewed by**: Joshua Alexander Clement + claude-sonnet-4-6
**Risk classification**: Medium
**Dependency chain**: spec-kit templates must be present (`.specify/templates/constitution-template.md`)

---

### Static Analysis

**§2.0 File Inventory**

| File | Category |
|---|---|
| `templates/commands/constitution.md` | Skill definition (pure-prompt, no `scripts:` key) |

No bash scripts, MCP config, hooks, or agents/.

**§2.1 Tool Inventory**

| Tool | Risk | Notes |
|---|---|---|
| `Read` | Low | Loads `.specify/memory/constitution.md` and template files |
| `Write` | Medium | Overwrites `.specify/memory/constitution.md` |
| `Read` | Low | Reads `.specify/templates/plan-template.md`, `spec-template.md`, `tasks-template.md`, command files for propagation check |
| `Write` | Low–Medium | May update those template files to propagate principle changes |

**§2.2 File Scope Analysis**

Primary write: `.specify/memory/constitution.md`. Secondary writes: may update template files under `.specify/templates/` if constitution changes require propagation. Write scope is bounded to `.specify/` directory.

**⚠️ CRITICAL PATH MISMATCH — LLM-Quickstart context**

This command operates on `.specify/memory/constitution.md`. LLM-Quickstart's constitution is at `memory/constitution.md` (no `.specify/` prefix). These are **different files**. If invoked in LLM-Quickstart:
- Attempts to read `.specify/memory/constitution.md` — file does not exist
- Falls back to copying `.specify/templates/constitution-template.md` — also absent
- Would create a **new, separate constitution file** at `.specify/memory/constitution.md`
- Our actual governance document (`memory/constitution.md`) would be **untouched and unaffected**, but the new file would create **authority ambiguity** — two competing constitutions

**This command must not be used in LLM-Quickstart** without adapting the path references.

**§2.3 Network Scope Analysis**

No network calls. Pure-prompt, file operations only.

**§2.4 Prompt Injection Scan**

No override instructions. `$ARGUMENTS` supplies principle values but does not control file paths. The command enforces constitutional versioning (MAJOR/MINOR/PATCH) and requires propagation checks. No bypass language.

**§2.5 Hook and Injection Analysis**

No scripts, hooks, or MCP tools. Not applicable.

---

### Constitutional Review

| Part | Check | Result |
|---|---|---|
| Part 1, Amendment 5 | No oversight bypass | PASS — in a fresh spec-kit project |
| Part 1, Amendment 5 | No oversight bypass | **CAUTION in LLM-Quickstart** — creating a parallel constitution file undermines governance clarity |
| Part 5, Amendment 1 | No deception | PASS — sync impact report is produced |
| Part 5, Amendment 4 | No unauthorized data handling | PASS |
| Part 5, Amendment 5 | Outputs attributable | PASS |
| Part 3, Amendment 1 | No authority overreach | PASS — in spec-kit projects; CAUTION in LLM-Quickstart |

---

### Execution Test

**Phase 4 — Not applicable**: Pure-prompt command, no script execution.

---

### Decision

**APPROVED WITH CONDITIONS** — for use in fresh spec-kit-initialized projects only.

**Conditions:**
1. **NOT for use in LLM-Quickstart** — path mismatch would create a parallel constitution at `.specify/memory/constitution.md`, separate from the governing `memory/constitution.md`
2. Only invoke in projects where spec-kit is fully installed and `.specify/memory/constitution.md` is the authoritative constitution path
3. After any constitution update, human review of the Sync Impact Report is required before the updated constitution is treated as authoritative
4. Version bump type (MAJOR/MINOR/PATCH) must be confirmed with the user before writing

**Approved by:** Joshua Alexander Clement + claude-sonnet-4-6, 2026-03-14
