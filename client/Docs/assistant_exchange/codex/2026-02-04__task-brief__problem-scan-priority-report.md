# Task Brief

## Context
Нужно перейти от простого сканирования к управляемому списку проблем с приоритетами, чтобы быстро видеть, что чинить первым.

## Changes
- Добавлен скрипт `scripts/problem_scan_prioritize.py`:
  - читает `build_logs/problem_scan_latest.json`
  - строит приоритетный отчет: top tools, top rules, top files, top blocking rules
  - пишет:
    - `build_logs/problem_scan_priority.json`
    - `build_logs/problem_scan_priority.md`
- Обновлен `scripts/problem_scan.sh`:
  - после базового сканирования автоматически запускает `problem_scan_prioritize.py`
- Исправлен стиль импортов в новом скрипте (ruff I001), чтобы не создавать блокирующие ошибки.

## Verification
Запуски:
- `./scripts/problem_scan.sh`
- `REQUIRE_BASEDPYRIGHT_IN_SCAN=true ./scripts/problem_scan_gate.sh`

Результат:
- scan проходит
- gate проходит (`blocking: 0`)
- total issues: `467` (warnings)
- priority-отчеты успешно генерируются

## Snapshot
Top rules:
- `reportAttributeAccessIssue`: 155
- `reportMissingTypeArgument`: 110
- `reportOptionalMemberAccess`: 54

Top files:
- `modules/input_processing/keyboard/keyboard_monitor.py`: 26
- `run_diagnostics.py`: 26
- `modules/screenshot_capture/macos/simple_bridge.py`: 24

## Impact
Теперь есть единый и повторяемый шаг: сканирование + автоматическая приоритизация проблем для пакетного исправления.
