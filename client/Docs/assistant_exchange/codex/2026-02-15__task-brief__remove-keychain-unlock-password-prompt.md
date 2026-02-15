# Task Brief: remove interactive keychain unlock from packaging preflight

## Context
- Request: убрать запрос `password to unlock login.keychain` в упаковке приложения.
- Observed source: `packaging/build_final.sh` preflight certificate check block.

## Change
- Removed explicit `security unlock-keychain login.keychain` call.
- Kept certificate validation centralized via `security find-identity`.
- Added explanatory non-interactive log line in preflight.

## Architecture Fit
- Where it belongs: packaging preflight gate in `packaging/build_final.sh`.
- Source of truth: existing certificate checks (`security find-identity`) in the same script.
- No new state/flags/paths introduced.

## Risk
- Low. Flow now avoids interactive keychain prompt and remains compatible with CI/non-interactive runs.
- If keychain is locked, signing/notarization commands still fail naturally with explicit tool errors.

## Verification
1. Run packaging script and confirm no prompt `password to unlock login.keychain`.
2. Confirm preflight still validates identities (`Developer ID Application`).
3. Confirm signing/notarization pipeline behavior unchanged when identities are available.
