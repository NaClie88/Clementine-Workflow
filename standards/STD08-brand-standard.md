# STD08 — Brand & Document Design Standard

**Type**: Standard
**Number**: STD08
**Status**: Ratified
**Constitutional Authority**: `memory/constitution.md` Article IX (Respect for Persons — respect their time), Article VIII (Honesty & Transparency)

---

## Purpose

Defines how documents, interfaces, and communications produced by or for this system should look and behave. The guiding philosophy is **business casual**: professional without being stiff, functional without being ugly, navigable without being over-designed.

**Priority order:**
1. Function — does it do what the reader needs?
2. Navigation — can the reader find what they need quickly?
3. Clarity — is it unambiguous?
4. Appearance — does it look intentional?

Appearance is last. A beautiful document that is hard to navigate is a failure. An ugly document that is fast to use is a success.

---

## 1. Document Structure

Every document must open with a metadata block so its type, status, and authority are visible without reading the body:

```markdown
# [CODE] — [Title]

**Type**: [Standard | Specification | Decision | etc.]
**Number**: [CODE]
**Status**: [Draft | Review | Ratified | Superseded]
**Constitutional Authority**: [Article reference]
```

After the metadata block: a **Purpose** section in plain language. One paragraph. What this document is for and who needs it.

Then content sections. Then Revision History last (STD02).

---

## 2. Navigation Aids

Long documents (more than ~4 sections) must include a table of contents immediately after the Purpose section:

```markdown
## Contents
1. [Section Name](#1-section-name)
2. [Section Name](#2-section-name)
```

### Numbered Sections

All top-level content sections must be numbered: `## 1. Section Name`, `## 2. Section Name`. This enables unambiguous cross-referencing ("see STD08 §3.2") without fragile anchor links.

### Cross-References

Always reference by code and section number. Never reference by page or by prose description alone:

| Good | Avoid |
|---|---|
| `See STD05 §2.3` | "See the session end section of the AI continuity doc" |
| `STD01 applies` | "The naming standard applies" |
| `D01 §Consequences` | "The earlier decision about this" |

---

## 3. Typography and Formatting

### Headers

- `#` — Document title only. One per document.
- `##` — Top-level sections. Numbered.
- `###` — Subsections. Named but not numbered unless they will be cross-referenced.
- `####` — Use sparingly. If you need four levels of nesting, the section structure is wrong.

### Emphasis

- **Bold** — for terms being defined, critical rules, and UI labels
- *Italic* — for titles of other documents on first mention
- `Code` — for file paths, commands, document codes, field names, and values
- > Blockquote — for footnotes, caveats, and callouts that are important but not main flow

Do not use bold for decoration. If everything is bold, nothing is.

### Lists

Use bullet lists for unordered items with no ranking. Use numbered lists when order or sequence matters. Use tables when items have multiple attributes — a table of three columns beats three parallel bullet lists every time.

**Prefer tables over prose for:**
- Comparisons
- Permission matrices
- Status summaries
- Any list where each item has more than one attribute

---

## 4. Information Density

Documents are written for people who need to work efficiently, not people who need to be convinced. Assume the reader is competent. Write accordingly.

- **Use tables.** A 5-row table is faster to scan than 5 bullet points.
- **Lead with the rule, follow with the reason.** Not: "Because X is true, you should do Y." But: "Do Y. Reason: X."
- **No preamble.** Do not open a section by restating what the section is about to say.
- **No summary sections** that just repeat what was already written.
- **Examples beat descriptions.** Show it, then explain it if needed.

---

## 5. Tone

Business casual means: how a knowledgeable colleague writes to another knowledgeable colleague when the stakes are real.

| Use | Avoid |
|---|---|
| "Do X." | "It is recommended that one consider doing X." |
| "This fails when Y." | "There may be potential issues in scenarios involving Y." |
| "See STD03." | "Please refer to the commit message standard document for further guidance." |
| Direct corrections | Hedged corrections ("you might want to consider..."). |
| Short sentences | Long compound sentences with multiple subordinate clauses. |

Not casual: slang, emoji, rhetorical questions, humor at the expense of clarity.
Not formal: passive voice for accountability avoidance, jargon without definition, legalese.

---

## 6. Status Indicators

Use consistent language for document and work item states. Do not invent synonyms.

### Document Status

| Status | Meaning |
|---|---|
| `Draft` | In progress, not ready for use |
| `Review` | Complete, awaiting sign-off |
| `Ratified` | Approved and in force |
| `Superseded` | Replaced by a newer document — preserved for history |
| `Deprecated` | No longer applies — not superseded, just retired |

### Work Item States

| State | Meaning |
|---|---|
| `Open` | Not yet started |
| `In Progress` | Actively being worked |
| `Blocked` | Cannot proceed — reason must be noted |
| `Done` | Complete |
| `Won't Do` | Decided not to proceed — reason must be noted |

---

## 7. Visual Hierarchy in Practice

A well-structured document section looks like this:

```
## 3. Section Title

One sentence stating the rule or purpose of this section.

Explanation or detail if needed — kept to what the reader needs, not everything
that could be said.

| Column A | Column B | Column C |
|---|---|---|
| Value    | Value    | Value    |

> Caveat or footnote if applicable.
```

It does not look like this:

```
## Section 3: Some Title (Important!)

In this section we will be discussing the important topic of X, which as you
may know is very relevant to the overall goals we have established in previous
sections. There are several key points to consider...
```

---

## Revision History

| Rev | Date | Author | Why |
|---|---|---|---|
| 1.0 | 2026-03-10 | Claude | Initial creation — business casual, function-first design standard |
