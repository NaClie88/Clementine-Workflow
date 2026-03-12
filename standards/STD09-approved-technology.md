# STD09 — Approved Technology and Dependency Governance

**Type**: Standard
**Number**: STD09
**Status**: Ratified
**Constitutional Authority**: `memory/constitution.md` Article V (No Undermining Oversight), Article XII (Accountability)

---

## Purpose

Defines which technologies, runtimes, and libraries are approved for use in this system and governs how new dependencies are introduced. The default answer to "can I add this?" is no — until the owner explicitly says yes.

This standard applies to AI sessions and human contributors equally. Neither may introduce an unapproved dependency on the grounds of convenience, familiarity, or assumed approval.

---

## Contents
1. [The Rule](#1-the-rule)
2. [Approved Technology Registry](#2-approved-technology-registry)
3. [Using Approved Technologies](#3-using-approved-technologies)
4. [Requesting a New Dependency](#4-requesting-a-new-dependency)
5. [Prohibited Behaviors](#5-prohibited-behaviors)
6. [Audit and Revocation](#6-audit-and-revocation)

---

## 1. The Rule

**Use what is already approved. Do not add what is not.**

Before using any external library, runtime, framework, tool, or service:
1. Check the Approved Technology Registry in §2.
2. If it is listed — use it.
3. If it is not listed — stop. Do not install it, import it, or reference it in code. Request approval per §4.

If completing a task requires an unapproved dependency, surface that blocker to the user before proceeding. Do not find a workaround that quietly pulls in something unapproved.

---

## 2. Approved Technology Registry

### 2.1 Runtimes and Languages

| Technology | Approved Use | Notes |
|---|---|---|
| Python | General scripting, automation, data processing, AI/ML tooling | Use standard library first; see §3 |
| Node.js | Backend services, CLI tooling, JavaScript runtime | npm ecosystem; see §3 |
| SQL (relational database) | Structured data storage and querying | See approved engines below |

### 2.2 Approved Database Engines

| Engine | Approved Use |
|---|---|
| PostgreSQL | Production relational data storage |
| SQLite | Lightweight/local relational data storage, testing, prototyping |

### 2.3 Approved Package Ecosystems

| Ecosystem | Associated Runtime | Notes |
|---|---|---|
| pip / PyPI | Python | Standard library preferred; third-party packages require approval per §4 |
| npm / Node.js packages | Node.js | Core packages preferred; third-party packages require approval per §4 |

> Approval of a runtime (Python, Node.js) does not constitute approval of the entire ecosystem. Individual third-party packages still require explicit approval unless they are part of the standard library or listed in §2.4.

### 2.4 Approved Third-Party Packages

> This table is populated as packages are approved through the §4 process. Start here — add approved packages as they are granted.

| Package | Version | Ecosystem | Approved Use | Approved By | Date |
|---|---|---|---|---|---|
| [package-name] | [x.y.z] | [pip / npm] | [what it is used for] | [approver] | [date] |

> Version pinning is required. Approving `requests` without a version means the approval covers an undefined range of behavior. Approve a specific version (`requests==2.31.0`). If the version must be updated, reapprove — do not assume the new version behaves identically.
>
> Semantic version ranges (`^1.2.0`, `~1.2`) are acceptable only when the session owner explicitly approves the range in writing. Blanket "latest" approvals are not permitted.

---

## 3. Using Approved Technologies

Approval of a technology means it may be used — it does not mean it must be used. Before reaching for an approved external package:

1. **Check the standard library first.** If Python's `json`, `os`, `pathlib`, or Node's `fs`, `path`, `http` can do the job, use them. Do not import a package for something the standard library handles.
2. **Use the simplest approved option.** If SQLite is sufficient, do not use PostgreSQL. If a shell script is sufficient, do not write a Python service.
3. **Do not import unused packages.** Every dependency added to a project is a dependency that must be maintained, audited, and updated. Add only what is used.

---

## 4. Requesting a New Dependency

When a task genuinely requires something not in the registry:

1. **Stop.** Do not proceed with the task using the unapproved dependency.
2. **Identify the need.** What specific capability is required that approved technology cannot provide?
3. **Surface it to the user.** State clearly: "This task requires [dependency], which is not in the approved technology registry. Do you approve adding it?"
4. **Wait for explicit approval.** Implied approval is not approval. "I guess that's fine" is not approval. The user must clearly say yes.
5. **Log the decision.** Create a decision record in `registry/decisions/` per STD06 — Decision Log, documenting what was requested, why, and that it was approved.
6. **Add to §2.4.** Update the Approved Third-Party Packages table in this document before using the dependency.

### What Counts as Explicit Approval

| Counts as approval | Does not count |
|---|---|
| "Yes, add it." | Silence after the request |
| "Approved — go ahead." | "I guess we need it." |
| Explicit written confirmation in the session | Assumed approval based on context |

---

## 5. Prohibited Behaviors

- **Do not install dependencies speculatively.** "It might be useful later" is not a justification.
- **Do not add a dependency and ask for approval afterward.** Approval must come before installation or import.
- **Do not use an unapproved package by aliasing or wrapping it** in a way that obscures what it is.
- **Do not treat a prior approval in another project as approval here.** Each project maintains its own registry. Approval is not transferable.
- **Do not circumvent this standard by embedding a dependency's code directly** into the project without approval. Vendored code is still a dependency.

---

## 6. Audit and Revocation

Approvals accumulate. Packages that are approved but no longer used, or that have known vulnerabilities, must be removed from the registry.

### Periodic Review

The §2.4 table must be reviewed at minimum:
- Before any new deployment goes live
- When a session adds a new entry to §2.4

During a review, confirm for each entry:
1. Is the package still in active use in this project?
2. Does the approved version have known CVEs? Check the package's security advisories.
3. Is a newer version required by another dependency?

If a package fails any check, revoke it per the process below.

### Revocation Process

1. Remove or update the row in §2.4.
2. Identify every file in the project that imports or uses the package.
3. Either replace the usage with an approved alternative, or request re-approval of a clean version.
4. Create a decision record in `registry/decisions/` noting: what was revoked, why, and what replaced it.
5. Commit the revocation as a `chore:` commit per STD03.

Do not simply delete the row and leave the import in place. The package is not considered removed until both the registry and the codebase are clean.

---

## Revision History

| Rev | Date | Author | Why |
|---|---|---|---|
| 1.0 | 2026-03-10 | Claude | Initial creation — approved technology and dependency governance |
| 1.1 | 2026-03-12 | Claude | Added version pinning requirement to §2.4, added §6 audit and revocation process |
