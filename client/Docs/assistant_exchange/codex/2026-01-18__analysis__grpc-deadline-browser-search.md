# Browser Search Failure — Analysis

## Context
- Пользователь наблюдает сбой во время «browser search».
- Логи показывают: `grpc.response.audio` поток, затем `StatusCode.DEADLINE_EXCEEDED` и reset session_id.

## Findings
- Фактический сбой происходит в gRPC аудио-стриме (`StreamAudio`): deadline exceeded.
- После ошибки цепочка: `grpc.request_failed` → `playback.failed` → возврат в `AppMode.SLEEPING`.
- В предоставленном отрывке нет событий `browser.progress`, поэтому «browser search» не подтвержден логами.

## Likely Cause
- В `modules/grpc_client/core/grpc_client.py` для `StreamAudio` используется фиксированный timeout=30с.
- Длинная серверная операция (например, browser search) может не успеть отправить данные за 30с → gRPC deadline exceeded.

## Suggested Fix Direction
- Передавать timeout из `GrpcClientIntegrationConfig.request_timeout_sec` в `GrpcClient.stream_audio` вместо жесткой 30с.
- Проверить server-side keepalive/первые чанки, чтобы не превышать deadline.

## References
- `modules/grpc_client/core/grpc_client.py`
- `integration/integrations/grpc_client_integration.py`
