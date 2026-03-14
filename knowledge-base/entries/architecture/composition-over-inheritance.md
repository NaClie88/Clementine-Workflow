---
id: composition-over-inheritance
title: "Composition over Inheritance"
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

Favour assembling behaviour from discrete components rather than building deep inheritance hierarchies.

## Example

Instead of `class PDFExporter(Exporter, FileHandler)`, use `class Exporter: def __init__(self, formatter, file_handler)` where formatter and file_handler are injected.

## Strengths

- More flexible at runtime — behaviour can be swapped
- Avoids the fragile base class problem
- Components are easier to test in isolation

## Weaknesses

- More objects to manage and inject
- Dependency injection can obscure what a class actually does
- Some inheritance hierarchies are genuinely appropriate and cleaner than composition

## Mitigation

Use composition by default. Resort to inheritance only for true is-a relationships with stable, shared base behaviour. Never inherit for code reuse alone.
