---
id: principle-of-least-astonishment
title: "Principle of Least Astonishment (POLA)"
domain: architecture
sub-domain: "design principles"
applies-to: [all]
complexity: low
maturity: established
theorist: multiple
year: 1984
related: [api-design, convention-over-configuration, accessibility]
tags: [api-design, ux, developer-experience, consistency]
---

## Definition

A component should behave in the way a reasonable user would expect. Surprising behaviour is a design defect regardless of whether it is documented.

## Example

A `save()` method that also deletes old backups surprises callers. `save_with_backup_cleanup()` or two separate calls make the side effect explicit and expected.

## Strengths

- Code is predictable — reduces bugs from incorrect mental models
- Reduces the need for extensive documentation of side effects
- APIs that don't surprise are faster to use correctly

## Weaknesses

- "Astonishing" is audience-dependent — experts may find defensive naming verbose
- Applied too strictly, it prohibits useful side effects that are well-understood in context
- Naming everything exhaustively can make call sites verbose

## Mitigation

Name functions for their complete behaviour, not just their primary purpose. Document side effects explicitly in the function signature or docstring.
