# Disable Autostart Feature

## Метаданные
- Ассистент: codex
- Тип: task-brief
- Дата: 2026-02-05
- ID (INS-###): INS-000

## Diagnosis
Нужно полностью отключить функционал автозапуска на уровне приложения.

## Root Cause
Автозапуск включен через интеграцию `autostart_manager` в конфиге.

## Optimal Fix
Отключить интеграцию автозапуска в `config/unified_config.yaml`.

## Verification
Автозапуск не инициализируется, интеграция не стартует.

## Запрос/цель
Убрать функционал автозапуска (временное отключение).

## Контекст
- Файлы: config/unified_config.yaml
- Документы: Docs/ARCHITECTURE_OVERVIEW.md
- Ограничения: без удаления системных plist

## Решения/выводы
- `integrations.autostart_manager.enabled` установлен в `false`.

## Открытые вопросы
- Нужно ли также отключать системный LaunchAgent вручную.

## Следующие шаги
- При необходимости выполнить `launchctl bootout` для системных LaunchAgents.
