---
name: "session-start"
description: "Start a working session — read project state, last session note, active work, and governing rules. Outputs a compact status briefing. Use at the beginning of any session on this project."
---

# Session Start

Follow STD05. Read in this exact order — do not skip steps, do not begin work first.

## Step 1 — Read project state

Read `registry/progress.md` in full. Note:
- The Last Session Note (what the previous session left behind)
- Every row in the Active Work table
- Any warnings or blockers flagged

## Step 2 — Read governing law

Read `memory/constitution.md`. You do not need to summarise it — you need to have read it so its constraints are in context for this session.

## Step 3 — Read session rules

Read `standards/STD05-ai-session-continuity.md`. Note any session-end obligations you will need to fulfil before closing.

## Step 4 — Read active work documents

For each document listed in the Active Work table of `registry/progress.md`: read it (or skim if large — enough to understand current state and next step).

If Active Work is empty, skip this step.

## Step 5 — Check branch

Run `git status` and `git log --oneline -5`. Confirm the branch is correct and the working tree is clean. Note any uncommitted changes.

## Step 6 — Output briefing

Respond with exactly this structure — keep it under 12 lines total:

```
SESSION OPEN — [date]

Last worked on: [one sentence from the Last Session Note]
Active:
  • [item 1]
  • [item 2]
  (or "None — clean docket")
Warnings: [anything flagged in the session note, or "None"]
Branch: [branch name] — [clean / N files uncommitted]

Ready.
```

Do not add commentary, summaries, or suggestions beyond this output. The user will direct what happens next.

## Rules

- Complete all 6 steps before outputting the briefing
- If `registry/progress.md` is missing: stop, report it, do not proceed
- If `memory/constitution.md` is missing: stop, report it, do not proceed
- If any active work document is missing: note it in the Warnings line, then continue
- Do not begin any work until the briefing has been output and the user responds
