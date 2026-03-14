---
id: error-handling
title: "Error Handling"
domain: coding-practices
sub-domain: "coding discipline"
applies-to: [all]
complexity: medium
maturity: established
theorist: multiple
year: 1975
related: [fail-fast, defensive-programming, logging-observability]
tags: [exceptions, error-propagation, resilience, robustness, circuit-breaker]
---

## Definition

Errors should be caught at the right level, carry context, and never be swallowed silently. Catch the full range of exceptions the environment can produce.

## Example

A Docker canary script catches `(PermissionError, OSError)` not just `PermissionError` — Docker's `--read-only` flag raises `OSError (EROFS errno 30)`, not `PermissionError`. Catching only the subclass caused the canary to crash on the exact condition it was testing.

```python
try:
    with open("/readonly-path/test.txt", "w") as f:
        f.write("test")
    print("FAIL: write should have been blocked")
except (PermissionError, OSError) as e:
    print(f"PASS: write blocked as expected ({type(e).__name__}: {e})")
except Exception as e:
    print(f"ERROR: unexpected exception: {e}")
```

## Strengths

- System degrades predictably — every failure path is explicit
- Errors carry context — `type(e).__name__` and `e` identify the cause
- Recovery paths are documented and tested

## Weaknesses

- Over-catching (bare `except:`) hides bugs by catching exceptions that should propagate
- Under-catching crashes on valid conditions that a narrower exception clause didn't anticipate
- Swallowed exceptions produce silent failures that are discovered in production

## Mitigation

Catch base classes (`OSError`, `IOError`) unless the specific subclass has been verified in the target environment. Always log or re-raise in catch blocks — never pass silently.
