# Feature Flags & Kill-Switches Registry

**Цель**: Карта соответствий между feature flags/kill-switches и путями в коде для мгновенного отката без релиза.

## Формат

| Flag/Switch | Type | Config Path | Code Location | Function/Method | Default | Purpose |
|-------------|------|-------------|---------------|----------------|---------|---------|
| `NEXY_FEATURE_PERMISSION_RESTART_V2` | Feature Flag | `unified_config.yaml: permission_restart.enabled` | `modules/permission_restart/core/restart_scheduler.py` | `RestartScheduler.maybe_schedule_restart()` | `true` | Включить автоматический перезапуск после разрешений |
| `NEXY_KS_PERMISSION_RESTART_V2` | Kill-Switch | `unified_config.yaml: permission_restart.enabled` | `modules/permission_restart/core/restart_scheduler.py:69` | `if not self._config.enabled: return None` | `true` | Отключить автоматический перезапуск (откат) |
| `NEXY_DISABLE_AUTO_RESTART` | Kill-Switch | Environment variable | `permission_restart_integration.py` | `_do_start()` | `false` | Dry-run mode (перезапуск не выполняется) |
| `NEXY_FEATURE_FIRST_RUN_V2` | Feature Flag | `unified_config.yaml: first_run_permissions.enabled` | `integration/integrations/first_run_permissions_integration.py` | `FirstRunPermissionsIntegration.initialize()` | `true` | Включить систему первого запуска |

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

