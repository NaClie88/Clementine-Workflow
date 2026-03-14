---
id: principle-of-least-authority
title: "Principle of Least Authority (POLA)"
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

A stronger formulation of least privilege applied to capability-based security. Actors receive only the capabilities they need — and not capabilities that grant the ability to acquire more capabilities.

## Example

seL4 microkernel: a process receives an unforgeable capability object to perform specific operations on a specific resource. It cannot access anything it doesn't hold a capability for, and it cannot elevate its own authority by requesting new capabilities.

## Strengths

- Prevents confused deputy attacks (a trusted program abused by an untrusted caller)
- Capabilities are unforgeable tokens — ambient authority exploitation is impossible by design
- Fine-grained, object-level authority control

## Weaknesses

- Capability systems require OS or language runtime support — hard to retrofit onto ACL-based systems
- Managing capability objects at scale adds complexity
- Most production systems use ACLs and RBAC, not capability systems

## Mitigation

Apply POLA principles within conventional systems via fine-grained IAM roles, OAuth scopes, and API key scoping. Avoid ambient authority patterns (global admin roles, wildcard permissions).
