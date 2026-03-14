#!/usr/bin/env python3
"""
embed.py — Index all knowledge-base entries into LanceDB.

Usage (from repo root):
    python3 knowledge-base/scripts/embed.py [--entries-dir PATH] [--db-path PATH]

Walks knowledge-base/entries/ recursively, parses YAML frontmatter,
validates required fields, embeds body text, and upserts into LanceDB.
Safe to re-run — rebuilds the table from scratch each time (overwrite mode).

Dependencies (all approved in STD09 §2.4 via D01):
    lancedb==0.29.2
    sentence-transformers==5.3.0
    python-frontmatter==1.1.0
    pyyaml==6.0.3
"""

import argparse
import sys
import warnings
from pathlib import Path

import frontmatter
import lancedb
from sentence_transformers import SentenceTransformer

# Silence noisy HuggingFace / transformers warnings in normal operation
warnings.filterwarnings("ignore", category=FutureWarning)

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

EMBEDDING_MODEL = "all-MiniLM-L6-v2"
EMBEDDING_DIM = 384
TABLE_NAME = "entries"
REQUIRED_FIELDS = {"id", "title", "domain", "sub-domain"}

ALLOWED_DOMAINS = {
    "security", "privacy", "architecture", "methodology", "coding-practices",
    "database", "distributed-systems", "ux", "systems-thinking",
    "functional-programming", "ml-ai", "ethics", "performance",
    "organisation", "documentation",
}


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def normalise_list(value) -> list[str]:
    """Coerce a frontmatter list field to a clean list of strings."""
    if not value:
        return []
    if isinstance(value, list):
        return [str(v) for v in value if v]
    return [str(value)]


def load_entry(path: Path) -> tuple[dict | None, list[str]]:
    """
    Parse a single entry file.
    Returns (record_dict, warnings_list).
    Returns (None, warnings) if entry should be skipped.
    """
    warnings_out = []

    try:
        post = frontmatter.load(str(path))
    except Exception as e:
        return None, [f"YAML parse error: {e}"]

    meta = post.metadata
    body = post.content.strip()

    # --- Required field validation ---
    missing = REQUIRED_FIELDS - set(meta.keys())
    if missing:
        warnings_out.append(f"missing required fields: {sorted(missing)}")
        return None, warnings_out

    entry_id = str(meta["id"]).strip()
    title = str(meta["title"]).strip()
    domain = str(meta["domain"]).strip()
    subdomain = str(meta.get("sub-domain", "")).strip()

    if not entry_id:
        return None, ["id field is empty"]
    if not body:
        warnings_out.append("body text is empty — entry will index with zero-length embedding text")

    # Warn on invalid domain (but still index — per schema.yaml validation rules)
    if domain not in ALLOWED_DOMAINS:
        warnings_out.append(f"unknown domain '{domain}' (not in schema.yaml allowed list)")

    record = {
        "id": entry_id,
        "title": title,
        "domain": domain,
        "sub_domain": subdomain,
        "applies_to": normalise_list(meta.get("applies-to")),
        "complexity": str(meta.get("complexity") or ""),
        "maturity": str(meta.get("maturity") or ""),
        "theorist": str(meta.get("theorist") or ""),
        "year": int(meta["year"]) if meta.get("year") and str(meta["year"]).isdigit() else 0,
        "related": normalise_list(meta.get("related")),
        "tags": normalise_list(meta.get("tags")),
        "body": body,
        "source_file": str(path.relative_to(path.parent.parent.parent)),
    }

    return record, warnings_out


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Index knowledge-base entries into LanceDB")
    parser.add_argument("--entries-dir", default=None, help="Path to entries/ directory")
    parser.add_argument("--db-path", default=None, help="Path to LanceDB database directory")
    args = parser.parse_args()

    repo_root = Path(__file__).resolve().parent.parent.parent
    entries_dir = Path(args.entries_dir) if args.entries_dir else repo_root / "knowledge-base" / "entries"
    db_path = Path(args.db_path) if args.db_path else repo_root / "knowledge-base" / "db" / "lance"

    if not entries_dir.exists():
        print(f"ERROR: entries directory not found: {entries_dir}", file=sys.stderr)
        sys.exit(1)

    db_path.mkdir(parents=True, exist_ok=True)

    # --- Discover entry files ---
    entry_files = sorted(entries_dir.rglob("*.md"))
    print(f"Found {len(entry_files)} .md files in {entries_dir.relative_to(repo_root)}")

    # --- Load and validate entries ---
    records = []
    total_warnings = 0
    skipped = 0

    for path in entry_files:
        record, warns = load_entry(path)
        rel = path.relative_to(repo_root)
        for w in warns:
            print(f"  WARNING [{rel}]: {w}")
            total_warnings += 1
        if record is None:
            skipped += 1
        else:
            records.append(record)

    print(f"\nLoaded {len(records)} entries ({skipped} skipped, {total_warnings} warnings)")

    if not records:
        print("ERROR: no entries to index", file=sys.stderr)
        sys.exit(1)

    # --- Load embedding model ---
    print(f"\nLoading embedding model: {EMBEDDING_MODEL} (CPU)")
    model = SentenceTransformer(EMBEDDING_MODEL, device="cpu")
    print("Model loaded.")

    # --- Embed body text ---
    print(f"Embedding {len(records)} entries...", end="", flush=True)
    texts = [r["body"] for r in records]
    embeddings = model.encode(texts, batch_size=32, show_progress_bar=False)
    print(" done.")

    for record, embedding in zip(records, embeddings):
        record["vector"] = embedding.tolist()

    # --- Write to LanceDB ---
    print(f"\nConnecting to LanceDB at {db_path.relative_to(repo_root)}")
    db = lancedb.connect(str(db_path))

    print(f"Writing table '{TABLE_NAME}' (overwrite mode)...")
    table = db.create_table(TABLE_NAME, data=records, mode="overwrite")

    count = table.count_rows()
    print(f"Table '{TABLE_NAME}' created with {count} rows.")

    # --- Summary ---
    print(f"""
Index complete
──────────────
  Entries indexed : {count}
  Entries skipped : {skipped}
  Warnings        : {total_warnings}
  DB path         : {db_path.relative_to(repo_root)}
  Table           : {TABLE_NAME}
  Embedding model : {EMBEDDING_MODEL} ({EMBEDDING_DIM}d)
""")

    if total_warnings > 0:
        print(f"  {total_warnings} warning(s) above — review entries with missing/invalid fields.")


if __name__ == "__main__":
    main()
