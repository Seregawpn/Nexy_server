# grpc-missing-response

## Метаданные
- Ассистент: codex
- Тип: analysis
- Дата: 2026-01-12
- ID (INS-###): INS-005

## Diagnosis
В цепочке voice.recognition_completed → GrpcClientIntegration отсутствует валидный session_id, поэтому gRPC отправка не стартует.

## Root Cause
Потеря/пустой session_id в событиях распознавания → _on_voice_completed игнорирует событие → grpc.request_started/response не публикуются.

## Optimal Fix
Использовать ApplicationStateManager как SoT для session_id при публикации voice.* и при сборке запроса в gRPC интеграции.

## Verification
Проверить логи TRACE phase=stt.done и TRACE phase=grpc.start с одинаковым session_id, затем увидеть grpc.response.

## Запрос/цель
Разобрать, почему клиент не получает ответ от сервера при успешном распознавании.

## Контекст
- Файлы: integration/integrations/voice_recognition_integration.py, integration/integrations/grpc_client_integration.py
- Документы: Docs/ARCHITECTURE_OVERVIEW.md, Docs/PROJECT_REQUIREMENTS.md
- Ограничения: единый источник истины session_id через ApplicationStateManager

## Решения/выводы
- Отсутствие session_id в voice.recognition_completed блокирует gRPC отправку.
- Минимальный фикс — fallback на selector get_current_session_id в voice_recognition и grpc_client интеграциях.

## Открытые вопросы
- Почему в рантайме появляется session_id в формате timestamp (не uuid4)?

## Следующие шаги
- Добавить fallback на session_id из state_manager при публикации voice.recognition_completed.
- Подтвердить цепочку событий в логах.
