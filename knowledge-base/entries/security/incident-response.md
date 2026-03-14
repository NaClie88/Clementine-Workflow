---
id: incident-response
title: "Incident Response"
domain: security
sub-domain: "secure development"
applies-to: []  # TODO: backend | frontend | infrastructure | cloud | mobile | data | ml | all
complexity: ""  # TODO: low | medium | high
maturity: ""    # TODO: established | emerging | theoretical
theorist: ""    # TODO: primary originator or "multiple"
year: null      # TODO: year concept was formally named/published
related: []     # TODO: IDs of related entries
tags: []        # TODO: free-form tags
---

## Definition

NIST SP 800-61 phases: Prepare → Detect & Analyse → Contain, Eradicate & Recover → Post-Incident Activity.

## Example

A SIEM alert fires on anomalous data exfiltration at 2am. IR playbook: confirm true positive (15 minutes), isolate affected system (30 minutes), scope the breach (2 hours), rotate all credentials used by the compromised system (4 hours), notify affected users per breach notification policy, write post-mortem within 5 business days.

## Strengths

- Structured response reduces chaos and decision fatigue during incidents
- Pre-written playbooks reduce time-to-contain — minutes matter
- Post-incident activity produces systemic improvements

## Weaknesses

- IR plans are often not tested until a real incident — tabletop exercises are deprioritised
- Containment vs. forensic preservation creates tension — containment destroys evidence; preservation allows damage to continue
- IR plans are often stored on the systems they cover — inaccessible when those systems are down

## Mitigation

Run tabletop exercises quarterly for top incident scenarios. Store IR plans offline and in a hardcopy. Define forensic preservation windows in the plan — collect evidence for N hours before containment unless damage is ongoing.
