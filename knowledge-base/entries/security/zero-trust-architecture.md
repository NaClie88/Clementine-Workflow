---
id: zero-trust-architecture
title: "Zero Trust Architecture"
domain: security
sub-domain: "foundational principles"
applies-to: [all]
complexity: high
maturity: established
theorist: John Kindervag
year: 2010
related: [least-privilege, complete-mediation, defence-in-depth, federated-identity]
tags: [never-trust-always-verify, microsegmentation, identity-first, iam, bzt]
---

## Definition

"Never trust, always verify." No user, device, or network location is trusted by default — not even internal networks. Every access request is authenticated, authorised, and encrypted regardless of origin.

## Example

Google BeyondCorp: employees access internal services via an identity-aware proxy. No VPN. Access is granted based on device health posture, user identity, and contextual signals — not network location. A compromised laptop on the corporate LAN receives the same treatment as an unknown device on public WiFi.

```
Traditional model:  [internet] -> [firewall] -> [trusted internal network]
                    Inside the firewall = trusted. VPN = trusted.

Zero Trust model:   [every request] -> [identity + device health check] -> [specific resource]
                    No implicit trust. Every access is verified every time.
```

## Strengths

- Eliminates implicit trust from network location — lateral movement after initial breach is contained
- Enables remote work and BYOD without VPN infrastructure
- Supports micro-segmentation — compromised component cannot reach unrelated systems

## Weaknesses

- Requires mature identity management (IdP), device management (MDM), and network infrastructure
- Complex to retrofit onto legacy systems designed for perimeter security
- Session continuity (long-lived tokens vs. continuous re-verification) requires careful design

## Mitigation

Implement incrementally — start with the most sensitive applications. Use NIST SP 800-207 as the reference architecture. Invest in device posture checking (certificate health, OS patch level) before full implementation.
