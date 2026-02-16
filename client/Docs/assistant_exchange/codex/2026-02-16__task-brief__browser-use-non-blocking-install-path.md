# Task Brief: browser_use non-blocking install path

## Context
User requested to remove blocking behavior in browser task execution when Playwright Chromium is not yet ready.

## Changes
- Updated `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/modules/browser_automation/module.py`.
- Removed synchronous install waiting from `BrowserUseModule.process()`.
- New behavior in request path:
  - If browser not installed and no install task exists: start install in background, return immediate `BROWSER_TASK_FAILED` with `browser_setup_in_progress`.
  - If install task is running: return immediate `BROWSER_TASK_FAILED` with `browser_setup_in_progress`.
  - If install task failed/cancelled: clear stale task and return immediate `BROWSER_TASK_FAILED`.
  - Emit `BROWSER_TASK_STARTED` only when browser is actually ready and agent launch begins.

## Architecture Gates
- Single Owner: `BrowserUseModule` remains owner of install/run lifecycle.
- Zero Duplication: no new install path added, reused `_install_task` single-flight.
- Anti-Race: install still serialized by existing module lock/task; request path no longer blocks waiting for lock.
- Flag Lifecycle: no new feature flags added.

## Verification
- `python3 -m py_compile modules/browser_automation/module.py integration/integrations/browser_use_integration.py integration/workflows/processing_workflow.py` passed.

## Expected Runtime Outcome
- No hanging on `Waiting for install lock...` in active request path.
- User gets immediate terminal status and can retry shortly.
