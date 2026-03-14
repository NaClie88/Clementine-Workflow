---
id: trusted-execution-environments
title: "Trusted Execution Environments (TEE) / Secure Enclaves"
domain: security
sub-domain: "architecture patterns"
applies-to: [infrastructure, cloud, mobile]
complexity: high
maturity: established
theorist: multiple
year: 2003
related: [hardware-security-modules, cryptographic-hygiene, secure-by-default]
tags: [tee, sgx, trustzone, secure-enclave, hardware-isolation, confidential-computing]
---

## Definition

Hardware-isolated execution environments in which code and data are protected from the host OS, hypervisor, and other processes — including the cloud provider.

## Example

Intel SGX: application code runs in an encrypted memory region (enclave). The OS and hypervisor cannot read or modify enclave memory. Remote attestation allows a client to cryptographically verify that a specific binary hash is running inside a genuine SGX enclave on genuine Intel hardware before sending sensitive data to it.

```
# TEE remote attestation flow (Intel SGX):

# 1. Client sends:    "prove you are running code X in a genuine enclave"
# 2. Enclave generates: attestation report containing the code measurement (hash)
# 3. SGX hardware signs: the report with Intel's provisioning key
# 4. Client verifies:  signature chain → Intel Attestation Service → code hash
# 5. Client confirms:  correct binary AND genuine SGX hardware
# 6. Client sends:     data encrypted to the enclave's public key
#                      Only the enclave can decrypt it — host OS cannot
```

Used in production: Azure Confidential Computing, AWS Nitro Enclaves, Apple Secure Enclave (biometric keys + Apple Pay), Signal's Private Contact Discovery.

## Strengths

- Protects data even from privileged attackers (root, hypervisor, cloud provider)
- Hardware root of trust provides stronger guarantees than software isolation
- Enables confidential ML inference and privacy-preserving analytics in untrusted cloud environments

## Weaknesses

- Side-channel attacks (Spectre, Meltdown, SGAxe, LVI) have repeatedly broken SGX isolation
- Trusted computing base still includes the CPU manufacturer — trust is moved, not eliminated
- Remote attestation infrastructure is centralised (Intel Attestation Service) — a dependency and potential target

## Mitigation

Keep enclave code minimal (small Trusted Computing Base reduces attack surface). Apply Intel microcode updates promptly — SGX vulnerabilities are patched via microcode. Combine TEE with other controls (E2EE to the enclave boundary, minimal data retention in the enclave).
