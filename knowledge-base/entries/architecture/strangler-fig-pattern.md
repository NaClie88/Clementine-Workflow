---
id: strangler-fig-pattern
title: "Strangler Fig Pattern"
domain: architecture
sub-domain: "architectural philosophy"
applies-to: [backend, infrastructure]
complexity: medium
maturity: established
theorist: Martin Fowler
year: 2004
related: [monolith-first, microservices, domain-driven-design]
tags: [migration, legacy, incremental-replacement, re-architecture]
---

## Definition

Incrementally replace a legacy system by routing new functionality to a new implementation while the old system handles everything else.

## Example

A legacy PHP monolith is incrementally replaced by routing `/api/orders` to a new Go service via an nginx proxy. Everything else still hits the monolith. The proxy is removed when the monolith is fully drained.

## Strengths

- No big-bang rewrite risk — production traffic validates the new system incrementally
- Rollback is a routing change — fast and low-risk
- Teams learn the domain while migrating, not before

## Weaknesses

- Long-lived parallel systems must both be maintained during migration
- The routing layer is a new point of failure
- Migrations can stall if there is no forcing function to complete them

## Mitigation

Time-box the migration phase. Remove the legacy system aggressively once traffic is migrated. Treat a stalled migration as technical debt with a cost.
