---
id: clean-architecture
title: "Clean Architecture (Robert C. Martin)"
domain: architecture
sub-domain: "architectural philosophy"
applies-to: [all]
complexity: high
maturity: established
theorist: Robert C. Martin
year: 2012
related: [hexagonal-architecture, solid, domain-driven-design, separation-of-concerns]
tags: [architecture, dependency-rule, layers, use-cases, entities]
---

## Definition

Organises code in concentric rings: Entities → Use Cases → Interface Adapters → Frameworks & Drivers. Dependencies point inward only — the inner rings are independent of the outer rings.

## Example

A FastAPI app where route handlers call use case functions that call repository interfaces. The database is a plugin — swap SQLite for PostgreSQL by changing only the repository implementation. The business logic never imports SQLAlchemy.

## Strengths

- Business logic is testable without a database, web framework, or any external system
- Infrastructure changes don't ripple into the domain
- The domain model is the most stable part of the codebase

## Weaknesses

- Boilerplate-heavy for small projects — the ring structure can dwarf the actual logic
- The boundary between rings requires ongoing discipline to maintain
- Mapping between layers (domain objects → DTOs → database models) adds code volume

## Mitigation

Apply to the core domain first. Don't force every script or utility through the full ring structure — reserve it for the parts of the system that carry the most business value and change the most.
