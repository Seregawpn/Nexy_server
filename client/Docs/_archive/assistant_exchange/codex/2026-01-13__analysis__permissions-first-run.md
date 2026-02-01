# Analysis: first-run permissions prompts

## Context
- User reports: Accessibility prompt not shown on first launch; Input Monitoring prompt shown even though UI cell not added; after manual granting all permissions app activated.
- Logs provided: `log.md` (system logs, no app-level permission logs).

---

## Current Implementation (Updated 2026-01-13)

### Permission Activation APIs

| Permission | API Used | File |
|------------|----------|------|
| **Microphone** | `sounddevice.InputStream` | `activator.py` |
| **Accessibility** | `CoreGraphics.CGRequestPostEventAccess()` | `activator.py` |
| **Input Monitoring** | `IOHIDRequestAccess(kIOHIDRequestTypeListenEvent)` | `activator.py` |
| **Screen Capture** | `ScreenCapturePermissionManager.request_permission()` | `activator.py` |

### Permission Flow

```
1. FirstRunPermissionsIntegration.start()
   ↓
2. Check all permissions status
   ↓
3. For each missing permission:
   - Call activation function (triggers system dialog)
   - Polling status every 1s for up to 13s
   - If GRANTED → next permission
   - If timeout → mark as failed, continue
   ↓
4. If all GRANTED → emit "permissions.first_run_completed"
```

---

## Known Issues & History

### FIXED: TCCAccessRequest Error for Accessibility (2026-01-13)

**Problem:**
- `AXIsProcessTrustedWithOptions` with `prompt=True` requires private entitlement `com.apple.private.tcc.manager.check-by-audit-token`
- On macOS Sequoia 15+, this causes TCC error and dialog is NOT shown

**Solution:**
- Replaced with `CGRequestPostEventAccess()` from Quartz CoreGraphics
- This is a public API that directly triggers TCC dialog

### FIXED: Duplicate App Instances (2026-01-13)

**Problem:**
- `trigger_accessibility_prompt.py` subprocess was causing TAL (Terminate After Launch)
- Python subprocess inside .app bundle → macOS interprets as app termination → auto-restart
- Result: 8+ copies of the application running

**Solution:**
- Removed subprocess approach
- `CGRequestPostEventAccess()` is a direct API call, no subprocess

---

## Canonical Files

| File | Purpose |
|------|---------|
| `modules/permissions/first_run/activator.py` | Triggers permission dialogs |
| `modules/permissions/first_run/status_checker.py` | Checks permission status (no prompt) |
| `integration/integrations/first_run_permissions_integration.py` | Orchestrates permission flow |
| `config/unified_config.yaml` | Defines `required_permissions` list |

---

## Testing Commands

Reset permissions for clean test:
```bash
tccutil reset Accessibility com.nexy.assistant
tccutil reset ScreenCapture com.nexy.assistant
tccutil reset Microphone com.nexy.assistant
tccutil reset ListenEvent com.nexy.assistant
```
