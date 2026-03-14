---
id: hexagonal-architecture
title: "Hexagonal Architecture (Ports and Adapters — Alistair Cockburn)"
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

The application core is surrounded by ports (interfaces) and adapters (implementations). Any external system — UI, database, message queue — is an adapter.

## Example

A domain service processes payments through a `PaymentGatewayPort` interface. Tests inject a `FakePaymentGateway`; production uses a `StripeAdapter`. The domain never imports the Stripe SDK — the dependency is inverted.

## Strengths

- Any external system is replaceable without changing domain logic
- The domain is fully testable in isolation with fakes
- Multiple delivery mechanisms (REST API, CLI, background job) can share one application core

## Weaknesses

- More interfaces and adapters to maintain
- Can feel over-engineered for simple integrations with one external system
- Requires discipline to keep adapters from leaking domain concerns

## Mitigation

Create ports only for dependencies that are genuinely likely to change or require test faking. A direct Stripe import is fine until you need to test without Stripe or swap providers.
