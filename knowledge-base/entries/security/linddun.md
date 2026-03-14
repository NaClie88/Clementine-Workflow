---
id: linddun
title: "LINDDUN (KU Leuven)"
domain: security
sub-domain: "threat modelling"
applies-to: [all]
complexity: medium
maturity: established
theorist: "Mina Deng, Kim Wuyts, Riccardo Scandariato, Bart Preneel"
year: 2010
related: [stride, privacy-by-design, gdpr, dpia]
tags: [privacy-threat-modelling, linkability, identifiability, disclosure, unawareness]
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
