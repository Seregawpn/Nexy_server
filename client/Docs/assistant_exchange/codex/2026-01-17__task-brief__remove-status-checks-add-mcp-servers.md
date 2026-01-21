# Remove Status Checks + Add MCP Servers

## Goal
Disable all permission status checks (time-based sequence only) and restore MCP open_app/close_app servers.

## Changes
- Removed status-check/polling logic from first-run permission sequence.
- Added MCP servers: `mcp_servers/open_app/server.py` and `mcp_servers/close_app/server.py`.
- Updated `config/unified_config.yaml` MCP server paths.

## Notes
Required project docs referenced by AGENTS.md are missing in this workspace: `Docs/ASSISTANT_COORDINATION_PROTOCOL.md`, `Docs/ANTIGRAVITY_PROMPT.md`, `Docs/CODEX_PROMPT.md`, `Docs/assistant_exchange/TEMPLATE.md`.
