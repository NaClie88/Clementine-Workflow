---
id: yagni
title: "YAGNI — You Aren't Gonna Need It"
domain: architecture
sub-domain: "design principles"
applies-to: [all]
complexity: low
maturity: established
theorist: Ron Jeffries
year: 2001
related: [kiss, dry, wet]
tags: [simplicity, agile, speculative-generality, over-engineering]
---

## Definition

Do not add functionality until it is needed. Speculative generality creates code that must be maintained, tested, and understood but may never be used.

## Example

Not building a plugin system for a tool that currently has exactly one use case, even if "someone might want plugins someday."

## Strengths

- Reduces codebase size and maintenance burden
- Keeps the team focused on delivering value now
- Deferred decisions are often better decisions (more information is available later)

## Weaknesses

- Can lead to costly rewrites if the deferred need materialises at scale
- Requires judgment about what constitutes speculative vs. clearly upcoming need
- Sometimes conflicts with designing for testability (which requires certain interfaces upfront)

## Mitigation

Pair with ADRs — record why a capability was deferred so future decisions are informed rather than starting from scratch.
