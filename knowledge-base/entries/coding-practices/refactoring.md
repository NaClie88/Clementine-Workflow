---
id: refactoring
title: "Refactoring"
domain: coding-practices
sub-domain: "coding discipline"
applies-to: []  # TODO: backend | frontend | infrastructure | cloud | mobile | data | ml | all
complexity: ""  # TODO: low | medium | high
maturity: ""    # TODO: established | emerging | theoretical
theorist: ""    # TODO: primary originator or "multiple"
year: null      # TODO: year concept was formally named/published
related: []     # TODO: IDs of related entries
tags: []        # TODO: free-form tags
---

## Definition

Change the structure of code without changing its observable behaviour. Requires a green test suite as a prerequisite.

## Example

Martin Fowler's Extract Method — a 50-line `processOrder()` is refactored into `validateOrder()`, `calculateTotal()`, and `applyDiscounts()`. The tests pass before and after; only the structure changed.

## Strengths

- Reduces technical debt — the next change is cheaper
- Improves readability and onboarding
- The refactored structure often reveals design insights

## Weaknesses

- Refactoring without tests is rewriting with undetected risk
- Time pressure consistently defers refactoring until debt is unmanageable
- Wrong abstractions introduced during refactoring are expensive to undo

## Mitigation

Always refactor with a green test suite. Apply the scout rule (leave code cleaner than you found it) rather than scheduling dedicated refactoring sprints — sustained small improvements outperform big periodic rewrites.
