---
id: surveillance-capitalism
title: "Surveillance Capitalism (Shoshana Zuboff)"
domain: privacy
sub-domain: "foundational theory"
applies-to: [all]
complexity: low
maturity: established
theorist: Shoshana Zuboff
year: 2019
related: [privacy-as-limitation-of-power, privacy-as-a-human-right, data-minimisation, consent-management]
tags: [behavioral-data, prediction, advertising, tech-critique, data-economy]
---

## Definition

Human experience is treated as raw material for extraction and prediction products sold to third parties. Users are not customers — they are the raw material. The asymmetry of knowledge between platforms and users is the central power imbalance.

## Example

Google's advertising ecosystem: search queries, location history, Gmail content, YouTube watch history, and Chrome browsing are combined to build behavioural profiles sold to advertisers. The user receives the service "free"; the product is their future behaviour, predicted and sold.

## Strengths

- Explains the economic logic driving privacy violations — essential for evaluating third-party integrations
- Provides a framework for understanding why "consent" is insufficient in asymmetric power relationships
- Motivates the data minimisation and purpose limitation principles at a deeper level

## Weaknesses

- Critique without a constructive alternative — "don't use third-party analytics" is hard for resource-constrained teams
- Can feel paralyzing without actionable guidance
- Some data collection genuinely improves products — the theory can over-generalise

## Mitigation

Evaluate every third-party SDK and analytics integration for behavioural data extraction patterns before adoption. Prefer open-source, self-hosted alternatives (Plausible, PostHog self-hosted) for sensitive data contexts.
