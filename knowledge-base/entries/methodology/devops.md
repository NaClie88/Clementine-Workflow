---
id: devops
title: "DevOps"
domain: methodology
sub-domain: "operational philosophy"
applies-to: [infrastructure, cloud, backend]
complexity: medium
maturity: established
theorist: Patrick Debois
year: 2009
related: [devsecops, gitops, site-reliability-engineering, infrastructure-as-code, observability]
tags: [automation, collaboration, ci-cd, deployment, culture]
---

## Definition

Remove organisational barriers between development and operations. Shared ownership of the full lifecycle — build, deploy, monitor, respond.

## Example

A team where developers write runbooks, own on-call rotations, and deploy their own code via a self-service pipeline. No separate ops ticket queue — "you build it, you run it."

## Strengths

- Fast feedback loop from production to code
- Shared ownership eliminates the "throw it over the wall" failure mode
- Deployment frequency and mean time to recovery improve measurably (DORA metrics)

## Weaknesses

- Requires significant cultural change — often resisted by both dev and ops
- Small teams may lack operational depth for on-call
- On-call fatigue if reliability is poor

## Mitigation

Build reliability into the product before expanding on-call scope. Use error budgets to balance feature velocity against reliability investment. Invest in SLOs before on-call rotation.
