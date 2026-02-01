# Impact Map — First-Run Restart Pending

Дата: 2026-01-14  
Контекст: first-run permissions → restart pending → permission restart scheduling → ready_to_greet

## Impact Map

| Ось или инвариант | Модули/интеграции | EventBus события/контракты | Конфиги/флаги | Тест-планы/скрипты |
| --- | --- | --- | --- | --- |
| permissions.first_run | `integration/integrations/first_run_permissions_integration.py` | `permissions.first_run_restart_pending` | `config/unified_config.yaml` (required_permissions order) | `scripts/test_first_run_integration.sh` |
| permissions.restart_pending | `integration/core/simple_module_coordinator.py`, `integration/integrations/permission_restart_integration.py` | `permissions.first_run_restart_pending`, `permissions.restart_pending.changed` | `Docs/FEATURE_FLAGS.md` (нет новых флагов) | `tests/test_coordinator_critical_subscriptions.py` |
| permission_restart scheduling | `integration/integrations/permission_restart_integration.py` | `permissions.first_run_restart_pending` (replay on start) | `config/unified_config.yaml` (permission_restart.*) | `scripts/test_restart_priority.sh`, `Docs/TAL_TESTING_CHECKLIST.md` |
| greet readiness | `integration/integrations/permission_restart_integration.py`, `integration/integrations/welcome_message_integration.py` | `system.permissions_ready`, `system.ready_to_greet` | `config/unified_config.yaml` (welcome_message.*) | `tests/test_golden_first_run_logs.py` |

## План (до изменений)

1. Flags discovery: `python scripts/verify_feature_flags.py --module integration/`
2. Обновить `Docs/PROJECT_REQUIREMENTS.md` (REQ-011 + Implementation Map).
3. Код: восстановить обработку `permissions.first_run_restart_pending` в координаторе и fallback для pending restart в PermissionRestartIntegration.
4. Проверки: `scripts/update_requirements_snapshot.py --check`, `scripts/check_requirements_mapping.py`, unit tests при необходимости.

## Flags Discovery

- Module: `integration/`
- Result: no flags found (0)
