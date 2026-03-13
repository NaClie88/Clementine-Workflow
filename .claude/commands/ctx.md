---
name: "ctx"
description: "Manages persistent company context at memory/company-context.md. Subcommands: load (display context), status (health check), update [dimension] [value] (propose a change — requires Operator confirmation before writing), init (create from template with Operator input)."
---

# Company Context Manager

Manages the company knowledge base at `memory/company-context.md`. Provides persistent context to c-level advisor sessions so you don't re-explain your company every session.

**All writes require explicit Operator confirmation in the current session. Never update the context file autonomously.**

---

## Subcommands

### `/ctx load`

Read `memory/company-context.md` and display it formatted by dimension.

- If the file does not exist: output "No company context found. Run `/ctx init` to create one."
- If last updated more than 90 days ago: flag as stale and suggest `/ctx status`

---

### `/ctx status`

Read `memory/company-context.md` and report:

- Last updated date and days since last update (flag stale if >90 days)
- Which dimensions are populated and which are empty
- Approximate word count per dimension
- Overall completeness assessment

If the file does not exist, report that and suggest `/ctx init`.

---

### `/ctx update [dimension] [proposed value]`

1. Read the current `memory/company-context.md`
2. Display the current value of `[dimension]`
3. Display the proposed new value
4. State exactly what will change and what will not change
5. Ask: **"Apply this update to memory/company-context.md? (yes / no)"**
6. Write only if the Operator responds yes in this session
7. Confirm after writing: "Updated [dimension] — memory/company-context.md saved."

If the file does not exist, redirect to `/ctx init`.

---

### `/ctx init`

1. Check if `memory/company-context.md` already exists
   - If yes: "Company context already exists. Use `/ctx update [dimension]` to modify individual dimensions, or `/ctx load` to review it."
   - If no: proceed

2. Walk through each dimension one at a time, asking the Operator for a value. Accept "—" or blank to skip a dimension.

3. After collecting all values, display the complete proposed file.

4. Ask: **"Create memory/company-context.md with this content? (yes / no)"**

5. Write only if the Operator confirms.

6. Confirm after writing: "Created memory/company-context.md."

---

## Context File Format

```markdown
# Company Context

**Last Updated**: YYYY-MM-DD

## Company
[Mission, stage (pre-seed / seed / Series-A / etc.), founding year, team size, HQ]

## Product
[Core offering, key features, primary differentiator]

## Market
[Target customer, ICP description, key segments]

## Competition
[Named competitors and your positioning relative to each]

## Metrics
[Key business KPIs and current values — update when they change materially]

## Voice
[Tone, communication style, brand personality]

## Team
[Key roles, decision makers, org structure notes]
```

---

## Rules

- Never modify `memory/company-context.md` without an explicit "yes" from the Operator in the current session
- Never infer or assume values — only record what the Operator explicitly provides
- If the Operator mentions something during a session that seems like context worth capturing (e.g., a new competitor, a metric update), note it and ask: "Should I add this to company context?" — never add it without asking
- The context file is the Operator's source of truth — treat stated values as authoritative; do not fact-check or contradict them
- This skill never accesses `~/.claude/`, `memory/constitution.md`, `standards/`, or `AGENTS.md`
