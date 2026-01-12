# Accessibility prompt missing (analysis)

## Context
- User report: Accessibility prompt does not appear in packaged app; other permissions do.
- Logs show TCCAccessRequest warning for Accessibility without private entitlement.

## Sources
- log.md:467, 479, 1203, 1209
- modules/permissions/first_run/activator.py
- modules/permissions/first_run/status_checker.py
- modules/permissions/first_run/trigger_accessibility_prompt.py
- _Docs_ARCHIVED/ARCHITECTURE_OVERVIEW.md (Docs/ARCHITECTURE_OVERVIEW.md missing)
- _Docs_ARCHIVED/PROJECT_REQUIREMENTS.md (Docs/PROJECT_REQUIREMENTS.md missing)

## Findings
- Accessibility prompt is not triggered because current activator avoids AXIsProcessTrustedWithOptions (prompt API) and only uses AppleScript + Settings deep link.
- AppleScript path does not guarantee a system prompt on current macOS; it often just fails silently.
- The repo already contains a safe subprocess helper to trigger AXIsProcessTrustedWithOptions, but it is not wired into the activator.

## Proposed fix (summary)
- Use modules/permissions/first_run/trigger_accessibility_prompt.py from activator via subprocess to request prompt in an isolated process.
- Keep status_checker as source of truth for polling; remove AppleScript-only activation path as primary.

## Risks
- On Sequoia, AXIsProcessTrustedWithOptions may crash the subprocess; isolation mitigates app crash.

## Notes
- Required docs missing in Docs/: PROJECT_REQUIREMENTS.md, ARCHITECTURE_OVERVIEW.md, ASSISTANT_COORDINATION_PROTOCOL.md, ANTIGRAVITY_PROMPT.md, CODEX_PROMPT.md, assistant_exchange/TEMPLATE.md. Used archived versions where available.
