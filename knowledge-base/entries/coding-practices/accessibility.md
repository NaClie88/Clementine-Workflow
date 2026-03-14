---
id: accessibility
title: "Accessibility (A11y)"
domain: coding-practices
sub-domain: "coding discipline"
applies-to: [frontend]
complexity: medium
maturity: established
theorist: Tim Berners-Lee
year: 1997
related: [principle-of-least-astonishment, api-design]
tags: [wcag, a11y, screen-readers, inclusive-design, aria]
---

## Definition

Build accessibility in from the start. WCAG 2.1 AA is the legal baseline in most jurisdictions. Retrofitting is expensive.

## Example

A form with `<label for="email">Email</label><input id="email" type="email">` — screen readers announce the label when the input is focused. Contrast ratio ≥ 4.5:1 for normal text (WCAG AA 1.4.3). All interactive elements reachable via keyboard Tab.

## Strengths

- Broadens the user base — 15–20% of the population has a disability
- Often legally required (ADA, EN 301 549, AODA)
- Semantic HTML improves SEO as a side effect

## Weaknesses

- Retrofitting accessibility into existing UIs is expensive — it touches layout, interaction, and content
- Automated tools catch only 30–40% of WCAG violations — manual testing is required
- Requires screen reader testing across multiple assistive technologies

## Mitigation

Build accessibility into the component library from the start. Include a screen reader check in the Definition of Done for all UI work. Test with at least NVDA + Firefox and VoiceOver + Safari.
