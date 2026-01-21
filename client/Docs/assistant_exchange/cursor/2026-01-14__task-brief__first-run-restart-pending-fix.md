# Task Brief — First-Run Restart Pending Fix

Дата: 2026-01-14  
Задача: восстановить обработку `permissions.first_run_restart_pending`, чтобы restart после выдачи разрешений не терялся, а PTT/приветствие запускались корректно.

## Что сделано

- Добавлена синхронизация restart_pending состояния в `FirstRunPermissionsIntegration` и сохранение payload в `ApplicationStateManager`.
- Координатор снова подписан на `permissions.first_run_restart_pending`, сохраняет состояние и публикует `permissions.restart_pending.changed`.
- `PermissionRestartIntegration` воспроизводит pending restart на старте, если событие было опубликовано до подписки.
- Обновлены тесты координатора под текущую модель состояния.
- Обновлены требования (REQ-011) + Implementation Map.
- Обновлён `client/VERSION_INFO.json` через `scripts/update_requirements_snapshot.py --update`.

## Затронутые файлы

- `integration/integrations/first_run_permissions_integration.py`
- `integration/core/simple_module_coordinator.py`
- `integration/integrations/permission_restart_integration.py`
- `tests/test_coordinator_critical_subscriptions.py`
- `Docs/PROJECT_REQUIREMENTS.md`
- `client/VERSION_INFO.json`
- `.crm/TASKS.json`

## Команды

- `python3 scripts/verify_feature_flags.py --module integration/`
- `python3 scripts/update_requirements_snapshot.py --check`
- `python3 scripts/check_requirements_mapping.py` (❌ см. ниже)
- `python3 scripts/update_requirements_snapshot.py --update`

## Проверки

- Линтеры: `read_lints` — ошибок нет.
- Автотесты: не запускались.

## Проблемы/заметки

- `scripts/check_requirements_mapping.py` падает из‑за уже существующих несоответствий в `PROJECT_REQUIREMENTS.md` (не связано с текущей правкой).
- Packaging контур (PRE_PACKAGING_VERIFICATION / PACKAGING_READINESS_CHECKLIST) не запускался.

## Далее (рекомендации)

- Проверить first-run flow в .app: выдача разрешений → автоперезапуск → приветствие → PTT.
- При необходимости прогнать `scripts/test_first_run_integration.sh` и `scripts/test_restart_priority.sh`.
