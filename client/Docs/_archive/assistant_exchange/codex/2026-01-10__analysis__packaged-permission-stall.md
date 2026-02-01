# Packaged Permission Stall

## Метаданные
- Ассистент: codex
- Тип: analysis
- Дата: 2026-01-10
- ID (INS-###): INS-005

## Diagnosis
После выдачи разрешений packaged-приложение не переходит в готовность: `system.ready_to_greet` не публикуется, из-за чего не стартуют приветствие и голосовая активация.

## Root Cause
Недостаточная централизация разрешений → перезапуск после критических TCC (input monitoring) не выполняется или не срабатывает готовность → приложение остаётся в состоянии без `ready_to_greet`.

## Optimal Fix
Цель: гарантировать рестарт после критических разрешений и публикацию readiness через PermissionRestartIntegration.

## Verification
- В логах Nexy видны `permissions.first_run_*`, `permission_restart.*`, `system.ready_to_greet`.
- После выдачи Input Monitoring происходит перезапуск.
- Приветствие воспроизводится после `system.ready_to_greet`.

## Запрос/цель
Разобрать, почему после выдачи Mic/Input нет приветствия и активации в packaged приложении.

## Контекст
- Файлы: `integration/integrations/first_run_permissions_integration.py`, `integration/integrations/permission_restart_integration.py`, `modules/permission_restart/macos/permissions_restart_handler.py`, `log.md`
- Документы: `Docs/ARCHITECTURE_OVERVIEW.md`, `Docs/PROJECT_REQUIREMENTS.md`

## Решения/выводы
- Приветствие зависит от `system.ready_to_greet`, публикуемого в PermissionRestartIntegration.
- `ready_to_greet` не публикуется без подтверждения Accessibility/Input Monitoring/Screen Capture.
- Если рестарт после выдачи input monitoring не произошёл, readiness не наступит.

## Открытые вопросы
- Был ли фактический рестарт после выдачи input monitoring в packaged-сборке?
- Есть ли в Nexy-логах `permission_restart` события?

## Следующие шаги
- Проверить логи Nexy на `permission_restart.*` и `system.ready_to_greet`.
- Проверить наличие флагов в `~/Library/Application Support/Nexy/`.
- Убедиться, что переменные `NEXY_DISABLE_AUTO_RESTART`/`NEXY_KS_FIRST_RUN_RESTART` не выставлены.
