#!/usr/bin/env python3
"""
migrate.py — One-time migration from docs/dev-philosophy-reference.md
              into individual per-entry files under knowledge-base/entries/.

Usage (from repo root):
    python3 knowledge-base/scripts/migrate.py [--dry-run]

No external dependencies — stdlib only.
"""

import argparse
import re
import sys
from pathlib import Path


# ---------------------------------------------------------------------------
# Section heading → domain + sub-domain mapping
# Keys are substrings of the actual heading text (partial match is fine).
# ---------------------------------------------------------------------------

SECTION_MAP = {
    "1.1 Design Principles":              {"domain": "architecture",      "sub-domain": "design principles"},
    "1.2 Architectural Philosophies":     {"domain": "architecture",      "sub-domain": "architectural philosophy"},
    "1.3 Development Methodologies":      {"domain": "methodology",       "sub-domain": "development methodology"},
    "1.4 Operational Philosophies":       {"domain": "methodology",       "sub-domain": "operational philosophy"},
    "2. Coding Best Practice Domains":    {"domain": "coding-practices",  "sub-domain": "coding discipline"},
    "3.1 Foundational Privacy Theories":  {"domain": "privacy",           "sub-domain": "foundational theory"},
    "3.2 Regulatory Frameworks":          {"domain": "privacy",           "sub-domain": "regulatory framework"},
    "3.3 Technical Privacy Approaches":   {"domain": "privacy",           "sub-domain": "technical approach"},
    "4.1 Foundational Security Principles": {"domain": "security",        "sub-domain": "foundational principles"},
    "4.2 Threat Modelling Methodologies": {"domain": "security",          "sub-domain": "threat modelling"},
    "4.3 Industry Frameworks":            {"domain": "security",          "sub-domain": "industry frameworks"},
    "4.4 Secure Development Practices":   {"domain": "security",          "sub-domain": "secure development"},
    "4.5 Privacy & Security Architecture Patterns": {"domain": "security", "sub-domain": "architecture patterns"},
}

STOP_MARKER = "5. Research Meta-Tags"


def title_to_id(title: str) -> str:
    """Convert an entry title to a kebab-case ID.

    Strategy:
      1. Remove everything from the first "(" onwards (drops abbreviations/attributions)
      2. Remove em-dash suffix ("— Full Name")
      3. Lowercase, replace non-alphanumeric with hyphens, deduplicate
    """
    if "(" in title:
        title = title[: title.index("(")].strip()
    if " — " in title:
        title = title.split(" — ")[0].strip()
    title = title.lower()
    title = re.sub(r"[^a-z0-9]+", "-", title)
    title = re.sub(r"-+", "-", title).strip("-")
    return title


def match_section(heading_text: str) -> dict | None:
    """Return section meta if heading_text contains a known section key."""
    for key, meta in SECTION_MAP.items():
        if key in heading_text:
            return meta
    return None


def make_frontmatter(entry_id: str, title: str, domain: str, subdomain: str) -> str:
    return f"""---
id: {entry_id}
title: "{title}"
domain: {domain}
sub-domain: "{subdomain}"
applies-to: []  # TODO: backend | frontend | infrastructure | cloud | mobile | data | ml | all
complexity: ""  # TODO: low | medium | high
maturity: ""    # TODO: established | emerging | theoretical
theorist: ""    # TODO: primary originator or "multiple"
year: null      # TODO: year concept was formally named/published
related: []     # TODO: IDs of related entries
tags: []        # TODO: free-form tags
---
"""


def format_body(raw_body: str) -> str:
    """Convert bold markers to ## headings and prepend ## Definition."""
    body = raw_body.strip()

    # Convert bold section markers to ## headings
    body = re.sub(r"\*\*Example:\*\*\s*", "\n## Example\n\n", body)
    body = re.sub(r"\*\*Strengths:\*\*\s*", "\n## Strengths\n\n", body)
    body = re.sub(r"\*\*Weaknesses:\*\*\s*", "\n## Weaknesses\n\n", body)
    body = re.sub(r"\*\*Mitigation:\*\*\s*", "\n## Mitigation\n\n", body)

    # Prepend ## Definition to the first block (before any ## heading)
    if not body.startswith("##"):
        body = "## Definition\n\n" + body

    # Clean up excessive blank lines
    body = re.sub(r"\n{3,}", "\n\n", body)

    return body.strip()


def parse_entries(source: Path) -> list[dict]:
    """Parse source doc into a list of entry dicts."""
    lines = source.read_text(encoding="utf-8").splitlines()

    entries = []
    current_meta = None
    current_title = None
    current_body_lines: list[str] = []

    def flush_entry():
        if current_title and current_meta:
            body = "\n".join(current_body_lines).strip()
            if body:
                entries.append({
                    "title": current_title,
                    "domain": current_meta["domain"],
                    "sub-domain": current_meta["sub-domain"],
                    "body": body,
                })

    for line in lines:
        stripped = line.strip()

        # Stop at research meta-tags section
        if STOP_MARKER in stripped:
            break

        # ## or ### heading — check for section context update
        if stripped.startswith("### ") or stripped.startswith("## "):
            heading_text = re.sub(r"^#{2,3}\s+", "", stripped)
            meta = match_section(heading_text)
            if meta:
                flush_entry()
                current_title = None
                current_body_lines = []
                current_meta = meta
            continue

        # #### heading — new entry
        if stripped.startswith("#### "):
            flush_entry()
            current_title = stripped[5:].strip()
            current_body_lines = []
            continue

        # Skip bare horizontal rules (entry separators)
        if stripped == "---":
            continue

        # Accumulate body lines when inside an entry
        if current_title is not None:
            current_body_lines.append(line.rstrip())

    flush_entry()
    return entries


def write_entry(entry: dict, entries_dir: Path, dry_run: bool) -> tuple[bool, str]:
    entry_id = title_to_id(entry["title"])
    domain = entry["domain"]
    filepath = entries_dir / domain / f"{entry_id}.md"

    if filepath.exists():
        return False, f"SKIP (exists): {filepath.relative_to(entries_dir.parent.parent)}"

    frontmatter = make_frontmatter(entry_id, entry["title"], domain, entry["sub-domain"])
    body = format_body(entry["body"])
    content = frontmatter + "\n" + body + "\n"

    if dry_run:
        return True, f"DRY-RUN: {filepath.relative_to(entries_dir.parent.parent)}"

    filepath.parent.mkdir(parents=True, exist_ok=True)
    filepath.write_text(content, encoding="utf-8")
    return True, str(filepath.relative_to(entries_dir.parent.parent))


def main():
    parser = argparse.ArgumentParser(description="Migrate dev-philosophy-reference.md to per-entry files")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be written without writing")
    args = parser.parse_args()

    repo_root = Path(__file__).resolve().parent.parent.parent
    source = repo_root / "docs" / "dev-philosophy-reference.md"
    entries_dir = repo_root / "knowledge-base" / "entries"

    if not source.exists():
        print(f"ERROR: source not found: {source}", file=sys.stderr)
        sys.exit(1)

    entries = parse_entries(source)
    print(f"Parsed {len(entries)} entries from {source.name}")
    if args.dry_run:
        print("(dry-run — no files written)\n")

    written = skipped = 0
    for entry in entries:
        ok, msg = write_entry(entry, entries_dir, args.dry_run)
        if ok:
            written += 1
        else:
            skipped += 1
        print(f"  {'WROTE' if ok and not args.dry_run else msg.split(':')[0]}: {msg.split(': ', 1)[-1]}")

    print(f"\nDone: {written} {'would write' if args.dry_run else 'written'}, {skipped} skipped")


if __name__ == "__main__":
    main()
