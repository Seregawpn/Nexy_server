# Packaging Keys + Preflight Checks

## Date
2026-01-27

## Changes
- Added missing Info.plist usage keys to `packaging/Nexy.spec`:
  - `NSInputMonitoringUsageDescription`
  - `NSFullDiskAccessUsageDescription`
- Added required key checks to `scripts/verify_pyinstaller.py`:
  - `NSContactsUsageDescription`
  - `NSInputMonitoringUsageDescription`
  - `NSFullDiskAccessUsageDescription`

## Files
- `packaging/Nexy.spec`
- `scripts/verify_pyinstaller.py`

## Verification Plan
- Run `scripts/verify_pyinstaller.py` and confirm it fails if any key missing.
- Rebuild `.app` and validate Info.plist contains the new keys.
