---
id: design-by-contract
title: "Design by Contract (DbC)"
domain: architecture
sub-domain: "design principles"
applies-to: [all]
complexity: medium
maturity: established
theorist: Bertrand Meyer
year: 1986
related: [defensive-programming, fail-fast, testing-taxonomy]
tags: [preconditions, postconditions, invariants, eiffel, contracts]
---

## Definition

Functions specify preconditions, postconditions, and invariants as part of their contract. Callers are responsible for preconditions; functions guarantee postconditions if preconditions are met. (Bertrand Meyer / Eiffel.)

## Example

A `withdraw(amount)` method: precondition `amount > 0 and balance >= amount`, postcondition `balance == old_balance - amount`. Violations are detected at the contract boundary, not downstream.

```python
def withdraw(self, amount: float) -> None:
    assert amount > 0, "amount must be positive"
    assert self.balance >= amount, "insufficient funds"
    old_balance = self.balance
    self.balance -= amount
    assert self.balance == old_balance - amount  # postcondition
```

## Strengths

- Self-documenting specifications
- Catches violations at the point of breach, not downstream
- Forces explicit thinking about valid states

## Weaknesses

- Runtime assertions are typically disabled in production (`-O` flag in Python)
- Contracts must be maintained alongside code — drift is common
- Not all languages have first-class DbC support

## Mitigation

Use type systems and static analysis (mypy, TypeScript, Rust's type system) to enforce contracts at compile time where possible. Reserve runtime assertions for invariants that cannot be statically verified.
