---
id: the-12-factor-app
title: "The 12-Factor App (Heroku)"
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

Twelve principles for building portable, scalable, cloud-native applications. Covers: codebase, dependencies, config, backing services, build/release/run, processes, port binding, concurrency, disposability, dev/prod parity, logs, admin processes.

## Example

A Docker-containerised Python service reads all config from environment variables (factor III), writes logs to stdout (factor XI), starts cleanly on SIGTERM (factor IX), and uses the same Postgres image in dev and prod (factor X — dev/prod parity).

## Strengths

- Portable across cloud providers and runtime environments
- Enables horizontal scaling without architectural changes
- Strong operational hygiene built in from the start

## Weaknesses

- Some factors (strict process statelesness) don't fit all problem domains
- Can over-constrain architecture for systems with legitimate local state requirements
- The list is incomplete — security, observability, and data management are under-addressed

## Mitigation

Treat as a cloud-native checklist, not a rigid ruleset. Document deliberate departures. Supplement with SRE practices for operational reliability.
