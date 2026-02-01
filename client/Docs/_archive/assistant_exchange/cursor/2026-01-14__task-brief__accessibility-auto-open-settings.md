# Task Brief — Accessibility Auto-Open Settings

Дата: 2026-01-14  
Задача: автоматически открыть System Settings для Accessibility, если доступ не выдан.

## Что сделано

- В `FirstRunPermissionsIntegration` добавлен auto‑open: при провале Accessibility стартует фоновая задача, открывающая Settings после `open_settings_after_sec`.
- In‑app alert остаётся и показывается сразу.
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
