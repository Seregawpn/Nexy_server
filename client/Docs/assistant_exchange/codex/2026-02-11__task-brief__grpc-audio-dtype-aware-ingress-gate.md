# Task Brief: dtype-aware ingress audio gate (gRPC stream)

Date: 2026-02-11
Owner: Codex

## Context
User reported: welcome audio is audible, while assistant response audio is often not audible.

## Diagnosis
`GrpcClientIntegration` evaluated stream chunk loudness/noise-floor as `int16` unconditionally, even when chunk `dtype` could be `float32`/`int16_be`. This could misclassify valid speech chunks as near-silent/noise-floor before publishing `grpc.response.audio`.

## Architecture Fit
- Where: `integration/integrations/grpc_client_integration.py`
- Source of Truth: gRPC stream format normalization/gating stays in `GrpcClientIntegration` (format owner)
- No new state axes/flags added

## Changes
- Replaced int16-only amplitude diagnostics/gating with dtype-aware decoding:
  - `float32|float|f32` → decode as `np.float32`, finite sanitize, compute peak/rms
  - `int16_be|pcm_s16be` → decode as big-endian int16
  - fallback → little-endian int16
- Normalized float32 peak/rms to int16 scale (`* 32767`) so existing thresholds remain valid.

## Verification
- `python3 -m py_compile integration/integrations/grpc_client_integration.py` passed.

## Risk
Low: localized change in ingress diagnostics/gating path, no protocol/interface changes.
