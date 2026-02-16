# Task Brief: Browser local-ready bypass for stuck setup loop

## Problem
Runtime repeatedly emitted `BROWSER_SETUP_IN_PROGRESS` although Chromium binaries were already present on disk. This created a false blocked state for browser tasks.

## Root Cause
`process()` gate relied on `_browser_installed` + install task completion state. If install task stayed pending/stale, request flow remained blocked even when local Chromium was already ready.

## Fix
- Added centralized local readiness check in module owner:
  - `BrowserUseModule._is_local_chromium_ready()`
  - requires `chromium-*` with `INSTALLATION_COMPLETE` marker.
- Added centralized browsers path resolver:
  - `BrowserUseModule._resolve_playwright_browsers_path()`
- Initialization now short-circuits to installed state when local Chromium is ready (no eager install task start).
- `_ensure_browser_installed()` now reuses the same local-ready check before install command path.
- `process()` now hard-guards against false setup loop:
  - if local-ready is true, marks installed and bypasses setup wait path;
  - cancels stale in-flight install task best-effort under install-task guard.

## Concurrency / Architecture
- Single owner preserved: `modules/browser_automation/module.py`.
- No new state axis introduced; reused existing `_browser_installed` and install-task guard.
- Race handling: stale task cancellation occurs only after positive local-ready proof.

## Verification
- Added test: `tests/test_browser_module_ready_bypass.py`
  - verifies no `BROWSER_SETUP_IN_PROGRESS` when local Chromium ready;
  - verifies stale install task gets cancelled.
- Existing install contract tests still pass.

Run:
- `pytest -q tests/test_browser_module_ready_bypass.py tests/test_browser_install_contracts.py`
- Result: `7 passed`.
