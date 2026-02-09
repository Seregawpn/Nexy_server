# Task Brief: Welcome gRPC Connect Race Fix

## Symptom
- На старте welcome-поток доходил до `generate_welcome_audio`, но воспроизведение не запускалось стабильно.
- В логах видно повторный connect сразу после успешного connect в тот же сервер.

## Root Cause
- `ConnectionManager.connect()` был неидемпотентным: каждый вызов запускал `_connect()` и пересоздавал канал, даже если уже `CONNECTED`.
- При старте было несколько конкурентных вызовов connect (eager connect + welcome RPC), из-за чего канал пересоздавался во время активного welcome RPC.

## Fix
- Файл: `modules/grpc_client/core/connection_manager.py`
- В `connect()` добавлен guard:
  - если уже `CONNECTED`,
  - есть активный `channel`,
  - и запрошен тот же сервер,
  - тогда reconnect пропускается (`return True`).

Это переводит `connect()` в корректный single-flight/idempotent режим для одинаковой цели подключения.

## Validation
- `python3 -m py_compile modules/grpc_client/core/connection_manager.py integration/integrations/welcome_message_integration.py` — OK.

## Expected Result
- Повторные вызовы `connect()` во время старта не рвут активный канал.
- Welcome RPC не прерывается лишним reconnect.
- После успешной генерации welcome доходит до отправки в playback-пайплайн.
