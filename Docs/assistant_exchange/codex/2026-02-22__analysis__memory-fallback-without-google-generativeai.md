# Analysis: Memory fallback when `google.generativeai` is unavailable

## Context
User reported: assistant says "I will remember" but later cannot recall personal fact.

## Root Cause
- Runtime log shows `MemoryAnalyzer initialization failed: google.generativeai not available`.
- `MemoryManager.analyze_conversation()` returned empty memory when analyzer was unavailable.
- As a result, `update_memory_background()` had nothing to persist and memory stayed empty.

## Architecture Fit
- Owner preserved: `MemoryManager` remains single owner for memory extraction policy.
- No new owner-paths for mode/workflow were introduced.
- Existing `MemoryWorkflowIntegration -> MemoryManagementAdapter -> MemoryManager` chain kept intact.

## Change
- Added heuristic fallback extraction in `MemoryManager` for analyzer-unavailable mode:
  - detects explicit remember intent (`запомни`, `remember this`, etc.),
  - extracts simple preference facts (`я люблю ...`, `I like ...`, favorites),
  - sanitizes secret-like payloads (password/token/api key) to safe reference.
- `analyze_conversation()` now uses fallback instead of no-op when analyzer is missing.

## Files
- `server/server/modules/memory_management/core/memory_manager.py`
- `server/server/tests/test_memory_manager_heuristic_fallback.py`

## Verification
- Target tests run:
  - `PYTHONPATH=. ../.venv/bin/pytest -q tests/test_memory_manager_heuristic_fallback.py`
- Result: `2 passed`.

## Residual Risk
- Heuristic extraction is intentionally lightweight and less semantic than Gemini-based analyzer.
- Best quality still requires fixing env dependency mismatch (`google-generativeai` absent in active `.venv`).
