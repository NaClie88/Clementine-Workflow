---
id: mitre-att-ck-framework
title: "MITRE ATT&CK Framework"
domain: security
sub-domain: "threat modelling"
applies-to: []  # TODO: backend | frontend | infrastructure | cloud | mobile | data | ml | all
complexity: ""  # TODO: low | medium | high
maturity: ""    # TODO: established | emerging | theoretical
theorist: ""    # TODO: primary originator or "multiple"
year: null      # TODO: year concept was formally named/published
related: []     # TODO: IDs of related entries
tags: []        # TODO: free-form tags
---

## Definition

Knowledge base of adversary tactics, techniques, and procedures (TTPs) based on real-world attack observations. Matrices for Enterprise, Mobile, and ICS.

## Example

A SOC team maps an observed phishing campaign to ATT&CK: Initial Access T1566 (Phishing) → Execution T1204 (User Execution) → Persistence T1547 (Registry Run Keys) → C2 T1071 (Web Protocols). Detection rules are written for each technique; coverage gaps are identified and prioritised.

## Strengths

- Based on real adversary behaviour — not theoretical threats
- Shared vocabulary between offensive and defensive teams
- Enables detection gap analysis and red team planning against a common framework

## Weaknesses

- Vast scope — 14 tactics and hundreds of techniques; prioritisation is required
- Techniques evolve; the knowledge base requires continuous maintenance
- Mapping observed behaviour to ATT&CK requires analyst expertise

## Mitigation

Focus on the techniques most relevant to your industry and threat actors using ATT&CK Navigator heat maps. Prioritise detection coverage of high-frequency techniques relevant to your attack surface.
