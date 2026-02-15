# Task Brief: Release v1.6.1.38 Publish

## Scope
Подготовка и заливка клиентского репозитория в GitHub c версией `v1.6.1.38`.

## Changes
- Обновлен единый источник версии:
  - `config/unified_config.yaml`: `app.version` `1.6.0.37` -> `1.6.1.38`
- В commit также включены ранее подготовленные канонические doc-sync изменения:
  - `Docs/FLOW_INTERACTION_SPEC.md`
  - `Docs/ARCHITECTURE_OVERVIEW.md`
  - `Docs/PROJECT_REQUIREMENTS.md`
  - `Docs/README.md`
  - `Docs/assistant_exchange/codex/2026-02-15__analysis__compatibility-bridges-doc-sync.md`

## Verification
- Политика remote: push только в `client_test`.
- Версия читается из `config/unified_config.yaml` как single source of truth для packaging scripts.

## Publish
- Branch target: `release/v1.6.1.38`
- Remote: `client_test` (`https://github.com/Seregawpn/Nexy_client_test`)
