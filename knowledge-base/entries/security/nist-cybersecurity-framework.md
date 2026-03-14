---
id: nist-cybersecurity-framework
title: "NIST Cybersecurity Framework (CSF 2.0)"
domain: security
sub-domain: "industry frameworks"
applies-to: [all]
complexity: medium
maturity: established
theorist: NIST
year: 2014
related: [iso-iec-27001, cis-controls, incident-response]
tags: [identify-protect-detect-respond-recover, risk-management, us-government, csf]
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
