---
id: test-driven-development
title: "Test-Driven Development (TDD)"
domain: methodology
sub-domain: "development methodology"
applies-to: [all]
complexity: medium
maturity: established
theorist: Kent Beck
year: 1999
related: [behaviour-driven-development, extreme-programming, refactoring, testing-taxonomy]
tags: [red-green-refactor, unit-testing, feedback, design]
---

## Definition

Write a failing test first, then write the minimum code to pass it, then refactor. Red → Green → Refactor.

## Example

Implementing fizzbuzz — test first, then minimum passing implementation, then clean up.

```python
# Red: write the failing test first
def test_fizzbuzz_fifteen():
    assert fizzbuzz(15) == "FizzBuzz"  # NameError: fizzbuzz not defined

# Green: minimum code to pass
def fizzbuzz(n):
    if n % 15 == 0: return "FizzBuzz"
    if n % 3 == 0: return "Fizz"
    if n % 5 == 0: return "Buzz"
    return str(n)

# Refactor: the test suite stays green throughout
```

## Strengths

- Tests drive design toward testable (loosely coupled) code
- Regression suite is a free byproduct of development
- Forces thinking about desired behaviour before implementation

## Weaknesses

- Slows initial development — significant discipline investment upfront
- Tests can be brittle if written against implementation rather than behaviour
- Difficult to apply to legacy code without significant refactoring first

## Mitigation

Write tests at the behaviour level (what the code does, not how). Use test doubles to isolate dependencies. Apply TDD to new code; invest in characterisation tests before refactoring legacy code.
