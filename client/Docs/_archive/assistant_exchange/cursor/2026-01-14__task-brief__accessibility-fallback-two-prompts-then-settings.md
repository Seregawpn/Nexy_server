# Task Brief — Accessibility: Two Prompts Then Settings

Дата: 2026-01-14  
Задача: для Accessibility делать 2 попытки prompt, затем открывать Settings.

## Что сделано

- Логика Accessibility: `CGRequestPostEventAccess()` → subprocess `AXIsProcessTrustedWithOptions(prompt=True)` → открыть System Settings при неуспехе.
- Убраны alert/двойные открытия Settings для Accessibility.
- Документация/требования обновлены.
- `client/VERSION_INFO.json` обновлён через `scripts/update_requirements_snapshot.py --update`.

## Затронутые файлы

- `integration/integrations/first_run_permissions_integration.py`
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
