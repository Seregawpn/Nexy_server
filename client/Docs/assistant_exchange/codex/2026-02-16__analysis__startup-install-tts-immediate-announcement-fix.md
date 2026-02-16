# Analysis: startup browser install had no TTS; immediate announcement fix

## Observed in logs
- At `2026-02-15 20:56:07` startup install path was triggered:
  - `Waiting for install lock`
  - `Acquired install lock`
  - `Checking browser installation (Chromium)`
  - `Executing install command: ... playwright install chromium`
- There were no follow-up logs:
  - no `Installing browser (downloading)`
  - no `Browser installation check passed`
  - no TTS logs for browser setup status

## Cause
- Previous TTS start message depended on the >2s timeout branch (`Installing browser (downloading)`), which did not execute in this startup path.

## Fix
- Updated `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/modules/browser_automation/module.py`.
- Added immediate setup announcement right before starting install task:
  - notification: `Browser setup started: Installing Chromium...`
  - TTS: `The browser installation has started. Please wait a moment.`
- Kept timeout-branch TTS as fallback, guarded by `install_start_announced` to avoid duplicate voice prompts.

## Verification
- `python3 -m py_compile modules/browser_automation/module.py integration/integrations/browser_use_integration.py` passed.
