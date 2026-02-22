# Task Brief — Collect/Commit hardening (debounce + TTL + buffer limits)

## Scope
После базового collect/commit добавлены anti-race и anti-growth guard'ы:
- client collect debounce;
- server stale collect cleanup (TTL);
- server collect buffer limits.

## Изменения

### Client (`GrpcClientIntegration`)
Файл:
- `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/integration/integrations/grpc_client_integration.py`

Что добавлено:
- `self._collect_pending` per session и `self._collect_debounce_sec=0.12`.
- `_schedule_collect_send` теперь:
  - дебаунсит текстовые collect отправки,
  - коалесцирует в последний `chunk_text/chunk_seq`,
  - отправляет screenshot-collect без задержки.
- cancel lifecycle:
  - `_cancel_collect_pending(session_id)`
  - `_cancel_collect_pending_all()`
  - вызывается на commit, request_cancel, interrupt, stop.

### Server (`NewStreamingServicer`)
Файл:
- `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/server/server/modules/grpc_service/core/grpc_server.py`

Что добавлено:
- параметры hardening:
  - `_collect_ttl_sec=90.0`
  - `_collect_max_chunks=256`
  - `_collect_max_text_chars=20000`
- `_cleanup_collect_sessions()` — удаляет stale collect sessions.
- `_collect_phase_store()`:
  - хранит `updated_at`, `total_chars`,
  - ограничивает рост буфера по chunks/chars.
- `StreamAudio()` вызывает cleanup на входе.

## Тесты

### Client
- `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/tests/test_grpc_client_interim_commit_gate.py`
  - debounce отправляет только последний chunk;
  - screenshot collect отправляется сразу.

### Server
- `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/server/server/tests/test_grpc_collect_commit_flow.py`
  - stale cleanup удаляет протухшие collect state;
  - buffer limits сохраняют стабильность без роста.

## Прогоны
- `pytest -q tests/test_grpc_client_interim_commit_gate.py` (cwd=`client`) → `4 passed`
- `pytest -q server/server/tests/test_grpc_collect_commit_flow.py server/server/tests/test_grpc_identifier_validation.py` → `10 passed`
- `python3 -m py_compile ...` (измененные файлы) → OK

## Архитектурные гейты
- Single Owner: запуск LLM только через COMMIT path.
- Zero Duplication: collect trigger централизован в одном owner (`GrpcClientIntegration`).
- Anti-Race:
  - client: pending-task cancellation + debounced coalescing + dispatched gate;
  - server: seq guard + ttl cleanup + buffer limits.
- Flag Lifecycle: новые feature flags не добавлялись.
