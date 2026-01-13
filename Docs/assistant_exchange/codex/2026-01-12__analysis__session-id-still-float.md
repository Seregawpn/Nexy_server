# session-id-still-float

## Метаданные
- Ассистент: codex
- Тип: analysis
- Дата: 2026-01-12
- ID (INS-###): INS-005

## Diagnosis
Логи показывают session_id в виде timestamp (float), из-за чего selectors возвращают None и gRPC цепочка не стартует.

## Root Cause
Источник session_id не гарантирует uuid4 → state_manager отвергает/не подтверждает session_id → voice.recognition_completed публикуется с None → gRPC не отправляется.

## Optimal Fix
Заставить InputProcessingIntegration нормализовать session_id в uuid4 до публикации событий и записи в state_manager; при невалидном значении генерировать новый uuid4.

## Verification
Проверить, что TRACE phase=recording.start, voice.mic_closed, voice.recognition_completed и grpc.start используют один uuid4.

## Запрос/цель
Разобрать, почему после фикса fallback в voice_recognition/gRPC session_id остается None и цепочка не восстанавливается.

## Контекст
- Файлы: integration/integrations/input_processing_integration.py, integration/integrations/voice_recognition_integration.py, integration/integrations/grpc_client_integration.py
- Документы: Docs/ARCHITECTURE_OVERVIEW.md, Docs/PROJECT_REQUIREMENTS.md
- Ограничения: единственный источник истины session_id — ApplicationStateManager

## Решения/выводы
- Сейчас события приходят с session_id=timestamp, что ломает is_valid_session_id.
- Нужна нормализация/генерация uuid4 на входе в InputProcessingIntegration.

## Открытые вопросы
- Используется ли в рантайме актуальный исходник или старая сборка?

## Следующие шаги
- Добавить/усилить нормализацию session_id в InputProcessingIntegration до публикации событий.
- Проверить, что runtime действительно использует актуальный код.
