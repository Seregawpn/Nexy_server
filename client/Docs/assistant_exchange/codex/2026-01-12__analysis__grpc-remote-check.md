# GRPC Remote Check

## Метаданные
- Ассистент: codex
- Тип: analysis
- Дата: 2026-01-12
- ID (INS-###): <из Docs/CRM_INSTRUCTION_REGISTRY.md>

## Diagnosis
Выбор gRPC сервера управляется конфигом и может быть переопределен переменной окружения, из-за чего возможен уход на production при локальном ожидании.

## Root Cause
Глобальная конфигурация + env override → выбор `server` в GrpcClientIntegration → подключение к production адресу при неверной настройке.

## Optimal Fix
Зафиксировать источник истины в unified_config и явно логировать итоговый target (host:port) для каждого подключения.

## Verification
- Проверить `integrations.grpc_client.server` и `NEXY_GRPC_SERVER`.
- Убедиться, что лог показывает нужный host:port при connect.

## Запрос/цель
Определить, может ли клиент подключаться к удаленному серверу для обработки запроса.

## Контекст
- Файлы: `integration/integrations/grpc_client_integration.py`, `config/unified_config.yaml`
- Документы: `Docs/ARCHITECTURE_OVERVIEW.md`, `Docs/PROJECT_REQUIREMENTS.md`
- Ограничения: архитектура EventBus + centralized config

## Решения/выводы
- Подключение к remote возможно при `server=production` или при `NEXY_GRPC_SERVER=production`.

## Открытые вопросы
- Нужно ли запрещать env override в релизной сборке?

## Следующие шаги
- Если нужно жестко запретить remote, зафиксировать `server=local` и убрать/ограничить env override.
