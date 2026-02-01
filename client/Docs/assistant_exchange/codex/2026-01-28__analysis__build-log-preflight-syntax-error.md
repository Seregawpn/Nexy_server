# Analysis — Build log root cause

## Finding
Preflight log shows SyntaxError in `modules/permissions/v2/orchestrator.py:352` (expected indented block after `else`). This prevents V2 from importing and causes `V2 отключена или недоступна` at runtime.

## Fix
Removed broken if/else and restored `_probe_once` call (timed-slot mode) to make the file syntactically valid.

## File
- modules/permissions/v2/orchestrator.py
