---
id: differential-privacy
title: "Differential Privacy"
domain: privacy
sub-domain: "technical approach"
applies-to: [data, ml]
complexity: high
maturity: established
theorist: "Cynthia Dwork, Frank McSherry, Kobbi Nissim, Adam Smith"
year: 2006
related: [privacy-enhancing-technologies, anonymisation-vs-pseudonymisation, data-minimisation]
tags: [mathematical-privacy, noise-addition, epsilon, analytics, apple-google]
---

## Definition

A mathematical framework for releasing aggregate statistics while providing provable guarantees that no individual's data can be inferred. Calibrated noise is added to outputs.

## Example

Apple's iOS keyboard telemetry: emoji usage statistics are collected with differential privacy. Laplace noise is added to each device's data. The aggregate statistic is accurate; individual records are mathematically deniable. Apple publishes ε (epsilon) values of 1–8 depending on the use case — lower ε = stronger privacy but less accurate statistics.

```
# Conceptual differential privacy mechanism (Laplace):
true_count = count_users_using_emoji("😀")
noise = laplace_noise(sensitivity=1, epsilon=1.0)
reported_count = true_count + noise
# Individual contribution is plausibly deniable; population trend is preserved
```

## Strengths

- Mathematically provable privacy guarantees — not just engineering best-effort
- Enables population statistics without individual exposure
- Composable — multiple DP queries have a total privacy budget

## Weaknesses

- ε parameter selection is difficult and context-dependent — no universal "good" value
- Adds noise that reduces accuracy — especially for small populations
- Hard to explain to non-specialists; "epsilon" is not intuitive

## Mitigation

Use established libraries (Apple's DP library, Google's DP library, OpenDP) rather than implementing from scratch. Consult a privacy engineer for ε selection. Publish the ε value alongside statistics for auditability.
