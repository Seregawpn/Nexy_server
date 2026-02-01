# Task Brief — First-Run Hold 15s

Дата: 2026-01-14  
Задача: увеличить удержание каждого разрешения до 15 секунд.

## Что сделано

- `permissions.first_run.activation_hold_duration_sec` установлен в `15.0`.
- `client/VERSION_INFO.json` обновлён через `scripts/update_requirements_snapshot.py --update`.

## Затронутые файлы

- `config/unified_config.yaml`
- `client/VERSION_INFO.json`

## Команды

- `python3 scripts/update_requirements_snapshot.py --check`
- `python3 scripts/update_requirements_snapshot.py --update`

## Проверки

- Линтеры: `read_lints` — ошибок нет.

## Примечания

- Изменение конфигурации — packaging‑триггер; packaging‑контур не запускался.
