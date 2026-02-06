# Task Brief: browser_use missing zstandard in packaged app

## Context
User reports browser automation doesn’t open in packaged macOS app, while terminal run works. Server logs show browser_use command dispatched.

## Evidence
- Client log (`~/Library/Logs/Nexy/nexy.log`) shows:
  - `modules.browser_automation.module` -> `Process called: task=...`
  - Immediate warning: `browser-use not installed: No module named 'zstandard'`
  - `browser.failed` emitted

## Root Cause
`zstandard` is excluded in `packaging/Nexy.spec`, so packaged app lacks dependency required by `browser-use`.

## Change
- Removed `zstandard` from `excludes` in `packaging/Nexy.spec`.

## Follow-up
- Rebuild app and re-test browser_use flow.
- Verify `zstandard` is present in `Contents/Resources` after build and that browser_use launches the browser.

