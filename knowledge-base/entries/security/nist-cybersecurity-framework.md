---
id: nist-cybersecurity-framework
title: "NIST Cybersecurity Framework (CSF 2.0)"
domain: security
sub-domain: "industry frameworks"
applies-to: []  # TODO: backend | frontend | infrastructure | cloud | mobile | data | ml | all
complexity: ""  # TODO: low | medium | high
maturity: ""    # TODO: established | emerging | theoretical
theorist: ""    # TODO: primary originator or "multiple"
year: null      # TODO: year concept was formally named/published
related: []     # TODO: IDs of related entries
tags: []        # TODO: free-form tags
---

## Definition

Six functions: Govern, Identify, Protect, Detect, Respond, Recover. Technology-neutral, risk-based. Widely accepted for regulatory communication.

## Example

A financial institution — Identify: asset inventory and risk register. Protect: MFA on all admin accounts, network segmentation. Detect: SIEM with 24h alert SLA. Respond: IR playbooks for top 5 incident types. Recover: RTO < 4h for core banking. Govern: board-level security risk ownership.

## Strengths

- Technology-neutral — applies across industries and architectures
- Maps to other frameworks (ISO 27001, CIS Controls) for gap analysis
- Widely accepted for regulatory and executive communication

## Weaknesses

- High-level guidance requires significant interpretation for implementation
- CSF 2.0 (2024) adds Govern but adoption is early — most practitioners are still on v1.1
- Compliance-oriented use often produces documentation without security improvement

## Mitigation

Use CIS Controls as the implementation layer under CSF — they provide specific, prioritised, actionable controls. Use CSF for communication; use CIS Controls for implementation.
