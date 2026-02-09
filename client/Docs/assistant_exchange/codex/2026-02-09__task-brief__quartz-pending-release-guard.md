# Task Brief: Quartz pending-release guard for Ctrl+N

## Context
- Симптом: во время удержания `Ctrl+N` периодически приходил ложный `keyUp N`, что мгновенно вызывало `RELEASE`.
- Эффект: `InputProcessingIntegration` завершал запись и переводил режим в `PROCESSING`, после offline-ошибки система уходила в `SLEEPING`.

## Root Cause
- В `QuartzKeyboardMonitor` деактивация комбинации происходила сразу на первом `keyUp N`.
- Для подавляемого `N` это создаёт race: transient/ложный `keyUp` интерпретировался как реальный отпуск.

## Changes
- Файл: `modules/input_processing/keyboard/mac/quartz_monitor.py`
- Добавлен anti-race state:
  - `_pending_n_release_at`
  - `_n_release_confirm_delay_sec=0.09`
- Логика:
  - При `keyUp N` в состоянии `combo_active=True` и `control_pressed=True` release не выполняется сразу, а ставится в `pending`.
  - Любой следующий `keyDown N` отменяет pending (ложный `keyUp`).
  - В watchdog (`_check_and_reset_stuck_state`) pending подтверждается по таймеру и только тогда выполняется деактивация комбинации.
  - При `Control up` pending очищается.
  - При reset залипшего состояния pending тоже очищается.

## Validation
- `python3 -m py_compile modules/input_processing/keyboard/mac/quartz_monitor.py` — успешно.

## Expected Outcome
- Удержание `Ctrl+N` не прерывается из-за одиночного ложного `keyUp N`.
- `RELEASE` происходит только при подтверждённом отпускании, что стабилизирует переходы режимов.
