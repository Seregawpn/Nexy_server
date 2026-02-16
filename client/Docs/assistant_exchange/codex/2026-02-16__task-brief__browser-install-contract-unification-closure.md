# Task Brief: browser install contract unification closure

## Goal
Close residual conflicts by enforcing one canonical setup event contract and one install-task owner model.

## Changes

### 1) `modules/browser_automation/module.py`
- Unified install owner model to class-level axes:
  - `_install_lock` (already class-level)
  - `_browser_installed` (already class-level)
  - `_install_task` (moved to class-level)
  - `_install_task_guard` (moved to class-level)
- Removed instance-level `_install_task` / `_install_task_guard`.
- `_get_or_start_install_task()` now uses class-level guard/task, eliminating mixed ownership and multi-instance drift.

### 2) `integration/integrations/browser_use_integration.py`
- Removed legacy fallback semantics for setup transition:
  - deleted handling of `BROWSER_TASK_FAILED + error=browser_setup_in_progress` as primary path.
- Canonical setup transition now only via `BROWSER_SETUP_IN_PROGRESS`.
- `BROWSER_TASK_QUEUED` remains the integration-facing queue/progress signal.

## Architecture Gates
- Single Owner: install status/ownership centralized in `BrowserUseModule`.
- Zero Duplication: removed dual contract for setup transition.
- Anti-Race: guarded install-task creation with class-level mutex.
- Flag Lifecycle: no new flags introduced.

## Verification
- `python3 -m py_compile` passed for:
  - `modules/browser_automation/module.py`
  - `integration/integrations/browser_use_integration.py`
  - `integration/integrations/action_execution_integration.py`
  - `integration/workflows/processing_workflow.py`

## Expected runtime effect
- No false terminal failure on setup transition.
- No duplicate install-task creation due to instance-level drift.
- One canonical event contract for setup-in-progress.
