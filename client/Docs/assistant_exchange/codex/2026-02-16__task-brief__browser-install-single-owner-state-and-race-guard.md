# Task Brief: browser install single-owner state + race guard

## Context
User asked to eliminate conflicts/duplication/races in browser install + browser_use startup behavior.

## Changes

### 1) `modules/browser_automation/module.py`
- Added explicit install task ownership and creation guard:
  - `self._install_task: asyncio.Task | None`
  - `self._install_task_guard = asyncio.Lock()`
  - `_get_or_start_install_task(restart_if_failed: bool)` helper.
- `initialize()` now starts eager install via `_get_or_start_install_task(...)` instead of direct `create_task`, removing duplicate creation path.
- `process()` non-blocking setup path now emits canonical non-terminal event:
  - `BROWSER_SETUP_IN_PROGRESS` (instead of fake `BROWSER_TASK_FAILED`).
- Kept hard failures only for actual install/task failure.

### 2) `integration/integrations/browser_use_integration.py`
- Setup-in-progress handling now recognizes canonical `BROWSER_SETUP_IN_PROGRESS` (with backward compatibility for old failed+error contract).
- Keeps queue/retry semantics using `BROWSER_TASK_QUEUED` without emitting terminal `browser.failed`.
- Removed duplicated setup TTS at integration layer (install status remains owner concern in module).

## Architecture Gates
- Single Owner: install lifecycle/status owned by `BrowserUseModule`.
- Zero Duplication: removed second semantics path (`FAILED + browser_setup_in_progress` as primary signal).
- Anti-Race: guarded install task creation with dedicated mutex.
- Flag Lifecycle: no new feature flags introduced.

## Verification
- `python3 -m py_compile` passed for:
  - `modules/browser_automation/module.py`
  - `integration/integrations/browser_use_integration.py`
  - `integration/integrations/action_execution_integration.py`
  - `integration/workflows/processing_workflow.py`
