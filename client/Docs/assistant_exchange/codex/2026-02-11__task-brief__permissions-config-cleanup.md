# Task Brief: permissions_v2 config cleanup

## Goal
Remove distracting/non-essential timing settings and keep strict policy: 15s per permission step.

## Changes
- Kept:
  - `advance_on_timeout: true`
  - `default_step_timeout_s: 15.0`
  - `inter_step_pause_s: 0.0`
  - per-step `step_timeout_s: 15.0`
- Removed per-step noisy timing keys:
  - `grace_s`
  - `poll_s`
  - `waiting_long_after_s`
  - `waiting_long_poll_s`
  - `post_restart_verify_window_s`
  - `post_restart_verify_tick_s`

## File
- `config/unified_config.yaml`

## Result
- Config is simplified and aligned to strict 15s-per-step behavior.
