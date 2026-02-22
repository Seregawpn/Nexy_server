# Subscription period gate centralization

## Task
Align subscription activity logic so paid access is period-aware (`current_period_end`) and consistent between runtime quota checks and status API.

## Changes
- Added centralized policy `is_unlimited_access_active(...)` in:
  - `server/server/modules/subscription/core/subscription_types.py`
- Switched runtime unlimited checks to centralized policy in:
  - `server/server/modules/subscription/core/quota_checker.py`
  - `check_quota()`
  - `increment_usage()`
- Switched API status evaluation to centralized policy in:
  - `server/server/modules/subscription/subscription_module.py`
  - `get_subscription_status()`
- Added status response fields:
  - `access_tier`
  - `billing_active`

## Architecture Gates
- Single Owner: access activity decision centralized in one policy helper.
- Zero Duplication: removed duplicated unlimited logic in quota checker.
- Anti-Race: runtime decision now does not rely only on delayed webhook status updates.
- Flag Lifecycle: no new flags introduced.

## Validation
- `python3 -m py_compile` on modified files: OK
- Policy smoke checks (`PYTHONPATH=server/server`): OK

## Expected Behavior
- Paid/trial users remain unlimited until `current_period_end`.
- After `current_period_end`, unlimited access is removed even if webhook is delayed.
- `grandfathered` and `admin_active` remain perpetual unlimited.
