---
id: convention-over-configuration
title: "Convention over Configuration"
domain: architecture
sub-domain: "design principles"
applies-to: []  # TODO: backend | frontend | infrastructure | cloud | mobile | data | ml | all
complexity: ""  # TODO: low | medium | high
maturity: ""    # TODO: established | emerging | theoretical
theorist: ""    # TODO: primary originator or "multiple"
year: null      # TODO: year concept was formally named/published
related: []     # TODO: IDs of related entries
tags: []        # TODO: free-form tags
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
