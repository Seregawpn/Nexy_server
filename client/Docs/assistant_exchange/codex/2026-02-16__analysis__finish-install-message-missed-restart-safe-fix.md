# Analysis: finish install message missed; restart-safe one-time fix

## Problem
User did not receive "browser installed" message after install.

## Observed behavior
- Start TTS was emitted (`Browser installation has started ...`).
- Finish message did not always appear in the same runtime cycle.
- Browser binaries were present later, implying install completed eventually.

## Root cause
Finish announcement was runtime-branch dependent and could be skipped when app lifecycle/interruption occurred between install start and final success branch execution.

## Fix
Updated `/modules/browser_automation/module.py` with restart-safe install-cycle marker:
- Added pending flag file in app support:
  - `browser_install_pending.flag`
- On install start announcement: set pending flag.
- On success (`returncode == 0`): announce finish + clear flag.
- On detected-installed branch (`Chromium detected ...`) and pending flag exists:
  - announce finish once, then clear flag.
- On explicit install failure: clear flag.

## Effect
- Finish message is delivered exactly once per real install cycle, including recovery after restart.
- No repeated "installed" message on normal startup when no pending cycle exists.

## Verification
- `python3 -m py_compile modules/browser_automation/module.py integration/integrations/browser_use_integration.py` passed.
