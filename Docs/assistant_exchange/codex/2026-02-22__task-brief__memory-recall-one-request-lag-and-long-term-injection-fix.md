# Task Brief: Memory recall fixes (one-request lag + long-term prompt injection)

## Problem
User reports: after "запомни, я люблю спорт" assistant later says it does not remember.

## Findings
1. `MemoryWorkflowIntegration.get_memory_context_parallel()` was non-blocking on cold fetch and returned `None` immediately while only scheduling background fetch.
   - Effect: one-request lag (memory often missing exactly on the next question).
2. `StreamingWorkflowIntegration._enrich_context()` injected only `recent_context` and ignored `long_term_context`.
   - Effect: durable facts (preferences) could be present in DB but not passed to LLM prompt.

## Changes
1. `server/server/integrations/workflow_integrations/memory_workflow_integration.py`
   - Increased `memory_fetch_timeout` to `0.35`.
   - `get_memory_context_parallel()` now:
     - returns cache if available,
     - waits briefly for existing in-flight fetch,
     - performs a short direct fetch for current request,
     - falls back to background fetch only on timeout/empty.
2. `server/server/integrations/workflow_integrations/streaming_workflow_integration.py`
   - `_enrich_context()` now injects both:
     - `Memory Context (recent): ...`
     - `Memory Context (long-term): ...`

## Tests
Added tests:
- `server/server/tests/test_memory_context_injection_and_fetch.py`
  - immediate context return without one-request lag,
  - long-term memory included in enriched prompt.

Also retained fallback memory extraction tests:
- `server/server/tests/test_memory_manager_heuristic_fallback.py`

Run:
- `PYTHONPATH=. ../.venv/bin/pytest -q tests/test_memory_manager_heuristic_fallback.py tests/test_memory_context_injection_and_fetch.py`
- Result: `4 passed`.
