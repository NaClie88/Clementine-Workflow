# STD02 — Document Revision History Standard

**Type**: Standard
**Number**: STD02
**Status**: Ratified
**Constitutional Authority**: `memory/constitution.md` Article XII (Accountability)

---

## Purpose

Every document must carry a record of when and why it changed. This allows any reader — human or AI — to understand the current state of a document and the reasoning behind its evolution without reading every prior version.

---

## 1. Required Format

Every document must end with a Revision History table:

```markdown
## Revision History

| Rev | Date | Author | Why |
|---|---|---|---|
| 1.0 | YYYY-MM-DD | [Author] | Initial creation |
| 1.1 | YYYY-MM-DD | [Author] | [Reason for change] |
```

### Rules

- **Rev**: semantic versioning — `1.0` for initial, `1.1` for minor additions or clarifications, `2.0` for changes that alter the document's fundamental meaning
- **Date**: ISO 8601 format (`YYYY-MM-DD`)
- **Author**: the person or AI session that made the change
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

| Rev | Date | Author | Why |
|---|---|---|---|
| 1.0 | 2026-03-10 | Claude | Initial creation, adapted from Clement-Personal-Assistant STD02 |
