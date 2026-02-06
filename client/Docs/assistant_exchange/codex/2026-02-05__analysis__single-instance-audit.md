# Single Instance Audit

## Метаданные
- Ассистент: codex
- Тип: analysis
- Дата: 2026-02-05
- ID (INS-###): INS-NA

## Diagnosis
Основные гонки связаны с дублирующими источниками автозапуска и несогласованными путями lock-файла между InstanceManager и PermissionRestart.

## Root Cause
1) Legacy автозапуск и возможные Login Items создают второй источник старта.
2) PermissionRestart проверяет lock по дефолтному пути, игнорируя unified_config.

## Optimal Fix
Централизовать автозапуск в AutostartManagerIntegration и синхронизировать lock-file path во всех перезапусках.

## Verification
Параллельные старты, перезапуск после разрешений и Quit не приводят к двум экземплярам.

## Запрос/цель
Проанализировать текущую логику и определить необходимые исправления для отсутствия гонок.

## Контекст
- Файлы: integration/integrations/instance_manager_integration.py, modules/instance_manager/core/instance_manager.py, modules/permission_restart/macos/permissions_restart_handler.py, integration/integrations/autostart_manager_integration.py
- Документы: Docs/ARCHITECTURE_OVERVIEW.md, Docs/PROJECT_REQUIREMENTS.md

## Решения/выводы
- Нужна синхронизация lock-file path для PermissionRestart.
- Убедиться, что Login Items/legacy LaunchAgents отключены.

## Открытые вопросы
- Есть ли активные Login Items/PKG postinstall, которые создают второй автозапуск?

## Следующие шаги
- Добавить единый источник lock-файла (UnifiedConfigLoader) в PermissionRestartHandler.
- Проверить систему на активные Login Items.
