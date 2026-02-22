# Short-term Memory Idle Cleanup (2h)

## Goal
Добавить периодическую очистку только краткосрочной памяти при неактивности ассистента 2 часа, без влияния на долгосрочную память.

## Architecture Fit
- Owner cleanup-path: `memory_management` module (adapter + MemoryManager + DB function).
- Source of truth для очистки: `cleanup_expired_short_term_memory(hours)` в БД.
- Long-term memory не затрагивается (`long_term_memory` не изменяется).

## Changes
1. `server/server/config/unified_config.py`
- Добавлены параметры memory-конфига:
  - `short_term_cleanup_enabled` (default `True`)
  - `short_term_cleanup_interval_seconds` (default `7200`)
  - `short_term_cleanup_idle_hours` (default `2`)
- Добавлены env-переменные:
  - `MEMORY_SHORT_TERM_CLEANUP_ENABLED`
  - `MEMORY_SHORT_TERM_CLEANUP_INTERVAL_SECONDS`
  - `MEMORY_SHORT_TERM_CLEANUP_IDLE_HOURS`

2. `server/server/modules/memory_management/adapter.py`
- Добавлен lifecycle-safe фоновый цикл очистки short-term памяти:
  - старт в `initialize()`
  - стоп в `cleanup()`
  - периодический вызов `self._manager.cleanup_expired_memory(hours=...)`
- Добавлены guard'ы и логирование результатов (`cleaned_rows`).

3. `server/server/tests/test_memory_short_term_cleanup_scheduler.py`
- Тестирует:
  - запуск цикла и вызов cleanup с `idle_hours=2`
  - корректную остановку фоновой задачи при `cleanup()`.

## Validation
- `pytest -q tests/test_memory_short_term_cleanup_scheduler.py tests/test_memory_single_call_smoke.py tests/test_grpc_phase_collect_commit.py`
- Result: `10 passed`
- `python3 -m py_compile modules/memory_management/adapter.py config/unified_config.py tests/test_memory_short_term_cleanup_scheduler.py`
- Result: ok

## Notes
- Очистка влияет только на `short_term_memory` через существующую SQL-функцию.
- Интервал запуска и порог неактивности заданы по требованию: каждые 2 часа / idle 2 часа.
