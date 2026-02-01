# DMG spctl context handling

## Summary
- Clarified DMG spctl validation to handle "Insufficient Context" without masking notarization.

## Change
- packaging/build_final.sh now:
  - Tracks DMG notarization via stapler validate.
  - Captures spctl output and logs a clear reason when Insufficient Context occurs.
  - Still verifies DMG integrity via hdiutil verify.

## Files updated
- packaging/build_final.sh
