# Task Brief: Production Playwright driver resolution fix

## Context
Production app periodically showed browser install notifications. Investigation found install retries despite no completed Chromium in `~/Library/Application Support/Nexy/ms-playwright`.

## Root cause
Packaging included Playwright driver under `Contents/Resources/playwright/driver` with modern layout (`node + package/cli.js`) but runtime installer in frozen mode expected primarily `playwright.sh` and limited paths.

## Change
Updated `modules/browser_automation/module.py`:
- Added `_resolve_frozen_playwright_install_cmd()` with centralized frozen driver resolution.
- Supports both layouts:
  - legacy wrapper script (`playwright.sh` / `playwright.cmd`)
  - modern driver layout (`driver/node` + `driver/package/cli.js`)
- Added candidate search paths:
  - installed package driver dir
  - `_MEIPASS/playwright/driver`
  - `Contents/MacOS/playwright/driver`
  - `Contents/Resources/playwright/driver`
- Updated frozen install flow to use this resolver and avoid invalid fallback.

## Architecture gates
- Single owner: install command resolution remains in `BrowserUseModule`.
- Zero duplication: old fragmented path probing replaced by one resolver.
- Anti-race: existing single-flight install guards unchanged.
- Flags: none added.

## Verification
- `pytest -q tests/test_browser_install_contracts.py tests/test_browser_module_ready_bypass.py` → `8 passed`
- `python3 scripts/verify_architecture_guards.py` → `Architecture guards OK`
- `python3 -m py_compile modules/browser_automation/module.py` → OK
