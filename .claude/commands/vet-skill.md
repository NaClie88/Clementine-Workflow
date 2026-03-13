---
name: "vet-skill"
description: "Automated Phase 1 static analysis helper for script-backed skills. Reads all Python files in a skill directory and produces a structured §2.6 Script Analysis report plus §2.7 Package Review Gate check. Run before the full Phase 1 review to surface risks quickly."
---

# Vet Skill

Automated static analysis for script-backed skills. Covers Phase 1 §2.5 Hook Analysis, §2.6 Script Analysis, and §2.7 Package Review Gate. Outputs a structured report for use in the full vetting workflow.

**This skill is read-only. It never writes, installs, or executes anything.**

---

## Usage

```
/vet-skill <path-to-skill-directory>
```

Examples:
```
/vet-skill skills/playwright-pro
/vet-skill /path/to/alirezarezvani-skills/engineering/api-test-suite-builder
```

---

## Behaviour

### Step 1 — Discover skill contents

Read the skill directory. Identify and list:
- `SKILL.md` (required — abort with error if missing)
- `hooks.json` (if present)
- `settings.json` (if present)
- All `.py` files (recursively)
- All `.sh` files (recursively)
- Any other executable or config files

Report the file inventory before proceeding.

### Step 2 — Read SKILL.md

Extract:
- Skill name and description
- Stated capabilities
- Any mentions of file paths, external services, or shell commands

### Step 3 — §2.5 Hook Analysis (if hooks.json or settings.json present)

For `hooks.json`:
- List each hook: event type, matcher (if any), command
- For each hook command: is it a shell script, inline command, or python call?
- Read each referenced shell script and summarize what it does
- Flag any hook that:
  - Fires on ALL Bash commands (no matcher, or matcher is `.*`)
  - Writes to files (especially governance files: CLAUDE.md, standards/, .claude/)
  - Reads governance or secret files
  - Makes network calls
  - Has no clear bounded purpose

For `settings.json`:
- List all pre-granted `Bash(...)` permissions
- Flag any that grant broad shell access (wildcards, no command restriction)
- Note: pre-granted permissions bypass per-use confirmation — this is by design for automation tools but must be explicitly justified

### Step 4 — §2.6 Script Analysis

For each `.py` file, produce a structured analysis:

#### 4a — Import Inventory

List every import statement. For each:
- Package name
- Is it stdlib / Tier 1 / Tier 2 / Tier 3 / Tier 4 / Unknown?
  - Look up each package in `docs/package-review.md` to determine tier
  - Any package not in the registry = **Unknown — must be reviewed before Phase 4**
- Flag Tier 3+ packages immediately

#### 4b — File Operation Analysis

Search for:
- `open(`, `Path(...).write`, `Path(...).read`, `shutil.copy`, `shutil.move`, `os.remove`, `os.unlink`, `os.makedirs`, `tempfile`
- For each: what path is accessed? Is the path user-controlled or fixed?
- Flag any writes outside `/tmp/` or the project working directory
- Hard flag: writes to `~/.claude/`, `~/.aws/`, `~/.ssh/`, `~/.config/`, `CLAUDE.md`, `standards/`, `.claude/rules/`

#### 4c — Network Call Analysis

Search for:
- `requests.get`, `requests.post`, `httpx.get`, `httpx.post`, `urllib.request`, `socket.connect`, `http.client`
- For each: what is the target URL/host? Is it a fixed constant or user-controlled?
- Flag any calls where the URL/host is constructed from user input without validation
- Flag any calls to non-local hosts (anything not `127.0.0.1` / `localhost`)
- Hard flag: calls that send file contents or environment variables to external hosts

#### 4d — Shell Execution Analysis

Search for:
- `subprocess.run`, `subprocess.Popen`, `subprocess.call`, `os.system`, `os.popen`, `shlex`
- For each: what command is run? Is it a fixed string or constructed from user input?
- Hard flag: user input passed to shell without sanitization (`shell=True` with variable interpolation)
- Hard flag: `exec()`, `eval()`, `compile()` with any non-literal input

#### 4e — Data Flow Summary

High-level: what comes in (args, stdin, files, env) → what happens to it → what goes out (files, network, stdout)?

Flag any path where sensitive data (credentials, file contents) flows to external destinations.

### Step 5 — §2.7 Package Review Gate

Produce a gate checklist:

```
Package Review Gate
──────────────────
[package-name] (version if pinned) — Tier X — [APPROVED / APPROVED WITH CONDITIONS / BLOCKED / Unknown]
...

Gate result:
□ All packages reviewed in docs/package-review.md?          YES / NO
□ Any Tier 4 (Blocked) packages present?                    YES / NO  ← auto hard reject if YES
□ Any Unknown packages present?                             YES / NO  ← must review before Phase 4
□ Any Tier 3 packages with missing justification?           YES / NO

Verdict: GATE PASS / GATE HOLD (packages need review) / GATE FAIL (Tier 4 present)
```

### Step 6 — Summary Report

Output a complete structured report:

```
═══════════════════════════════════════════════════
VET-SKILL REPORT — [skill-name]
Generated: [date]
═══════════════════════════════════════════════════

SKILL TYPE: Script-Backed

FILE INVENTORY
  SKILL.md          ✓
  hooks.json        [present / absent]
  settings.json     [present / absent]
  Python files:     [list]
  Shell scripts:    [list]

────────────────────────────────────────────────────
§2.5 HOOK ANALYSIS
────────────────────────────────────────────────────
[Hook findings or "No hooks.json or settings.json found"]

FLAGS:
  [list any hook flags, or "None"]

────────────────────────────────────────────────────
§2.6 SCRIPT ANALYSIS — [filename.py]
────────────────────────────────────────────────────
Import Inventory:
  [package list with tiers]

File Operations:
  [findings or "None detected"]

Network Calls:
  [findings or "None detected"]

Shell Execution:
  [findings or "None detected"]

Data Flow:
  [summary]

FLAGS:
  [list any script flags, or "None"]

[Repeat for each .py file]

────────────────────────────────────────────────────
§2.7 PACKAGE REVIEW GATE
────────────────────────────────────────────────────
[Gate checklist]

════════════════════════════════════════════════════
OVERALL PHASE 1 PRE-ASSESSMENT
════════════════════════════════════════════════════
Hard reject triggers present:  YES / NO
  [list any triggers]

Flags requiring review:         [count]
  [list]

Recommended Phase 1 verdict:
  □ PASS — proceed to Phase 2
  □ PASS WITH FLAGS — proceed to Phase 2, resolve flags before Phase 4
  □ HARD REJECT — [reason]
  □ GATE HOLD — add unknown packages to package-review.md, then re-run

Next steps:
  [specific actions needed]
════════════════════════════════════════════════════
```

---

## Hard Reject Triggers

Immediately mark **HARD REJECT** if any of the following are found:

- Any read or write to `~/.claude/` paths
- Any write to `CLAUDE.md` or `standards/STD*.md`
- Any `PostToolUse` hook with no event type matcher (fires on all tool uses)
- Any `Bash(*)` pre-grant in settings.json (blanket shell permission)
- Tier 4 package present in imports
- `exec()` / `eval()` receiving user-controlled input
- Network calls sending environment variables or file contents to external hosts
- Shell command constructed from user input with `shell=True`

---

## Rules

- This skill never installs packages, runs Python, or executes any commands
- This skill never writes files (except saving the report if the Operator explicitly asks)
- All analysis is static — reading source code only
- If `docs/package-review.md` does not exist, note it and classify all packages as Unknown
- Unknown packages are not automatic rejects — they are a hold: the package must be reviewed and added to the registry before Phase 4 proceeds
- This skill does not replace the full Phase 1 review in `docs/skill-vetting-workflow.md` — it accelerates §2.5, §2.6, and §2.7; the reviewer still applies §2.1–§2.4 and §2.8 manually
