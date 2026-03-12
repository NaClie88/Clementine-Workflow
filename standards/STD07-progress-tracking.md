# STD07 — Progress Tracking

**Type**: Standard
**Number**: STD07
**Status**: Ratified
**Constitutional Authority**: `memory/constitution.md` Article XII (Accountability)

---

## Purpose

`registry/progress.md` is the single source of truth for the current state of this project. It tells any reader — human or AI — what is done, what is in progress, and what the last session left behind. It must always be current.

---

## 1. Required Sections

`registry/progress.md` must contain, in order:

### Session Briefing

The first section. Contains:
1. The mandatory read list (per STD05 §1)
2. The last session note

This section must remain first so it is the first thing any session reads.

### Active Work

A table of documents and tasks currently in progress:

```markdown
| Document | Type | State | In state since | Notes |
|---|---|---|---|---|
| STD08 — Brand Standard | Standard | Draft | 2026-03-10 | Awaiting ratification |
```

**States:**
- Governance documents: `Draft` → `Review` → `Ratified`
- Deployment work: `Development` → `Testing` → `Deployed`
- Issues: `Open` → `In Progress` → `Resolved`

### Completed Work

A table of completed documents and tasks with their completion date.

```markdown
| Document | Type | Completed | Notes |
|---|---|---|---|
| STD01 — Document Naming | Standard | 2026-03-10 | Ratified |
```

### Key Files

A table of the most important files in the project with a one-line description of each. Updated when significant files are added or moved.

```markdown
| File | Description |
|---|---|
| `memory/constitution.md` | Governing law — highest authority |
| `AGENTS.md` | Runtime agent context — role, scope, voice |
| `registry/progress.md` | This file — current project state |
```

---

## 2. When to Update

Update `registry/progress.md`:
- At the end of every session (per STD05 §2.2)
- When any document changes state
- In the same commit as the state-changing work — not as a separate later commit

---

## 3. What Not to Put Here

`registry/progress.md` is a state tracker, not a log. Do not:
- Write narrative summaries of what was done
- Duplicate content already in the documents themselves
- Record decisions here — those belong in `registry/decisions/` per STD06

---

## Revision History

| Rev | Date | Author | Why |
|---|---|---|---|
| 1.0 | 2026-03-10 | Claude | Initial creation, adapted from Clement-Personal-Assistant STD07 |
