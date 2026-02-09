# Автор
Codex

# Запрос/цель
Разобрать, почему приветствие на старте иногда не слышно, и убрать конфликт последовательности без новых локальных state-веток.

# Контекст
- `/Users/sergiyzasorin/Fix_new/client/integration/workflows/processing_workflow.py`
- `/Users/sergiyzasorin/Fix_new/client/integration/integrations/welcome_message_integration.py`
- `/Users/sergiyzasorin/Fix_new/client/tests/test_processing_workflow_session_guard.py`

# Наблюдение из логов
- `welcome_message` публикует `mode.request(PROCESSING)` с `session_id=None`.
- `ProcessingWorkflow` реагировал на `app.mode_changed(processing)` даже без `session_id` и запускал `capture -> grpc`.
- Это создаёт параллельный путь обработки поверх startup-приветствия (конфликт владельцев PROCESSING-сценария).

# Root cause
В `ProcessingWorkflow` отсутствовал guard на `session_id` при входе в processing.  
Итог: workflow запускался даже для не-request mode-switch (welcome), что добавляло конкурирующую цепочку.

# Исправление
1. Добавлен guard в `_on_mode_changed`:
   - если `mode=processing` и `session_id is None` → не запускать processing chain.
2. Добавлены тесты:
   - без `session_id` chain не стартует,
   - с `session_id` chain стартует.

# Проверка
- Команда: `pytest -q tests/test_welcome_startup_sequence.py tests/test_processing_workflow_session_guard.py`
- Результат: `4 passed`.

# Вывод
Последовательность централизована:
- startup-приветствие больше не порождает рабочую `capture/grpc` цепочку;
- `ProcessingWorkflow` остаётся owner только для request-сценариев с валидным `session_id`.
