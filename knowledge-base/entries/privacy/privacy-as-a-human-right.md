---
id: privacy-as-a-human-right
title: "Privacy as a Human Right"
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

Article 12 of the Universal Declaration of Human Rights (1948) and Article 8 of the European Convention on Human Rights (1950) establish privacy as a fundamental right grounded in human dignity — not in utility.

## Example

GDPR's Article 7 right to withdraw consent, Apple's App Tracking Transparency requiring explicit opt-in before cross-app tracking, and the EU-US Data Privacy Framework all operationalise the human rights framing as legal obligations.

## Strengths

- Grounds privacy in dignity — harder to trade away against economic interests
- Creates legal obligations on organisations rather than voluntary best-practice
- Provides a principled basis for refusing "we have consent" as a complete justification

## Weaknesses

- Human rights framing is difficult to operationalise in engineering — it requires interpretation
- Jurisdiction-dependent enforcement — rights that exist in the EU may not exist in the US
- Can feel abstract to engineers who need concrete implementation guidance

## Mitigation

Implement FIPPs operationally as the engineering expression of privacy rights. Use the DPIA process to surface rights obligations before a feature is built.
