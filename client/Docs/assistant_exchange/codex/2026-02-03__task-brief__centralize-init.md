# Centralize Initialization Order

Goal: centralize integration initialization/start order in one Source of Truth.

## Changes
- Added centralized startup order lists in `integration/core/integration_factory.py` with `get_startup_order()`.
- Updated `integration/core/simple_module_coordinator.py` to use centralized order for initialize/start and warn on missing entries.

## Rationale
Removes duplicated order definitions and keeps initialization/start aligned.

## Files
- `integration/core/integration_factory.py`
- `integration/core/simple_module_coordinator.py`

## Notes
- Unknown integrations not present in the centralized order are appended and logged as a warning.
