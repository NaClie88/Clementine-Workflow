---
id: zero-knowledge-proof-architectures
title: "Zero-Knowledge Proof Architectures"
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

A cryptographic method by which one party proves knowledge of a value without revealing the value itself. The prover convinces the verifier the statement is true; the verifier learns nothing beyond that fact.

Two major production-ready variants:

**zk-SNARKs — Succinct Non-interactive ARguments of Knowledge**
Small proof size, fast verification, requires a one-time trusted setup ceremony.

## Example

Zcash shielded transactions — a user proves they hold a private key authorising ≥ X ZEC without revealing the key, balance, or counterparty. The proof is ~200 bytes; verification takes milliseconds.

```
# Conceptual ZKP for age verification (real use case: Polygon ID, WorldCoin):
# Prover knows:    birthdate = 1995-01-15  (private input / witness)
# Public statement: age >= 18 as of 2026-03-14
# ZKP circuit:    computes (today - birthdate) >= 18*365.25
# Verifier learns: True / False — and cryptographic proof of validity
#                  They learn NOTHING about the actual birthdate

# In production: circom circuit + snarkjs / bellman / halo2 proving library
```

**zk-STARKs — Scalable Transparent ARguments of Knowledge**
No trusted setup (uses public randomness). Post-quantum secure. Larger proofs than SNARKs.

## Example

StarkNet (Ethereum L2): validity proofs for batches of transactions use STARKs. Thousands of transactions are verified by a single on-chain proof. No trusted setup — the security assumptions are purely hash functions.

## Strengths

- Prove claims about private data without revealing the data itself
- SNARKs produce small proofs that are fast to verify on-chain
- STARKs require no trusted setup and are post-quantum resistant

## Weaknesses

- Proof generation is computationally expensive (minutes for complex circuits)
- SNARKs require a trusted setup ceremony — if compromised, forged proofs are undetectable
- Circuit design requires specialist expertise; bugs in circuits are security vulnerabilities

## Mitigation

Use audited circuit libraries (circomlib, arkworks standard library). For SNARKs, use universal or updatable setups (PLONK, Halo2 — no per-circuit trusted setup). Benchmark proving time early — it is the primary performance bottleneck.
