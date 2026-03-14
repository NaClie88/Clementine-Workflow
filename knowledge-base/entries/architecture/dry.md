---
id: dry
title: "DRY — Don't Repeat Yourself"
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

Every piece of knowledge must have a single, unambiguous, authoritative representation. Violations produce maintenance hazards.

## Example

A discount calculation duplicated across checkout, order history, and invoicing. Extract to `DiscountCalculator`; one change propagates everywhere.

## Strengths

- Single point of change prevents inconsistency bugs
- Forces identification of the canonical source of truth
- Reduces codebase size

## Weaknesses

- Premature DRY creates the wrong abstraction, which is harder to undo than duplication
- "DRY" applied to structurally similar but conceptually different things creates coupling
- Sandi Metz: "duplication is far cheaper than the wrong abstraction"

## Mitigation

Rule of three — tolerate two copies; abstract on the third occurrence, and only when the copies represent the same concept, not just similar structure.
