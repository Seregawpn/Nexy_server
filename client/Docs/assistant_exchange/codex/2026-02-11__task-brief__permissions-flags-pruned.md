# Task Brief: pruned redundant permission flags

## Removed from config
- `integrations.permissions` (legacy V1 block) - removed entirely.
- `integrations.permission_restart.polling_enabled` - removed.
- `integrations.permission_restart.poll_interval_sec` - removed.
- `integrations.permissions_v2.batching.enabled` - removed.

## Kept
- `permissions_v2` runtime policy and timing (`advance_on_timeout`, `default_step_timeout_s`, `order`, `inter_step_pause_s`, per-step `step_timeout_s`).
- `permission_restart` active settings required by current flow.

## File
- `config/unified_config.yaml`
