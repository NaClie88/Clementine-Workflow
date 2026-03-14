# Phase 4 Sandbox Testing — Docker Procedure

**Type**: Reference Document
**Status**: Ratified
**Applies to**: `docs/skill-vetting-workflow.md` §4 (Phase 4)

---

## Purpose

Phase 4 sandboxed execution confirms that a skill's runtime behaviour matches what code review found in Phase 1–3. It is not a substitute for code review — it is a final confirmation that the skill cannot exceed its approved scope when run.

This document defines the standard Docker-based procedure for Phase 4. Docker Desktop is the approved runtime.

---

## 1. When Phase 4 Applies

| Skill type | Phase 4 required? | Reason |
|---|---|---|
| Pure-prompt (no scripts) | **No** | Nothing to execute; characterised fully by reading |
| Script-backed, stdlib-only, no network, fully code-reviewed | **No** | Code review is sufficient; sandbox confirms what is already known |
| Script-backed with network calls (urllib, requests, httpx) | **Yes** | Confirm network scope is limited to approved targets |
| Script-backed with subprocess calling external binaries | **Yes** | Confirm blast radius — what processes and paths the binary can reach |
| skill-tester (executes other scripts) | **Yes** | Executes arbitrary code; cannot be characterised by reviewing its own source |
| Any skill where code review was incomplete | **Yes** | Runtime verification covers what was missed |

When in doubt, run it. The cost is low.

---

## 2. Network Policy

**Default: `--network none`**

No outbound network access unless explicitly approved for that skill. Network access is granted on an as-needed basis, per skill, with an individual decision recorded before Phase 4 runs.

### Requesting a network exception

Before running Phase 4 with network enabled, the following must be documented in `docs/approved-skills.md` for the skill under review:

1. **Target host(s)** — exact domain(s) the skill connects to (e.g. `example.com`)
2. **Protocol and method** — HTTP GET only? POST? What port?
3. **What is sent** — URL path and query params; any request body
4. **What is returned** — response structure; whether it contains user data
5. **Why network is required** — what the skill cannot do without it

Only connect to the specific approved host(s). Use `--add-host` to restrict to a known IP where possible, or scope a custom Docker network to a single external endpoint.

### Network modes used in this document

| Mode | Docker flag | When used |
|---|---|---|
| No network | `--network none` | Default for all Phase 4 runs |
| Host-restricted | `--network none` + upstream proxy or `--add-host` | URL-fetching skills with approved host |
| Full outbound | not used | Never — not an approved mode |

---

## 3. Standard Container Configuration

All Phase 4 runs use this base configuration unless a skill-specific exception is documented.

```bash
docker run --rm \
  --network none \
  --read-only \
  --tmpfs /tmp:rw,size=64m,mode=1777 \
  --cap-drop ALL \
  --security-opt no-new-privileges \
  -v /path/to/skill:/skill:ro \
  python:3.11-slim \
  python /skill/scripts/<script_name>.py [args]
```

**Flags explained:**

| Flag | What it does |
|---|---|
| `--rm` | Container removed after exit — no state persists |
| `--network none` | No network access |
| `--read-only` | Root filesystem is read-only |
| `--tmpfs /tmp:rw,size=64m` | Only writable location is `/tmp`, capped at 64 MB |
| `--cap-drop ALL` | Drops all Linux capabilities (no raw sockets, no mount, no chown, etc.) |
| `--security-opt no-new-privileges` | Prevents privilege escalation via setuid binaries |
| `-v /path/to/skill:/skill:ro` | Mounts the skill directory read-only |

If a skill writes output to a project path (not stdout), mount an output volume:

```bash
-v /path/to/output:/output:rw
```

And confirm in the test that writes go to `/output/` and not to `/tmp/` when that is the intended destination.

---

## 4. Test Procedures by Category

### 4.1 skill-tester

`script_tester.py` has no built-in sandbox — it runs tested scripts via `subprocess.run()` with `cwd=script_path.parent` and no path restrictions. The container boundary is the only sandbox.

**Static-mode use (safe in-session, no Docker required):**
`--help`, syntax checks, import checks, argparse checks, main guard checks — these use `ast.parse()` only. Safe to run directly in a Claude session.

**Execution-mode use (Docker required):**
`_test_script_execution`, `_test_help_functionality`, `_test_sample_data_processing`, `_test_output_formats` — these call `subprocess.run()` on the target script. Only run inside the container.

**Procedure:**

```bash
# 1. Mount the skill under test and the skill-tester itself
docker run --rm \
  --network none \
  --read-only \
  --tmpfs /tmp:rw,size=64m,mode=1777 \
  --cap-drop ALL \
  --security-opt no-new-privileges \
  -v /tmp/claude-skills/engineering/skill-tester:/skill-tester:ro \
  -v /tmp/claude-skills/<target-skill>:/target:ro \
  python:3.11-slim \
  python /skill-tester/scripts/script_tester.py /target --verbose

# 2. Canary test — confirm a write outside /tmp/ is blocked
# Place a canary script in /tmp/ before the run:
cat > /tmp/canary.py << 'EOF'
import pathlib
# Attempt write outside /tmp/
try:
    pathlib.Path("/home/canary.txt").write_text("escaped")
    print("FAIL: wrote outside /tmp/")
except (PermissionError, OSError):
    print("PASS: write outside /tmp/ blocked")
# Confirm /tmp/ write works
pathlib.Path("/tmp/canary_ok.txt").write_text("ok")
print("PASS: /tmp/ write succeeded")
EOF

docker run --rm \
  --network none \
  --read-only \
  --tmpfs /tmp:rw,size=64m,mode=1777 \
  --cap-drop ALL \
  --security-opt no-new-privileges \
  -v /tmp/canary.py:/canary.py:ro \
  python:3.11-slim \
  python /canary.py
```

**Pass criteria:**
- Canary write to `/home/` gets `PermissionError`
- Canary write to `/tmp/` succeeds
- skill-tester runs against a target skill without errors
- No files appear outside `/tmp/` after the run

---

### 4.2 URL-fetching skills (page-cro, seo-audit, site-architecture)

These use `urllib.request.urlopen()` to fetch from a user-provided URL. Phase 4 confirms the fetch is GET-only and no data is written back to an unintended location.

**Approved network scope for these skills:** HTTP/HTTPS GET to operator-owned domains only (documented per invocation — no fixed host to lock down here).

**Procedure:**

```bash
# Run without network — script should fail cleanly with a connection error,
# not crash or attempt writes
docker run --rm \
  --network none \
  --read-only \
  --tmpfs /tmp:rw,size=64m,mode=1777 \
  --cap-drop ALL \
  --security-opt no-new-privileges \
  -v /tmp/claude-skills/<skill>/scripts:/scripts:ro \
  python:3.11-slim \
  python /scripts/<script>.py --url https://example.com
```

**Pass criteria:**
- With `--network none`: script exits with a `urllib.error.URLError` or similar network error — it does not hang, does not crash with an unhandled exception, and does not attempt writes
- Script output (if any) goes to stdout only — no unexpected files written

**For live testing against an approved URL (operator-owned):**
Run the same command but use a custom Docker network that permits outbound to that specific host. Document the target URL in the Phase 4 record.

---

### 4.3 subprocess skills (prompt-engineer-toolkit, senior-backend api_load_tester)

**prompt-engineer-toolkit `--runner-cmd`:**

```bash
docker run --rm \
  --network none \
  --read-only \
  --tmpfs /tmp:rw,size=64m,mode=1777 \
  --cap-drop ALL \
  --security-opt no-new-privileges \
  -v /tmp/claude-skills/marketing-skill/prompt-engineer-toolkit:/skill:ro \
  python:3.11-slim \
  python /skill/scripts/prompt_tester.py \
    --runner-cmd "python -c 'print(\"{prompt}\")'" \
    --prompts "hello" \
    --inputs "world"
```

**Pass criteria:** Command executes only the fixed template; no filesystem writes; output is the rendered prompt only.

**senior-backend `api_load_tester.py`:**

```bash
# Confirm --no-verify-ssl does not bypass container network isolation
docker run --rm \
  --network none \
  --read-only \
  --tmpfs /tmp:rw,size=64m,mode=1777 \
  --cap-drop ALL \
  --security-opt no-new-privileges \
  -v /tmp/claude-skills/engineering-team/senior-backend/scripts:/scripts:ro \
  python:3.11-slim \
  python /scripts/api_load_tester.py --url https://httpbin.org/get --requests 1
```

**Pass criteria:** With `--network none`, fails with connection error. No writes outside `/tmp/`.

---

## 5. Pass / Fail Criteria (all tests)

| Check | Pass | Fail |
|---|---|---|
| Filesystem writes | Only to `/tmp/` or approved mounted output volume | Any write to `/home/`, `/root/`, `/etc/`, or unmounted paths |
| Network calls | None (or only to approved host if network exception granted) | Any outbound connection attempt when `--network none` is set |
| Process spawning | Only the approved subprocess pattern from code review | Additional unexpected child processes |
| Exit behaviour | Exits cleanly (0, 1, or 2) within timeout | Hangs, segfault, or unhandled exception crash |
| Container state | No files persist after `--rm` | (cannot fail — Docker handles this) |

---

## 6. Recording Phase 4 Results

After a successful Phase 4 run, update the skill's entry in `docs/approved-skills.md`:

1. Change status from `Phase 4 pending` to `**Approved**` or `**Approved with caveat**`
2. Add to the Notes column: `Phase 4 Docker sandbox passed YYYY-MM-DD`
3. Note the Docker flags used and any network exception granted
4. Add a revision history entry to `docs/approved-skills.md`

Example note addition:
```
Phase 4 Docker sandbox passed 2026-03-13 (--network none, --read-only, --tmpfs /tmp).
Canary confirmed writes blocked outside /tmp/.
```

---

## 7. Adding a New Skill to Phase 4

When a new script-backed skill reaches Phase 4:

1. Determine which category it falls into (§1)
2. If network is needed, document the exception per §2 before running
3. Use the standard container config (§3) as the base
4. Run the appropriate procedure from §4, or adapt it for the skill's specific tool
5. Add a canary test if the skill has significant subprocess or filesystem activity
6. Record results per §6

---

## Revision History

| Rev | Date | Author | Model | Why |
|---|---|---|---|---|
| 1.0 | 2026-03-13 | Joshua Alexander Clement | claude-sonnet-4-6 | Initial document. Covers skill-tester, URL-fetching skills, subprocess skills. Network policy: default none, per-skill opt-in. Informed by full read of script_tester.py (no built-in sandbox — Docker is the only isolation boundary). |
