---
id: defensive-programming
title: "Defensive Programming"
domain: architecture
sub-domain: "design principles"
applies-to: [all]
complexity: medium
maturity: established
theorist: multiple
year: 1976
related: [fail-fast, design-by-contract, error-handling, input-validation-output-encoding]
tags: [robustness, input-validation, error-handling, assertions]
---

## Definition

Expect unexpected inputs and failure modes. Validate inputs aggressively, handle all exception paths, assume the caller will misuse the interface.

## Example

A file parser that validates the header magic bytes, handles truncated files, and rejects malformed records with specific error messages rather than crashing on the first bad byte.

## Strengths

- Robust against unexpected inputs
- Easier to diagnose failures — errors carry context
- Reduces security vulnerabilities from unexpected input handling

## Weaknesses

- Excessive defensiveness creates verbose, hard-to-read code
- Can hide bugs by "handling" conditions that should have been prevented by the caller
- Defensive code inside a trusted module adds noise

## Mitigation

Be defensive at trust boundaries (user input, external APIs, file I/O, network). Trust internal code you control. Distinguish boundary validation from internal defensiveness.
