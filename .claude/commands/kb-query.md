---
name: "kb-query"
description: "Query the knowledge base for relevant entries. Usage: /kb-query [query text] [--domain DOMAIN] [--applies-to VALUE] [--top-k N]. Returns ranked knowledge base entries with similarity scores."
---

# Knowledge Base Query

Queries the LanceDB knowledge base index for entries relevant to the user's query.

**This skill is read-only.** It runs `query.py` and presents results. No files are written. No network calls are made (model and DB are local).

---

## Invocation

```
/kb-query [query] [options]
```

**Arguments:**
- `[query]` — The search query (required). Quote it if it contains special characters.
- `--domain DOMAIN` — Filter to a specific domain (e.g. `security`, `architecture`, `ux`, `database`, `distributed-systems`, `functional-programming`, `systems-thinking`)
- `--applies-to VALUE` — Post-filter by applies-to value (e.g. `backend`, `frontend`, `all`)
- `--top-k N` — Number of results to return (default: 10, max: practical limit ~30)

---

## Execution Steps

1. Extract the query string and any options from the user's invocation.
2. Run the following command from the repo root:

```bash
python3.12 knowledge-base/scripts/query.py "[QUERY]" [OPTIONS] --json
```

3. Parse the JSON output. Each result has:
   - `id`, `title`, `domain`, `sub_domain`
   - `theorist`, `year`
   - `applies_to`, `tags`
   - `similarity` (0.0–1.0; higher is more relevant)
   - `body` (full entry text)

4. Present results to the user in a readable format:
   - Lead with a brief summary: "Found N relevant entries for '[query]'"
   - For each result: title, domain/sub-domain, theorist (year), similarity score, and the first sentence of the Definition section
   - If `--domain` was used, note the filter in the summary line
   - If no results: "No matching entries found. Try broadening the query or removing the --domain filter."

5. If the user asks for the full content of a specific entry, read the file directly:
   ```
   knowledge-base/entries/[domain]/[id].md
   ```

---

## Error Handling

- **DB not found**: `knowledge-base/db/lance/` does not exist — tell user to run `python3.12 knowledge-base/scripts/embed.py` first.
- **Model load failure**: Unlikely if sentence-transformers is installed. Report the error verbatim.
- **No results**: Broaden the query or remove domain/applies-to filters.
- **JSON parse error**: Report the raw output and note the error.

---

## Rules

- Never write to any file during this skill
- Never send the query or results to any external service
- Never pass user input as the `--db-path` argument (path is always derived from repo root)
- Do not modify the DB — query.py is read-only
- If the user requests a domain that does not exist in the index, report the available domains rather than silently returning no results
