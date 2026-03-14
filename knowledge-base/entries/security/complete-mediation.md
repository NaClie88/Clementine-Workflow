---
id: complete-mediation
title: "Complete Mediation"
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

Every access to every resource must be checked against the access control policy every time — not just on first access.

## Example

A caching proxy that checks permissions when a resource is first fetched but not on subsequent cache hits — an attacker whose permissions are revoked can still access cached resources until TTL expires.

## Strengths

- Prevents permission-cache desynchronisation attacks
- Ensures access control reflects current state, not state at time of last check
- Complements least privilege — permissions are only effective if checked

## Weaknesses

- Checking every access adds latency — often traded away for performance
- Long-lived tokens (JWT with 24h expiry) inherently compromise complete mediation
- Difficult to implement in CDN and edge caching architectures

## Mitigation

Use short TTLs on cached access decisions (minutes, not hours). Implement revocation events that invalidate caches immediately for sensitive resources. Use short-lived tokens (15 minutes) for high-value resources.
