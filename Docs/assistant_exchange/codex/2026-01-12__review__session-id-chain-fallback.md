# session-id-chain-fallback

## Метаданные
- Ассистент: codex
- Тип: review
- Дата: 2026-01-12
- ID (INS-###): INS-005

## Diagnosis
Часть цепочки session_id восстановлена, но есть места, где событие все еще может быть отброшено при пустом/невалидном session_id.

## Root Cause
Проверка session_id до fallback → ранний return в _on_recording_stop → отсутствие публикации событий при defer сценарии.

## Optimal Fix
Добавить fallback на state_manager до сравнения session_id в _on_recording_stop и логировать mismatch.

## Verification
Логи должны содержать TRACE phase=stt.done и TRACE phase=grpc.start с одинаковым uuid4.

## Запрос/цель
Проверить корректность правок по восстановлению session_id в цепочке voice → gRPC.

## Контекст
- Файлы: integration/integrations/voice_recognition_integration.py, integration/integrations/grpc_client_integration.py
- Документы: Docs/ARCHITECTURE_OVERVIEW.md, Docs/PROJECT_REQUIREMENTS.md
- Ограничения: единственный источник истины session_id — ApplicationStateManager

## Решения/выводы
- Fallback в _publish_v2_completed/_publish_v2_failed и _on_voice_completed реализован корректно.
- В _on_recording_stop fallback добавлен, но до него есть ранний return при mismatch.

## Найденные проблемы (если review)
- Medium: _on_recording_stop возвращает до fallback при session mismatch, из-за чего deferred результат может быть утерян. Файл: integration/integrations/voice_recognition_integration.py

## Открытые вопросы
- Почему в рантайме появляется session_id в формате timestamp (не uuid4)?

## Следующие шаги
- Перенести fallback/нормализацию session_id до проверки active_session_id в _on_recording_stop.
- Повторить лог-проверку цепочки stt.done → grpc.start.
