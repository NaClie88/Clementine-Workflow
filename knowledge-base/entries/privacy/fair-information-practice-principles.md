---
id: fair-information-practice-principles
title: "Fair Information Practice Principles (FIPPs)"
domain: privacy
sub-domain: "foundational theory"
applies-to: []  # TODO: backend | frontend | infrastructure | cloud | mobile | data | ml | all
complexity: ""  # TODO: low | medium | high
maturity: ""    # TODO: established | emerging | theoretical
theorist: ""    # TODO: primary originator or "multiple"
year: null      # TODO: year concept was formally named/published
related: []     # TODO: IDs of related entries
tags: []        # TODO: free-form tags
---

## Definition

First codified by the US HEW (1973). Core: Notice, Choice, Access, Security, Enforcement. Basis of most subsequent privacy law globally.

## Example

Apple's App Store privacy nutrition labels implement Notice — users see what data categories an app collects before installing. GDPR Articles 13/14 notices implement the same principle at the regulatory level.

## Strengths

- Widely adopted — understanding FIPPs explains most privacy regulations
- Practical and implementable — each principle maps to engineering controls
- The foundational framework for GDPR, CCPA, PIPEDA, and most national privacy laws

## Weaknesses

- The notice-and-consent model is broken in practice — users don't read privacy policies
- Consent fatigue leads to blanket acceptance that negates the "choice" principle
- FIPPs were designed before surveillance capitalism — they underestimate aggregation and inference risks

## Mitigation

Supplement FIPPs with data minimisation and purpose limitation to reduce the volume of data that notice and consent must cover. Where less data is collected, consent is less critical because there is less to consent to.
