---
id: kiss
title: "KISS — Keep It Simple, Stupid"
domain: architecture
sub-domain: "design principles"
applies-to: [all]
complexity: low
maturity: established
theorist: multiple
year: 1960
related: [yagni, dry, defensive-programming]
tags: [simplicity, complexity-management, design]
---

## Definition

Unnecessary complexity should be avoided. A simple solution that works is better than a complex one that also works.

## Example

A 3-line `strftime` formatter vs. a 200-line custom date parsing engine. The latter is only justified when the 3-line version demonstrably cannot meet the requirement.

## Strengths

- Easier to debug, review, and onboard
- Less surface area for bugs
- Simpler systems have fewer failure modes

## Weaknesses

- "Simple" is subjective and audience-dependent
- KISS can be weaponised to justify avoiding legitimate complexity that a domain genuinely requires
- Simple solutions can be naive solutions

## Mitigation

Define "simple" relative to the team's skill level and the domain — not in absolute terms. Distinguish necessary complexity from accidental complexity.
