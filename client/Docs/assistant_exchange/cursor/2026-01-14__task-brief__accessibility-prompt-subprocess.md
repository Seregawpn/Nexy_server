# Task Brief — Accessibility Prompt Subprocess

Дата: 2026-01-14  
Задача: повысить вероятность показа Accessibility prompt без краша процесса.

## Что сделано

- `activate_accessibility()` теперь:
  - активирует приложение перед запросом;
  - вызывает `CGRequestPostEventAccess()`;
  - запускает `AXIsProcessTrustedWithOptions(prompt=True)` в subprocess.
- Документация и требования обновлены.
- `client/VERSION_INFO.json` обновлён через `scripts/update_requirements_snapshot.py --update`.

## Затронутые файлы

- `modules/permissions/first_run/activator.py`
- `Docs/first_run_flow_spec.md`
- `Docs/PROJECT_REQUIREMENTS.md`
- `client/VERSION_INFO.json`

## Команды

- `python3 scripts/verify_feature_flags.py --module modules/permissions/first_run/activator.py`
- `python3 scripts/update_requirements_snapshot.py --check`
- `python3 scripts/update_requirements_snapshot.py --update`

## Проверки

- Линтеры: `read_lints` — ошибок нет.

## Примечания

- Изменение `Docs/` и логики активации — packaging‑триггер; packaging‑контур не запускался.
