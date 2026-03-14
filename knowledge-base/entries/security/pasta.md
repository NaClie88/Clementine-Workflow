---
id: pasta
title: "PASTA — Process for Attack Simulation and Threat Analysis"
domain: security
sub-domain: "threat modelling"
applies-to: [all]
complexity: high
maturity: established
theorist: "Tony UcedaVélez, Marco Morana"
year: 2012
related: [stride, attack-trees, mitre-att-ck-framework]
tags: [risk-based, attack-simulation, business-context, threat-modelling, seven-stages]
---

## Definition

Risk-centric, seven-stage methodology connecting technical threats to business impact: define objectives → technical scope → decompose application → analyse threats → identify vulnerabilities → enumerate attacks → risk/impact analysis.

## Example

A payment system — Stage 1: data breach affects revenue and regulatory standing. Stage 7: SQL injection on the payment form is the highest-risk attack path given likelihood and business impact. Mitigations: parameterised queries, WAF, quarterly pen test.

## Strengths

- Business-aligned output — connects threats to impact in terms stakeholders understand
- Produces a risk register that can be prioritised and tracked
- Suitable for executive and regulatory communication

## Weaknesses

- Seven stages make it heavy for small projects or time-constrained teams
- Requires both business and technical expertise to complete
- Can produce comprehensive documentation that no one acts on

## Mitigation

Use PASTA for high-value systems with regulatory exposure or significant financial risk. Use STRIDE for component-level threat modelling. Right-size the methodology to the risk.
