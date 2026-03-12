# Change Management

**Type**: Reference Document
**Status**: Ratified
**Constitutional Authority**: `memory/constitution.md` Articles XVIII, XIX

> **Document type:** Compliance — Change Management
> Defines how changes to this system's architecture are proposed, reviewed, approved, tested, and deployed. The governance layer of an LLM is only as strong as the discipline around changing it. No document in this system changes without going through this process.

---

## 1. Core Principle

**Every change is documented, reviewed, and tested before it is deployed.** There are no hotfixes to governance documents. Speed is not a valid reason to skip review.

---

## 2. Change Classification

| Type | Description | Approvals Required |
|---|---|---|
| Critical | Changes to `memory/constitution.md` or `docs/guardrails.md` | Legal/Ethics + Technical Owner + Operator |
| Major | Changes to conduct articles (constitution Parts II–III), roles/permissions, tool use policy | Technical Owner + Product Owner + [HR/Policy if conduct] |
| Standard | Changes to `AGENTS.md`, knowledge sources, session policy | Technical Owner + Product Owner |
| Minor | Corrections to typos, formatting, or clarifications with no semantic change | Technical Owner |

When in doubt, classify higher. Downgrade only after review confirms it is warranted.

---

## 3. Change Process

### 1. Propose
- Open a change request describing: what is changing, why, and what the expected effect is.
- Identify which documents are affected.
- Classify the change.
- Identify risks and how they will be mitigated.

### 2. Review
- Route to all required approvers for the classification.
- Allow [3 business days] minimum for review of Critical/Major changes.
- Approvers may approve, reject, or request modifications.
- All review feedback is documented in the change record.

### 3. Test
- Apply the change in a staging environment.
- Run the evaluation rubric against a representative test set.
- For Critical/Major changes: include adversarial test cases specifically targeting the changed behavior.
- Document test results. A change that fails testing does not proceed.

### 4. Deploy
- Deploy to production only after all approvals and testing are complete.
- Update the version history in the affected document(s).
- Notify all relevant owners that the change is live.

### 5. Monitor
- Monitor for unexpected behavior for [7 days] after any Critical/Major change.
- Run a focused audit within [5 business days] of deployment.
- If unexpected behavior is detected, treat as an incident (see incident-response.md).

---

## 4. Version History

Every document governed by this system must maintain a version history block:

```
## Version History
| Version | Date | Author | Change Summary | Approved By |
|---|---|---|---|---|
| 1.0 | [date] | [author] | Initial release | [approver] |
```

Version numbers follow semantic versioning:
- **Major (X.0)** — Substantive change to meaning or scope
- **Minor (X.Y)** — Addition or clarification that does not alter existing rules
- **Patch (X.Y.Z)** — Typo, formatting, or non-semantic correction

---

## 5. What Cannot Be Changed

The following cannot be changed through this process or any other:

- **Constitutional Rules C1–C3** (harm, weapons, CSAM) — These are non-negotiable regardless of business justification. Any proposal to modify them must be referred to [Legal/Ethics board] and is presumed to fail.
- The change management process itself cannot be bypassed by any role below Operator, and Operator changes to this process require the same review as Critical changes.

---

## 6. Emergency Changes

If a critical vulnerability requires an immediate fix (e.g., an active exploit of a guardrail):
1. The Incident Commander may authorize a temporary mitigation (e.g., taking the system offline or disabling a specific capability) without full review.
2. A full change request must be opened within [24 hours] of the emergency action.
3. The permanent fix must still go through the full change process.
4. Emergency actions that modify Constitutional Rules are not permitted under any circumstances — take the system offline instead.

---

## 7. Change Request Log

All change requests — approved, rejected, or withdrawn — are retained for [3 years]. This log is auditable by Operators and designated auditors.

---

## Revision History

| Rev | Date | Author | Why |
|---|---|---|---|
| 1.0 | 2026-03-10 | Claude | Initial creation |
