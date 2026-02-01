# Task Brief — Accessibility Settings Only

Дата: 2026-01-14  
Задача: отключить все prompt‑активации Accessibility и сразу открывать System Settings.

## Что сделано

- Accessibility activation отключена; prompt‑вызовы не используются.
- При отсутствии доступа открываются System Settings.
- Fallback‑диалог по missing убран; вместо него открывается Settings.
- Документация и требования обновлены.
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
