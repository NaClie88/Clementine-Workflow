---
id: law-of-demeter
title: "Law of Demeter (Principle of Least Knowledge)"
domain: architecture
sub-domain: "design principles"
applies-to: [all]
complexity: medium
maturity: established
theorist: Ian Holland
year: 1987
related: [solid, separation-of-concerns, composition-over-inheritance, encapsulation]
tags: [coupling, encapsulation, oop, principle-of-least-knowledge]
---

## Definition

A component should only communicate with its immediate collaborators. Avoid chains like `a.b.c.doSomething()`.

## Example

`order.getCustomer().getAddress().getCity()` couples the caller to `Order`'s internal structure three levels deep. `order.getShippingCity()` hides the navigation and decouples the caller.

## Strengths

- Reduces coupling — changes to intermediate objects don't cascade to callers
- Forces interfaces to expose semantically meaningful methods
- Easier to mock in tests

## Weaknesses

- Strict LoD leads to "forwarding method explosion" — many thin delegation methods on every class
- Applied to data transfer objects, it is counterproductive
- Within tightly coupled subsystems it adds boilerplate without benefit

## Mitigation

Apply at module and service boundaries. Within a tightly cohesive module, strict LoD may produce unnecessary boilerplate.
