# Task Brief: UpdateNotification session_id UUID normalization

Date: 2026-02-14
Owner: codex

## Context
In updater voice notifications, `UpdateNotificationIntegration` generated `session_id` as `update_notification_<timestamp>`. Runtime selectors/validators expect UUID-format `session_id`, causing warnings like `badly formed hexadecimal UUID string`.

## Diagnosis
- Source of Truth for session_id format is runtime event/session contract (UUID string).
- `update_notification_integration.py` violated that contract with a custom non-UUID identifier.

## Change
- File: `integration/integrations/update_notification_integration.py`
- Replaced session id generation:
  - from: `f"update_notification_{int(time.time() * 1000)}"`
  - to: `str(uuid.uuid4())`
- Added import: `import uuid`

## Why this is architecture-safe
- No new state/flags added.
- No ownership changes.
- Aligns integration with existing global session_id contract.

## Validation
- `python3 -m py_compile integration/integrations/update_notification_integration.py` passed.
- `git diff` confirms only UUID generation change.

## Expected Runtime Effect
- No more `Session ID validation failed ... badly formed hexadecimal UUID string` from update notification sessions.
- Update TTS flow remains unchanged functionally.
