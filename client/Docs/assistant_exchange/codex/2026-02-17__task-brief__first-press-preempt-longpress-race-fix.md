# Task Brief: First-press preempt long-press race fix

## Context
В dev-логах первый зажим `Ctrl+N` при хвосте playback часто не запускал запись сразу: состояние уходило в `armed`, затем происходил долгий wait и поздний `long_press` запуск уже после `release`.

## Diagnosis
В `InputProcessingIntegration` был race между preempt/wait и lifecycle release:
- `long_press` мог продолжить выполнение после смены state на `WAITING_GRPC`;
- при preempt по `playback_active` ожидание completion зависело от терминального события playback, которое могло запаздывать/теряться для локального флага.

## Architecture Fit
- Owner: `InputProcessingIntegration` (PTT lifecycle source of truth)
- Source of truth: `PTTState` + `_active_press_id` + локальный `_playback_active`
- Централизация сохранена: не добавлялись новые owner-пути в workflow/mode/speech.

## Implementation
Изменения в `integration/integrations/input_processing_integration.py`:
1. В `_handle_press` после `press_preempt` по причине `playback_active` добавлен локальный fallback:
   - сразу сбрасываем `_playback_active=False`;
   - резолвим локальные `_playback_waiters`.
2. В `_handle_long_press` добавлен stale-tail guard перед `voice.recording_start`:
   - старт разрешен только если state всё ещё `ARMED`;
   - дополнительная проверка `press_id` на совпадение с активным циклом.

## Concurrency / Race Guard
- State-guard по `PTTState.ARMED` перед стартом записи.
- Idempotent wake-up для waiters при preempt-cancel.
- Без новых runtime-флагов и без второго owner пути.

## Verification
- `python3 -m py_compile integration/integrations/input_processing_integration.py` — OK.
- Логически проверено: поздний `long_press` после `release` теперь отсекается stale-guard.

## Информация об изменениях
- Что изменено:
  - Устранена гонка первого зажима при preempt playback.
  - Убран запуск `recording_start` из устаревшего `long_press` хвоста после release.
- Список файлов:
  - `integration/integrations/input_processing_integration.py`
  - `Docs/assistant_exchange/codex/2026-02-17__task-brief__first-press-preempt-longpress-race-fix.md`
- Причина/цель изменений:
  - Исправить сценарий «зажимаю, но ничего не происходит» на первом запуске/хвосте playback.
- Проверка:
  - Синтаксис проверен (`py_compile`), логический сценарий race закрыт guard-ами.
