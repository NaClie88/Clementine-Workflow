---
id: cia-triad
title: "CIA Triad"
domain: security
sub-domain: "foundational principles"
applies-to: []  # TODO: backend | frontend | infrastructure | cloud | mobile | data | ml | all
complexity: ""  # TODO: low | medium | high
maturity: ""    # TODO: established | emerging | theoretical
theorist: ""    # TODO: primary originator or "multiple"
year: null      # TODO: year concept was formally named/published
related: []     # TODO: IDs of related entries
tags: []        # TODO: free-form tags
---

## Definition

- **Confidentiality:** information accessible only to authorised parties
- **Integrity:** information is accurate and has not been tampered with
- **Availability:** information and systems are accessible when needed

Extended by some frameworks to include: **Authenticity** (source is who they claim) and **Non-repudiation** (a party cannot deny performing an action).

## Example

A database system: Confidentiality — AES-256 encryption at rest and TLS in transit; Integrity — checksums and write-ahead logs prevent silent corruption; Availability — multi-AZ replication with automatic failover. A ransomware attack simultaneously targets all three: encrypts (confidentiality broken), corrupts (integrity broken), and denies access (availability broken).

## Strengths

- Simple, memorable framework — widely understood across technical and non-technical audiences
- Maps directly to control selection — encrypt for confidentiality, sign for integrity, replicate for availability
- Provides a complete first-pass view of what a system must protect

## Weaknesses

- Does not directly address authenticity, non-repudiation, or privacy
- Can lead to siloed thinking — each property optimised independently at the expense of the others
- Availability and confidentiality can conflict (a system locked down for security may be unavailable)

## Mitigation

Use CIA as a framework for initial control identification. Supplement with STRIDE threat modelling for systematic coverage of threats the triad doesn't name. Add Authenticity and Non-repudiation for systems that need them.
