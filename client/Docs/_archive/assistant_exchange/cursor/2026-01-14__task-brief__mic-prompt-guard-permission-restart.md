# Task Brief — Mic Prompt Guard in PermissionRestart

Дата: 2026-01-14  
Задача: предотвратить ранний микрофон‑prompt до Input Monitoring.

## Что сделано

- Добавлена неинвазивная проверка микрофона `check_microphone_status_no_prompt`.
- First‑run initial snapshot и PermissionRestart readiness используют неинвазивную проверку, пока first‑run не завершён.
- Добавлен selector `is_first_run_required` для безопасного доступа к состоянию.
- Документация/требования обновлены.
- `client/VERSION_INFO.json` обновлён через `scripts/update_requirements_snapshot.py --update`.

## Затронутые файлы

- `modules/permissions/first_run/status_checker.py`
- `integration/integrations/first_run_permissions_integration.py`
- `integration/integrations/permission_restart_integration.py`
- `integration/core/selectors.py`
- `Docs/first_run_flow_spec.md`
- `Docs/PROJECT_REQUIREMENTS.md`
- `client/VERSION_INFO.json`

## Команды

- `python3 scripts/verify_feature_flags.py --module modules/permissions/first_run/status_checker.py`
- `python3 scripts/verify_feature_flags.py --module integration/integrations/permission_restart_integration.py`
- `python3 scripts/verify_feature_flags.py --module integration/core/selectors.py`
- `python3 scripts/update_requirements_snapshot.py --check`
- `python3 scripts/update_requirements_snapshot.py --update`

## Проверки

- Линтеры: `read_lints` — ошибок нет.

## Примечания

- Изменения в логике/Docs — packaging‑триггер; packaging‑контур не запускался.
