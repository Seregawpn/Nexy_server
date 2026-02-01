# Permissions Config Centralization

## Метаданные
- Ассистент: codex
- Тип: task-brief
- Дата: 2026-01-24
- ID (INS-###): INS-000 (registry missing)

## Diagnosis
Дубли источников порядка разрешений и второй рестарт-путь создавали конфликты.

## Root Cause
Параллельные конфиги и рестарт-координаторы без единого владельца.

## Optimal Fix
Синхронизировать порядок в `integrations.permissions.required_permissions` с `permissions_v2.order` и отключить `permission_restart` для first-run.

## Verification
Проверить порядок в конфиге и что рестарт выполняется единожды через V2.

## Запрос/цель
Централизовать конфиг и убрать конфликтующий рестарт-путь.

## Контекст
- Файлы: config/unified_config.yaml
- Документы: Docs/PROJECT_REQUIREMENTS.md, Docs/first_run_flow_spec.md

## Решения/выводы
- `permission_restart.enabled` отключен.
- `required_permissions` синхронизирован с V2.

## Открытые вопросы
- Отсутствует Docs/CRM_INSTRUCTION_REGISTRY.md; нужен источник INS-###.

## Следующие шаги
- Прогон first-run на чистых разрешениях.
