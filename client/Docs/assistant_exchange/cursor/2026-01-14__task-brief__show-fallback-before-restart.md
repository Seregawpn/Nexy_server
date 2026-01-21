# Task Brief — Show Fallback Before Restart

Дата: 2026-01-14  
Задача: показывать fallback‑диалог по missing разрешениям **до** рестарта.

## Что сделано

- Перестроен порядок: fallback‑диалог показывается перед `permissions.first_run_restart_pending`.
- Обновлены требования и спецификация first‑run.
- Обновлён `VERSION_INFO.json` через snapshot‑скрипт.

## Затронутые файлы

- `integration/integrations/first_run_permissions_integration.py`
- `Docs/first_run_flow_spec.md`
- `Docs/PROJECT_REQUIREMENTS.md`
- `client/VERSION_INFO.json`

## Команды

- `python3 scripts/update_requirements_snapshot.py --check`
- `python3 scripts/update_requirements_snapshot.py --update`
- `python3 scripts/check_requirements_mapping.py` (известные несоответствия в репозитории)

## Проверки

- Линтеры: `read_lints` — ошибок нет.

## Примечания

- Изменения в `integration/` — packaging‑триггер; packaging‑контур не запускался.
