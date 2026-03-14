---
id: privacy-by-design
title: "Privacy by Design (Ann Cavoukian — 7 Principles)"
domain: privacy
sub-domain: "foundational theory"
applies-to: [all]
complexity: medium
maturity: established
theorist: Ann Cavoukian
year: 1995
related: [fair-information-practice-principles, data-minimisation, gdpr, dpia]
tags: [privacy-engineering, proactive, default-settings, gdpr-article-25, seven-principles]
---

## Definition

Privacy is built into the system design, not bolted on afterward. Seven foundational principles: proactive/preventative, privacy as default, embedded in design, full functionality (positive-sum), end-to-end security, visibility and transparency, respect for user privacy.

## Example

Signal messenger implements all seven: E2EE by default (principle 2), minimal metadata collection (principle 1, 7), open-source auditable code (principle 6), messages deleted on read if configured (principle 5), no ads or third-party trackers (principle 3).

## Strengths

- Proactive — builds privacy in rather than managing breaches after the fact
- Principle 4 (positive-sum) rejects the false "privacy vs. security" trade-off
- Adopted by GDPR Article 25 as a legal requirement — not just best practice

## Weaknesses

- Seven principles are high-level — operationalising them requires significant interpretation
- "Privacy by design" is claimed by many systems that implement only superficial changes
- No enforcement mechanism beyond GDPR's Article 25, which has rarely been prosecuted specifically

## Mitigation

Map each principle to specific engineering controls (principle 2 → E2EE by default, not opt-in; principle 1 → data minimisation checklist at design review). Include PbD review in the SDLC gate before any feature that collects new data.
