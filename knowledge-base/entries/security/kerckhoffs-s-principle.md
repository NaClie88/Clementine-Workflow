---
id: kerckhoffs-s-principle
title: "Kerckhoffs's Principle (1883)"
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

A cryptosystem should be secure even if everything about the system, except the key, is public knowledge.

## Example

AES is the global encryption standard with a fully published algorithm, reference implementations, and academic analysis. Security rests entirely on the key. A proprietary scheme whose security depends on the algorithm being secret — once the algorithm leaks (and it will), all historical data is compromised.

## Strengths

- Enables public peer review of cryptographic systems — the only meaningful form of cryptographic validation
- Forces key management to be taken seriously as the actual security mechanism
- Prevents investment in "security through obscurity" that provides false confidence

## Weaknesses

- Widely understood but routinely violated in practice — proprietary crypto remains common
- Applying it to non-cryptographic systems requires interpretation
- Some systems legitimately use obscurity as one layer of many (security through obscurity is ineffective alone, not always harmful as one layer)

## Mitigation

Never design security controls that depend on implementation secrecy as the primary mechanism. Assume all implementation details will eventually be public. Use established, peer-reviewed algorithms; never roll your own crypto.
