# Analysis: startup browser install started but no TTS announcement

## What happened
- In `nexy-dev.log` at `2026-02-15 20:52:08` install did start:
  - `Checking browser installation (Chromium)`
  - `PLAYWRIGHT_BROWSERS_PATH=/Users/sergiyzasorin/Library/Application Support/Nexy-Dev/ms-playwright`
  - `Executing install command: ... -m playwright install chromium`
- Browser artifacts now exist in:
  - `/Users/sergiyzasorin/Library/Application Support/Nexy-Dev/ms-playwright/chromium-1208`

## Why no assistant voice
- Startup install runs from module `initialize()` eager path.
- Previous TTS messages were added only for request-path (`browser_setup_in_progress` handling in BrowserUseIntegration), not eager startup install.

## Fix applied
- Added TTS announcements inside `BrowserUseModule._ensure_browser_installed()`:
  - when downloading starts: "The browser installation has started. Please wait a moment."
  - when install completes: "The browser has been installed. You can now use browser search."
- Session id for startup announcements: `system`.

## Verification
- `python3 -m py_compile modules/browser_automation/module.py integration/integrations/browser_use_integration.py` passed.
