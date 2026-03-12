# Implementation Plan: LLM Deployment

**Branch**: `001-llm-deployment` | **Date**: [DATE] | **Spec**: `specs/llm-deployment/spec.md`

---

## Summary

Deploy a governed LLM assistant with a layered architecture that enforces constitutional rules, conduct standards, and operational guardrails — configurable per deployment context while keeping governance stable across all deployments.

---

## Technical Context

**Platform**: [e.g., Claude API, OpenAI, local model]
**Model**: [e.g., claude-sonnet-4-6, gpt-4o]
**Deployment Target**: [e.g., internal web app, Slack bot, API endpoint]
**Storage**: [e.g., PostgreSQL for session logs, Redis for session state]
**Auth**: [e.g., SSO, API key, OAuth]
**Performance Goals**: [e.g., p95 response time < 3s]
**Constraints**: [e.g., max context window, rate limits, cost ceiling]
**Scale**: [e.g., 50 concurrent users, 1000 sessions/day]

---

## Constitution Check

*All implementation decisions must pass these gates before proceeding.*

- [ ] No feature or configuration overrides `memory/constitution.md` Part I (Absolute Prohibitions).
- [ ] Governance layer injection order confirmed: Constitution → Guardrails → Conduct → Roles → Tools → Memory → Knowledge → System Prompt.
- [ ] No runtime instruction path allows a user to self-assign elevated roles.
- [ ] All tool integrations reviewed for minimal-footprint compliance.
- [ ] Logging and audit confirmed active before go-live.

---

## Architecture

### Layer Injection Order

```
[memory/constitution.md]          ← Highest precedence, injected first
[docs/guardrails.md]              ← Operational filters
[conduct layer — Part II/III of constitution]
[docs/user-roles-permissions.md]  ← Role enforcement
[docs/tool-use-policy.md]         ← Tool rules
[docs/memory-context-policy.md]   ← Context boundaries
[docs/knowledge-sources.md]       ← Source hierarchy
[AGENTS.md]                       ← Role, persona, scope ← Lowest precedence
```

### Project Structure

```text
Clementine-LLM-QuickStart/
├── AGENTS.md                          ← Runtime agent context (role, voice, tools, sources)
├── memory/
│   └── constitution.md               ← Governing law
├── specs/
│   └── llm-deployment/
│       ├── spec.md                   ← This deployment's user stories and requirements
│       ├── plan.md                   ← This file
│       └── tasks.md                  ← Deployment task list
└── docs/
    ├── guardrails.md
    ├── user-roles-permissions.md
    ├── tool-use-policy.md
    ├── memory-context-policy.md
    ├── session-policy.md
    ├── knowledge-sources.md
    ├── response-quality-criteria.md
    ├── evaluation-rubric.md
    ├── logging-audit-policy.md
    ├── incident-response.md
    └── change-management.md
```

---

## Implementation Phases

### Phase 0 — Governance Configuration
- Fill all `[bracketed placeholders]` in `AGENTS.md`, `docs/knowledge-sources.md`, `docs/tool-use-policy.md`, and `docs/user-roles-permissions.md`.
- Confirm `memory/constitution.md` requires no deployment-specific amendments.
- Set up logging infrastructure per `docs/logging-audit-policy.md`.
- Confirm incident response contacts and escalation paths per `docs/incident-response.md`.

### Phase 1 — Integration
- Implement role assignment and authentication at session start.
- Implement layer injection in the correct precedence order.
- Integrate authorized knowledge sources with RAG if applicable.
- Implement tool integrations with authorization checks.
- Implement session lifecycle (start, timeout, end, handoff).

### Phase 2 — Safety & Guardrails
- Implement all guardrail filters (input, output, scope, escalation triggers).
- Implement prompt injection detection.
- Implement escalation flow — trigger → log → notify user → human handoff.
- Test all constitutional prohibition refusals against adversarial inputs.

### Phase 3 — Quality & Evaluation
- Run evaluation rubric against minimum 20 test cases including edge cases.
- Achieve ≥ 3.0 overall score with no compliance dimension at 0.
- Document all failures and root causes before clearing for production.

### Phase 4 — Go-Live
- Complete all items in `specs/llm-deployment/tasks.md`.
- Obtain all sign-offs in the deployment checklist.
- Confirm monitoring is active.
- Brief incident response team that system is live.

---

## Complexity Justification

| Decision | Why | Simpler Alternative Rejected Because |
|---|---|---|
| Layered injection order | Ensures governance cannot be overridden by lower layers | Flat prompt would allow system prompt to override constitution |
| Separate constitution file | Stable governance across deployments | Embedding in system prompt makes it deployment-variable |
| Role-based permissions | Different users need different access | Single role level is either too permissive or too restrictive |

---

## Revision History

| Rev | Date | Author | Why |
|---|---|---|---|
| 1.0 | 2026-03-10 | Claude | Initial creation |
