# Analysis: Ctrl combo global capture verification

## Summary
- Проверен текущий код input-стека.
- `Control` сам по себе не блокируется.
- Комбинация `Ctrl+N` перехватывается глобально и не пробрасывается в другие приложения, пока активен keyboard monitor.

## Evidence
- `config/unified_config.yaml`: `integrations.keyboard.key_to_monitor: ctrl_n`, `enable_keyboard_monitoring: true`.
- `integration/integrations/input_processing_integration.py`: монитор запускается в `start()` и работает глобально.
- `modules/input_processing/keyboard/mac/quartz_monitor.py`:
  - `Control flagsChanged` возвращает `event` (не блокирует сам `Control`).
  - при `N keydown` + нажатом `Control` активируется combo и возвращается `None` (событие подавляется).

## Conclusion
- Если проблема про `Ctrl+N` в других приложениях при включённом Nexy: это ожидаемое текущее поведение.
- Если проблема про отдельный `Control` (без `N`): по коду блокировки нет; в таком случае искать runtime race/secure-input сценарий в логах.
