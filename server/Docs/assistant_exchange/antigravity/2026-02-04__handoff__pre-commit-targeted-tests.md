## Автор
Codex

## Запрос / Цель
Ускорить pre-commit за счет запуска релевантных тестов по измененным файлам.

## Контекст
- `server/scripts/pre_commit_gate.sh`

## Решение
Обновлен `pre_commit_gate.sh`:
1. Собирает staged Python-файлы в `server/`.
2. Формирует список релевантных тестов:
- staged тесты из `server/tests/`;
- связанные тесты по шаблонам для измененных production-файлов:
  - `test_<module>.py`
  - `test_*<module>*.py`
3. Если релевантные тесты найдены, запускает только их.
4. Если нет совпадений, падает в full fallback:
- `pytest server/tests -q --maxfail=1`

## Проверка
- `bash server/scripts/pre_commit_gate.sh` (без staged Python) — корректный skip.
- `bash server/scripts/full_quality_scan.sh` — `74 passed`.

## Следующие шаги
1. Использовать `git commit` в обычном режиме, pre-commit сам выберет целевые тесты.
2. При необходимости донастроить паттерны маппинга тестов под конкретные модули.
