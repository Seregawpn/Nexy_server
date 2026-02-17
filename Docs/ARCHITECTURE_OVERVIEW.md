# Nexy Architecture Overview (Root Index)

Этот файл — корневой индекс архитектуры и владельцев канонов.
Детальная runtime-логика должна храниться только в канонических документах ниже.

## Source of Truth

### Client (macOS runtime)
- Архитектура: `client/Docs/ARCHITECTURE_OVERVIEW.md`
- Контракты flow/events: `client/Docs/FLOW_INTERACTION_SPEC.md`
- Каталог состояний: `client/Docs/STATE_CATALOG.md`
- Требования клиента: `client/Docs/PROJECT_REQUIREMENTS.md`

### Server (gRPC/runtime/deploy)
- Архитектура: `server/server/Docs/ARCHITECTURE_OVERVIEW.md`
- Контракты flow: `server/server/Docs/FLOW_INTERACTION_SPEC.md`
- Протокол/аудит: `server/server/Docs/GRPC_PROTOCOL_AUDIT.md`
- Deploy: `server/server/Docs/SERVER_DEPLOYMENT_GUIDE.md`
- Release/AppCast: `server/server/Docs/RELEASE_AND_UPDATE_GUIDE.md`
- Incident runbook: `server/server/Docs/DEPLOY_INCIDENT_RUNBOOK.md`

## Root-level rules
- В root-документах не дублируем runtime-детали client/server (чтобы не создавать второй источник истины).
- Любые изменения архитектуры выполняются в профильном каноне (client или server) и затем отражаются ссылкой в root.
- Для межассистентной передачи используйте `Docs/ASSISTANT_COORDINATION_PROTOCOL.md` и `Docs/assistant_exchange/TEMPLATE.md`.
- Архитектурные гейты (single-owner/anti-race/flags) фиксируются в `Docs/ARCHITECTURE_GOVERNANCE.md`.
- Release integrity gate: production release должен исключать риск Gatekeeper “Open Anyway”; проверки подписи/нотаризации и publish-порядок закреплены в:
  - `client/Docs/RELEASE_VERSIONING_AND_PUBLISHING.md` (раздел `9. Пошаговый Production Release`)
  - `server/server/Docs/RELEASE_AND_UPDATE_GUIDE.md`

## Quick integrity checks
- Пути из требований должны существовать физически.
- Startup order клиента сверяется с `client/integration/core/integration_factory.py::STARTUP_ORDER`.
- Документация first-run должна соответствовать `client/modules/permissions/v2/` и `client/config/unified_config.yaml`.

## Change policy
- Обновления в этом файле разрешены только как index/scope changes.
- Runtime-контент переносится в client/server каноны, а не добавляется сюда.
