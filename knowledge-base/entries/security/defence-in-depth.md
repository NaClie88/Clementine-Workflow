---
id: defence-in-depth
title: "Defence in Depth"
domain: security
sub-domain: "foundational principles"
applies-to: [all]
complexity: medium
maturity: established
theorist: multiple
year: 1990
related: [least-privilege, zero-trust-architecture, cia-triad, attack-surface-minimisation]
tags: [layered-security, controls, redundancy, multiple-barriers]
---

## Definition

No single security control is sufficient. Layer multiple independent controls so that an attacker must defeat every layer.

## Example

A corporate network: perimeter firewall + network IDS + WAF + host-based IDS + endpoint detection + SIEM. An attacker who bypasses the perimeter firewall still faces network detection, WAF rules, and endpoint protection — each operating independently.

## Strengths

- No single point of failure — one layer failing does not result in compromise
- Layered controls catch different attack vectors
- Attacker cost increases with each layer

## Weaknesses

- Complexity overhead — more tools, more alerts, more maintenance
- False sense of security if layers are not independently effective
- Alert fatigue from multiple tools producing overlapping noise

## Mitigation

Ensure each layer is independently effective and monitors independently. Avoid layers that all depend on the same underlying assumption. Treat alert fatigue as a signal that layers are poorly tuned.
