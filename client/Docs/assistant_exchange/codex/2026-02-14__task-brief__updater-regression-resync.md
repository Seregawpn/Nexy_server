# Task Brief: updater regression resync

## Context
- Re-synced updater flow with previously agreed behavior after regression.
- Focus: remove duplicate startup/scheduled attempts and stabilize update failure contract for notification/UI.

## Changes
1. `integration/integrations/updater_integration.py`
- Added startup retry guard window (`_last_startup_attempt_ts`, `_startup_retry_block_sec=120s`) to prevent immediate scheduled re-run after startup attempt.
- Added stable `reason_code` in `updater.update_failed` payload.
- Added centralized classifier `_classify_update_error()` for permission/network/security/verification/artifact/unknown classes.

2. `integration/integrations/update_notification_integration.py`
- Removed unsubscribe-on-complete and unsubscribe-on-failed behavior to keep handlers active for full app runtime.
- Switched error speech to reason-code mapping (`_error_phrase_for_reason`) with stable English phrases.

3. `integration/integrations/updater_integration.py` (first-run conflict guard)
- Extended update preconditions to block not only `first_run_in_progress`, but also snapshot states:
  - `first_run` (`StateKeys.FIRST_RUN_REQUIRED`)
  - `restart_pending` (`StateKeys.PERMISSIONS_RESTART_PENDING`)
- This prevents updater checks/install attempts during first-run and restart handoff windows.

## Verification
- `python3 -m py_compile integration/integrations/updater_integration.py integration/integrations/update_notification_integration.py` passed.

## Notes
- Core install failure for `/Applications/Nexy.app` without elevated rights remains architectural/OS-level and requires privileged install path (PKG/SMJobBless/prompted admin flow) outside this patch scope.
