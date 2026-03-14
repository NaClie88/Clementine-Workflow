---
id: performance-engineering
title: "Performance Engineering"
domain: coding-practices
sub-domain: "coding discipline"
applies-to: []  # TODO: backend | frontend | infrastructure | cloud | mobile | data | ml | all
complexity: ""  # TODO: low | medium | high
maturity: ""    # TODO: established | emerging | theoretical
theorist: ""    # TODO: primary originator or "multiple"
year: null      # TODO: year concept was formally named/published
related: []     # TODO: IDs of related entries
tags: []        # TODO: free-form tags
---

## Definition

Profile before optimising. Premature optimisation is the root of much evil (Knuth).

## Example

A Django API with N+1 queries: `for order in orders: order.customer.name` hits the database once per order. `select_related('customer')` reduces 100 queries to 1. Profiling identified the hotspot; `EXPLAIN ANALYZE` confirmed the fix.

## Strengths

- Profiling-driven optimisation targets real bottlenecks — not imagined ones
- Measurable improvement with measurable cost
- SLOs define "fast enough" so the work has a clear endpoint

## Weaknesses

- Premature optimisation creates complex code for negligible gains
- Caching adds invalidation complexity — "there are only two hard things in computer science"
- Performance fixes can hide underlying design problems

## Mitigation

Establish performance baselines with load testing before optimising. Set latency SLOs so "done" has a definition. Profile in production-like conditions — dev machine benchmarks mislead.
