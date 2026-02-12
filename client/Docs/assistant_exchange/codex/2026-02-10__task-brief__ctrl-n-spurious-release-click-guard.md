# Task Brief — Ctrl+N spurious release click guard

## Context
Пользователь сообщил «щелчки» при активации микрофона по комбинации `Ctrl+N`, особенно критично не ломать VoiceOver/shortcut behavior.

## Diagnosis
По `log.md` видно micro-flap аудиосессии: быстрое `input_running=true -> false` в пределах миллисекунд.
Это соответствует ложному раннему `RELEASE` сразу после `LONG_PRESS` (микрофон стартует и мгновенно закрывается).

## Root cause
В owner-слое PTT (`InputProcessingIntegration`) не было guard против раннего ложного `RELEASE`.
Если Quartz/модификаторы дают transient pulse, lifecycle проходил в terminal stop, что и создавало audible click.

## Implemented changes
1. File: `integration/integrations/input_processing_integration.py`
- Added `self._spurious_release_guard_sec = 0.12`.
- Added `_is_spurious_early_release(event)`:
  - проверяет окно после старта записи,
  - подтверждает физическое удержание через `keyboard_monitor.get_status()`.
- Added `_is_input_still_physically_pressed()`:
  - generic: `key_pressed`,
  - combo: `combo_active` OR (`control_pressed` and `n_pressed` and not `combo_blocked_by_modifiers`).
- Updated `_handle_release()`:
  - short-tap path unchanged,
  - for early spurious release: suppress terminal stop, keep `PTT_PRESSED=True`, wait for real release,
  - normal release path unchanged.

2. File: `tests/test_interrupt_playback.py`
- Added `test_release_suppressed_when_combo_still_pressed_early_after_start`.
- Added `test_release_not_suppressed_when_combo_not_pressed`.

## Architecture fit
- Source of Truth не менялся: `InputProcessingIntegration` остается owner PTT lifecycle.
- Quartz/Keyboard monitor остаются low-level adapters и не принимают бизнес-решений.
- Новых параллельных state-owner путей не введено.

## Verification
- `PYTHONPATH=. pytest -q tests/test_interrupt_playback.py -k "release_suppressed_when_combo_still_pressed_early_after_start or release_not_suppressed_when_combo_not_pressed"`
- Result: `2 passed`.

## Expected effect
- Убираются ложные мгновенные `recording_start -> recording_stop` циклы, которые давали щелчки.
- Реальный `RELEASE` продолжает работать как раньше.
- VoiceOver и другие shortcut не блокируются (tap по-прежнему listen-only, modifier guard сохранен).
