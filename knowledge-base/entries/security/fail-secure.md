---
id: fail-secure
title: "Fail Secure"
domain: security
sub-domain: "foundational principles"
applies-to: []  # TODO: backend | frontend | infrastructure | cloud | mobile | data | ml | all
complexity: ""  # TODO: low | medium | high
maturity: ""    # TODO: established | emerging | theoretical
theorist: ""    # TODO: primary originator or "multiple"
year: null      # TODO: year concept was formally named/published
related: []     # TODO: IDs of related entries
tags: []        # TODO: free-form tags
---

## Definition

When a system fails, it should fail in a state that denies access rather than grants it.

## Example

A door access controller loses power — the magnetic lock stays engaged (fail secure) rather than releasing (fail open). Software equivalent: a broken authentication service returns 503 Service Unavailable, not 200 OK.

## Strengths

- Prevents security failures from creating access windows
- Predictable failure mode — the system degrades to "no access" not "all access"
- Auditable — a deny event is logged; an unexpected grant might not be

## Weaknesses

- Fail-secure conflicts with availability — a broken auth service that blocks all access is a denial of service
- Safety-critical systems (fire exits) must fail open — fail-secure and fail-safe are different requirements
- Over-applied, fail-secure creates systems that become inaccessible on minor failures

## Mitigation

Distinguish security-critical systems (fail secure — deny access on failure) from safety-critical systems (fail safe — open the fire exit in a fire). Design both properties explicitly. Build fallback auth paths (break-glass access) for fail-secure systems.
