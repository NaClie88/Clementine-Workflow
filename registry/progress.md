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

Session 2026-03-15 (completed). Docs alignment pass (all 10 docs/ files) + skill vetting automation decision (D02). skill-tester rejected as Phase 1 automation base — quality tool without security awareness; /vet-skill already covers §2.6 automation. --help/JSON/dual-output checks adopted as Phase 4 supplementary quality checks (§5.6 added to skill-vetting-workflow.md). Active Work queue is now empty.

**Constitution v6.0 (MAJOR):**
- Part 1: Complete Mediation (Saltzer & Schroeder, 1975) in Amendment 5; input-validation/attack-surface vocabulary in Amendment 6
- Part 2: Contextual Integrity (Nissenbaum), Privacy by Design (Cavoukian), aggregation harms (Cohen/Solove), GDPR subject rights (DSARs, lawful basis, Art. 25)
- Part 3: Cynefin (Snowden), Chesterton's Fence (Chesterton, 1929), Feedback Loops (Meadows)
- Part 4: CIA Triad as opening framework; STRIDE (Garg & Kohnfelder) as mandatory methodology; POLA (Miller et al.) in Amendment 1; Zero Trust (Kindervag) in Amendment 5; OWASP Top 10 in Amendment 5; NIST SP 800-61 phases in Amendment 6; supply-chain security + SBOM in Amendment 4
- Part 5: ACM Code of Ethics in preamble; named dark patterns (Brignull) in Amendment 3; algorithmic accountability + blameless post-mortems (Allspaw) in Amendment 5; psychological safety (Edmondson) in Amendment 9
- Part 6: DevOps (Debois) + Conway's Law in Amendment 1; SRE error budgets (Treynor Sloss) in Amendment 2
- Part 7: SOLID + Clean Architecture (Martin) as opening design framework; version control discipline (conventional commits, Torvalds) in Amendment 1; chaos engineering (Netflix) in Amendment 2; docs-as-code + why-not-what comments in Amendment 3; defensive programming + fail-fast (Nygard) + code review (Fagan/200-400 line limits) in Amendment 4; NEW Amendment 7 (Dependency Management + SBOM); NEW Amendment 8 (API Design — Fielding)

**Standards alignment:**
- STD01, STD04, STD05, STD06, STD07, STD08, STD09: constitutional authority lines updated from old `Article XX` format to `Part X, Amendment Y` format
- STD09 §6 periodic review: added pip-audit + SBOM verification requirements (Part 7, Amendment 7 alignment)
- STD02, STD03, STD10: already correct — no changes needed

**Secondary docs flagged for next session** (stale Article references in body text; vocabulary alignment needed):
- `docs/guardrails.md` — Article XI, VIII, XVII refs; input-validation/attack-surface vocabulary
- `docs/tool-use-policy.md` — least-privilege, fail-secure framing
- `docs/incident-response.md` — NIST SP 800-61 alignment (now in constitution)
- `docs/skill-vetting-workflow.md` — STRIDE threat modelling integration
- `docs/change-management.md` — established change-control vocabulary
- `docs/evaluation-rubric.md`, `docs/logging-audit-policy.md`, `docs/memory-context-policy.md`, `docs/knowledge-sources.md`, `docs/user-roles-permissions.md` — stale Article refs in Constitutional Authority fields

---

## Active Work

No active work items.

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
| Salty-CDP-DB entry files | Knowledge Base | 2026-03-14 | dev-philosophy-reference.md split into per-entry chapter files; visual presentation improved |
| `memory/constitution.md` | Constitution | 2026-03-15 | v6.0 — Salty-CDP-DB vocabulary absorbed throughout all 7 Parts; 2 new amendments in Part 7 (Dependency Management, API Design) |
| `standards/STD01,04–09` | Standards | 2026-03-15 | Constitutional authority alignment pass (Article → Part/Amendment format); STD09 §6 SBOM requirement added |
| `docs/guardrails.md` | Reference | 2026-03-15 | Authority refs fixed; prompt injection framed as trust boundary violation; §3 Article refs fixed; §4 escalation Article XVII fixed; §6 attack-surface-minimisation framing |
| `docs/incident-response.md` | Reference | 2026-03-15 | Authority refs fixed; §3 NIST SP 800-61 lifecycle preamble; §5 ROOT CAUSE blameless analysis (Allspaw, 2012) |
| `docs/skill-vetting-workflow.md` | Reference | 2026-03-15 | §1 STRIDE (Garg & Kohnfelder, 1999) intro + threat table STRIDE category annotations |
| `docs/tool-use-policy.md` | Reference | 2026-03-15 | Authority refs fixed; §1 POLA (Miller et al., 2003) with confused-deputy language; fail-secure naming |
| `docs/change-management.md` | Reference | 2026-03-15 | Authority refs fixed; §2 conduct amendment refs; §5 Part 1 Amendment refs |
| `docs/evaluation-rubric.md` | Reference | 2026-03-15 | Authority ref fixed: Article XII → Part 5, Amendment 5 |
| `docs/logging-audit-policy.md` | Reference | 2026-03-15 | Authority ref fixed: Article XII → Part 5, Amendment 5 |
| `docs/memory-context-policy.md` | Reference | 2026-03-15 | Authority ref fixed: Article XI → Part 5, Amendment 4; §2 body ref fixed |
| `docs/knowledge-sources.md` | Reference | 2026-03-15 | Authority refs fixed: Articles VIII/XI → Part 5 Amendments 1+4; §4 and §5 body refs fixed |
| `docs/user-roles-permissions.md` | Reference | 2026-03-15 | Authority refs fixed: Articles XIII/XVII → Part 1 Amendment 7 + Part 3 Amendment 1; §2 Admin body ref fixed |
| `registry/decisions/D02-skill-vetting-automation.md` | Decision | 2026-03-15 | skill-tester rejected as Phase 1 automation base; --help/JSON/dual-output adopted as Phase 4 supplementary quality checks |
| `docs/skill-vetting-workflow.md` §5.6 | Reference | 2026-03-15 | Phase 4 quality checks added for script-backed skills per D02 |
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
