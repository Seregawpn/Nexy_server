# Analysis: Compatibility Bridges Doc Sync (2026-02-15)

## Scope
Синхронизированы канонические документы с фактическим runtime по активным compatibility-путям.

## Diagnosis
Конфликт документации и кода был в описании `grpc.response.action`: в коде активен compatibility путь через `text_chunk`, а в каноне был помечен как отключенный.

## Changes
- `Docs/FLOW_INTERACTION_SPEC.md`
  - Обновлён контракт `grpc.response.action` (primary `ActionMessage` + compatibility `text_chunk_legacy`).
  - Добавлен раздел `5.1 Активные compatibility-пути (runtime)`:
    - `app.state_changed`
    - `permissions.first_run_restart_pending`
    - `grpc.response.action` via `text_chunk_legacy`
    - `speech.playback.request` compatibility ingress
- `Docs/ARCHITECTURE_OVERVIEW.md`
  - Для `grpc_client_integration.py` добавлены `grpc.response.text|action` и правило compatibility-path.
  - Для `tts_integration.py` формулировка уточнена как compatibility ingress.
- `Docs/PROJECT_REQUIREMENTS.md`
  - REQ-007 дополнен правилом owner-path для `grpc.response.action` и ограничением compatibility bridge.
- `Docs/README.md`
  - Добавлена ссылка на compatibility-пути (`FLOW_INTERACTION_SPEC` §5.1).
  - Уточнён архивный контекст: `Docs/_archive/` и `_Docs_ARCHIVED/`.

## Verification
- `./.venv/bin/python scripts/verify_doc_links.py` -> passed.
- grep-проверка конфликтной формулировки (`legacy text-tunneling отключен`) -> не найдена.
- grep-проверка новых маркеров (`text_chunk_legacy`, `Активные compatibility-пути`) -> найдены в канонических документах.

## Result
Документация приведена к фактическому runtime по совместимым путям; явный конфликт `grpc.response.action` устранён.
