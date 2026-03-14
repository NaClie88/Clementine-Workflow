---
id: trunk-based-development
title: "Trunk-Based Development"
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

All developers commit to a single shared branch (trunk/main) at least daily. Short-lived feature branches are acceptable; long-lived branches are not.

## Example

Google's monorepo: thousands of engineers commit to a single trunk. Feature flags hide incomplete work. Every commit triggers a full test suite; broken builds are rolled back within minutes.

## Strengths

- No integration debt — the system is always in a known, integrated state
- Forces small, reviewable commits
- Main is always releasable

## Weaknesses

- Requires fast CI (a slow test suite kills the daily-commit discipline)
- Incomplete features must be hidden behind flags — flag management is a new overhead
- Cultural discipline required — one careless commit can block everyone

## Mitigation

Invest in fast CI (target: < 10 minutes to green). Establish clear feature flag lifecycle management with a planned removal date at creation time.
