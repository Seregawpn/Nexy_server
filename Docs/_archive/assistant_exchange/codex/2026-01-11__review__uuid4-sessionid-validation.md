# UUID4 Session ID Validation Review

## Метаданные
- Ассистент: codex
- Тип: review
- Дата: 2026-01-11
- ID (INS-###): INS-005

## Diagnosis
Строгая валидация session_id добавлена, но uuid.UUID() не гарантирует версию 4, и при невалидном session_id генерация нового UUID может ломать корреляцию событий.

## Root Cause
Валидация проверяет формат UUID без проверки версии + нормализация заменяет session_id без синхронизации с incoming event payload.

## Optimal Fix
Проверять version==4 и при невалидном значении либо отклонять обновление, либо генерировать новый session_id и использовать его дальше по цепочке (с явной записью в логах и решением для источника события).

## Verification
Проверить: session_id всегда uuid4, корреляция событий не теряется при невалидном входе.

## Запрос/цель
Проверить корректность добавленной строгой валидации session_id и импорты.

## Контекст
- Файлы: integration/integrations/voice_recognition_integration.py, integration/integrations/input_processing_integration.py, integration/core/selectors.py
- Документы: Docs/PROJECT_REQUIREMENTS.md

## Решения/выводы
- Итоговый статус: ЧАСТИЧНОЕ
- Требуется доработка проверки версии uuid4 и политики замены session_id.

## Найденные проблемы (если review)
- Средний риск: uuid.UUID(value) принимает любые версии UUID, но REQ-009 требует uuid4. integration/integrations/voice_recognition_integration.py#L198, integration/integrations/input_processing_integration.py#L370.
- Средний риск: генерация нового session_id при входе с невалидным id может разорвать корреляцию с событием-источником. integration/integrations/voice_recognition_integration.py#L198, integration/integrations/input_processing_integration.py#L370.
- Низкий риск: TRACE лог в _handle_press пишет timestamp, а session_id теперь uuid4 → несоответствие трассировки. integration/integrations/input_processing_integration.py#L157.

## Открытые вопросы
- Какую политику выбирать при невалидном session_id: отклонение или генерация нового и повторная публикация событий?

## Следующие шаги
- Добавить проверку uuid.version == 4.
- Определить и закрепить политику обработки невалидных session_id.
- Привести TRACE лог к актуальному session_id.
