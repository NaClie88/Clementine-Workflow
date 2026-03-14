---
id: testing-taxonomy
title: "Testing Taxonomy"
domain: coding-practices
sub-domain: "coding discipline"
applies-to: [all]
complexity: medium
maturity: established
theorist: Mike Cohn
year: 2009
related: [test-driven-development, behaviour-driven-development, code-review]
tags: [unit-tests, integration-tests, e2e-tests, test-pyramid, contract-testing]
---

## Definition

Different test types catch different failure modes. The pyramid matters: many unit tests, fewer integration tests, few E2E tests.

## Example

A payment system — unit tests verify discount calculation logic; integration tests verify the Stripe API integration against a test account; contract tests verify the order service honours the payment service's OpenAPI spec; E2E tests verify checkout through a real browser.

| Type | Speed | Isolation | Catches |
|---|---|---|---|
| Unit | Fast | Complete | Logic bugs |
| Integration | Medium | Partial | Component interaction bugs |
| Contract | Medium | Partial | API compatibility bugs |
| E2E | Slow | None | User journey bugs |
| Property-based | Medium | Complete | Edge cases |
| Mutation | Slow | Complete | Weak assertions |

## Strengths

- Each layer catches failure modes other layers miss
- Fast unit tests provide rapid feedback; E2E tests provide end-to-end confidence
- Test suite is the specification for the system's behaviour

## Weaknesses

- Slow E2E tests discourage running them; the pyramid is easily inverted
- Mocks that diverge from real service behaviour give false confidence
- Property-based and mutation testing require tooling investment and expertise

## Mitigation

Enforce the pyramid in CI — fastest tests run first, E2E in a separate gated stage. Use contract tests to reduce reliance on E2E tests for integration verification.
