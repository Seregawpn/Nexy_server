# Task Brief: Pending Release Pair Correlation

## Context
- После предыдущих правок `pending release Control` всё ещё мог подтверждаться в отрыве от `N` при шумных событиях.

## Change
- В `quartz_monitor.py` добавлена корреляция pending release:
  - `pending Control` имеет stale timeout (`_pending_control_stale_sec=0.8`);
  - подтверждение `Control` допустимо только при наличии `pending N`;
  - добавлен max gap между `pending Control` и `pending N` (`_pending_release_pair_max_gap_sec=0.35`).

## Expected Effect
- Исключается “заднее” подтверждение release по Control без согласованного release N.
- Меньше ложных `DEACTIVATION TRIGGERED` в длительном удержании.

## Validation
- `python3 -m py_compile modules/input_processing/keyboard/mac/quartz_monitor.py` — OK.
