# Task Brief: guard build_final.sh runtime shell to prevent function syntax errors

## Context
- Build log showed `syntax error near unexpected token '('` around the new parallel packaging block.
- This error pattern appears when bash script is parsed by `sh`-semantics.

## Change
- Added shell guard at the top of `packaging/build_final.sh`:
  - if `BASH_VERSION` is empty, re-exec script with `/bin/bash`.

## Why
- Ensures function definitions and bash-specific syntax are always interpreted correctly.
- Prevents accidental breakage when script is launched through `sh` wrappers/aliases.

## Verification
- `bash -n packaging/build_final.sh` -> OK
- `sh -n packaging/build_final.sh` -> OK (guard syntax-safe)
