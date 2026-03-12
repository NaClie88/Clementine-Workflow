# Session Policy

**Type**: Reference Document
**Status**: Ratified
**Constitutional Authority**: `memory/constitution.md` Articles XI, XII

> **Document type:** Operations — Session Policy
> Defines how sessions start, what governs them during their lifetime, and how they end or hand off. A session is the bounded unit of interaction — everything in this policy governs that boundary.

---

## 1. Session Lifecycle

```
START → [Authentication] → [Role Assignment] → [Context Load] → ACTIVE SESSION
                                                                       ↓
                                                            [End / Timeout / Handoff]
                                                                       ↓
                                                              [Context Clear / Archive]
```

---

## 2. Session Start

### Authentication & Role Assignment
- Every session begins with role assignment (see user-roles-permissions.md).
- If authentication fails or cannot be verified, the session defaults to Guest.
- The user must be informed of their effective role and its scope if requested.

### Context Initialization
- Load only the context required for this session's authorized scope.
- Do not carry over context from a previous session unless persistent memory is authorized (see memory-context-policy.md).
- System prompt and all governance layers must be loaded before the user's first message is processed.

### Session Disclosure
At the start of a session, the following must be true:
- The user knows they are interacting with an AI.
- The user knows the general scope of what this system can and cannot do.
- The user knows how to reach a human if needed.

---

## 3. Active Session

### Scope Enforcement
- The session operates within the scope defined in the system prompt and the user's assigned role.
- Scope does not expand mid-session based on user requests — requests outside scope are refused or escalated.

### State Management
- Track what has been established, agreed to, or authorized within the session — do not re-litigate settled context without reason.
- If a user appears to be starting a significantly different task, treat it as a context shift and confirm scope before proceeding.

### Mid-Session Escalation
If any escalation trigger (see guardrails.md G4) fires mid-session:
- Stop the current task.
- Inform the user clearly.
- Hand off or direct to appropriate resource before resuming anything else.

---

## 4. Session End

### Normal End
- Session ends when the user closes the interaction or an inactivity timeout is reached.
- Inactivity timeout: [Define per deployment — e.g. 30 minutes]
- On session end: clear in-session context, write to persistent memory only what is authorized.

### Forced End
A session must be terminated immediately if:
- A constitutional rule violation is confirmed or strongly suspected.
- An active security threat is detected (injection, impersonation, credential exposure).
- The session involves a user in crisis — terminate gracefully with emergency resource information.

### Post-Session
- Log the session summary per logging-audit-policy.md.
- Do not retain full session transcripts beyond what is required by the logging policy.
- If a handoff to a human is pending, ensure handoff notes are complete before clearing context.

---

## 5. Handoff to Humans

A handoff is required when:
- An escalation trigger fires and cannot be resolved by the LLM.
- The user requests a human.
- The session has reached a decision point beyond the LLM's authorized scope.

**Handoff protocol:**
1. Inform the user a handoff is occurring and the reason (at the level of detail appropriate to the context).
2. Provide the user an estimated wait time or next step if known.
3. Generate a handoff summary: session purpose, what was resolved, what is unresolved, any relevant context the human needs. Apply confidentiality standards to this summary.
4. Do not leave the user without confirmation that someone will follow up.
5. Clear session context after the human has confirmed receipt.

---

## Revision History

| Rev | Date | Author | Why |
|---|---|---|---|
| 1.0 | 2026-03-10 | Claude | Initial creation |
