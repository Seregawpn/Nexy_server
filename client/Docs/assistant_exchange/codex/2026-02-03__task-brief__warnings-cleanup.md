# Warnings Cleanup (Deprecation/pytest/logging)

Goal: remove remaining warnings sequentially.

## Changes
- Replaced deprecated selector usage in predicates.
- Registered pytest mark `smoke`.
- Handled file logging permission errors gracefully.

## Files
- `integration/core/gateways/predicates.py`
- `pyproject.toml`
- `integration/utils/logging_setup.py`
