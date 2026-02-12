# Screenshot Capture Audit (Race/Centralization/Delay)

Date: 2026-02-11
Type: analysis

## Scope
- Runtime path of screenshot creation in client processing flow.
- Checks: delay sources, race/conflict scenarios, centralization, duplication, dead code.

## Pre-Change Gate Evidence
- Read: `AGENTS.md`
- Read: `Docs/DOCS_INDEX.md`
- Read: `Docs/PRE_CHANGE_CHECKLIST.md`
- Read: `Docs/PROJECT_REQUIREMENTS.md`
- Read: `Docs/ARCHITECTURE_OVERVIEW.md`
- Read: `Docs/FLOW_INTERACTION_SPEC.md`
- Read: `Docs/STATE_CATALOG.md`
- Read: `Docs/FEATURE_FLAGS.md`
- Note: `Docs/ASSISTANT_COORDINATION_PROTOCOL.md`, `Docs/CODEX_PROMPT.md`, `Docs/ANTIGRAVITY_PROMPT.md`, `Docs/assistant_exchange/TEMPLATE.md` are not present in this workspace path.

## Source of Truth (current)
- Owner path for screenshot capture orchestration:
  - `integration/integrations/screenshot_capture_integration.py`
- Module for actual capture:
  - `modules/screenshot_capture/core/screenshot_capture.py`
  - `modules/screenshot_capture/macos/*`
- Event contract:
  - `Docs/FLOW_INTERACTION_SPEC.md` (`screenshot.captured`, `screenshot.error`)

## Findings

1. Race: session binding uses mutable local cache instead of event session
- `ScreenshotCaptureIntegration._on_mode_changed` uses `self._last_session_id` instead of `event.data.session_id`.
- File: `integration/integrations/screenshot_capture_integration.py` lines ~289-329.
- Risk: out-of-order `voice.recording_*` events can overwrite `_last_session_id`, causing screenshot publish under wrong session.

2. Duplication: second CLI screenshot implementation in integration layer
- `_fallback_capture_cli` duplicates behavior already implemented in `SimpleCoreGraphicsBridge._capture_via_screencapture`.
- Files:
  - `integration/integrations/screenshot_capture_integration.py` lines ~433-527
  - `modules/screenshot_capture/macos/simple_bridge.py` lines ~135+.
- Risk: two capture paths drift in format/metadata/error handling.

3. Delay risk: no enforced async timeout around executor capture
- `ScreenshotCapture.capture_screenshot()` catches `asyncio.TimeoutError` but does not wrap executor call with `asyncio.wait_for`.
- File: `modules/screenshot_capture/core/screenshot_capture.py` lines ~60-98.
- Risk: if bridge call stalls, coroutine may wait indefinitely.

4. Contract mismatch in consumer
- Processing workflow reads `path`, while producer contract uses `image_path`.
- File: `integration/workflows/processing_workflow.py` line ~318.
- Effect: logs path as `None`; weak observability and debugging.

5. Dead/legacy path and disabled permission branch
- `_on_state_changed` exists but is never subscribed.
- `_enforce_permissions` is hardcoded `False`; related methods are effectively dead in runtime.
- File: `integration/integrations/screenshot_capture_integration.py` lines ~332+, ~667+.

6. Minor latency tax
- Fixed `await asyncio.sleep(0.05)` before capture in `_capture_once`.
- File: `integration/integrations/screenshot_capture_integration.py` line ~410.
- Effect: adds deterministic 50ms per capture.

7. Dead config axis
- `workflow_config.screenshot_timeout` and `continue_without_screenshot` exist but are not used by `ProcessingWorkflow`.
- Files:
  - `integration/workflows/workflow_config.py`
  - `integration/workflows/processing_workflow.py`

## Primary Fix Direction
- Centralize session ownership to `event.data.session_id` in `app.mode_changed`.
- Remove integration-local CLI fallback and route all capture through module bridge.
- Add explicit `wait_for(..., timeout=config.timeout)` around executor capture.
- Remove/substitute dead legacy handlers and inactive permission branch from screenshot integration.
- Align consumer key usage to `image_path` and keep contract single.

## Risk Snapshot
- Duplication risk: medium-high
- Race risk: medium
- Delay risk: medium
- Centralization status: partial (owner exists, but has bypass/legacy branches)

