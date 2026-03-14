#!/usr/bin/env python3
"""
apply-metadata.py — Apply known metadata from entry-metadata.yaml to entry files.

Usage (from repo root):
    python3 knowledge-base/scripts/apply-metadata.py [--dry-run]

Reads entry-metadata.yaml and updates the frontmatter of each matching
entry file using targeted line replacements. Preserves file structure.
After running, re-run embed.py to rebuild the LanceDB index.

No external dependencies beyond pyyaml (approved in STD09 §2.4).
"""

import argparse
import re
import sys
from pathlib import Path

import yaml


# ---------------------------------------------------------------------------
# YAML value formatters (produce valid inline YAML for the frontmatter)
# ---------------------------------------------------------------------------

def fmt_list(items: list) -> str:
    if not items:
        return "[]"
    return "[" + ", ".join(str(i) for i in items) + "]"


def fmt_string(s: str) -> str:
    if not s:
        return '""'
    # Quote if the string contains characters that would break YAML parsing
    if any(c in s for c in (',', ':', '#', '[', ']', '{', '}')):
        escaped = s.replace('"', '\\"')
        return f'"{escaped}"'
    return s


def fmt_value(field: str, value) -> str:
    """Format a frontmatter value for inline YAML output."""
    if isinstance(value, list):
        return fmt_list(value)
    if isinstance(value, int):
        return str(value)
    if value is None:
        return "null"
    return fmt_string(str(value))


# ---------------------------------------------------------------------------
# File update
# ---------------------------------------------------------------------------

# Fields we know how to update (in the order they appear in migrated files)
MANAGED_FIELDS = [
    "applies-to",
    "complexity",
    "maturity",
    "theorist",
    "year",
    "related",
    "tags",
]


def apply_to_file(filepath: Path, meta: dict, dry_run: bool) -> bool:
    """
    Apply metadata values to a single entry file.
    Returns True if file was (or would be) changed.
    """
    content = filepath.read_text(encoding="utf-8")
    original = content

    for field in MANAGED_FIELDS:
        if field not in meta:
            continue
        new_value = fmt_value(field, meta[field])
        # Replace the field line (and any trailing inline comment)
        content = re.sub(
            rf"^({re.escape(field)}:).*$",
            f"{field}: {new_value}",
            content,
            flags=re.MULTILINE,
        )

    if content == original:
        return False

    if not dry_run:
        filepath.write_text(content, encoding="utf-8")
    return True


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Apply entry-metadata.yaml to entry files")
    parser.add_argument("--dry-run", action="store_true", help="Show changes without writing")
    args = parser.parse_args()

    scripts_dir = Path(__file__).resolve().parent
    repo_root = scripts_dir.parent.parent
    metadata_file = scripts_dir / "entry-metadata.yaml"
    entries_dir = repo_root / "knowledge-base" / "entries"

    if not metadata_file.exists():
        print(f"ERROR: {metadata_file} not found", file=sys.stderr)
        sys.exit(1)

    with open(metadata_file, encoding="utf-8") as f:
        data = yaml.safe_load(f)

    entries_meta: dict = data.get("entries", {})
    print(f"Loaded metadata for {len(entries_meta)} entries")

    # Build ID → filepath index
    id_to_file: dict[str, Path] = {}
    for md_file in entries_dir.rglob("*.md"):
        # Fast: derive ID from filename (no parse needed for lookup)
        stem = md_file.stem
        id_to_file[stem] = md_file

    updated = not_found = unchanged = 0

    for entry_id, meta in entries_meta.items():
        if entry_id not in id_to_file:
            print(f"  NOT FOUND: {entry_id}")
            not_found += 1
            continue

        filepath = id_to_file[entry_id]
        changed = apply_to_file(filepath, meta, args.dry_run)

        if changed:
            rel = filepath.relative_to(repo_root)
            print(f"  {'WOULD UPDATE' if args.dry_run else 'UPDATED'}: {rel}")
            updated += 1
        else:
            unchanged += 1

    label = "would update" if args.dry_run else "updated"
    print(f"\nDone: {updated} {label}, {unchanged} unchanged, {not_found} not found")
    print("\nNext: run embed.py to rebuild the LanceDB index with the new metadata.")


if __name__ == "__main__":
    main()
