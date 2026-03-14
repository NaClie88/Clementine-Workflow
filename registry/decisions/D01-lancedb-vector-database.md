# D01 — LanceDB as Vector Database for Knowledge Base RAG System

**Date**: 2026-03-14
**Status**: Accepted
**Decided by**: Joshua Alexander Clement

---

## Context

The knowledge base RAG system (`docs/knowledge-base-rag-plan.md`) requires vector similarity search: the ability to embed a natural-language query and retrieve the most semantically relevant entries from a corpus of ~500–1000 documents. This is not a capability that PostgreSQL or SQLite (the two pre-approved database engines in STD09 §2.2) provide natively.

Three additional packages are required alongside the vector database:
- An embedding model to convert text to float vectors (`sentence-transformers`)
- A YAML parser for `schema.yaml` and entry frontmatter (`pyyaml`)
- A frontmatter parser to extract YAML headers from markdown files (`python-frontmatter`)

None of these are in the approved package registry. All four require approval per STD09 §4 before use.

**Constraints in play:**
- Phase 1 must be fully local and embedded — no server process
- Phase 2 requires self-hosted deployment with the same Python API
- Phase 3 requires a cloud migration path without switching systems
- CPU-only (no GPU requirement)
- Apache 2.0 or similarly permissive licence required

---

## Options Considered

Twelve options were evaluated in session 2026-03-14. Six were eliminated before comparison:

| Eliminated | Reason |
|---|---|
| FAISS | No metadata storage — would require building a database on top of a library |
| Annoy | Same as FAISS; index must be fully rebuilt to add any entry |
| NumPy-only | O(N) linear scan; no indexing, no persistence, no metadata |
| Weaviate | BSL (proprietary) licence; embedded mode experimental |
| Marqo | Docker required for Phase 1 — violates no-server constraint |
| Qdrant | Phase 1 in-memory only (no file persistence without server); AGPL licence |

The six remaining candidates:

### Option A — pgvector (PostgreSQL extension)
PostgreSQL is already approved (STD09 §2.2). pgvector adds HNSW vector indexing as a PG extension. Full SQL capabilities alongside vector search. Best cloud migration path (every major managed Postgres offering supports it). Requires a PostgreSQL server process running locally — not truly embedded for Phase 1.

### Option B — sqlite-vec (SQLite extension)
SQLite is already approved (STD09 §2.2). sqlite-vec (by Alex Garcia, 2024) adds HNSW vector indexing as a SQLite extension. Single `.db` file, no server. Very new — limited production track record. Cloud migration requires switching to a different system entirely (SQLite does not have a managed cloud offering).

### Option C — ChromaDB
Purpose-built for LLM/RAG use cases. File-based for Phase 1, server-mode for Phase 2 (`chroma run`), same Python API throughout. Strong ecosystem and documentation for RAG workflows. Cloud offering was in beta as of early 2026. Apache 2.0.

### Option D — LanceDB *(chosen)*
File-based for Phase 1 (Apache Arrow columnar format on disk). LanceDB server for Phase 2. LanceDB Cloud for Phase 3. Same Python API throughout — migration is a connection string change, not a code rewrite. Built on Arrow: columnar storage with efficient filtering on metadata fields. Apache 2.0.

### Option E — DuckDB + VSS extension
DuckDB is excellent for analytical SQL queries. The VSS extension adds HNSW vector indexing. Would consolidate vector search and structured queries into one tool. The cloud and self-hosted story for vector workloads is weak — DuckDB is an embedded analytics engine, not a vector service. VSS extension is not the primary DuckDB use case.

### Option F — Milvus Lite
Purpose-built vector DB with a clean Lite → Milvus → Zilliz Cloud progression. AGPL 3.0 licence on the server component — requires legal review before commercial deployment.

---

## Decision

**LanceDB** (Option D) was chosen.

The deciding factors over the other remaining candidates:

- **vs. pgvector:** pgvector requires a PostgreSQL server for Phase 1 — a significant operational cost for a local knowledge base. LanceDB is truly embedded.
- **vs. sqlite-vec:** sqlite-vec is new (2024) with limited production track record. It also has no cloud migration path, which is a stated Phase 3 requirement.
- **vs. ChromaDB:** LanceDB's Arrow columnar format provides better performance characteristics as the knowledge base scales. Both are comparable for Phase 1; LanceDB has the cleaner architecture for Phase 3.
- **vs. DuckDB + VSS:** DuckDB's vector story is secondary to its SQL story. LanceDB's vector story is primary.
- **vs. Milvus Lite:** AGPL licence on the server is a blocker pending legal review.

The complete package set approved in this decision:

| Package | Version | Purpose |
|---|---|---|
| `lancedb` | 0.29.2 | Vector database — storage, indexing, and similarity search |
| `sentence-transformers` | 5.3.0 | Embedding model (`all-MiniLM-L6-v2`) — converts text to float vectors |
| `pyyaml` | 6.0.3 | YAML parser — reads `schema.yaml` and validates entry frontmatter |
| `python-frontmatter` | 1.1.0 | Frontmatter parser — extracts YAML header blocks from `.md` files |

`sentence-transformers` has no standard library equivalent; it performs ML inference. `pyyaml` is necessary because Python's stdlib contains no YAML parser. `python-frontmatter` is a thin wrapper around `pyyaml` that handles the `---` delimiter convention in markdown files.

---

## Consequences

**Made easier:**
- Phase 1 local development with zero server infrastructure
- Metadata pre-filtering on `domain` and `applies-to` fields during retrieval
- Migration to self-hosted (Phase 2) and cloud (Phase 3) is a connection string change, not a code rewrite

**Made harder or ruled out:**
- Full SQL joins on the knowledge base entries (LanceDB has SQL-like filtering but is not a general-purpose relational DB)
- pgvector remains the right choice if this project later adopts PostgreSQL as its primary app datastore and wants to consolidate

**Review trigger:**
- If the project adopts PostgreSQL as the primary app datastore in a future phase, this decision should be revisited — migrating to pgvector at that point would eliminate a dependency.

---

## Revision History

| Rev | Date | Author | Why |
|---|---|---|---|
| 1.0 | 2026-03-14 | Joshua Alexander Clement | Initial record — LanceDB selected from 12-option evaluation |

Assisted-By: Anthropic Claude Sonnet 4.6 (claude-sonnet-4-6)
