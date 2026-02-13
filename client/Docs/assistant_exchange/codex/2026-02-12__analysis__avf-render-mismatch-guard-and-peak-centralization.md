# AVF Render Mismatch Guard + Peak Centralization

## Context
User observed intermittent "audio arrives but not audible" with logs showing healthy pipeline (`engine=True`, `player=True`, queued/scheduled chunks).

## Diagnosis
`Scheduled chunk peak` diagnostic was derived from a tiny middle window of PCM buffer, producing misleading low values and masking true write/render issues.

## Changes
- File: `modules/speech_playback/core/avf_player.py`
1. Added centralized write-integrity streak counter in AVF owner:
   - `self._write_mismatch_streak = 0`
2. Added source-vs-written peak check immediately after buffer write:
   - compute `write_peak` from destination buffer (`dst`)
   - detect mismatch when `src_peak > 0.02 && write_peak < src_peak * 0.15`
   - increment/reset streak accordingly
3. Added self-heal trigger on repeated mismatch:
   - if streak >= 3 -> `self._maybe_recreate_for_render_stall(reason="write_peak_mismatch")`
4. Replaced misleading scheduled peak metric:
   - removed middle-window `peak`
   - logging now shows `src_peak` and `written_peak` directly.

## Architecture Fit
- Owner unchanged: AVFoundationPlayer remains single source of truth for render-path health.
- No duplication in integration/workflow/mode layers.
- No additional cross-layer state introduced.

## Verification
- `python3 -m py_compile modules/speech_playback/core/avf_player.py` passed.
- New diagnostics expected:
  - `Scheduled chunk ... src_peak=... written_peak=...`
  - on issue: `Buffer write mismatch ... streak=...`
  - on repeated issue: `write_peak_mismatch` self-heal recreate.
