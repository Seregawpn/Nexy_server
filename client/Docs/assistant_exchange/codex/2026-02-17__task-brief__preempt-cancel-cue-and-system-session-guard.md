# Task Brief: preempt cancel-cue and system session guard

## Context
После фикса mode-sleep guard оставались остаточные гонки:
1) preempt interrupt запускал cancel cue и mode-фликерные side-effects;
2) в state попадал `session_id='system'`, что давало `Session ID validation failed` и нестабильные ветвления guard-логики.

## Diagnosis
Root cause: interrupt-path не передавал source-aware политику suppress для cancel cue, а playback-path безусловно синхронизировал `session_id` в state даже для не-UUID системных TTS сессий.

## Architecture Fit
- Owner mode-chain: `ModeManagementIntegration -> ModeController -> ApplicationStateManager` (сохранен).
- Owner interrupt side-effects: `InterruptManagementIntegration` (расширен source-aware контрактом).
- Owner cue-policy: `SignalIntegration` (добавлен фильтр preempt cancel cue).

## Changes
1. `integration/integrations/interrupt_management_integration.py`
- В `grpc.request_cancel` добавлены поля:
  - `interrupt_source`
  - `suppress_cancel_cue` (True для `keyboard.press_preempt` и `keyboard.long_press`).

2. `integration/integrations/speech_playback_integration.py`
- В `_on_audio_chunk` state sync session_id выполняется только для валидных UUID.
- Невалидные sid (например `system`) не записываются в `state_manager`.
- В `playback.cancelled` payload проброшены `interrupt_source` и `suppress_cancel_cue` из `grpc.request_cancel`.

3. `integration/integrations/signal_integration.py`
- В `_on_playback_cancelled` cancel cue подавляется для preempt-path:
  - если `suppress_cancel_cue=True`
  - или `interrupt_source in {keyboard.press_preempt, keyboard.long_press}`.

4. Тесты
- `tests/test_interrupt_management_preempt_mode_skip.py`
  - добавлен тест прокидывания `suppress_cancel_cue` и `interrupt_source`.
- `tests/test_signal_integration_cancel_done_suppression.py`
  - добавлен тест подавления CANCEL cue для preempt-path.
- `tests/test_voice_audio_owner_guards.py`
  - добавлен тест, что sid=`system` не пишется в state через audio chunk.

## Verification
- Команда:
  - `PYTHONPATH=. pytest -q tests/test_interrupt_management_preempt_mode_skip.py tests/test_signal_integration_cancel_done_suppression.py tests/test_voice_audio_owner_guards.py`
- Результат: `15 passed`.

## Информация об изменениях
- Что изменено:
  - Устранен конфликт preempt interrupt vs cancel cue (source-aware suppress).
  - Исключено загрязнение session SoT значением `system`.
  - Стабилизирован interrupt/playback/signal контракт без добавления новых owner-путей mode.
- Список файлов:
  - `integration/integrations/interrupt_management_integration.py`
  - `integration/integrations/speech_playback_integration.py`
  - `integration/integrations/signal_integration.py`
  - `tests/test_interrupt_management_preempt_mode_skip.py`
  - `tests/test_signal_integration_cancel_done_suppression.py`
  - `tests/test_voice_audio_owner_guards.py`
  - `Docs/assistant_exchange/codex/2026-02-17__task-brief__preempt-cancel-cue-and-system-session-guard.md`
- Причина/цель изменений:
  - Убрать остаточные race/dup side-effects в preempt-сценариях и восстановить единый контракт session_id (UUID|None).
- Проверка:
  - Точечный pytest прогон по измененным контрактам.
