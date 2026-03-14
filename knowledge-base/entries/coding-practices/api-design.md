---
id: api-design
title: "API Design"
domain: coding-practices
sub-domain: "coding discipline"
applies-to: [backend, frontend]
complexity: high
maturity: established
theorist: Roy Fielding
year: 2000
related: [idempotency, principle-of-least-astonishment, separation-of-concerns, versioning]
tags: [rest, graphql, grpc, versioning, contracts, openapi]
---

## Definition

APIs are contracts. Once published, breaking changes are expensive. Design for the consumer, not the implementer.

## Example

REST: `GET /api/v1/orders/123` returns an order; `POST /api/v1/orders` creates one; `PATCH /api/v1/orders/123` updates it. The verb is in the HTTP method, not the URL. Version is in the path from day one.

## Strengths

- Well-designed APIs are self-documenting — the URL and method convey intent
- Versioning from day one enables evolution without breaking clients
- Standard conventions reduce integration friction

## Weaknesses

- API contracts are hard to change once published — consumers accumulate
- REST has no formal schema without OpenAPI; GraphQL has schema but complex security surface
- Over/under-fetching are common pain points in REST

## Mitigation

Version from day one (`/v1/`). Use OpenAPI to generate documentation and client SDKs. Design the API from the consumer's perspective — what does the client need, not what is easy to implement.
