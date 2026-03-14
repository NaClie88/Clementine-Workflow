---
id: attack-surface-minimisation
title: "Attack Surface Minimisation"
domain: security
sub-domain: "foundational principles"
applies-to: [all]
complexity: medium
maturity: established
theorist: multiple
year: 2000
related: [least-privilege, defence-in-depth, secure-by-default]
tags: [hardening, reduce-exposure, attack-vectors, default-config]
---

## Definition

The less code that runs, the fewer services that are exposed, and the fewer features that are enabled, the smaller the attack surface.

## Example

A production Docker container: `FROM python:3.11-slim` (not `python:3.11`), no SSH daemon, no package manager in the image, non-root user (`USER appuser`), read-only filesystem (`--read-only`), single process. Every removed component eliminates a potential attack vector.

## Strengths

- Fewer components = fewer vulnerabilities to patch and exploit
- Smaller images are faster to pull, scan, and deploy
- Simpler systems are easier to audit

## Weaknesses

- Minimisation can conflict with operational needs — minimal containers are hard to debug
- Over-minimisation removes legitimate monitoring and logging capabilities
- Teams resist minimisation because it makes development harder

## Mitigation

Use distroless or minimal base images in production; maintain a separate debug image with tooling for incident response. Treat every installed package as a potential liability requiring justification.
