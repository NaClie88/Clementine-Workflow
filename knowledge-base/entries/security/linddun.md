---
id: linddun
title: "LINDDUN (KU Leuven)"
domain: security
sub-domain: "threat modelling"
applies-to: []  # TODO: backend | frontend | infrastructure | cloud | mobile | data | ml | all
complexity: ""  # TODO: low | medium | high
maturity: ""    # TODO: established | emerging | theoretical
theorist: ""    # TODO: primary originator or "multiple"
year: null      # TODO: year concept was formally named/published
related: []     # TODO: IDs of related entries
tags: []        # TODO: free-form tags
---

## Definition

Privacy-specific threat modelling mirroring STRIDE: Linkability, Identifiability, Non-repudiation, Detectability, Disclosure of information, Unawareness, Non-compliance.

## Example

A healthcare app DFD — Linkability: user queries across sessions build a longitudinal health profile (mitigation: unlinkable tokens per session). Identifiability: IP + symptom queries identify the user (mitigation: differential privacy on query logs). Unawareness: users don't know their queries are retained (mitigation: in-app disclosure).

## Strengths

- Privacy-specific — STRIDE systematically misses privacy threats
- Structured approach produces actionable mitigations for each privacy threat type
- Complements STRIDE — together they cover both security and privacy

## Weaknesses

- Requires privacy engineering expertise to apply well
- Less tool support than STRIDE — fewer automated analysis options
- Less widely known — finding practitioners is harder

## Mitigation

Use LINDDUN alongside STRIDE for any system that handles personal data. Include at least one privacy engineer in the threat modelling session.
