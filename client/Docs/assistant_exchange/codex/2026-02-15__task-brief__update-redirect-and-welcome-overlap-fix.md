# Task Brief: updater redirect + welcome overlap fix

## Problem
1. Startup update failed with `too many redirects` on GitHub release URL.
2. Update announcement and welcome message overlapped at startup.

## Changes
- `/modules/updater/net.py`
  - Reworked urllib3 retry policy:
    - `total=None`
    - `connect/read/status = retries`
    - `redirect=10`
    - `raise_on_redirect=False`
  - Redirect following is now independent from connect/read retry budget.

- `/integration/integrations/welcome_message_integration.py`
  - Added startup-update guard:
    - subscribe to `updater.update_started/completed/failed/skipped`
    - defer welcome while startup update is active
    - apply short cooldown after startup update terminal event
    - schedule retry for pending welcome after cooldown

## Validation
- `python3 -m py_compile modules/updater/net.py integration/integrations/welcome_message_integration.py` passed.

## Expected Logs
- On startup update begin:
  - `[WELCOME_INTEGRATION] Startup update started - welcome deferred`
- After update terminal event:
  - `[WELCOME_INTEGRATION] Startup update terminal event - applying welcome cooldown`
- Welcome starts only after cooldown window, not immediately over update voice.
