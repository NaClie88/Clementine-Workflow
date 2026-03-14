---
id: secure-by-default
title: "Secure by Default"
domain: security
sub-domain: "foundational principles"
applies-to: [all]
complexity: low
maturity: established
theorist: multiple
year: 1999
related: [attack-surface-minimisation, fail-secure, least-privilege, defence-in-depth]
tags: [default-deny, hardening, configuration, security-posture]
---

## Definition

Systems should be secure in their default configuration. The least-secure configuration should require explicit effort to achieve.

## Example

Spring Security in a Java application requires explicit opt-out of CSRF protection — by default, all state-changing requests require a CSRF token. A developer who doesn't configure it is protected; one who disables it must do so deliberately and explicitly.

## Strengths

- Protects users when developers don't know what they don't know
- Reduces security misconfiguration — the most common category of security failure
- Security experts don't need to review every deployment to ensure basic protection

## Weaknesses

- Secure defaults sometimes conflict with development convenience — developers disable them for speed
- Developers who don't understand the default may disable it without understanding the risk
- "Secure by default" can create false confidence in the default configuration

## Mitigation

Document what each default does and why. Make disabling a secure default require explicit, self-documenting configuration. Flag overrides of secure defaults in code review.
