# Task Brief: all permissions mandatory

## Scope
Mark every permission in V2 as mandatory (hard) per request.

## Changes
- `config/unified_config.yaml`: set `integrations.permissions_v2.steps.screen_capture.criticality` to `hard`.
- `config/unified_config.yaml`: set `integrations.permissions_v2.steps.full_disk_access.criticality` to `hard`.

## Verification
- Re-run first-run after TCC reset; ensure `all_hard_granted=True` only when all permissions are granted.
