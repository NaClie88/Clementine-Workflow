# STD01 — Document Naming and Organisation Convention

**Type**: Standard
**Number**: STD01
**Status**: Ratified
**Constitutional Authority**: `memory/constitution.md` Article XIX (Consistency)

---

## Purpose

Every document in this system must be findable, referenceable, and self-describing without requiring the reader to open it. This standard defines how documents are named, where they live, and how they are referenced across the project.

Two goals, equally weighted:
- **Human readability** — the filename tells you what the document is about
- **Functional referencing** — a short code (`STD01`, `D03`) lets any document reference another precisely without ambiguity

---

## 1. Folder Structure

Document type is conveyed by folder location. Each folder has one purpose.

| Folder | Code | Description |
|---|---|---|
| `memory/` | C## | Constitution — the highest governing document. Rarely changes. |
| `standards/` | STD## | Operational rules derived from the constitution. Prescriptive — "always do X". |
| `specs/[deployment-name]/` | S## | Specifications for a deployment: user stories, requirements, success criteria. |
| `docs/` | — | Operational reference: guardrails, roles, tools, session, quality, compliance. |
| `registry/` | — | Project state and decision records. |
| `registry/decisions/` | D## | Records of design choices made at decision forks. |

---

## 2. File Naming Convention

```
TYPE##-descriptive-kebab-case-name.md
```

| Prefix | Folder | Example |
|---|---|---|
| `C` | `memory/` | `C01-llm-constitution.md` |
| `STD` | `standards/` | `STD01-document-naming.md` |
| `D` | `registry/decisions/` | `D01-spec-kit-structure-adoption.md` |

### Rules

- Numbers zero-padded to two digits: `01`, `02`, `03`
- Descriptive names in lowercase kebab-case
- The descriptive name must be meaningful without opening the file
- No abbreviations unless universally understood

### Cross-referencing

Use the short code followed by the descriptive name on first mention, then the short code alone:

> See STD05 — AI Session Continuity for the session start protocol. STD05 applies at the beginning of every working session.

---

## 3. Files That Do Not Follow This Convention

These files exist at fixed paths required by tooling or convention and are exempt:

| File | Reason |
|---|---|
| `AGENTS.md` | Required by spec-kit and Claude Code conventions |
| `README.md` | Required by GitHub and most tooling |
| `registry/progress.md` | Fixed path referenced by STD05 and STD07 |
| `memory/constitution.md` | Fixed path — single constitution |

---

## Revision History

| Rev | Date | Author | Why |
|---|---|---|---|
| 1.0 | 2026-03-10 | Claude | Initial creation, adapted from Clement-Personal-Assistant STD01 |
