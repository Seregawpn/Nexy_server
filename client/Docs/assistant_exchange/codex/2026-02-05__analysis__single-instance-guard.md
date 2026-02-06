# Single Instance Guard

## Метаданные
- Ассистент: codex
- Тип: analysis
- Дата: 2026-02-05
- ID (INS-###): INS-000

## Diagnosis
Дубли запускаются из-за второго источника автозапуска (legacy LaunchAgent) и параллельного старта.

## Root Cause
Два LaunchAgent (разные label/bundle) → параллельный запуск → InstanceManager гасит дубликат, но визуально выглядит как два запуска/перезапуск.

## Optimal Fix
Оставить единственный источник автозапуска `com.nexy.assistant`, удалить legacy `com.sergiyzasorin.nexy.voiceassistant`, добавить мониторинг конфликтов автозапуска (лог) и при необходимости проверку lock перед relaunch.

## Verification
Проверить отсутствие legacy job в `launchctl`, один процесс Nexy при ручном запуске, автозапуск работает через один LaunchAgent.

## Запрос/цель
Гарантировать единственный экземпляр Nexy и запретить любые дубли.

## Контекст
- Файлы: integration/integrations/autostart_manager_integration.py, modules/autostart_manager/macos/launch_agent.py, modules/instance_manager/core/instance_manager.py
- Документы: Docs/ARCHITECTURE_OVERVIEW.md
- Ограничения: без новых источников истины, централизовать через InstanceManager/LaunchAgent

## Решения/выводы
- Дубликат создается внешним legacy LaunchAgent.
- Решение: удалить legacy job и оставить один источник автозапуска.

## Открытые вопросы
- Используется ли еще legacy `com.sergiyzasorin.nexy.voiceassistant` в продакшн-инсталляциях?

## Следующие шаги
- Согласовать удаление legacy LaunchAgent.
- При необходимости добавить проверку lock перед relaunch в restart handlers.
