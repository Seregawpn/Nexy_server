# Task Brief — Collect/Commit streaming phases (client+server)

## Goal
Реализовать двухфазную передачу данных:
- `COLLECT`: отправка partial STT чанков и раннего скриншота без запуска LLM;
- `COMMIT`: запуск полной серверной обработки только после финального события.

## Что внедрено

### 1) Протокол
Добавлены поля в `StreamRequest` (client/server proto):
- `phase` (`REQUEST_PHASE_COLLECT|REQUEST_PHASE_COMMIT`)
- `chunk_seq`
- `chunk_text`

Файлы:
- `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/modules/grpc_client/proto/streaming.proto`
- `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/server/server/modules/grpc_service/streaming.proto`

### 2) Client transport (owner: GrpcClientIntegration)
- `interim=true`:
  - обновляет буфер сессии,
  - инкрементирует `collect_seq`,
  - отправляет `COLLECT` с `chunk_text`.
- ранний `screenshot.captured`:
  - отправляет `COLLECT` со скриншотом (dedup по hash).
- `interim=false`:
  - помечает `ready_to_send=True` и запускает `COMMIT` path (как основной запрос).
- commit-path по-прежнему single-dispatch (`dispatched` guard).

Файл:
- `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/integration/integrations/grpc_client_integration.py`

### 3) Client gRPC core
- `GrpcClient.stream_audio(...)` расширен параметрами:
  - `phase`, `chunk_seq`, `chunk_text`
- При формировании `StreamRequest` выставляются новые поля.

Файл:
- `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/modules/grpc_client/core/grpc_client.py`

### 4) Server StreamAudio handler
- Добавлен collect-buffer per session в `NewStreamingServicer`:
  - хранит `last_seq`, `chunks`, `screenshot`, размеры.
- `COLLECT`:
  - только буферизует,
  - out-of-order защита (`chunk_seq <= last_seq` -> drop),
  - возвращает `end_message=collect_ok` без запуска workflow.
- `COMMIT`:
  - объединяет collected state + final request,
  - запускает существующую processing цепочку один раз,
  - очищает collected state (pop).

Файл:
- `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/server/server/modules/grpc_service/core/grpc_server.py`

### 5) Regenerated protobuf artifacts
- `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/modules/grpc_client/proto/streaming_pb2.py`
- `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/modules/grpc_client/proto/streaming_pb2_grpc.py`
- `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/server/server/modules/grpc_service/streaming_pb2.py`
- `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/server/server/modules/grpc_service/streaming_pb2_grpc.py`

### 6) Тесты
Добавлен тест server collect/commit flow:
- `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/server/server/tests/test_grpc_collect_commit_flow.py`

## Архитектурные гейты
- Single Owner: запуск обработки остаётся в `StreamAudio` COMMIT path.
- Zero Duplication: удален ранний старт из interim send-path.
- Anti-Race:
  - client: `dispatched` + `ready_to_send`;
  - server: `chunk_seq` monotonic guard + `pop on commit`.
- Flag Lifecycle: новые runtime-флаги не добавлялись.

## Проверки
- `./scripts/regenerate_proto.sh` → OK
- `pytest -q server/server/tests/test_grpc_identifier_validation.py server/server/tests/test_grpc_collect_commit_flow.py` → 8 passed
- `pytest -q tests/test_grpc_client_interim_commit_gate.py` (cwd=`client`) → 2 passed
- `python3 -m py_compile ...` (измененные python файлы) → OK

## Оставшийся риск
COLLECT сейчас реализован через отдельные unary-like вызовы `StreamAudio` (short-lived stream with `collect_ok`).
Это рабочий и архитектурно совместимый этап, но при очень высокой частоте interim может потребоваться дополнительная client-side коалесценция/дебаунс.
