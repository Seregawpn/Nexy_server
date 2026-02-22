# Memory Path Validation (client/server)

## Scope
Проверка корректности памяти после фиксов collect/commit: чтение контекста, отсутствие дублей owner, запуск фоновой записи.

## What was checked
- Тесты:
  - `tests/test_memory_single_call_smoke.py`
  - `tests/test_streaming_workflow_concurrency_guards.py`
  - `tests/test_grpc_phase_collect_commit.py`
- Рантайм-пути:
  - Read: `streaming_workflow_integration.py` (`prefetch_memory`, `_get_memory_context_parallel`)
  - Write: `grpc_service_integration.py` (`save_to_memory_background`)
  - Background write executor: `memory_workflow_integration.py` (`_save_memory_background`)

## Results
- Test suite status: **10 passed**.
- Single Owner чтения памяти подтвержден: запрос контекста выполняется в `StreamingWorkflowIntegration`, дублирующий owner в `GrpcServiceIntegration` отсутствует.
- Запись памяти запускается асинхронно при наличии `prompt/response`.

## Findings
1. Архитектурно путь памяти корректный: read/write централизованы по текущей схеме.
2. По логам из репозитория подтверждено получение memory context (размер > 0 в последующих запросах).
3. Для доказательства конкретного кейса пользователя ("сказал да, ответил про код") не хватает явной корреляции runtime-логов update_background по тем же session_id/hardware_id.
4. Вероятная причина описанного поведения: фрагментированный/короткий финальный prompt, а не отказ памяти как подсистемы.

## Recommended DoD for runtime proof
1. Включить INFO-лог на событие успешного `update_background` с `hardware_id`, `prompt_len`, `response_len`.
2. Для 2 последовательных запросов одного `hardware_id` проверить:
   - Request#1: есть `update_background success`
   - Request#2: есть `Memory context получен ... (размер > 0)` и в enriched prompt присутствует контекст по Request#1.
3. Негативный тест: пустой/обрезанный prompt не должен записываться как полноценная память.

