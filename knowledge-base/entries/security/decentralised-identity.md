---
id: decentralised-identity
title: "Decentralised Identity (DIDs / Verifiable Credentials — W3C Standards)"
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

Identities controlled by the holder rather than an identity provider. Decentralised Identifiers (DIDs) are self-sovereign identifiers. Verifiable Credentials (VCs) are signed attestations issued by trusted parties and held by the subject.

## Example

A university issues a degree as a W3C Verifiable Credential signed with the university's DID. The graduate stores it in a digital wallet. An employer verifies the credential by resolving the university's DID document (from a blockchain or well-known URL) to find the signing key — without contacting the university.

```json
{
  "@context": ["https://www.w3.org/2018/credentials/v1"],
  "type": ["VerifiableCredential", "UniversityDegreeCredential"],
  "issuer": "did:web:mit.edu",
  "credentialSubject": {
    "id": "did:key:zABC123...",
    "degree": { "type": "BachelorOfScience", "name": "Computer Science" }
  },
  "proof": {
    "type": "Ed25519Signature2020",
    "verificationMethod": "did:web:mit.edu#key-1",
    "jws": "eyJ..."
  }
}
```

Selective disclosure: BBS+ signatures allow the holder to prove specific attributes (e.g., "degree type = BSc") without revealing others (e.g., graduation date, GPA).

## Strengths

- User controls their identity data — no IdP as gatekeeper
- Selective disclosure: prove one attribute without revealing the full credential
- Eliminates the centralised IdP as a single point of failure and surveillance

## Weaknesses

- DID ecosystem is fragmented — 30+ DID methods with varying security properties
- Key recovery for lost wallets is an unsolved UX problem
- Credential revocation requires coordination — no universal revocation mechanism

## Mitigation

Use well-supported DID methods (did:web for organisational identity, did:ion for anchored identity). Implement BBS+ signatures for selective disclosure use cases. Build key recovery (social recovery, guardian-based recovery) into the wallet before deployment. Use StatusList2021 for scalable credential revocation.
