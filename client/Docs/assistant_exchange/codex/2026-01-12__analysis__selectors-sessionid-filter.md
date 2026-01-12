# Selectors Session ID Filter

## Метаданные
- Ассистент: codex
- Тип: analysis
- Дата: 2026-01-12
- ID (INS-###): <из Docs/CRM_INSTRUCTION_REGISTRY.md>

## Diagnosis
Невалидный session_id может попасть в state_manager и возвращаться читателям без фильтрации.

## Root Cause
get_current_session_id() возвращает значение как есть → float/мусор распространяется в события → gRPC падает на .strip().

## Optimal Fix
Фильтровать session_id на уровне selectors.py (uuid4 или None) как централизованный guard чтения.

## Verification
Перезапуск клиента, проверка что session_id в логах только uuid4 или None; отсутствие ошибки `.strip()`.

## Запрос/цель
Гарантировать валидный session_id для всех потребителей без дублирования логики.

## Контекст
- Файлы: `integration/core/selectors.py`
- Документы: `Docs/ARCHITECTURE_OVERVIEW.md`, `Docs/PROJECT_REQUIREMENTS.md`

## Решения/выводы
- Добавлена централизованная проверка uuid4 в селекторе.

## Открытые вопросы
- Нужен ли одноразовый guard‑лог при обнаружении невалидного session_id?

## Следующие шаги
- Перезапустить клиент и проверить цепочку PTT → gRPC.
