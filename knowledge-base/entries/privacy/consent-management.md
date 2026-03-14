---
id: consent-management
title: "Consent Management"
domain: privacy
sub-domain: "technical approach"
applies-to: [frontend, backend]
complexity: medium
maturity: established
theorist: multiple
year: 2016
related: [gdpr, ccpa-cpra, contextual-integrity, privacy-by-design]
tags: [opt-in, cookie-consent, preference-management, cmp, iab-tcf]
---

## Definition

Mechanisms by which users grant, deny, or withdraw consent for specific data uses. Consent must be: freely given, specific, informed, and unambiguous.

## Example

OneTrust CMP: a cookie consent banner categorises cookies (strictly necessary, functional, analytics, marketing), records consent with timestamp and consent text version, provides re-consent when policy changes, and supports withdrawal.

## Strengths

- Auditable consent trail satisfies GDPR Art. 7 record-keeping requirements
- Granular consent lets users accept necessary functions without accepting advertising
- Enables consent withdrawal linked to data deletion workflows

## Weaknesses

- Cookie banners are widely dismissed with "accept all" — consent fatigue is real
- Dark patterns in consent UIs (grey-out reject, consent walls) are rampant
- Consent management adds infrastructure complexity and UX friction

## Mitigation

Design consent UIs for genuine informed choice — equal visual prominence for accept and reject; no pre-ticked boxes; no consent walls. Supplement with data minimisation so less consent is required in the first place.
