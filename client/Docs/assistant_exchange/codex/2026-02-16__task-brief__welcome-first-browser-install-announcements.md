# Task Brief

## Context
User reported missing browser-install voice messages, wrong order with startup welcome, and requested explicit message when browser is already installed.

## Diagnosis
Browser install TTS could be emitted before startup welcome and before stable playback context, causing perceived message loss and poor UX ordering.

## Changes
1. `integration/integrations/welcome_message_integration.py`
- Added explicit lifecycle events:
  - `welcome.completed` on successful welcome flow.
  - `welcome.failed` on failed welcome flow.

2. `integration/integrations/browser_use_integration.py`
- Added startup TTS gate:
  - Browser startup/install TTS (`session_id == "system"`) is queued until `welcome.completed`.
  - Added timeout fallback (20s) to avoid deadlock if welcome event never arrives.
  - Added dedupe set for queued startup TTS messages.
- Subscribed to `welcome.completed` and flushes queued browser TTS in order.

3. `modules/browser_automation/module.py`
- In chromium-detected branch (no pending install), added explicit notification + TTS:
  - "Browser is already installed and ready to use."

## Architecture Fit
- Browser installation state owner remains `BrowserUseModule`.
- UX delivery orchestration moved to `BrowserUseIntegration` (single runtime owner for ordering vs welcome).
- No new global state axis introduced.

## Concurrency/Race Notes
- Existing single-flight install guards remain unchanged (`_install_lock`, `_install_task_guard`, `_install_task`).
- Startup TTS queue flush is idempotent and deduplicated.
- Timeout fallback prevents indefinite wait on `welcome.completed`.

## Validation
- `python3 -m py_compile integration/integrations/browser_use_integration.py integration/integrations/welcome_message_integration.py modules/browser_automation/module.py`
- Result: success.

## Expected Runtime Behavior
1. Welcome is spoken first.
2. Browser install/startup messages are spoken after welcome.
3. If browser is already present, assistant says it is already installed and ready.
