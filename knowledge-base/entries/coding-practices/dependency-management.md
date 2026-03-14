---
id: dependency-management
title: "Dependency Management"
domain: coding-practices
sub-domain: "coding discipline"
applies-to: [all]
complexity: medium
maturity: established
theorist: multiple
year: 2004
related: [supply-chain-security, version-control-discipline]
tags: [semver, package-managers, transitive-dependencies, vulnerabilities, lock-files]
---

## Definition

Every dependency is a liability as well as an asset. Audit continuously; pin versions; maintain a Software Bill of Materials.

## Example

`pip-audit` in CI flags `requests==2.28.0` with a known CVE. The build fails until the dependency is updated or the vulnerability is explicitly accepted with documented justification.

## Strengths

- Automated vulnerability detection catches known CVEs before production
- Pinned versions produce reproducible builds
- SBOM provides supply chain visibility for security audits

## Weaknesses

- Pinning creates upgrade debt — version drift accumulates over time
- Transitive dependency conflicts are hard to resolve
- Vendoring large dependency trees inflates repository size

## Mitigation

Use Dependabot or Renovate for automated dependency PRs. Pin direct dependencies; track transitive dependencies via lockfiles. Use hash pinning for security-critical packages.
