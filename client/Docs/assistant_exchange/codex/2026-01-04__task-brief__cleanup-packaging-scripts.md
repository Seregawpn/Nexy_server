# Task Brief

## Objective
Remove legacy packaging scripts and obsolete docs, keep only the canonical release path.

## Changes
- Removed legacy packaging scripts:
  - `packaging/build_final_no_notary.sh`
  - `packaging/build_final_notarized.sh`
  - `packaging/build_test_hardened.sh`
  - `packaging/build_test_notarized.sh`
  - `packaging/build_test_quick.sh`
  - `packaging/build_universal_app_only.sh`
  - `packaging/finish_test_build.sh`
- Removed legacy helper:
  - `scripts/create_packages_without_notarization.sh`
- Removed legacy doc:
  - `Docs/PACKAGING_NO_NOTARY_GUIDE.md`

## Docs Updated
- `Docs/PACKAGING_VERIFICATION_CHECKLIST.md`
- `Docs/INSTALLATION_WITHOUT_NOTARIZATION.md`
- `Docs/TESTING_PACKAGED_APP.md`

## Canonical Path
- Build: `scripts/release_build.sh release|local`
- Verify: `scripts/verify_packaging_artifacts.sh`

## Verification
- No remaining references to removed scripts in `Docs/`, `packaging/`, or `scripts/`.
