# Contract & conflict fixes

## Метаданные
- Ассистент: codex
- Тип: task-brief
- Дата: 2026-02-03
- ID (INS-###): INS-005

## Diagnosis
Потенциальные конфликты: override `session_id` без метрики, пере‑маскирование `key`, отсутствие теста приоритета ошибок для двух невалидных id.

## Root Cause
Автоматические правила override/маскирования не были зафиксированы тестами и метриками.

## Optimal Fix
Добавлены метрика override, сужение маскирования, и тесты на приоритеты/несекретные key‑слова.

## Verification
`python3 -m pytest server/tests/test_grpc_identifier_validation.py server/tests/test_assistant_response_parser.py server/tests/test_secret_masking.py -q` → 26 passed.

## Запрос/цель
Закрыть потенциальные конфликты контрактов и маскирования.

## Контекст
- Файлы: `server/integrations/core/assistant_response_parser.py`, `server/utils/logging_formatter.py`, `server/tests/test_grpc_identifier_validation.py`, `server/tests/test_secret_masking.py`, `server/tests/test_assistant_response_parser.py`
- Документы: `Docs/ARCHITECTURE_OVERVIEW.md`, `Docs/PROJECT_REQUIREMENTS.md`, `Docs/_archive/ASSISTANT_COORDINATION_PROTOCOL.md`, `Docs/_archive/CODEX_PROMPT.md`, `Docs/_archive/assistant_exchange/TEMPLATE.md`
- Ограничения: без изменения архитектуры

## Решения/выводы
- Override `session_id` теперь метрика + warning.
- Маскирование не затрагивает `keyboard`/`monkey`.
- Приоритет ошибки при двух невалидных id закреплен тестом.

## Открытые вопросы
- Нет.

## Следующие шаги
- Прогнать полный `pytest server/tests -q` при необходимости.
