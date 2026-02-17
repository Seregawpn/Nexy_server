# Task Brief: Clear first-run flags (Nexy + Nexy-Dev)

## Context
Запрос пользователя: удалить флаги first-run.

## Verification
Проверены директории:
- `/Users/sergiyzasorin/Library/Application Support/Nexy`
- `/Users/sergiyzasorin/Library/Application Support/Nexy-Dev`

Удалены целевые first-run артефакты:
- `permissions_first_run_completed.flag`
- `permission_ledger.json`
- `permissions_granted.flag` (legacy)
- `restart_completed.flag` (legacy)

Пост-проверка `ls | rg` не находит перечисленные файлы в обеих директориях.

## Информация об изменениях
- Что изменено:
  - Удалены first-run флаги/ledger в runtime данных пользователя для `Nexy` и `Nexy-Dev`.
- Список файлов:
  - `/Users/sergiyzasorin/Library/Application Support/Nexy/permissions_first_run_completed.flag`
  - `/Users/sergiyzasorin/Library/Application Support/Nexy/permission_ledger.json`
  - `/Users/sergiyzasorin/Library/Application Support/Nexy/permissions_granted.flag`
  - `/Users/sergiyzasorin/Library/Application Support/Nexy/restart_completed.flag`
  - `/Users/sergiyzasorin/Library/Application Support/Nexy-Dev/permissions_first_run_completed.flag`
  - `/Users/sergiyzasorin/Library/Application Support/Nexy-Dev/permission_ledger.json`
  - `/Users/sergiyzasorin/Library/Application Support/Nexy-Dev/permissions_granted.flag`
  - `/Users/sergiyzasorin/Library/Application Support/Nexy-Dev/restart_completed.flag`
- Причина/цель изменений:
  - Принудительно сбросить first-run состояние для повторного clean first launch.
- Проверка:
  - Файлы удалены, повторная проверка подтверждает отсутствие.
