---
id: behaviour-driven-development
title: "Behaviour-Driven Development (BDD)"
domain: methodology
sub-domain: "development methodology"
applies-to: []  # TODO: backend | frontend | infrastructure | cloud | mobile | data | ml | all
complexity: ""  # TODO: low | medium | high
maturity: ""    # TODO: established | emerging | theoretical
theorist: ""    # TODO: primary originator or "multiple"
year: null      # TODO: year concept was formally named/published
related: []     # TODO: IDs of related entries
tags: []        # TODO: free-form tags
---

## Definition

Extends TDD by writing tests in human-readable language (Given/When/Then) that describe system behaviour from the user's perspective.

## Example

A Cucumber/Gherkin scenario: `Given a user has items in their cart / When they apply coupon "SAVE10" / Then the total is reduced by 10%`. The same sentence is the test, the acceptance criterion, and the documentation.

## Strengths

- Bridges business and technical language — shared understanding, not just shared code
- Executable specifications serve as living documentation
- Non-technical stakeholders can read and contribute to test scenarios

## Weaknesses

- Maintaining Gherkin scenarios adds overhead — they drift from implementation
- Over-specified scenarios become implementation-coupled and fragile
- Tooling (Cucumber, Behave) adds a layer of abstraction that slows debugging

## Mitigation

Keep scenarios at the business rule level. Avoid UI-level implementation details in Given/When/Then. Treat step definitions as thin wrappers over a real test API.
