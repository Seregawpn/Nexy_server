# Permissions Sequence + MCP Fallback

## Goal
Fix long first-run hangs and ensure sequential permission flow continues; add MCP open_app fallback when server script is missing.

## Changes
- First-run flow now checks permission status in smart mode, skips already granted, polls for status changes, and avoids long holds (FDA hold set to 0).
- Settings opening is non-blocking (`Popen`) to avoid stalls.
- MCP open_app falls back to system `open` when MCP server path is missing.

## Notes
Required project docs referenced by AGENTS.md are missing in this workspace: `Docs/ASSISTANT_COORDINATION_PROTOCOL.md`, `Docs/ANTIGRAVITY_PROMPT.md`, `Docs/CODEX_PROMPT.md`, `Docs/assistant_exchange/TEMPLATE.md`.
