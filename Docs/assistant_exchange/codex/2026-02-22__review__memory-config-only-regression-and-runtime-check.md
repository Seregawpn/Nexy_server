# Memory config-only regression and runtime check

## Scope
Проверка после централизации memory prompt (config-only), расширения short/long policy и scheduler очистки short-term.

## Test execution
- `python3 -m py_compile` для затронутых memory/grpc/workflow файлов и тестов
- `pytest -q tests/test_memory_prompt_policy.py tests/test_memory_short_term_cleanup_scheduler.py tests/test_memory_single_call_smoke.py tests/test_streaming_workflow_concurrency_guards.py tests/test_grpc_phase_collect_commit.py`

## Results
- Py-compile: OK
- Pytest: `14 passed`

## Runtime DB verification
- Стандартный `server/server/scripts/test_db_connection.py` использует `server/server/config.env` (там плейсхолдер пароля), поэтому падает.
- Проведена прямая проверка через рабочий `server/config.env`:
  - DB connect: OK
  - `get_memory_stats()`: `total_users=26, users_with_memory=0, short_chars=0, long_chars=0`

## Conclusion
- Изменения memory policy и config-only owner-path работают корректно в тестовом покрытии.
- Контур БД доступен и возвращает консистентные memory-метрики.
