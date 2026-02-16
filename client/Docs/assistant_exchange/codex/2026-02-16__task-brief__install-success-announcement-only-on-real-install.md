# Task Brief: install success announcement only on real install

## Goal
Stop announcing "browser installed" on every app startup when Chromium is already present.

## Change
Updated `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/modules/browser_automation/module.py`:
- Removed success notification/TTS from `has_chromium` detection branch (`Chromium detected ... skipping install check`).
- Kept success notification/TTS only in actual install completion branch (`returncode == 0`).

## Result
- No repeated "installed" message on each app launch.
- User still gets start + finish announcements during a real install cycle.

## Verification
- `python3 -m py_compile modules/browser_automation/module.py` passed.
