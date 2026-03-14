---
id: hardware-security-modules
title: "Hardware Security Modules (HSM)"
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

Dedicated cryptographic hardware devices that generate, store, and use cryptographic keys within tamper-resistant hardware. Keys never leave the HSM in plaintext; all cryptographic operations are performed inside the device.

## Example

A Certificate Authority uses a FIPS 140-2 Level 3 HSM to store its root CA private key. Signing a certificate requires the HSM. If the server is fully compromised — OS, application, all storage — the attacker cannot export the signing key. Physical tamper detection erases keys on intrusion.

Cloud HSMs: AWS CloudHSM, Azure Dedicated HSM, Google Cloud HSM. Managed key services with HSM backing: AWS KMS (FIPS 140-2 L2), Azure Key Vault Premium.

```
# HSM key hierarchy (best practice for cloud deployments):

# HSM holds:      Customer Master Key (CMK) — never exported
# CMK wraps:      Data Encryption Key (DEK) — generated fresh per resource
# DEK encrypts:   actual data at rest
#
# Attacker with DB access:  gets encrypted data + wrapped DEK — cannot decrypt
# Attacker with HSM access: gets CMK — but HSM requires physical access + PIN
# Envelope encryption means bulk data operations don't touch the HSM
```

## Strengths

- Keys are physically irremovable — even the HSM operator cannot export them
- FIPS 140-2/3 certification provides third-party assurance of tamper resistance
- Audit logging of all key operations — complete record of every sign, decrypt, and key generation

## Weaknesses

- Expensive — dedicated HSMs cost $10k–$50k+; cloud HSMs are cheaper but still costly
- Single point of failure unless clustered — requires HA architecture
- Key ceremony for root keys requires physical coordination — operationally complex

## Mitigation

Use HSM clustering for availability. Document key ceremony procedures before they are needed. Use HSM for key wrapping + software for bulk encryption (envelope encryption pattern) to avoid HSM becoming a throughput bottleneck.
