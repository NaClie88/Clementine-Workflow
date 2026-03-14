---
id: owasp-top-10
title: "OWASP Top 10"
domain: security
sub-domain: "industry frameworks"
applies-to: []  # TODO: backend | frontend | infrastructure | cloud | mobile | data | ml | all
complexity: ""  # TODO: low | medium | high
maturity: ""    # TODO: established | emerging | theoretical
theorist: ""    # TODO: primary originator or "multiple"
year: null      # TODO: year concept was formally named/published
related: []     # TODO: IDs of related entries
tags: []        # TODO: free-form tags
---

## Definition

Annual list of the ten most critical web application security risks. Not a complete standard — a risk-awareness baseline.

## Example

A1 (Broken Access Control): a web app using sequential user IDs (`/users/123`, `/users/124`) with no ownership check allows any authenticated user to access any other user's profile. Fix: UUID-based IDs + object-level authorisation check on every request.

## Strengths

- Widely understood — engineers, PMs, and auditors share the vocabulary
- Vendor-neutral; each edition reflects current attack trends
- Good starting point for developer security training

## Weaknesses

- Only ten categories — not a complete security standard
- "OWASP Top 10 compliant" is not a meaningful security claim
- Descriptions are high-level — implementation guidance requires the Testing Guide

## Mitigation

Treat OWASP Top 10 as a minimum developer awareness checklist. Use OWASP ASVS for comprehensive security requirements. Use the OWASP Testing Guide for specific verification procedures.
