# Task Brief: problem scan list generator

## Goal
Сделать единый сканер, который прогоняет проверки и формирует централизованный список проблем в файлах.

## Changes
1. Добавлен `scripts/scan_problem_list.py`.
- Запускает:
  - `ruff check . --output-format json`
  - `basedpyright --outputjson` (если доступен)
- Формирует единый список проблем (tool/severity/file/line/code/message).
- Пишет отчеты:
  - `build_logs/problem_scan_latest.json`
  - `build_logs/problem_scan_latest.md`

2. Добавлен короткий алиас `scripts/problem_scan.sh`.
- Запускает генератор списка проблем одной командой.

## Verification
- `./.venv/bin/python scripts/scan_problem_list.py` -> OK
- `scripts/problem_scan.sh` -> OK
- Отчет сформирован:
  - `build_logs/problem_scan_latest.json`
  - `build_logs/problem_scan_latest.md`

## Current snapshot
- `total_issues: 0`
- `ruff_status: ok`
- `basedpyright_status: skipped` (в окружении нет basedpyright)

## Result
- Теперь есть отдельный централизованный скан/лист проблем, который можно запускать регулярно и использовать как вход в цикл исправлений.
