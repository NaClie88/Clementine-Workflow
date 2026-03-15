---
name: "session-end"
description: "End a working session — update progress.md, update memory if needed, commit all changes, and push. Enforces the STD05 session-end checklist. Use before closing any session on this project."
---

# Session End

Follow STD05 §2. Complete every step in order. Do not skip steps.

## Step 1 — Check working tree

Run `git status`. Identify all modified, staged, and untracked files that are intentional changes from this session.

If the working tree is clean and there is nothing to commit, confirm that and skip to Step 5.

## Step 2 — Update registry/progress.md

Make the following changes to `registry/progress.md`:

**Last Session Note** — Replace the existing note with a 2–3 sentence summary written for the next AI session (not for the user). Include:
- What was completed this session (be specific — name files and what changed)
- Anything left incomplete and what state it is in
- Any gotcha, decision pending, or warning the next session needs to know

If everything is complete and clean: `Session [date] (completed). [What was done]. Active Work queue is empty.`

**Verification line** — Append this as the final line of the Last Session Note (required, never skip):

Run the four checks, then record the result:
- **A** — File path references: do referenced paths exist on disk?
- **B** — Name/rename consistency: do any renamed files leave stale references elsewhere?
- **C** — Test suite: run tests if any exist; if docs-only session, say so explicitly
- **D** — Structural integrity: are governing docs (constitution, STD05) well-formed and complete?

```
Verification: ✅ A, B, C (skip — docs-only), D — all checks passed [date].
```
or
```
Verification: ❌ [category] — [what failed or was skipped and why] [date].
```

A missing verification line means the handoff is unverified. The next session must run the checks before starting new work.

**Active Work table** — Verify it accurately reflects what is still in progress. Move any items completed this session to the Completed Work table.

**Completed Work table** — Add a row for each document or decision completed this session. Use today's date.

## Step 3 — Update MEMORY.md (if needed)

Check `memory/MEMORY.md`. Update only if something material changed this session:
- New decisions recorded (add pointer to decision file)
- New key files added to the project
- New patterns or rules that should persist across sessions
- Anything in MEMORY.md that is now stale or wrong

If nothing changed, skip this step.

## Step 4 — Commit

Stage the files that changed this session. Do not use `git add -A` — stage files by name.

Write a commit message following STD03 (conventional commits):
```
type(scope): description

Assisted-By: [Your model name and ID from your system context]
```

Example: `Assisted-By: Claude Sonnet 4.6 (claude-sonnet-4-6)` — but use whatever model you actually are, not this example.

Common types for session-end commits: `docs`, `chore`, `feat`. The scope is the area of the project affected.

If this session's work was already committed incrementally during the session, write a session-close commit for `registry/progress.md` and any MEMORY.md changes only:
```
chore(session): close session — update progress and memory

Assisted-By: [Your model name and ID from your system context]
```

If the working tree was already clean at Step 1, skip this step.

## Step 5 — Push

```bash
git push
```

If the branch has no upstream yet: `git push -u origin [branch-name]`

## Step 6 — Confirm

Output a close report:

```
SESSION CLOSED — [date]

Committed: [commit hash] on [branch]
Files: [list of committed files, or "working tree was already clean"]
Pushed: yes

Next session will open to: [one sentence — what the next session note says]
```

## Rules

- Write the Last Session Note for the next AI session, not for the user — it is context for a reader who has no memory of this conversation
- `Assisted-By: [model name] ([model ID])` not `Co-Authored-By:` — Claude is an assistant, not an author. Use the model name from your system context, not a hardcoded value (see feedback_attribution_format.md)
- Stage files by name — never `git add -A`
- Do not end without pushing — unpushed commits are lost if the local environment resets
- Do not invent or fabricate commit hashes — run the actual `git push` and report the real hash
