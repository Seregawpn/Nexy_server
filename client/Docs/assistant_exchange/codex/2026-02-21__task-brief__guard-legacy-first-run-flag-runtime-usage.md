# Task Brief: guard legacy first-run flag runtime usage

## Goal
Предотвратить возврат второго source-of-truth: запретить runtime-использование `permissions_first_run_completed.flag` в owner-path клиента.

## Changes
1. `scripts/verify_architecture_guards.py`
- Добавлен regex `LEGACY_FIRST_RUN_FLAG_RE`.
- Добавлена проверка `check_legacy_first_run_flag_runtime_usage()`:
  - сканирует runtime-код (`integration/`, `modules/`, `config/`, `main.py`);
  - добавляет finding `legacy_first_run_flag_runtime_usage` при любом появлении `permissions_first_run_completed.flag`.
- Проверка включена в общий `build_findings()` pipeline.

## Verification
- `python3 scripts/verify_architecture_guards.py`
  - result: `Architecture guards OK (no new violations beyond baseline).`

## Информация об изменениях
- Что изменено:
  - Добавлен архитектурный guard против runtime-чтения/использования legacy first-run flag.
- Список файлов:
  - `scripts/verify_architecture_guards.py`
  - `Docs/assistant_exchange/codex/2026-02-21__task-brief__guard-legacy-first-run-flag-runtime-usage.md`
- Причина/цель изменений:
  - Устранить риск повторного появления второго owner-path и конфликтов между ledger и legacy-флагами.
- Проверка:
  - Локальный запуск архитектурного guard script прошел успешно.
