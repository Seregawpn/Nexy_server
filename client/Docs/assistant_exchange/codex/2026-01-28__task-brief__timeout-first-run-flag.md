# Timeout first-run flag delay

## Goal
Ensure first-run completion flag is set only after time-boxed pipeline finishes.

## Changes
- In timeout mode, first-run no longer marks completion immediately; it awaits pipeline completion in background, then sets flag and publishes completion.
- Added timeout duration calculation based on config order, step_timeout, and inter-step pause.

## Files touched
- `integration/integrations/first_run_permissions_integration.py`

## Notes
- Required docs referenced by AGENTS.md are missing in this repo: `Docs/ASSISTANT_COORDINATION_PROTOCOL.md`, `Docs/ANTIGRAVITY_PROMPT.md`, `Docs/CODEX_PROMPT.md`, `Docs/assistant_exchange/TEMPLATE.md`.
