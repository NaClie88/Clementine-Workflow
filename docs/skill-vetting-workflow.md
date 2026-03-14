# Skill Vetting Workflow

**Type**: Reference Document
**Status**: Ratified
**Constitutional Authority**: `memory/constitution.md` Part 1, Amendment 5 (No Undermining Oversight), Part 5, Amendment 5 (Accountability)

---

## Purpose

Defines the process for reviewing, testing, and approving Claude Code skills from external or unverified sources before they are added to `docs/approved-skills.md`. A skill that has not completed this workflow is treated as unapproved regardless of its apparent quality or source reputation.

Skills are either **pure-prompt** (SKILL.md only — no scripts) or **script-backed** (includes Python, shell, or TypeScript/JavaScript scripts). The workflow covers both. Script-backed skills require additional phases — §2.6 (Script Analysis), §2.7 (Package Review), and the execution sandbox in §7.2–7.3.

---

## Contents
1. [Threat Model](#1-threat-model)
2. [Phase 1 — Static Analysis](#2-phase-1--static-analysis)
   - [§2.0 Full File Inventory](#20-full-file-inventory)
   - [§2.1 Tool Inventory](#21-tool-inventory)
   - [§2.2 File Scope Analysis](#22-file-scope-analysis)
   - [§2.3 Network Scope Analysis](#23-network-scope-analysis)
   - [§2.4 Prompt Injection Scan](#24-prompt-injection-scan)
   - [§2.5 Hook and Injection Analysis](#25-hook-and-injection-analysis) (hooks.json, settings.json, .sh scripts, CLAUDE.md, MCP config, plugin.json, agents/)
   - [§2.6 Script Analysis — Python](#26-script-analysis-script-backed-skills-only)
   - [§2.6b Script Analysis — TypeScript/JavaScript](#26b-typescriptjavascript-script-analysis-if-tsjs-files-present)
   - [§2.7 Package Review Gate — Python](#27-package-review-gate-script-backed-skills-only)
   - [§2.7b Package Review Gate — npm](#27b-npm-package-review-gate-typescriptjavascript-skills-only)
   - [§2.8 Static Analysis Checklist](#28-static-analysis-checklist)
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

### 2.0 Full File Inventory

**Before any analysis begins, enumerate every file in the skill directory.** Do not proceed to §2.1 until this inventory is complete. Approval cannot be granted for a skill unless every file in this list has been read.

```bash
find [skill-dir] -type f | sort
```

Record the results in your review document. Categorise each file:

| Category | Files to look for | Covered in |
|---|---|---|
| Skill definition | `SKILL.md` | §2.1–2.4 |
| Session injection | `CLAUDE.md` | §2.5 |
| Hook config | `hooks.json`, `settings.json` | §2.5 |
| Shell hook scripts | `*.sh` (any depth) | §2.5 |
| Python scripts | `*.py` (any depth) | §2.6 |
| TypeScript/JavaScript | `*.ts`, `*.js`, `*.mjs` (any depth) | §2.6b |
| npm config | `package.json`, `package-lock.json` | §2.7b |
| MCP config | `.mcp.json`, `mcp.json` | §2.5, §2.6b |
| Sub-skills | `skills/` directory | §2.0 — recursive inventory |
| Agent definitions | `agents/` directory | §2.5, §2.6b |
| Plugin config | `plugin.json` | §2.5 |
| Templates/reference | `templates/`, `docs/` inside skill | Note — usually inert |

If the skill contains a `skills/` subdirectory with nested skills, run the inventory recursively and treat each sub-skill as a separate skill for analysis purposes.

**Stop before §2.1 if SKILL.md is absent.** A skill directory without SKILL.md is an unstructured code drop — it is not a reviewable skill.

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

### 2.5 Hook and Injection Analysis

This section covers every file that executes automatically or injects instructions into Claude sessions. These files carry outsized risk because they act without explicit Operator invocation.

#### 2.5.1 CLAUDE.md (if present)

A `CLAUDE.md` inside a skill package is **more powerful than SKILL.md**. It loads unconditionally into every Claude session in the directory, regardless of whether the skill was explicitly invoked.

Read the entire file. Check for:
- Override instructions, persona replacement, or constitution bypass patterns (see §2.4)
- Instructions that expand the skill's effective scope beyond what SKILL.md describes
- References to external URLs or services not declared in SKILL.md
- Any instruction that contradicts the constitution or this workflow

A CLAUDE.md containing override or bypass language is a **hard reject** under §2.4 rules, with the additional severity that it fires on every session, not just on explicit skill invocation.

#### 2.5.2 hooks.json and settings.json (if present)

- What events trigger each hook? (`PostToolUse`, `SessionStart`, `PreToolUse`, etc.)
- Does the hook have a matcher that scopes it to specific tools or patterns?
- Does `settings.json` pre-grant Bash permissions? What scope?

A `PostToolUse` hook with no event type matcher (fires on every tool use) is a **hard reject**. Pre-granted Bash permissions with broad wildcards (`Bash(*)`) are a **hard reject**. Scoped patterns (`Bash(npx playwright*)`) require Operator review and explicit approval.

#### 2.5.3 Shell scripts (if present)

For **every `.sh` file** referenced in hooks.json or present anywhere in the skill directory:

- Read the entire script.
- What does it do? Summarise in plain terms.
- Does it write to any files? Which paths?
- Does it make network calls?
- Does it call external commands (`curl`, `wget`, `ssh`, `scp`, `rsync`)?
- Is any user-controlled input passed to shell commands without validation?

A shell script is executed code, not documentation. Read it all — the one function you skip is the one that matters.

#### 2.5.4 MCP server config (.mcp.json, mcp.json) (if present)

MCP servers are persistent processes registered to Claude that expose tools beyond Claude's built-in set.

- What servers are registered? List each by name.
- What runtime is used? (`npx tsx`, `node`, `python`, etc.)
- What entry point file does each server start? Note the path.
- What environment variables does each server require? Are they credentials?
- Does the server fail fast if credentials are absent, or does it proceed without auth?

The MCP server source files identified here are analysed in §2.6b.

#### 2.5.5 plugin.json (if present)

Some skills ship a `plugin.json` for third-party tool integrations. Read the file and document:
- What external services are connected?
- What permissions or OAuth scopes are requested?
- Are credentials stored locally or transmitted to an external service?

#### 2.5.6 agents/ directory (if present)

If the skill includes an `agents/` subdirectory:
- What agents are defined?
- What tools do they invoke?
- Do they operate autonomously on any trigger, or only on explicit invocation?
- Do they access shared state files, configuration, or credentials?

Autonomous agents that run without explicit Operator invocation at each step are a **hard reject** unless the skill documentation explicitly describes and limits the autonomy scope.

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

### 2.6b TypeScript/JavaScript Script Analysis (if .ts/.js/.mjs files present)

Applies to any skill containing TypeScript, JavaScript, or MJS files — including MCP server source identified in §2.5.4. Structure mirrors §2.6 for consistency.

Run `/vet-skill [path]` — it will flag TS/JS files for manual review (the tool covers Python only; TS/JS analysis is manual).

#### 2.6b.1 Import/Require Inventory

Extract every import and require statement:

```bash
grep -rn "^import\|require(" [skill-dir]/**/*.{ts,js,mjs} | sort
```

For each package:
- Is it an npm package or a Node.js built-in?
- Cross-reference against `docs/npm-package-review.md` (see §2.7b). Flag any package not listed as **unreviewed**.

Node.js built-ins (`fs`, `path`, `os`, `child_process`, `net`, `http`, `https`, `crypto`, `stream`, `util`, `events`, `url`, `buffer`, `assert`, `readline`) do not require npm review — but their usage is assessed in §2.6b.2–2.6b.4.

#### 2.6b.2 File Operation Analysis

Scan for file system access:

```bash
grep -n "fs\.\|readFile\|writeFile\|appendFile\|mkdir\|unlink\|rename\|copyFile\|createReadStream\|createWriteStream" [file].ts
```

For each finding:
- What path is accessed — hardcoded constant or constructed from input?
- Read or write mode?
- Can a user-controlled value reach the path argument? (path traversal risk)

Flag any writes outside the skill's own directory or `/tmp/`.

#### 2.6b.3 Network Call Analysis

Scan for HTTP and network access:

```bash
grep -n "fetch(\|axios\.\|got\.\|http\.request\|https\.request\|WebSocket\|createConnection" [file].ts
```

For each finding:
- What URL/host is called?
- Is the URL hardcoded or constructed from user input?
- What data is sent in the request body or query string?
- Are any local file contents or environment variables transmitted?

A script that sends file contents or environment variables to an external URL is a **hard reject**.

#### 2.6b.4 Shell Execution Analysis

Scan for subprocess and eval patterns:

```bash
grep -n "exec(\|execSync\|spawn\|spawnSync\|execFile\|child_process\|eval(\|new Function(" [file].ts
```

For each finding:
- What command is run?
- Is the command string or any argument constructed from user-controlled input?
- Is `shell: true` used with variable interpolation?

Shell commands constructed from unvalidated user input are a **hard reject**. `eval()` or `new Function()` receiving user-controlled input is a **hard reject**.

#### 2.6b.5 Environment Variable Access

TypeScript/JavaScript files frequently read environment variables for credentials. This is expected for MCP servers — but must be documented.

```bash
grep -n "process\.env\." [file].ts
```

For each `process.env.X` reference:
- What credential or configuration does it read?
- Is it only read, or is it transmitted outward (network call, logged to file)?
- Does the script fail gracefully if the variable is absent, or does it proceed silently with undefined?

A script that transmits `process.env` values to external hosts is a **hard reject**.

#### 2.6b.6 Data Flow Summary

For each TS/JS file, summarise:
- What inputs it accepts (CLI args, stdin, env vars, API calls)
- What outputs it produces (files written, network calls, stdout)
- Whether any sensitive values (credentials, file contents) flow to external destinations

### 2.7 Package Review Gate (script-backed skills only)

After §2.6.1 import inventory, for every package not already in `docs/package-review.md`:

1. Look up the package on PyPI — note author, version history, download count
2. Check for known CVEs: `pip audit --require-hashes` (if pip-audit is available) or manually check the PyPI security advisories page
3. Review the package's own imports — does it pull in unexpected transitive dependencies?
4. Classify the package using §9 (Package Risk Tiers)
5. Add it to `docs/package-review.md` with findings

**A skill cannot proceed to Phase 4 until all its packages are in `docs/package-review.md`.**

### 2.7b npm Package Review Gate (TypeScript/JavaScript skills only)

After §2.6b.1 import inventory, for every npm package not already in `docs/npm-package-review.md`:

1. Check `package.json` for the declared version range — note whether it is pinned (`"1.2.3"`), range-pinned (`"^1.2.3"`), or floating (`"*"`, `"latest"`)
2. Look up the package on npmjs.com — note maintainers, weekly downloads, last publish date
3. Check for known CVEs: `npm audit` in the skill's directory, or check the npm security advisories page
4. Review the package's own `package.json` — what does it depend on transitively?
5. Classify the package using the npm package tiers below
6. Add it to `docs/npm-package-review.md` with findings

**npm Package Risk Tiers:**

| Tier | Description | Examples | Requirements |
|---|---|---|---|
| **Built-in** | Node.js built-in modules | `fs`, `path`, `os`, `child_process`, `crypto` | None — but usage patterns assessed in §2.6b |
| **Tier 1 — Low** | Single-purpose, well-known, narrow scope, stable | `zod`, `chalk`, `commander`, `dotenv`, `date-fns` | npm check + usage scan only |
| **Tier 2 — Medium** | Network OR broad filesystem; well-known | `axios`, `got`, `node-fetch`, `@modelcontextprotocol/sdk` | npm check + CVE audit + Operator review |
| **Tier 3 — High** | Broad capabilities, credential handling, large dep tree | `openai`, `@anthropic-ai/sdk`, `puppeteer`, `playwright` | Full source review of key files + CVE audit + Phase 4 testing + Operator sign-off |
| **Tier 4 — Block** | Known supply chain risk, shell execution wrapper, or critical CVE history | (evaluate case-by-case) | Do not use — requires explicit constitutional exception |
| **Unknown** | Not yet in `docs/npm-package-review.md` | Any package not yet assessed | Complete §2.7b before skill can proceed to Phase 4 |

**Floating version ranges are a flag.** `"*"` or `"latest"` means the package version is not reproducible — a malicious update could alter the skill's behaviour between installs. Require pinned or narrow-range versions before Phase 4.

**A skill with TypeScript/JavaScript cannot proceed to Phase 4 until all its npm packages are in `docs/npm-package-review.md`.**

### 2.8 Static Analysis Checklist

**For all skills:**
```
[ ] §2.0 File inventory complete — every file in the skill directory listed and categorised
[ ] Every file in the inventory has been read — no file approved unseen
[ ] CLAUDE.md reviewed if present — no override/bypass language
[ ] Tool inventory complete — all tools identified and listed
[ ] File scope documented — all read/write paths noted
[ ] No access to governance documents (memory/, standards/, .claude/)
[ ] Network calls identified — URLs and data sent documented
[ ] No project data sent to external URLs
[ ] Prompt injection scan complete — no override patterns found
[ ] Skill does what it claims and only what it claims
[ ] Source noted — where did this skill come from?
[ ] hooks.json reviewed if present — event types, matchers, scope
[ ] settings.json reviewed if present — pre-granted permissions documented
[ ] Every .sh hook script read in full — file ops, network calls, shell exec documented
[ ] MCP config reviewed if present — servers listed, entry points identified
[ ] plugin.json reviewed if present — external services and permissions documented
[ ] agents/ directory reviewed if present — autonomy scope documented
[ ] Sub-skills inventoried if present — each treated as a separate skill for analysis
```

**Additional for Python script-backed skills:**
```
[ ] Python import inventory complete — all packages listed
[ ] All packages checked against docs/package-review.md
[ ] No unreviewed Python packages (or unreviewed packages explicitly queued for §2.7)
[ ] File operations documented — paths, modes, construction methods
[ ] No file writes outside skill working directory or /tmp/
[ ] Network calls documented — URLs and request bodies identified
[ ] No project data in network requests
[ ] No shell execution with user-controlled arguments
[ ] No eval() or exec() with dynamic content
[ ] Data flow documented — inputs and outputs clearly understood
[ ] Dependency chain checked — does this skill depend on another? (see §10)
```

**Additional for TypeScript/JavaScript skills:**
```
[ ] npm import/require inventory complete — all packages listed
[ ] All packages checked against docs/npm-package-review.md
[ ] No unreviewed npm packages (or unreviewed packages explicitly queued for §2.7b)
[ ] No floating version ranges ("*" or "latest") without flag
[ ] MCP server source files read in full (§2.6b)
[ ] File operations documented — paths, modes, user input paths flagged
[ ] Network calls documented — URLs, request bodies, env var transmission
[ ] No shell execution with user-controlled arguments (shell: true with variables)
[ ] No eval() or new Function() with dynamic content
[ ] Environment variable access documented — no credential transmission outward
[ ] Data flow documented — inputs and outputs clearly understood
```

---

## 3. Phase 2 — Constitutional Review

**Goal**: Confirm the skill's instructions are consistent with the constitution.

Check against each Part:

| Part | Check |
|---|---|
| Part 1, Amendment 5 | Does the skill ask Claude to conceal its actions or bypass oversight? |
| Part 5, Amendment 1 | Does the skill instruct Claude to fabricate, omit, or mislead? |
| Part 5, Amendment 4 | Does the skill handle or transmit private or sensitive data? |
| Part 5, Amendment 5 | Does the skill produce auditable, attributable outputs? |
| Part 5, Amendment 8 | Does the skill respect attribution — does it claim authorship for work it did not originate? |
| Part 3, Amendment 1 | Does the skill ask Claude to act beyond its defined authority? |

Any constitutional violation is a **hard reject**. Document the specific article violated.

```
[ ] Part 1 — no oversight bypass
[ ] Part 5, Amendment 1 — no deception or omission
[ ] Part 5, Amendment 4 — no unauthorized data handling
[ ] Part 5, Amendment 5 — outputs are attributable
[ ] Part 5, Amendment 8 — attribution respected
[ ] Part 3, Amendment 1 — no authority overreach
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
**Required**: No real credentials or sensitive data in scope.

### When Phase 4 applies

| Skill type | Phase 4 required? |
|---|---|
| Pure-prompt (no scripts) | **No** — fully characterised by reading |
| Script-backed, stdlib-only, no network, fully code-reviewed | **No** — code review is sufficient |
| Script-backed with network calls | **Yes** |
| Script-backed with subprocess calling external binaries | **Yes** |
| skill-tester or any skill that executes other scripts | **Yes** |
| Any skill where code review was incomplete | **Yes** |

### Sandbox method

**Use Docker Desktop.** The full procedure, container configuration, network policy, per-category test procedures, and pass/fail criteria are in **`docs/phase4-sandbox.md`**.

The strace and Python venv approach in §7 below remains available as a fallback on systems without Docker, but Docker is the preferred and more complete isolation boundary.

**Network policy**: default `--network none`. Network access is granted per skill, as needed, with an individual decision documented before Phase 4 runs. See `docs/phase4-sandbox.md §2` for the network exception process.

Pure-prompt skills do not use the git worktree sandbox (§7.1) — they have nothing to execute. Script-backed skills requiring Phase 4 use Docker per `docs/phase4-sandbox.md` in preference to the Python venv sandbox (§7.2).

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

### Python script-layer red flags

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

### TypeScript/JavaScript red flags

| Red Flag | Action |
|---|---|
| Script uses `eval()` or `new Function()` with dynamic/user-supplied content | Hard reject |
| Script constructs shell commands from user input (`exec(userInput)`, `spawn('sh', ['-c', userInput])`) | Hard reject |
| Script passes user input to `child_process` with `shell: true` | Hard reject |
| Script transmits `process.env` values or file contents to external hosts | Hard reject |
| Script writes to paths outside `/tmp/` or its own working directory | Hard reject |
| Script uses an unreviewed npm package (not in `docs/npm-package-review.md`) | Stop — complete §2.7b before proceeding |
| Script imports a Tier 4 npm package | Hard reject |
| npm package uses a floating version range (`"*"`, `"latest"`) | Flag — require pin before Phase 4 |
| Script accesses `~/.claude/`, `~/.ssh/`, `~/.aws/`, or credential paths via `fs` | Hard reject |
| MCP server transmits credentials or file contents to non-declared external services | Hard reject |

### Hook and injection red flags

| Red Flag | Action |
|---|---|
| CLAUDE.md contains override, persona-replacement, or bypass instructions | Hard reject |
| `PostToolUse` hook with no event matcher (fires on every tool use) | Hard reject |
| `Bash(*)` blanket permission in `settings.json` | Hard reject |
| Shell hook script writes to governance files (`CLAUDE.md`, `standards/`, `.claude/`) | Hard reject |
| Shell hook script makes outbound network calls | Hard reject |
| Autonomous agent in `agents/` directory runs without explicit Operator invocation | Hard reject (unless scope is documented and bounded) |

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
| 3.0 | 2026-03-13 | Joshua Alexander Clement | claude-sonnet-4-6 | Comprehensive gap remediation after playwright-pro oversight revealed structural gaps. Added: §2.0 Full File Inventory (enumerate all files before analysis begins — approval requires every file read); expanded §2.5 into six subsections (CLAUDE.md injection analysis, hooks.json/settings.json, every .sh file in full, MCP config, plugin.json, agents/ directory); added §2.6b TypeScript/JavaScript Script Analysis (import inventory, file ops, network calls, shell exec, env var access, data flow); added §2.7b npm Package Review Gate with npm package risk tiers; updated §2.8 checklist with all new mandatory items; updated §8 with TypeScript/JS red flags and hook/injection red flags section |
