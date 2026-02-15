# Analysis — flags/keys/licensing interactions baseline

## Scope
- Проанализированы: config flags, state keys, env overrides, payment/licensing path, startup/update/permission взаимодействия и лог-контракты.
- Основные источники:
  - `Docs/ARCHITECTURE_OVERVIEW.md`
  - `Docs/PROJECT_REQUIREMENTS.md`
  - `Docs/STATE_CATALOG.md`
  - `Docs/FLOW_INTERACTION_SPEC.md`
  - `Docs/FEATURE_FLAGS.md`
  - `config/unified_config.yaml`
  - `config/unified_config_loader.py`
  - `integration/core/simple_module_coordinator.py`
  - `integration/integrations/first_run_permissions_integration.py`
  - `integration/integrations/permission_restart_integration.py`
  - `integration/integrations/updater_integration.py`
  - `integration/integrations/action_execution_integration.py`
  - `integration/integrations/payment_integration.py`
  - `integration/utils/logging_setup.py`
  - `integration/core/state_keys.py`
  - `integration/core/state_manager.py`

## Fast checks run
- `python3 scripts/verify_feature_flags.py` → OK
- `python3 scripts/verify_state_catalog.py` → OK
- `python3 scripts/verify_rule_coverage.py` → OK
- `python3 scripts/verify_no_direct_state_access.py` → OK

## Source-of-Truth map (current)
- Feature availability SoT: `UnifiedConfigLoader.is_feature_enabled(...)`
- Runtime state SoT: `ApplicationStateManager` + `integration/core/state_keys.py`
- First-run/restart SoT (V2): ledger (`permission_ledger.json`) via V2 orchestrator
- Update state SoT: `UpdaterIntegration._update_in_progress` (mirrored в state_manager)
- Event contracts SoT: `Docs/FLOW_INTERACTION_SPEC.md`

## Key flag groups
- Permissions/first-run/restart:
  - `integrations.permissions_v2.enabled` (канон)
  - `integrations.permission_restart.enabled`
  - `features.ks_first_run_normalization.enabled`
  - env: `NEXY_DISABLE_AUTO_RESTART`, `NEXY_KS_FIRST_RUN_RESTART`, `NEXY_BYPASS_PERMISSION_READY`
- Update:
  - `updater.default.*`, `updater.development.*`
  - `features.use_events_for_update_status.enabled`
- Actions/features:
  - `features.browser.enabled`, `features.messages.enabled`, `features.payment.enabled`, `features.browser_use.enabled`
  - alias sections: `browser_use.enabled`, `payment_use.enabled`, `messages.enabled`, `whatsapp.enabled`
- Tray/logging/runtime:
  - env: `NEXY_DISABLE_TRAY`, `NEXY_ENV`, `NEXY_ENVIRONMENT`, `NEXY_APP_NAME`, `NEXY_APP_DATA_SUFFIX`
  - logging: `logging.console_level`, `logging.file_level`, `logging.file_path`
- API keys/credentials:
  - `UnifiedConfigLoader.get_api_key()` priority:
    1) env
    2) `~/Library/Application Support/Nexy/credentials.yaml`
    3) config fallback (warn)

## Interaction points (critical)
- Startup gate owner: `SimpleModuleCoordinator` (critical subscriptions before integrations init)
- First-run owner: `FirstRunPermissionsIntegration` (V2 orchestrator path)
- Restart owner in V2 mode: V2 orchestrator; `PermissionRestartIntegration` legacy paths frozen
- Update owner: `UpdaterIntegration` (`update_in_progress` + `updater.*` events)
- Licensing/payment trigger path:
  - gRPC limit error → `grpc.response.action` with `buy_subscription`
  - dispatch via `ActionExecutionIntegration` (feature gate `payment`)
  - if enabled → `PaymentIntegration`

## Conflicts / risk hotspots
1. Logging config API drift:
   - `UnifiedConfigLoader.get_logging_config()` ожидает старые поля (`level/file/error_file/...`), а реальный YAML использует `console_level/file_level/file_path`.
   - Сейчас runtime использует `integration/utils/logging_setup.py` (raw logging section), поэтому не падает, но API остаётся потенциально опасным.

2. Feature-flag duality (canonical + aliases):
   - Для payment/browser есть `features.*` и alias sections (`payment_use`, `browser_use`).
   - `is_feature_enabled()` резолвит это корректно, но конфигурация усложнена и повышает риск несогласованности при ручных правках.

3. V1 leftovers in permissions config:
   - В `permissions.first_run` ещё присутствуют batching-поля, при том что runtime first-run идёт через V2 orchestrator.
   - Это создаёт шум и риск неверных ожиданий.

4. Payment disabled path UX:
   - При `features.payment=false` action `buy_subscription/manage_subscription` в `ActionExecutionIntegration` просто игнорируется (silent no-op для payment).
   - Технически корректно, но может восприниматься как “команда потерялась”.

5. Credentials path vs app data suffix:
   - Credentials читаются из фиксированного `~/Library/Application Support/Nexy/credentials.yaml`, тогда как данные/флаги могут жить в `Nexy-Dev` через suffix.
   - Для dev/prod изоляции это пограничный источник путаницы.

## Correct log baseline (healthy run)
- Startup:
  - `tray.integration_ready` появляется один раз на запуск.
  - Нет циклических повторов инициализации одинаковых интеграций в одной сессии.
- First-run V2:
  - `permissions.first_run_started` → terminal (`permissions.first_run_completed|failed`) с валидным `session_id/source`.
  - При `permissions_v2.enabled=true` публикация `system.ready_to_greet` идет через V2 owner path.
- Processing:
  - `voice.recording_start` → `voice.recording_stop` → `grpc.request_started` → `playback.started` → `playback.completed` → `mode.request(SLEEPING)` / `app.mode_changed`.
- Update:
  - Нет `updater.update_started` без реального manifest update.
  - `updater.in_progress.changed` консистентно с accessor/state.
- Interrupt:
  - cancel path проходит через `grpc.request_cancel` + `playback.cancelled`.

## Note
- Проверка `scripts/verify_architecture.py` невозможна: файл отсутствует в текущем workspace (`scripts/`).
