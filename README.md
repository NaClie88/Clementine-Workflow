# Clementine LLM System Architecture — Quickstart Template

A comprehensive, reusable architecture for deploying LLMs in professional environments. Built on [Spec-Driven Development](https://github.com/github/spec-kit) conventions.

Copy this folder, fill in the `[bracketed placeholders]`, and follow the task list in `specs/llm-deployment/tasks.md` before going live.

---

## Structure

```
Clementine-LLM-QuickStart/
├── AGENTS.md                               ← Runtime agent context: role, scope, voice, tools, sources
├── memory/
│   └── constitution.md                    ← Governing law — supersedes all other layers
├── specs/
│   └── llm-deployment/
│       ├── spec.md                        ← User stories, requirements, success criteria
│       ├── plan.md                        ← Architecture, injection order, implementation phases
│       └── tasks.md                       ← Executable deployment checklist
├── standards/                             ← Operational rules — how this project is run
│   ├── STD01-document-naming.md           ← File naming, folder structure, cross-referencing
│   ├── STD02-revision-history.md          ← Required revision history on every document
│   ├── STD03-commit-message.md            ← Commit message format and co-authorship
│   ├── STD04-branch-and-workflow.md       ← Branch naming and merge workflow
│   ├── STD05-ai-session-continuity.md     ← Session start/end protocol for AI sessions
│   ├── STD06-decision-log.md              ← How to record design decisions
│   ├── STD07-progress-tracking.md         ← How to maintain registry/progress.md
│   ├── STD08-brand-standard.md           ← Document design: business casual, function-first
│   └── STD09-approved-technology.md      ← Approved runtimes, databases, packages; no new deps without permission
├── registry/                              ← Project state — updated every session
│   ├── progress.md                        ← Current state, active work, last session note
│   └── decisions/
│       └── D01-spec-kit-structure-adoption.md ← Why this structure was chosen
└── docs/                                  ← Operational reference — stable across deployments
    ├── guardrails.md                      ← Input/output filters and escalation triggers
    ├── user-roles-permissions.md          ← Role definitions and permission matrix
    ├── tool-use-policy.md                 ← Tool invocation rules
    ├── memory-context-policy.md           ← What persists and what clears
    ├── session-policy.md                  ← Session lifecycle and handoff
    ├── knowledge-sources.md               ← Approved sources and RAG rules
    ├── response-quality-criteria.md       ← What a good response looks like
    ├── evaluation-rubric.md               ← Scoring tool for audits
    ├── logging-audit-policy.md            ← What gets logged and who sees it
    ├── incident-response.md               ← When things go wrong
    ├── change-management.md              ← How to safely update this system
    ├── approved-skills.md                ← Reviewed and approved Claude Code skills registry
    ├── skill-vetting-workflow.md         ← Process for safely evaluating external skills
    └── rejected-skill-design-intents.md ← Design intent summaries for rejected skills — reference for compliant re-implementation
```

---

## Layer Precedence

When layers conflict, higher wins — always.

```
┌─────────────────────────────────────────────────────────┐
│           memory/constitution.md                        │
│     Absolute prohibitions. Cannot be overridden.        │
├─────────────────────────────────────────────────────────┤
│           docs/guardrails.md                            │
│   Operational filters enforced before every response.   │
├─────────────────────────────────────────────────────────┤
│     Conduct layer (Part II–III of constitution)         │
│    HOW the LLM behaves — ethics and professionalism.    │
├─────────────────────────────────────────────────────────┤
│       docs/user-roles-permissions.md                    │
│         What each class of user can do.                 │
├─────────────────────────────────────────────────────────┤
│          docs/tool-use-policy.md                        │
│      Rules for invoking external tools and APIs.        │
├─────────────────────────────────────────────────────────┤
│        docs/memory-context-policy.md                    │
│       What persists, what clears, what is off limits.   │
├─────────────────────────────────────────────────────────┤
│         docs/knowledge-sources.md                       │
│    Approved sources, hierarchy, staleness handling.     │
├─────────────────────────────────────────────────────────┤
│                  AGENTS.md                              │
│      Role, persona, scope — customize per deployment.   │
└─────────────────────────────────────────────────────────┘
```

---

## How to Deploy

1. **Fill placeholders** — every `[bracketed placeholder]` in `AGENTS.md`, `docs/knowledge-sources.md`, `docs/tool-use-policy.md`, `docs/user-roles-permissions.md`.
2. **Review the spec** — `specs/llm-deployment/spec.md` defines user stories and success criteria for your deployment.
3. **Follow the plan** — `specs/llm-deployment/plan.md` defines implementation phases and the constitution check gates.
4. **Work the tasks** — `specs/llm-deployment/tasks.md` is your executable checklist. Do not skip phases.
5. **Inject layers** in the correct order (see precedence above).
6. **Run the evaluation rubric** — `docs/evaluation-rubric.md` against minimum 20 test cases before exposing to real users.
7. **Get sign-offs** — all roles in `specs/llm-deployment/tasks.md` Phase 4 before go-live.

---

## What to Customize vs. What to Leave Alone

| Layer | Customize? | Notes |
|---|---|---|
| `memory/constitution.md` Part I | Never | Absolute prohibitions — change management + legal/ethics required even to attempt |
| `memory/constitution.md` Part II–IV | Rarely | Organization-wide conduct standard — full change management required |
| `docs/guardrails.md` | Sometimes | Add triggers; don't remove existing ones without review |
| `docs/user-roles-permissions.md` | Often | Adapt to org structure |
| `docs/tool-use-policy.md` | Often | Add tools per deployment |
| `docs/knowledge-sources.md` | Always | Unique per deployment |
| `AGENTS.md` | Always | Unique per deployment |
| `specs/llm-deployment/` | Always | Document the specific deployment's requirements and tasks |
| `docs/logging-audit-policy.md` | Rarely | Legal/compliance-driven |
| `docs/incident-response.md` | Rarely | Update contacts; process is org-wide standard |
| `docs/change-management.md` | Never | Meta-level governance |

---

## Built With

- [Spec-Driven Development — GitHub Spec Kit](https://github.com/github/spec-kit)
