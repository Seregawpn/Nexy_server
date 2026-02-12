# Audio Device Management Audit

Date: 2026-02-11
Scope: client audio device management (input/output routing, playback cancel path, route monitoring, gateway ownership).

## Gate / Sources Used
- `AGENTS.md`
- `Docs/DOCS_INDEX.md`
- `Docs/PRE_CHANGE_CHECKLIST.md`
- `Docs/PROJECT_REQUIREMENTS.md`
- `Docs/ARCHITECTURE_OVERVIEW.md`
- `Docs/FLOW_INTERACTION_SPEC.md`
- `Docs/STATE_CATALOG.md`
- `Docs/FEATURE_FLAGS.md`
- `config/interaction_matrix.yaml`

Note: `Docs/ASSISTANT_COORDINATION_PROTOCOL.md`, `Docs/CODEX_PROMPT.md`, `Docs/ANTIGRAVITY_PROMPT.md`, `Docs/assistant_exchange/TEMPLATE.md` are absent in this workspace snapshot.

## Findings
1. Duplicate cancel handling in playback integration.
- `SpeechPlaybackIntegration` handles cancel in two parallel paths: `_on_grpc_cancel` and `_on_unified_interrupt`.
- Both stop player/queue and mutate cancel guards; dedup exists but complexity remains high.

2. Route-manager governance exists in config/gateway but has no runtime owner.
- `decide_route_manager_reconcile` + matrix rules are defined/tested.
- No integration/module invokes this gateway in runtime path.

3. Feature flag duplication/conflict risk for AVFoundation toggles.
- Env-style flags (`NEXY_FEATURE_*`, `NEXY_KS_*`) exist in registry.
- Config-style flags (`audio_system.avfoundation_*`, `ks_avfoundation_*`) exist in unified config.
- No single resolver path in runtime discovered.

4. Input device monitor duplication at module level.
- `AudioRouteMonitor` is active via `GoogleSRController`.
- `AudioDeviceMonitor` exists as separate implementation but currently unused.
- This is dormant duplication with drift risk.

5. Output route-change recreate has no cross-layer arbitration.
- AVF player recreates itself directly on route-change notification thread.
- This bypasses gateway policy (`first_run/update/device busy` conditions), so policy centralization is incomplete for output side.

## Recommended Primary Direction
- Keep `SpeechPlaybackIntegration` as single runtime owner for playback cancel and terminal playback events.
- Keep `GoogleSRController` as single runtime owner for input route monitoring.
- Wire one runtime orchestrator for route-manager reconcile through existing gateway (`decide_route_manager_reconcile`) and remove dead path/flags.
- Introduce one canonical AVFoundation flag resolver (config + env normalization) and retire alias duplicates.

## Risks
- Duplication risk: medium
- Race risk: medium
- Centralization gap: yes (route reconcile + feature resolver)

## Verification Targets
- One cancel path emits `playback.cancelled` once per session.
- Route reconcile gateway is invoked in runtime logs (or removed from matrix/docs).
- AVFoundation flags resolve through one owner with deterministic precedence.
- No unused monitor implementation remains without explicit archival.
