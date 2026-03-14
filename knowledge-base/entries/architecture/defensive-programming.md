---
id: defensive-programming
title: "Defensive Programming"
domain: architecture
sub-domain: "design principles"
applies-to: []  # TODO: backend | frontend | infrastructure | cloud | mobile | data | ml | all
complexity: ""  # TODO: low | medium | high
maturity: ""    # TODO: established | emerging | theoretical
theorist: ""    # TODO: primary originator or "multiple"
year: null      # TODO: year concept was formally named/published
related: []     # TODO: IDs of related entries
tags: []        # TODO: free-form tags
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
