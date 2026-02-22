# Analysis: first-run appears on every startup

## Context
Проверка причины, почему при каждом запуске создается впечатление повторного first-run.

## Diagnosis
SoT `permission_ledger.json` не сбрасывается: в обеих директориях (`Nexy`, `Nexy-Dev`) `phase=completed`.
Проблема в startup-поведенческой интерпретации: first-run owner-path стартует V2 интеграцию на каждом запуске для re-emit completion-событий, что визуально/по логам может выглядеть как «первый запуск снова».

## Root Cause
1. `SimpleModuleCoordinator` синхронизирует состояние как `completed=true` из ledger.
2. `FirstRunPermissionsIntegration.start()` все равно запускает V2 orchestrator (`start()` вызывается всегда) и логирует путь «Запускаем V2 систему разрешений», если `is_first_run_complete()!=True` в момент проверки.
3. В логах подтверждено: затем `PermissionOrchestrator` пишет `Ledger already completed ... Re-emitted completed from ledger`.
4. Следствие: не реальный reset SoT, а повторная публикация first-run completion-цепочки на старте.

## Evidence
- `/Users/sergiyzasorin/Library/Application Support/Nexy/permission_ledger.json` -> `phase=completed`
- `/Users/sergiyzasorin/Library/Application Support/Nexy-Dev/permission_ledger.json` -> `phase=completed`
- `/Users/sergiyzasorin/Library/Logs/Nexy/nexy.log`:
  - `[PERMISSIONS] Synced first_run state from ledger (in_progress=False, completed=True ...)`
  - `[FIRST_RUN_PERMISSIONS] Запускаем V2 систему разрешений`
  - `[ORCHESTRATOR] Ledger already completed ... Re-emitted completed from ledger`

## Verification
- Проверен текущий runtime ledger в `Nexy` и `Nexy-Dev`.
- Проверена последовательность логов startup вокруг first-run owner-path.
- Проверен код owner-цепочки:
  - `integration/core/simple_module_coordinator.py`
  - `integration/integrations/first_run_permissions_integration.py`
  - `modules/permissions/v2/integration.py`
  - `modules/permissions/v2/orchestrator.py`

## Информация об изменениях
- Что изменено:
  - Добавлен диагностический отчет.
- Список файлов:
  - `Docs/assistant_exchange/codex/2026-02-21__analysis__first-run-reappears-on-every-start.md`
- Причина/цель изменений:
  - Зафиксировать root cause и доказательства по симптомам «first-run на каждом запуске».
- Проверка:
  - Сопоставлены кодовые owner-path и фактические runtime-логи/ledger файлы.
