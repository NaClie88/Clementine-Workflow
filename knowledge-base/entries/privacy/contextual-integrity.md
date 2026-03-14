---
id: contextual-integrity
title: "Contextual Integrity (Helen Nissenbaum)"
domain: privacy
sub-domain: "foundational theory"
applies-to: [all]
complexity: medium
maturity: established
theorist: Helen Nissenbaum
year: 2004
related: [privacy-as-control, privacy-by-design, gdpr, consent-management]
tags: [information-flow, context, norms, appropriateness, social-norms]
---

## Definition

Privacy is about appropriate information flow, not just secrecy. Information flows appropriately when it matches the norms of the context in which it was originally shared.

## Example

A fitness app that shares step count data with a health insurance company for premium discounts. The user shared data in a fitness tracking context; the insurance pricing context violates contextual norms even if the user "consented" in buried terms.

## Strengths

- Explains privacy violations that purely technical definitions (secrecy, consent) miss
- Provides a concrete design question: "does this data flow match the norms of the original sharing context?"
- Captures why aggregation and secondary use feel like violations even when no secret is disclosed

## Weaknesses

- Contextual norms are not universal — different cultures have different expectations
- Hard to encode algorithmically — requires human judgment about norms
- "Norms" are contested, especially in new domains like social media

## Mitigation

Use contextual integrity as a design review lens. For each data flow, ask explicitly: "Does this flow match the norms of the context in which the user shared this?" Flag flows that don't match and escalate to the Operator.
