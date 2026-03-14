---
id: site-reliability-engineering
title: "Site Reliability Engineering (SRE — Google)"
domain: methodology
sub-domain: "operational philosophy"
applies-to: [infrastructure, cloud, backend]
complexity: high
maturity: established
theorist: Ben Treynor Sloss
year: 2003
related: [devops, observability, chaos-engineering, incident-response]
tags: [slo, sla, error-budget, toil, google, on-call]
---

## Definition

Apply software engineering to operations. Key concepts: SLOs, error budgets, toil elimination, blameless post-mortems, gradual rollouts.

## Example

Gmail's SRE team sets a 99.9% monthly uptime SLO. The error budget (0.1% = ~43 minutes/month) is tracked in real time. When the error budget is exhausted, all feature work pauses until reliability is restored.

## Strengths

- Error budget creates a quantitative, non-political conversation between product and engineering
- Toil elimination frees engineers for high-value work
- DORA metrics provide an objective measure of DevOps capability

## Weaknesses

- SLO definition is hard to get right the first time
- Error budget model requires organisational buy-in — without it, the budget is ignored
- Toil is subjective — what counts as toil vs. necessary manual work requires ongoing negotiation

## Mitigation

Start with SLIs that users actually experience (latency, error rate). Revisit SLOs quarterly. Use the error budget as a conversation starter, not a punitive metric.
