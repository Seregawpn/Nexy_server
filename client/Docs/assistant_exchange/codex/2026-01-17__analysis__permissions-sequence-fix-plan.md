# Permissions Sequence Fix Plan (Analysis)

## Context
- User reports overlapping permission prompts (microphone + input), missing Accessibility prompt, and no entry added for Full Disk Access/Contacts.
- Reviewed first-run permissions flow and activators.

## Key Findings
- First-run sequence uses fixed order and fixed hold durations; `pause_between_requests_sec` is unused.
- Accessibility activator still calls `CGRequestPostEventAccess`, which conflicts with settings-only requirement.
- Full Disk Access/Contacts settings open, but app cannot be auto-added; needs explicit access attempt + settings guidance.

## Proposed Primary Fix
- Centralize order from `config/unified_config.yaml` (`integrations.permissions.required_permissions`) to remove duplication.
- Add per-permission wait loop (status change or timeout) + apply `pause_between_requests_sec` to prevent overlapping prompts.
- Switch Accessibility to settings-only flow (open settings if not granted; remove CGRequestPostEventAccess prompt path).

## Touchpoints
- `integration/integrations/first_run_permissions_integration.py`
- `modules/permissions/first_run/activator.py`
- `config/unified_config.yaml`

## Risks
- Minimal: behavior changes only in first-run flow; ensure not to introduce extra prompts.
