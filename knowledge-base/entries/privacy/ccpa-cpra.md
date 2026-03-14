---
id: ccpa-cpra
title: "CCPA / CPRA (California, 2020/2023)"
domain: privacy
sub-domain: "regulatory framework"
applies-to: []  # TODO: backend | frontend | infrastructure | cloud | mobile | data | ml | all
complexity: ""  # TODO: low | medium | high
maturity: ""    # TODO: established | emerging | theoretical
theorist: ""    # TODO: primary originator or "multiple"
year: null      # TODO: year concept was formally named/published
related: []     # TODO: IDs of related entries
tags: []        # TODO: free-form tags
---

## Definition

Rights to know, delete, opt out of sale, and non-discrimination. CPRA adds: right to correct, right to limit use of sensitive personal information, and enforcement via a dedicated Privacy Protection Agency.

## Example

A US retailer adds a "Do Not Sell or Share My Personal Information" link in the footer, implements an opt-out API for data brokers, and builds a DSAR portal for access and deletion requests within 45 days.

## Strengths

- Strong opt-out rights for California residents; applies to mid-size businesses
- CPRA adds sensitive data category protections similar to GDPR's special categories
- Driving a de facto national standard in the absence of US federal privacy law

## Weaknesses

- Opt-out (not opt-in) model means data collection proceeds by default
- Enforcement has been inconsistent historically
- Narrower than GDPR — notably weaker on consent requirements

## Mitigation

Implement GDPR-level consent management — it satisfies CCPA/CPRA and most other US state laws as a superset. Avoid building separate compliance stacks per jurisdiction.
