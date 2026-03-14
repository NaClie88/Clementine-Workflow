---
id: domain-driven-design
title: "Domain-Driven Design (DDD — Eric Evans)"
domain: architecture
sub-domain: "architectural philosophy"
applies-to: [backend]
complexity: high
maturity: established
theorist: Eric Evans
year: 2003
related: [clean-architecture, hexagonal-architecture, event-driven-architecture, cqrs, microservices]
tags: [bounded-context, ubiquitous-language, aggregates, domain-model]
---

## Definition

Model software around the business domain. Core concepts: bounded contexts, ubiquitous language, aggregates, entities, value objects, domain events, repositories.

## Example

An e-commerce system with three bounded contexts: `Catalogue` (products, pricing), `Orders` (cart, checkout), `Fulfilment` (shipping, inventory). Each has its own `Product` model — in `Catalogue` a Product has a price and description; in `Fulfilment` it has a weight and warehouse location. They are different things in different contexts.

## Strengths

- Model reflects the business — domain experts and developers share a language
- Bounded contexts prevent the "big ball of mud" that emerges from a single shared model
- Domain events make business processes explicit and auditable

## Weaknesses

- Requires deep domain understanding upfront — and the domain must be complex enough to warrant it
- Overkill for CRUD-heavy systems with simple business rules
- Bounded context boundaries are hard to get right and expensive to change

## Mitigation

Start with event storming to identify boundaries. Let contexts emerge from where domain experts disagree on the meaning of the same term. Apply DDD tactical patterns only within high-complexity core domains.
