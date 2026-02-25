# Feature Flags & Kill-Switches Registry (Server)

**Цель**: Единый реестр всех feature flags и kill-switches серверной части с автоматической проверкой перед внедрением новой логики.

**ВАЖНО**: Все флаги должны быть зарегистрированы в этом реестре ДО использования в коде. Скрипт `scripts/verify_feature_flags.py` автоматически проверяет соответствие кода и реестра.

## Формат реестра

**Обязательные колонки**:
- `name` — имя флага (например: `NEXY_KS_*` или `use_module_coordinator`)
- `type` — тип: `feature` (feature flag) или `kill_switch` (kill-switch)
- `owner` — владелец флага (команда/модуль)
- `default` — значение по умолчанию (`true`/`false`)
- `scope` — область применения: `client` (только клиент), `server` (только сервер), `both` (оба)
- `kill_switch` — связанный kill-switch (если есть, иначе `-`)
- `description` — краткое описание назначения

## Реестр флагов

| name | type | owner | default | scope | kill_switch | description |
|------|------|-------|---------|-------|-------------|-------------|
| `use_module_coordinator` | feature | server-platform | true | server | `disable_module_coordinator` | Включить использование ModuleCoordinator для управления модулями |
| `use_workflow_integrations` | feature | server-platform | true | server | `disable_workflow_integrations` | Включить использование workflow integrations для orchestration |
| `use_fallback_manager` | feature | server-platform | true | server | - | Включить использование FallbackManager для обработки ошибок |
| `forward_assistant_actions` | feature | mcp-integration | true | server | `disable_forward_assistant_actions` | Включить передачу JSON действий на клиента (MCP command forwarding) |
| `messages_enabled` | feature | messages | true | server | - | Включить обработку iMessage-команд в серверном prompt/router |
| `web_search_enabled` | feature | browser | true | server | - | Включить обработку web-search intents и команд |
| `disable_module_coordinator` | kill_switch | server-platform | false | server | - | Отключить ModuleCoordinator (мгновенный откат) |
| `disable_workflow_integrations` | kill_switch | server-platform | false | server | - | Отключить workflow integrations (мгновенный откат) |
| `disable_forward_assistant_actions` | kill_switch | mcp-integration | false | server | - | Отключить передачу JSON действий на клиента (мгновенный откат) |
| `NEXY_KS_DISABLE_MODULE_COORDINATOR` | kill_switch | server-platform | false | server | - | Отключить ModuleCoordinator через env переменную (мгновенный откат) |
| `NEXY_KS_DISABLE_WORKFLOW_INTEGRATIONS` | kill_switch | server-platform | false | server | - | Отключить workflow integrations через env переменную (мгновенный откат) |
| `NEXY_KS_DISABLE_FORWARD_ASSISTANT_ACTIONS` | kill_switch | mcp-integration | false | server | - | Отключить передачу JSON действий на клиента через env переменную (мгновенный откат) |
| `USE_MODULE_COORDINATOR` | env_override | server-platform | true | server | - | Env переменная для переопределения features.use_module_coordinator |
| `USE_WORKFLOW_INTEGRATIONS` | env_override | server-platform | true | server | - | Env переменная для переопределения features.use_workflow_integrations |
| `USE_FALLBACK_MANAGER` | env_override | server-platform | true | server | - | Env переменная для переопределения features.use_fallback_manager |
| `FORWARD_ASSISTANT_ACTIONS` | env_override | mcp-integration | false | server | - | Env переменная для переопределения features.forward_assistant_actions |
| `BROWSER_USE_ENABLED` | env_config | browser | true | server | - | Включить модуль browser automation (F-2025-015) |
| `BROWSER_USE_KEEP_OPEN` | env_config | browser | true | server | - | Сохранять браузер открытым между задачами |
| `BROWSER_USE_TIMEOUT` | env_config | browser | 120 | server | - | Таймаут задачи браузера (секунды) |
| `BROWSER_USE_MAX_STEPS` | env_config | browser | 50 | server | - | Максимум шагов агента на задачу |
| `BROWSER_USE_MODEL` | env_config | browser | gemini-2.5-flash | server | - | LLM модель для browser-агента |
| `MESSAGES_ENABLED` | env_config | messages | true | server | - | Включить интеграцию iMessage (read_messages, send_message, find_contact) |
| `SUBSCRIPTION_ENABLED` | env_config | payment | true | server | - | Включить систему подписок и проверку квот |
| `SUBSCRIPTION_GRANDFATHERED_ENABLED` | env_config | payment | true | server | - | Разрешить unlimited-доступ для статуса `grandfathered` |
| `SUBSCRIPTION_GRANDFATHER_AUTO_ASSIGN_EXISTING` | env_config | payment | false | server | - | One-shot авто-bootstrap grandfathered на старте сервера |
| `SUBSCRIPTION_GRANDFATHER_CUTOFF_DATE` | env_config | payment | - | server | - | Граница one-shot bootstrap (`YYYY-MM-DD`, правило: `created_at < cutoff_date`) |

## Правила добавления

1. **Перед использованием флага**:
   - Добавьте флаг в этот реестр с полной информацией
   - Запустите `python scripts/verify_feature_flags.py` для проверки

2. **Формат флагов**:
   - **Config flags**: `features.*` в `unified_config.yaml` (например: `use_module_coordinator`)
   - **Kill-switches**: `kill_switches.*` в `unified_config.yaml` или `NEXY_KS_*` в env (например: `disable_module_coordinator`)
   - **Env overrides**: `USE_*` или специальные имена (например: `USE_MODULE_COORDINATOR`, `FORWARD_ASSISTANT_ACTIONS`) — env переменные для переопределения feature flags

3. **Обязательные поля**:
   - Все флаги должны иметь `owner`, `default`, `scope`, `description`
   - Kill-switches должны быть связаны с соответствующими feature flags

4. **Проверка перед мерджем**:
   - Скрипт `verify_feature_flags.py` должен проходить без ошибок
   - Все флаги в коде должны быть зарегистрированы в реестре

## Исключения (не feature flags)

Следующие env переменные **НЕ** являются feature flags и исключены из проверки:

- `USE_GITHUB` — используется в update scripts для выбора источника обновлений
- `USE_TLS` — используется в gRPC config для включения TLS, не является feature flag override

**ВАЖНО**: Если вы добавляете новую env переменную с префиксом `USE_*`, которая **не является** feature flag override, добавьте её в список исключений в `scripts/verify_feature_flags.py` (константа `EXCLUDED_USE_VARS`) и обновите этот раздел документации.

## Связанные документы

- `config/unified_config.yaml` — значения флагов
- `config/unified_config.py` — загрузка и валидация конфигурации
- `scripts/verify_feature_flags.py` — автоматическая проверка регистрации
- `Docs/SERVER_DEVELOPMENT_RULES.md` — правила разработки сервера
