# Task Brief: Suppress Auto-Update Loops After Permission Denied

Date: 2026-02-15
Owner: Codex

## Context
Updater retried immediately after a failed installation with:
`PermissionError: [Errno 13] Permission denied: '/Applications/Nexy.app' -> '/Applications/Nexy.app.backup'`.
This caused repeated download/install attempts in the same app session.

## Change
Updated `integration/integrations/updater_integration.py`:
- Added session-level guard:
  - `_suppress_auto_update_until_restart: bool`
  - `_last_update_fail_reason_code: str | None`
- In `_execute_update(trigger)`:
  - If suppression is active and trigger is `startup` or `scheduled`, publish `updater.update_skipped` with
    `reason_code=permission_denied_suppressed` and return without retry.
  - On exception classification:
    - store `reason_code`
    - if `reason_code == permission_denied`, enable suppression.
  - On successful completion, clear suppression flags.

## Architecture Fit
- Owner/SoT remains `UpdaterIntegration`.
- No new parallel owner introduced.
- Keeps update policy centralized and event-driven.

## Verification
- Compile check passed:
  - `python3 -m py_compile integration/integrations/updater_integration.py`
- Expected runtime behavior:
  - After one `updater.update_failed` with `reason_code=permission_denied`, no new auto `updater.update_started` in same session.
  - Instead, `updater.update_skipped` with `reason_code=permission_denied_suppressed`.
