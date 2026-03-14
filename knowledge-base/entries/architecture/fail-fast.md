---
id: fail-fast
title: "Fail Fast"
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

Detect and report errors at the earliest possible point. A system that fails late obscures the origin of the problem.

## Example

An API endpoint that validates all inputs at the boundary and returns 400 immediately, rather than passing invalid data deep into business logic where it causes an obscure error 10 stack frames later.

## Strengths

- Errors are caught close to their cause — easier to diagnose
- Prevents corrupted state from propagating
- Makes invalid states unrepresentable rather than detectable

## Weaknesses

- Aggressive early termination can mask valid edge cases in exploratory code
- Requires clear distinction between validation errors (expected) and exceptional cases (unexpected)
- Over-validation at internal boundaries adds noise

## Mitigation

Fail fast at trust boundaries (user input, external APIs, file I/O). Trust internal code you control. Combine with structured, informative error responses.
