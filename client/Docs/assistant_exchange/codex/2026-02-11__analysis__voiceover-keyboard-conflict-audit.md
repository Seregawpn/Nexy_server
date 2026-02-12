# Analysis: VoiceOver / keyboard conflict audit

## Scope
- Input monitor paths (`quartz` + `pynput`) and VoiceOver control path.
- Risk focus: shortcut suppression, VoiceOver combo interference, duplicate owners.

## Findings
1. Quartz path is observe-only and does not suppress system shortcuts.
   - `modules/input_processing/keyboard/mac/quartz_monitor.py:145-147` uses `kCGEventTapOptionListenOnly`.
   - Combo handler returns event in all normal paths (`.../quartz_monitor.py:357-359`, `:393-404`).

2. VoiceOver keyboard-triggered ducking is subscribed globally but disabled by config.
   - Subscription exists: `integration/integrations/voiceover_ducking_integration.py:58`.
   - Runtime gate: `.../voiceover_ducking_integration.py:125`.
   - Default config keeps it off: `config/unified_config.yaml:20`.

3. High-risk toggles exist in VoiceOver controller (currently disabled by defaults).
   - Hard toggle via Command+F5: `modules/voiceover_control/core/controller.py:275-278`, `:293-301`.
   - Synthetic Control key fallback: `.../controller.py:314-340`, `:534-540`.
   - VoiceOver speech shortcut (Ctrl+Opt+Shift+1): `.../controller.py:491-493`.

4. Fallback `pynput` backend has weaker VoiceOver guard semantics than Quartz.
   - Listener is non-suppressing (`modules/input_processing/keyboard/keyboard_monitor.py:183-186`).
   - But single-key path emits PRESS on Control edge without explicit VoiceOver chord block (`.../keyboard_monitor.py:334-361`).
   - Quartz has explicit blocking for non-PTT modifiers (`.../quartz_monitor.py:318-320`, `:420-423`).

5. Test coverage validates only a subset of VoiceOver passthrough contract.
   - Current tests assert modifier classification only (`tests/test_quartz_voiceover_passthrough.py:29-44`).
   - No integration-level regression test for real event lifecycle under VoiceOver chords.

## Architectural conclusion
- Source of Truth for keyboard lifecycle remains centralized in `InputProcessingIntegration`.
- Main conflict vector is not duplicated ownership, but feature-toggle combinations in VoiceOver controller + fallback backend behavior differences.
