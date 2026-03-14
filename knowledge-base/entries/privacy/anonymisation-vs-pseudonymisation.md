---
id: anonymisation-vs-pseudonymisation
title: "Anonymisation vs. Pseudonymisation"
domain: privacy
sub-domain: "technical approach"
applies-to: []  # TODO: backend | frontend | infrastructure | cloud | mobile | data | ml | all
complexity: ""  # TODO: low | medium | high
maturity: ""    # TODO: established | emerging | theoretical
theorist: ""    # TODO: primary originator or "multiple"
year: null      # TODO: year concept was formally named/published
related: []     # TODO: IDs of related entries
tags: []        # TODO: free-form tags
---

## Definition

- **Anonymisation:** data cannot, by any reasonable means, be traced back to an individual. Truly anonymous data is outside GDPR scope. Genuinely difficult to achieve.
- **Pseudonymisation:** identifiers replaced with tokens; re-identification possible with the mapping table. Reduces risk; data remains personal under GDPR.

## Example

Netflix Prize dataset (2006): 500,000 "anonymised" users re-identified by Narayanan and Shmatikoff by correlating with public IMDb ratings. True anonymisation failed. Pseudonymisation: replace `user_id` with `HMAC-SHA256(user_id, secret_salt)` — re-identification requires the salt.

## Strengths

- True anonymisation removes GDPR applicability entirely (if genuine)
- Pseudonymisation reduces breach impact — the mapping table is the valuable asset
- Both reduce regulatory risk relative to plaintext PII

## Weaknesses

- True anonymisation is very hard to achieve with high-dimensional data — re-identification attacks are common
- Pseudonymised data is still personal data under GDPR — compliance obligations remain
- k-anonymity alone is insufficient against background knowledge attacks

## Mitigation

Apply the "motivated intruder test" — assume an attacker will attempt re-identification with available background data. Supplement with k-anonymity (k≥5), l-diversity, or differential privacy for statistical releases.
