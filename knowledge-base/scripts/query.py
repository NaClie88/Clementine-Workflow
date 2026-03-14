#!/usr/bin/env python3
"""
query.py — Query the knowledge-base LanceDB index.

Usage (from repo root):
    python3 knowledge-base/scripts/query.py "your query" [options]

Options:
    --domain DOMAIN       Pre-filter by domain (e.g. security, architecture)
    --applies-to VALUE    Post-filter by applies-to value (e.g. backend, all)
    --top-k N             Number of results to return (default: 10)
    --json                Output as JSON (for agent/machine consumption)
    --db-path PATH        Override default DB path

Examples:
    python3 knowledge-base/scripts/query.py "designing auth for a healthcare app" --domain security --top-k 8
    python3 knowledge-base/scripts/query.py "event-driven microservices" --json --top-k 5
"""

import argparse
import json
import sys
import warnings
from pathlib import Path

import lancedb
from sentence_transformers import SentenceTransformer

warnings.filterwarnings("ignore", category=FutureWarning)

EMBEDDING_MODEL = "all-MiniLM-L6-v2"
TABLE_NAME = "entries"


def build_query(table, query_vector: list[float], domain: str | None, top_k: int) -> list[dict]:
    """Run cosine similarity search with optional domain pre-filter."""
    q = table.search(query_vector).metric("cosine").limit(top_k * 3 if domain else top_k)
    if domain:
        q = q.where(f"domain = '{domain}'")
    return q.to_list()


def post_filter_applies_to(results: list[dict], applies_to: str) -> list[dict]:
    """Keep only results whose applies_to list contains the requested value or 'all'."""
    filtered = []
    for r in results:
        values = r.get("applies_to") or []
        if applies_to in values or "all" in values:
            filtered.append(r)
    return filtered


def format_human(results: list[dict], query: str, top_k: int) -> str:
    lines = [
        f"Query: \"{query}\"",
        f"Results: {min(len(results), top_k)} of {len(results)} found",
        "─" * 60,
    ]
    for i, r in enumerate(results[:top_k], 1):
        # _distance is cosine distance in [0, 2]; convert to similarity in [0, 1]
        dist = r.get("_distance", r.get("score"))
        score_str = f"{1 - dist / 2:.3f}" if isinstance(dist, float) else "?"
        domain = r.get("domain", "")
        subdomain = r.get("sub_domain", "")
        theorist = r.get("theorist", "")
        year = r.get("year", 0)
        applies_to = ", ".join(r.get("applies_to") or []) or "—"
        tags = ", ".join(r.get("tags") or []) or "—"

        lines.append(f"\n#{i}  {r['title']}  (score: {score_str})")
        lines.append(f"    ID       : {r['id']}")
        lines.append(f"    Domain   : {domain}" + (f" / {subdomain}" if subdomain else ""))
        if theorist:
            lines.append(f"    Theorist : {theorist}" + (f" ({year})" if year else ""))
        lines.append(f"    Applies  : {applies_to}")
        lines.append(f"    Tags     : {tags}")

        # Print first paragraph of body as a snippet
        body = r.get("body", "")
        snippet = ""
        for line in body.splitlines():
            stripped = line.strip()
            if stripped and not stripped.startswith("#"):
                snippet = stripped[:200] + ("…" if len(stripped) > 200 else "")
                break
        if snippet:
            lines.append(f"    Snippet  : {snippet}")

    return "\n".join(lines)


def format_json(results: list[dict], top_k: int) -> str:
    output = []
    for r in results[:top_k]:
        dist = r.get("_distance", r.get("score"))
        output.append({
            "id": r["id"],
            "title": r["title"],
            "domain": r.get("domain", ""),
            "sub_domain": r.get("sub_domain", ""),
            "theorist": r.get("theorist", ""),
            "year": r.get("year", 0),
            "applies_to": r.get("applies_to") or [],
            "tags": r.get("tags") or [],
            "similarity": round(1 - (dist / 2), 4) if isinstance(dist, float) else None,
            "body": r.get("body", ""),
        })
    return json.dumps(output, indent=2)


def main():
    parser = argparse.ArgumentParser(description="Query the knowledge-base")
    parser.add_argument("query", nargs="?", help="Query string")
    parser.add_argument("--domain", default=None, help="Pre-filter by domain")
    parser.add_argument("--applies-to", dest="applies_to", default=None, help="Post-filter by applies-to value")
    parser.add_argument("--top-k", type=int, default=10, help="Number of results (default: 10)")
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    parser.add_argument("--db-path", default=None, help="Override DB path")
    args = parser.parse_args()

    if not args.query:
        parser.print_help()
        sys.exit(1)

    repo_root = Path(__file__).resolve().parent.parent.parent
    db_path = Path(args.db_path) if args.db_path else repo_root / "knowledge-base" / "db" / "lance"

    if not db_path.exists():
        print(f"ERROR: database not found at {db_path}", file=sys.stderr)
        print("Run embed.py first to build the index.", file=sys.stderr)
        sys.exit(1)

    # Load model (CPU — GPU not used per plan spec)
    model = SentenceTransformer(EMBEDDING_MODEL, device="cpu")
    query_vector = model.encode([args.query])[0].tolist()

    # Connect and search
    db = lancedb.connect(str(db_path))
    try:
        table = db.open_table(TABLE_NAME)
    except Exception:
        print(f"ERROR: table '{TABLE_NAME}' not found. Run embed.py first.", file=sys.stderr)
        sys.exit(1)

    results = build_query(table, query_vector, args.domain, args.top_k)

    if args.applies_to:
        results = post_filter_applies_to(results, args.applies_to)

    if not results:
        msg = "No results found."
        if args.json:
            print("[]")
        else:
            print(msg)
        sys.exit(0)

    if args.json:
        print(format_json(results, args.top_k))
    else:
        print(format_human(results, args.query, args.top_k))

    sys.exit(0)


if __name__ == "__main__":
    main()
