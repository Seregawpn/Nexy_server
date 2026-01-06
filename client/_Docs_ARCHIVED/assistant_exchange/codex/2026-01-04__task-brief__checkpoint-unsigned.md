# Task Brief

## Objective
Prevent build failure at checkpoint before signing.

## Change
- `packaging/build_final.sh`: added an `allow_unsigned` flag to `checkpoint()`.
- Updated CHECKPOINT 01 to allow unsigned app before signing.

## Rationale
Pre-sign checkpoints should warn rather than fail when codesign is not yet valid.
