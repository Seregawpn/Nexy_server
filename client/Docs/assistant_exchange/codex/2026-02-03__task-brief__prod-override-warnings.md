# Task Brief: Production Override Warnings

## Scope
Добавлены предупреждения при использовании env-override флагов в production.

## Changes
- Added `integration/utils/env_detection.py` with `is_production_env()` helper.
- Added production warnings for:
  - `NEXY_APP_NAME`, `NEXY_APP_DATA_SUFFIX` (`integration/utils/resource_path.py`)
  - `NEXY_BYPASS_PERMISSION_READY` (`integration/integrations/permission_restart_integration.py`)
  - `NEXY_DISABLE_TRAY` (`integration/integrations/tray_controller_integration.py`)
  - `NEXY_GRPC_SERVER` (`integration/integrations/grpc_client_integration.py`)
  - `NEXY_INSTANCE_LOCK_FILE` (`integration/integrations/instance_manager_integration.py`)
  - `NEXY_DISABLE_AUTO_RESTART`, `NEXY_KS_FIRST_RUN_RESTART` (`modules/permission_restart/macos/permissions_restart_handler.py`)

## Verification
Не запускалась.
