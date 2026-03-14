---
id: event-driven-architecture
title: "Event-Driven Architecture (EDA)"
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

Components communicate by producing and consuming events rather than direct calls. Decouples producers from consumers; enables asynchronous workflows.

## Example

An order placed event is published to Kafka. Three consumers react independently: `InventoryService` reserves stock, `EmailService` sends a confirmation, `AnalyticsService` records the sale. None know each other exist. Adding a new consumer requires no change to the producer.

## Strengths

- Loose coupling — producers and consumers evolve independently
- Natural audit trail — the event log is a complete record of what happened
- Scales individual consumers independently

## Weaknesses

- Eventual consistency complicates error handling and UI feedback
- Event ordering guarantees are hard to achieve across partitions
- Debugging requires distributed tracing across multiple services

## Mitigation

Use correlation IDs; implement dead-letter queues; design all consumers to be idempotent (at-least-once delivery is the default). Invest in distributed tracing (OpenTelemetry) before going to production.
