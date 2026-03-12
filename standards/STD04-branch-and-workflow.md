# STD04 — Branch Naming and Development Workflow

**Type**: Standard
**Number**: STD04
**Status**: Ratified
**Constitutional Authority**: `memory/constitution.md` Article XII (Accountability)

---

## Purpose

Defines how work is branched, reviewed, and merged so that `main` always reflects ratified, complete work and in-progress changes are clearly isolated.

---

## 1. Branch Types

| Branch | Pattern | Purpose |
|---|---|---|
| Main | `main` | Ratified, complete work only. Never commit directly. |
| Feature | `feat/STD##-description` or `feat/description` | New standards, constitution changes, new deployment docs |
| Fix | `fix/description` | Corrections to existing documents |
| Chore | `chore/description` | Housekeeping, restructuring, registry updates |

### Naming Rules

- Lowercase kebab-case only
- Include the document code where the work is scoped to a specific document
- Short enough to be readable in a branch list

### Examples

```
feat/STD08-brand-standard
feat/001-llm-deployment-spec
fix/guardrails-escalation-trigger
chore/restructure-docs-to-flat
```

---

## 2. Workflow

1. Cut a branch from an up-to-date `main`
2. Do all work on the branch
3. Commit following STD03 — Commit Message Convention
4. Push and open a pull request to `main`
5. Merge only when the work is complete and self-consistent
6. Delete the branch after merge

---

## 3. AI Session Branches

When an AI session is doing extended work, the branch name may include a short random suffix to distinguish parallel sessions:

```
feat/STD08-brand-standard-AdxCj
```

The suffix is generated at session start and kept for the duration of that session's work.

---

## 4. Pull Request Review Criteria

Before merging a pull request, the reviewer must confirm:

| Check | Criterion |
|---|---|
| **Complete** | All intended changes are included — no half-applied edits, no broken cross-references |
| **Self-consistent** | No document in the PR contradicts another document in the same PR or in `main` |
| **Standard-compliant** | All affected documents have a metadata block, numbered sections, and a revision history entry (per STD02, STD08) |
| **No new dependencies** | If code or tooling was modified, no unapproved dependencies were introduced (STD09) |
| **Constitution-safe** | No change conflicts with `memory/constitution.md` — critical changes must go through `docs/change-management.md` first |

"Self-consistent" is not satisfied by the absence of obvious conflicts. The reviewer must check that every cross-reference (`See STD03 §2`, `D01`) still points to something real and accurate.

For AI-authored PRs: the checklist above must be verified by a human reviewer before merge.

---

## 5. Never on Main

- Never force-push to `main`
- Never commit unfinished work directly to `main`
- Never rewrite history on `main`

---

## Revision History

| Rev | Date | Author | Why |
|---|---|---|---|
| 1.0 | 2026-03-10 | Claude | Initial creation, adapted from Clement-Personal-Assistant STD04 |
| 1.1 | 2026-03-12 | Claude | Added §4 PR review criteria — defined "self-consistent" and added merge checklist |
