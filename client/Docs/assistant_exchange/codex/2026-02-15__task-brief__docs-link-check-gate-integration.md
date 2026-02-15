# Task Brief: Docs Link Check in problem_scan_gate

Дата: 2026-02-15

## Цель
Добавить автоматическую блокирующую проверку ссылок в канонических документах, чтобы битые repo-path ссылки останавливали quality gate.

## Изменения

1. Добавлен новый скрипт:
- `scripts/verify_doc_links.py`

Что делает:
- Проверяет только канонический набор документов в `Docs/`.
- Валидирует только repo-path ссылки (например, `Docs/...`, `scripts/...`, `integration/...`, `modules/...`, `tests/...`).
- Игнорирует внешние URL, архивные ссылки, runtime/generated пути (`dist/`, `build_logs/`, `~/...`) и секцию "Отсутствующие документы" в `Docs/README.md`.
- Возвращает `exit 1` при найденных битых ссылках.

2. Интегрирован в gate:
- `scripts/problem_scan_gate.sh`
- После проверки `blocking_issues` добавлен блокирующий вызов:
  - `./.venv/bin/python scripts/verify_doc_links.py`

3. Синхронизированы документы для прохождения нового чекера:
- `Docs/PROJECT_REQUIREMENTS.md`
- `Docs/ARCHITECTURE_OVERVIEW.md`
- `Docs/FEATURE_FLAGS.md`

## Проверка

- `./.venv/bin/python scripts/verify_doc_links.py` → pass
- `bash -n scripts/problem_scan_gate.sh` → pass

## Результат

`problem_scan_gate` теперь дополнительно блокирует merge/release при битых ссылках в канонической документации, снижая риск повторного рассинхрона docs vs codebase.
