---
id: blameless-post-mortems
title: "Blameless Post-Mortems"
domain: methodology
sub-domain: "operational philosophy"
applies-to: [all]
complexity: low
maturity: established
theorist: John Allspaw
year: 2012
related: [site-reliability-engineering, incident-response, devops, observability]
tags: [incident-review, psychological-safety, learning, culture, five-whys]
---

## Definition

When incidents occur, focus on systemic causes rather than individual fault. The goal is to improve the system, not to punish people.

## Example

Google's post-mortem template: timeline, root cause, contributing factors, action items. Individual names are absent from the root cause section — the question is "what failed?" not "who failed?"

## Strengths

- Honest incident analysis — people share what really happened rather than self-protecting
- Systemic causes are identified and addressed rather than symptoms
- Culture of learning rather than fear

## Weaknesses

- "Blameless" can be misread as "accountable-free" — repeated negligence should have consequences
- Action items written in post-mortems are often not tracked to completion
- Requires psychological safety that many organisations claim but few have

## Mitigation

Distinguish blameless analysis (always) from accountability (for genuine repeated negligence). Track action item completion rates — a post-mortem with no completed actions is a post-mortem that changed nothing.
