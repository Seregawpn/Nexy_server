# Analysis: Repeated Accessibility permission prompts

## Symptoms
- After granting Accessibility in System Settings, the app still reports it as not granted and shows the help dialog again.
- Repeated prompts after restart or after the first-run loop continues.

## Root cause
- `modules/permissions/first_run/status_checker.py::check_accessibility_status()` returns `NOT_DETERMINED` unconditionally (safe mode), so the system never recognizes the grant.
- The first-run flow trusts this checker, so it keeps treating Accessibility as missing even after user approval.

## Proposed fix direction
- Introduce a safe real check for Accessibility using the existing `modules/permissions/macos/accessibility_handler.py` (AXIsProcessTrustedWithOptions) with guardrails:
  - Run the check in a subprocess to avoid potential crash after reset.
  - Only use the real check after the user opens Settings or after a restart.
  - If true, mark GRANTED and stop showing the dialog.

## Expected impact
- Eliminates repeated Accessibility prompts.
- Preserves safety by isolating the AX check.
