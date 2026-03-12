# STD03 — Commit Message Convention

**Type**: Standard
**Number**: STD03
**Status**: Ratified
**Constitutional Authority**: `memory/constitution.md` Article XII (Accountability), Article VIII (Honesty & Transparency)

---

## Purpose

Commit messages are the primary record of why the project changed at each point in time. A well-formed commit message lets any reader — including an AI session with no prior context — reconstruct the reasoning behind a change without reading the diff. The diff shows what changed. The message explains why.

---

## 1. Format

```
type(scope): short summary in present tense

Optional body — explain why, not what.
```

### Type

| Type | When to use |
|---|---|
| `feat` | New document, new standard, new deployment content |
| `fix` | Correcting an error in existing content |
| `refactor` | Restructuring without changing meaning |
| `docs` | Administrative documentation (README, progress tracking) |
| `chore` | Housekeeping — moving files, renaming, updating registry |

### Scope

The scope is the document code or folder affected: `STD01`, `memory`, `registry`, `specs`. Omit scope only when the change spans the whole project.

### Summary

- Present tense: "add", "fix", "remove" — not "added", "fixed", "removed"
- 72 characters or fewer
- No full stop at the end

---

## 2. Examples

```
feat(STD01): add document naming convention

feat(memory): ratify constitution v1.0

fix(docs/guardrails): correct escalation trigger for prompt injection

refactor(specs): rename deployment spec to match branch convention

docs(registry): update progress after STD03 ratification

chore: move operational docs from governance/ to docs/
```

---

## 3. Co-authorship

When a commit is produced with AI assistance, append:

```
Co-Authored-By: [Model Name] <noreply@anthropic.com>
```

---

## Revision History

| Rev | Date | Author | Why |
|---|---|---|---|
| 1.0 | 2026-03-10 | Claude | Initial creation, adapted from Clement-Personal-Assistant STD03 |
