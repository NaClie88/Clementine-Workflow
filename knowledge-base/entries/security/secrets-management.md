---
id: secrets-management
title: "Secrets Management"
domain: security
sub-domain: "secure development"
applies-to: [backend, infrastructure, cloud]
complexity: medium
maturity: established
theorist: multiple
year: 2010
related: [cryptographic-hygiene, hardware-security-modules, least-privilege]
tags: [vault, environment-variables, key-rotation, secrets-scanning, hashicorp]
---

## Definition

Secrets must never appear in version control under any circumstances. Rotation must not require code changes.

## Example

A GitHub Action uses `${{ secrets.DATABASE_URL }}` — the secret is stored in GitHub Secrets, injected at runtime, never appears in logs or the repository. Rotation: update the secret in the GitHub UI; all future runs use the new value with no code change required.

## Strengths

- Secrets never touch version control — the most common secret exposure vector
- Rotation doesn't require code changes — enables rotation without deployment
- Access is auditable — GitHub Secrets logs who accessed what and when

## Weaknesses

- Secret sprawl: the same secret in CI, Kubernetes Secrets, .env files, and a secrets manager simultaneously
- Rotation discipline is hard to enforce operationally — stale secrets accumulate
- No single tool works across all environments (cloud, Kubernetes, CI, local dev)

## Mitigation

Designate one authoritative secrets manager per environment (Vault, AWS Secrets Manager). Audit all other secret stores for consolidation. Automate rotation using the secrets manager's rotation feature where the downstream service supports it.
