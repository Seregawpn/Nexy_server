# BrowserUse & Autostart Warning Mitigation

Goal: reduce browser_use watchdog warnings and auto-repair autostart LaunchAgent.

## Changes
- Added runtime tuning in `BrowserUseModule` to set browser_use event timeouts and optionally suppress bubus warnings.
- Enabled autostart auto-repair in config and wired integration to install LaunchAgent when missing.

## Files
- `modules/browser_automation/module.py`
- `config/unified_config.yaml`
- `integration/integrations/autostart_manager_integration.py`
