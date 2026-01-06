# Task Brief

## Objective
Add a guard to prevent notarization when `TIMESTAMP_MODE=none`.

## Change
- `packaging/build_final.sh`: if `TIMESTAMP_MODE=none` and `NEXY_SKIP_NOTARIZATION` is not set, force `SKIP_NOTARIZATION=1` with a warning.

## Rationale
Notarization requires a secure timestamp; `--timestamp=none` causes notarization to fail.

## Verification
- Manual run with `TIMESTAMP_MODE=none` should skip notarization steps and avoid notarytool failures.
