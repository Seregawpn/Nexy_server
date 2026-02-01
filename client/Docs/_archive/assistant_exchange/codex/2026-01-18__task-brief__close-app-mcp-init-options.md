# Close App MCP Initialization Options

## Goal
Fix MCP close_app server startup error requiring initialization_options.

## Change Summary
- Added `server.create_initialization_options()` to `server.run` in close_app MCP server.

## Files Touched
- `mcp_servers/close_app/server.py`

## Verification
- Run `python3 mcp_servers/close_app/server.py` and confirm it starts without `TypeError`.
