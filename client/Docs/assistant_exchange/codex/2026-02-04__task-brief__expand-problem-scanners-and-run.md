# Task Brief: expand problem scanners and run

## Goal
Расширить централизованный сканер, чтобы он выдавал единый список проблем по нескольким классам проверок, и выполнить сканирование.

## Changes
1. `scripts/scan_problem_list.py`
- Добавлены сканеры:
  - `ruff`
  - `basedpyright` (если доступен)
  - `scripts/verify_imports.py`
  - `scripts/verify_no_direct_state_access.py`
  - `scripts/check_dependency_violations.py`
  - `pytest` (включается флагом `--with-tests`)
- Добавлена агрегация статусов каждого сканера в summary.
- Добавлена агрегация всех найденных проблем в единый `issues` список.
- Добавлен `PYTHONPATH` в subprocess env для стабильного запуска сканеров.

2. `scripts/problem_scan.sh`
- Обновлен для запуска полного скана по умолчанию:
  - `scan_problem_list.py --with-tests`

## Verification
- `./.venv/bin/python scripts/scan_problem_list.py --with-tests` -> OK
- `scripts/problem_scan.sh` -> OK
- Сформированы отчеты:
  - `build_logs/problem_scan_latest.json`
  - `build_logs/problem_scan_latest.md`

## Current scan result
- `total_issues: 1`
- Найдена проблема в `pytest` scan:
  - `ModuleNotFoundError: No module named 'client.modules'`
  - during collection: `tests/test_coordinator_critical_subscriptions.py`

## Result
- Теперь есть действительно централизованный сканер с несколькими источниками проблем и единым списком issue.
