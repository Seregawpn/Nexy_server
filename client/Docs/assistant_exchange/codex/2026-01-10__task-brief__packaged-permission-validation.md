# Packaged Permission Validation

## Метаданные
- Ассистент: codex
- Тип: task-brief
- Дата: 2026-01-10
- ID (INS-###): INS-005

## Diagnosis
Нужно подтвердить корректность реализации permission‑flow при запуске из .app: рестарт, readiness и запуск приветствия.

## Root Cause
Сценарий запуска из .app может отличаться от терминала, поэтому без проверок по логам и флагам нельзя подтвердить корректность readiness.

## Optimal Fix
Проверить цепочку событий first‑run → restart → ready → welcome в packaged запуске.

## Verification
- Логи Nexy: permissions.first_run_*, permission_restart.*, system.ready_to_greet.
- Наличие флагов permissions_granted.flag / restart_completed.flag.
- Фактический рестарт после выдачи Input Monitoring.

## Запрос/цель
Проверить, что всё корректно реализовано для запуска из .app.

## Контекст
- Файлы: integration/integrations/first_run_permissions_integration.py, integration/integrations/permission_restart_integration.py, modules/permission_restart/macos/permissions_restart_handler.py
- Документы: Docs/ARCHITECTURE_OVERVIEW.md, Docs/PROJECT_REQUIREMENTS.md

## Решения/выводы
- Основной критерий: публикация system.ready_to_greet после рестарта.

## Открытые вопросы
- Где хранится лог Nexy в packaged окружении?

## Следующие шаги
- Собрать лог Nexy и проверить цепочку событий.
- Подтвердить рестарт после input monitoring.
