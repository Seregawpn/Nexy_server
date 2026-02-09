# Handoff: Quartz Monitor V2 rebuild

## Scope
- Полностью пересоздан `modules/input_processing/keyboard/mac/quartz_monitor.py` как thin adapter.

## What changed

1. Удалена сложная локальная бизнес-логика lifecycle.
2. Оставлены только low-level обязанности:
   - детекция edge-событий (`PRESS`, `LONG_PRESS`, `RELEASE`)
   - `SHORT_PRESS` только для non-combo пути
   - подавление combo-клавиш для Ctrl+N
   - health/status (`tap_enabled`, recovery counter)
3. Добавлен forced release на событиях tap disable:
   - `kCGEventTapDisabledByTimeout`
   - `kCGEventTapDisabledByUserInput`
4. Сохранен API-совместимый контракт:
   - `register_callback`
   - `set_loop`
   - `start_monitoring`
   - `stop_monitoring`
   - `get_status`

## Compile validation
- `python3 -m py_compile modules/input_processing/keyboard/mac/quartz_monitor.py`
- `python3 -m py_compile integration/integrations/input_processing_integration.py`

## Expected runtime effect
- Quartz не является владельцем PTT lifecycle (owner = InputProcessingIntegration).
- При tap disable combo не залипает локально: monitor принудительно эмитит RELEASE.
- Логика mode/session остается централизованной в coordinator.
