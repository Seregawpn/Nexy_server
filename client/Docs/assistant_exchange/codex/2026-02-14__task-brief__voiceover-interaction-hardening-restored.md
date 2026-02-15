# VoiceOver Interaction Hardening Restored

## Context
После переустановки/изменений часть согласованных фиксов по VoiceOver оказалась отсутствующей в текущем коде:
- в `VoiceOverController` не было capability-latch для `stop speaking`;
- в `VoiceOverDuckingIntegration` не было single-flight/dedup на `app.mode_changed`.

## Goal
Вернуть согласованную устойчивую модель взаимодействия Nexy ↔ VoiceOver без конфликтов с hotkey-потоком и без race на mode events.

## Source of Truth
- Hotkey interception owner: `modules/input_processing/keyboard/mac/quartz_monitor.py`
- VoiceOver control owner: `modules/voiceover_control/core/controller.py`
- VoiceOver mode orchestration owner: `integration/integrations/voiceover_ducking_integration.py`

## Implemented Changes

### 1) VoiceOverController hardening
File: `modules/voiceover_control/core/controller.py`
- Added `_stop_speaking_supported` latch.
- `_stop_voiceover_speaking(...)` now:
  - bypasses AppleScript path if unsupported,
  - executes `stop speaking` with `quiet_errors=True`,
  - disables unsupported AppleScript path via `_handle_stop_speaking_unsupported(...)`,
  - falls back to control-key path.
- Added `_handle_stop_speaking_unsupported(...)` with one-way capability disable.
- `_apply_voiceover_silence_fallback(...)` now respects capability latch and avoids repeated unsupported path spam.

### 2) VoiceOverDuckingIntegration race guard
File: `integration/integrations/voiceover_ducking_integration.py`
- Added `asyncio.Lock` (`_mode_apply_lock`) for single-flight mode processing.
- Added `_last_applied_mode` dedup guard.
- `handle_mode_change(...)` now:
  - normalizes mode value,
  - drops duplicate mode events,
  - serializes `update_voiceover_status + apply_mode` for fast event-bus path.

### 3) Regression test coverage
File: `tests/test_voiceover_ducking_mode_guard.py`
- Added tests for:
  - duplicate concurrent mode events -> coalesced into single apply,
  - different concurrent modes -> serialized without overlap.

## Validation
- `python3 -m compileall -q modules/voiceover_control/core/controller.py integration/integrations/voiceover_ducking_integration.py tests/test_voiceover_ducking_mode_guard.py` -> passed
- `PYTHONPATH=. python3 -m unittest discover -s tests -p 'test_voiceover_ducking_mode_guard.py'` -> passed (2/2)
- `PYTHONPATH=. python3 -m unittest discover -s tests -p 'test_quartz_monitor_chord_logic.py'` -> passed (2/2)

## Risks / Notes
- New local state introduced in integration: `_last_applied_mode` (scoped, owner-defined).
- Architecture remains centralized; no new side path for hotkey interception introduced.
