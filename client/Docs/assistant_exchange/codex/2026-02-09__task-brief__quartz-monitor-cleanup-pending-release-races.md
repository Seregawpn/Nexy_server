# Quartz Monitor Cleanup: pending-release races and log noise

## Goal
Снизить ложные RELEASE при удержании combo и убрать дубли/шум в quartz monitor.

## Changes
- Добавлен `self._pending_n_stale_sec`.
- В `_reconcile_combo_state()` синхронизация Control через flags больше не выполняется, когда локально зажаты `Control` и `N`.
- В `_check_and_reset_stuck_state()` добавлена очистка протухших pending-состояний (`N` и `Control`) до confirm-логики.
- Подтверждение `pending release Control` теперь только при свежей коррелированной паре (`Control+N`).
- Убраны `print(...)` отладочные выводы (оставлен logger).
- Уменьшен шум deactivation-логов (без stack dump на каждом триггере).

## File
- `/Users/sergiyzasorin/Fix_new/client/modules/input_processing/keyboard/mac/quartz_monitor.py`

## Validation
- `python3 -m py_compile /Users/sergiyzasorin/Fix_new/client/modules/input_processing/keyboard/mac/quartz_monitor.py`

