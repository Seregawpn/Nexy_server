# Mode Log Clarity and Preempt Press Guard

## Метаданные
- Ассистент: codex
- Тип: task-brief
- Дата: 2026-02-11
- ID (INS-###): N/A

## Diagnosis
- По логам mode transition в tray показывался как `sleeping -> sleeping`/`listening -> listening`, что скрывало реальные переходы.
- В `InputProcessingIntegration` был узкий race-window: press при preempt мог сразу армить новый цикл и давать лишний `armed -> short_tap -> reset`.

## Root Cause
- `app.mode_changed` не содержал `old_mode`, а tray логировал переход без явного источника old/new.
- Press-preempt path не имел краткого suppress окна на тот же press во время interrupt/mode-transition in-flight.

## Optimal Fix
- `StateManager` теперь публикует `old_mode/new_mode` внутри `app.mode_changed`.
- `TrayControllerIntegration` логирует режим как `old_mode -> new_mode`.
- В `InputProcessingIntegration` добавлен preempt-press guard:
  - после `interrupt.request` на `keyboard.press_preempt` ставится suppress окно 150ms;
  - press в этом окне игнорируется (long_press после окна работает штатно).

## Verification
- `pytest -q tests/test_tray_quit_dispatch.py tests/test_user_quit_ack.py tests/test_keyboard_monitor_dispatch_order.py tests/test_keyboard_monitor_stale_timeout.py tests/test_quartz_stale_state_timeout.py tests/test_quartz_voiceover_passthrough.py tests/test_interrupt_playback.py`
- Результат: `31 passed`.

## Запрос/цель
- Убрать лог-шум и пограничную гонку preempt/press, сохранив текущую архитектуру.

## Контекст
- Файлы:
  - `integration/core/state_manager.py`
  - `integration/integrations/tray_controller_integration.py`
  - `integration/integrations/input_processing_integration.py`

## Решения/выводы
- Source of truth по mode переходам стал прозрачнее в логах.
- Поведение preempt в input стало детерминированнее без новых state owners.

## Открытые вопросы
- Нужен ручной прогон пользовательского сценария (Safari/YouTube/VO/Spotlight) для финального подтверждения UX.

## Следующие шаги
- Повторить сценарий из пользовательских логов и проверить отсутствие лишнего `idle -> armed -> short_tap -> reset` сразу после preempt.
