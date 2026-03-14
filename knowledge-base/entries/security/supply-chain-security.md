---
id: supply-chain-security
title: "Supply Chain Security"
domain: security
sub-domain: "secure development"
applies-to: [all]
complexity: high
maturity: emerging
theorist: multiple
year: 2020
related: [dependency-management, devsecops, cryptographic-hygiene]
tags: [sbom, software-bill-of-materials, provenance, slsa, sigstore, solarwinds]
---

## Definition

Every dependency, build tool, and CI component is a potential attack vector. Verify provenance; generate SBOMs; sign artifacts.

## Example

The SolarWinds attack (2020): malicious code was injected into the Orion build pipeline. 18,000 organisations installed the backdoored update. SLSA Level 3 would have required signed, reproducible builds with a tamper-evident build log — making the injection detectable post-hoc.

## Strengths

- Addresses a critical and often-overlooked attack vector
- SBOM provides visibility into the full dependency graph for incident response
- Signed artifacts and reproducible builds provide provenance guarantees

## Weaknesses

- SLSA adoption is early — most organisations are at Level 0
- SBOMs are useful only if they are acted upon — generating one is insufficient
- Even fully verified, signed builds can contain vulnerable dependencies

## Mitigation

Pin dependency versions with hash verification (`pip-compile --generate-hashes`). Sign all build artifacts. Generate and publish an SBOM with every release. Subscribe to OSV and NVD for automated CVE alerting against the SBOM.
