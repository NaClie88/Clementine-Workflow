---
id: infrastructure-as-code
title: "Infrastructure as Code (IaC)"
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

Manage and provision infrastructure through machine-readable configuration files rather than manual processes.

## Example

A Terraform module provisions a VPC, subnets, security groups, and an RDS instance. The same module parameterised differently deploys identical infrastructure to dev, staging, and prod. `terraform destroy` cleanly removes everything.

## Strengths

- Reproducible environments — "works in staging, broken in prod" is eliminated
- Infrastructure changes are reviewable in PRs
- Disaster recovery is `terraform apply`

## Weaknesses

- Terraform state management is fragile — concurrent applies corrupt state
- Drift between declared and real state (manual changes) is hard to detect and reconcile
- Learning curve: HCL, state management, provider APIs

## Mitigation

Use remote state with locking (S3 + DynamoDB or Terraform Cloud). Run `terraform plan` in CI before every `apply`. Forbid manual changes to managed infrastructure — route all changes through code.
