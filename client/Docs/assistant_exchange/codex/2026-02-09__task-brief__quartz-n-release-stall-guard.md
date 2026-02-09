# Task Brief: Quartz N-release stall guard

## Problem
- По логам `pending release N` подтверждался через ~0.1s и вызывал `DEACTIVATION TRIGGERED`, хотя удержание еще продолжалось.
- Это приводило к преждевременному `RELEASE` и сбросу записи.

## Root Cause
- Критерий подтверждения отпускания `N` был слишком агрессивным (короткий таймер без проверки паузы автоповтора).

## Change
- Файл: `modules/input_processing/keyboard/mac/quartz_monitor.py`
- Добавлен guard: `self._n_repeat_stall_release_sec = 0.35`
- Подтверждение `pending release N` теперь проходит только если:
  - истек `confirm_delay`, и
  - нет автоповтора `N` минимум `0.35s` (`now - _n_last_event_time >= stall`).
- Если автоповтор был недавно, pending release отклоняется.

## Validation
- `python3 -m py_compile modules/input_processing/keyboard/mac/quartz_monitor.py` — успешно.

## Expected
- Удержание `Ctrl+N` не будет случайно срываться из-за кратковременных пауз/ложных `keyUp N`.
