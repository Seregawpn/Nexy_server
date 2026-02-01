# Duplicates, Conflicts, Races in Permissions Flow

## Метаданные
- Ассистент: codex
- Тип: analysis
- Дата: 2026-01-24
- ID (INS-###): INS-000 (registry missing)

## Diagnosis
Есть дубли источников порядка/критичности разрешений и потенциальные конфликты между V2 restart-handler и PermissionRestartIntegration; часть потоков противоречит канону first_run.

## Root Cause
Сосуществуют V1 спецификация/конфиг и V2 pipeline без единого владельца → дубли и расхождения в поведении и рестарте.

## Optimal Fix
Требуется централизация единого источника порядка/критичности и единственного рестарт-координатора (V2 или PermissionRestartIntegration).

## Verification
Сверить порядок и рестарт с `Docs/first_run_flow_spec.md` и логами first-run; убедиться, что только один путь рестарта активен.

## Запрос/цель
Анализ дублей/конфликтов/гонок в текущем flow разрешений.

## Контекст
- Файлы: config/unified_config.yaml, modules/permissions/v2/orchestrator.py, modules/permissions/v2/integration.py, integration/integrations/permission_restart_integration.py, Docs/first_run_flow_spec.md
- Документы: Docs/PROJECT_REQUIREMENTS.md, Docs/ARCHITECTURE_OVERVIEW.md

## Решения/выводы
- Дубли: порядок разрешений задан в `integrations.permissions.required_permissions` и `integrations.permissions_v2.order`.
- Конфликт: V2 использует restart-handler напрямую, PermissionRestartIntegration слушает `permissions.first_run_restart_pending` — потенциально два рестарт-пути.
- Конфликт со спецификацией: канон first_run предписывает «без status pre-checks», V2 делает probe/polling.

## Открытые вопросы
- Отсутствует Docs/CRM_INSTRUCTION_REGISTRY.md; нужен источник INS-###.

## Следующие шаги
- Выбрать единый Source of Truth для порядка/критичности и рестарта.
