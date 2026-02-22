# Review: dev startup log check (first-run completed fast-path)

## Scope
Проверка runtime после фикса:
- short-run запуск dev версии,
- анализ startup логов,
- проверка ledger/flags,
- проверка дублей first-run событий.

## Runtime check
- Launch window: `2026-02-21 15:19:49`–`15:20:12` (process PID 45301, controlled SIGTERM).
- Log file with relevant startup entries: `~/Library/Logs/Nexy/nexy.log`.
- Data dir during run: `~/Library/Application Support/Nexy-Dev`.

## Findings
1. Completed fast-path активирован корректно:
- `Ledger shows completed - re-emitting completion without pipeline start`.

2. Full pipeline старт не запускался:
- `Запускаем V2 систему разрешений` в run-window отсутствует.

3. Публикации first-run completion/readiness не дублировались:
- `system.ready_to_greet`: 1 publish
- `permissions.first_run_completed`: 1 publish
- `permissions.first_run_started`: 0 publish
- `permissions.first_run_restart_pending`: 0 publish

4. Ledger/flags после запуска:
- `permission_ledger.json`: `phase=completed`, `restart_count=1`, `updated_at` не изменился
- `permissions_first_run_completed.flag`: отсутствует
- `restart_completed.flag`: присутствует
- `restart_abort.flag`: отсутствует

## Verification commands
- Controlled run: `NEXY_ENV=development NEXY_APP_DATA_SUFFIX=Dev python3 main.py` (22s, then SIGTERM)
- Log grep/count:
  - startup first-run markers in `~/Library/Logs/Nexy/nexy.log`
  - exact publish counters for `permissions.first_run_completed` and `system.ready_to_greet`
- Filesystem check:
  - `~/Library/Application Support/Nexy-Dev/*`
  - ledger JSON summary

## Result
Поведение корректное: конфликтного повторного first-run/restart owner-path в dev старте не обнаружено.

## Информация об изменениях
- Что изменено:
  - Добавлен отчет по проверке runtime логов dev запуска.
- Список файлов:
  - `Docs/assistant_exchange/codex/2026-02-21__review__dev-startup-log-check-first-run-fastpath.md`
- Причина/цель изменений:
  - Подтвердить на фактическом запуске, что fixed completed-fast-path работает без дублей и конфликтных флагов.
- Проверка:
  - Controlled runtime run + log counters + ledger/flags post-check.
