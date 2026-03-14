---
id: dpia
title: "DPIA — Data Protection Impact Assessment"
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

Required under GDPR Art. 35 for high-risk processing. Systematically assesses: nature and purposes of processing; necessity and proportionality; risks to individuals; mitigating measures.

## Example

Before deploying facial recognition attendance, an HR team completes a DPIA: identifies biometric special category data, documents necessity analysis, identifies risks (breach, function creep, employee chilling effect), documents mitigations (local processing only, retention limits, access controls), gets DPO sign-off.

## Strengths

- Surfaces privacy risks before deployment — when they are cheapest to mitigate
- Required by GDPR Art. 35 — not optional for high-risk processing
- Produces an auditable record of the decision-making process

## Weaknesses

- Can become a checkbox exercise without genuine risk analysis
- Resource-intensive for small organisations without a dedicated privacy function
- "High risk" is not always obvious — triggers are not exhaustively defined

## Mitigation

Use a DPIA template with mandatory risk scoring. Require DPO or senior privacy review for any processing involving special categories, children, or large-scale monitoring. Tie completion to a go/no-go gate in the SDLC.
