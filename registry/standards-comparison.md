# Standards Comparison — Clement vs. Clementine-LLM-QuickStart

**Type**: Reference Document
**Status**: Draft — For Future Standards Strengthening
**Scope**: `/home/josh/Development/Clement-Personal-Assistant/standards/` vs. `/home/josh/Development/Clementine-LLM-QuickStart/standards/`
**Purpose**: Identify strengths, weaknesses, and holes in each standards set to inform a future consolidation pass.

---

## Contents
1. [Coverage Map](#1-coverage-map)
2. [Side-by-Side Analysis — Shared Standards](#2-side-by-side-analysis--shared-standards)
3. [Quickstart-Only Standards](#3-quickstart-only-standards)
4. [Holes in Clement](#4-holes-in-clement)
5. [Holes in Quickstart](#5-holes-in-quickstart)
6. [Holes in Both](#6-holes-in-both)
7. [Recommended Actions](#7-recommended-actions)

---

## 1. Coverage Map

| Standard | Topic | Clement | Quickstart | Notes |
|---|---|---|---|---|
| STD01 | Document naming | ✅ | ✅ | Different scope — see §2 |
| STD02 | Revision history | ✅ | ✅ | Near-identical |
| STD03 | Commit messages | ✅ | ✅ | Quickstart has more examples |
| STD04 | Branch workflow | ✅ | ✅ | Minor pattern differences |
| STD05 | AI session continuity | ✅ | ✅ | Quickstart is materially stronger |
| STD06 | Decision log | ✅ | ✅ | Quickstart adds constitutional link |
| STD07 | Progress tracking | ✅ | ✅ | Quickstart adds anti-patterns |
| STD08 | Brand & document design | ❌ | ✅ | Absent in Clement |
| STD09 | Approved technology | ❌ | ✅ | Absent in Clement |
| AMD## | Amendment process | ✅ | ❌ | Absent in Quickstart |
| F## | Feature tracking | ✅ | ❌ | Absent in Quickstart |
| P## / T## | Plans and tasks (granular) | ✅ | ❌ | Quickstart uses specs/ instead |

---

## 2. Side-by-Side Analysis — Shared Standards

### STD01 — Document Naming

| Dimension | Clement | Quickstart |
|---|---|---|
| Document types tracked | 7 (C, STD, AMD, S, F, P, T, D) | 3 (C, STD, D) |
| Exemptions list | ❌ Missing | ✅ Explicit table (AGENTS.md, README, etc.) |
| Rationale section | ✅ "Why This Convention" explains reasoning | ❌ Absent — rules stated, not justified |
| Amendment mechanism | ✅ AMD## folder and prefix defined | ❌ No amendment process |
| docs/ reference docs | ❌ Not addressed | ✅ Explicitly scoped as unnumbered reference layer |

**Clement strength:** Richer document lifecycle — tracks what was built (F##) vs. what to build (S##), and has a formal amendment path.

**Quickstart strength:** Exemptions table prevents ambiguity about special files. Explicit about the `docs/` layer having no code prefix.

**Weakness of both:** Neither explains what happens when two documents conflict, or when a standard is wrong and needs to be violated before it can be formally changed.

---

### STD02 — Revision History

Near-identical. Quickstart's section 3 is titled "Position" vs. Clement's "The Revision History Section Position" — functionally the same.

**No material difference. Both are solid.**

---

### STD03 — Commit Messages

| Dimension | Clement | Quickstart |
|---|---|---|
| Example scope values | `constitution`, `registry` | `memory`, `registry`, `specs`, `docs/guardrails` |
| Example count | 4 | 6 |
| Content types in examples | Methodology-focused | Deployment/governance-focused |

**Both are solid.** Quickstart examples are more specific to its domain. Clement's examples are slightly more generic and reusable.

---

### STD04 — Branch Workflow

| Dimension | Clement | Quickstart |
|---|---|---|
| Feature branch pattern | `feat/STD##-description` only | `feat/STD##-description` OR `feat/description` |
| Spec-based branches | ❌ Not addressed | ✅ `feat/001-llm-deployment-spec` example |
| Cross-reference to commit standard | Implicit (`following STD03`) | Explicit (`STD03 — Commit Message Convention`) |
| PR review process | ❌ Not defined beyond "open a pull request" | ❌ Not defined beyond "open a pull request" |

**Shared weakness:** Neither defines what a pull request review must include before merging. Both say "merge only when complete and self-consistent" but leave "self-consistent" undefined.

---

### STD05 — AI Session Continuity

This is the most significant divergence between the two sets.

| Dimension | Clement | Quickstart |
|---|---|---|
| Session start read list items | 3 | 5 |
| Reads constitution at start | ❌ Not required | ✅ Required |
| Reads AGENTS.md at start | ❌ Not applicable | ✅ Required |
| LLM deployment handoff section | ❌ Absent | ✅ §4 covers guardrail events, overrides, knowledge issues |
| Cognitive overhead | Lower — faster to execute | Higher — more thorough |
| "Why" column in read list | ❌ Absent | ✅ Each item has a justification |

**Clement strength:** Simpler protocol — good for non-LLM projects where reading the constitution at every session would be unnecessary overhead.

**Quickstart strength:** Materially stronger for AI-governed systems. The constitution read at start prevents a session from unknowingly violating governing constraints. The LLM handoff section (§4) has no equivalent in Clement and is genuinely valuable.

**Shared weakness:** Neither standard defines what to do if the session start read list cannot be completed (e.g., a file is missing or corrupted). Both assume the documents exist.

---

### STD06 — Decision Log

| Dimension | Clement | Quickstart |
|---|---|---|
| "First-class document" framing | ❌ Absent | ✅ Explicit — elevates decision records in importance |
| Constitutional change link | ❌ Absent | ✅ §5 links decisions to change management process |
| Format | Identical | Identical |
| Superseding process | ✅ Defined | ✅ Defined — adds rationale for preserving history |

**Quickstart is strictly stronger** here. The constitutional link (§5) closes a real gap: without it, a decision that changes governing law could proceed without triggering the change management process.

---

### STD07 — Progress Tracking

| Dimension | Clement | Quickstart |
|---|---|---|
| Required sections | 4 (same) | 4 (same) |
| State vocabulary | `Draft/Review/Ratified` + `Development/Testing/Shipped` | Adds `Open/In Progress/Blocked/Resolved` for issues |
| Anti-patterns section | ❌ Absent | ✅ §3 "What Not to Put Here" |
| Example rows in code blocks | ✅ Present | ✅ Present |

**Quickstart is stronger.** The anti-patterns section prevents `progress.md` from drifting into a narrative log — a common failure mode. Blocked state in issue tracking is also a practical addition.

---

## 3. Quickstart-Only Standards

### STD08 — Brand & Document Design Standard

**Absent in Clement entirely.** This is a significant gap in Clement — without it, document formatting decisions are made ad hoc. Documents drift in structure, tone, and navigability over time.

**Strengths of the Quickstart STD08:**
- Explicit priority order (function > navigation > clarity > appearance)
- Named status vocabulary locks terminology across the system
- Counter-example at end ("It does not look like this") is unusually effective for a style guide
- Numbered section requirement enables unambiguous cross-referencing

**Weaknesses of the Quickstart STD08:**
- No guidance on image or diagram use
- No guidance on code block language tagging (` ```python ` vs. ` ``` `)
- The "7. Visual Hierarchy in Practice" section shows a good example but does not define a required template — it is advisory, not prescriptive
- No guidance on document length limits or when to split a document

---

### STD09 — Approved Technology and Dependency Governance

**Absent in Clement entirely.** Without this, any session can pull in any dependency without oversight.

**Strengths of the Quickstart STD09:**
- "Default is no" framing is strong and unambiguous
- Explicit approval definition table ("counts as approval" vs. "does not count") closes a common loophole
- Standard library preference rule is practical and prevents dependency bloat
- Vendored code prohibition is thorough

**Weaknesses of the Quickstart STD09:**
- No audit process — approved packages are logged in the table but there is no defined process for reviewing or revoking approvals
- No version pinning requirement — approving `requests` doesn't specify which version
- No security/vulnerability review requirement for new dependencies before approval
- The approved package table (§2.4) lives inside the standard itself — if the standard changes, the registry changes. These should arguably be separate documents.

---

## 4. Holes in Clement

These are topics Clement has no coverage for:

| Gap | Impact | Priority | Status |
|---|---|---|---|
| No brand/document design standard | Document quality and navigability drift over time | High | ✅ Fixed — STD08-document-design.md created |
| No technology/dependency governance | Uncontrolled dependency introduction | High | ✅ Fixed — STD09-approved-technology.md created |
| No session start constitution read | AI sessions may violate governing constraints unknowingly | High | ✅ Fixed — STD05 §1 now requires reading C01 at session start |
| No exemptions list in STD01 | Ambiguity about special files (README, AGENTS.md equivalent) | Medium | ✅ Fixed — STD01 §4 exemptions table added |
| No link between decisions and constitutional changes (STD06) | Governance changes can slip through without change management | Medium | ✅ Fixed — STD06 §5 links constitutional/standard changes to AMD## process |
| No "What Not to Put Here" in STD07 | progress.md drifts into a narrative log | Low | ✅ Fixed — STD07 §3 anti-patterns added |
| No PR review criteria in STD04 | "Self-consistent" is undefined — review quality varies | Low | ✅ Fixed — STD04 §4 merge checklist added |
| No guidance for missing/corrupt files at session start (STD05) | Silent failure mode | Low | ✅ Fixed — STD05 §1 missing-file protocol table added |

---

## 5. Holes in Quickstart

These are topics Quickstart has no coverage for:

| Gap | Impact | Priority | Status |
|---|---|---|---|
| No amendment (AMD##) process | Constitution and standards changes have no formal rollback path | High | Open — change-management.md partially covers this; a formal STD01 §4 amendment path was added pointing to it |
| No feature tracking (F##) | No record of what was actually built vs. what was specified | High | Open |
| STD01 lacks rationale section | New contributors don't understand why the convention exists | Medium | ✅ Fixed — "Why This Convention" section added to STD01 |
| No plan/task document types (P##, T##) in STD01 | specs/ covers this but without numbered codes | Medium | ✅ Fixed — specs/ layer clarified in STD01 §1 folder table |
| No version pinning in STD09 | Approved packages can silently change behavior across versions | Medium | ✅ Fixed — §2.4 now requires version column and pinning rationale |
| No package audit/revocation process in STD09 | Approvals accumulate and are never reviewed | Medium | ✅ Fixed — STD09 §6 audit and revocation added |
| No PR review criteria in STD04 | Same gap as Clement | Medium | ✅ Fixed — STD04 §4 added with merge checklist and "self-consistent" definition |
| No guidance on diagram/image use in STD08 | Inconsistent visual content | Low | ✅ Fixed — STD08 §4 Diagrams and Images added |
| No code block language tagging rule in STD08 | Syntax highlighting is inconsistent | Low | ✅ Fixed — STD08 §4 Code Blocks language tagging table added |
| No document length guidance in STD08 | Long documents are never split | Low | ✅ Fixed — STD08 §6 Document Length added |
| No guidance for missing files at session start (STD05) | Same silent failure mode as Clement | Low | ✅ Fixed — STD05 §1 missing-file protocol table added |

---

## 6. Holes in Both

Topics neither standards set addresses:

| Gap | Description | Priority |
|---|---|---|
| **Meta-standard: how standards are proposed** | How does a new standard get created? Who can propose one? What is the ratification process beyond "ratified"? | High |
| **Conflict resolution between standards** | What happens when two standards give contradictory guidance? Which wins? | High |
| **Review and expiry** | Standards can become outdated. Neither set has a process for periodic review or marking a standard as stale. | High |
| **Security standards** | No standard governs how security-sensitive content is handled in commits, docs, or sessions. | High |
| **Testing/validation standards** | No standard defines how to verify that a system built under these standards actually works. | Medium |
| **Onboarding standard** | No document defines the minimum a new contributor (human or AI) must read before making their first change. | Medium |
| **Escalation path when a standard is wrong** | If a standard is causing harm and needs to be violated before it can be changed, what is the path? | Medium |
| **Ownership and accountability** | Neither set defines who owns a standard, who can approve changes, or who is accountable when a standard is not followed. | Medium |
| **Archival standard** | What happens to superseded or deprecated documents? Are they deleted, moved, or kept in place? | Low |
| **Tooling standard** | What tools (editors, CI, linters) are required or recommended? No guidance exists. | Low |

---

## 7. Recommended Actions

Listed in priority order for a future strengthening pass.

### Immediate (fix before next use)

1. ~~**Add STD08 and STD09 equivalents to Clement.**~~ `✅ Done`
2. ~~**Add constitution read to Clement STD05.**~~ `✅ Done`
3. ~~**Add STD06 §5 (constitutional change link) to Clement.**~~ `✅ Done`

### Near-term (next standards revision)

4. **Build an amendment process for Quickstart.** STD01 §4 now points to change-management.md as the path; a dedicated amendment standard (or STD01 expansion) would make this explicit. `OPEN`
5. **Add feature/implementation tracking to Quickstart.** Decide whether F## documents live in specs/ or a new layer. `OPEN`
6. **Add a meta-standard (STD00 or equivalent) to both.** Defines: how standards are proposed, who ratifies, what "ratified" means operationally, and how to handle a standard that is wrong. `OPEN`
7. ~~**Add STD01 rationale section to Quickstart.**~~ `✅ Done`
8. ~~**Add version pinning to Quickstart STD09.**~~ `✅ Done`

### Future (when the system is mature)

9. **Add a periodic review standard to both.** Standards older than X months should be flagged for review.
10. **Add security standards to both.** At minimum: no secrets in commits, no sensitive data in progress.md, handling of security-relevant decisions.
11. **Add PR review criteria to both STD04s.** Define what "self-consistent" means — at least a checklist.
12. **Consolidate the two standards sets** into a single canonical set once both projects have stabilized, using this document as the merge guide.

---

## Revision History

| Rev | Date | Author | Why |
|---|---|---|---|
| 1.0 | 2026-03-12 | Claude | Initial creation — full diff of Clement vs. Quickstart standards sets |
| 1.1 | 2026-03-12 | Claude | Pass 1 complete — Quickstart gaps addressed; §5 status column updated; §7 near-term actions marked done |
| 1.2 | 2026-03-12 | Claude | Pass 2 complete — all 8 Clement gaps addressed; §4 status column updated; §7 immediate actions marked done |
