# npm Package Review Registry

All npm packages used by TypeScript/JavaScript skills in this project must be reviewed here before Phase 4 sandboxed testing begins. A package needs only one review; subsequent skills cite the review by package name.

**Last updated:** 2026-03-13
**Workflow reference:** `docs/skill-vetting-workflow.md` §2.7b

---

## How to Read This Registry

Each entry includes:
- **Version reviewed** — pinned or range version at time of review
- **Risk tier** — Built-in | Tier 1 (Low) | Tier 2 (Medium) | Tier 3 (High) | Tier 4 (Blocked) | Unknown
- **Install footprint** — direct + key transitive deps at that version
- **Capabilities** — what the package actually does that is relevant to security review
- **Concerns** — any red flags or conditions on use
- **Decision** — APPROVED | APPROVED WITH CONDITIONS | BLOCKED

---

## Tier Reference (from §2.7b of workflow)

| Tier | Risk | Description |
|---|---|---|
| Built-in | Baseline | Ships with Node.js; no install needed |
| Tier 1 — Low | Low | Single-purpose, well-known, no network, no shell exec, stable |
| Tier 2 — Medium | Medium | Network OR broad filesystem access; well-known and auditable |
| Tier 3 — High | High | Broad capabilities, credential handling, large dep tree |
| Tier 4 — Blocked | Blocked | Known supply chain risk, shell execution wrapper, or critical CVE history |
| Unknown | Unclassified | Not yet reviewed — treat as Tier 3 until assessed |

---

## Node.js Built-ins — Pre-Approved

These ship with every Node.js installation. No install required, no npm review needed. Usage patterns are still assessed in §2.6b.

| Module | Purpose | Usage notes |
|---|---|---|
| `fs` / `fs/promises` | File system read/write | Paths constructed from user input must be validated |
| `path` | Path manipulation | Pure utility — sanitise before joining with user input |
| `os` | OS information | `os.homedir()` can expose paths — flag if used to construct write targets |
| `child_process` | Subprocess execution | High risk — `exec()` / `spawn()` with user input requires hard scrutiny |
| `net` / `http` / `https` | Network access | Flag any outbound calls with dynamic URL construction |
| `crypto` | Cryptographic primitives | Flag if used to encode/obfuscate data before transmission |
| `stream` | Data streaming | Flag if streaming file contents to network destinations |
| `util` | Utility functions | Low risk in isolation |
| `events` | Event emitter | Low risk in isolation |
| `url` | URL parsing | Flag if URL constructed from user input is passed to fetch/http |
| `buffer` | Binary data handling | Flag if used with network transmission |
| `assert` | Assertion utilities | Low risk — test/validation use |
| `readline` | Line-by-line input | Low risk in isolation |
| `process` | Process info and env vars | `process.env` access must be documented; never transmit env vars outward |
| `console` | Stdout/stderr logging | Low risk — watch for credential values logged |

---

## Reviewed Packages

---

### @modelcontextprotocol/sdk

**Version reviewed:** ^1.0.0 (range-pinned)
**Tier:** Tier 2 — Medium
**Reviewed:** 2026-03-13
**Skills using this:** playwright-pro (testrail-mcp, browserstack-mcp)

**Install footprint:**
- Direct dep only — no significant transitive dependencies beyond Node built-ins
- ESM module format

**Capabilities:**
- Official Anthropic MCP SDK for building MCP servers
- Provides `Server`, `StdioServerTransport`, and schema types
- Handles the MCP protocol layer — routing tool calls, formatting responses
- Does not make outbound network calls itself; all network activity comes from the implementing server

**Concerns:**
- Range-pinned (`^1.0.0`) rather than exact pin — a breaking patch release could alter behaviour between installs. Acceptable for this SDK given Anthropic authorship, but note the condition.
- The implementing server controls what tools are exposed and what external services are called. The SDK itself is neutral — the risk lives in the server that wraps it.

**Decision:** APPROVED WITH CONDITIONS
- Condition: Implementing server source must be read in full (§2.6b) — the SDK is clean but is a multiplier for whatever the server does
- Condition: Credentials must come from environment variables only, not hardcoded
- Condition: Server must fail fast if required credentials are absent

---

### tsx

**Version reviewed:** ^4.0.0 (range-pinned)
**Tier:** Tier 1 — Low
**Reviewed:** 2026-03-13
**Skills using this:** playwright-pro (devDependency — MCP servers run via `npx tsx`)
**Role:** devDependency / runtime executor

**Install footprint:**
- TypeScript executor — runs `.ts` files directly without a separate compile step
- Wraps esbuild for fast transpilation

**Capabilities:**
- Executes TypeScript source files at runtime
- No network access, no file writes beyond standard transpile cache
- Used as the runtime in `.mcp.json` entries: `"command": "npx tsx src/index.ts"`

**Concerns:**
- If used to execute untrusted `.ts` files, it would run arbitrary TypeScript. In the skill context, it only runs the MCP server source files that are part of the reviewed skill — this is expected use.
- Range-pinned — esbuild transitive dependency updates are possible but low risk for this use case.

**Decision:** APPROVED
- Approved for use as a TypeScript executor for MCP server source files that have themselves been reviewed in §2.6b

---

### typescript

**Version reviewed:** ^5.0.0 (range-pinned)
**Tier:** Tier 1 — Low
**Reviewed:** 2026-03-13
**Skills using this:** playwright-pro (devDependency — type checking only)
**Role:** devDependency / type checker

**Install footprint:**
- The TypeScript compiler (tsc)
- No runtime dependency — compile-time only in skill context

**Capabilities:**
- Type checking and compilation
- Does not execute, no network access, no file system side effects beyond compilation output

**Concerns:**
- None in skill context. When used as a devDependency for type-checking MCP server source, risk is negligible.

**Decision:** APPROVED

---

### axios

**Version reviewed:** 1.5.0 (pinned — seen in dependency-auditor test project)
**Tier:** Tier 2 — Medium
**Reviewed:** 2026-03-13
**Skills using this:** None yet — pre-seeded for reference

**Install footprint:**
- Core dep: `follow-redirects`, `form-data`, `proxy-from-env`
- Relatively lean dep tree for an HTTP client

**Capabilities:**
- HTTP/HTTPS client — GET, POST, PUT, DELETE, etc.
- Supports request/response interceptors (flag if interceptors are used to log or transmit data)
- Browser and Node.js environments

**Concerns:**
- CVE history: CVE-2023-45857 (credential leak via CSRF token header) fixed in 1.6.0+. Version 1.5.0 is affected — flag for upgrade.
- Any skill using axios must document what URLs it calls and what data is in request bodies.
- Interceptors can be used to log or forward all requests — read any interceptor registrations in full.

**Decision:** APPROVED WITH CONDITIONS
- Condition: Minimum version 1.6.0 (CVE-2023-45857 patch)
- Condition: All request targets (URLs, request bodies) documented in skill review
- Condition: No interceptors that log or forward credential values

---

### dotenv

**Version reviewed:** 16.0.3 (pinned — seen in dependency-auditor test project)
**Tier:** Tier 1 — Low
**Reviewed:** 2026-03-13
**Skills using this:** None yet — pre-seeded for reference

**Install footprint:**
- Minimal — no significant transitive dependencies

**Capabilities:**
- Loads `.env` file into `process.env`
- Read-only from the file system; no network access

**Concerns:**
- Skills that load `.env` files must document which environment variables they read and what they do with the values. The package itself is safe; the risk is in what env vars it exposes.
- Should never commit `.env` files to the skill repository.

**Decision:** APPROVED

---

### chalk

**Version reviewed:** 4.1.2 (pinned — seen in dependency-auditor test project)
**Tier:** Tier 1 — Low
**Reviewed:** 2026-03-13
**Skills using this:** None yet — pre-seeded for reference

**Install footprint:**
- `ansi-styles`, `supports-color` — both lightweight, well-known

**Capabilities:**
- Terminal string styling (colours, bold, underline)
- No network access, no file system writes, no subprocess calls

**Concerns:**
- None.

**Decision:** APPROVED

---

### commander

**Version reviewed:** 9.4.1 (pinned — seen in dependency-auditor test project)
**Tier:** Tier 1 — Low
**Reviewed:** 2026-03-13
**Skills using this:** None yet — pre-seeded for reference

**Install footprint:**
- Zero dependencies

**Capabilities:**
- CLI argument parsing
- No network access, no file system writes, no subprocess calls

**Concerns:**
- None.

**Decision:** APPROVED

---

### express

**Version reviewed:** 4.18.1 (pinned — seen in dependency-auditor test project)
**Tier:** Tier 2 — Medium
**Reviewed:** 2026-03-13
**Skills using this:** None yet — pre-seeded for reference

**Install footprint:**
- Significant dep tree: `accepts`, `body-parser`, `cookie`, `cookie-signature`, `depd`, `encodeurl`, `escape-html`, `finalhandler`, `fresh`, `http-errors`, `merge-descriptors`, `methods`, `on-finished`, `parseurl`, `path-to-regexp`, `proxy-addr`, `qs`, `range-parser`, `safe-buffer`, `send`, `serve-static`, `setprototypeof`, `statuses`, `type-is`, `utils-merge`, `vary`

**Capabilities:**
- HTTP server framework — opens a network listener, handles incoming requests
- Skills that embed an Express server are exposing a network port on the host machine

**Concerns:**
- Any skill that starts an Express server must document what port it listens on, what routes it exposes, and what authentication is required.
- `path-to-regexp` CVE history — verify version compatibility when reviewing.
- Not appropriate for skills that should be purely local tools — a listening HTTP server is a meaningful privilege grant.

**Decision:** APPROVED WITH CONDITIONS
- Condition: Skill must document exposed routes, listen port, and authentication requirements
- Condition: Server must bind to `127.0.0.1` only, not `0.0.0.0`, unless Operator explicitly approves external exposure

---

### winston

**Version reviewed:** 3.8.2 (pinned — seen in dependency-auditor test project)
**Tier:** Tier 1 — Low
**Reviewed:** 2026-03-13
**Skills using this:** None yet — pre-seeded for reference

**Install footprint:**
- `@colors/colors`, `@dabh/diagnostics`, `async`, `is-stream`, `logform`, `one-time`, `readable-stream`, `safe-stable-stringify`, `stack-trace`, `triple-beam`

**Capabilities:**
- Logging framework — writes to stdout, files, or custom transports
- Custom transports can write to network destinations

**Concerns:**
- Custom transport configurations must be reviewed — a transport that POSTs log entries to an external URL is a data exfiltration risk.
- Skill must not log credential values, tokens, or PII.

**Decision:** APPROVED WITH CONDITIONS
- Condition: No network transports (HTTP, HTTPS, webhook) unless Operator-approved
- Condition: Log output must not contain credential values

---

### jsonwebtoken

**Version reviewed:** 8.5.1 (pinned — seen in dependency-auditor test project)
**Tier:** Tier 3 — High
**Reviewed:** 2026-03-13
**Skills using this:** None yet — pre-seeded for reference

**Install footprint:**
- `jws`, `lodash.includes`, `lodash.isboolean`, `lodash.isinteger`, `lodash.isnumber`, `lodash.isplainobject`, `lodash.isstring`, `lodash.once`, `ms`

**Capabilities:**
- JWT signing and verification
- Handles authentication tokens — a skill using this is processing or generating security credentials

**Concerns:**
- CVE-2022-23529, CVE-2022-23540, CVE-2022-23541 all affect versions before 9.0.0. Version 8.5.1 is affected.
- Minimum safe version is 9.0.0.

**Decision:** APPROVED WITH CONDITIONS
- Condition: Minimum version 9.0.0 (multiple CVE fixes)
- Condition: Skill must document what tokens are signed/verified and where they are transmitted

---

## Packages Not Yet Reviewed

The following packages appear in the dependency-auditor test project but have not been formally reviewed. They are not currently used by any vetted skill — they are flagged here for future reference if a skill depends on them.

| Package | Reason to review when encountered |
|---|---|
| `bcrypt` | Password hashing — credential-sensitive domain |
| `mongoose` | MongoDB ODM — database access with broad filesystem/network scope |
| `socket.io` | WebSocket server — persistent bidirectional network connections |
| `redis` | Redis client — external service network access |
| `nodemailer` | Email sending — outbound network, credential handling |
| `sharp` | Image processing — large native dep tree, potential CVE surface |
| `multer` | File upload handling — writes to filesystem from user-supplied data |
| `moment` | Date/time — deprecated; prefer `date-fns` or native `Temporal` |
| `helmet` | HTTP security headers — low risk but review configuration |
| `cors` | CORS policy middleware — review allowed origins |
| `express-rate-limit` | Rate limiting — low risk |
| `jest` / `supertest` | Testing — devDependency, low risk |
| `eslint` and plugins | Linting — devDependency, low risk |
| `webpack` and loaders | Build tooling — devDependency, low risk |

---

## Adding a New Package

When a skill review in §2.6b surfaces an unreviewed npm package:

1. Look up the package on npmjs.com — note maintainers, weekly downloads, last publish date, source repository
2. Run `npm audit` in the skill directory or check the npm security advisories page for known CVEs
3. Inspect the package's own `package.json` — what does it depend on transitively?
4. Classify using the tier table above
5. Add an entry to this file using the format below
6. Reference the entry in the skill's Phase 1 review record

**Entry template:**
```markdown
### [package-name]

**Version reviewed:** [exact or range version]
**Tier:** [Tier X — Label]
**Reviewed:** YYYY-MM-DD
**Skills using this:** [skill-name(s) or "None yet — pre-seeded for reference"]

**Install footprint:**
- [Key direct and transitive deps]

**Capabilities:**
- [What the package does that is relevant to security review]

**Concerns:**
- [CVEs, broad access patterns, conditions on use, or "None"]

**Decision:** APPROVED | APPROVED WITH CONDITIONS | BLOCKED
- Condition: [if applicable]
```

---

## Revision History

| Rev | Date | Author | Model | Why |
|---|---|---|---|---|
| 1.0 | 2026-03-13 | Joshua Alexander Clement | claude-sonnet-4-6 | Initial creation — npm package registry for TypeScript/JavaScript skills. Seeded with Node.js built-ins, packages from playwright-pro MCP servers (@modelcontextprotocol/sdk, tsx, typescript), and common packages from dependency-auditor test project |
