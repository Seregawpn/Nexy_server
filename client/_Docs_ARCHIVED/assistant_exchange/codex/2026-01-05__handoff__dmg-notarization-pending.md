# Handoff: DMG notarization pending

## Status
- DMG notarization submission: 9c4c994a-8785-42a8-acc9-f7325f500665
- Current status: In Progress (as of last check)

## Next steps
1) Wait for notarization to complete:
   xcrun notarytool info 9c4c994a-8785-42a8-acc9-f7325f500665 --keychain-profile "nexy-notary"
2) When Accepted:
   xcrun stapler staple dist/Nexy.dmg
3) Resume PKG steps via packaging/build_final.sh (or manual continuation if preferred)
4) Run scripts/verify_packaging_artifacts.sh

## Notes
- Previous build_final.sh run completed app signing+notarization+stapling and created DMG; waiting on DMG notarization.
