# Analysis: ideal first-run permissions flow alignment

## Sources reviewed
- _Docs_ARCHIVED/PROJECT_REQUIREMENTS.md (REQ-010, REQ-011, REQ-014)
- _Docs_ARCHIVED/ARCHITECTURE_OVERVIEW.md (integration boundaries)
- _Docs_ARCHIVED/first_run_flow_spec.md (canonical flow)
- PERMISSIONS_REPORT.md (current expected permissions set)

## Current vs ideal gaps (high level)
- FirstRunPermissionsIntegration performs restart directly, bypassing PermissionRestartIntegration.
- Flags used differ from spec (permissions_granted.flag vs permissions_first_run_completed.flag + restart_completed.flag).
- Event contract incomplete (missing permissions.status_checked / permissions.changed / permissions.first_run_restart_pending).
- Timeout-based polling deviates from spec’s infinite polling (or explicit max_wait rules).
- Required permissions include input_monitoring despite report stating not required post v2.
- Sequential prompt cadence (13s delay) not enforced.

## Proposed alignment (direction only)
- Restore spec-led flow and event contracts; restart only via PermissionRestartIntegration.
- Normalize flags to spec paths/names and use them as cache only.
- Make required permissions set reflect spec/report, not UI cells.
- Ensure request sequence + pause and avoid duplicate sources of truth for status.
