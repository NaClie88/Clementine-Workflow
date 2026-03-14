# STD10 — AI Tool Usage Discipline

**Type**: Standard
**Number**: STD10
**Status**: Ratified
**Constitutional Authority**: `memory/constitution.md` Part 7, Amendment 4 (Coding Standards), Part 5, Amendment 2 (Respect for Persons — respect the user's time and attention)

---

## Purpose

Every tool call that requires user permission is an interruption. Unnecessary interruptions train the user to approve prompts without reading them — which is a security hazard, not a convenience. This standard defines the rules for choosing tools and batching operations to minimise the permission surface to the minimum required for the work being done.

A permission prompt that appears without a clear reason is waste. A permission prompt that appears because the AI chose the wrong tool is a process defect.

---

## 1. File Operations

### Rule: Prefer the dedicated file tools over Bash

| Task | Use This | Not This |
|---|---|---|
| Write a new file | `Write` tool | `Bash: cat > file` |
| Edit an existing file | `Edit` tool | `Bash: sed / awk / cat >>` |
| Read a file | `Read` tool | `Bash: cat / head / tail` |
| Find files | `Glob` tool | `Bash: find / ls` |
| Search file content | `Grep` tool | `Bash: grep / rg` |

**Why:** The `Write` and `Edit` tools each produce a single, clearly-described permission prompt that the user can review and approve or deny. A `Bash` call produces a shell command prompt that obscures what is happening — the user must read the raw command to understand the intent.

### Exception: Large file creation (token ceiling)

The `Write` tool passes file content as a parameter in the AI's response. For documents exceeding approximately 800–1000 lines, the content approaches the output token ceiling and the `Write` tool call may fail or be truncated.

When the `Write` tool cannot handle the full content in a single call:

1. **Write the first chunk with `cat > file`** — this creates and populates the file
2. **Append remaining chunks with `cat >> file`** — each subsequent call appends
3. **Minimise the number of chunks** — consolidate as many sections as possible per call; target ≤ 3 Bash calls for the full file
4. **Label each call clearly** in the description field: `"Write section 1–3 of 5 to new file"`

This is the only acceptable use of `cat >` / `cat >>` in Bash. For files of normal size, use the `Write` tool without exception.

---

## 2. Git Operations

### Rule: Batch git operations into a single Bash call

Git add, commit, and push are almost always performed together. Each as a separate call is three permission prompts where one is sufficient.

**Standard form — do this:**
```bash
git add file1.md file2.md && git commit -m "message" && git push
```

**Not this (three prompts for one logical operation):**
```bash
git add file1.md file2.md   # prompt 1
git commit -m "message"     # prompt 2
git push                    # prompt 3
```

### When to keep git operations separate

Split git operations only when there is a decision point between them that requires user input or tool output:

- When you need to inspect `git status` or `git diff` before deciding what to stage
- When a `git commit` might fail due to a hook, and the failure output must be read before proceeding
- When you are uncertain which files to include and need to verify with `git status` first

In those cases, run the diagnostic command first (one Bash call), then the full sequence (one Bash call). Two prompts, not four.

---

## 3. General Bash Discipline

### Default: avoid Bash when a dedicated tool exists

The system provides dedicated tools for the most common operations. Bash is reserved for operations that require shell execution — system commands, pipelines, and processes with no dedicated tool equivalent.

Before reaching for Bash, ask: is there a dedicated tool that does this?

| If you need to... | First try... |
|---|---|
| Read file content | `Read` tool |
| Search for text | `Grep` tool |
| Find files by name | `Glob` tool |
| Write or overwrite a file | `Write` tool |
| Make a targeted edit | `Edit` tool |

### Combining independent Bash commands

When multiple Bash commands are independent (neither depends on the other's output), run them in a single message as parallel tool calls rather than sequential separate calls. This does not reduce the number of prompts but reduces the elapsed time.

When commands are sequential and must all succeed, chain them with `&&`:
```bash
command1 && command2 && command3
```

Use `;` only when later commands should run regardless of earlier failures — which is rarely the right behaviour.

---

## 4. Measuring Permission Surface

As a rough guide, any single logical operation — "write this file", "commit this work", "run this test" — should produce at most 1–2 permission prompts. More than that is a signal that the operation was not batched correctly or the wrong tools were used.

| Operation | Expected prompts | Red flag |
|---|---|---|
| Write a normal file | 1 (Write tool) | > 1 |
| Write a large file (chunked) | 2–3 (Bash) | > 4 |
| Commit and push | 1 (batched Bash) | > 2 |
| Edit an existing file | 1 (Edit tool) | > 1 |
| Read + edit + commit | 3 (Read, Edit, Bash) | > 4 |

If a session produced significantly more prompts than this table implies, it is a process defect to note in the session retrospective.

---

## Revision History

| Rev | Date | Author | Why |
|---|---|---|---|
| 1.0 | 2026-03-14 | Joshua Alexander Clement — claude-sonnet-4-6 | Created from direct observation: 9 Bash prompts generated to write one document + git commit. Root causes: large file chunking used Bash instead of Write tool; git add/commit/push run as 3 separate calls instead of 1. |
