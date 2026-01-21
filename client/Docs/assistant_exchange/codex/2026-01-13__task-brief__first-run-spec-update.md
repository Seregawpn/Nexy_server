# Task Brief: update first-run flow spec

## Goal
Align first-run permissions spec with agreed logic: dialog-only requests, fixed order (Accessibility first, Input Monitoring last), max 13s wait with early continue, restart via PermissionRestartIntegration, and fallback to Settings only when system dialog is impossible.

## Changes
- Updated `_Docs_ARCHIVED/first_run_flow_spec.md` to reflect:
  - dialog-only requirement
  - fixed permission order
  - per-permission max wait with early continuation
  - restart criteria and post-restart re-request behavior
  - Settings fallback only when prompt is impossible

## Files
- `_Docs_ARCHIVED/first_run_flow_spec.md`

## Notes
- No code changes performed; doc update only.
