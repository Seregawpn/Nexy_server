# Accessibility prompt root cause (analysis)

## Context
User reports Accessibility permission prompt does not appear in packaged app; other prompts do.

## Findings
- Logs show `TCCAccessRequest for kTCCServiceAccessibility` without entitlement, which indicates a non-recommended path was hit.
- Current activator path avoids `AXIsProcessTrustedWithOptions` and relies on AppleScript + System Settings deep link, which does not reliably trigger a system prompt.
- Subprocess helper `modules/permissions/first_run/trigger_accessibility_prompt.py` exists but is not used in the activator.

## Root cause
The prompt call is not executed via the supported public API in the current activation flow; therefore the OS never shows the Accessibility dialog.

## Proposed fix (summary)
Call `trigger_accessibility_prompt.py` from the activator via subprocess to request the prompt in an isolated process, then keep polling status via the centralized status checker.

## Sources
- log.md (tccd errors around TCCAccessRequest)
- modules/permissions/first_run/activator.py
- modules/permissions/first_run/status_checker.py
- modules/permissions/first_run/trigger_accessibility_prompt.py
- _Docs_ARCHIVED/ARCHITECTURE_OVERVIEW.md
- _Docs_ARCHIVED/PROJECT_REQUIREMENTS.md
