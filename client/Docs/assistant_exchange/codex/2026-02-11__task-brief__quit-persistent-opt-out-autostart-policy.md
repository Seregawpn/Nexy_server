# Quit Persistent Opt-Out for Autostart Policy

## Метаданные
- Ассистент: codex
- Тип: task-brief
- Дата: 2026-02-11

## Diagnosis
Требование: автозапуск после reboot должен работать только если ранее не был нажат `Quit`.

## Root Cause
`USER_QUIT_INTENT` был только runtime-состоянием; после перезапуска не сохранялся. Из-за этого auto-repair мог снова включать автозапуск.

## Changes
- В `AutostartManagerIntegration` добавлен persistent opt-out флаг:
  - `~/Library/Application Support/Nexy/autostart_user_opt_out.flag` (через `get_user_data_dir`).
- На `app.shutdown` при `user_initiated`:
  - ставится opt-out,
  - выполняется `disable_autostart()` (удаление/выгрузка LaunchAgent).
- В policy `_should_repair_autostart(...)` добавлен guard `user_opt_out`.
- В `autostart.status_checked` добавлено поле `user_opt_out`.
- Добавлен тест `test_should_not_repair_when_user_opt_out`.

## Verification
- `pytest -q tests/test_autostart_repair_policy.py` -> 4 passed
- `python3 -m py_compile integration/integrations/autostart_manager_integration.py tests/test_autostart_repair_policy.py` -> ok
