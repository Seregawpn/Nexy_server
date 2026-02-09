# Handoff: PTT dedup and race guards (Secure Input / Release / Reset)

## Scope
- Устранены дубли terminal stop и лишние `mode.request(SLEEPING)` в PTT lifecycle.
- Добавлен guard против гонки `Secure Input fail-safe` vs `RELEASE -> PROCESSING`.

## Applied changes
- File: `integration/integrations/input_processing_integration.py`

1. `SESSION RESET` stop dedup:
   - В `_reset_session()` stop-публикация теперь проходит через `terminal stop` guard.
   - Условие расширено до `(_recording_started or _mic_active)` для корректного аварийного закрытия.

2. SLEEPING request dedup:
   - Добавлены поля:
     - `_last_sleep_mode_request_sig`
     - `_last_sleep_mode_request_ts`
     - `_sleep_mode_request_dedup_window_sec`
   - Добавлен метод `_publish_sleeping_mode_request_once(...)` для короткого anti-spam окна.
   - `Secure Input` force-stop использует этот метод вместо прямого `event_bus.publish("mode.request", ...)`.

3. RELEASE race guard:
   - В `_handle_key_release()` перед переходом в `PROCESSING` добавлен check:
     - если `self._secure_input_active == True`, переход в `PROCESSING` пропускается,
     - отправляется dedup `mode.request(SLEEPING)`,
     - lifecycle переводится в `IDLE`.

## Validation
- `python3 -m py_compile integration/integrations/input_processing_integration.py` passed.

## Expected effect
- Один terminal stop на press-cycle (без повторного `voice.recording_stop` из reset-path).
- Меньше дублирующих `mode.request(SLEEPING)` в коротких race-сценариях.
- Нет перехода в `PROCESSING`, если во время RELEASE уже активирован `Secure Input` fail-safe.
