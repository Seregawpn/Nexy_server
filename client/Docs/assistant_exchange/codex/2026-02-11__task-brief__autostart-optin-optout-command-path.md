# Autostart Opt-In/Opt-Out Command Path

## Метаданные
- Ассистент: codex
- Тип: task-brief
- Дата: 2026-02-11

## Diagnosis
Требовался явный путь вернуть автозапуск после persistent opt-out (Quit), без обхода центра управления.

## Root Cause
Был только implicit auto-repair path; explicit команды enable/disable через EventBus отсутствовали.

## Changes
- В `AutostartManagerIntegration` добавлены subscriptions:
  - `autostart.enable_requested`
  - `autostart.disable_requested`
- Добавлены handlers:
  - `_on_enable_requested`: снимает opt-out, включает LaunchAgent, публикует `autostart.command_result`.
  - `_on_disable_requested`: ставит opt-out, отключает LaunchAgent, публикует `autostart.command_result`.
- Оба handlers выполняются под `self._status_check_lock`.
- Документация `Docs/ARCHITECTURE_OVERVIEW.md` синхронизирована по подпискам/публикациям.
- Тесты расширены (`tests/test_autostart_repair_policy.py`): 8 passed.

## Verification
- `pytest -q tests/test_autostart_repair_policy.py` -> 8 passed
- `python3 -m py_compile integration/integrations/autostart_manager_integration.py tests/test_autostart_repair_policy.py` -> ok
