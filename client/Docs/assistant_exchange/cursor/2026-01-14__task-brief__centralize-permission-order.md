# Task Brief — Centralize Permission Order

Дата: 2026-01-14  
Задача: централизовать порядок запросов разрешений через `integrations.permissions.required_permissions` и устранить дубли в коде/доках.

## Что сделано

- `activate_all_permissions()` теперь читает порядок из `unified_config.yaml`.
- Документация обновлена: порядок указано как config-driven.
- REQ-010 обновлён под config-driven порядок.
- Обновлён `client/VERSION_INFO.json` через `scripts/update_requirements_snapshot.py --update`.

## Затронутые файлы

- `modules/permissions/first_run/activator.py`
- `Docs/first_run_flow_spec.md`
- `Docs/PROJECT_REQUIREMENTS.md`
- `client/VERSION_INFO.json`
- `.crm/TASKS.json`

## Команды

- `python3 scripts/verify_feature_flags.py --module modules/permissions/first_run`
- `python3 scripts/update_requirements_snapshot.py --check`
- `python3 scripts/update_requirements_snapshot.py --update`
- `python3 scripts/check_requirements_mapping.py` (❌ см. ниже)

## Проверки

- Линтеры: `read_lints` — ошибок нет.
- Автотесты: не запускались.

## Проблемы/заметки

- `scripts/check_requirements_mapping.py` падает из‑за уже существующих несоответствий в `PROJECT_REQUIREMENTS.md` (не связано с текущей правкой).
