# Task Brief: Centralize restart owner (remove duplicate restart paths)

## Goal
Eliminate duplicate/conflicting restart ownership in first-run permissions flow.

## Problem
Two restart-capable paths existed in codebase:
1) V2 orchestrator internal restart branch (`_enter_restart_sequence` with `restart_handler.trigger_restart`)
2) Integration-level restart scheduling from coordinator via `PermissionRestartIntegration`

This creates potential ownership conflict when config/modes change.

## Changes
1. `modules/permissions/v2/orchestrator.py`
- `_enter_restart_sequence()` no longer executes restart directly.
- It now emits restart-required signal and completes flow (`_complete(full_mode=True)`), delegating actual restart execution to centralized integration layer.

2. Existing centralized path kept:
- `SimpleModuleCoordinator._on_permissions_completed()` requests restart via
  `PermissionRestartIntegration.request_restart_after_first_run_completed(...)`.

3. `PermissionRestartIntegration` remains the single restart executor with guards:
- single-flight `_restart_task`
- recent restart flag guard
- updater/user-quit guards

## Verification
- `python3 -m py_compile modules/permissions/v2/orchestrator.py integration/core/simple_module_coordinator.py integration/integrations/permission_restart_integration.py` passed.

## Expected behavior
- One restart owner in runtime: `PermissionRestartIntegration`.
- No duplicate restart scheduling from V2 orchestrator internals.
- First-run completion triggers centralized restart request only once.
