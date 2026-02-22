# Task Brief — STT interim commit gate (client)

## Контекст
В `GrpcClientIntegration` запрос мог стартовать на `voice.recognition_completed(interim=true)` и/или косвенно через `screenshot.captured`, если текст уже был в session buffer.

## Что сделано
- Добавлен commit-gate в `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/integration/integrations/grpc_client_integration.py`:
  - `interim=true`:
    - обновляет только `sess["text"]`
    - ставит `sess["ready_to_send"]=False`
    - **не вызывает** `_maybe_send`
  - `interim=false`:
    - ставит `sess["ready_to_send"]=True`
    - вызывает `_maybe_send`
- В `_maybe_send` добавлены guards:
  - send только при `ready_to_send=True`
  - single-dispatch per session через `sess["dispatched"]`

## Архитектурные гейты
- Single Owner Gate: owner запуска send остается `GrpcClientIntegration` (без второго owner-path).
- Zero Duplication Gate: ранний send-path из interim исключен, единый terminal gate в `_maybe_send`.
- Anti-Race Gate: `dispatched` предотвращает повторный запуск для того же `session_id`.
- Flag Lifecycle Gate: новых runtime-флагов не добавлено.

## Измененные файлы
- `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/integration/integrations/grpc_client_integration.py`
- `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/tests/test_grpc_client_interim_commit_gate.py`

## Проверка
- `pytest -q tests/test_grpc_client_interim_commit_gate.py` (cwd=`client`) → `2 passed`
- `pytest -q tests/test_voice_audio_owner_guards.py` (cwd=`client`) → `8 passed`

## Риск/ограничение
Это клиентский этап commit-gate. Полный collect/commit на уровне protobuf/server workflow пока не внедрен.
