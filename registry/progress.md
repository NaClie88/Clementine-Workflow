# registry/progress.md — Project State

## Session Briefing

### Mandatory Read List (per STD05 §1)

| # | Document | Why |
|---|---|---|
| 1 | This file (`registry/progress.md`) | Current state and last session note |
| 2 | `memory/constitution.md` | Governing law |
| 3 | `standards/STD05-ai-session-continuity.md` | Session rules |
| 4 | Active work documents listed below | What is in progress |

### Last Session Note

Session 2026-03-14 complete. Vetting queue fully cleared (skill-tester Phase 4 Docker passed). Constitution rewritten to v5.0 (Parts reordered by importance, Parts 2+3 merged into Conduct with two-tier hierarchy, 12 gaps from Garden Helper diff closed). Cross-references in docs/ and standards/ audited and corrected to new Part numbers. New: dev-philosophy-reference.md (107 entries with examples, strengths, weaknesses, mitigations). New: STD10 tool usage discipline. Fill in `[bracketed placeholders]` throughout `AGENTS.md`, `docs/knowledge-sources.md`, `docs/tool-use-policy.md`, and `docs/user-roles-permissions.md` before first deployment.

---

## Active Work

| Document | Type | State | In state since | Notes |
|---|---|---|---|---|
| — | — | — | — | No active work. Template is ready for deployment configuration. |

---

## Completed Work

| Document | Type | Completed | Notes |
|---|---|---|---|
| `memory/constitution.md` | Constitution | 2026-03-10 | Ratified — merged from constitutional-rules + conduct-policy |
| `AGENTS.md` | Agent Runtime File | 2026-03-10 | Ratified — merged from system-prompt + persona-voice-guide |
| `specs/llm-deployment/spec.md` | Specification | 2026-03-10 | Ratified |
| `specs/llm-deployment/plan.md` | Plan | 2026-03-10 | Ratified |
| `specs/llm-deployment/tasks.md` | Tasks | 2026-03-10 | Ratified |
| `docs/guardrails.md` | Reference | 2026-03-10 | Ratified |
| `docs/user-roles-permissions.md` | Reference | 2026-03-10 | Ratified |
| `docs/tool-use-policy.md` | Reference | 2026-03-10 | Ratified |
| `docs/memory-context-policy.md` | Reference | 2026-03-10 | Ratified |
| `docs/session-policy.md` | Reference | 2026-03-10 | Ratified |
| `docs/knowledge-sources.md` | Reference | 2026-03-10 | Ratified |
| `docs/response-quality-criteria.md` | Reference | 2026-03-10 | Ratified |
| `docs/evaluation-rubric.md` | Reference | 2026-03-10 | Ratified |
| `docs/logging-audit-policy.md` | Reference | 2026-03-10 | Ratified |
| `docs/incident-response.md` | Reference | 2026-03-10 | Ratified |
| `docs/change-management.md` | Reference | 2026-03-10 | Ratified |
| `standards/STD01-document-naming.md` | Standard | 2026-03-10 | Ratified |
| `standards/STD02-revision-history.md` | Standard | 2026-03-10 | Ratified |
| `standards/STD03-commit-message.md` | Standard | 2026-03-10 | Ratified |
| `standards/STD04-branch-and-workflow.md` | Standard | 2026-03-10 | Ratified |
| `standards/STD05-ai-session-continuity.md` | Standard | 2026-03-10 | Ratified |
| `standards/STD06-decision-log.md` | Standard | 2026-03-10 | Ratified |
| `standards/STD07-progress-tracking.md` | Standard | 2026-03-10 | Ratified |
| `standards/STD08-brand-standard.md` | Standard | 2026-03-10 | Ratified |
| `standards/STD09-approved-technology.md` | Standard | 2026-03-10 | Ratified |
| `standards/STD10-tool-usage-discipline.md` | Standard | 2026-03-14 | Ratified — tool and git operation batching to minimise permission prompts |
| `memory/constitution.md` | Constitution | 2026-03-14 | v5.0 — Parts reordered by importance ranking; cross-refs audited across all docs |
| `docs/dev-philosophy-reference.md` | Reference | 2026-03-14 | 107-entry reference: dev philosophies, privacy theories, security frameworks with examples, S/W/M |
| `docs/approved-skills.md` | Reference | 2026-03-14 | Rev 2.3 — skill-tester approved with Phase 4 Docker caveat |
| `docs/phase4-sandbox.md` | Reference | 2026-03-14 | Docker sandbox procedure; OSError canary fix documented |

---

## Key Files

| File | Description |
|---|---|
| `memory/constitution.md` | Governing law — highest authority, supersedes all other layers |
| `AGENTS.md` | Runtime agent context — role, scope, voice, tools, sources |
| `registry/progress.md` | This file — current project state |
| `specs/llm-deployment/spec.md` | User stories and success criteria for a deployment |
| `specs/llm-deployment/plan.md` | Architecture, injection order, implementation phases |
| `specs/llm-deployment/tasks.md` | Executable deployment checklist (40 tasks across 4 phases) |
| `docs/guardrails.md` | Input/output filters and escalation triggers |
| `docs/change-management.md` | How to safely update any part of this system |
| `docs/incident-response.md` | What to do when something goes wrong |
| `standards/STD05-ai-session-continuity.md` | Session start/end protocol for AI sessions |
| `standards/STD08-brand-standard.md` | Document design and tone standard |
| `registry/decisions/` | Decision records — why the system is the way it is |
