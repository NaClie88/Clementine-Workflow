---
id: immutable-infrastructure
title: "Immutable Infrastructure"
domain: architecture
sub-domain: "architectural philosophy"
applies-to: []  # TODO: backend | frontend | infrastructure | cloud | mobile | data | ml | all
complexity: ""  # TODO: low | medium | high
maturity: ""    # TODO: established | emerging | theoretical
theorist: ""    # TODO: primary originator or "multiple"
year: null      # TODO: year concept was formally named/published
related: []     # TODO: IDs of related entries
tags: []        # TODO: free-form tags
---

## Definition

Servers and environments are never modified in place — they are replaced by a new version built from a known-good image.

## Example

A Terraform + Packer pipeline bakes a new AMI for every release. The old EC2 instance is terminated; the new one is launched from the immutable image. No SSH, no configuration drift, no "works on my machine."

## Strengths

- Eliminates configuration drift — every instance is identical to every other
- Deployments are reproducible and auditable
- Rollback is launching the previous image

## Weaknesses

- Longer deployment cycles than in-place updates
- Requires mature CI/CD and image management
- Stateful services need external state stores — the stateless/stateful boundary must be explicit

## Mitigation

Separate stateful and stateless components by design. Use managed services (RDS, S3, ElastiCache) for state. Treat stateful components as exceptions that require explicit justification.
