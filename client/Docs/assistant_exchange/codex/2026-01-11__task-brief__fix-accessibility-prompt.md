# Fix Accessibility prompt (task brief)

## Goal
Trigger Accessibility prompt reliably in packaged app without crashing main process.

## Changes
- Use subprocess helper `trigger_accessibility_prompt.py` from `activate_accessibility()`.
- Keep centralized status check in `status_checker.py`.
- Fallback to System Settings only if prompt helper did not grant.

## Files
- modules/permissions/first_run/activator.py
- modules/permissions/first_run/trigger_accessibility_prompt.py
- modules/permissions/first_run/status_checker.py

## Rationale
AppleScript does not guarantee a prompt on current macOS; helper isolates AXIsProcessTrustedWithOptions call and can trigger prompt safely.

## Verification
- Reset Accessibility via tccutil, run packaged app, confirm system prompt appears.
- Logs show prompt helper exit code; no main-process crash.
