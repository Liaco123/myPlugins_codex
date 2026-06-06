# Codex Plugin Marketplace

This repository contains a local Codex plugin marketplace and bundled plugin packages.

## Marketplace

- Marketplace manifest: `.agents/plugins/marketplace.json`
- Plugins directory: `plugins/`

## Included Plugins

- `context7`: Up-to-date library and API documentation for Codex via Context7 MCP.
- `mem0`: Persistent memory for Codex across coding sessions.

## Repository Layout

```text
.agents/plugins/marketplace.json
plugins/
  context7/
  mem0/
```

Each plugin keeps its own manifest, skills, MCP configuration, assets, and supporting scripts under its plugin directory.

## Development Notes

- Keep plugin changes scoped to one plugin whenever possible.
- Do not commit local virtual environments, caches, editor settings, or secrets.
- Use the existing plugin manifests as the source of truth for metadata.
