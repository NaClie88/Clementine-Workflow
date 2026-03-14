---
id: reactive-systems
title: "Reactive Systems (Reactive Manifesto)"
domain: architecture
sub-domain: "architectural philosophy"
applies-to: [backend, cloud]
complexity: high
maturity: established
theorist: "Jonas Bonér, Dave Farley, Roland Kuhn, Martin Thompson"
year: 2013
related: [event-driven-architecture, microservices, observability]
tags: [reactive, resilience, elasticity, message-driven, backpressure]
---

## Definition

Systems should be Responsive, Resilient, Elastic, and Message-Driven.

## Example

Erlang/OTP (used by WhatsApp, RabbitMQ) and Elixir/Phoenix (Discord): actor-based processes communicate by message; failures are isolated per actor; supervisors restart failed actors automatically; the system degrades gracefully under load rather than collapsing.

## Strengths

- Natural resilience — failure isolation prevents cascading
- Back-pressure prevents overload from propagating up the call chain
- Scales horizontally with load

## Weaknesses

- Steep learning curve — actor model reasoning is different from synchronous programming
- Message-driven debugging is harder than synchronous stack traces
- Eventual consistency is the default, which complicates some business logic

## Mitigation

Apply reactive principles at the service boundary level first (message queues between services). Introduce actor models within a service only when concurrency requirements justify the complexity.
