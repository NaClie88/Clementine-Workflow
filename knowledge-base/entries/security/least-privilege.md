---
id: least-privilege
title: "Least Privilege"
domain: security
sub-domain: "foundational principles"
applies-to: []  # TODO: backend | frontend | infrastructure | cloud | mobile | data | ml | all
complexity: ""  # TODO: low | medium | high
maturity: ""    # TODO: established | emerging | theoretical
theorist: ""    # TODO: primary originator or "multiple"
year: null      # TODO: year concept was formally named/published
related: []     # TODO: IDs of related entries
tags: []        # TODO: free-form tags
---

## Definition

Every user, process, and system component operates with the minimum permissions required to perform its documented function — nothing more.

## Example

An AWS Lambda function that reads from one S3 bucket has an IAM role with exactly `s3:GetObject` on `arn:aws:s3:::my-bucket/*` — no `s3:*`, no other services. A compromised function cannot exfiltrate data from other buckets, write to any bucket, or access any other AWS service.

## Strengths

- Limits blast radius of a compromised component
- Reduces insider threat impact — over-permissioned insiders can do more damage
- Simplifies audit — the permission set is small and easy to verify

## Weaknesses

- Operationally burdensome — teams grant broad permissions to avoid the friction of debugging access denials
- Permission creep: requirements change and permissions are added but never removed
- Least-privilege enforcement at scale (thousands of IAM roles) requires tooling

## Mitigation

Use infrastructure-as-code for all IAM roles (permissions are reviewable in PRs). Audit for unused permissions quarterly with tools like AWS IAM Access Analyzer. Treat broad wildcards (`s3:*`, `*:*`) as requiring written justification.
