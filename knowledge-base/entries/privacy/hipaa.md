---
id: hipaa
title: "HIPAA (US, 1996)"
domain: privacy
sub-domain: "regulatory framework"
applies-to: []  # TODO: backend | frontend | infrastructure | cloud | mobile | data | ml | all
complexity: ""  # TODO: low | medium | high
maturity: ""    # TODO: established | emerging | theoretical
theorist: ""    # TODO: primary originator or "multiple"
year: null      # TODO: year concept was formally named/published
related: []     # TODO: IDs of related entries
tags: []        # TODO: free-form tags
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
