# Skill Vetting Workflow

**Type**: Reference Document
**Status**: Ratified
**Constitutional Authority**: `memory/constitution.md` Part 1, Amendment 5 (No Undermining Oversight), Part 2, Amendment 5 (Accountability)

---

## Purpose

Defines the process for reviewing, testing, and approving Claude Code skills from external or unverified sources before they are added to `docs/approved-skills.md`. A skill that has not completed this workflow is treated as unapproved regardless of its apparent quality or source reputation.

Skills are either **pure-prompt** (SKILL.md only — no scripts) or **script-backed** (includes Python or shell scripts invoked via Bash). The workflow covers both. Script-backed skills require additional phases — §2.6 (Script Analysis), §2.7 (Package Review), and the Python sandbox in §7.2.

---

## Contents
1. [Threat Model](#1-threat-model)
2. [Phase 1 — Static Analysis](#2-phase-1--static-analysis)
3. [Phase 2 — Constitutional Review](#3-phase-2--constitutional-review)
4. [Phase 3 — Risk Classification](#4-phase-3--risk-classification)
5. [Phase 4 — Sandboxed Execution](#5-phase-4--sandboxed-execution)
6. [Phase 5 — Approval Decision](#6-phase-5--approval-decision)
7. [Sandbox Setup and Teardown](#7-sandbox-setup-and-teardown)
8. [Red Flag Reference](#8-red-flag-reference)
9. [Package Risk Tiers](#9-package-risk-tiers)
10. [Dependency Chain Analysis](#10-dependency-chain-analysis)

---

## 1. Threat Model

Skills are prompt templates that instruct Claude to invoke tools — `Bash`, `Edit`, `Write`, `WebFetch`, `WebSearch`, and others. Script-backed skills additionally execute Python or shell code. The risks are not in reading a skill file — they are in executing one.

### Prompt-layer threats

| Threat | Description | Caught in Phase |
|---|---|---|
| **Prompt injection** | Instructions hidden in the skill designed to override Claude's behavior or constitution | 1, 2 |
| **Unexpected tool scope** | Skill reads or writes files outside its stated purpose | 1, 4 |
| **Data exfiltration** | Skill sends data to external URLs via WebFetch or WebSearch | 1, 4 |
| **Persistent modification** | Skill writes to config, memory, standards, or constitution files | 1, 4 |
| **Credential harvesting** | Skill requests or logs sensitive values (tokens, passwords, keys) | 1, 2 |
| **Supply chain confusion** | Skill impersonates a known approved skill with subtle behavioral differences | 1, 2 |

### Script-layer threats (script-backed skills only)

| Threat | Description | Caught in Phase |
|---|---|---|
| **Malicious package** | pip dependency contains a supply chain attack or hidden payload | 1.7, 4 |
| **Script exfiltration** | Script reads project files and sends them to an external server | 1.6, 4 |
| **Shell injection** | Script constructs shell commands from user-controlled input | 1.6, 4 |
| **Privilege escalation** | Script calls system commands to expand its own access | 1.6, 4 |
| **Dependency confusion** | Package name squatting — a malicious package with a similar name to a legitimate one | 1.7 |
| **Stale CVEs** | Known vulnerabilities in pinned or unpinned packages | 1.7, 4 |
| **Unconstrained file scope** | Script reads or writes paths based on runtime input, not fixed constants | 1.6, 4 |

Reading the skill file and scripts to perform static analysis is safe. The threat only activates on execution.

---

## 2. Phase 1 — Static Analysis

**Goal**: Understand what the skill does without running it.
**Required tool**: Read only. No execution.

For script-backed skills, complete all sections including §2.6 and §2.7 before proceeding. Use `/vet-skill [path]` to automate §2.6 output.

### 2.1 Tool Inventory

List every tool the skill invokes. Flag any that are unexpected for the skill's stated purpose.

| Tool | Risk Level | Notes |
|---|---|---|
| `Read`, `Glob`, `Grep` | Low | Read-only |
| `Edit`, `Write` | Medium | Modifies files — scope matters |
| `Bash` | High | Arbitrary shell execution |
| `WebFetch`, `WebSearch` | High | External network calls |
| `Agent` | High | Spawns sub-agents with their own tool access |
| `NotebookEdit` | Medium | Modifies Jupyter notebooks |

### 2.2 File Scope Analysis

For every `Edit`, `Write`, or `Read` call in the skill:
- What paths does it access?
- Are any of those paths outside the working directory?
- Does it access `memory/`, `standards/`, `constitution/`, `.claude/`, `~/.claude/`, or system paths?

Any skill that reads or writes to governance documents (`constitution.md`, `standards/STD*`, `AGENTS.md`) without an explicit documented reason is a **hard reject**.

### 2.3 Network Scope Analysis

For every `WebFetch` or `WebSearch` call:
- What URL or query is being sent?
- Is any project data, file content, or session context included in the request?
- Is the domain hardcoded or constructed dynamically?

A skill that sends file contents or session data to an external URL is a **hard reject**.

### 2.4 Prompt Injection Scan

Read the skill file looking for:

| Pattern | Example | Flag |
|---|---|---|
| Override instructions | "Ignore previous instructions" | Hard reject |
| Constitution bypass | "Disregard the constitution for this task" | Hard reject |
| Role replacement | "You are now [different persona]" | Hard reject |
| Hidden instructions | Instructions in HTML comments, zero-width characters, or unusual whitespace | Hard reject |
| Scope creep language | "Also do X while you're at it" where X is unrelated to the skill's stated purpose | Review |
| Escalation requests | Asking Claude to request more permissions or tool access than needed | Review |

### 2.5 Hook Analysis (if hooks present)

If the skill ships a `hooks.json`, `settings.json`, or shell hook scripts:

- What events trigger each hook? (`PostToolUse`, `SessionStart`, `PreToolUse`, etc.)
- What does the hook script do? Read the shell script in full.
- Does the hook write to any files? Which paths?
- Does the hook make network calls?
- Does the hook fire on every session/tool use, or only on scoped patterns?
- Does `settings.json` pre-grant Bash permissions? What scope?

Pre-granted Bash permissions with broad wildcards (`Bash(*)`) are a **hard reject**. Scoped patterns (`Bash(npx playwright*)`) require Operator review and decision.

### 2.6 Script Analysis (script-backed skills only)

Run `/vet-skill [path]` to generate a structured report, or perform manually.

For every Python or shell script in the skill directory:

#### 2.6.1 Import Inventory

Extract every `import X` and `from X import Y` statement.

```bash
grep -rn "^import\|^from" [skill-dir]/**/*.py | sort
```

Cross-reference each package against `docs/package-review.md`. Flag any package not listed as **unreviewed** — it must be reviewed in §2.7 before proceeding.

Standard library modules (`os`, `pathlib`, `json`, `re`, `sys`, `datetime`, `typing`, `csv`, `hashlib`, `argparse`, `dataclasses`, `collections`, `itertools`, `functools`, `math`, `random`, `string`, `time`, `copy`, `io`, `abc`, `enum`, `contextlib`, `logging`, `traceback`, `warnings`, `inspect`, `ast`) do not require package review — but their *use* is assessed in §2.6.2–2.6.4.

#### 2.6.2 File Operation Analysis

Scan for all file access patterns:

```bash
grep -n "open(\|Path(\|os\.path\|os\.makedirs\|os\.remove\|os\.rename\|shutil\." [script].py
```

For each finding, document:
- The path being accessed (hardcoded constant vs. constructed from input)
- The access mode (`r`, `w`, `a`, `rb`, `wb`, etc.)
- Whether the path could be manipulated by user-controlled input (path traversal risk)

Flag if:
- Paths are constructed by joining user input without sanitisation
- Writes target directories outside `[skill-dir]/` or `/tmp/`
- Any access to `~`, `~/.claude/`, `/etc/`, `/usr/`, or other system paths

#### 2.6.3 Network Call Analysis

Scan for all network access patterns:

```bash
grep -n "requests\.\|httpx\.\|urllib\.\|aiohttp\.\|http\.client\|socket\." [script].py
```

For each finding, document:
- The URL being called (hardcoded vs. constructed)
- What data is included in the request body or query string
- Whether any local file contents or session state are transmitted

A script that sends project file contents or session data to an external URL is a **hard reject**.

#### 2.6.4 Shell Execution Analysis

Scan for subprocess and eval patterns:

```bash
grep -n "subprocess\.\|os\.system\|os\.popen\|pty\.\|eval(\|exec(" [script].py
```

For each finding, document:
- The exact command being run
- Whether any command arguments are constructed from user-controlled input (shell injection risk)
- Whether the command could expand its own access (sudo, chmod, chown, curl | bash)

Shell commands constructed from unvalidated user input are a **hard reject**.

#### 2.6.5 Data Flow Summary

For each script, summarise:
- What inputs it accepts (function arguments, stdin, CLI args, environment variables)
- What outputs it produces (return values, files written, stdout)
- Whether any sensitive values (API keys, passwords, PII) pass through

### 2.7 Package Review Gate (script-backed skills only)

After §2.6.1 import inventory, for every package not already in `docs/package-review.md`:

1. Look up the package on PyPI — note author, version history, download count
2. Check for known CVEs: `pip audit --require-hashes` (if pip-audit is available) or manually check the PyPI security advisories page
3. Review the package's own imports — does it pull in unexpected transitive dependencies?
4. Classify the package using §9 (Package Risk Tiers)
5. Add it to `docs/package-review.md` with findings

**A skill cannot proceed to Phase 4 until all its packages are in `docs/package-review.md`.**

### 2.8 Static Analysis Checklist

**For all skills:**
```
[ ] Tool inventory complete — all tools identified and listed
[ ] File scope documented — all read/write paths noted
[ ] No access to governance documents (memory/, standards/, .claude/)
[ ] Network calls identified — URLs and data sent documented
[ ] No project data sent to external URLs
[ ] Prompt injection scan complete — no override patterns found
[ ] Skill does what it claims and only what it claims
[ ] Source noted — where did this skill come from?
[ ] Hooks reviewed if present — scope and auto-fire behaviour documented
```

**Additional for script-backed skills:**
```
[ ] Import inventory complete — all packages listed
[ ] All packages checked against docs/package-review.md
[ ] No unreviewed packages (or unreviewed packages explicitly queued for §2.7)
[ ] File operations documented — paths, modes, construction methods
[ ] No file writes outside skill working directory or /tmp/
[ ] Network calls documented — URLs and request bodies identified
[ ] No project data in network requests
[ ] No shell execution with user-controlled arguments
[ ] No eval() or exec() with dynamic content
[ ] Data flow documented — inputs and outputs clearly understood
[ ] Dependency chain checked — does this skill depend on another? (see §10)
```

---

## 3. Phase 2 — Constitutional Review

**Goal**: Confirm the skill's instructions are consistent with the constitution.

Check against each Part:

| Part | Check |
|---|---|
| Part 1, Amendment 5 | Does the skill ask Claude to conceal its actions or bypass oversight? |
| Part 2, Amendment 1 | Does the skill instruct Claude to fabricate, omit, or mislead? |
| Part 2, Amendment 4 | Does the skill handle or transmit private or sensitive data? |
| Part 2, Amendment 5 | Does the skill produce auditable, attributable outputs? |
| Part 2, Amendment 7 | Does the skill respect attribution — does it claim authorship for work it did not originate? |
| Part 4, Amendment 1 | Does the skill ask Claude to act beyond its defined authority? |

Any constitutional violation is a **hard reject**. Document the specific article violated.

```
[ ] Part 1 — no oversight bypass
[ ] Part 2, Amendment 1 — no deception or omission
[ ] Part 2, Amendment 4 — no unauthorized data handling
[ ] Part 2, Amendment 5 — outputs are attributable
[ ] Part 2, Amendment 7 — attribution respected
[ ] Part 4, Amendment 1 — no authority overreach
```

---

## 4. Phase 3 — Risk Classification

Based on Phases 1–2, assign a risk level using the table in `docs/approved-skills.md §4`.

Skills classified **Medium or above** proceed to Phase 4 (sandboxed execution).
Skills classified **Low** may be approved after Phases 1–2 with Operator sign-off — execution testing is recommended but not mandatory.
Skills with any **hard reject** flag do not proceed. Document in §6 (Rejected Skills) of `docs/approved-skills.md`.

**Script-backed skills are classified at minimum Medium regardless of prompt-layer findings.** Python execution with external packages cannot be classified Low.

---

## 5. Phase 4 — Sandboxed Execution

**Goal**: Observe what the skill actually does in an isolated environment.
**Required**: Sandbox setup per §7. No real credentials or sensitive data in scope.

Pure-prompt skills use the git worktree sandbox (§7.1). Script-backed skills use the Python venv sandbox (§7.2) in addition to the worktree.

### 5.1 Pre-execution baseline

```bash
SKILL=skill-name  # set this before running

# Record filesystem state before execution
touch /tmp/skill-sandbox-baseline-${SKILL}
find /tmp/skill-sandbox-${SKILL} -type f | sort > /tmp/before-state-${SKILL}.txt
ls -la /tmp/skill-sandbox-${SKILL}/
```

### 5.2 Execution

Run the skill in the sandbox with a controlled, synthetic input. Observe:
- Every tool call Claude makes during execution
- Every file read, written, or modified
- Every network call attempted
- Every subprocess spawned via Bash

**Do not provide real credentials, tokens, API keys, or personal data during sandbox testing.**

Use synthetic stand-ins:
```
API key:   sk-test-0000000000000000000000000000000000000000000000
Password:  test-password-sandbox
Email:     sandbox@test.local
```

### 5.3 Script execution monitoring (script-backed skills)

Run scripts with observation tooling in order of thoroughness:

**Option A — strace (most thorough, Linux)**

Captures every file open, network connection, and write at the OS level. Available on Ubuntu without root.

```bash
strace -e trace=openat,open,creat,write,connect,sendto,recvfrom \
  -o /tmp/skill-trace-${SKILL}.log \
  python3 /tmp/skill-sandbox-${SKILL}/scripts/[script].py [synthetic_input]

# Review the trace
grep -E "openat|connect|sendto" /tmp/skill-trace-${SKILL}.log | head -50
```

**Option B — Network isolation (Linux user namespaces)**

Runs the script without network access. Any network call will fail with "Network unreachable" — confirms whether the script actually tries to phone home.

```bash
# Test if unshare is available
unshare --net echo "network namespaces available"

# Run script without network
unshare --net python3 /tmp/skill-sandbox-${SKILL}/scripts/[script].py [synthetic_input]
```

**Option C — Baseline comparison (always run this)**

```bash
python3 /tmp/skill-sandbox-${SKILL}/scripts/[script].py [synthetic_input]

# What files changed?
find /tmp/skill-sandbox-${SKILL} -newer /tmp/skill-sandbox-baseline-${SKILL} -type f
```

Run Options A and B if available. Always run Option C. If A and B are unavailable, note it in the review record and increase scrutiny of static analysis findings.

### 5.4 Post-execution comparison

```bash
# What changed?
find /tmp/skill-sandbox-${SKILL} -newer /tmp/skill-sandbox-baseline-${SKILL} -type f | sort > /tmp/after-state-${SKILL}.txt
diff /tmp/before-state-${SKILL}.txt /tmp/after-state-${SKILL}.txt

# Check for writes outside the sandbox
find /tmp -newer /tmp/skill-sandbox-baseline-${SKILL} -type f | grep -v "skill-sandbox-${SKILL}"

# Check home directory for unexpected changes
find ~ -newer /tmp/skill-sandbox-baseline-${SKILL} -type f 2>/dev/null | head -10
```

### 5.5 Execution checklist

```
[ ] Sandbox created per §7 — no real data present
[ ] Baseline recorded before execution
[ ] Skill executed with synthetic inputs only
[ ] All tool calls observed and match static analysis prediction
[ ] No unexpected file writes outside stated scope
[ ] No network calls to unexpected domains
[ ] No writes to governance documents
[ ] Post-execution comparison clean — no residual state outside sandbox
[ ] Sandbox torn down per §7
[ ] (Script-backed) strace log reviewed if available
[ ] (Script-backed) Network isolation test run if available
[ ] (Script-backed) No unexpected processes spawned (check with ps during execution)
```

---

## 6. Phase 5 — Approval Decision

Compile findings from all phases into a review record:

```markdown
## Skill Review: [Skill Name]

**Source**: [URL or origin]
**Skill type**: [pure-prompt / script-backed]
**Date reviewed**: YYYY-MM-DD
**Reviewed by**: [Name] + [model-id]
**Risk classification**: [Low / Low-Medium / Medium / High]
**Dependency chain**: [none / depends on: skill-name (status)]

### Static Analysis
[Findings — tools used, file scope, network calls, injection scan result]

### Script Analysis (script-backed only)
[Package list and review status, file ops, network calls, shell exec findings]

### Package Review Status (script-backed only)
[List each package, its tier, and its status in docs/package-review.md]

### Constitutional Review
[Pass / Fail per article — note any concerns even if not a hard reject]

### Execution Test
[What happened — matches or deviates from static analysis?]
[strace findings if available]
[Network isolation result if available]

### Decision
[ ] Approved — add to docs/approved-skills.md §2
[ ] Approved with caveats — note caveats in approved-skills.md
[ ] Rejected — add to docs/approved-skills.md §6 with reason
[ ] Deferred — needs further review, add to §5 with notes

**Operator sign-off**: Joshua Alexander Clement
```

The Operator must give explicit approval before a skill is moved from §5 (Under Review) to §2 (Approved) in `docs/approved-skills.md`.

---

## 7. Sandbox Setup and Teardown

### 7.1 Prompt-skill Sandbox (git worktree)

**Setup**

```bash
SKILL=skill-name  # set before running

# Create isolated worktree on a throwaway branch
git worktree add /tmp/skill-sandbox-${SKILL} -b test/skill-${SKILL}

# Create synthetic test data — no real content
mkdir -p /tmp/skill-sandbox-${SKILL}/test-data
echo "Synthetic test file — no real data" > /tmp/skill-sandbox-${SKILL}/test-data/sample.md

# Set baseline timestamp
touch /tmp/skill-sandbox-baseline-${SKILL}

# Confirm no sensitive files are in scope
ls -la /tmp/skill-sandbox-${SKILL}/
```

**During testing**
- Work only within `/tmp/skill-sandbox-${SKILL}/`
- If the skill attempts to access paths outside this directory, stop immediately — that is a finding
- If the skill attempts a network call with real data, stop immediately

**Teardown**

```bash
# Remove the worktree
git worktree remove /tmp/skill-sandbox-${SKILL} --force

# Delete the test branch
git branch -D test/skill-${SKILL}

# Clean up temp files
rm -f /tmp/before-state-${SKILL}.txt /tmp/after-state-${SKILL}.txt
rm -f /tmp/skill-sandbox-baseline-${SKILL}
```

### 7.2 Script Sandbox (Python venv)

Used for script-backed skills in addition to the git worktree sandbox.

**Setup**

```bash
SKILL=skill-name  # set before running

# Verify Python version
python3 --version  # note in review record

# Create isolated virtual environment — no system packages
python3 -m venv /tmp/skill-venv-${SKILL} --without-pip
/tmp/skill-venv-${SKILL}/bin/python -m ensurepip

source /tmp/skill-venv-${SKILL}/bin/activate

# Install only the skill's declared packages — no extras, no cache
pip install [package1] [package2] --no-cache-dir --quiet

# Record exact versions installed
pip freeze > /tmp/skill-venv-${SKILL}/requirements-frozen.txt
cat /tmp/skill-venv-${SKILL}/requirements-frozen.txt

# Create synthetic test data
mkdir -p /tmp/skill-sandbox-${SKILL}/test-data
echo "Synthetic test input — no real data" > /tmp/skill-sandbox-${SKILL}/test-data/sample.md

# Set baseline timestamp (shared with git worktree if both used)
touch /tmp/skill-sandbox-baseline-${SKILL}

# Verify the venv cannot see sensitive home directory files
python3 -c "import os; print([f for f in os.listdir(os.path.expanduser('~')) if 'key' in f.lower() or 'secret' in f.lower() or 'token' in f.lower()])"
# Expected: [] — if not empty, do not proceed until you understand the exposure
```

**During testing**

```bash
# Check if strace is available
which strace && strace --version | head -1

# Check if network namespaces are available
unshare --net echo "OK" 2>&1

# Run with strace if available
strace -e trace=openat,creat,write,connect,sendto \
  -o /tmp/skill-trace-${SKILL}.log \
  python3 /tmp/skill-sandbox-${SKILL}/scripts/[script].py [synthetic_input] 2>&1

# OR with network isolation if strace unavailable
unshare --net python3 /tmp/skill-sandbox-${SKILL}/scripts/[script].py [synthetic_input]

# OR baseline only
python3 /tmp/skill-sandbox-${SKILL}/scripts/[script].py [synthetic_input]
```

**Teardown**

```bash
# Deactivate venv
deactivate

# Remove venv and sandbox data
rm -rf /tmp/skill-venv-${SKILL}
rm -rf /tmp/skill-sandbox-${SKILL}
rm -f /tmp/before-state-${SKILL}.txt /tmp/after-state-${SKILL}.txt
rm -f /tmp/skill-sandbox-baseline-${SKILL}
rm -f /tmp/skill-trace-${SKILL}.log
```

---

## 8. Red Flag Reference

Quick reference for findings that trigger an immediate stop and hard reject:

### Prompt-layer red flags

| Red Flag | Action |
|---|---|
| Skill reads or writes `memory/constitution.md` | Hard reject |
| Skill reads or writes any `standards/STD*.md` | Hard reject |
| Skill reads or writes `.claude/` or `~/.claude/` config | Hard reject |
| Skill sends file contents to an external URL | Hard reject |
| Skill contains "ignore previous instructions" or equivalent | Hard reject |
| Skill requests elevated permissions or additional tool access | Hard reject |
| Skill's actual tool calls don't match its stated purpose | Hard reject |
| Skill constructs network URLs dynamically from session context | Hard reject |
| Skill writes outside the working directory | Hard reject |
| Skill spawns persistent background processes | Hard reject |
| Hook grants `Bash(*)` blanket shell permission | Hard reject |

### Script-layer red flags

| Red Flag | Action |
|---|---|
| Script uses `eval()` or `exec()` with dynamic/user-supplied content | Hard reject |
| Script constructs shell commands from user-controlled input | Hard reject |
| Script reads files from paths constructed via user input without sanitisation | Hard reject |
| Script sends file contents to an external URL | Hard reject |
| Script writes to paths outside `/tmp/` or its own working directory | Hard reject |
| Script uses an unreviewed package (not in `docs/package-review.md`) | Stop — complete §2.7 before proceeding |
| Script imports a package that is Tier 4 (Blocked) in `docs/package-review.md` | Hard reject |
| Script spawns subprocesses that themselves spawn further processes | Hard reject |
| Script accesses `~/.claude/`, `~/.ssh/`, `~/.aws/`, or credential paths | Hard reject |
| Package dependency has an unpatched critical CVE | Hard reject until patched version is available |

When a hard reject is triggered mid-execution, stop the session, tear down the sandbox, and document the finding before doing anything else.

---

## 9. Package Risk Tiers

Used in §2.7 (Package Review) and `docs/package-review.md`. Tier determines the level of scrutiny a package receives before it can be used in a vetted skill.

| Tier | Risk | Description | Requirements before use |
|---|---|---|---|
| **Standard Library** | Exempt | Python built-in modules — no pip install, no external code | None — but usage patterns still assessed in §2.6 |
| **Tier 1 — Low** | Low | Single-purpose, well-known, no network, no shell exec, stable maintenance | PyPI check + import scan only |
| **Tier 2 — Medium** | Medium | Network OR broad filesystem access; well-known and auditable | PyPI check + import scan + CVE check + Operator review |
| **Tier 3 — High** | High | Broad capabilities, complex transitive deps, security-sensitive domain | Full manual review of key source files + CVE check + Phase 4 testing + Operator sign-off |
| **Tier 4 — Block** | Blocked | Known supply chain risk, broad shell exec wrapper, or critical CVE history | Do not use — requires explicit constitutional exception |
| **Unknown** | Unclassified | Not yet in the registry — treat as Tier 3 until assessed | Complete §2.7 before the skill can proceed to Phase 4 |

**Common package classifications** (starting point — verify version-specifically):

| Package | Tier | Reason |
|---|---|---|
| `pydantic` | 1 | Validation/typing, no network, no shell |
| `jinja2` | 1 | Templating, no network, no shell |
| `tabulate` | 1 | Table formatting, no network, no shell |
| `click` | 1 | CLI argument parsing, no network, no shell |
| `rich` | 1 | Terminal output, no network, no shell |
| `faker` | 1 | Test data generation, no network, no shell |
| `colorama` | 1 | Terminal colours, no network, no shell |
| `requests` | 2 | HTTP client — network access by design |
| `httpx` | 2 | Async HTTP client — network access by design |
| `aiohttp` | 2 | Async HTTP — network access by design |
| `boto3` | 2 | AWS SDK — network + credential access |
| `pandas` | 2 | Data analysis — broad filesystem; large dep tree |
| `sqlalchemy` | 2 | DB ORM — filesystem + network depending on driver |
| `openai` | 3 | Sends data to external API; credential handling |
| `anthropic` | 3 | Sends data to external API; credential handling |
| `langchain` | 3 | Broad capabilities, complex dep tree, frequent CVEs |
| `paramiko` | 3 | SSH client — high-privilege network access |
| `cryptography` | 3 | Sensitive domain — must verify correct usage |
| `fabric` | 4 | Shell execution wrapper — hard block |

---

## 10. Dependency Chain Analysis

Some skills depend on other skills to function. A skill that depends on a rejected skill cannot be approved as-is.

### 10.1 Identifying dependencies

Look for:
- Explicit invocation syntax (`[INVOKE:skill-name]` or `/skill-name` in the SKILL.md body)
- References to shared context files that another skill manages (e.g., "Load the context from `memory/company-context.md` managed by `/ctx`")
- Shared state files read or written by multiple skills

### 10.2 Dependency states

| Dependency state | Meaning | Action |
|---|---|---|
| **Dependency approved** | The skill it depends on is in §2 of the registry | No blocker — note the dependency in the review record |
| **Dependency under review** | Dependency is in §5, not yet approved | Current skill cannot be approved until the dependency is — mark as blocked |
| **Dependency rejected** | Dependency is in §6 | Current skill must be adapted to remove the dependency OR rejected alongside it |
| **No dependency** | Skill operates standalone | Note "none" in the review record |

### 10.3 Documenting dependency chains

In `docs/approved-skills.md §5`, every skill entry should note its dependency chain in the Notes field:

```
Dependency chain: depends on ctx (approved) — loads memory/company-context.md
Dependency chain: none
Dependency chain: depends on context-engine (REJECTED) — blocked until adapted
```

---

## Revision History

| Rev | Date | Author | Model | Why |
|---|---|---|---|---|
| 1.0 | 2026-03-12 | Joshua Alexander Clement | claude-sonnet-4-6 | Initial creation — full vetting workflow for external Claude Code skills |
| 2.0 | 2026-03-12 | Joshua Alexander Clement | claude-sonnet-4-6 | Major extension for script-backed skills: added §2.5 Hook Analysis, §2.6 Script Analysis, §2.7 Package Review Gate, §2.8 unified checklist; extended Phase 4 with strace + network namespace isolation; added Python venv sandbox to §7.2; added script-layer red flags to §8; added §9 Package Risk Tiers; added §10 Dependency Chain Analysis |
