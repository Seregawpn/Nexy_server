# Task Brief: MCP executor resource paths

## Goal
Fix MCP open/close app failures by resolving server paths correctly and using the correct interpreter/runtime, plus ensure MCP server scripts are packaged.

## Changes
- Resolve MCP server script paths via resource resolver and return clear error if missing.
- Use current runtime executable for MCP server process.
- Default MCP server paths to mcp_servers/* in ActionExecutionIntegration.
- Package mcp_servers in PyInstaller datas.
- Updated REQ-016 to include mcp_servers in packaged resources.

## Files
- modules/mcp_action/core/mcp_action_executor.py
- integration/integrations/action_execution_integration.py
- packaging/Nexy.spec
- Docs/PROJECT_REQUIREMENTS.md

## Tests
- Not run (config/runtime change).

## Notes
- Feature flags discovery run for mcp_action_executor and action_execution_integration (no flags found).
