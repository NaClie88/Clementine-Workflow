---
id: chaos-engineering
title: "Chaos Engineering"
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

Deliberately inject failures into a system to verify that it is resilient.

## Example

Netflix Chaos Monkey randomly terminates EC2 instances in production during business hours. Teams that cannot handle random instance loss fix their resilience; teams whose systems survive gain confidence in their design.

## Strengths

- Proves resilience under real conditions — not just assumed
- Surfaces hidden dependencies and single points of failure
- Builds operational confidence that documentation alone cannot provide

## Weaknesses

- Production impact risk if resilience is not yet mature enough
- Requires mature observability and rollback capabilities before running experiments
- Cultural resistance: "you want to break production on purpose?"

## Mitigation

Start in staging. Define a "blast radius" for each experiment. Run during business hours when the team can respond. Use the GameDay format for first experiments.
