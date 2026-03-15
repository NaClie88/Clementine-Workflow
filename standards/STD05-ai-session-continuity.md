# STD05 — AI Session Continuity

**Type**: Standard
**Number**: STD05
**Status**: Ratified
**Constitutional Authority**: `memory/constitution.md` Part 5, Amendment 1 (Honesty & Transparency), Part 5, Amendment 5 (Accountability)

---

## Purpose

Each AI session starts with no memory of prior sessions. Without a formal protocol, context is reconstructed slowly or incorrectly, decisions already made are revisited, and work drifts from established standards. This standard defines what must be read at session start, what must be captured at session end, and how to hand off cleanly between sessions.

This applies to any AI session working on this system — development, configuration, deployment, or maintenance.

---

## 1. Session Start Protocol

Before any work begins, read in order:

| # | Document | Why |
|---|---|---|
| 1 | `registry/progress.md` | Current project state and last session note |
| 2 | `memory/constitution.md` | Governing law — confirms constraints before work begins |
| 3 | This document (STD05) | Session rules |
| 4 | Any documents listed as active in `registry/progress.md` | What is currently in progress |
| 5 | `AGENTS.md` | Deployment context if working on a specific deployment |

### If a Required File Is Missing

Do not proceed with the session if any item in the read list above is missing or unreadable. A missing required file is a blocker, not an inconvenience.

| Situation | Action |
|---|---|
| `registry/progress.md` is missing | Stop. Notify the user. Do not begin work without known project state. |
| `memory/constitution.md` is missing | Stop. The governing law cannot be assumed from memory. |
| STD05 (this document) is missing | This situation is self-resolving — if you are reading this, it exists. |
| Any active document listed in progress.md is missing | Flag it. Continue read list, then notify before beginning work on affected areas. |
| `AGENTS.md` is missing for a deployment session | Stop if the session is deployment-specific. Proceed with template work if not deployment-specific. |

Do not reconstruct or infer a missing document's contents from memory or prior sessions. Each session must read the live document.

### Verify the branch

Before any commits:

```bash
git status
git log --oneline -5
```

Confirm you are on the correct branch. Do not commit to `main` directly (see STD04).

---

## 2. Session End Protocol

### 2.1 Commit all work

All meaningful changes must be committed before ending the session, following STD03 — Commit Message Convention. Do not leave uncommitted changes — the next session may start on a different machine or branch.

If work is incomplete, use a WIP commit so nothing is lost:

```
chore: WIP — [description of incomplete state]
```

### 2.2 Update registry/progress.md

Update `registry/progress.md` to reflect the current project state — what is done, what is in progress, what changed this session. See STD07 — Progress Tracking for the required format.

### 2.3 Write the last session note

Update the **Last session note** in `registry/progress.md`. Write it for the next session, not for the project owner. Include:

- Any work left incomplete and what state it is in
- Any decision pending the owner's input
- Any context not obvious from the documents alone
- Any warning or gotcha discovered during the session

If nothing needs handing forward:
```
Last session note: No outstanding context. All work committed and pushed.
```

### 2.4 Push before ending

```bash
git push -u origin [branch-name]
```

Unpushed commits exist only locally. If the local environment resets between sessions, they are lost.

---

## 3. Working Directory Safety

Never rename or move the project root folder during an active session. The shell is anchored to the working directory path recorded at session start. If the root folder is renamed, all subsequent shell commands fail.

Perform root-folder renames only after ending the session cleanly, then reopen from the new path.

Renaming files and subdirectories within the project during a session is safe.

---

## 4. Context Handoff for LLM Deployments

When an AI session is working on a live LLM deployment (not just this template), the following must also be captured at session end:

- Any guardrail trigger events that occurred during the session
- Any override requests made and their outcomes
- Any knowledge source issues discovered (stale data, retrieval failures)
- Any user-reported issues not yet resolved

This context belongs in the deployment's incident log (`docs/logging-audit-policy.md`) as well as `registry/progress.md`.

---

## 5. Quick-Reference Checklist

**Session start:**
- [ ] Read `registry/progress.md` — noted current state and last session note
- [ ] Read `memory/constitution.md`
- [ ] Read STD05 (this document)
- [ ] Read active work documents
- [ ] All required files confirmed present — if any missing, stopped and notified user
- [ ] Verified correct branch with `git status`

**Session end:**
- [ ] All work committed (clean tree or WIP commit)
- [ ] `registry/progress.md` updated
- [ ] Last session note written
- [ ] Branch pushed to remote

---

## Revision History

| Rev | Date | Author | Why |
|---|---|---|---|
| 1.0 | 2026-03-10 | Claude | Initial creation, adapted from Clement-Personal-Assistant STD05; added LLM deployment handoff section |
| 1.1 | 2026-03-12 | Claude | Added missing-file protocol to §1 and checklist item — closes silent failure mode |
| 1.2 | 2026-03-15 | claude-sonnet-4-6 | Constitutional authority updated: Article VIII/XII → Part 5, Amendment 1 + Amendment 5 |
