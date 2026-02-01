# UUID4 Session Source Fix

## Метаданные
- Ассистент: codex
- Тип: analysis
- Дата: 2026-01-12
- ID (INS-###): <из Docs/CRM_INSTRUCTION_REGISTRY.md>

## Diagnosis
session_id генерировался как timestamp/monotonic и распространялся по событиям, что ломало gRPC на .strip().

## Root Cause
Источник session_id в input_processing создавал float → gRPC boundary ожидал строку uuid4 → исключение до отправки.

## Optimal Fix
Генерировать uuid4 в input_processing и передавать только строковый session_id; в voice_recognition убрать float-конвертацию; добавить guard в grpc_client_integration.

## Verification
Перезапуск клиента, логи с uuid4 в session_id, отсутствие ошибки `.strip()` и появление `grpc.request_started`.

## Запрос/цель
Внести необходимые правки для стабилизации gRPC отправки и единообразного session_id.

## Контекст
- Файлы: `integration/integrations/input_processing_integration.py`, `integration/integrations/voice_recognition_integration.py`, `integration/integrations/grpc_client_integration.py`, `integration/core/selectors.py`

## Решения/выводы
- session_id теперь формируется как uuid4 на источнике и валидируется на gRPC boundary.

## Открытые вопросы
- Нужна ли отдельная метрика/лог при обнаружении невалидного session_id на boundary?

## Следующие шаги
- Перезапуск клиента и проверка цепочки PTT → gRPC.
