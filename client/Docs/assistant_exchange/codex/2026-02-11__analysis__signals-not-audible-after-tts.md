# Analysis: signals not audible after assistant TTS

Date: 2026-02-11
Owner: Codex

## Observed
- Signal event path is alive in logs: `app.mode_changed -> signal.emit -> sink.publish -> playback.signal -> avf.queue_push -> avf.render_start`.
- User still reports not hearing cues after assistant playback.

## Root Cause
Primary issue is audibility profile, not event delivery:
- `config/unified_config.yaml` contained low cue profile values (`done/error/cancel` short + quiet).
- `SignalIntegration` merged config values directly, so audible defaults were overridden by quiet config.

## Implemented
1. Strengthened default cue profile in `SignalIntegration`.
2. Added audibility floor when config overrides are present:
   - `duration_ms = max(default_duration, config_duration)`
   - `volume = max(default_volume, config_volume)` (clamped to 1.0)

This keeps one owner (`SignalIntegration`) and prevents silent/too subtle cues from config drift.

## Files
- `integration/integrations/signal_integration.py`
- `integration/integrations/grpc_client_integration.py` (dtype-aware stream gate fix from previous step)

## Validation
- `python3 -m py_compile integration/integrations/signal_integration.py`
- `python3 -m py_compile integration/integrations/grpc_client_integration.py`
