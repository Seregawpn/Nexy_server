# Task Brief: Sync timeout flow (remove background completion task)

## Goal
Привести first-run к жёсткой модели: последовательный таймбокс на каждый шаг и синхронное завершение, без фонового completion task.

## Changes
1. `integration/integrations/first_run_permissions_integration.py`
   - Удалён non-blocking путь:
     - `advance_on_timeout=true — не блокируем startup`
     - `asyncio.create_task(_await_timeout_completion())`
   - Теперь `start()` всегда ждёт `wait_for_completion(timeout=...)` синхронно.
   - Для timeout-mode после синхронного ожидания вызывается публикация completion-событий через `_publish_timeout_completion_events()`.
   - Удалён старый метод `_await_timeout_completion()`.
   - Удалён неиспользуемый import `asyncio`.

2. `tests/test_first_run_status_policy.py`
   - Тест обновлён на новый путь: вызывается `_publish_timeout_completion_events()` вместо удалённого `_await_timeout_completion()`.

## Validation
- `PYTHONPATH=. pytest -q tests/test_first_run_status_policy.py tests/test_first_run_orchestrator_single_restart.py tests/test_coordinator_critical_subscriptions.py` -> `11 passed`
- `python3 -m py_compile integration/integrations/first_run_permissions_integration.py tests/test_first_run_status_policy.py` -> OK

## Result
- Timeout-mode больше не зависит от фоновой задачи, которая могла теряться после перехода в UI loop.
- First-run flow стал предсказуемым: дождались завершения -> опубликовали completion -> продолжили.
