---
id: homomorphic-encryption
title: "Homomorphic Encryption"
domain: security
sub-domain: "architecture patterns"
applies-to: []  # TODO: backend | frontend | infrastructure | cloud | mobile | data | ml | all
complexity: ""  # TODO: low | medium | high
maturity: ""    # TODO: established | emerging | theoretical
theorist: ""    # TODO: primary originator or "multiple"
year: null      # TODO: year concept was formally named/published
related: []     # TODO: IDs of related entries
tags: []        # TODO: free-form tags
---

## Definition

A form of encryption that allows computation on ciphertext. The result, when decrypted, matches the result of performing the same operations on the plaintext. The computing party never sees the plaintext.

## Example

A healthcare analytics company wants a hospital to compute average patient age without revealing individual ages. The hospital encrypts each age under the Paillier scheme (additively homomorphic). The company sums the ciphertexts, returns the encrypted sum. The hospital decrypts and divides by count — the analytics company never saw individual ages.

Production-ready libraries: Microsoft SEAL, OpenFHE, TFHE-rs. CKKS scheme is used for approximate ML inference (privacy-preserving neural network evaluation).

## Strengths

- Computation on sensitive data without data exposure — cloud providers process data they cannot read
- Enables outsourced computation (ML inference, analytics) without centralising plaintext
- Strong cryptographic guarantees — not just organisational policy

## Weaknesses

- 1,000x–1,000,000x computational overhead compared to plaintext operations
- Only Fully Homomorphic Encryption (FHE) supports arbitrary computation — most practical schemes are limited
- Bootstrapping (refreshing the ciphertext) is the main performance bottleneck in FHE

## Mitigation

Use partially homomorphic encryption (Paillier for sums, ElGamal for products) where the computation can be decomposed into supported operations. Use FHE only where the privacy requirement justifies the performance cost. Monitor the field — TFHE and CKKS performance is improving rapidly (2-3x per year).
