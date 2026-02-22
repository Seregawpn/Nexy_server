# Task Brief: Single owner payment toggle

Date: 2026-02-18
Assistant: Codex

## Goal
Use one runtime toggle for payment feature in active config.

## Change
- Removed alias block `payment_use` from active config:
  - `client/config/unified_config.yaml`
- Kept canonical flag:
  - `features.payment.enabled`

## Owner
- Source of Truth for runtime: `features.payment.enabled`
- `is_feature_enabled('payment')` still supports legacy alias as fallback for old external configs, but active config now has single toggle only.

## Validation
- `payment_use` key absent in YAML
- `features.payment.enabled = false`
