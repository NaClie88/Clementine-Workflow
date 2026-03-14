---
id: cqrs
title: "CQRS — Command Query Responsibility Segregation"
domain: architecture
sub-domain: "architectural philosophy"
applies-to: [backend, data]
complexity: high
maturity: established
theorist: Greg Young
year: 2010
related: [event-sourcing, event-driven-architecture, domain-driven-design]
tags: [command-query, read-model, write-model, eventual-consistency]
---

## Definition

Separate the model for writes (commands) from the model for reads (queries). Enables independent scaling and optimisation of each path.

## Example

An order system where `PlaceOrderCommand` writes to a normalised SQL database and `GetOrderHistoryQuery` reads from a denormalised read model updated by event projections. The query model is rebuilt from events any time.

```
Write path:  POST /orders → PlaceOrderCommand → SQL (normalised)
Read path:   GET /orders/history → SQL read model (denormalised, indexed for this query)
Sync:        OrderPlacedEvent → read model projector
```

## Strengths

- Read and write models optimised independently — one can scale without the other
- Read models can be rebuilt from the event log if requirements change
- Eliminates ORM impedance mismatch for complex queries

## Weaknesses

- Eventual consistency between write and read models — users may not immediately see their changes
- Significantly more code and infrastructure than a shared model
- Operational complexity of maintaining two data stores

## Mitigation

Use CQRS only when read/write performance requirements genuinely diverge or query complexity justifies a separate model. Start with a shared model and extract only when the pain is real.
