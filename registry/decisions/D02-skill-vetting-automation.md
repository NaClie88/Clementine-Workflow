# D02 — Skill Vetting Automation: skill-tester Evaluation

**Date**: 2026-03-15
**Status**: Accepted
**Decided by**: Joshua Alexander Clement

---

## Context

The backlog contained two related questions arising from prior skill vetting work:

1. Can the `skill-tester` skill (`/tmp/claude-skills/engineering/skill-tester`) serve as a Phase 1 automation base for the vetting workflow?
2. Should its quality checks (`--help` validation, JSON output compliance, dual output format) become a formal Phase 1 gate?

Phase 1 of the vetting workflow (`docs/skill-vetting-workflow.md §2`) is defined as "Read only. No execution." It covers: full file inventory (§2.0), tool inventory (§2.1), file scope analysis (§2.2), network scope analysis (§2.3), prompt injection scan (§2.4), hook and injection analysis (§2.5), script analysis (§2.6), and package review (§2.7). The workflow already references `/vet-skill [path]` to automate §2.6 output.

---

## Options Considered

### Option A — Adopt skill-tester as Phase 1 automation base

skill-tester's `skill_validator.py` performs static checks: SKILL.md existence, frontmatter parsing, section presence, Python syntax (AST), argparse usage, main guard, and external import detection. These partially overlap with §2.6.

**Against:** Phase 1's highest-value sections — §2.1 (Claude tool inventory), §2.2 (file scope), §2.3 (network scope), §2.4 (prompt injection scan), §2.5 (hook and injection analysis) — are not touched by skill-tester at all. Its import whitelist is quality-focused, not security-focused: it flags non-stdlib packages but does not detect `shell=True`, dangerous `subprocess` patterns, or path traversal constructions. `/vet-skill` already covers the automatable portion of §2.6 in the context of this workflow. Adopting skill-tester as a "base" creates false confidence by associating automated output with the security-critical sections it never checks.

### Option B — Add --help/JSON/dual-output as Phase 1 quality gates

skill-tester's `script_tester.py` validates `--help` output, dual format support (JSON + human-readable), and expected output compliance.

**Against:** These checks require executing the scripts. Phase 1 is explicitly read-only and no-execution. They cannot be Phase 1 checks by definition. They are valid quality checks and belong in Phase 4 (sandboxed execution), not Phase 1.

### Option C — Adopt skill-tester structural checks as supplementary pre-screen (Phase 0)

Before full Phase 1 review, skill-tester could flag skills that fail basic structure requirements immediately (no SKILL.md, wrong directory layout). This would be a fast early-exit filter, not a replacement for Phase 1.

**Against:** The gain is minimal. §2.0 (Full File Inventory) already catches structural absences in the first step of Phase 1, and Claude reads the output of that inventory directly before proceeding. A separate pre-screen tool adds process complexity without meaningful security benefit.

### Option D — Don't adopt skill-tester; add --help/JSON/dual-output as Phase 4 checks

Keep Phase 1 as-is (`/vet-skill` for §2.6 automation; Claude judgment for all other sections). Add `--help` validation, JSON output compliance, and dual output format as Phase 4 supplementary checks for script-backed skills. These are legitimate quality standards and Phase 4 is the right home because execution is required.

---

## Decision

**Option D.**

skill-tester is not adopted as a Phase 1 automation base. The reasoning is structural: the most security-critical Phase 1 checks (§2.1–§2.5) require Claude reading and reasoning about prompt content, tool invocations, file paths, and hook configurations — not pattern-matching script execution. skill-tester was built for quality assurance in the claude-skills ecosystem, not adversarial security review. Its import detection is security-naive and its most useful capabilities (runtime testing, `--help` validation, output format compliance) require execution, placing them in Phase 4.

`/vet-skill` already provides the right automation for §2.6. No change to Phase 1 is warranted.

`--help` validation, JSON output compliance, and dual output format support are added as Phase 4 supplementary checks for script-backed skills (see Consequences). These are meaningful quality gates that execution can verify.

---

## Consequences

**What this makes easier:**
- Phase 1 remains a focused, security-aware review — Claude reads and reasons; tools assist on the mechanical §2.6 section only.
- Phase 4 gains three new quality checks for script-backed skills, executable in the sandbox already used for execution testing.

**What this rules out:**
- Fully automated Phase 1 passing without Claude review. This is intentional — the security-critical sections (§2.4 prompt injection, §2.5 hook analysis) require human or AI judgment, not pattern matching.

**Required follow-up:**
- Update `docs/skill-vetting-workflow.md §5` (Phase 4 — Sandboxed Execution) to add, for script-backed skills: (1) run each script's `--help` flag and confirm it outputs a usage message without error; (2) run with `--json` and confirm valid JSON is produced; (3) confirm a human-readable format is also available. These are supplementary — failure is a flag for Operator review, not an automatic reject.

---

## Revision History

| Rev | Date | Author | Why |
|---|---|---|---|
| 1.0 | 2026-03-15 | claude-sonnet-4-6 | Initial record |
