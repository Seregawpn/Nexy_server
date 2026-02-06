# Task Brief: quality strict alias

## Goal
Добавить короткую команду-алиас для строгого quality-gate с обязательным basedpyright.

## Changes
1. Добавлен скрипт `scripts/quality_strict.sh`.
- Оборачивает единый pipeline:
  - `./scripts/pre_build_gate.sh --require-basedpyright "$@"`
- Поддерживает проброс любых доп. флагов (`--skip-tests`, `--skip-gui`, и т.д.).

## Verification
- `bash -n scripts/quality_strict.sh` -> OK
- `scripts/quality_strict.sh --skip-tests --skip-gui` -> FAIL ожидаемо в текущем окружении (basedpyright не установлен, strict mode работает корректно)

## Result
- Теперь есть одна короткая команда для строгой проверки:
  - `./scripts/quality_strict.sh`
