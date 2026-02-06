# Race/Timing Review — First-run Events

Date: 2026-02-01
Assistant: Codex

## Scope
Reviewed first-run event ordering, duplicate state writers, and timing risks around `permissions.first_run_*`, `system.ready_to_greet`, and integration startup sequencing.

## Key Findings
- Multiple writers update first-run state (`SimpleModuleCoordinator`, `PermissionRestartIntegration`), which can cause out-of-order or conflicting flags.
- Event priority ordering is reliable only when callbacks are awaited on the same loop; when `run_coroutine_threadsafe` is used, ordering across subscribers is not guaranteed.
- Welcome message defers correctly during first-run and is protected by lock + played flags; duplication risk is low.

## Recommended Primary Fix
Centralize first-run state mutations in `SimpleModuleCoordinator` and remove direct `set_first_run_state` calls from `PermissionRestartIntegration`. Update coordinator handler for `permissions.first_run_restart_pending` to set the same state transitions.

## Files Touched (planned)
- `integration/integrations/permission_restart_integration.py`
- `integration/core/simple_module_coordinator.py`

## Verification Notes
- Ensure only coordinator writes first-run flags (grep for `set_first_run_state` outside coordinator).
- Trigger `permissions.first_run_restart_pending` and confirm state updates and restart scheduling logs.

## Missing Required Docs
Required docs referenced by `AGENTS.md` are not present in this repo snapshot:
- `Docs/ASSISTANT_COORDINATION_PROTOCOL.md`
- `Docs/ANTIGRAVITY_PROMPT.md`
- `Docs/CODEX_PROMPT.md`
- `Docs/assistant_exchange/TEMPLATE.md`
