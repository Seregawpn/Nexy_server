# Task Brief — Gemini rate-limit fallback API key

Date: 2026-02-18
Assistant: Codex
Type: task-brief

## Goal
Добавить архитектурно-централизованный fallback на второй Gemini API key только при rate-limit/quota ошибках.

## Changes

1) Unified config (single source)
- File: `server/server/config/unified_config.py`
- Added `TextProcessingConfig.gemini_api_key_fallback`.
- Added env read: `GEMINI_API_KEY_FALLBACK`.

2) Text module config pass-through
- File: `server/server/modules/text_processing/config.py`
- Added `self.gemini_api_key_fallback`.
- Added provider config pass-through key: `fallback_api_key`.
- Added status field: `gemini_api_key_fallback_set`.

3) Provider fallback logic (single owner)
- File: `server/server/modules/text_processing/providers/langchain_gemini_provider.py`
- Added fallback key state and fallback LLM clients.
- Added `_is_rate_limit_error()` classifier.
- Added `_astream_with_api_key_fallback()`:
  - primary astream
  - on 429/RESOURCE_EXHAUSTED/rate-limit/quota -> switch to fallback key for current request
  - non-rate-limit errors re-raised
- `initialize()`, `process()`, `process_with_image()` now use fallback-aware streaming path.
- `cleanup()` clears fallback clients.

4) Runtime config value
- File: `server/config.env`
- Added `GEMINI_API_KEY_FALLBACK=...` (provided by user).

5) Tests
- Added: `server/server/tests/test_langchain_gemini_provider_api_key_fallback.py`
  - rate-limit => fallback used
  - non-rate-limit => no fallback
  - rate-limit without fallback key => error propagated

## Verification
- `pytest -q server/server/tests/test_langchain_gemini_provider_api_key_fallback.py` -> 3 passed
- `pytest -q server/server/tests/test_grpc_collect_commit_flow.py` -> 5 passed
- `pytest -q server/server/tests/test_config_validation.py` -> 4 passed
- `python3 -m py_compile ...` for touched files -> OK

## Architecture gates
- Single Owner: fallback decision centralized in `LangChainGeminiProvider`.
- Zero Duplication: no parallel fallback paths added in workflow/grpc layers.
- Anti-Race: fallback switch scoped to request stream path; no shared mutable global switching.
- Flag Lifecycle: `GEMINI_API_KEY_FALLBACK` is runtime-consumed via unified config.
