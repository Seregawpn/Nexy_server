# Task Brief — Client browser rate-limit fallback key

Date: 2026-02-18
Assistant: Codex
Type: task-brief

## Goal
Добавить fallback API key на клиентской browser-execution ветке при `429/RESOURCE_EXHAUSTED` без дублирования owner-логики в интеграциях.

## Changes

1) Single-owner fallback in browser LLM adapter
- File: `client/modules/browser_automation/module.py`
- `GeminiLLMAdapter` updated:
  - new arg: `fallback_api_key`
  - maintains `primary` and optional `fallback` LLM clients
  - on rate-limit from primary (`429`, `resource_exhausted`, `quota`, `rate limit`) switches to fallback and retries current invocation
  - existing user-facing callbacks preserved for cases when fallback is unavailable/also fails

2) Browser module config wiring
- File: `client/modules/browser_automation/module.py`
- `_create_llm()` now reads fallback key via unified loader:
  - `unified_config.get_api_key("gemini_api_key_fallback")`
- Passes key into `GeminiLLMAdapter`.

3) Config schema alignment
- File: `client/config/unified_config.yaml`
- Added field in `browser_use` section:
  - `gemini_api_key_fallback: ''`

4) Tests
- File: `client/tests/test_token_reporting.py`
- Updated constructor calls for new adapter signature.
- Added test: fallback switch on rate limit (`test_rate_limit_switches_to_fallback_key`).

## Verification
- `pytest -q tests/test_token_reporting.py tests/test_browser_module_ready_bypass.py` (run in `client/`) -> 8 passed
- `python3 -m py_compile client/modules/browser_automation/module.py client/config/unified_config_loader.py client/tests/test_token_reporting.py` -> OK

## Architecture gates
- Single Owner: fallback switch lives only in `GeminiLLMAdapter`.
- Zero Duplication: no retry/fallback branching added to `BrowserUseIntegration`/workflow layers.
- Anti-Race: switch is adapter-local per task execution context; no shared global toggles.
- Flag lifecycle: fallback key consumed through existing unified key-loader path.
