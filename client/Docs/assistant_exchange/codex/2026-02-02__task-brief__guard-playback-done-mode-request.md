# Task Brief: guard playback.completed -> mode.request

Context
- Issue: mic opens on long-press, then immediately deactivates while key is still held.
- Likely trigger: playback.completed from previous session drives mode.request(SLEEPING).

Changes
- Guarded ModeManagementIntegration playback bridge to only request SLEEPING when current_mode=PROCESSING and session_id matches.
- Added session_id to mode.request for traceability.

Files
- integration/integrations/mode_management_integration.py

Tests
- Not run (not requested).

Risks
- Low: bridge still active but now session- and mode-scoped.
