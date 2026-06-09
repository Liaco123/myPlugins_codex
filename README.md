# Codex Plugin Marketplace

This repository contains a local Codex plugin marketplace and bundled plugin packages.

## Marketplace

- Marketplace manifest: `.agents/plugins/marketplace.json`
- Plugins directory: `plugins/`

## Included Plugins

- `context7`: Up-to-date library and API documentation for Codex via Context7 MCP.
- `codegraphcontext`: Graph-based code intelligence for Codex via CodeGraphContext MCP.
- `gitnexus`: Code intelligence powered by a local knowledge graph.
- `mem0`: Persistent memory for Codex across coding sessions.

## Repository Layout

```text
.agents/plugins/marketplace.json
plugins/
  codegraphcontext/
  context7/
  gitnexus/
  mem0/
```

Each plugin keeps its own manifest, skills, MCP configuration, assets, and supporting scripts under its plugin directory.

## Development Notes

- Keep plugin changes scoped to one plugin whenever possible.
- Do not commit local virtual environments, caches, editor settings, or secrets.
- Use the existing plugin manifests as the source of truth for metadata.
