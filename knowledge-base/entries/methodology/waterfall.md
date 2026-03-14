---
id: waterfall
title: "Waterfall"
domain: methodology
sub-domain: "development methodology"
applies-to: []  # TODO: backend | frontend | infrastructure | cloud | mobile | data | ml | all
complexity: ""  # TODO: low | medium | high
maturity: ""    # TODO: established | emerging | theoretical
theorist: ""    # TODO: primary originator or "multiple"
year: null      # TODO: year concept was formally named/published
related: []     # TODO: IDs of related entries
tags: []        # TODO: free-form tags
---

## Definition

Sequential phases: requirements → design → implementation → verification → maintenance. Each phase must complete before the next begins.

## Example

A defence contractor delivering firmware for a flight control system: requirements are contractually fixed, sign-off at each phase is auditable, and changes require formal change requests with impact assessment.

## Strengths

- Predictable — milestones and deliverables are defined upfront
- Auditable — each phase produces documented artifacts
- Well-suited to fixed-requirement, safety-critical, or regulated domains

## Weaknesses

- Cannot accommodate requirements change without expensive change management
- Defects found late (verification phase) are 10-100x more expensive to fix than defects found at design
- Working software appears only at the very end

## Mitigation

Combine with prototyping phases to validate requirements before design is locked. Use incremental waterfall (mini-waterfalls per module) to surface integration issues earlier.
