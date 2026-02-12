# Task Brief

- Author: Codex
- Date: 2026-02-11
- Type: task-brief

## Request
Понять, почему иногда не срабатывает сигнал перехода в SLEEPING, и убрать дубли/конфликты.

## Context
- Файл: `integration/integrations/signal_integration.py`
- Наблюдение в логах: `Signals: SLEEP cue skipped (dedup session=...)`
- Одновременно присутствовали два пути эмиссии terminal/sleep cues: `processing.terminal` и `app.mode_changed`.

## Diagnosis
Два конкурирующих владельца DONE/SLEEP cue в одном модуле создавали подавление через dedup и неочевидное поведение.

## Implemented Fix
- Централизован владелец SLEEP cue: только `app.mode_changed`.
- В `_on_mode_changed` удален dedup по `_last_terminal_session_id`.
- В `_on_processing_terminal` отключена эмиссия terminal-тонов; оставлен только debug-лог (событие жизненного цикла сохраняется).
- Удалено поле `_last_terminal_session_id`.

## Architecture Fit
- Source of Truth для смены режима и SLEEP cue: `app.mode_changed`.
- Централизация соблюдена, второй путь принятия решения удален.

## Risks
- Низкий: меняется только политика эмиссии signal cues.
- Возможный эффект: больше не будет terminal cue до mode change (ожидаемо и целенаправленно).

## Verification
- `python3 -m py_compile integration/integrations/signal_integration.py` — OK.
- Ожидаемые логи после фикса:
  - Есть `Signals: SLEEP cue (app.mode_changed, old=...)`.
  - Нет `Signals: SLEEP cue skipped (dedup session=...)`.
  - Нет `Signals: TERMINAL (...)` как источника DONE/SLEEP.

## Next Steps
- Прогнать 3 сценария: success, failed_recognition, interrupt.
- Подтвердить единичный SLEEP cue на каждое `PROCESSING -> SLEEPING`.
