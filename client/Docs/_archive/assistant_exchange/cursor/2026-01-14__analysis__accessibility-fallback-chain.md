# Impact Map — Accessibility Fallback Chain

Дата: 2026-01-14  
Цель: добавить цепочку fallback для Accessibility (prompt1 → prompt2 → Settings).

| Ось или инвариант | Модули/интеграции | EventBus события/контракты | Конфиги/флаги | Тест-планы/скрипты |
| --- | --- | --- | --- | --- |
| permissions.accessibility | `modules/permissions/first_run/activator.py` | `permissions.status_checked`, `permissions.changed` | `permissions.first_run.activation_hold_duration_sec`, `permissions.first_run.open_settings_after_sec` | manual first-run |
| first_run flow | `integration/integrations/first_run_permissions_integration.py` | `permissions.first_run_started/completed/restart_pending` | `permissions.first_run.mode` | `scripts/test_first_run_integration.sh` (manual) |
