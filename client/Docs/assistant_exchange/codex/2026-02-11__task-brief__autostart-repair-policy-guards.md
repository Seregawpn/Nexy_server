# Autostart Repair Policy Guards

## Метаданные
- Ассистент: codex
- Тип: task-brief
- Дата: 2026-02-11

## Diagnosis
`auto_repair` не имел единой policy-ветки и был привязан к legacy-сценарию, из-за чего поведение включения автозапуска было неочевидным.

## Root Cause
Repair-логика находилась внутри блока `legacy_launch_agent_exists`, без централизованных guard-условий по lifecycle/state.

## Changes
- В `AutostartManagerIntegration` добавлен единый policy-метод `_should_repair_autostart(...)`.
- Repair теперь выполняется по условию `auto_repair=true && launch_agent_missing`, а не только при наличии legacy LaunchAgent.
- Добавлены guard-блокировки repair:
  - `USER_QUIT_INTENT`
  - `update_in_progress`
  - `first_run_in_progress`
  - `restart_pending`
- Legacy cleanup оставлен отдельной независимой веткой.
- Добавлены unit-тесты policy:
  - `tests/test_autostart_repair_policy.py` (3 сценария)

## Verification
- `pytest -q tests/test_autostart_repair_policy.py` -> 3 passed
- `python3 -m py_compile integration/integrations/autostart_manager_integration.py tests/test_autostart_repair_policy.py` -> ok
