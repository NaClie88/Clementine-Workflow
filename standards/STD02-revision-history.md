# STD02 — Document Revision History Standard

**Type**: Standard
**Number**: STD02
**Status**: Ratified
**Constitutional Authority**: `memory/constitution.md` Part 5, Amendment 5 (Accountability)

---

## Purpose

Every document must carry a record of when and why it changed. This allows any reader — human or AI — to understand the current state of a document and the reasoning behind its evolution without reading every prior version.

---

## 1. Required Format

Every document must end with a Revision History table:

```markdown
## Revision History

| Rev | Date | Author | Model | Why |
|---|---|---|---|---|
| 1.0 | YYYY-MM-DD | [Author] | [model-id or "human"] | Initial creation |
| 1.1 | YYYY-MM-DD | [Author] | [model-id or "human"] | [Reason for change] |
```

### Rules

- **Rev**: semantic versioning — `1.0` for initial, `1.1` for minor additions or clarifications, `2.0` for changes that alter the document's fundamental meaning
- **Date**: ISO 8601 format (`YYYY-MM-DD`)
- **Author**: the person who directed or owns the change — the Operator for AI-assisted work, the individual for human-only work
- **Model**: the full model ID if AI-assisted (e.g. `claude-sonnet-4-6`, `gpt-4o-2024-11-20`), or `human` if no AI was involved. Use the canonical model ID, not a display name — it must be machine-searchable. This enables vulnerability auditing: if a model version is found to have a flaw, every document it touched can be identified by searching this column.
- **Why**: one sentence describing why it changed — not what the new content says, but why the change was made

---

## 2. When to Add a Revision Entry

**Add an entry when:**
- The document is first created (Rev 1.0)
- Any substantive content change — new sections, changed rules, removed clauses
- The document's status changes (e.g. Draft → Ratified)

**Do not add an entry for:**
- Typo or formatting fixes that do not change meaning
- Reordering content without changing it

---

## 3. Position

The Revision History section must be the **last section** of every document. Nothing follows it.

---

## Revision History

| Rev | Date | Author | Model | Why |
|---|---|---|---|---|
| 1.0 | 2026-03-10 | Claude | claude-sonnet-4-6 | Initial creation, adapted from Clement-Personal-Assistant STD02 |
| 1.1 | 2026-03-12 | Joshua Alexander Clement | claude-sonnet-4-6 | Added Model column for vulnerability traceability; updated constitutional reference |
