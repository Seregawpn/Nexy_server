# Task Brief: browser LLM 503 user callback

## Request
When browser LLM path hits temporary service overload (503/UNAVAILABLE), inform user to try again.

## Changes
- `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/modules/browser_automation/module.py`
  - Added `llm_error_callback` support in `GeminiLLMAdapter`.
  - Added `_is_service_unavailable_error()` matcher (`503`, `UNAVAILABLE`, `high demand`, `try again later`).
  - On first matching error per adapter instance, emits callback payload:
    - `reason=llm_service_unavailable`
    - `model`
    - `error`
  - Callback is propagated from `BrowserUseModule.initialize(...)` to adapter creation.

- `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/integration/integrations/browser_use_integration.py`
  - Registered `on_llm_error` callback and wired into module init.
  - On `llm_service_unavailable`:
    - publishes `system.notification` with retry guidance
    - publishes `grpc.tts_request` voice prompt: "Browser service is busy right now. Please try again."

## Architecture gates
- Single owner: user-facing browser LLM errors handled in `BrowserUseIntegration` (UX owner).
- Zero duplication: reused existing notification + TTS channels, no new messaging path.
- Anti-race: callback throttled to one notification per adapter instance (`_service_unavailable_notified`).
- Flag lifecycle: no new flags.

## Validation
- `python3 -m py_compile modules/browser_automation/module.py integration/integrations/browser_use_integration.py` passed.
