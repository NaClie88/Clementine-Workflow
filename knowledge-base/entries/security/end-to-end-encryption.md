---
id: end-to-end-encryption
title: "End-to-End Encryption (E2EE) Architecture"
domain: security
sub-domain: "architecture patterns"
applies-to: [backend, mobile]
complexity: high
maturity: established
theorist: "Whitfield Diffie, Martin Hellman; Trevor Perrin, Moxie Marlinspike"
year: 1976
related: [cryptographic-hygiene, federated-identity, hardware-security-modules, trustless-architecture]
tags: [e2ee, signal-protocol, forward-secrecy, double-ratchet, key-exchange, diffie-hellman]
---

## Definition

Messages are encrypted on the sender's device and decrypted only on the recipient's device. The service provider transmits ciphertext but can never access plaintext. Compromise of the server reveals nothing about message content.

## Example

Signal Protocol (used by Signal, WhatsApp E2EE, Matrix): Double Ratchet algorithm + X3DH key agreement. Each message uses a new symmetric key derived from a ratcheting chain — compromise of one message key does not compromise past or future messages (forward secrecy + break-in recovery).

```
# E2EE architecture layers:

# 1. Identity keys:     each device generates a long-term Ed25519 keypair
# 2. Key exchange:      X3DH (Extended Triple Diffie-Hellman) establishes
#                       a shared secret from identity + ephemeral keys
#                       Server sees only public keys; never derives the secret
# 3. Session keys:      Double Ratchet generates a new AES-256 key per message
# 4. Encryption:        AES-256-CBC + HMAC-SHA256 (or AES-GCM in newer versions)
# 5. Server's role:     routes encrypted blobs; holds no keys; sees no plaintext
# 6. Forward secrecy:   old message keys deleted after use; past messages
#                       remain secure even if current keys are compromised
```

## Strengths

- Server compromise does not expose message content — the server never had the keys
- Forward secrecy protects past messages even after a future key compromise
- Break-in recovery: new messages are secure after a key compromise without re-registering

## Weaknesses

- Key management UX is hard — device loss means message loss unless key backup is implemented
- Metadata (who talks to whom, when, message frequency) is typically not E2EE
- Key backup (for device loss recovery) introduces a new attack surface if not secured properly

## Mitigation

Implement sealed sender (Signal's technique) to protect metadata. Design secure key backup using a user-controlled PIN with rate-limited HSM (Signal's SVR approach). Clearly document what is and is not protected — metadata protection is a separate problem from content protection.
