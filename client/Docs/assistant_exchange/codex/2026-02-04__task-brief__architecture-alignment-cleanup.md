# Task Brief

## Context
Пользователь запросил проверить соответствие модулей текущей архитектуре и убрать точечные рассинхроны (инициализация, дубли, актуальность config checks).

## Changes
1. `scripts/verify_config.py`
- Обновлены критичные интеграции под текущий канон:
  - `grpc_client`, `permissions_v2`, `voice_recognition`
- Блок проверки разрешений переведен с legacy `first_run_permissions` на актуальные:
  - `integrations.permissions_v2.enabled`
  - `integrations.permissions_v2.order`
  - `integrations.permission_restart.critical_permissions`

2. `integration/core/simple_module_coordinator.py`
- Удален дубликат строки:
  - повторное `tray_controller = tray_integration.get_tray_controller()`.

3. `integration/core/integration_factory.py`
- Синхронизированы комментарии с фактической config-driven политикой:
  - payment/whatsapp теперь описаны как profile/config dependent, а не жёстко "disabled by default".

4. Дополнительно
- Устранены 2 blocking ruff-ошибки (`I001`) в `scripts/check_permissions_snapshot.py`, чтобы восстановить прохождение strict gate.

## Verification
- `python3 scripts/verify_config.py` → PASS (1 warning updater)
- `python3 scripts/verify_imports.py` → PASS
- `python3 scripts/check_dependency_violations.py` → PASS
- `REQUIRE_BASEDPYRIGHT_IN_SCAN=true ./scripts/problem_scan_gate.sh` → PASS
  - `TOTAL_ISSUES=200`
  - `BLOCKING_ISSUES=0`

## Impact
- Убраны ложные warning в config preflight относительно устаревших секций.
- Убраны локальные дубли в coordinator path.
- Комментарии IntegrationFactory соответствуют текущему поведению конфигурации.
- Общий quality gate снова проходит в strict режиме.
