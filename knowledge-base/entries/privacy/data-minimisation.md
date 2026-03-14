---
id: data-minimisation
title: "Data Minimisation"
domain: privacy
sub-domain: "technical approach"
applies-to: [all]
complexity: low
maturity: established
theorist: multiple
year: 1973
related: [privacy-by-design, gdpr, differential-privacy, anonymisation-vs-pseudonymisation]
tags: [data-hygiene, collection-limitation, retention-policy, purpose-limitation]
---

## Definition

Collect only what is strictly necessary. Data that is never collected cannot be breached.

## Example

A registration form that asks only for email and password. Stripe Checkout collects payment data directly so the merchant never holds raw card numbers — they receive only a token.

## Strengths

- Most reliable form of data protection — eliminates risk at the source
- Simplifies compliance — less data means fewer rights obligations
- Reduces storage costs and breach impact

## Weaknesses

- Teams resist minimisation citing "future use" — product managers see data as an asset
- Removing existing data collection is politically harder than preventing new collection
- "Minimum necessary" requires judgment about what the function actually requires

## Mitigation

Require documented justification for every data field at design time. Audit data fields for use — remove fields that have not been accessed in N months. Treat new data collection as requiring approval, not as a default.
