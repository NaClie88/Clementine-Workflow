# Logging & Audit Policy

**Type**: Reference Document
**Status**: Ratified
**Constitutional Authority**: `memory/constitution.md` Part 5, Amendment 5 (Accountability)

> **Document type:** Compliance — Logging & Audit Policy
> Defines what gets logged, how long it is kept, who can access it, and how it is used. Logs exist to enable accountability and improvement — not surveillance. Handle them accordingly.

---

## 1. What Gets Logged

### Session-Level Logs (Every Session)
- Session ID (anonymized or pseudonymized unless role requires full identification)
- User role assigned
- Session start and end timestamps
- Session end reason (normal, timeout, forced, handoff)
- Whether any escalation triggers fired and which ones
- Whether any override was requested and the outcome

### Interaction-Level Logs (Sampled or Full, Per Deployment Config)
- Input summary (not full text unless required — see privacy note below)
- Output summary (not full text unless required)
- Tools invoked and their outcomes
- Knowledge sources accessed
- Any compliance flags raised

### Incident Logs (All Incidents, Full Detail)
- Full session transcript for the incident window
- Trigger conditions and system response
- Human actions taken
- Resolution and follow-up

---

## 2. What Does Not Get Logged

- Passwords, credentials, or authentication tokens shared in a session — these must be flagged but not stored.
- Health, financial, or other regulated sensitive data beyond what is required for audit purposes.
- Full session transcripts as default — only when required by incident or compliance review.

---

## 3. Retention Schedule

| Log Type | Retention Period | Notes |
|---|---|---|
| Session-level logs | [90 days] | Adjust per legal/compliance requirement |
| Interaction-level logs | [30 days] | Shorter retention for privacy |
| Incident logs | [2 years] | Or per legal hold requirement, whichever is longer |
| Audit reports | [3 years] | Permanent if related to litigation |

After retention period: logs are deleted or anonymized — not archived indefinitely by default.

---

## 4. Access Control

| Role | Access |
|---|---|
| Operator | Full access to all logs for their deployment |
| Admin | Session-level and interaction-level logs for their team/scope |
| Standard User | Their own session logs on request |
| Guest | None |
| External Auditor | Scoped access per audit engagement — time-limited |

Log access must be:
- Authenticated and role-verified before access is granted.
- Itself logged — who accessed what, when, and why.
- Revoked when the access justification no longer applies.

---

## 5. Use of Logs

Logs may be used for:
- Incident investigation and root cause analysis.
- Quality audits per the evaluation rubric.
- Compliance reviews and regulatory requirements.
- System improvement — in aggregate and anonymized form.

Logs must not be used for:
- Monitoring individual users beyond what is necessary for a specific investigation.
- Building behavioral profiles on users without their knowledge and consent.
- Punitive action against users without a formal review process.

---

## 6. Audit Schedule

| Audit Type | Frequency | Owner |
|---|---|---|
| Access log review (who accessed logs) | Monthly | [Security Owner] |
| Compliance flag review | Monthly | [Technical Owner] |
| Escalation trigger review | Monthly | [Product Owner] |
| Full system audit | Annually | [Designated Auditor] |
| Post-incident audit | After every incident | [Incident Owner] |

Audit findings must be documented and reviewed within [10 business days] of the audit completion date.

---

## Revision History

| Rev | Date | Author | Why |
|---|---|---|---|
| 1.0 | 2026-03-10 | Claude | Initial creation |
| 1.1 | 2026-03-15 | claude-sonnet-4-6 | Constitutional authority updated: Article XII → Part 5, Amendment 5 |
