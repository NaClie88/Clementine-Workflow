# D01 — Adopt Spec-Kit Directory Structure

**Date**: 2026-03-10
**Status**: Accepted
**Decided by**: Project Owner

---

## Context

The LLM Quickstart template initially used a flat governance-first directory structure with five subdirectories: `governance/`, `identity/`, `operations/`, `quality/`, `compliance/`. This was descriptive but did not align with any established development convention, making it harder to integrate with tooling and harder for an AI session to orient itself quickly.

GitHub's [spec-kit](https://github.com/github/spec-kit) provides a well-defined Spec-Driven Development structure with established conventions for `memory/`, `specs/`, `AGENTS.md`, and supporting `docs/`. Separately, a working operational standards system (STD01–STD07) existed in a sibling project with a `standards/` and `registry/` layer.

---

## Options Considered

### Option A — Keep Original Structure
Retain `governance/`, `identity/`, `operations/`, `quality/`, `compliance/` subdirectories.

**Pros:** Descriptive. Self-explanatory to a new human reader.
**Cons:** No tooling alignment. No established convention to reference. AI sessions have no prior pattern to anchor on. Five directories for what is conceptually a two-level system (law + operations).

### Option B — Adopt Spec-Kit + Clement Standards
Reorganize to spec-kit's `memory/` + `specs/` + `AGENTS.md` structure, add `standards/` and `registry/` from the Clement Personal Assistant operational standards system, and flatten all reference docs into `docs/`.

**Pros:** Aligns with an established, actively maintained open-source convention. `AGENTS.md` is recognized by Claude Code and other AI tools. `memory/constitution.md` maps directly to spec-kit's constitutional pattern. Standards and registry add session continuity and decision traceability that the original structure lacked entirely.
**Cons:** Requires mapping existing content to new locations. Some content (persona guide, system prompt) must be merged into `AGENTS.md`.

---

## Decision

Option B was chosen. The spec-kit structure is a better foundation because it is externally documented, tooling-recognized, and provides an upgrade path. The `standards/` and `registry/` additions fill gaps that spec-kit does not cover: operational conventions and session-to-session continuity. The merged `AGENTS.md` is a cleaner runtime artifact than separate system-prompt and persona files.

---

## Consequences

**Easier:**
- AI sessions can orient using established spec-kit conventions
- `AGENTS.md` is auto-recognized by Claude Code and compatible tools
- Session continuity is formally governed (STD05)
- Decision rationale is now traceable (this record)

**Harder or ruled out:**
- The original five-category mental model (governance/identity/operations/quality/compliance) is no longer reflected in the directory structure — it survives only in the README precedence table
- Any tooling built against the old paths needs updating

---

## Revision History

| Rev | Date | Author | Why |
|---|---|---|---|
| 1.0 | 2026-03-10 | Claude | Initial record |
