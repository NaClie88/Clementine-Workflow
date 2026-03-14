---
id: devsecops
title: "DevSecOps"
domain: methodology
sub-domain: "operational philosophy"
applies-to: []  # TODO: backend | frontend | infrastructure | cloud | mobile | data | ml | all
complexity: ""  # TODO: low | medium | high
maturity: ""    # TODO: established | emerging | theoretical
theorist: ""    # TODO: primary originator or "multiple"
year: null      # TODO: year concept was formally named/published
related: []     # TODO: IDs of related entries
tags: []        # TODO: free-form tags
---

## Definition

Embed security into the DevOps pipeline. Security is everyone's responsibility, not a gate at the end.

## Example

A CI pipeline that runs `trivy` for container vulnerability scanning, `gitleaks` for secret detection, `bandit` for Python static analysis, and OWASP ZAP for DAST — all before a PR can merge.

## Strengths

- Security defects caught before production
- Security becomes a shared team responsibility, not a separate team's gate
- Automated tools scale security review without scaling headcount

## Weaknesses

- Pipeline complexity increases — false positives cause alert fatigue
- Teams may treat automated checks as a compliance checkbox rather than engaging with findings
- Tool sprawl without integration creates noise

## Mitigation

Tune rules to reduce false positives before enforcing as blocking. Treat findings as first-class bugs. Review security tool output in retrospectives — not just in the moment of failure.
