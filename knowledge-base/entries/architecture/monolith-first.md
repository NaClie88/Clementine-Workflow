---
id: monolith-first
title: "Monolith-First (Martin Fowler)"
domain: architecture
sub-domain: "architectural philosophy"
applies-to: [backend, cloud]
complexity: medium
maturity: established
theorist: Martin Fowler
year: 2015
related: [microservices, domain-driven-design, strangler-fig-pattern]
tags: [architecture, incremental, pragmatic, migration]
---

## Definition

Start with a monolith; extract microservices when you understand the domain boundaries.

## Example

Shopify ran as a Rails monolith for years before extracting services — by then they understood which boundaries were stable. Companies that decomposed prematurely spent years unwinding wrong service boundaries.

## Strengths

- Faster initial development — no distributed systems overhead
- Easier debugging — a single process, a single log stream
- Domain boundaries reveal themselves through use; you can't design them correctly upfront

## Weaknesses

- Monoliths are hard to decompose if internal modules were never given clean boundaries
- Scaling specific components requires scaling the whole monolith
- Organisational scaling (many teams, many features) can create deployment bottlenecks

## Mitigation

Build the monolith with modular internal boundaries (packages, namespaces, internal interfaces) from day one. Treat them as pre-extracted services — the extraction is then mechanical.
