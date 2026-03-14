---
id: logging-observability
title: "Logging & Observability"
domain: coding-practices
sub-domain: "coding discipline"
applies-to: []  # TODO: backend | frontend | infrastructure | cloud | mobile | data | ml | all
complexity: ""  # TODO: low | medium | high
maturity: ""    # TODO: established | emerging | theoretical
theorist: ""    # TODO: primary originator or "multiple"
year: null      # TODO: year concept was formally named/published
related: []     # TODO: IDs of related entries
tags: []        # TODO: free-form tags
---

## Definition

Log structured events at the right level. Logs are a security artifact — their retention, access control, and integrity matter.

## Example

Structured JSON log: `{"timestamp": "2026-03-14T10:23Z", "level": "ERROR", "request_id": "abc-123", "event": "payment_failed", "amount": 99.99, "error": "gateway_timeout"}` — queryable, correlatable, sanitised of PII.

## Strengths

- Machine-queryable structured logs enable alerting and dashboards
- Correlation IDs enable distributed tracing across services
- Appropriate log levels prevent alert fatigue

## Weaknesses

- Over-logging adds noise and cost; under-logging makes incidents impossible to diagnose
- Sensitive data leaks into logs are extremely common and hard to detect
- Unstructured logs don't support automated analysis

## Mitigation

Log at the event level (what happened), not the code level (which function ran). Run a log sanitisation check in CI using pattern matching for common PII formats (email, phone, card numbers).
