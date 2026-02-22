# Task Brief: EdgeTTS initial silence should not fail fast

## Problem
`GenerateWelcomeAudio` and server TTS failed with `Silent PCM detected in initial window`, causing no server audio and fallback to local `say`.

## Root cause
EdgeTTS streaming converter treated initial low-amplitude/silent PCM window as a hard error and raised exception, forcing retries and eventual failure.

## Change
File changed:
- `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/server/server/modules/audio_generation/providers/edge_tts_provider.py`

Behavior update:
- Initial silent prebuffer window no longer raises exception.
- Provider now logs warning and continues stream (flushes prebuffered chunks).
- End-of-stream all-silent prebuffer also no longer hard-fails; stream is released.

## Why this fits architecture
- Kept single owner in EdgeTTS provider for stream validation policy.
- No new flags/state owners introduced.
- Avoided client-side workaround and preserved central server TTS contract.

## Verification
- Ran: `python3 -m py_compile .../edge_tts_provider.py`
- Result: OK

## Expected outcome
- Welcome/server TTS should stop failing on initial silent window.
- Fewer false retries and fewer fallback-to-local events.
