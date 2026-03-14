---
id: input-validation-output-encoding
title: "Input Validation & Output Encoding"
domain: security
sub-domain: "secure development"
applies-to: []  # TODO: backend | frontend | infrastructure | cloud | mobile | data | ml | all
complexity: ""  # TODO: low | medium | high
maturity: ""    # TODO: established | emerging | theoretical
theorist: ""    # TODO: primary originator or "multiple"
year: null      # TODO: year concept was formally named/published
related: []     # TODO: IDs of related entries
tags: []        # TODO: free-form tags
---

## Definition

Validate all input at every trust boundary. Encode all output for the context in which it will be rendered. SQL injection and XSS are both failures of this principle.

## Example

SQL injection via string interpolation vs. parameterised query:

```python
# VULNERABLE: string interpolation
cursor.execute(f"SELECT * FROM users WHERE email = '{email}'")
# Attacker input: ' OR '1'='1 — returns all users

# SAFE: parameterised query
cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
# Input is always treated as data, never as SQL
```

## Strengths

- Prevents the most prevalent web vulnerabilities (SQLi, XSS, command injection)
- Parameterisation is simple and reliable — no need to reason about escaping
- Validates at the boundary — errors surface immediately with context

## Weaknesses

- Developers must remember to use parameterised queries every time — one missed instance is sufficient
- Context-specific output encoding (HTML vs. JavaScript vs. SQL vs. shell) requires knowledge of each context
- Sanitisation (trying to clean up bad input) is error-prone — rejection is safer

## Mitigation

Use ORMs and templating engines that parameterise by default. Add SAST rules that flag string interpolation in query and shell contexts. Reject invalid input rather than sanitising it.
