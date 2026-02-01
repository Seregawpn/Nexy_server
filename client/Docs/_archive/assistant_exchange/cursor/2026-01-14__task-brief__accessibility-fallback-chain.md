# Task Brief — Accessibility Fallback Chain

Дата: 2026-01-14  
Задача: добавить цепочку fallback для Accessibility (prompt → prompt → Settings).

## Что сделано

- Добавлен best‑effort subprocess‑prompt через `AXIsProcessTrustedWithOptions(prompt=True)` как второй шаг.
- Если Accessibility не выдана после двух попыток → in‑app alert + авто‑open Settings.
- Документация/требования обновлены.
- `client/VERSION_INFO.json` обновлён через `scripts/update_requirements_snapshot.py --update`.

## Затронутые файлы

- `modules/permissions/first_run/activator.py`
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
