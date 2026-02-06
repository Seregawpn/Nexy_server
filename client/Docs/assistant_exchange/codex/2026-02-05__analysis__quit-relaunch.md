# Quit Relaunch Cause

## Метаданные
- Ассистент: codex
- Тип: analysis
- Дата: 2026-02-05
- ID (INS-###): INS-NA

## Diagnosis
При Quit процесс завершается, но LaunchAgent перезапускает приложение; найден legacy LaunchAgent в /Library/LaunchAgents, создающий дублирование автозапуска.

## Root Cause
Legacy LaunchAgent (com.sergiyzasorin.nexy.voiceassistant) остаётся активным вне контроля AutostartManagerIntegration и может держать KeepAlive, из-за чего Quit приводит к автоматическому рестарту.

## Optimal Fix
Централизовать управление автозапуском через AutostartManagerIntegration и удалить legacy LaunchAgent при старте (под управлением конфигурации), чтобы избежать повторного запуска после Quit.

## Verification
Проверить, что legacy LaunchAgent удалён, и после Quit приложение не перезапускается. Убедиться, что текущий LaunchAgent остаётся единственным источником автозапуска.

## Запрос/цель
Понять причину перезапуска после Quit и предложить архитектурно корректный фикс.

## Контекст
- Файлы: modules/autostart_manager/macos/launch_agent.py, integration/integrations/autostart_manager_integration.py, modules/tray_controller/macos/menu_handler.py
- Документы: Docs/ARCHITECTURE_OVERVIEW.md, Docs/PROJECT_REQUIREMENTS.md
- Ограничения: не создавать второй источник истины

## Решения/выводы
- Вероятная причина: legacy LaunchAgent в /Library/LaunchAgents с KeepAlive/дублирующим автозапуском.
- Фикс должен жить в AutostartManagerIntegration и использовать существующий autostart_manager.

## Открытые вопросы
- Нужна ли автоматическая очистка legacy LaunchAgent по умолчанию или только под фичефлагом?

## Следующие шаги
- Добавить безопасную очистку legacy LaunchAgent и верифицировать поведение Quit.
