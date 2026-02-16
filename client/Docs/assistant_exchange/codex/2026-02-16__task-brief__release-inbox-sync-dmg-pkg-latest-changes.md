# Task Brief: mandatory release_inbox sync for DMG/PKG/latest changes

## Request
Ensure packaged artifacts (`DMG`, `PKG`) and latest change notes are always pushed into `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/server/release_inbox` as part of release flow.

## Implemented

1. Centralized sync step in release pipeline
- Updated `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/scripts/release_build.sh`.
- Added mandatory Step 3: run `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/scripts/sync_release_inbox.sh`.
- Build now fails if sync step fails.

2. Dedicated owner-script for inbox synchronization
- Finalized `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/scripts/sync_release_inbox.sh` (executable).
- Script copies exactly:
  - `dist/Nexy.dmg`
  - `dist/Nexy.pkg`
  - `Docs/LATEST_CHANGES.md` -> `server/release_inbox/LATEST_CHANGES.md`

3. Governance/documentation updates
- Updated `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/Docs/RELEASE_VERSIONING_AND_PUBLISHING.md` with mandatory `release_inbox` sync section.
- Updated `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/Docs/PACKAGING_READINESS_CHECKLIST.md` with required checklist block for `sync_release_inbox.sh` and inbox contents.

## Validation
- `bash -n scripts/release_build.sh` -> OK
- `bash -n scripts/sync_release_inbox.sh` -> OK
- `./scripts/sync_release_inbox.sh` -> FAIL (expected in current workspace: missing `client/dist/Nexy.dmg` and `client/dist/Nexy.pkg`)

## Outcome
Release flow now has a single owner step that enforces synchronization of release artifacts and `LATEST_CHANGES.md` into `server/release_inbox`; missing artifacts correctly fail fast.
