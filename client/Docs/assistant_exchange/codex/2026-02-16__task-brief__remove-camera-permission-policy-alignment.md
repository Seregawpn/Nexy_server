# Task Brief: remove camera permission (policy alignment)

## Request
Remove camera permission because camera is not required by current product behavior.

## Implemented

1. Removed camera entitlement
- Updated `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/packaging/entitlements.plist`.
- Deleted `com.apple.security.device.camera`.

2. Removed camera usage description
- Updated `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/packaging/Nexy.spec`.
- Deleted `NSCameraUsageDescription` from app `info_plist`.

3. Updated mandatory change journal
- Updated `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/Docs/LATEST_CHANGES.md` with this policy change.

## Validation
- `rg -n "com.apple.security.device.camera|NSCameraUsageDescription" packaging/entitlements.plist packaging/Nexy.spec` -> no matches.

## Outcome
Packaging permissions now match current product policy (`camera.enabled=false`), with no camera permission declared in release artifacts.
