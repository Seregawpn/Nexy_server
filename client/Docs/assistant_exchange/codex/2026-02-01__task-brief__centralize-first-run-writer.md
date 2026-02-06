# Centralize First-Run State Writer

Date: 2026-02-01
Assistant: Codex

## Summary
Centralized first-run state mutations in `SimpleModuleCoordinator` and removed duplicate writes from `PermissionRestartIntegration` to prevent races and maintain a single source of truth.

## Changes
- `integration/integrations/permission_restart_integration.py`: removed `set_first_run_state(...)` from `_on_first_run_restart_pending`; keep only `set_restart_pending(True)`.
- `integration/core/simple_module_coordinator.py`: added centralized `set_first_run_state(...)` when handling `permissions.first_run_restart_pending`, plus a log line.

## Rationale
Multiple writers of first-run flags risk out-of-order and conflicting state. Coordinator is the architecture owner for cross-integration state transitions.

## Verification
- `rg -n "set_first_run_state" integration/` shows only coordinator writes for restart_pending path.
- Trigger `permissions.first_run_restart_pending` and confirm log:
  `[PERMISSIONS] first_run state cleared due to restart_pending ...`

## Missing Required Docs
Required docs referenced by `AGENTS.md` are not present in this repo snapshot:
- `Docs/ASSISTANT_COORDINATION_PROTOCOL.md`
- `Docs/ANTIGRAVITY_PROMPT.md`
- `Docs/CODEX_PROMPT.md`
- `Docs/assistant_exchange/TEMPLATE.md`
