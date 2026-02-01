# Permissions First-Run Stabilization

## Метаданные
- Ассистент: codex
- Тип: task-brief
- Дата: 2026-01-24
- ID (INS-###): INS-000 (registry missing)

## Diagnosis
First-run permissions V2 разблокирует модули слишком рано и не инициирует рестарт после выдачи критичных разрешений.

## Root Cause
Неверные ссылки на состояние V2 (ledger/hard_permissions) + игнор флагов рестарта из конфига → gating пропускает модули и рестарт не запускается.

## Optimal Fix
Исправить чтение ledger/hard_permissions для gate, учитывать restart.require_* из unified_config и корректно формировать legacy payload.

## Verification
Проверить, что после первого запуска сначала идут последовательные диалоги, затем рестарт; зависимые модули не стартуют до pass по hard.

## Запрос/цель
Стабилизировать first-run: последовательные запросы, корректный gate, рестарт после выдачи критичных разрешений.

## Контекст
- Файлы: integration/integrations/first_run_permissions_integration.py, modules/permissions/v2/orchestrator.py, modules/permissions/v2/integration.py, modules/permissions/v2/config_loader.py, modules/permissions/v2/types.py, config/unified_config.yaml
- Документы: Docs/PROJECT_REQUIREMENTS.md, Docs/first_run_flow_spec.md, Docs/ARCHITECTURE_OVERVIEW.md
- Ограничения: без реархитектуры, сохранить централизованный координатор

## Решения/выводы
- Gate теперь читает реальные статусы V2 и блокирует старт зависимых модулей до hard=pass.
- Рестарт после first-run управляется через флаги конфигурации.

## Открытые вопросы
- Отсутствует Docs/CRM_INSTRUCTION_REGISTRY.md; нужен источник INS-###.

## Следующие шаги
- Прогнать first-run вручную и убедиться в рестарте после выдачи критичных.
