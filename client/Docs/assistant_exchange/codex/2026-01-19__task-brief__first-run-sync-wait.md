# First-Run Sync Wait (Task Brief)

## Goal
- Make first-run permission prompts follow a synchronous 15-second window per permission without batching.

## Changes
- Added a status wait-loop after each activator call to avoid overlapping prompts.
- Enforced a minimum per-permission window using `activation_hold_duration_sec`.

## Files
- `integration/integrations/first_run_permissions_integration.py`

## Notes
- Uses status checkers that do not trigger prompts.
- `pause_between_requests_sec` remains applied after the wait-loop (config-controlled).

## Missing Docs
- `Docs/ASSISTANT_COORDINATION_PROTOCOL.md`
- `Docs/ANTIGRAVITY_PROMPT.md`
- `Docs/CODEX_PROMPT.md`
- `Docs/assistant_exchange/TEMPLATE.md`
