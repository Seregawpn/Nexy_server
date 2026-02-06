# Browser automation missing in packaged app

## Context
- User reports browser automation starts (voice command) but no browser opens in packaged macOS .app; works from terminal.
- Reviewed: `modules/browser_automation/module.py`, `integration/integrations/browser_use_integration.py`, `packaging/Nexy.spec`, `packaging/entitlements.plist`, `config/unified_config.yaml`, and local `browser_use` package defaults.
- Required docs missing in repo: `Docs/ASSISTANT_COORDINATION_PROTOCOL.md`, `Docs/ANTIGRAVITY_PROMPT.md`, `Docs/CODEX_PROMPT.md`, `Docs/assistant_exchange/TEMPLATE.md`.

## Findings (hypotheses)
1) Frozen app resolves Playwright driver but does not pin a writable browsers path or ensure driver exec perms; install may fail silently or run headless.
2) In packaged app, browser binaries are not bundled; runtime download may fail due to missing driver path or environment.

## Proposed primary fix (design)
- Centralize Playwright runtime resolution inside `BrowserUseModule`:
  - Set `PLAYWRIGHT_BROWSERS_PATH` to `~/Library/Application Support/Nexy/ms-playwright` (ensure dirs).
  - Resolve driver path in frozen mode (Resources or `_MEIPASS`) and ensure executable bit.
  - Add explicit logging for driver path, browsers path, install stdout/stderr.
- Optional packaging hardening: bundle Playwright browsers into `.app` Resources and point `PLAYWRIGHT_BROWSERS_PATH` there.

## Verification ideas
- In packaged app, run a browser_use task and check logs for resolved paths and successful Chromium launch.
- Confirm `~/Library/Application Support/Nexy/ms-playwright` contains browsers and visible window opens.
