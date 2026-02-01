# First-Run Permissions Ledger Gate

## Метаданные
- Ассистент: codex
- Тип: task-brief
- Дата: 2026-01-30
- ID (INS-###): N/A

## Diagnosis
First-run разрешения пропускались из-за флага и dev‑bypass, а не ledger.

## Root Cause
Флаг `permissions_first_run_completed.flag` и auto‑created dev flag использовались как gate → V2 pipeline не запускался.

## Optimal Fix
Перенести gate на `permission_ledger.json`, ограничить dev‑bypass только dev и без авто‑создания.

## Verification
- Очистить `permissions_first_run_completed.flag` и `permission_ledger.json`
- Запуск .app вызывает `permissions.first_run_started` и TCC/Settings диалоги
- Повторный запуск при completed‑ledger не вызывает wizard

## Запрос/цель
Сделать first-run: запрос разрешений → только после завершения создать флаг.

## Контекст
- Файлы: `integration/integrations/first_run_permissions_integration.py`, `modules/permissions/v2/integration.py`, `integration/core/simple_module_coordinator.py`
- Документы: `Docs/PROJECT_REQUIREMENTS.md` (REQ-010)
- Ограничения: без реархитектуры

## Решения/выводы
- Gate переведён на ledger.
- Dev‑bypass отключён для .app и не создаётся автоматически.

## Открытые вопросы
- Нужен ли явный флаг/конфиг для dev‑bypass (если да — зарегистрировать в `Docs/FEATURE_FLAGS.md`).

## Следующие шаги
- Проверка первого запуска из /Applications.
