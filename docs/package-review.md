# Package Review Registry

All Python packages used by skills in this project must be reviewed here before Phase 4 sandboxed testing begins. A package needs only one review; subsequent skills cite the review by package name.

**Last updated:** 2026-03-12
**Workflow reference:** `docs/skill-vetting-workflow.md` §2.7, §9

---

## How to Read This Registry

Each entry includes:
- **Version reviewed** — pinned version at time of review
- **Risk tier** — Standard Library | Tier 1 (Low) | Tier 2 (Medium) | Tier 3 (High) | Tier 4 (Blocked) | Unknown
- **Install footprint** — direct + transitive deps at that version
- **Capabilities** — what the package actually does that is relevant to security review
- **Concerns** — any red flags or conditions on use
- **Decision** — APPROVED | APPROVED WITH CONDITIONS | BLOCKED

---

## Tier Reference (from §9 of workflow)

| Tier | Risk | Description |
|---|---|---|
| Standard Library | Baseline | Ships with Python; no install needed |
| Tier 1 — Low | Low | Widely used, stable, well-audited (requests, click, pydantic, etc.) |
| Tier 2 — Medium | Medium | Useful but broader attack surface (paramiko, PyYAML, Jinja2, etc.) |
| Tier 3 — High | High | Significant capability grant; needs explicit justification |
| Tier 4 — Blocked | Blocked | Known malicious, network exfiltration risk, or raw code execution |

---

## Standard Library Packages

Standard library packages are pre-approved. They require no entry here but are listed for reference when they appear in import inventories.

**Pre-approved:** `os`, `sys`, `re`, `json`, `pathlib`, `subprocess`, `shutil`, `tempfile`, `hashlib`, `hmac`, `datetime`, `time`, `logging`, `argparse`, `io`, `csv`, `xml`, `html`, `urllib`, `http`, `email`, `socket`, `ssl`, `threading`, `multiprocessing`, `asyncio`, `typing`, `dataclasses`, `collections`, `itertools`, `functools`, `contextlib`, `copy`, `enum`, `abc`, `inspect`, `traceback`, `unittest`, `textwrap`, `string`, `struct`, `base64`, `binascii`, `uuid`, `random`, `math`, `statistics`, `decimal`, `fractions`

**Standard library packages with elevated concern (review in context):**
- `subprocess` — shell execution; verify no user input is passed unsanitized
- `socket` / `ssl` — raw network; verify target hosts are fixed or validated
- `os.system` / `os.popen` — shell exec shorthands; prefer `subprocess` with list args
- `importlib` / `__import__` — dynamic imports; flag if target is user-controlled
- `exec()` / `eval()` / `compile()` — dynamic code execution; hard flag if user input reaches these

---

## Tier 1 — Low Risk

### pypdf
- **Version reviewed:** 4.1.0
- **Risk tier:** Tier 1
- **Install footprint:** none
- **Capabilities:** Pure-Python PDF reader — extracts text, metadata, page content from existing PDF files. No write capability.
- **Concerns:** None for read-only use. Malformed PDFs could trigger parsing edge cases but no known RCE history.
- **Decision:** APPROVED

### pdfplumber
- **Version reviewed:** 0.11.0
- **Risk tier:** Tier 1
- **Install footprint:** pypdf, pdfminer.six (Wand optional)
- **Capabilities:** PDF text and table extraction; higher-level than pypdf. Read-only.
- **Concerns:** Same as pypdf — reads existing files only. No network, no shell.
- **Decision:** APPROVED

### reportlab
- **Version reviewed:** 4.1.0
- **Risk tier:** Tier 2
- **Install footprint:** chardet, pillow (optional)
- **Capabilities:** PDF generation — can embed text, images, hyperlinks, and arbitrary binary content into PDF output
- **Concerns:** Generates binary output; if skill writes to user-specified paths verify destination is project-local. No network at runtime (font loading may check system paths on first run).
- **Decision:** APPROVED WITH CONDITIONS — verify output path is project-local or temp; do not write to user-specified paths without sanitization

### openpyxl
- **Version reviewed:** 3.1.2
- **Risk tier:** Tier 1
- **Install footprint:** et-xmlfile
- **Capabilities:** Excel (.xlsx) read and write — cells, formulas, charts, named ranges
- **Concerns:** None for local file I/O. Writes stay within the file path given; verify path is project-local. No network, no shell.
- **Decision:** APPROVED WITH CONDITIONS — verify output path is project-local

### pillow
- **Version reviewed:** 10.2.0
- **Risk tier:** Tier 1
- **Install footprint:** none (optional: libjpeg, libpng, libtiff via system)
- **Capabilities:** Image processing — open, transform, save many image formats (JPEG, PNG, GIF, TIFF, BMP, WebP, etc.)
- **Concerns:** Historical CVEs in image format decoders (mostly resolved in recent versions); do not process untrusted external images without input validation. No network, no shell.
- **Decision:** APPROVED WITH CONDITIONS — process only locally generated or known-source images; do not pipe user-supplied URLs to Pillow directly

### imageio
- **Version reviewed:** 2.34.0
- **Risk tier:** Tier 1
- **Install footprint:** pillow, numpy
- **Capabilities:** Image and video reading/writing; delegates to pillow, ffmpeg (via imageio-ffmpeg), or other backends depending on format
- **Concerns:** By itself, Tier 1. Risk depends on which backend is activated — if imageio-ffmpeg is present, ffmpeg URI handling applies (see imageio-ffmpeg entry below).
- **Decision:** APPROVED — see imageio-ffmpeg entry if video output is required

### imageio-ffmpeg
- **Version reviewed:** 0.5.1
- **Risk tier:** Tier 2
- **Install footprint:** ships a self-contained ffmpeg binary (~70MB)
- **Capabilities:** Wraps ffmpeg for video encode/decode. ffmpeg can open network URIs (rtsp://, http://, etc.) in addition to local files.
- **Concerns:** Ships a bundled binary that is not managed by the OS package manager or pip security audits. ffmpeg's network URI support could be abused if user input reaches the input path argument. Binary version should be tracked against ffmpeg security advisories.
- **Decision:** APPROVED WITH CONDITIONS — skill must pass only locally generated or fixed file paths to ffmpeg; do not pass user-controlled strings as input URI

### numpy
- **Version reviewed:** 1.26.4
- **Risk tier:** Tier 1
- **Install footprint:** none (C extensions only)
- **Capabilities:** Numeric array computation — mathematical operations, array manipulation, linear algebra
- **Concerns:** None. No network, no shell, no file I/O beyond what the calling code explicitly does.
- **Decision:** APPROVED

### requests
- **Version reviewed:** 2.31.0
- **Risk tier:** Tier 1
- **Install footprint:** certifi, charset-normalizer, idna, urllib3
- **Capabilities:** HTTP client — GET/POST/PUT/DELETE, session management, cookies, auth headers
- **Concerns:** All network calls go outward; verify target URLs are fixed constants or validated. Do not pass user input directly as URL without sanitization.
- **Decision:** APPROVED WITH CONDITIONS — verify outbound targets in each skill review

### click
- **Version reviewed:** 8.1.7
- **Risk tier:** Tier 1
- **Install footprint:** none (no mandatory deps beyond colorama on Windows)
- **Capabilities:** CLI argument parsing and command dispatch
- **Concerns:** None. Pure argument/UI library.
- **Decision:** APPROVED

### pydantic
- **Version reviewed:** 2.5.3
- **Risk tier:** Tier 1
- **Install footprint:** annotated-types, pydantic-core, typing-extensions
- **Capabilities:** Data validation and serialization via Python type annotations
- **Concerns:** None. No network, no filesystem writes, no shell.
- **Decision:** APPROVED

### pydantic-settings
- **Version reviewed:** 2.1.0
- **Risk tier:** Tier 1
- **Install footprint:** pydantic, python-dotenv
- **Capabilities:** Reads config from environment variables and `.env` files
- **Concerns:** Reads `.env` files — verify which files are accessed and that they don't contain secrets being forwarded to untrusted code.
- **Decision:** APPROVED WITH CONDITIONS — verify `.env` scope in each skill review

### python-dotenv
- **Version reviewed:** 1.0.0
- **Risk tier:** Tier 1
- **Install footprint:** none
- **Capabilities:** Reads `.env` files into `os.environ`
- **Concerns:** Can expose secrets to subsequent code; verify what consumes the loaded env vars.
- **Decision:** APPROVED WITH CONDITIONS — verify downstream consumers

### rich
- **Version reviewed:** 13.7.0
- **Risk tier:** Tier 1
- **Install footprint:** markdown-it-py, mdurl, pygments
- **Capabilities:** Terminal rendering — tables, panels, progress bars, syntax highlighting
- **Concerns:** None. Pure terminal output library.
- **Decision:** APPROVED

### typer
- **Version reviewed:** 0.9.0
- **Risk tier:** Tier 1
- **Install footprint:** click
- **Capabilities:** CLI framework built on Click
- **Concerns:** None. Pure argument/UI library.
- **Decision:** APPROVED

### httpx
- **Version reviewed:** 0.26.0
- **Risk tier:** Tier 1
- **Install footprint:** anyio, certifi, h11, httpcore, idna, sniffio
- **Capabilities:** Async-capable HTTP client; API-compatible replacement for `requests`
- **Concerns:** Same as `requests` — verify outbound targets.
- **Decision:** APPROVED WITH CONDITIONS — verify outbound targets in each skill review

### jinja2
- **Version reviewed:** 3.1.3
- **Risk tier:** Tier 2 (see Tier 2 section)
- **Install footprint:** MarkupSafe
- **Capabilities:** Template engine with sandboxed mode; can execute arbitrary code if `Environment(undefined=...)` sandbox is bypassed
- **Concerns:** Server-side template injection (SSTI) if user input reaches template rendering
- **Decision:** See Tier 2 entry

### PyYAML
- **Version reviewed:** 6.0.1
- **Risk tier:** Tier 2 (see Tier 2 section)
- **Capabilities:** YAML parsing and serialization
- **Concerns:** `yaml.load()` without `Loader=yaml.SafeLoader` executes arbitrary Python — must use `yaml.safe_load()`
- **Decision:** See Tier 2 entry

---

## Tier 2 — Medium Risk

### jinja2 / Jinja2
- **Version reviewed:** 3.1.3
- **Risk tier:** Tier 2
- **Install footprint:** MarkupSafe
- **Capabilities:** Template rendering; `Environment` supports `SandboxedEnvironment`
- **Concerns:** If user input reaches `env.from_string(user_input).render()`, arbitrary code execution is possible via SSTI. Skills must use `SandboxedEnvironment` or render from static template strings only.
- **Decision:** APPROVED WITH CONDITIONS — skill review must confirm no user input reaches template source; `SandboxedEnvironment` preferred

### PyYAML
- **Version reviewed:** 6.0.1
- **Risk tier:** Tier 2
- **Install footprint:** none
- **Capabilities:** YAML parse/emit
- **Concerns:** `yaml.load(data)` without `Loader=yaml.SafeLoader` can instantiate arbitrary Python objects. Skills must use `yaml.safe_load()`.
- **Decision:** APPROVED WITH CONDITIONS — skill review must confirm `yaml.safe_load()` or `yaml.load(..., Loader=yaml.SafeLoader)` only

### paramiko
- **Version reviewed:** 3.4.0
- **Risk tier:** Tier 2
- **Install footprint:** bcrypt, cryptography, pynacl
- **Capabilities:** SSH client and server implementation; can execute remote commands, transfer files via SFTP
- **Concerns:** Significant network capability grant; can connect to arbitrary SSH hosts. Requires explicit justification of why SSH access is needed and what hosts are targeted.
- **Decision:** APPROVED WITH CONDITIONS — skill must document target host(s) and use case; key-based auth preferred over password

### GitPython
- **Version reviewed:** 3.1.41
- **Risk tier:** Tier 2
- **Install footprint:** gitdb, smmap
- **Capabilities:** Python interface to Git operations — clone, commit, push, diff, log
- **Concerns:** Can push to remote repositories (data exfiltration vector). Skills using GitPython must scope operations to local repo only unless remote operations are explicitly part of the skill's purpose.
- **Decision:** APPROVED WITH CONDITIONS — remote push/fetch operations need explicit Operator approval in skill review

### cryptography
- **Version reviewed:** 42.0.2
- **Risk tier:** Tier 2
- **Install footprint:** cffi (native extension)
- **Capabilities:** Cryptographic primitives — symmetric/asymmetric encryption, hashing, certificate handling
- **Concerns:** Can encrypt data (potential for obfuscated exfiltration) or decrypt secrets. Skill must document what is encrypted/decrypted and why.
- **Decision:** APPROVED WITH CONDITIONS — document encrypt/decrypt purpose in skill review

### boto3
- **Version reviewed:** 1.34.0
- **Risk tier:** Tier 2
- **Install footprint:** botocore, jmespath, s3transfer, urllib3
- **Capabilities:** AWS SDK — full AWS API access (S3, EC2, Lambda, IAM, etc.)
- **Concerns:** Reads AWS credentials from `~/.aws/` or environment. Can access/modify cloud resources. Requires explicit justification.
- **Decision:** APPROVED WITH CONDITIONS — skill must document which AWS services are accessed, with what permissions, and confirm no credential logging

### openai
- **Version reviewed:** 1.12.0
- **Risk tier:** Tier 2
- **Install footprint:** anyio, distro, httpx, pydantic, sniffio, tqdm
- **Capabilities:** OpenAI API client — sends data to OpenAI's servers
- **Concerns:** User data sent externally. API key must come from environment, not hardcoded.
- **Decision:** APPROVED WITH CONDITIONS — no hardcoded API keys; document what data is sent to OpenAI

### anthropic
- **Version reviewed:** 0.18.0
- **Risk tier:** Tier 2
- **Install footprint:** anyio, distro, httpx, pydantic, sniffio, tokenizers
- **Capabilities:** Anthropic API client — sends data to Anthropic's servers
- **Concerns:** Same as openai — external data transmission. API key from environment only.
- **Decision:** APPROVED WITH CONDITIONS — no hardcoded API keys; document what data is sent

---

## Tier 3 — High Risk

*Packages in this tier require explicit written justification for the use case and Operator sign-off before Phase 4.*

### selenium
- **Version reviewed:** 4.17.2
- **Risk tier:** Tier 3
- **Install footprint:** certifi, trio, trio-websocket, urllib3, webdriver-manager (if used)
- **Capabilities:** Browser automation — can interact with any website, submit forms, extract cookies, perform authenticated sessions
- **Concerns:** High exfiltration potential; can log into sites with stored credentials; can exfiltrate browser session state. Skill must be narrowly scoped to specific test URLs.
- **Decision:** APPROVED WITH CONDITIONS — requires explicit Operator sign-off; skill must document target URLs; no production credential access

### playwright (Python)
- **Version reviewed:** 1.41.2
- **Risk tier:** Tier 3
- **Install footprint:** greenlet + browser binaries (~300MB)
- **Capabilities:** Same as Selenium; additionally can intercept network requests, modify responses
- **Concerns:** Same as Selenium plus network interception capability.
- **Decision:** APPROVED WITH CONDITIONS — same conditions as selenium; additionally verify no network intercept in script

### docker
- **Version reviewed:** 7.0.0
- **Risk tier:** Tier 3
- **Install footprint:** requests, urllib3, websocket-client
- **Capabilities:** Docker SDK — can create/run/destroy containers, pull images, exec into running containers
- **Concerns:** Container escape is a known attack vector; exec into running containers is essentially shell access. Very powerful.
- **Decision:** APPROVED WITH CONDITIONS — Operator sign-off required; document which images, what exec commands, and why container access is needed

### pyautogui
- **Version reviewed:** 0.9.54
- **Risk tier:** Tier 3
- **Install footprint:** pillow, pymsgbox, pygetwindow, pyscreeze, pytweening, mouseinfo
- **Capabilities:** Desktop GUI automation — can control mouse, keyboard, take screenshots
- **Concerns:** Can interact with any application on the desktop, including password managers and terminal emulators.
- **Decision:** APPROVED WITH CONDITIONS — Operator sign-off required; skill must run in sandboxed display (Xvfb) during testing

---

## Tier 4 — Blocked

*No skill may depend on these packages. Presence of a Tier 4 package is an automatic hard reject.*

### pycryptodome (as `Crypto`)
- **Reason blocked:** Historically used in obfuscated malware payloads; naming conflict with legitimate `pycryptography`; better replaced by `cryptography` package
- **Status:** BLOCKED

### requests-unixsocket
- **Reason blocked:** Enables HTTP over Unix domain sockets — can be used to access Docker socket or other privileged local APIs
- **Status:** BLOCKED

### pyzmq (in skill scripts)
- **Reason blocked:** ZeroMQ bindings enable hidden inter-process communication channels that could be used for covert C2. Legitimate in infrastructure code but not in skill scripts.
- **Status:** BLOCKED in skill scripts; Operator exception required for infrastructure use

### pickle / cloudpickle (deserialization of untrusted data)
- **Reason blocked:** Deserializing untrusted pickle data executes arbitrary code. Use is blocked when input source is external or user-controlled. Safe when serializing/deserializing your own data within a controlled pipeline.
- **Status:** BLOCKED for untrusted input; flag and review for internal use

---

## Packages Flagged as Unknown

*Packages seen in skill import inventories that have not yet been reviewed. Add a full entry above before any skill depending on them reaches Phase 4.*

| Package | First seen in skill | Flagged date | Reviewer notes |
|---|---|---|---|
| — | — | — | — |

---

## Changelog

| Date | Change |
|---|---|
| 2026-03-12 | Initial registry created. Standard library pre-approvals, Tier 1 (requests, click, pydantic, pydantic-settings, python-dotenv, rich, typer, httpx), Tier 2 (jinja2, PyYAML, paramiko, GitPython, cryptography, boto3, openai, anthropic), Tier 3 (selenium, playwright, docker, pyautogui), Tier 4 (pycryptodome, requests-unixsocket, pyzmq in scripts, pickle for untrusted input). |
| 2026-03-13 | Added 8 packages required by Anthropic official skills: Tier 1 (pypdf, pdfplumber, openpyxl, pillow, imageio, numpy), Tier 2 (reportlab, imageio-ffmpeg). Clears package gate hold on pdf, xlsx, slack-gif-creator skills from github.com/anthropics/skills. |
