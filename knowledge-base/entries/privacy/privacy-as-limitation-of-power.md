---
id: privacy-as-limitation-of-power
title: "Privacy as Limitation of Power (Solove's Taxonomy)"
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

Privacy violations are not a single thing — they are a taxonomy of harmful activities: surveillance, aggregation, intrusion, decisional interference, secondary use, disclosure, blackmail, exposure.

## Example

The aggregation problem — a name (public) + employer (public) + medical condition (semi-public) + home address (public) = a dossier that enables targeted harassment. Each piece is innocuous; the combination is a violation. No single data point was misused.

## Strengths

- Identifies harms that control-based models miss (aggregation, secondary use, inference)
- Each harm type implies a different mitigation
- Explains why "we only use public information" is not a complete defence

## Weaknesses

- Taxonomic approach doesn't directly prescribe technical controls — requires interpretation
- The full taxonomy is complex and not well-known among engineers
- Some categories overlap (disclosure vs. exposure) in ways that complicate application

## Mitigation

Apply data minimisation and purpose limitation to prevent aggregation. Evaluate each secondary use against the harm taxonomy before approval. Include aggregation risk in threat models for analytics systems.
