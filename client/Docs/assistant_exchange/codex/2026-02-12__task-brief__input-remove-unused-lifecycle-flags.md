# Task Brief: remove unused input lifecycle flags

## Goal
Упростить `InputProcessingIntegration` и убрать write-only состояние без влияния на поведение.

## Removed
- `_session_recognized`
- `_recording_start_time`

## Changes
- `integration/integrations/input_processing_integration.py`
  - удалены поля из `__init__`;
  - удалены все reset/set присваивания;
  - `voice.recognition_completed` handler оставлен как no-op (совместимость подписки без доп. состояния).

## Architecture check
- Owner не изменен: `InputProcessingIntegration`.
- Source of Truth не размыт: используются только активные lifecycle-флаги.
- Новые ветки/флаги/пути управления не добавлены.

## Verification
- `PYTHONPATH=. pytest -q tests/test_microphone_activation.py` -> `6 passed`
- `PYTHONPATH=. pytest -q tests/test_interrupt_playback.py` -> `15 passed`

## Risk
- Duplication risk: low
- Race risk: low
- Breaks architecture: no
