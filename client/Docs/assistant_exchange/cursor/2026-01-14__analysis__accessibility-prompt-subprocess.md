# Impact Map — Accessibility Prompt Subprocess

Дата: 2026-01-14  
Цель: повысить вероятность показа системного диалога Accessibility без падения процесса.

| Ось или инвариант | Модули/интеграции | EventBus события/контракты | Конфиги/флаги | Тест-планы/скрипты |
| --- | --- | --- | --- | --- |
| permissions.accessibility | `modules/permissions/first_run/activator.py` | `permissions.status_checked`, `permissions.changed` | `permissions.first_run.activation_hold_duration_sec` | `scripts/update_requirements_snapshot.py --check`, manual first-run |
| first_run flow | `integration/integrations/first_run_permissions_integration.py` | `permissions.first_run_started/completed/restart_pending` | `permissions.first_run.mode` | `scripts/test_first_run_integration.sh` (manual) |

Ожидаемый эффект: системный Accessibility prompt появляется чаще за счёт изолированного вызова `AXIsProcessTrustedWithOptions(prompt=True)` в subprocess.
