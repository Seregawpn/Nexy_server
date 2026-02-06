# Single Instance Source

## Метаданные
- Ассистент: codex
- Тип: handoff
- Дата: 2026-02-05
- ID (INS-###): INS-000

## Diagnosis
Дубли запусков обусловлены внешним legacy LaunchAgent и отсутствием guard в некоторых relaunch путях.

## Root Cause
Legacy LaunchAgent → параллельный запуск; relaunch без проверки lock → потенциальный дубль.

## Optimal Fix
Оставить один автозапуск (com.nexy.assistant) и добавить guard через InstanceManager lock во всех relaunch путях.

## Verification
Проверить отсутствие legacy LaunchAgent и единичный процесс после ручного запуска/перезапуска.

## Запрос/цель
Гарантировать, что в коде всегда один источник и нет дублей запуска.

## Контекст
- Файлы: modules/permission_restart/macos/permissions_restart_handler.py, modules/updater/updater.py, modules/updater/migrate.py, integration/integrations/autostart_manager_integration.py, modules/instance_manager/core/instance_manager.py
- Документы: Docs/ARCHITECTURE_OVERVIEW.md
- Ограничения: без новых источников истины

## Решения/выводы
- Добавлен guard (InstanceManager lock) в permission restart и updater relaunch.
- Добавлен guard в migrate relaunch.
- Добавлен лог‑детектор legacy LaunchAgent.

## Открытые вопросы
- Нужно ли автоматическое удаление legacy LaunchAgent в инсталляторе.

## Следующие шаги
- Удалить legacy LaunchAgent в системе (sudo).
- Проверить запуск после сборки.
