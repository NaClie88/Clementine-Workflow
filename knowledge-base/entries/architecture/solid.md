---
id: solid
title: "SOLID"
domain: architecture
sub-domain: "design principles"
applies-to: [all]
complexity: medium
maturity: established
theorist: Robert C. Martin
year: 1995
related: [dry, kiss, separation-of-concerns, composition-over-inheritance, defensive-programming]
tags: [oop, design-principles, clean-code, single-responsibility]
---

## Definition

Five object-oriented design principles (Robert C. Martin): Single Responsibility, Open/Closed, Liskov Substitution, Interface Segregation, Dependency Inversion.

## Example

A `User` class that handles authentication, profile updates, and email notifications violates SRP. Split into `AuthService`, `UserProfileService`, `NotificationService` — each has one reason to change.

## Strengths

- Units are independently testable and deployable
- Changes to one concern don't ripple into others
- Onboarding a new developer to a single class is cheap

## Weaknesses

- Over-application produces dozens of tiny classes that are hard to trace end-to-end
- Interface segregation adds abstraction layers that obscure what code actually does
- SRP applied too aggressively produces premature decomposition

## Mitigation

Apply at the pain point — extract responsibilities only when a class demonstrably changes for multiple independent reasons. Apply SOLID at the module level before the class level.
