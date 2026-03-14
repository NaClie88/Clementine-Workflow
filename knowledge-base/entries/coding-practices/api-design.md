---
id: api-design
title: "API Design"
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
