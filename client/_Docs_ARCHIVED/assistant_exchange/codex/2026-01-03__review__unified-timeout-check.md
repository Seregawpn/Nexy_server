# Review: Unified 30s permission timeout

## Scope
Checked unified timeout integration and impact on permission detection logic.

## Findings
- `max_wait_sec=30`, `open_settings_after_sec=10` added in config and wired into `_activate_and_wait_for_permission()`.
- Unified timeout now marks NOT_DETERMINED as `DENIED` after 30s for all permissions.
- The previous mic-specific “stale cache assumed granted” path is no longer present; this may misclassify mic as DENIED if AVFoundation remains stale after user grant.

## Recommendation
- For microphone only, treat timeout as `GRANTED` (stale-cache assumption) while keeping 30s duration uniform.
- Keep logs to distinguish `timeout_assumed_granted` vs `timeout_proceed_to_next`.

## Verification
- Reset mic permission, grant it, wait >30s, confirm status moves to GRANTED (not DENIED) or proceed logic is acceptable.
