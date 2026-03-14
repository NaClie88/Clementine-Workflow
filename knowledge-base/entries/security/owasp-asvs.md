---
id: owasp-asvs
title: "OWASP ASVS (Application Security Verification Standard)"
domain: security
sub-domain: "industry frameworks"
applies-to: [backend, frontend]
complexity: high
maturity: established
theorist: OWASP Foundation
year: 2008
related: [owasp-top-10, nist-cybersecurity-framework, input-validation-output-encoding]
tags: [verification, security-requirements, assurance-levels, checklist, level-1-2-3]
---

## Definition

Defines security requirements at three assurance levels. Level 1: opportunistic security; Level 2: standard for most applications; Level 3: critical applications (financial, healthcare, safety).

## Example

Level 2 assessment of a payment API: V2 (authentication — MFA required), V3 (session management — 30-minute idle timeout), V4 (access control — RBAC with object-level checks), V5 (validation — all inputs validated and encoded), V6 (cryptography — TLS 1.2+ only, no weak ciphers).

## Strengths

- Specific, testable requirements — each control has a clear pass/fail criterion
- Three levels match the control intensity to the risk level of the application
- Maps to OWASP Testing Guide for verification procedures

## Weaknesses

- Level 3 is resource-intensive to achieve and verify
- Requirements are written for web applications — require interpretation for APIs and native apps
- Not all requirements apply to all architectures

## Mitigation

Use ASVS Level 1 as a penetration test scope baseline. Level 2 for any application handling personal data or financial transactions. Level 3 for safety-critical or high-value financial systems.
