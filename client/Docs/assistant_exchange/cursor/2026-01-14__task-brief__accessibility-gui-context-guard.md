# Task Brief — Accessibility GUI Context Guard

Дата: 2026-01-14  
Задача: не вызывать Accessibility‑prompt из Terminal/agent контекста; делегировать в GUI .app.

## Что сделано

- Добавлен GUI‑context guard в `FirstRunPermissionsIntegration`.
- При неверном контексте: best‑effort активация GUI `.app` и пропуск prompt.
- Документация обновлена (REQ‑010, first_run_flow_spec).
- Обновлён `VERSION_INFO.json` через snapshot‑скрипт.

## Затронутые файлы

- `integration/integrations/first_run_permissions_integration.py`
- `Docs/first_run_flow_spec.md`
- `Docs/PROJECT_REQUIREMENTS.md`
- `client/VERSION_INFO.json`

## Команды

- `python3 scripts/verify_feature_flags.py --module integration/integrations/first_run_permissions_integration.py`
- `python3 scripts/verify_feature_flags.py --module modules/permissions/first_run/activator.py`
- `python3 scripts/update_requirements_snapshot.py --check`
- `python3 scripts/update_requirements_snapshot.py --update`
- `python3 scripts/check_requirements_mapping.py` (известные несоответствия в репозитории)

## Проверки

- Линтеры: `read_lints` — ошибок нет.

## Примечания

- Изменения в `integration/` — packaging‑триггер; packaging‑контур не запускался.
