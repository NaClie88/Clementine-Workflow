---
id: separation-of-concerns
title: "Separation of Concerns"
domain: architecture
sub-domain: "design principles"
applies-to: [all]
complexity: medium
maturity: established
theorist: Edsger W. Dijkstra
year: 1974
related: [solid, hexagonal-architecture, clean-architecture, law-of-demeter]
tags: [modularity, decomposition, coupling, cohesion]
---

## Definition

Decompose a system into distinct sections, each addressing a separate concern — presentation, business logic, data access, etc. Reduces coupling, increases cohesion.

## Example

MVC — Model handles data, View handles display, Controller handles input. A controller that also executes SQL queries and sends emails violates SoC.

## Strengths

- Components can be tested, replaced, and reasoned about independently
- Enables parallel development across concerns
- Reduces the blast radius of a change

## Weaknesses

- Strict separation creates artificial seams that add indirection without clarity
- Over-layered systems (controller → service → repository → DAO → entity) can obscure simple logic
- Where to draw the boundary is a design judgment, not a formula

## Mitigation

Separate concerns at the level of change frequency and reason, not just logical category. A concern that changes together should stay together.
