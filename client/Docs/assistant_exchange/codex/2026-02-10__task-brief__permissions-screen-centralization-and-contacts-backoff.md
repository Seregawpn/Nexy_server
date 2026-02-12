# Task Brief — Screen permission centralization + Contacts helper backoff

## Context
После анализа `log.md` обнаружены доп. проблемы помимо PTT-click:
- дублированный локальный screen-capture preflight в ScreenshotCaptureIntegration;
- повторяющиеся transient ошибки Contacts helper (`Code=7`, `Full Sync Required`, `Invalid Change History Anchor`).

## Diagnosis
1. ScreenCapture permission проверялся в двух местах (local probe + permissions owner), что увеличивает риск конфликтных TCC-путей.
2. Contacts helper при transient system errors мог вызываться повторно, создавая шум и нестабильность.

## Implemented changes

### 1) Screen permission path centralized
- File: `integration/integrations/screenshot_capture_integration.py`
- Change:
  - В `start()` убран локальный вызов `await self._check_screen_capture_permissions()`.
  - Оставлен только owner-path через `permissions.check_required` (`_ensure_screen_permission_status`).
- Effect:
  - Единый источник истины для статуса screen permission: PermissionsIntegration.
  - Меньше дублей TCC check path.

### 2) Contacts helper transient-error backoff
- File: `modules/messages/contact_resolver.py`
- Added:
  - `_CONTACTS_HELPER_BACKOFF_UNTIL`, `_CONTACTS_HELPER_BACKOFF_REASON`, `_CONTACTS_HELPER_BACKOFF_SEC`.
  - `_contacts_helper_backoff_active()`, `_activate_contacts_helper_backoff(...)`.
  - `_is_contacts_transient_error(stderr)` c маркерами:
    - `code=7`
    - `full sync required`
    - `invalid change history anchor`
    - `store registration failed`
    - `acmonitoredaccountstore`
- Applied in:
  - `get_name_from_contacts_framework(...)`
  - `find_contacts_by_name(...)`
- Behavior:
  - При transient ошибках включается backoff на 120 сек и helper временно suppress-ится.
  - Исключается storm повторных helper-вызовов в деградированном состоянии.

## Architecture fit
- Source of truth preserved:
  - Screen permission: PermissionsIntegration owner.
  - Contacts lookup owner remains `contact_resolver`, без новых side paths.
- No cross-layer bypasses added.

## Verification
- `python3 -m py_compile integration/integrations/screenshot_capture_integration.py modules/messages/contact_resolver.py integration/integrations/input_processing_integration.py` ✅
- `PYTHONPATH=. pytest -q tests/test_interrupt_playback.py -k "release_suppressed_when_combo_still_pressed_early_after_start or release_not_suppressed_when_combo_not_pressed"` ✅ (2 passed)
- `PYTHONPATH=. pytest -q tests/test_microphone_activation.py -k "long_press_publishes_recording_start or release_guarantees_recording_stop"` ⚠️
  - 1 failure is pre-existing test mismatch (`_handle_key_release` vs `_handle_release`), not introduced by these changes.

## Expected runtime effect
- Screenshot integration больше не запускает конкурирующий local preflight и полагается на centralized permissions state.
- Contacts helper при transient системных сбоях не штормит вызовами и логами, приложение остается работоспособным через fallback-ветки.
