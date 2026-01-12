# Session ID Guards

## Метаданные
- Ассистент: codex
- Тип: task-brief
- Дата: 2026-01-12
- ID (INS-###): INS-008

## Diagnosis
session_id мог быть нестроковым и попадал в state/gRPC, что ломало отправку.

## Root Cause
отсутствие централизованной валидации session_id на Source of Truth и на серверной границе.

## Optimal Fix
добавлены централизованные guards в ApplicationStateManager и проверка uuid4 на gRPC сервере.

## Verification
ручная проверка логов на invalid session_id и отсутствие AttributeError; тесты не запускались.

## Запрос/цель
починить логику session_id в соответствии с архитектурой и централизовать проверки.

## Контекст
- Файлы: integration/core/state_manager.py, integration/integrations/grpc_client_integration.py, server/server/modules/grpc_service/core/grpc_server.py
- Документы: Docs/ARCHITECTURE_OVERVIEW.md, Docs/PROJECT_REQUIREMENTS.md
- Ограничения: централизация Source of Truth, минимальные локальные guards

## Решения/выводы
- Валидация uuid4 добавлена в StateManager и gRPC server boundary.
- gRPC client fail-fast больше не вызывает .strip() на non-str.

## Открытые вопросы
- Нужна ли синхронная ошибка INVALID_ARGUMENT через context.abort (вместо StreamResponse.error_message)?

## Следующие шаги
- Прогнать сценарий PTT и убедиться в корректном gRPC старте.
