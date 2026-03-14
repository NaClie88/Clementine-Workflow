---
id: code-review
title: "Code Review"
domain: coding-practices
sub-domain: "coding discipline"
applies-to: [all]
complexity: low
maturity: established
theorist: Michael Fagan
year: 1976
related: [refactoring, version-control-discipline, testing-taxonomy]
tags: [peer-review, pull-request, quality, collaboration, inspection]
---

## Definition

Reviews catch defects, share knowledge, and enforce standards. Small, frequent PRs are reviewed more thoroughly than large infrequent ones.

## Example

A 200-line PR reviewed in 15 minutes catches a missing authorisation check. A 2000-line PR reviewed in the same time catches nothing because the reviewer can only skim.

## Strengths

- Knowledge sharing — the second reviewer understands the change
- Defect detection — a fresh set of eyes catches what the author missed
- Architectural consistency — the team's standards are applied uniformly

## Weaknesses

- Bottleneck when reviewers are scarce or PR queues are long
- Large PRs receive superficial reviews — social pressure to approve
- Blocking vs. non-blocking comments are often not distinguished

## Mitigation

Enforce PR size limits (200–400 lines is a reasonable upper bound). Explicitly mark blocking (correctness, security) vs. non-blocking (style, preference) comments. Review the design and logic, not just the style — linters handle style.
