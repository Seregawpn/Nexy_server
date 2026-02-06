# Legacy Autostart Cleanup

## Метаданные
- Ассистент: codex
- Тип: analysis
- Дата: 2026-02-05
- ID (INS-###): INS-NA

## Diagnosis
Legacy LaunchAgent в /Library/LaunchAgents вызывает автоперезапуск после Quit и дублирует автозапуск.

## Root Cause
Legacy LaunchAgent живет вне централизованного управления autostart и включает KeepAlive/перезапуск.

## Optimal Fix
Добавить конфиг-флаг для очистки legacy LaunchAgent и выполнить удаление через AutostartManagerIntegration, сохраняя единственный источник истины.

## Verification
Проверить удаление legacy plist и отсутствие автоперезапуска после Quit.

## Запрос/цель
Устранить перезапуск Nexy после Quit.

## Контекст
- Файлы: integration/integrations/autostart_manager_integration.py, modules/autostart_manager/macos/launch_agent.py, config/unified_config.yaml
- Документы: Docs/ARCHITECTURE_OVERVIEW.md, Docs/PROJECT_REQUIREMENTS.md
- Ограничения: без второго источника истины

## Решения/выводы
- Добавлен cleanup_legacy_launch_agent и путь legacy plist в конфиг.
- Удаление legacy агента централизовано через autostart_manager.

## Открытые вопросы
- Нужен ли elevated-путь удаления (sudo) для /Library/LaunchAgents в инсталлере?

## Следующие шаги
- Проверить поведение Quit на установленной сборке.
