# Task Brief

## Context
User requested to simplify install UX: remove final install completion message and keep only one startup message: browser is installing and may take a few minutes.

## Changes

### 1) Browser install UX contract simplified
File: `integration/integrations/browser_use_integration.py`

- Kept only startup install message for status `started`:
  - "Browser is installing. It may take a few minutes. After that, you can use browser use."
- Disabled install progress repetition (`downloading` -> no user message).
- Disabled final install messages:
  - `completed` -> no user-facing message
  - `already_installed` -> no user-facing message
- Removed playback-ack retry logic introduced earlier (not needed after product decision to suppress final messages).

### 2) Tests updated to new product behavior
File: `tests/test_browser_install_contracts.py`

- Updated start-message expectations to new text.
- Asserted `completed` and `already_installed` are silent by contract.
- Kept gRPC readiness tests intact.

## Validation
- `python3 -m py_compile integration/integrations/browser_use_integration.py tests/test_browser_install_contracts.py`
- `pytest -q tests/test_browser_install_contracts.py`
- Result: `5 passed`

## Architecture impact
- Centralization preserved:
  - install state owner: `BrowserUseModule`
  - install UX owner: `BrowserUseIntegration`
- No new owner path introduced.
