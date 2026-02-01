# Timeboxed permissions flow

## Goal
Remove blocking behavior in permissions V2 by introducing time-based step advancement and non-blocking startup.

## Changes
- Added `advance_on_timeout` and per-step timeout support to V2 config loading and orchestrator.
- Orchestrator now advances after timeout and bypasses restart/limited-mode decisions in timeout mode.
- First-run integration now supports non-blocking startup when timeout mode is enabled and publishes early completion.
- Coordinator skips first-run restrictions and permission gating when timeout mode is enabled.
- Config updated to enable timeout mode and set `default_step_timeout_s`.

## Files touched
- `modules/permissions/v2/types.py`
- `modules/permissions/v2/config_loader.py`
- `modules/permissions/v2/orchestrator.py`
- `modules/permissions/v2/integration.py`
- `integration/integrations/first_run_permissions_integration.py`
- `integration/core/simple_module_coordinator.py`
- `config/unified_config.yaml`

## Notes
- Required docs referenced by AGENTS.md are missing in this repo: `Docs/ASSISTANT_COORDINATION_PROTOCOL.md`, `Docs/ANTIGRAVITY_PROMPT.md`, `Docs/CODEX_PROMPT.md`, `Docs/assistant_exchange/TEMPLATE.md`.
