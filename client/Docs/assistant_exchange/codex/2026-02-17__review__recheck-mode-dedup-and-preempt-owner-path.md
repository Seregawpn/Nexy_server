# Review: Recheck mode dedup and preempt owner path

## Context
Пользователь запросил повторную проверку наличия дублей/гонок и корректности централизации после последних фиксов.

## Findings
1. Целевые проверки mode/interrupt/sleep-guard выполнены.
2. Выявлено расхождение теста с новой архитектурной политикой:
- старый тест ожидал skip `mode.request` для preempt source;
- текущее поведение intentionally централизовано: `interrupt -> mode.request(SLEEPING)`.
3. После обновления теста все целевые тесты проходят.

## Verification
- `python3 -m py_compile` целевых интеграций — OK.
- `pytest -q tests/test_mode_management_mode_request_dedup.py tests/test_interrupt_management_preempt_mode_skip.py tests/test_mode_management_sleep_guard_session_scope.py` — **11 passed**.

## Информация об изменениях
- Что изменено:
  - Обновлен один тест на новое централизованное поведение preempt-path.
- Список файлов:
  - `tests/test_interrupt_management_preempt_mode_skip.py`
- Причина/цель изменений:
  - Синхронизировать тестовые ожидания с принятым owner-path (без skip mode.request для preempt).
- Проверка:
  - Повторный прогон целевых тестов: 11 passed.
