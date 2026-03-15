## Skill Review: Knowledge Base Query (kb-query)

**Source**: Internal — `knowledge-base/scripts/query.py` + `skills/kb-query/SKILL.md`
**Skill type**: Script-backed (Python)
**Date reviewed**: 2026-03-14
**Reviewed by**: Joshua Alexander Clement + claude-sonnet-4-6
**Risk classification**: Low–Medium
**Dependency chain**: none (D01 packages; standalone)

---

### Static Analysis

**§2.0 File Inventory**

| File | Category |
|---|---|
| `skills/kb-query/SKILL.md` | Skill definition |
| `knowledge-base/scripts/query.py` | Python script |

No CLAUDE.md, hooks.json, settings.json, .sh scripts, MCP config, plugin.json, or agents/ directory present.

**§2.1 Tool Inventory**

| Tool | Risk | Notes |
|---|---|---|
| `Bash` | High | Used to run `python3.12 knowledge-base/scripts/query.py "..."` |
| `Read` | Low | Used to display full entry file if user requests it |

**§2.2 File Scope Analysis**

Reads: `knowledge-base/db/lance/` (LanceDB files, project-local). No writes. The `--db-path` argument accepts a user-supplied path but the SKILL.md rules prohibit passing user input to this arg — always derived from `repo_root` constant in query.py.

**§2.3 Network Scope Analysis**

**Phase 4 finding:** `huggingface_hub` makes HTTPS calls to HuggingFace CDN (CloudFront, `143.204.130.x`, port 443) during `SentenceTransformer()` model load — even when model is cached. This is a version-check/telemetry call, not a model download. **Fix applied:** `os.environ.setdefault("TRANSFORMERS_OFFLINE", "1")` added to query.py. Post-fix strace confirms zero external connections.

No project data, credentials, or query text is transmitted externally.

**§2.4 Prompt Injection Scan**

SKILL.md reviewed — no override instructions, constitution bypass language, role replacement, or hidden instructions. Skill does exactly what it claims.

**§2.5 Hook and Injection Analysis**

No hooks, CLAUDE.md, shell scripts, MCP config, or agents directory. Not applicable.

---

### Script Analysis

**§2.6.1 Import Inventory**

| Package | Type | Registry Status |
|---|---|---|
| `argparse` | stdlib | Pre-approved |
| `json` | stdlib | Pre-approved |
| `os` | stdlib | Pre-approved |
| `sys` | stdlib | Pre-approved |
| `warnings` | stdlib | Pre-approved |
| `pathlib` | stdlib | Pre-approved |
| `lancedb` | third-party | Tier 2, APPROVED WITH CONDITIONS (added 2026-03-14) |
| `sentence_transformers` | third-party | Tier 3, APPROVED WITH CONDITIONS + Operator sign-off (added 2026-03-14) |

**§2.6.2 File Operations**

- `Path(__file__).resolve().parent.parent.parent` — derives `repo_root` from script location (fixed constant)
- `db_path = repo_root / "knowledge-base" / "db" / "lance"` — project-local, fixed path
- `db_path.exists()` — read check only
- `lancedb.connect(str(db_path))` — opens local DB (read)
- `db.open_table(TABLE_NAME)` — opens existing table (read)
- `q.to_list()` — reads results into memory

No writes. No user-controlled path construction.

**§2.6.3 Network Calls**

No direct `requests`, `httpx`, `urllib`, or `socket` calls in query.py. See §2.3 for transitive network calls via `huggingface_hub` — mitigated by `TRANSFORMERS_OFFLINE=1`.

**§2.6.4 Shell Execution**

No `subprocess`, `os.system`, `os.popen`, `eval()`, or `exec()` calls.

**§2.6.5 Data Flow Summary**

- **Inputs**: CLI args (`query`, `--domain`, `--applies-to`, `--top-k`, `--db-path`, `--json`)
- **Outputs**: stdout (formatted text or JSON)
- **Sensitive values**: none — no credentials, PII, or project file contents transmitted

---

### Package Review Status

| Package | Tier | Status |
|---|---|---|
| lancedb 0.29.2 | Tier 2 | APPROVED WITH CONDITIONS — local mode only |
| sentence-transformers 5.3.0 | Tier 3 | APPROVED WITH CONDITIONS — device="cpu", TRANSFORMERS_OFFLINE=1 |

---

### Constitutional Review

| Part | Check | Result |
|---|---|---|
| Part 1, Amendment 5 | No oversight bypass | PASS |
| Part 5, Amendment 1 | No deception or omission | PASS |
| Part 5, Amendment 4 | No unauthorized data handling | PASS — read-only, no transmission |
| Part 5, Amendment 5 | Outputs attributable | PASS — results sourced from local KB |
| Part 5, Amendment 8 | Attribution respected | PASS — entries retain theorist/year attribution |
| Part 3, Amendment 1 | No authority overreach | PASS — read-only query tool |

---

### Execution Test

**Phase 4 — Option B (network isolation):** `unshare --net` not permitted on this system.

**Phase 4 — Option A (strace network):**
- Pre-fix: HTTPS connections to `143.204.130.x:443` (HuggingFace CDN via CloudFront) on every `SentenceTransformer()` call
- Root cause: `huggingface_hub` version-checks even when model is cached
- Fix: `os.environ.setdefault("TRANSFORMERS_OFFLINE", "1")` added to query.py before imports
- Post-fix strace: zero external AF_INET connections confirmed

**Phase 4 — Option C (baseline comparison):**
- Execution: `query.py "functional programming purity" --top-k 2` — returned correct results
- `find ~ -newer baseline -type f` — only Brave browser cache files (unrelated to script)
- No writes to project directory, home directory, or /tmp beyond OS state

**Verdict**: PASS — post-fix behaviour matches static analysis prediction. Zero external network calls at runtime.

---

### Decision

**APPROVED** — added to `docs/approved-skills.md` §2 (Custom Skills) with conditions.

**Conditions:**
1. `TRANSFORMERS_OFFLINE=1` must remain set in query.py — do not remove
2. `--db-path` argument must not accept user-supplied paths in skill invocation
3. Run `embed.py` to rebuild index if DB is absent or stale

**Approved by:** Joshua Alexander Clement + claude-sonnet-4-6, 2026-03-14
