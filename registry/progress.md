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

Session 2026-03-14 (continued). All 107 original entries have full frontmatter (applied via entry-metadata.yaml + apply-metadata.py). 44 Tier 1 domain entries written across 5 domains: database (10), distributed-systems (8), systems-thinking (10), functional-programming (5), ux (11). LanceDB index rebuilt — 151 entries total. Next: vet query.py as agent skill through Phase 1–4 workflow; add to docs/approved-skills.md.

---

## Active Work

| Document | Type | State | In state since | Notes |
|---|---|---|---|---|
| `docs/approved-skills.md` | Reference | Completed | 2026-03-14 | /kb-query approved — Phase 1–4 complete; strace network fix applied |

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
| `docs/knowledge-base-rag-plan.md` | Plan | 2026-03-14 | RAG system plan — ChromaDB replaced with LanceDB (D01) |
| `registry/decisions/D01-lancedb-vector-database.md` | Decision | 2026-03-14 | 12-option evaluation; LanceDB chosen; 4 packages approved in STD09 §2.4 |
| `knowledge-base/schema.yaml` | Schema | 2026-03-14 | Ratified entry frontmatter schema |
| `knowledge-base/scripts/migrate.py` | Script | 2026-03-14 | One-time migration: dev-philosophy-reference.md → 107 per-entry files |
| `knowledge-base/scripts/embed.py` | Script | 2026-03-14 | Indexes entries into LanceDB (CPU, all-MiniLM-L6-v2, 384d) |
| `knowledge-base/scripts/query.py` | Script | 2026-03-14 | CLI query tool; cosine similarity; --domain, --applies-to, --top-k, --json |
| `knowledge-base/scripts/entry-metadata.yaml` | Data | 2026-03-14 | Metadata for all 107 original entries; applied via apply-metadata.py |
| `knowledge-base/scripts/apply-metadata.py` | Script | 2026-03-14 | Regex-based batch frontmatter updater for entry files |
| `knowledge-base/entries/database/` (10) | Knowledge Base | 2026-03-14 | Tier 1: relational-model, normalisation, acid, cap, pacelc, base, data-modelling-paradigms, schema-evolution, dimensional-modelling, data-mesh |
| `knowledge-base/entries/distributed-systems/` (8) | Knowledge Base | 2026-03-14 | Tier 1: fallacies, two-generals, byzantine-generals, lamport-clocks, saga, crdts, circuit-breaker, bulkhead |
| `knowledge-base/entries/systems-thinking/` (10) | Knowledge Base | 2026-03-14 | Tier 1: cynefin, feedback-loops, theory-of-constraints, conways-law, goodharts-law, hyrums-law, galls-law, postels-principle, littles-law, second-order-thinking |
| `knowledge-base/entries/functional-programming/` (5) | Knowledge Base | 2026-03-14 | Tier 1: immutability, referential-transparency, function-composition, algebraic-data-types, unix-philosophy |
| `knowledge-base/entries/ux/` (11) | Knowledge Base | 2026-03-14 | Tier 1: user-centered-design, cognitive-load-theory, affordance-theory, gestalt-principles, fitts-law, hicks-law, nielsens-heuristics, progressive-disclosure, design-thinking, jobs-to-be-done, dark-patterns |

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
