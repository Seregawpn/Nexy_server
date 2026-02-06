# Add State Catalog Check to Pre-Build Gate (Soft)

Goal: include STATE_CATALOG ↔ Snapshot consistency check in pre-build gate as soft block.

## Changes
- Added soft-block check for `scripts/verify_state_catalog.py` to pre_build_gate.

## Files
- `scripts/pre_build_gate.sh`
