# Task Brief — Disable Sequential Permissions

Дата: 2026-01-14  
Задача: отключить `permissions.sequential` по запросу.

## Что сделано

- В `config/unified_config.yaml` установлено `permissions.sequential: false`.

## Затронутые файлы

- `config/unified_config.yaml`

## Проверки

- Линтеры: `read_lints` — ошибок нет.

## Примечания

- Изменение конфигурации — packaging‑триггер; packaging‑контур не запускался.
