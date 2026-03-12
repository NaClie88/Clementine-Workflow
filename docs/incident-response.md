# Incident Response

**Type**: Reference Document
**Status**: Ratified
**Constitutional Authority**: `memory/constitution.md` Articles XII, XVII

> **Document type:** Compliance — Incident Response
> Defines what constitutes an incident, who is responsible, and what steps to take when something goes wrong. Speed and clarity matter in incident response — this document is written to be usable under pressure.

---

## 1. Incident Classification

| Severity | Definition | Response Time |
|---|---|---|
| P0 — Critical | Constitutional rule violated, user harmed, or active security threat | Immediate — within 15 minutes |
| P1 — High | Guardrail failure, significant data exposure, or repeated escalation trigger | Within 1 hour |
| P2 — Medium | Quality failure affecting multiple users, single escalation failure, or policy breach | Within 4 hours |
| P3 — Low | Isolated quality defect, minor policy deviation with no harm | Within 1 business day |

When in doubt, treat as the higher severity. Downgrade after investigation, not before.

---

## 2. Incident Response Team

| Role | Responsibility | Contact |
|---|---|---|
| Incident Commander | Owns the response end-to-end | [Name / contact] |
| Technical Owner | Diagnoses system behavior, implements fixes | [Name / contact] |
| Communications Lead | Manages user and stakeholder communication | [Name / contact] |
| Legal / Compliance | Advises on regulatory obligations, data breach rules | [Name / contact] |
| [Additional role] | [Responsibility] | [Contact] |

---

## 3. Response Runbook

### Step 1 — Detect & Declare (0–15 min for P0/P1)
- Confirm an incident has occurred (not a false positive).
- Classify severity.
- Declare the incident and notify the Incident Commander.
- If P0: consider immediate system suspension until the threat is contained.

### Step 2 — Contain (15–60 min for P0/P1)
- Stop the harm from continuing or spreading.
- Options: suspend the session, restrict the affected capability, take the system offline.
- Do not sacrifice containment for speed of investigation — contain first.
- Notify affected users if the incident affects them directly (see Communication below).

### Step 3 — Investigate
- Pull logs for the affected session(s).
- Identify the root cause: was it a governance failure, a system failure, a user action, or a combination?
- Do not assign blame during investigation — focus on what happened and why.
- Document findings in real time — do not reconstruct after the fact.

### Step 4 — Remediate
- Fix the root cause, not just the symptom.
- If a governance document needs updating, go through the change management process.
- If a guardrail needs updating, test before redeploying.
- Do not reopen the affected capability until the fix is verified.

### Step 5 — Review & Close
- Complete the post-incident report (template below).
- Run the evaluation rubric against the affected session type before returning to production.
- Confirm all affected users have been communicated with.
- Log the closure and file the post-incident report per the logging policy.

---

## 4. Communication Standards

### With Affected Users
- Inform them an issue occurred that may have affected their session.
- Tell them what happened at the level of detail appropriate to the incident.
- Tell them what has been done or is being done.
- Do not speculate about cause or blame before the investigation is complete.
- Do not minimize — if it was a significant incident, say so.

### Internal Communication
- Incident Commander sends status updates every [30 minutes] during active P0/P1 incidents.
- All communications logged in the incident record.

### Regulatory / Legal Notification
- Consult Legal / Compliance for any incident involving personal data exposure, potential regulatory breach, or user harm.
- Notification timelines are governed by applicable law — do not miss them.

---

## 5. Post-Incident Report Template

```
Incident ID:
Date / Time Detected:
Date / Time Resolved:
Severity:
Incident Commander:

SUMMARY
[2–3 sentence plain-language description of what happened]

TIMELINE
[Chronological log of events from detection to resolution]

ROOT CAUSE
[What caused the incident — be specific]

IMPACT
[Who was affected, what data or interactions were involved, any harm caused]

CONTAINMENT ACTIONS
[What was done to stop the incident]

REMEDIATION
[What was changed to prevent recurrence]

OPEN ITEMS
[Anything not yet resolved, with owner and due date]

LESSONS LEARNED
[What can be improved in detection, response, or governance]
```

---

## 6. Triggers Requiring Automatic Escalation to Incident Status

- Any constitutional rule violation confirmed or strongly suspected.
- Any unauthorized data exposure, even if unintentional.
- Any attempt to use the system to harm a user.
- Any prompt injection that succeeded in altering system behavior.
- Any system behavior that cannot be explained by the current configuration.
- A user reporting harm as a result of a system response.

---

## Revision History

| Rev | Date | Author | Why |
|---|---|---|---|
| 1.0 | 2026-03-10 | Claude | Initial creation |
