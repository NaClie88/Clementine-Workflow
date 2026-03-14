---
id: privacy-as-control
title: "Privacy as Control (Westin)"
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

Privacy is the individual's ability to control information about themselves — when, how, and to what extent it is communicated to others.

## Example

GDPR's rights to access, rectification, erasure, portability, and consent withdrawal are each a mechanism by which users exercise control. Apple's privacy settings dashboard implements this directly.

## Strengths

- Intuitive to users — people understand "my data, my control"
- Directly implementable as product features (access portals, consent management, deletion requests)
- Aligns with most privacy regulations' consent and rights frameworks

## Weaknesses

- Meaningful control is undermined by 50-page privacy policies and dark patterns
- Control without comprehension is illusory — users click "accept" without understanding
- Does not address aggregation and inference harms where no single data point was misused

## Mitigation

Supplement control mechanisms with plain-language disclosure. Audit consent flows for dark patterns (pre-ticked boxes, consent walls, buried opt-outs). Pair with data minimisation so there is less to control.
