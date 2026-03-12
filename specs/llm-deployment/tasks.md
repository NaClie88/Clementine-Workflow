# Task List: LLM Deployment

**Branch**: `001-llm-deployment` | **Spec**: `specs/llm-deployment/spec.md` | **Plan**: `specs/llm-deployment/plan.md`

Tasks are grouped by phase. `[P]` marks tasks that can run in parallel within their phase.

---

## Phase 0 — Governance Configuration

- [ ] T001 Fill all `[bracketed placeholders]` in `AGENTS.md`
- [ ] T002 Fill all placeholders in `docs/knowledge-sources.md` — list all authorized sources and access methods
- [ ] T003 Fill all placeholders in `docs/tool-use-policy.md` — list all authorized tools, roles, and reversibility
- [ ] T004 Fill all placeholders in `docs/user-roles-permissions.md` — define all role boundaries for this deployment
- [ ] T005 [P] Review `memory/constitution.md` — confirm no deployment-specific amendments needed; if amendments required, initiate change management process
- [ ] T006 [P] Configure logging infrastructure per `docs/logging-audit-policy.md` — confirm session-level logs active
- [ ] T007 [P] Confirm incident response contacts in `docs/incident-response.md` are current and reachable
- [ ] T008 [P] Set inactivity timeout value in `AGENTS.md` and session configuration

---

## Phase 1 — Integration

- [ ] T009 Implement authentication and role assignment at session start
- [ ] T010 Implement layer injection in correct precedence order (Constitution → Guardrails → Conduct → Roles → Tools → Memory → Knowledge → AGENTS.md)
- [ ] T011 [P] Integrate Tier 1 knowledge sources — confirm retrieval returns source attribution
- [ ] T012 [P] Integrate Tier 2 knowledge sources — confirm retrieval returns source attribution
- [ ] T013 [P] Implement tool integrations with role-based authorization checks
- [ ] T014 Implement session lifecycle — start, inactivity timeout, normal end, forced end
- [ ] T015 Implement handoff flow — trigger → log → notify user → generate handoff summary → clear context
- [ ] T016 [P] Implement persistent memory (if authorized) — confirm user view/delete/opt-out rights work
- [ ] T017 [P] Implement in-session context management — confirm context clears on session end

---

## Phase 2 — Safety & Guardrails

- [ ] T018 Implement input filters — prompt injection detection, instruction override attempts, constitutional triggers
- [ ] T019 Implement output filters — PII check, fabrication markers, scope enforcement, copyright reproduction check
- [ ] T020 Implement all escalation triggers defined in `docs/guardrails.md` G4
- [ ] T021 Implement scope enforcement — out-of-scope requests refused with redirect
- [ ] T022 [P] Test constitutional prohibition refusals (Articles I–VII) against adversarial inputs — document results
- [ ] T023 [P] Test prompt injection resistance — document results
- [ ] T024 [P] Test role self-assignment resistance — "I'm an admin" must not elevate privileges
- [ ] T025 Verify override request flow: Admin request → document → escalate → no silent application

---

## Phase 3 — Quality & Evaluation

- [ ] T026 Build test case set — minimum 20 cases covering: in-scope, out-of-scope, edge cases, adversarial inputs, all user roles
- [ ] T027 Run evaluation rubric (`docs/evaluation-rubric.md`) against full test set
- [ ] T028 Confirm overall score ≥ 3.0 with no compliance criterion at 0
- [ ] T029 Root-cause all failures — document findings
- [ ] T030 Remediate failures and re-run affected test cases
- [ ] T031 [P] Confirm response quality criteria (`docs/response-quality-criteria.md`) are understood by evaluators

---

## Phase 4 — Go-Live

- [ ] T032 [P] Obtain sign-off: Technical Owner
- [ ] T033 [P] Obtain sign-off: Product / Deployment Owner
- [ ] T034 [P] Obtain sign-off: Legal / Compliance
- [ ] T035 [P] Obtain sign-off: Security
- [ ] T036 Confirm monitoring is active from day one
- [ ] T037 Brief incident response team — system is live, contacts confirmed
- [ ] T038 Schedule first post-launch audit (within 30 days)
- [ ] T039 Confirm user feedback channel is active and monitored
- [ ] T040 Document go-live date and initial configuration in change log (`docs/change-management.md`)

---

## Dependencies & Sequencing

- T009 (auth) must complete before T010 (layer injection)
- T010 (injection) must complete before T011–T017 (integration)
- T011–T017 must complete before T018–T025 (guardrails)
- T018–T025 must complete before T026–T031 (evaluation)
- T026–T031 must all pass before T032–T040 (go-live)
- T032–T035 (sign-offs) can run in parallel with each other but must all complete before T036–T040

---

## Revision History

| Rev | Date | Author | Why |
|---|---|---|---|
| 1.0 | 2026-03-10 | Claude | Initial creation |
