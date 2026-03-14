---
id: cryptographic-hygiene
title: "Cryptographic Hygiene"
domain: security
sub-domain: "secure development"
applies-to: [backend, infrastructure]
complexity: high
maturity: established
theorist: multiple
year: 2000
related: [kerckhoffs-s-principle, secrets-management, end-to-end-encryption, hardware-security-modules]
tags: [tls, key-management, cipher-suite, algorithms, deprecation, post-quantum]
---

## Definition

Use established, peer-reviewed algorithms. Key management is usually harder than algorithm selection. Never implement cryptographic primitives from scratch.

## Example

A modern system uses: bcrypt (cost 12) for password hashing, TLS 1.3 for transit, AES-256-GCM for at-rest data, Ed25519 for signatures. Each algorithm is chosen from current NIST recommendations with a documented rotation plan.

## Strengths

- Established algorithms have peer-reviewed security proofs
- Documented rotation plans enable algorithm migration before deprecation (MD5, SHA-1, RSA-1024 are all now deprecated)
- High-level libraries (libsodium, Tink) make correct usage the easy path

## Weaknesses

- Key management is consistently under-resourced relative to algorithm selection
- Developers implement cryptographic protocols incorrectly even with good algorithms
- Algorithm deprecation cycles are long — legacy systems accumulate deprecated algorithms

## Mitigation

Use high-level cryptographic libraries that make correct usage the default (libsodium, Tink). Never implement cryptographic primitives directly. Review algorithm choices annually against current NIST recommendations (NIST SP 800-131A).
