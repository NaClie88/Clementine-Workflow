---
id: cis-controls
title: "CIS Controls (v8)"
domain: security
sub-domain: "industry frameworks"
applies-to: []  # TODO: backend | frontend | infrastructure | cloud | mobile | data | ml | all
complexity: ""  # TODO: low | medium | high
maturity: ""    # TODO: established | emerging | theoretical
theorist: ""    # TODO: primary originator or "multiple"
year: null      # TODO: year concept was formally named/published
related: []     # TODO: IDs of related entries
tags: []        # TODO: free-form tags
---

## Definition

Eighteen prioritised security controls in three implementation groups (IG1/2/3). IG1 covers the most critical controls for all organisations.

## Example

IG1 (essential hygiene): inventory all hardware (CIS 1), all software (CIS 2), configure securely (CIS 4), manage access (CIS 5), manage vulnerabilities (CIS 7). A small organisation implementing only IG1 blocks the vast majority of commodity attacks.

## Strengths

- Prioritised — IG1 gives the greatest risk reduction per unit of effort
- Practical and specific — each control has defined sub-controls and implementation guidance
- Free, with detailed benchmarks for specific technologies

## Weaknesses

- Prescriptive controls may not map cleanly to all architectures (cloud-native, serverless)
- IG3 is resource-intensive — appropriate only for large, mature security programmes
- Does not explicitly address AI/ML system security or supply chain risks

## Mitigation

Start with IG1 regardless of organisation size — it blocks commodity attacks efficiently. Use CIS Benchmarks for specific technology hardening (AWS, Kubernetes, Linux). Add IG2/3 controls based on risk profile.
