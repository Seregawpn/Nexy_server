# Task Brief — Restore Old Accessibility Prompt Logic

Дата: 2026-01-14  
Задача: вернуть старую логику Accessibility (только `CGRequestPostEventAccess()` + hold).

## Что сделано

- Удалён subprocess‑prompt через `AXIsProcessTrustedWithOptions(prompt=True)`.
- Accessibility снова полагается на `CGRequestPostEventAccess()` и фиксированную паузу.
- Документация/требования обновлены.
- `client/VERSION_INFO.json` обновлён через `scripts/update_requirements_snapshot.py --update`.

## Затронутые файлы

- `modules/permissions/first_run/activator.py`
- `Docs/first_run_flow_spec.md`
- `Docs/PROJECT_REQUIREMENTS.md`
- `client/VERSION_INFO.json`

## Команды

- `python3 scripts/update_requirements_snapshot.py --check`
- `python3 scripts/update_requirements_snapshot.py --update`

## Проверки

- Линтеры: `read_lints` — ошибок нет.

## Примечания

- Изменения в логике/Docs — packaging‑триггер; packaging‑контур не запускался.
