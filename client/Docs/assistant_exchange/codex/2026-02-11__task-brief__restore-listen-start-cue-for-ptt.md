# Task Brief: restore LISTEN_START cue for PTT

## Issue
LISTEN_START cue was not played when entering LISTENING via PTT.

## Root cause
Config had `integrations.signals.suppress_listen_start_for_ptt: true`, and logs confirmed suppression.

## Change
- Updated `/Users/sergiyzasorin/Fix_new/client/config/unified_config.yaml`
  - `suppress_listen_start_for_ptt: false`

## Expected result
On PTT transition to LISTENING, `SignalIntegration` should emit `listen_start` cue again.
