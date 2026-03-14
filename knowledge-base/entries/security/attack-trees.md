---
id: attack-trees
title: "Attack Trees (Bruce Schneier)"
domain: security
sub-domain: "threat modelling"
applies-to: [all]
complexity: medium
maturity: established
theorist: Bruce Schneier
year: 1999
related: [stride, pasta, mitre-att-ck-framework]
tags: [threat-modelling, attack-paths, risk-analysis, tree-structure]
---

## Definition

Hierarchical representation of how an attacker achieves a goal. Root = goal; branches = alternative methods; leaves = atomic attack steps. Enables cost-benefit analysis of defences.

## Example

Root: "Exfiltrate customer database." Branch 1: SQL injection (leaf: unsanitised input in search field). Branch 2: Compromise DB admin credentials (leaf: phishing attack). Branch 3: Insider exfiltration (leaf: over-privileged DB account). Cost and detection probability at each leaf → mitigate cheapest leaves first.

## Strengths

- Visual and intuitive — stakeholders can understand the threat model
- Enables quantitative cost-benefit analysis of mitigations
- Reusable across similar systems

## Weaknesses

- Maintenance burden as systems change — trees can become stale quickly
- Can miss emergent attack combinations (cross-tree attacks)
- Construction requires attacker mindset — not all teams can build accurate trees

## Mitigation

Build attack trees collaboratively with security engineers and developers. Review when major system components change. Focus on the leaves (atomic steps) when selecting mitigations.
