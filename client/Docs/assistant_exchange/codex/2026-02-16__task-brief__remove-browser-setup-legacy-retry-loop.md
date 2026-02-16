# Task Brief: Remove browser setup legacy retry loop from integration

## Context
User requested to keep browser flow non-blocking and stop controlling setup-status loop behavior.

## What was changed
- Removed legacy setup queue/retry path from `BrowserUseIntegration._run_process`:
  - removed handling branch for `BROWSER_SETUP_IN_PROGRESS`
  - removed retry loop and delay-based re-dispatch logic
  - removed timeout failure branch tied to setup retry attempts
- Kept single-pass event routing:
  - `BROWSER_TASK_STARTED` / step / terminal events
  - immediate start TTS remains active.
- Removed obsolete setup-wait helper state/method:
  - `_setup_retry_delay_sec`
  - `_setup_retry_max_attempts`
  - `_setup_wait_tts_cooldown_sec`
  - `_setup_wait_last_tts_by_session`
  - `_maybe_announce_setup_in_progress(...)`

## Files
- `integration/integrations/browser_use_integration.py`
- `tests/test_browser_install_contracts.py`

## Verification
- `pytest -q tests/test_browser_install_contracts.py tests/test_browser_module_ready_bypass.py`
  - Result: `8 passed`
- `python3 scripts/verify_architecture_guards.py`
  - Result: `Architecture guards OK`

## Architecture gates
- Single owner preserved: browser UX/event orchestration remains in `BrowserUseIntegration`.
- Zero duplication improved: removed secondary setup-loop control path.
- Anti-race: no additional shared state introduced; fewer retry branches.
- Flag lifecycle: no new flags added.
