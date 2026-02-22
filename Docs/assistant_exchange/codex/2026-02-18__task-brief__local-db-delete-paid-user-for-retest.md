# Task Brief: local DB delete paid user for retest

Date: 2026-02-18
Assistant: Codex

## Goal
Delete paid test user from local subscription DB to allow clean payment flow retest.

## Actions
1. Identified paid user in local DB:
- `E03D2455-8EF1-5270-AA03-13B5771C7CB2` (`status=paid`)

2. Executed destructive cleanup via guarded script:
- `NEXY_CONFIRM_DESTRUCTIVE=YES python3 clear_user_data.py --allow-delete --hardware-id E03D2455-8EF1-5270-AA03-13B5771C7CB2`

3. Verified deletion:
- `subscriptions_count=0`
- `payments_count=0`
- no `paid` subscriptions remain in local DB status report.

## Notes
- Deleted rows for this hardware_id:
  - subscriptions: 1
  - subscription_events: 3
  - payments: 0
  - quota_usage: 0
