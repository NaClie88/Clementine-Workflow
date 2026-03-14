---
id: privacy-enhancing-technologies
title: "Privacy-Enhancing Technologies (PETs)"
domain: privacy
sub-domain: "technical approach"
applies-to: [all]
complexity: high
maturity: established
theorist: multiple
year: 1995
related: [differential-privacy, anonymisation-vs-pseudonymisation, zero-knowledge-proof-architectures, homomorphic-encryption, secure-multi-party-computation]
tags: [cryptography, data-protection, anonymisation, pet, k-anonymity]
---

## Definition

A broad category of technologies that enable useful computation or data sharing while limiting privacy exposure. Includes homomorphic encryption, secure multi-party computation, federated learning, onion routing, and ZKPs.

## Example

Google's Gboard federated learning: the next-word prediction model is trained on-device. Only model gradient updates (not keystrokes) are sent to Google's servers, aggregated, and used to update the global model. No keystrokes ever leave the device.

## Strengths

- Enable useful computation without centralising raw data
- Reduce breach impact — raw data is never in one place
- Address threats that access controls alone cannot prevent (insider threat, cloud provider access)

## Weaknesses

- PETs add engineering complexity and computational overhead
- Some PETs (fully homomorphic encryption) are not yet practical at scale
- "PET-washing" — claiming PETs provide stronger guarantees than they actually do

## Mitigation

Select PETs based on the specific threat model, not trend. Federated learning addresses centralisation risk. ZKP addresses disclosure risk. Homomorphic encryption addresses computation-on-sensitive-data risk. Match the tool to the threat.
