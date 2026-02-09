# Analysis: Intermittent missing signal cue

## Symptom
Иногда UX-сигнал слышен нестабильно/обрывается после переходов режимов.

## Root cause
`InputProcessingIntegration` помечал `playback_active=True` на любое `playback.started`, включая `signal=true` (короткие UX beeps).
Это вызывало ложный `PRESS_PREEMPT should=True` и лишний interrupt/cancel на следующем нажатии, что могло резать cue.

## Fix
Файл: `integration/integrations/input_processing_integration.py`
- В `_on_playback_started` добавлен guard: если `event.data.signal == True`, не выставлять `_playback_active`.

## Verification
- `python3 -m py_compile integration/integrations/input_processing_integration.py` — OK.

## Expected result
- `playback_active` отражает только реальное assistant audio, не UX cues.
- Меньше ложных preempt/cancel, сигнал воспроизводится стабильнее.
