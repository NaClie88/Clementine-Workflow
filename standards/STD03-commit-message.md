# STD03 — Commit Message Convention

**Type**: Standard
**Number**: STD03
**Status**: Ratified
**Constitutional Authority**: `memory/constitution.md` Part 5, Amendment 5 (Accountability), Part 5, Amendment 1 (Honesty & Transparency)

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
Co-Authored-By: [Operator Name] <operator>
Assisted-By: [Provider] [Tier] [Version] ([model-id]) <noreply@[provider-domain]>
```

| Field | Description | Example |
|---|---|---|
| `[Provider]` | The AI company or platform | `Anthropic`, `OpenAI`, `Google` |
| `[Tier]` | Model capability tier if applicable | `Haiku`, `Sonnet`, `Opus`, `GPT-4o`, `Gemini Pro` |
| `[Version]` | Version number | `4.6`, `2024-11-20` |
| `([model-id])` | The canonical, unambiguous model identifier | `claude-sonnet-4-6`, `gpt-4o-2024-11-20` |

Examples:

```
Assisted-By: Anthropic Claude Sonnet 4.6 (claude-sonnet-4-6) <noreply@anthropic.com>
Assisted-By: OpenAI GPT-4o 2024-11-20 (gpt-4o-2024-11-20) <noreply@openai.com>
Assisted-By: Google Gemini Pro 1.5 (gemini-1.5-pro) <noreply@google.com>
```

The model ID in parentheses is the auditable identifier. If a vulnerability is discovered in a specific model version, `git log --grep="[model-id]"` surfaces every commit that model produced. This only works if the ID is consistent and machine-readable — do not paraphrase it.

---

## Revision History

| Rev | Date | Author | Model | Why |
|---|---|---|---|---|
| 1.0 | 2026-03-10 | Claude | claude-sonnet-4-6 | Initial creation, adapted from Clement-Personal-Assistant STD03 |
| 1.1 | 2026-03-12 | Joshua Alexander Clement | claude-sonnet-4-6 | Updated co-authorship to require full model ID for vulnerability traceability; updated constitutional references |
