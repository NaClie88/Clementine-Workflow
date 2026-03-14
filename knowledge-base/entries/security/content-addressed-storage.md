---
id: content-addressed-storage
title: "Content-Addressed Storage (CAS)"
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

A storage system where content is addressed by its cryptographic hash. The same content always has the same address; different content always has a different address. The hash is the integrity guarantee.

## Example

Git: every object (blob, tree, commit) is addressed by its SHA-256 hash. `git clone` verifies the integrity of every object in history — a tampered commit produces a different hash, breaking the chain. IPFS: a file is hashed (SHA-256 → CIDv1) and distributed across nodes. Requesting `ipfs://QmHash` retrieves the file from any node that has it; the hash verifies integrity regardless of source.

```
# CAS integrity guarantee (how git uses it):

# File content → SHA-256 hash → content address
echo "Hello, world" | git hash-object --stdin
# → 8ab686eafeb1f44702738c8b0f24f2567c36da6d

# Tampering with the file changes the hash → the reference is broken
# This makes git history tamper-evident:
# commit A → (tree, parent B, author, message) → SHA-256 → commit A's hash
# Change anything → different hash → all downstream commits are invalidated
```

## Strengths

- Built-in integrity verification — the address is the integrity proof
- Automatic deduplication — identical content has one address
- Immutable content — the hash identifies exactly one version of the content forever

## Weaknesses

- Content is immutable — updating requires a new hash and a mutable pointer layer (IPNS, git refs)
- Garbage collection of unreferenced content requires coordination (objects no one points to)
- Content discovery requires out-of-band address sharing — CAS is not a search system

## Mitigation

Use a mutable naming layer (IPNS for IPFS, DNS TXT records, git tags) over CAS for user-facing addresses. Implement GC policies with retention windows. Pin critical content to prevent accidental removal.
