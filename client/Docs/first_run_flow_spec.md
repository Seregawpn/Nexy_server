# First-Run Flow Specification (macOS Client)

## Overview
The “first run” experience prepares the Nexy client for normal operation by:
- requesting all macOS privacy permissions the app relies on;
- persisting flags so the flow executes exactly once unless explicitly reset;
- restarting the app after permissions are granted so every subsystem observes the new state.

The flow is coordinated by `FirstRunPermissionsIntegration` and `PermissionRestartIntegration`, with the `SimpleModuleCoordinator` orchestrating state.

---

## Sequence

1. **Launch**  
   - `SimpleModuleCoordinator.initialize()` attaches a background loop and initialises integrations.  
   - `FirstRunPermissionsIntegration.start()` runs early, before voice-recognition/audio chains.

2. **Eligibility Check**  
   - The integration inspects the “first run” flag in the user data directory (`~/Library/Application Support/Nexy/permissions_first_run_completed.flag`).  
   - If the flag exists, the flow is skipped; otherwise it proceeds.

3. **Permission Requests**  
   - For each permission (microphone, accessibility, input monitoring, screen capture) the integration:
     1. Publishes a `permissions.status_checked` event with status treated as `not_determined`.  
     2. Calls the activation helper (`activate_microphone`, etc.) to trigger the system dialog.  
     3. **Immediately after activation**, re-checks the TCC status. If not GRANTED, opens System Settings and waits via polling (infinite loop checking every 1 second).  
     4. Publishes `permissions.status_checked` after status changes; if it changed, emits `permissions.changed`.
   - **Important**: The integration waits for GRANTED status **without timeout** (infinite polling loop). The `wait_for_grant` and `grant_wait_timeout_sec` config fields are deprecated and not used.
   - macOS decides whether to show a prompt; the integration does not skip any permission even if a decision already exists.

4. **Flow Completion**  
   - After all permissions are processed, the integration:
     - sets `_permissions_in_progress = False`;  
     - writes `permissions_first_run_completed.flag`;  
     - sets `permissions_restart_pending` in `ApplicationStateManager` (legacy consumers still read the state);  
     - publishes `permissions.first_run_restart_pending` (eventBus) so downstream consumers know a restart is imminent.

5. **Restart Initiation**  
   - `SimpleModuleCoordinator` catches the restart-pending signal and invokes `PermissionRestartIntegration`.  
   - `PermissionRestartIntegration` schedules a restart via `PermissionsRestartHandler.trigger_restart()`.  
   - Handler strategy:  
     1. If running from a PyInstaller bundle (`sys.frozen`), call `os.execv` to replace the current process.  
     2. Otherwise run `open -n -a /Applications/Nexy.app`.  
     3. Wait for a **new PID** different from the current process before exiting; `allow_dev_fallback` is `False` in production, so it never drops to the dev restart path.  
     4. Persist `restart_completed.flag` in the user data directory when the new instance comes up.

6. **Post-Restart Launch**  
   - On the next start, the integration sees both `permissions_first_run_completed.flag` and `restart_completed.flag`, clears the restart flag, and emits `permissions.first_run_completed`.  
   - No further permission requests are performed until the flags are removed/reset manually (e.g., for testing).

---

## Flags & Persistence

| Flag / File | Location | When Created | Purpose |
|-------------|----------|--------------|---------|
| `permissions_first_run_completed.flag` | `~/Library/Application Support/Nexy/` | After successful permission loop | Marks that first-run permissions were attempted. |
| `restart_completed.flag` | same directory | When the post-first-run instance starts | Confirms that the restart took place. |
| (optional) `permission_request_attempted.flag` | same directory | On first attempt (even if user denied) | Prevents re-running flow after a manual reset — recommended for UX. |

*Note:* In addition to files, `ApplicationStateManager` maintains transient keys (`permissions_restart_pending`) for integrations that still rely on state data.

---

## EventBus Contracts

- `permissions.first_run_started`: emitted with a session ID at the start of the flow.  
- `permissions.status_checked`: emitted before and after each permission activation.  
- `permissions.changed`: emitted when TCC reports a new status.  
- `permissions.first_run_restart_pending`: tells the coordinator to schedule a restart.  
- `permissions.first_run_completed`: emitted by the next instance after the restart is detected.

All events include `session_id` and a `source` field for traceability.

---

## Integration Touchpoints

1. **FirstRunPermissionsIntegration**  
   - Controls activation sequence and flag handling.  
   - Uses `modules.permissions.first_run.*` helpers for macOS API access.

2. **PermissionRestartIntegration**  
   - Listens for permission events, coordinates with `RestartScheduler`.  
   - Ensures restarts are safe: checks for active sessions, updates in progress, etc.

3. **SimpleModuleCoordinator**  
   - Attaches the EventBus loop, subscribes to critical events early, kicks off restart workflow.  
   - Ensures no other integration starts consuming resources (e.g., voice) until permissions are settled.

---

## Additional Notes & Recommendations

- Always log activation attempts and the result status (`DEBUG` level is useful during QA).  
- Consider adding a timeout guard (`asyncio.wait_for`) around activation coroutines to avoid hangs if a system API stalls.  
- Keep the ability to override behaviour in dev via environment variables (e.g., `NEXY_DEV_FORCE_PERMISSIONS`), but default them off in production.  
- Document that testers can reset permissions by removing flags and running `tccutil reset` commands, otherwise the flow is skipped intentionally.

---

## Status Summary

- **Permissions requested?** Yes—always triggered regardless of existing TCC records.  
- **macOS decides dialogs?** Yes—activation APIs defer to TCC.  
- **Flags persisted?** Yes—`permissions_first_run_completed.flag` and `restart_completed.flag`.  
- **Restart ensured?** Yes—new PID verification prevents premature exit.  
- **Architecture preserved?** Yes—integrations communicate via EventBus/state manager without bypassing existing modules.

