# Task Brief: disable tray focus fallback

## Context
User observed focus stealing during startup periods.

## Change
Updated focus config to disable startup forced-focus fallback:
- `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/config/unified_config.yaml`
  - `focus.allow_tray_startup_fallback: false`

## Why
Logs show tray becomes ready quickly (single-digit ms), so fallback force-activation path is not needed in normal flow and can be disabled to avoid focus grabs in edge startup scenarios.

## Architecture gates
- Single owner: focus policy remains centralized in `focus` config consumed by coordinator/main.
- Zero duplication: no new pathways.
- Anti-race: no new concurrent state.
- Flag lifecycle: existing flag reused (changed value only).
