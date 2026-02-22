# Review: dev rerun after legacy-flag cleanup (no first-run duplicates)

## Scope
Проверка после удаления legacy-флага и повторного dev запуска:
- есть ли повторный full first-run,
- есть ли дубли first-run completion/readiness,
- корректность ledger/flags.

## Actions
1. Проверено текущее состояние `~/Library/Application Support/Nexy-Dev`.
2. Удалены legacy-флаги (если были):
   - `permissions_first_run_completed.flag`
   - `restart_abort.flag`
3. Выполнен controlled dev run (`NEXY_ENV=development NEXY_APP_DATA_SUFFIX=Dev`, ~24s).
4. Проанализированы startup записи за окно запуска.

## Findings
- До запуска:
  - `permission_ledger.json`: `phase=completed`, `restart_count=1`
  - `permissions_first_run_completed.flag`: отсутствует
- Во время запуска (в `~/Library/Logs/Nexy/nexy.log`):
  - `Ledger shows completed - re-emitting completion without pipeline start` — присутствует
  - `Запускаем V2 систему разрешений` — отсутствует
  - publish count в окне запуска:
    - `permissions.first_run_completed`: 1
    - `system.ready_to_greet`: 1
    - `permissions.first_run_started`: 0
    - `permissions.first_run_restart_pending`: 0
- После запуска:
  - ledger не изменился (`completed`, `restart_count=1`)
  - новых конфликтных first-run флагов не появилось

## Notes
- Для данного запуска активный файл лога: `~/Library/Logs/Nexy/nexy.log`.
- `nexy-dev.log` не обновлялся в этом прогоне.

## Result
Косяк с повторным first-run после удаления legacy-флага не воспроизводится.
Дубли критичных first-run событий в startup-окне отсутствуют.

## Информация об изменениях
- Что изменено:
  - Добавлен отчет проверки runtime после удаления legacy-флагов.
- Список файлов:
  - `Docs/assistant_exchange/codex/2026-02-21__review__dev-rerun-after-flag-clean-no-first-run-duplicates.md`
- Причина/цель изменений:
  - Подтвердить, что после удаления флага и повторного запуска нет дублей/конфликтов first-run.
- Проверка:
  - Controlled runtime run + анализ startup-событий/ledger/flags.
