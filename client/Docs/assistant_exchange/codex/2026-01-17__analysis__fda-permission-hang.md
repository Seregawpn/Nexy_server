# FDA Permission Hang Analysis

## Context
User reports the app hangs when the first-run flow reaches Full Disk Access (FDA). Logs provided were system-level (LaunchServices/tccd) and do not include Nexy permission flow logs. Required project docs listed in AGENTS.md are missing in this workspace: `Docs/ASSISTANT_COORDINATION_PROTOCOL.md`, `Docs/ANTIGRAVITY_PROMPT.md`, `Docs/CODEX_PROMPT.md`, `Docs/assistant_exchange/TEMPLATE.md`.

## Likely Root Cause
`activate_full_disk_access()` shows an `NSAlert` sheet before `app.run()` (no AppKit run loop yet). Even though it is called on the main thread, AppKit UI without a running NSApplication loop can appear frozen or unresponsive. If the dialog cannot be shown, the function falls back to a blocking `sleep` (default 13s), which looks like a hang in the sequential permission flow.

## Architecture Fit
- Owner: `FirstRunPermissionsIntegration` orchestrates sequential permissions.
- UI activation: `modules/permissions/first_run/activator.py` (FDA dialog and settings opening).
- Source of truth: `config/unified_config.yaml` permission order + integration flow.

## Fix Direction (Primary)
- Keep FDA activation in `modules/permissions/first_run/activator.py`.
- Avoid blocking holds when the FDA dialog is shown or cannot be shown.
- Ensure FDA dialog is non-blocking and safe to call before `app.run()` (or defer to a UI-safe context via coordinator callback).

## Suggested Verification
- Run first-run flow with fresh TCC: check logs for FDA activation and confirm no long pause before the next permission prompt.
- Ensure `permissions.first_run_restart_pending` still fires and restart occurs.
