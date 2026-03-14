---
id: event-sourcing
title: "Event Sourcing"
domain: architecture
sub-domain: "architectural philosophy"
applies-to: []  # TODO: backend | frontend | infrastructure | cloud | mobile | data | ml | all
complexity: ""  # TODO: low | medium | high
maturity: ""    # TODO: established | emerging | theoretical
theorist: ""    # TODO: primary originator or "multiple"
year: null      # TODO: year concept was formally named/published
related: []     # TODO: IDs of related entries
tags: []        # TODO: free-form tags
---

## Definition

State is derived by replaying a sequence of immutable events rather than stored as a current-state snapshot.

## Example

A bank account balance is never stored directly — it is calculated by replaying `MoneyDeposited` and `MoneyWithdrawn` events. Any past balance at any point in time is reconstructable. Snapshots are taken periodically to avoid replaying the full history.

## Strengths

- Complete audit trail — every state change has a cause
- Temporal queries: reconstruct the state at any point in time
- Events are the integration contract between bounded contexts

## Weaknesses

- Event replay at scale requires periodic snapshots
- Schema evolution of past events is painful — you cannot change history
- Debugging requires event log tooling that most teams don't have initially

## Mitigation

Snapshot aggregate state every N events; version event schemas and implement upcasters that transform old events to the current schema on read.
