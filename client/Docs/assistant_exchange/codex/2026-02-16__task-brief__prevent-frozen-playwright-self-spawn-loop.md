# Task Brief: Prevent frozen Playwright install from spawning Nexy binary

Date: 2026-02-16

## Context
Runtime loop was observed where Nexy repeatedly started/stopped with duplicate-instance detection, while browser installer kept running Playwright install via Nexy executable path.

## Change
File changed:
- `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/modules/browser_automation/module.py`

What changed:
- In `run_install()` for browser setup:
  - Removed frozen-mode fallback to `sys.executable -m playwright install chromium`.
  - Added explicit guard: if frozen and bundled Playwright driver is not found, fail-fast with clear error.
  - Non-frozen mode still uses `sys.executable -m playwright install chromium`.

## Why
In packaged `.app`, `sys.executable` points to `/Applications/Nexy.app/Contents/MacOS/Nexy`. Running it with `-m playwright ...` can spawn another Nexy process, which triggers duplicate-instance shutdown loop and focus disruptions.

## Architecture gates
- Single Owner: browser install command remains owned by BrowserUse module.
- Zero Duplication: no new parallel install path introduced.
- Anti-Race: existing install lock retained; removed dangerous self-spawn path.
- Flag Lifecycle: no new flags added.

## Verification
- `python3 -m py_compile modules/browser_automation/module.py` passed.
- Expected runtime after deploy:
  - No repeated `SAFE_EXIT: duplicate_instance` bursts caused by browser install path.
  - No repeated `Executing install command: [/Applications/Nexy.app/Contents/MacOS/Nexy, -m, playwright, install, chromium]` lines.
