# Task Brief: permissions V2 no-progress logs after startup

## Context
On first-run startup, logs stopped after `permissions.v2.step_changed: microphone` and `state=grace`. No further step progress logs appeared.

## Root cause
`PermissionOrchestratorIntegration` scheduled orchestrator/event coroutines with `asyncio.create_task()` on the current startup loop. After tray `app.run()` takes over, that loop can stall, so permission pipeline stops at first await.

## Changes
- File: `modules/permissions/v2/integration.py`
- Scheduled orchestrator/resume coroutines on attached EventBus loop (`event_bus.get_loop()`) via `asyncio.run_coroutine_threadsafe(...)` when needed.
- Updated sync event bridge `_emit_event_sync` to emit on attached EventBus loop, not blindly on current loop.
- Removed loop-bound completion wait (`asyncio.Event`) usage in cross-loop path.
- `wait_for_completion()` now polls `_completed` with timeout using monotonic time.
- Updated stop handling for both `asyncio.Task` and `concurrent.futures.Future`.

## Expected result
Permissions V2 pipeline continues running during/after tray `app.run()` and no longer freezes at first step because of loop mismatch.

## Validation
- `python3 -m py_compile modules/permissions/v2/integration.py integration/integrations/first_run_permissions_integration.py`
