# Single Instance Fix

## Метаданные
- Ассистент: codex
- Тип: task-brief
- Дата: 2026-02-05
- ID (INS-###): INS-000

## Diagnosis
Дубли запускаются из-за второго источника автозапуска и отсутствия guard перед relaunch в restart/update путях.

## Root Cause
Legacy LaunchAgent + параллельные relaunch → дополнительный процесс → визуальный “двойной запуск”.

## Optimal Fix
Оставить единый LaunchAgent и добавить централизованный guard перед relaunch, использующий InstanceManager lock.

## Verification
Удалить legacy LaunchAgent, проверить, что relaunch пропускается при активном другом экземпляре, запуск дает один процесс.

## Запрос/цель
Гарантировать единственный экземпляр и запретить запуск дублей.

## Контекст
- Файлы: modules/instance_manager/core/instance_manager.py, modules/permission_restart/macos/permissions_restart_handler.py, modules/updater/updater.py, integration/integrations/autostart_manager_integration.py
- Документы: Docs/ARCHITECTURE_OVERVIEW.md
- Ограничения: без новых источников истины

## Решения/выводы
- Добавлен guard через InstanceManager lock в restart/updater.
- Добавлен лог‑детектор legacy LaunchAgent.

## Открытые вопросы
- Нужна ли автоматическая миграция legacy LaunchAgent в продакшне.

## Следующие шаги
- Удалить legacy LaunchAgent в системе.
- Проверить запуск/перезапуск.
