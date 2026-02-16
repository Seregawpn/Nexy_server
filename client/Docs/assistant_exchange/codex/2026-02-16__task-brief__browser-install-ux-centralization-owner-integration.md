# Task Brief

## Context
User requested strict centralization: no scattered install UX logic, deterministic startup order (welcome first), and explicit "already installed" voice message.

## Diagnosis
Install UX text/voice was split across module + integration, which violates single owner and risks race/order issues.

## Changes

1. `modules/browser_automation/module.py`
- Added `install_status_callback` in `initialize(...)`.
- Added `_emit_install_status(status, **data)` helper.
- Removed direct install UX side-effects (no direct notification/TTS text for install lifecycle).
- Replaced with status emissions:
  - `started`
  - `downloading`
  - `completed`
  - `already_installed`
  - `failed`
  - `lock_wait`

2. `integration/integrations/browser_use_integration.py`
- Wired `install_status_callback` to new `_handle_install_status(...)`.
- Centralized install UX message mapping in integration only.
- Preserved startup ordering guard: browser startup TTS is queued until `welcome.completed`.
- Added explicit handling for `already_installed` with notification + TTS.

3. `integration/integrations/welcome_message_integration.py`
- Added explicit lifecycle events:
  - publish `welcome.completed` on success
  - publish `welcome.failed` on failure

## Architecture Fit
- Install state owner: `BrowserUseModule`.
- Install UX owner: `BrowserUseIntegration`.
- Welcome lifecycle owner: `WelcomeMessageIntegration`.
- No second decision path introduced.

## Concurrency / Race
- Existing single-flight install guards untouched.
- Startup TTS uses queued flush on `welcome.completed` with timeout fallback.
- Dedupe set prevents duplicate startup TTS lines.

## Validation
- `python3 -m py_compile integration/integrations/browser_use_integration.py modules/browser_automation/module.py integration/integrations/welcome_message_integration.py`
- Result: success.

## Expected Behavior
1. Welcome is first.
2. Browser install/start/done or already-installed voice lines are spoken after welcome.
3. Install UX text/voice is fully centralized in integration.
