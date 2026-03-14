---
id: complete-mediation
title: "Complete Mediation"
domain: security
sub-domain: "foundational principles"
applies-to: [backend, infrastructure]
complexity: medium
maturity: established
theorist: "Jerome Saltzer, Michael Schroeder"
year: 1975
related: [least-privilege, zero-trust-architecture, principle-of-least-authority]
tags: [access-control, authorization, every-access, caching-danger, reference-monitor]
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
