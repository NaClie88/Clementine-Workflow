---
id: documentation
title: "Documentation"
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

Code comments explain *why*, not *what*. Procedure documents must be verified by executing them, not re-reading them.

## Example

An ADR in `registry/decisions/ADR-012-postgres-over-mysql.md`: decision, alternatives considered, why this option was chosen, known trade-offs. Committed in the same PR as the schema migration it documents.

## Strengths

- ADRs make "why" decisions auditable across years and team changes
- Runbooks written and tested before incidents reduce response time
- Documentation committed with code prevents drift

## Weaknesses

- Documentation written from memory diverges from reality quickly
- Documentation debt accumulates — teams deprioritise it under schedule pressure
- LLM-generated documentation can look accurate while being wrong

## Mitigation

Verify procedure documentation by executing it, not re-reading it. Write documentation in the same PR as the code it describes. Treat a procedure that produces a different result than predicted as a documentation bug.
