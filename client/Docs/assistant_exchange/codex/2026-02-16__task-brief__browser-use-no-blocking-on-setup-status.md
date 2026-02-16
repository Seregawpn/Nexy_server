# Task Brief: browser_use without setup-status blocking

## Request
Allow browser use to proceed without blocking on install/setup status checks.

## Implemented
- Updated `BrowserUseModule.process()` to stop emitting/returning `BROWSER_SETUP_IN_PROGRESS` as a blocking gate.
- Current behavior:
  - if browser is not marked installed, install task is started/reused in background;
  - request flow proceeds immediately to `BROWSER_TASK_STARTED` and task execution path.

## Files
- `modules/browser_automation/module.py`
- `tests/test_browser_module_ready_bypass.py`

## Tests
- Added test: `test_process_does_not_emit_setup_in_progress_when_not_ready`
- Full run:
  - `pytest -q tests/test_browser_module_ready_bypass.py tests/test_browser_install_contracts.py`
  - Result: `8 passed`

## Architecture gates
- Single owner: logic remains in `BrowserUseModule`.
- Zero duplication: reused existing install-task single-flight path.
- Anti-race: existing `_install_task_guard` kept; no second owner introduced.
- New state: none.
