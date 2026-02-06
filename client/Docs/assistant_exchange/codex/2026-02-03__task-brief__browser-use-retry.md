# BrowserUse Session Recovery

Goal: mitigate browser_use "browser not connected" failures by retrying once with a fresh session.

## Changes
- Added retry path for browser session failures in BrowserUseModule.
- Added config `browser_use.recovery_retries`.

## Files
- `modules/browser_automation/module.py`
- `config/unified_config.yaml`
