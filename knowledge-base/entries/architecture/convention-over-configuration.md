---
id: convention-over-configuration
title: "Convention over Configuration"
domain: architecture
sub-domain: "design principles"
applies-to: [backend, frontend]
complexity: low
maturity: established
theorist: David Heinemeier Hansson
year: 2005
related: [kiss, yagni, principle-of-least-astonishment]
tags: [framework-design, rails, developer-experience, defaults]
---

## Definition

Assume sensible defaults; require explicit configuration only when deviation is needed.

## Example

Rails assumes a `posts` table for a `Post` model, `PostsController` for `/posts`, and templates in `views/posts/`. You configure only deviations.

## Strengths

- Dramatically reduces boilerplate
- Teams share a common mental model without extensive documentation
- Reduces decision fatigue

## Weaknesses

- Opaque for newcomers who don't know the conventions
- Debugging a convention violation requires framework-level knowledge
- "Magic" behaviour is hard to reason about when it breaks

## Mitigation

Document conventions explicitly (CLAUDE.md is an example of this applied to AI tooling). Treat deviations as explicit, documented opt-outs.
