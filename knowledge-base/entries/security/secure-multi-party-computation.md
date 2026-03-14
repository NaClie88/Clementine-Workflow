---
id: secure-multi-party-computation
title: "Secure Multi-Party Computation (MPC)"
domain: security
sub-domain: "architecture patterns"
applies-to: [data, backend]
complexity: high
maturity: emerging
theorist: Andrew C. Yao
year: 1982
related: [homomorphic-encryption, zero-knowledge-proof-architectures, privacy-enhancing-technologies]
tags: [mpc, distributed-trust, secret-sharing, garbled-circuits, federated-learning]
---

## Definition

A cryptographic protocol enabling multiple parties to jointly compute a function over their private inputs without any party revealing its inputs to the others. Output is correct; no party learns more than the output and their own input.

## Example

Salary benchmark: 100 employees want to know the average salary without revealing individual salaries. With Shamir's Secret Sharing: each employee secret-shares their salary with a set of computation nodes. Nodes compute the sum on shares (no single node sees any full salary). Result is reconstructed and divided by 100.

In production: Fireblocks (MPC crypto custody — the private key never exists reconstructed in one place), Unbound Security (key management), PySyft and TF Federated for privacy-preserving ML.

```
# MPC key management (threshold signatures — real use in crypto custody):

# Traditional:  one private key → sign transaction
#               Key compromise = all funds lost

# MPC (2-of-3): key is split into 3 shares (Shamir's Secret Sharing)
#               Any 2 holders can collaborate to sign — no single point of failure
#               No single holder has the full key at any time
#               Attacker must compromise 2 of 3 independent parties simultaneously
```

## Strengths

- No trusted third party needed — the protocol itself enforces privacy
- Private key never reconstructed in one place (MPC wallets)
- Enables collaborative analytics on datasets no single party can see in full

## Weaknesses

- High communication overhead — multiple rounds between all parties
- Requires honest-majority assumption in many protocols — colluding parties can extract data
- Complex to implement correctly; many subtle correctness requirements

## Mitigation

Use audited MPC libraries (MOTION, MP-SPDZ, Threshold Signature Schemes from IETF). Define the adversarial model (semi-honest vs. malicious adversaries) before selecting a protocol — the security guarantees differ significantly.
