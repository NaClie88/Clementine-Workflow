---
id: microservices
title: "Microservices"
domain: architecture
sub-domain: "architectural philosophy"
applies-to: []  # TODO: backend | frontend | infrastructure | cloud | mobile | data | ml | all
complexity: ""  # TODO: low | medium | high
maturity: ""    # TODO: established | emerging | theoretical
theorist: ""    # TODO: primary originator or "multiple"
year: null      # TODO: year concept was formally named/published
related: []     # TODO: IDs of related entries
tags: []        # TODO: free-form tags
---

## Definition

Decompose a system into small, independently deployable services each owning its data and communicating over a network.

## Example

Netflix runs hundreds of independent services. Each has its own database, deployment pipeline, and team. The Hystrix circuit breaker prevents a slow recommendation service from cascading into a homepage outage.

## Strengths

- Independent deployability — one team can ship without coordinating with others
- Technology heterogeneity — use the right tool for each service
- Fault isolation — one service's failure does not necessarily bring down others

## Weaknesses

- Distributed systems complexity: network latency, partial failure, data consistency across services
- Operational overhead: each service needs its own CI/CD, monitoring, alerting
- Wrong service boundaries are expensive to fix — and they are common

## Mitigation

Start with a modular monolith. Extract services only when team and domain boundaries align. Invest heavily in observability (logs, traces, metrics) before decomposing.
