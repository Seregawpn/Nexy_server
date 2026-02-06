# Task Brief: single restart after permissions + duplicate launch fix

## Goal
- Обеспечить не более одного авто-перезапуска в V2 permission flow.
- Исправить ложное нераспознавание уже запущенного Nexy (duplicate guard).

## Changes
1. `modules/instance_manager/core/instance_manager.py`
- Убрана конфликтная проверка `cmdline_check`, из-за которой живой `.app` процесс считался невалидным.
- Добавлена более надежная packaged-проверка через `process.exe()` и путь к `Nexy.app/Contents/MacOS/Nexy`.

2. `modules/permissions/v2/orchestrator.py`
- Добавлен hard guard: если `ledger.restart_count >= 1`, повторный auto-restart запрещен.
- Guard стоит в двух местах:
  - `_decide_after_first_run()`
  - `_enter_restart_sequence()`

## Why
- Дубликаты возникали из-за очистки валидного lock и повторного запуска.
- Повторные рестарты после permission flow должны быть централизованно ограничены до одного.

## Validation
- `python3 -m py_compile modules/permissions/v2/orchestrator.py modules/instance_manager/core/instance_manager.py`

## Expected result
- После выдачи разрешений максимум один авто-рестарт.
- Уже активный Nexy корректно определяется, новые дубликаты не стартуют.
