---
id: coppa
title: "COPPA (US, 1998)"
domain: privacy
sub-domain: "regulatory framework"
applies-to: [frontend, backend, data]
complexity: medium
maturity: established
theorist: US Congress
year: 1998
related: [gdpr, consent-management, data-minimisation]
tags: [children, age-verification, parental-consent, us-regulation, ftc]
---

## Definition

Operators of websites directed at children under 13 must obtain verifiable parental consent before collecting personal information.

## Example

A children's education app implements: verifiable parental consent via credit card micro-transaction verification, no behavioural advertising, data deletion within 30 days of parental request, no data sharing with third parties without consent.

## Strengths

- Strong protection for a vulnerable population
- Applies regardless of operator intent if the service is directed at children
- FTC enforcement has produced significant settlements

## Weaknesses

- "Verifiable parental consent" is operationally difficult and easily circumvented
- Age verification methods are unreliable and create friction for legitimate users
- Does not protect teens (13-17) despite similar vulnerabilities

## Mitigation

Apply COPPA requirements to any service that might plausibly be used by under-13s — err conservative. Build parental consent flows early; retrofitting is expensive.
