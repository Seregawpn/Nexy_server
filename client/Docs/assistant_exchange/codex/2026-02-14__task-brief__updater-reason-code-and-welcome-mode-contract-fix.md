# Task Brief: Updater reason_code + Welcome mode.request contract fix

Date: 2026-02-14
Owner: codex

## Scope
Implemented only requested changes:
1. Add stable `reason_code` to `updater.update_failed` event payload.
2. Fix Welcome contract: stop sending `mode.request(PROCESSING)` without session context.

## Changes

### 1) updater.update_failed reason_code
- File: `integration/integrations/updater_integration.py`
- Added `_classify_update_error(exc)` helper.
- `updater.update_failed` payload now includes:
  - `reason_code`
- Current mappings:
  - `install_permission_denied`
  - `download_redirect_error`
  - `network_timeout`
  - `network_ssl_error`
  - `manifest_error`
  - `artifact_verification_failed`
  - `update_failed_unknown`

### 2) welcome_message mode.request contract
- File: `integration/integrations/welcome_message_integration.py`
- Removed publish of:
  - `mode.request` with `target=PROCESSING` in welcome playback path
- Replaced with explicit log that processing request is skipped for welcome playback (no processing session).

## Why
- `reason_code` removes string-parsing ambiguity for UI/logic consumers.
- Welcome playback is not a user processing session; publishing PROCESSING without valid session context caused mode manager rejections.

## Validation
- `python3 -m py_compile integration/integrations/updater_integration.py integration/integrations/welcome_message_integration.py` passed.

## Out of Scope
- No changes to install permission flow, retry/cooldown policy, or first-run orchestration logic.
