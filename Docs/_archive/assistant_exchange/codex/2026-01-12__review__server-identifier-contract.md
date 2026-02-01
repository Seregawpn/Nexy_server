# Server Identifier Contract Review

## Метаданные
- Ассистент: codex
- Тип: review
- Дата: 2026-01-12
- ID (INS-###): INS-005

## Diagnosis
Правки в контракте идентификаторов в целом корректны, но есть риск поведения для старых клиентов (session_id теперь обязательный), нужен явный note о breaking change.

## Root Cause
Ужесточение входных проверок без явной совместимости с клиентами без session_id.

## Optimal Fix
Явно зафиксировать breaking change в документации и/или добавить режим degrade (по согласованию).

## Verification
Проверить StreamAudio без session_id/hardware_id — ожидается error_message; старые клиенты должны быть уведомлены.

## Запрос/цель
Оценка корректности изменений в server идентификаторах и guard.

## Контекст
- Файлы: server/server/modules/grpc_service/core/grpc_server.py, server/server/integrations/workflow_integrations/streaming_workflow_integration.py, server/server/config/unified_config.yaml, server/server/config/unified_config.py
- Документы: server/server/modules/grpc_service/streaming.proto

## Решения/выводы
- Поле InterruptResponse исправлено на message (соответствует proto).
- Guard по hardware_id сделан условным через конфиг.

## Найденные проблемы (если review)
- Средняя: session_id теперь обязателен; при старых клиентах это breaking change.

## Открытые вопросы
- Нужно ли временно поддерживать degrade режим при отсутствии session_id?

## Следующие шаги
- Зафиксировать поведение в документации и/или в релиз‑нотах.

## Итоговый статус
**ЧАСТИЧНОЕ**
