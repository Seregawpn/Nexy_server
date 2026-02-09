# Analysis: PTT sticky mic on Ctrl+N release under Quartz/Secure Input

## Context
- Симптом: после отпускания `Ctrl+N` микрофон продолжал слушать.
- Логи показали две связанные проблемы:
  - `quartz_monitor` держит combo активной при подавлении событий (`local=True, actual=False`).
  - `input_processing_integration` падал в аварийном stop-path: `AttributeError: _track_task`.

## Root causes
1. **Broken emergency stop path**
   - `InputProcessingIntegration._reset_session()` вызывал `self._track_task(...)`, но метод отсутствовал.
   - При `grpc_failed` fail-safe остановки микрофона не выполнялся.

2. **No centralized fail-safe on tap degradation**
   - При `Secure Input`/tap disable интеграция помечала `ptt_available=False`, но не завершала активный press/session принудительно.
   - Это оставляло второй активный путь состояния (`PTT lifecycle` vs фактический input stream).

## Changes implemented
- File: `integration/integrations/input_processing_integration.py`

1. Added missing background task runner:
   - `_track_task()` with safe loop handling (`running_loop` or `event_bus._loop`).

2. Added centralized fail-safe for secure-input degradation:
   - `_force_stop_active_ptt(reason)`:
     - сбрасывает `PTT_PRESSED`,
     - публикует `interrupt.request` + `grpc.request_cancel`,
     - публикует `voice.recording_stop` (idempotent),
     - ждёт `voice.mic_closed` с таймаутом и fallback reset,
     - отправляет `mode.request -> SLEEPING`,
     - сбрасывает сессию/lifecycle в `IDLE`.

3. Updated health-check orchestration:
   - `_run_health_check()` теперь на переходе `tap_enabled: true -> false` запускает `_force_stop_active_ptt(...)`.
   - Добавлен флаг `_secure_input_active` для edge-trigger поведения (без повторного шторминга событий каждый тик).

## Verification run
- `python3 -m py_compile integration/integrations/input_processing_integration.py` passed.

## Expected behavioral delta
- При `grpc_failed` больше нет падения аварийной остановки из-за `_track_task`.
- При `Secure Input` активный PTT цикл принудительно закрывается и не зависает в `LISTENING`.
- После восстановления tap PTT возвращается без двойных owner-path.
