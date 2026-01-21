# Task Brief — Accessibility Immediate Settings Fallback

Дата: 2026-01-14  
Задача: показать `Open Settings` сразу после проваленного Accessibility prompt.

## Что сделано

- В `FirstRunPermissionsIntegration` добавлен ранний fallback:
  - после попытки `accessibility` если статус не `GRANTED`, показываем in‑app alert c `Open Settings`;
  - на финальном шаге не показываем тот же alert повторно.
- Документация и требования обновлены.
- `client/VERSION_INFO.json` обновлён через `scripts/update_requirements_snapshot.py --update`.

## Затронутые файлы

- `integration/integrations/first_run_permissions_integration.py`
- `Docs/first_run_flow_spec.md`
- `Docs/PROJECT_REQUIREMENTS.md`
- `client/VERSION_INFO.json`

## Команды

- `python3 scripts/verify_feature_flags.py --module integration/integrations/first_run_permissions_integration.py`
- `python3 scripts/update_requirements_snapshot.py --check`
- `python3 scripts/update_requirements_snapshot.py --update`

## Проверки

- Линтеры: `read_lints` — ошибок нет.

## Примечания

- Изменения в логике/Docs — packaging‑триггер; packaging‑контур не запускался.
