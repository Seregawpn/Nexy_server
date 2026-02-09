# Task Summary
- Goal: prevent silent PCM from being streamed to client during EdgeTTS streaming conversion.
- Result: added one-time prebuffer check to detect silent PCM before yielding any chunks.

# Changes
- server/server/modules/audio_generation/providers/edge_tts_provider.py
  - Added one-time prebuffer guard (`prebuffer_done`) to avoid re-buffering after stream starts.
  - Silent detection now happens only before any bytes are yielded.

# Verification Steps (Manual)
1. Trigger server TTS (welcome or limit TTS).
2. Confirm no "Silent PCM detected" errors after chunks are already emitted.
3. Confirm audio plays (client logs show non-silent chunks).

# Notes / Risks
- If silent PCM persists, the retry will happen before streaming; if all retries fail, request fails early and client should fallback.
- Required docs (Docs/CODEX_PROMPT.md, Docs/ANTIGRAVITY_PROMPT.md, Docs/assistant_exchange/TEMPLATE.md) were not found in repo.

# Follow-ups
- If silent persists, consider fallback to non-streaming conversion for limit/welcome only.
