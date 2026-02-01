# Restore first-run gating in timeout mode

## Goal
Ensure app does not fully activate on first run until the timeout-based pipeline completes.

## Changes
- `are_all_granted` now returns `first_run_completed` when timeout mode is enabled.
- Removed timeout-mode bypass for startup restriction and module gating; first-run gate applies until flag exists.

## Files touched
- `integration/integrations/first_run_permissions_integration.py`
- `integration/core/simple_module_coordinator.py`

## Notes
- Required docs referenced by AGENTS.md are missing in this repo: `Docs/ASSISTANT_COORDINATION_PROTOCOL.md`, `Docs/ANTIGRAVITY_PROMPT.md`, `Docs/CODEX_PROMPT.md`, `Docs/assistant_exchange/TEMPLATE.md`.
