---
id: infrastructure-as-code
title: "Infrastructure as Code (IaC)"
domain: methodology
sub-domain: "operational philosophy"
applies-to: [infrastructure, cloud]
complexity: medium
maturity: established
theorist: multiple
year: 2006
related: [gitops, immutable-infrastructure, devops, the-12-factor-app]
tags: [terraform, ansible, pulumi, reproducible, idempotent, drift]
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
