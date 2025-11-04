# First-Run Permission Flow Requirements

## Goals
- Ensure the Nexy macOS client always requests every critical permission on the very first launch.
- Let macOS decide whether to show a prompt, without skipping any permission because of cached TCC status.
- Apply all granted permissions by restarting the app exactly once after the initial flow.

## Permissions to Handle
1. Microphone (`kTCCServiceMicrophone`)
2. Accessibility (`AXIsProcessTrustedWithOptions`)
3. Input Monitoring (`IOHIDRequestAccess`)
4. Screen Recording (`CGRequestScreenCaptureAccess`)

## Behaviour on First Launch
- Treat every permission as `not_determined` before activation:
  - Do **not** rely on existing TCC entries.
  - Always invoke the corresponding activation API and hold the resource for `activation_hold_duration_sec` (current default: 13 seconds).
- Allow macOS to decide whether a dialog appears; non-interactive responses (already granted/denied) are acceptable.
- After the hold period, re-check the actual TCC status and publish it through the EventBus (`permissions.status_checked`, `permissions.changed` when applicable).

## Restart Requirements
- After processing all permissions, initiate a restart identical to the update flow:
  - Try `execv` on the current PyInstaller bundle (`sys.frozen` case).
  - Otherwise run `open -n -a /Applications/Nexy.app`.
  - Verify that a **new process ID** is created before exiting the current instance.
  - Production builds must not fall back to the development restart path.

## Flags & State
- Record that the permission flow has been attempted to avoid repeating it on future launches.
- Use the standard restart-pending flags to inform the coordinator and keep state transitions centralised.

## Logging & Diagnostics
- Log each activation attempt and the post-check status.
- Surface restart actions (`[PERMISSION_RESTART] …`) so it is clear when the app expects a relaunch.

## Non-Goals
- Do not attempt to forcibly reset TCC.
- Do not bypass macOS permissions UI or cache responses.

