# Flow/State Spec Sync

Goal: align Flow Interaction Spec and State Catalog with current code.

## Changes
- Added EventTypes reference to Flow Interaction Spec.
- Updated firstRun and permissions.restart_pending axes to use V2 ledger as Source of Truth.
- Added missing gRPC event constants in `EventTypes`.

## Files
- `Docs/FLOW_INTERACTION_SPEC.md`
- `Docs/STATE_CATALOG.md`
- `integration/core/event_types.py`
