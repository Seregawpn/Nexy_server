# gRPC Session ID Break

## Метаданные
- Ассистент: codex
- Тип: analysis
- Дата: 2026-01-12
- ID (INS-###): <из Docs/CRM_INSTRUCTION_REGISTRY.md>

## Diagnosis
gRPC запросы не уходят, потому что session_id передается как float, а gRPC клиент ожидает строку и вызывает .strip().

## Root Cause
Несогласованность типов session_id → float из InputProcessing/VoiceRecognition → gRPC клиент проверяет строку → исключение `'float' object has no attribute 'strip'` → поток запроса прерывается до отправки.

## Optimal Fix
Стандартизировать session_id как строку в ApplicationStateManager и в событиях EventBus, убрать конвертацию в float.

## Verification
- Проверить, что session_id в событиях `voice.*`/`grpc.*` строка.
- Повторить запрос: нет ошибки `.strip`, есть `grpc.request_started` и ответные чанки.

## Запрос/цель
Проанализировать, почему клиент не отправляет запрос на сервер.

## Контекст
- Файлы: `modules/grpc_client/core/grpc_client.py`, `integration/integrations/input_processing_integration.py`, `integration/integrations/voice_recognition_integration.py`, `integration/core/state_manager.py`
- Документы: `Docs/ARCHITECTURE_OVERVIEW.md`, `Docs/PROJECT_REQUIREMENTS.md`
- Ограничения: единый источник истины для session_id

## Решения/выводы
- Фактическая ошибка соответствует несоответствию типов session_id.

## Открытые вопросы
- Нужно ли принудительно валидировать session_id в state_manager на формат uuid?

## Следующие шаги
- Привести session_id к строке в InputProcessing/VoiceRecognition и при публикации событий.
