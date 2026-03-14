---
id: observability
title: "Observability"
domain: methodology
sub-domain: "operational philosophy"
applies-to: [backend, infrastructure, cloud]
complexity: medium
maturity: established
theorist: multiple
year: 2015
related: [site-reliability-engineering, logging-observability, chaos-engineering, devops]
tags: [logs, metrics, traces, opentelemetry, three-pillars, cardinality]
---

## Definition

A system property: you can understand its internal state from its external outputs. Three pillars: logs, metrics, traces.

## Example

A distributed order service emits OpenTelemetry traces. A Grafana dashboard correlates a P99 latency spike to a specific Postgres query via trace IDs — without needing to add new instrumentation and redeploy.

## Strengths

- Debug novel failures without predicting them in advance
- Correlate logs, metrics, and traces across services to find root cause
- Enables SLO measurement and alerting

## Weaknesses

- High-cardinality metrics are expensive at scale (Prometheus cardinality limits)
- Instrumentation adds code overhead and can be neglected
- Tool sprawl (Prometheus, Jaeger, ELK, Datadog) is common without a platform strategy

## Mitigation

Standardise on OpenTelemetry for instrumentation — it is vendor-neutral and future-proof. Use sampling to control trace volume and cost. Define SLIs before building dashboards so metrics are purposeful.
