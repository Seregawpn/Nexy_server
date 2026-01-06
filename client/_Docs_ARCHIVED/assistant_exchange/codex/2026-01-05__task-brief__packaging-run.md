# Packaging Run

## Summary
- Started canonical packaging via packaging/build_final.sh with notarization.
- App notarization completed; DMG notarization still in progress (submission id noted).

## Progress
- /tmp/Nexy.app signed, notarized, stapled successfully (checkpoint 03 passed).
- DMG submission started: id 9c4c994a-8785-42a8-acc9-f7325f500665, status In Progress.

## Next Steps
- Wait for DMG notarization to finish, then stapler staple and continue PKG steps.
- Re-run build_final.sh or manually complete remaining steps when DMG notarization completes.

## Notes
- Initial run failed due to /tmp/Nexy_universal_backup.app being read-only; removed before retry.
