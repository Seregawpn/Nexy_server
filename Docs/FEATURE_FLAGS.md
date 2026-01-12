# Feature Flags Registry

> **Purpose**: Track all active feature flags and their kill-switches.
> **Source of Truth**: `config/unified_config.yaml` (features section).

## 🛡️ Critical Rules
1.  **Every new feature** must have a flag.
2.  **Naming Convention**: `snake_case_name` and `ks_snake_case_name` (kill-switch).
3.  **Default**: `enabled: false` for new features during development.

## 🚩 Active Flags

| Feature ID | Flag Name | Kill-Switch | Description | Status |
|---|---|---|---|---|
| F-000 | `template_feature` | `ks_template_feature` | Use for module templates | `disabled` |
| F-001 | `serial_tcc_prompts` | `ks_serial_tcc` | Sequential TCC permission prompts | `1% rollout` |
| F-002 | `use_events_for_update_status` | - | Shadow mode for update status | `1% rollout` |
| F-003 | `actions.open_app` | - | Open App MCP Action | `enabled` |
| F-004 | `actions.close_app` | - | Close App MCP Action | `enabled` |

## ➕ How to Register
1.  Add entry to this table.
2.  Add to `config/unified_config.yaml`.
3.  Use in Integration `__init__` via `UnifiedConfigLoader`.
