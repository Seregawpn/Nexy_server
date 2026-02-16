# Task Brief: Browser setup in-progress TTS throttle

## Context
User reported repeated `BROWSER_SETUP_IN_PROGRESS` loop without clear audible feedback while Playwright browser is still installing.

## Change
- Added centralized in-progress install announcement in owner integration:
  - File: `integration/integrations/browser_use_integration.py`
  - New method: `_maybe_announce_setup_in_progress(session_id)`
  - Message: `Browser is still installing. Please wait a few minutes.`
  - Added anti-spam cooldown: `self._setup_wait_tts_cooldown_sec` (default 20s)
  - Added bounded per-session timestamp map to avoid unbounded growth.
- Wired call into `BROWSER_SETUP_IN_PROGRESS` branch in `_run_process`.

## Architecture gates
- Single owner: install UX remains in `BrowserUseIntegration`.
- Zero duplication: reused existing TTS/notification publish paths.
- Anti-race: idempotent cooldown guard per session; no new parallel state owner.
- Flags lifecycle: no new flags introduced.

## Verification
- Updated tests in `tests/test_browser_install_contracts.py`:
  - Added `test_setup_in_progress_tts_is_throttled`.
- Test run:
  - `pytest -q tests/test_browser_install_contracts.py`
  - Result: `6 passed`.
