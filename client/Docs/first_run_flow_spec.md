# First-Run Flow Specification (macOS Client)

## Overview
The "first run" experience prepares the Nexy client for normal operation by:
- requesting all required macOS privacy permissions sequentially (no pre-checks);
- enforcing a permission order defined by `integrations.permissions_v2.order` (config-driven);
- activating each permission with a fixed grace window (`integrations.permissions_v2.steps.*.grace_s`) and post-trigger verification;
- using dialog-only activators for promptable permissions; Full Disk Access uses Settings-only;
- persisting flags as a cache (not a hard stop) for completed permission attempts;
- restarting the app after newly granted critical permissions so subsystems observe the new state.

The flow is coordinated by `FirstRunPermissionsIntegration` and `PermissionRestartIntegration`, with the `SimpleModuleCoordinator` orchestrating state.

Runtime ownership note (current):
- When `integrations.permissions_v2.enabled=true`, restart lifecycle owner is V2 orchestrator/ledger.
- Legacy `permissions.first_run_restart_pending` event remains compatibility-only and is not used as coordinator owner path in V2 mode.

---

## Permission Activation APIs (Updated 2026-01-13)

| Permission | API | Notes |
|------------|-----|-------|
| **Microphone** | `sounddevice.InputStream` | Opens mic → triggers system dialog |
| **Accessibility** | `CGRequestPostEventAccess()` | Triggers system dialog |
| **Input Monitoring** | `IOHIDRequestAccess(kIOHIDRequestTypeListenEvent)` | IOKit API, triggers system dialog |
| **Screen Capture** | `CGRequestScreenCaptureAccess()` via `ScreenCapturePermissionManager` | CoreGraphics API |
| **Contacts** | `CNContactStore.requestAccessForEntityType` | Contacts dialog |
| **Full Disk Access** | System Settings (open URL) | Settings-only |

### ⚠️ Known Issues (Fixed)

**Accessibility Prompt (2026-01-18)**
- **Decision:** Keep dialog-based Accessibility activation as-is; no Settings fallback.

**Duplicate App Instances (Fixed 2026-01-13)**  
- **Problem:** Python subprocess inside .app bundle caused TAL (Terminate After Launch)
- **Solution:** Removed subprocess, use direct API calls

---

## Diagram

```mermaid
flowchart TD
    A[App start] --> B[Ledger indicates all required granted?]
    B -- Yes --> C[Skip first-run flow]
    B -- No --> D[Publish permissions.first_run_started]
    D --> E[Iterate permissions_v2.order]
    E --> F[Activate permission + hold_duration]
    F --> G[Optional Settings-only for Full Disk Access]
    G --> H[Pause between requests]
    H --> E
    E --> I[Emit restart_scheduled if needed]
    I --> J[V2 restart handler triggers restart]
```

Notes:
- No status pre-checks are performed during first-run.
- For `AUTO_DIALOG` steps V2 orchestrator uses polling (`poll_s`) until terminal outcome/timeout.
- For `OPEN_SETTINGS` steps verification also uses polling with long-wait mode.
- Restart is blocked during first-run until `restart_pending` is set.

---

## Sequence

1. **Launch**  
   - `SimpleModuleCoordinator.initialize()` attaches a background loop and initialises integrations.  
   - `FirstRunPermissionsIntegration.start()` runs early, before voice-recognition/audio chains.

2. **Eligibility Check**  
   - The "first run" flag is treated as a cache only; the V2 ledger drives whether the flow runs.

3. **Permission Requests (Order + Dialog-Only)**  
   - Order source: `config/unified_config.yaml` → `integrations.permissions_v2.order`.
   - Если список отсутствует/пустой — first-run flow прерывается (нет fallback-списка).
   - For each permission in order, the integration:
     1. Calls the activation helper to trigger the **system dialog** (dialog-only).  
     2. Holds for `steps.*.grace_s`.  
     3. Performs post-trigger verification (polling for `AUTO_DIALOG`/`OPEN_SETTINGS`).  
     4. Proceeds to the next permission.
   - **Full Disk Access**: opens System Settings only (no dialog available).
   - The integration requests **all** permissions in the list (no pre-checks).

4. **Flow Completion**  
   - After all permissions are processed, the integration:
     - writes `permissions_first_run_completed.flag` after the sequential loop;  
     - sets `permissions_restart_pending` in `ApplicationStateManager`;  
     - for V2 owner path: advances ledger restart phase and delegates restart execution to `PermissionRestartIntegration`;
     - `permissions.first_run_restart_pending` remains legacy compatibility signal.

5. **Restart Initiation**  
   - V2 orchestrator triggers restart via `PermissionsRestartHandler`.  
   - Handler strategy:  
     1. If running from a PyInstaller bundle (`sys.frozen`), call `open -n -a /Applications/Nexy.app`.  
     2. Otherwise run dev fallback (python command).  
     3. Persist `restart_completed.flag` in the user data directory when the new instance comes up.
   - Runtime guards:
      - scheduled restart is cancelled on `app.shutdown`;
      - right before `trigger_restart()`, `USER_QUIT_INTENT` is re-checked, and restart is aborted if user quit is active.

6. **Post-Restart Launch**  
   - On the next start, the integration clears `restart_completed.flag` and emits `permissions.first_run_completed`.

---

## Canonical Files

| File | Purpose |
|------|---------|
| `integration/integrations/first_run_permissions_integration.py` | Orchestrates permission flow |
| `modules/permissions/v2/orchestrator.py` | Runs sequential pipeline |
| `modules/permissions/v2/probers/*` | Post-trigger probes |
| `config/unified_config.yaml` | Defines `permissions_v2.order` list |

---

## Flags & Persistence

| Flag / File | Location | When Created | Purpose |
|-------------|----------|--------------|---------|
| `permissions_first_run_completed.flag` | `~/Library/Application Support/Nexy/` | After successful permission loop | Marks that first-run permissions were attempted. |
| `restart_completed.flag` | same directory | When the post-first-run instance starts | Confirms that the restart took place. |

---

## Testing Commands

Reset permissions for clean test:
```bash
tccutil reset Accessibility com.nexy.assistant
tccutil reset ScreenCapture com.nexy.assistant
tccutil reset Microphone com.nexy.assistant
tccutil reset ListenEvent com.nexy.assistant
```

---

## Status Summary

- **Permissions requested?** Yes—sequential activation on first-run (no status checks).  
- **Dialogs only?** Yes—system dialogs for promptable permissions; Full Disk Access uses Settings-only.  
- **Flags persisted?** Yes—`permissions_first_run_completed.flag` and `restart_completed.flag` (cache only).  
- **Restart ensured?** Yes—new PID verification prevents premature exit.  
- **Architecture preserved?** Yes—integrations communicate via EventBus/state manager without bypassing existing modules.
