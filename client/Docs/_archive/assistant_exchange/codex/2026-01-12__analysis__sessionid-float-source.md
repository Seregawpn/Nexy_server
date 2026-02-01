# Session ID Float Source

## Метаданные
- Ассистент: codex
- Тип: analysis
- Дата: 2026-01-12
- ID (INS-###): <из Docs/CRM_INSTRUCTION_REGISTRY.md>

## Diagnosis
Логи показывают session_id как float в событиях и gRPC, значит проблема на источнике, а не на чтении через selectors.

## Root Cause
session_id генерируется как timestamp/monotonic float в input_processing → распространяется через события → gRPC client вызывает .strip() → исключение до отправки.

## Optimal Fix
Генерация uuid4 на источнике (input_processing) и передача только строкового uuid4 по всей цепочке; guard на gRPC boundary.

## Verification
Перезапуск клиента, логи показывают uuid4; нет ошибки `.strip()`.

## Запрос/цель
Определить, почему фильтр в selectors не устранил float в логах.

## Контекст
- Файлы: `integration/integrations/input_processing_integration.py`, `integration/integrations/grpc_client_integration.py`, `integration/core/state_manager.py`, `integration/core/selectors.py`

## Решения/выводы
- Фильтр в selectors не влияет на события, где session_id уже float.

## Открытые вопросы
- Требуется ли жесткий запрет non-uuid4 в mode_management?

## Следующие шаги
- Перевести генерацию session_id на uuid4 в input_processing и добавить boundary guard.
