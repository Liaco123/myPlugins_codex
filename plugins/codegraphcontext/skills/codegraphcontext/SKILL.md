---
name: codegraphcontext
description: Use CodeGraphContext MCP for graph-based repository indexing, symbol search, relationship analysis, call-chain tracing, and codebase impact exploration.
---

Use CodeGraphContext when a task benefits from repository-level graph context rather than isolated file reads.

Good triggers:
- Indexing the current repository for MCP-backed code graph queries.
- Finding callers, callees, imports, inheritance paths, or dependency chains.
- Exploring large-codebase architecture or impact before a change.
- Looking for dead code, complex functions, or cross-file relationships.

Workflow:
1. Ensure the target repository is indexed before relying on graph answers.
2. Prefer focused graph queries over broad scans.
3. Treat graph results as context, then verify important conclusions against source files.
4. If tools are unavailable, report that CodeGraphContext MCP is not connected and fall back to local code inspection.

Operational notes:
- This plugin starts CGC with `uvx codegraphcontext mcp start`.
- CGC may create or use configuration under the user's CodeGraphContext home directory.
- For C or C++ projects, accurate SCIP indexing may require a valid `compile_commands.json`.
