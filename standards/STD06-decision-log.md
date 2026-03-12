# STD06 — Decision Log Standard

**Type**: Standard
**Number**: STD06
**Status**: Ratified
**Constitutional Authority**: `memory/constitution.md` Article XII (Accountability), Article VIII (Honesty & Transparency)

---

## Purpose

When development reaches a fork — two or more valid approaches exist and one must be chosen — the choice and its reasoning must be recorded. This prevents the same question from being relitigated in future sessions and gives any reader the context to understand why the system is the way it is.

A decision record is a first-class document. It is as important as the spec or the standard it informs.

---

## 1. What Belongs in a Decision Record

**Appropriate when:**
- Two or more reasonable approaches existed
- The choice has lasting consequences on the system
- A future session might otherwise revisit the question without context

**Not appropriate for:**
- Choices with only one reasonable option
- Routine implementation details with no meaningful alternatives
- Choices that were immediately reversed

---

## 2. Location and Naming

Decision records live in `registry/decisions/` following STD01:

```
registry/decisions/D01-descriptive-name.md
```

---

## 3. Required Format

```markdown
# D## — [Decision Title]

**Date**: YYYY-MM-DD
**Status**: Accepted | Superseded by D##
**Decided by**: [Owner name or role]

---

## Context

What situation prompted this decision? What constraints were in play?

## Options Considered

### Option A — [Name]
[Description and tradeoffs]

### Option B — [Name]
[Description and tradeoffs]

## Decision

Option [X] was chosen. [One paragraph explaining why.]

## Consequences

What does this decision make easier? What does it make harder or rule out?

---

## Revision History

| Rev | Date | Author | Why |
|---|---|---|---|
| 1.0 | YYYY-MM-DD | [Author] | Initial record |
```

---

## 4. Superseding a Decision

If a decision is later reversed, do not delete the original record. Create a new decision record (D##) and mark the original as `Status: Superseded by D##`. This preserves the reasoning history — understanding why something was changed requires knowing what it was changed from.

---

## 5. Constitutional and Architectural Decisions

Decisions that result in changes to `memory/constitution.md` must additionally go through the change management process defined in `docs/change-management.md`. The decision record and the change management record cross-reference each other.

---

## Revision History

| Rev | Date | Author | Why |
|---|---|---|---|
| 1.0 | 2026-03-10 | Claude | Initial creation, adapted from Clement-Personal-Assistant STD06 |
