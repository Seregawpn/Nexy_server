# Task
- Confirm macOS permission dialog deadlock fix and assess main-thread safety.

# Sources
- AGENTS.md
- _Docs_ARCHIVED/PROJECT_REQUIREMENTS.md
- _Docs_ARCHIVED/ARCHITECTURE_OVERVIEW.md
- integration/integrations/first_run_permissions_integration.py

# Findings
- Main-thread NSAlert approach removes System Events dependency and resolves the TCC deadlock.
- Current implementation uses performSelectorOnMainThread and an asyncio.Future, which is correct for AppKit threading.
- Potential edge case: asyncio.wait_for timeout cancels the Future; later set_result can raise InvalidStateError unless guarded.

# Recommendation
- Add a future.done() guard before set_result to avoid InvalidStateError after timeout/cancellation.
