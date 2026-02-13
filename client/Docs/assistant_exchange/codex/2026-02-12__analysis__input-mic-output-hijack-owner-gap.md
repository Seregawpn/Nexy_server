# Analysis: Input/Mic -> Playback output hijack owner gap

## Context
User reports: audio chunks are received/scheduled with non-zero peaks, but assistant speech is sometimes inaudible after Input changes.

## Architecture finding
- `VoiceRecognitionIntegration` publishes `voice.mic_opened`/`voice.mic_closed` (owner of mic lifecycle signal).
- `SpeechPlaybackIntegration` subscribes to `voice.mic_closed`, but handler is `pass`.
- `AVFoundationPlayer` is owner of playback audio session/profile recovery.

## Root gap
There is no centralized post-mic recovery step in playback integration despite explicit event wiring.

## Why this can manifest as "audio present but not audible"
- Data plane is healthy (queue/schedule peaks non-zero).
- Session/route can still be transiently reconfigured by mic path (especially BT profile changes), while playback path does not run a deterministic resync on mic close event boundary.
- Current recovery is only opportunistic during chunk enqueue/start; no explicit lifecycle-bound recovery point.

## Primary fix direction
Implement `voice.mic_closed` handler in `SpeechPlaybackIntegration` as centralized resync trigger (single owner), using AVF runtime status + idempotent `start_playback()` reassert path, without adding new state owners.
