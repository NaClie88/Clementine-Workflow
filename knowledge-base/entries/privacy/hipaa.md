---
id: hipaa
title: "HIPAA (US, 1996)"
domain: privacy
sub-domain: "regulatory framework"
applies-to: [backend, data, cloud]
complexity: high
maturity: established
theorist: US Congress
year: 1996
related: [gdpr, data-minimisation, cryptographic-hygiene, end-to-end-encryption]
tags: [healthcare, phi, covered-entity, us-regulation, compliance, baa]
---

## Definition

Governs Protected Health Information (PHI). Privacy Rule: standards for use and disclosure. Security Rule: administrative, physical, and technical safeguards for electronic PHI.

## Example

A telehealth platform implements: Business Associate Agreements with all vendors, role-based access controls on PHI, audit logs of all PHI access, automatic session timeouts after 15 minutes of inactivity, and encrypted backups with tested restore procedures.

## Strengths

- Comprehensive PHI protection requirements
- BAA model extends obligations to all vendors handling PHI
- Breach notification requirements ensure user notification

## Weaknesses

- Focused on administrative and technical controls — does not always produce good security outcomes
- Breach safe harbour for "encrypted" data creates perverse incentives (weak encryption = safe harbour)
- Does not cover health data held by non-covered entities (fitness apps, direct-to-consumer genetic tests)

## Mitigation

Treat HIPAA as a floor. Apply NIST SP 800-66 as implementation guidance. Apply defence in depth beyond minimum controls — especially for cloud-hosted PHI.
