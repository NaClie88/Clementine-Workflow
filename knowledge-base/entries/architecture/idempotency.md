---
id: idempotency
title: "Idempotency"
domain: architecture
sub-domain: "design principles"
applies-to: []  # TODO: backend | frontend | infrastructure | cloud | mobile | data | ml | all
complexity: ""  # TODO: low | medium | high
maturity: ""    # TODO: established | emerging | theoretical
theorist: ""    # TODO: primary originator or "multiple"
year: null      # TODO: year concept was formally named/published
related: []     # TODO: IDs of related entries
tags: []        # TODO: free-form tags
---

## Definition

An operation that can be applied multiple times with the same result as a single application.

## Example

HTTP `PUT /users/123` sets a user's email — calling it 10 times produces the same result as once. A payment endpoint with an idempotency key (`Idempotency-Key: uuid`) prevents double-charges on retried requests.

## Strengths

- Safe to retry — simplifies distributed systems error recovery
- Enables at-least-once delivery semantics
- Makes systems resilient to network failures and client retries

## Weaknesses

- Some operations are inherently non-idempotent (appending to a log, incrementing a counter)
- Enforcing idempotency adds implementation complexity (deduplication storage)
- Idempotency windows require careful design

## Mitigation

Use idempotency keys (the Stripe payment API pattern) for non-naturally-idempotent operations. Document which operations are and are not idempotent in the API contract.
