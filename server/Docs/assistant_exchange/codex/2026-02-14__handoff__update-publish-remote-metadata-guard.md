# Handoff: update publish remote metadata guard

## Context
User requested: for update flow (not release), assistant/script must upload artifact, then determine factual file size and write that into manifest.

## Implemented
- Updated `server/scripts/publish_assets_and_sync.py`.
- Added remote verification step after each successful upload:
  - download artifact from release URL,
  - compute factual remote `size` and `sha256`,
  - compare against local metadata,
  - abort on mismatch (no manifest push).
- Manifest now uses remote metadata values for DMG (`artifact.size`, `artifact.sha256`).

## Documentation updates
- `Docs/RELEASE_AND_UPDATE_GUIDE.md`
  - Added expected log markers for remote verification.
  - Added mandatory `Update-only Integrity Rule` section.
- `server/Docs/SERVER_DEPLOYMENT_GUIDE.md`
  - Added explicit note that update-only publication must write manifest from release URL metadata.

## Verification
- `python3 -m py_compile server/scripts/publish_assets_and_sync.py` passed.

## Operational effect
- Prevents false manifest values when uploaded artifact URL is wrong or content differs.
- Reduces update failures caused by size/hash drift between local build and published artifact.
