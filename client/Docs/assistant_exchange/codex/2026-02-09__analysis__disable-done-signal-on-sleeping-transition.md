# Disable DONE audio on sleeping transition

## Problem
Наблюдался рассинхрон UX:
- режим уже `SLEEPING`,
- но после `app.mode_changed -> sleeping` запускался `playback.signal(pattern=done)`,
- ассистент продолжал звучать в "sleeping".

## Root Cause
`SignalIntegration` эмитил `DONE`-аудио при переходе режима в `SLEEPING`.
Это создавало новый playback уже после terminal mode transition.

## Change
- Файл: `integration/integrations/signal_integration.py`
- В `_on_mode_changed()` отключен emission:
  - `SignalPattern.DONE` для ветки `mode == SLEEPING`.
- Оставлены без изменений: `LISTEN_START`, `ERROR`, `CANCEL`.

## Architecture Fit
- Mode owner остается `ModeManagement/Workflow`.
- Signal layer больше не создает post-sleeping audio side-effect.

## Verification
- `python3 -m py_compile integration/integrations/signal_integration.py` ✅
- `pytest -q tests/test_processing_workflow_session_guard.py` ✅
- `pytest -q tests/test_welcome_startup_sequence.py` ✅

## Expected Effect
- После `app.mode_changed -> sleeping` не должно быть нового `playback.started` с `pattern=done`.
- Режим и фактическое звучание становятся согласованными.
