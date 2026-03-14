---
id: soc-2
title: "SOC 2 (AICPA)"
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

Audit framework for service organisations. Five Trust Service Criteria: Security, Availability, Processing Integrity, Confidentiality, Privacy. Type II: sustained controls over 6–12 months.

## Example

A cloud storage provider's Type II audit: over 12 months, an auditor samples evidence that encryption at rest was enforced (CC6.1), access was reviewed quarterly (CC6.2), and incidents were logged and resolved within SLA (CC7.3).

## Strengths

- Enterprise customer requirement for vendor onboarding — often mandatory for B2B SaaS
- Type II proves sustained control operation, not just point-in-time compliance
- Flexible scope — applies to any service organisation

## Weaknesses

- Expensive: auditor fees $30k–$100k+; internal preparation overhead
- Scope can be narrowed to exclude problematic areas while passing the audit
- Attestation ≠ security — a SOC 2 report is not a security assessment

## Mitigation

Use compliance automation tooling to reduce evidence collection overhead. Treat SOC 2 preparation as a security improvement exercise. Supplement with penetration testing — SOC 2 does not test for exploitability.
