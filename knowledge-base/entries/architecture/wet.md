---
id: wet
title: "WET — Write Everything Twice (counter-principle to DRY)"
domain: architecture
sub-domain: "design principles"
applies-to: [all]
complexity: low
maturity: established
theorist: multiple
year: 2013
related: [dry, kiss]
tags: [abstraction, code-duplication, pragmatic, rule-of-three]
---

## Definition

A deliberate critique of premature abstraction. Two copies are acceptable; three copies indicate a pattern worth abstracting.

## Example

Two similar validation functions are acceptable. When a third appears with the same logic, that is the signal to abstract.

## Strengths

- Avoids the "wrong abstraction" trap
- Keeps code readable without premature coupling
- The third occurrence reveals what is genuinely shared

## Weaknesses

- Without discipline, WET becomes a blanket excuse for indefinite duplication
- Can degrade into copy-paste culture if the team doesn't act on the three-occurrence signal

## Mitigation

Make the three-occurrence rule explicit in the team's coding standards; make duplication visible in code review so the signal isn't missed.
