# Feature Flags & Kill-Switches Registry

**Цель**: Единый реестр всех feature flags и kill-switches с автоматической проверкой перед внедрением новой логики.

**ВАЖНО**: Все флаги должны быть зарегистрированы в этом реестре ДО использования в коде. Скрипт `scripts/verify_feature_flags.py` автоматически проверяет соответствие кода и реестра.

## Формат реестра

**Обязательные колонки**:
- `name` — имя флага (например: `NEXY_FEATURE_*` или `NEXY_KS_*`)
- `type` — тип: `feature` (feature flag) или `kill_switch` (kill-switch)
- `owner` — владелец флага (команда/модуль)
- `default` — значение по умолчанию (`true`/`false`)
- `scope` — область применения: `client` (только клиент), `server` (только сервер), `both` (оба)
- `kill_switch` — связанный kill-switch (если есть, иначе `-`)
- `description` — краткое описание назначения

## Реестр флагов

| name | type | owner | default | scope | kill_switch | description |
|------|------|-------|---------|-------|-------------|-------------|
| `NEXY_FEATURE_FIRST_RUN_V2` | feature | permissions | true | client | `NEXY_KS_PERMISSION_RESTART_V2` | Включить систему первого запуска (v2) |
| `NEXY_FEATURE_PERMISSION_RESTART_V2` | feature | permissions | true | client | `NEXY_KS_PERMISSION_RESTART_V2` | Включить автоматический перезапуск после разрешений (v2) |
| `NEXY_KS_PERMISSION_RESTART_V2` | kill_switch | permissions | true | client | - | Отключить автоматический перезапуск (мгновенный откат) |
| `NEXY_DISABLE_AUTO_RESTART` | kill_switch | permissions | false | client | - | Dry-run mode (перезапуск не выполняется, env переменная) |
| `NEXY_FEATURE_AVFOUNDATION_AUDIO_V2` | feature | audio | false | client | `NEXY_KS_AVFOUNDATION_AUDIO_V2` | Включить AVFoundation аудиосистему (master switch) |
| `NEXY_FEATURE_AVFOUNDATION_INPUT_MONITOR_V2` | feature | audio | false | client | `NEXY_KS_AVFOUNDATION_INPUT_MONITOR_V2` | Включить AVFoundation мониторинг input устройств |
| `NEXY_FEATURE_AVFOUNDATION_OUTPUT_V2` | feature | audio | false | client | `NEXY_KS_AVFOUNDATION_OUTPUT_V2` | Включить AVFoundation output (AVAudioEngine) |
| `NEXY_FEATURE_AVFOUNDATION_ROUTE_MANAGER_V2` | feature | audio | false | client | `NEXY_KS_AVFOUNDATION_ROUTE_MANAGER_V2` | Включить RouteManager для reconcile логики |
| `NEXY_KS_AVFOUNDATION_AUDIO_V2` | kill_switch | audio | false | client | - | Отключить AVFoundation аудиосистему (мгновенный откат, master kill-switch) |
| `NEXY_KS_AVFOUNDATION_INPUT_MONITOR_V2` | kill_switch | audio | false | client | - | Отключить AVFoundation мониторинг input (мгновенный откат) |
| `NEXY_KS_AVFOUNDATION_OUTPUT_V2` | kill_switch | audio | false | client | - | Отключить AVFoundation output (мгновенный откат) |
| `NEXY_KS_AVFOUNDATION_ROUTE_MANAGER_V2` | kill_switch | audio | false | client | - | Отключить RouteManager (мгновенный откат) |
| `serial_tcc_prompts` | feature | permissions | false | client | `ks_serial_tcc` | Последовательный показ TCC диалогов (зарезервировано для будущего релиза) |
| `ks_serial_tcc` | kill_switch | permissions | false | client | - | Мгновенно отключает serial_tcc_prompts (зарезервировано) |
| `NEXY_KS_SERIAL_TCC` | kill_switch | permissions | false | client | - | Мгновенно отключает serial_tcc_prompts (env переменная, альтернатива ks_serial_tcc) |
| `NEXY_KS_FIRST_RUN_RESTART` | kill_switch | permissions | false | client | - | Отключить перезапуск после first-run (env переменная, мгновенный откат) |
| `NEXY_DISABLE_TERMINAL_PERMISSIONS_BYPASS` | kill_switch | permissions | false | client | - | Отключить обход проверки разрешений в терминале (env переменная) |
| `NEXY_DISABLE_TRAY` | kill_switch | tray | false | client | - | Отключить tray меню (env переменная, для тестирования) |
| `use_events_for_update_status` | feature | core | true | client | - | Включить shadow-mode публикацию `updater.in_progress.changed` вместо прямого state_data |
| `use_events_for_restart_pending` | feature | core | true | client | - | Читать `permissions.restart_pending` через события/селекторы вместо прямого state_data |
| `critical_subscriptions_fix` | feature | core | true | client | - | Гарантирует подписку на `permissions.*` до инициализации интеграций (fix race) |
| `ks_first_run_normalization` | kill_switch | permissions | false | client | - | Отключает gateway-проверку first_run/restart_pending для PermissionRestartIntegration |
| `actions.open_app` | feature | mcp | true | client | - | Включить функциональность открытия приложений через MCP (Feature ID: F-2025-013) |
| `actions.close_app` | feature | mcp | true | client | - | Включить функциональность закрытия приложений через MCP (Feature ID: F-2025-014) |
| `actions.browser_use` | feature | mcp | true | both | - | Включить веб-автоматизацию через голосовые команды (Feature ID: F-2025-015) |
| `actions.close_browser` | feature | mcp | true | both | - | Включить явное закрытие браузера через голосовые команды |
| `actions.messages` | feature | mcp | true | client | - | Работа с iMessage/SMS (F-2025-016) |
| `features.payment` | feature | payment | true | client | `ks_payment` | Включить систему оплаты и подписок (Tray menu + Integration) |
| `features.messages` | feature | messages | true | client | - | Включить команды iMessage (read_messages, send_message, find_contact) |
| `features.browser` | feature | browser | true | client | - | Включить browser automation интеграции (BrowserUseIntegration, BrowserProgressIntegration) |
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

**ОБЯЗАТЕЛЬНО**: Перед использованием любого флага в коде выполните следующие шаги:

1. **Добавьте флаг в реестр** (`Docs/FEATURE_FLAGS.md`) с обязательными колонками:
   - `name` — имя флага (например: `NEXY_FEATURE_*` или `NEXY_KS_*`)
   - `type` — `feature` или `kill_switch`
   - `owner` — владелец (команда/модуль: `permissions`, `audio`, `core`, `tray`, и т.д.)
   - `default` — значение по умолчанию (`true`/`false`)
   - `scope` — область применения (`client`/`server`/`both`)
   - `kill_switch` — связанный kill-switch (если есть, иначе `-`)
   - `description` — краткое описание назначения

2. **Добавьте конфигурацию** в `unified_config.yaml` (если флаг управляется через конфиг)

3. **Запустите проверку**: `python3 scripts/verify_feature_flags.py`
   - Скрипт автоматически проверит, что все флаги в коде зарегистрированы в реестре
   - При ошибке скрипт укажет файл и строку, где найден незарегистрированный флаг

4. **Проверка интегрирована** в `scripts/verify_architecture.py` и выполняется автоматически перед мерджем

## Проверка в CI

Все feature flags должны быть зарегистрированы в этом файле перед мерджем (см. `.cursorrules` раздел 6.1 и 19.1).

**Автоматическая проверка**:
- `scripts/verify_feature_flags.py` — проверяет соответствие кода и реестра
- `scripts/verify_architecture.py` — включает проверку флагов в общий архитектурный гейт
