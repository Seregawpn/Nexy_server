# Feature Flags & Kill-Switches Registry

**Цель**: Карта соответствий между feature flags/kill-switches и путями в коде для мгновенного отката без релиза.

## Формат

| Flag/Switch | Type | Config Path | Code Location | Function/Method | Default | Purpose |
|-------------|------|-------------|---------------|----------------|---------|---------|
| `NEXY_FEATURE_PERMISSION_RESTART_V2` | Feature Flag | `unified_config.yaml: permission_restart.enabled` | `modules/permission_restart/core/restart_scheduler.py` | `RestartScheduler.maybe_schedule_restart()` | `true` | Включить автоматический перезапуск после разрешений |
| `NEXY_KS_PERMISSION_RESTART_V2` | Kill-Switch | `unified_config.yaml: permission_restart.enabled` | `modules/permission_restart/core/restart_scheduler.py:69` | `if not self._config.enabled: return None` | `true` | Отключить автоматический перезапуск (откат) |
| `NEXY_DISABLE_AUTO_RESTART` | Kill-Switch | Environment variable | `permission_restart_integration.py` | `_do_start()` | `false` | Dry-run mode (перезапуск не выполняется) |
| `NEXY_FEATURE_FIRST_RUN_V2` | Feature Flag | `unified_config.yaml: first_run_permissions.enabled` | `integration/integrations/first_run_permissions_integration.py` | `FirstRunPermissionsIntegration.initialize()` | `true` | Включить систему первого запуска |
| `serial_tcc_prompts` | Feature Flag | `unified_config.yaml: features.serial_tcc_prompts.enabled` | `.impact/change_impact.yaml` (rollout spec) | `Pending wiring (reserved)` | `false` | Последовательный показ TCC диалогов (зарезервировано для будущего релиза) |
| `ks_serial_tcc` | Kill-Switch | `unified_config.yaml: features.ks_serial_tcc.enabled` | `.impact/change_impact.yaml` (rollout spec) | `Pending wiring (reserved)` | `false` | Мгновенно отключает serial_tcc_prompts (зарезервировано) |
| `use_events_for_update_status` | Feature Flag | `unified_config.yaml: features.use_events_for_update_status.enabled` | `integration/integrations/updater_integration.py` | `_set_update_state()` | `true` | Включить shadow-mode публикацию `updater.in_progress.changed` вместо прямого state_data |
| `use_events_for_restart_pending` | Feature Flag | `unified_config.yaml: features.use_events_for_restart_pending.enabled` | `integration/core/simple_module_coordinator.py` | `_on_permissions_restart_pending()` | `true` | Читать `permissions.restart_pending` через события/селекторы вместо прямого state_data |
| `critical_subscriptions_fix` | Feature Flag | `unified_config.yaml: features.critical_subscriptions_fix.enabled` | `integration/core/simple_module_coordinator.py` | `_setup_critical_subscriptions()` | `true` | Гарантирует подписку на `permissions.*` до инициализации интеграций (fix race) |
| `ks_first_run_normalization` | Kill-Switch | `unified_config.yaml: features.ks_first_run_normalization.enabled` | `integration/integrations/permission_restart_integration.py` | `_handle_transition()` | `false` | Отключает gateway-проверку first_run/restart_pending для PermissionRestartIntegration |

| `NEXY_FEATURE_AVFOUNDATION_AUDIO_V2` | Feature Flag | `unified_config.yaml: audio_system.avfoundation_enabled` | `AudioRouteManagerIntegration.initialize()` | `false` | Включить AVFoundation аудиосистему (master switch) |
| `NEXY_FEATURE_AVFOUNDATION_INPUT_MONITOR_V2` | Feature Flag | `unified_config.yaml: audio_system.avfoundation_input_monitor_enabled` | `AVFoundationDeviceMonitor.start_monitoring()` | `false` | Включить AVFoundation мониторинг input устройств |
| `NEXY_FEATURE_AVFOUNDATION_OUTPUT_V2` | Feature Flag | `unified_config.yaml: audio_system.avfoundation_output_enabled` | `AVFoundationAudioPlayback.initialize()` | `false` | Включить AVFoundation output (AVAudioEngine) |
| `NEXY_FEATURE_AVFOUNDATION_ROUTE_MANAGER_V2` | Feature Flag | `unified_config.yaml: audio_system.avfoundation_route_manager_enabled` | `AudioRouteManagerIntegration.initialize()` | `false` | Включить RouteManager для reconcile логики |
| `NEXY_KS_AVFOUNDATION_INPUT_MONITOR_V2` | Kill-Switch | `unified_config.yaml: audio_system.ks_avfoundation_input_monitor` | `AVFoundationDeviceMonitor.start_monitoring()` | `false` | Отключить AVFoundation мониторинг input (мгновенный откат) |
| `NEXY_KS_AVFOUNDATION_OUTPUT_V2` | Kill-Switch | `unified_config.yaml: audio_system.ks_avfoundation_output` | `AVFoundationAudioPlayback.initialize()` | `false` | Отключить AVFoundation output (мгновенный откат) |
| `NEXY_KS_AVFOUNDATION_ROUTE_MANAGER_V2` | Kill-Switch | `unified_config.yaml: audio_system.ks_avfoundation_route_manager` | `AudioRouteManagerIntegration.initialize()` | `false` | Отключить RouteManager (мгновенный откат) |
## Использование

### Feature Flag (постепенный роллаут)
```yaml
# unified_config.yaml
permission_restart:
  enabled: true  # Feature flag
```

### Kill-Switch (мгновенный откат)
```yaml
# unified_config.yaml (или через env)
permission_restart:
  enabled: false  # Kill-switch
```

Или через environment variable:
```bash
export NEXY_DISABLE_AUTO_RESTART=1
```

## Правила добавления

1. **Feature Flag** добавляется в `unified_config.yaml` и этот реестр
2. **Kill-Switch** указывает точный путь в коде где проверяется
3. **Default** указывает значение по умолчанию (включено/выключено)
4. **Purpose** кратко описывает назначение флага

## Проверка в CI

Все feature flags должны быть зарегистрированы в этом файле перед мерджем (см. `.cursorrules` раздел 19).
