# Autostart Quit Race and Policy Centralization

## Метаданные
- Ассистент: codex
- Тип: task-brief
- Дата: 2026-02-11

## Diagnosis
После ввода persistent opt-out оставались риски: shutdown-path не был сериализован с status/repair path, а проверки quit/opt-out были частично дублированы.

## Root Cause
`_on_app_shutdown` изменял состояние автозапуска без общего lock; policy читалась из разных мест напрямую.

## Changes
- `_on_app_shutdown` переведен под `async with self._status_check_lock`.
- Введены централизованные accessors:
  - `_is_user_quit_intent(...)`
  - `_is_autostart_opted_out()`
- `_should_repair_autostart(...)` использует централизованные accessors.
- `autostart.status_checked` публикует `user_opt_out` через единый accessor.
- Тесты дополнены:
  - `test_should_not_repair_when_user_opt_out`
  - `test_user_quit_intent_accessor_prefers_event_payload`

## Verification
- `pytest -q tests/test_autostart_repair_policy.py` -> 6 passed
- `python3 -m py_compile integration/integrations/autostart_manager_integration.py tests/test_autostart_repair_policy.py` -> ok
