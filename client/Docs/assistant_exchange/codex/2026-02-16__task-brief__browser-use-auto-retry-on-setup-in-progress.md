# Task Brief: browser_use auto-retry for non-blocking browser setup

## Context
After switching to non-blocking behavior, first browser_use request returned `browser_setup_in_progress` and terminated immediately, so user task did not auto-start.

## Changes
- Updated `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/integration/integrations/browser_use_integration.py`.
- Added integration-level retry loop for transient setup state.

### New behavior
- If module returns `BROWSER_TASK_FAILED` with `error=browser_setup_in_progress`:
  - integration treats it as non-terminal setup state,
  - publishes `BROWSER_TASK_QUEUED` to `browser.progress`,
  - waits 2s and retries the same request automatically,
  - retries up to 45 attempts (~90s).
- If setup still not ready after retries:
  - emits terminal `BROWSER_TASK_FAILED` with `error=browser_setup_timeout`.

## Architecture Gates
- Single Owner: install/run owner remains `BrowserUseModule`; integration only orchestrates retry semantics.
- Zero Duplication: no second install path added.
- Anti-Race: one processing task per request with bounded retry; no parallel fan-out.
- Flag Lifecycle: no new feature flags.

## Verification
- `python3 -m py_compile integration/integrations/browser_use_integration.py modules/browser_automation/module.py` passed.
