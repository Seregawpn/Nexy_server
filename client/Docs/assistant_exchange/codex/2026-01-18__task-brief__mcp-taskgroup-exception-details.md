# MCP TaskGroup Exception Details

## Goal
Expose sub-exceptions from MCP TaskGroup failures to make close_app errors actionable.

## Change Summary
- Added ExceptionGroup formatting in `McpActionExecutor` error handling.
- Error messages now include type and sub-exception summaries.

## Files Touched
- `modules/mcp_action/core/mcp_action_executor.py`

## Verification
- Trigger a failing MCP action and confirm logs show `ExceptionGroup(n): <sub-exception list>`.
