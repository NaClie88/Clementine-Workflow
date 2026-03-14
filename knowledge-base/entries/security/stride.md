---
id: stride
title: "STRIDE (Microsoft)"
domain: security
sub-domain: "threat modelling"
applies-to: [all]
complexity: medium
maturity: established
theorist: "Praerit Garg, Loren Kohnfelder"
year: 1999
related: [pasta, attack-trees, owasp-top-10, linddun]
tags: [threat-modelling, spoofing, tampering, repudiation, information-disclosure, denial-of-service]
---

## Definition

Six threat categories applied to data flow diagrams: Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, Elevation of Privilege.

## Example

Threat modelling a login endpoint — Spoofing: brute force/credential stuffing → rate limiting + MFA. Tampering: session token manipulation → signed JWT. Repudiation: login log manipulation → append-only audit log. Information Disclosure: passwords in logs → sanitise sensitive fields. DoS: login flood → rate limit + CAPTCHA. EoP: JWT algorithm confusion attack → enforce algorithm server-side.

## Strengths

- Systematic — covers six distinct threat categories
- Maps directly to mitigations
- Works well with DFDs — boundary-by-boundary analysis is tractable

## Weaknesses

- Produces long lists of threats without inherent prioritisation
- Requires facilitation skill to run effectively in a group
- Often done too late in the process (after the design is committed)

## Mitigation

Combine with risk scoring (CVSS or simple High/Medium/Low) to prioritise. Embed in design reviews before architecture is committed, not as a retrofit.
