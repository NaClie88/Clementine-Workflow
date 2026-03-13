---
name: "curate"
description: "Memory curation with mandatory Operator review at every step. Analyzes MEMORY.md for patterns worth promoting to CLAUDE.md rules or reusable skills. Never writes to CLAUDE.md or .claude/ directly — outputs formatted text for the Operator to apply manually. Subcommands: review, promote [id], confirm [id], extract [id], status."
---

# Memory Curator

Analyzes Claude Code's auto-memory (`MEMORY.md`) and identifies patterns worth promoting to permanent project rules (`CLAUDE.md`) or reusable skills. Every promotion goes through a consequence check and requires your explicit review before anything is applied.

**This skill never writes to `CLAUDE.md`, `.claude/`, `~/.claude/`, `memory/constitution.md`, or `standards/`. All promotions are formatted text output for manual application by the Operator.**

---

## The Promotion Loop

```
MEMORY.md              ──► /curate review
(raw observations)         (numbered candidate list — READ ONLY)
                                    │
                                    ▼
                            Operator reviews list
                            selects candidates to promote
                                    │
                                    ▼
                           /curate promote [id]
                           (consequence check → formatted block for CLAUDE.md)
                                    │
                                    ▼
                            Operator reviews consequences,
                            pastes block into CLAUDE.md manually
                                    │
                                    ▼
                           /curate confirm [id]
                           (marks entry as promoted in MEMORY.md)
```

---

## Subcommands

### `/curate review`

Read `MEMORY.md` and any topic files it references. Analyze the full contents for:

**Promotion candidates** — patterns worth moving from notes to enforced rules:
- Coding or architectural patterns that have appeared 3 or more times
- Debugging solutions that solved a recurring class of problem
- Preferences the Operator has expressed repeatedly
- Decisions that should be consistently enforced going forward

**Stale entries** — entries that may no longer be accurate:
- Older than 30 days without reappearing
- Contradicted by a newer entry
- Superseded by a decision that was logged

**Consolidation opportunities** — multiple entries that say the same thing differently and should be merged.

**Output format** (read-only — nothing is written):

```
## Memory Curator — Review Report
Generated: [date]

### Promotion Candidates

[P1] [Short title]
     Summary: [What the pattern says]
     Type: rule | preference | architecture | debug-solution
     Frequency: [N occurrences / explicitly flagged]
     Proposed destination: CLAUDE.md § [suggested section]

[P2] ...

### Stale Entries

[S1] [Entry summary] — Last active: [date]. Possible reason stale: [explanation]

### Consolidation Opportunities

[C1] Entries [x, y, z] overlap — suggest merging into: [canonical version]

---
[N] promotion candidates | [S] stale entries | [C] consolidation opportunities

To promote a candidate: /curate promote [P#]
To extract a candidate as a skill: /curate extract [P#]
To check memory health: /curate status
```

If `MEMORY.md` does not exist: "No auto-memory found. MEMORY.md does not exist in this project."

---

### `/curate promote [id]`

Takes a candidate ID from the most recent `/curate review` output.

**Step 1 — Consequence check**

Before generating the block, reason through the following explicitly. Do not skip this step.

- Does this rule conflict with any existing rule or instruction in `CLAUDE.md`?
- Is this rule specific enough to be enforceable, or is it too vague?
- Could this rule be overly broad — catching cases where it should not apply?
- Does enforcing this rule reduce flexibility in ways that might cause problems later?
- Does this rule interact with any constitutional principle or standard?

State each finding clearly, even if the finding is "no concern identified."

**Step 2 — Generate the formatted block**

Output the following (nothing is written to any file):

```
## Proposed CLAUDE.md Addition — [Candidate title]

Paste the following into CLAUDE.md under [suggested section]:

────────────────────────────────────────────
[Rule text, formatted and ready to paste]
────────────────────────────────────────────

⚠ Consequence review (complete before applying):
  - [Conflict check result]
  - [Scope assessment]
  - [Flexibility impact]
  - [Any constitutional or standards concerns]

Once you have applied it manually, run: /curate confirm [id]
To discard this candidate, simply do nothing — it remains in MEMORY.md.
```

**Step 3 — Wait**

Do not write anything. The Operator applies the change manually. This is intentional — Claude does not have authority to modify project rules unilaterally.

---

### `/curate confirm [id]`

Called by the Operator after manually applying a promotion to `CLAUDE.md`.

1. Retrieve the candidate entry from the most recent review
2. Draft the update to mark it promoted in `MEMORY.md`:

   Append `[promoted YYYY-MM-DD]` to the relevant entry

3. Show the exact change and ask: **"Mark entry [id] as promoted in MEMORY.md? (yes / no)"**

4. Write only if confirmed.

5. Confirm after writing: "Entry [id] marked as promoted in MEMORY.md."

This keeps MEMORY.md accurate and prevents re-flagging already-promoted patterns.

---

### `/curate extract [id]`

Turns a promotion candidate into a reusable skill file template.

1. Generate a `SKILL.md` template based on the pattern:

```markdown
---
name: "[skill-name]"
description: "[One-line description of what this skill does and when to invoke it]"
---

# [Skill Name]

[What this skill does and why it exists]

## When to Use
[Specific situations this skill applies to]

## Behaviour
[Step-by-step description of what Claude should do when invoked]

## Rules
[Constraints and limits — what this skill never does]
```

2. Display the complete template.

3. Specify the save path: `skills/[skill-name]/SKILL.md`
   Note: This is a staging directory, **not** `.claude/commands/`.

4. Ask: **"Save this template to skills/[skill-name]/SKILL.md? (yes / no)"**

5. If confirmed, write to `skills/[skill-name]/SKILL.md`.

6. After writing, output this mandatory notice:

```
Template saved to skills/[skill-name]/SKILL.md.

Before this skill can be used, it must complete the vetting workflow:
  docs/skill-vetting-workflow.md — Phase 1 through Phase 5

Do not move it to .claude/commands/ until it has been reviewed,
approved, and added to docs/approved-skills.md §2.
```

---

### `/curate status`

Read-only memory health report. Nothing is written.

Report:
- `MEMORY.md` existence and line count
  - Flag if approaching 200 lines (Claude Code's context truncation limit)
- Topic files referenced (names and sizes)
- Age range of entries (oldest and newest)
- Count of entries flagged as important vs. routine
- Count of entries already marked as promoted
- Recommendation if memory is crowded or stale

---

## Rules

- Never write to `CLAUDE.md`, `.claude/rules/`, `.claude/commands/`, `~/.claude/`, `memory/constitution.md`, or `standards/`
- The consequence check in `/curate promote` is mandatory — do not skip or compress it
- Never apply a promotion without showing the Operator the consequence check first
- The confirm step requires an explicit "yes" — silence is not confirmation
- `/curate extract` writes to `skills/` only — not `.claude/`; the skill must pass vetting before it moves
- If MEMORY.md does not exist, report it clearly and do not attempt to create it
- This skill does not install hooks, background processes, or session watchers of any kind
