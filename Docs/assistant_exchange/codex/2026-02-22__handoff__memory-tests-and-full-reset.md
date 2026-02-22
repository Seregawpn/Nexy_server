# Memory tests + full reset

## Done
1. Regression tests executed:
- `tests/test_memory_short_term_cleanup_scheduler.py`
- `tests/test_memory_single_call_smoke.py`
- `tests/test_grpc_phase_collect_commit.py`

Result: `10 passed`.

2. Full memory reset executed in PostgreSQL (both short-term and long-term):
- Updated table: `users`
- SQL effect: set `short_term_memory = NULL`, `long_term_memory = NULL` for rows where memory existed.

## Verification
Before reset:
- `users_with_memory = 8`
- `short_chars = 679`
- `long_chars = 64`

Updated rows:
- `8`

After reset:
- `users_with_memory = 0`
- `short_chars = 0`
- `long_chars = 0`

## Notes
- Reset was global for current DB (`voice_assistant_db`) and affected only memory fields.
