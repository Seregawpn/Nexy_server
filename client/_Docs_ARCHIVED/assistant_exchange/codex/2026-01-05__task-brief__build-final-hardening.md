# Build Final Script Hardening

- Date: 2026-01-05
- Scope: packaging/build_final.sh
- Goal: Prevent post-sign mutations of .app that invalidate codesign.
- Changes:
  - Added signing stage guard (pre/signed/post_staple).
  - Added pre-sign mutation enforcement for cleanup/version/repair steps.
  - Added bundle state recording and assertion using hash + mtime.
  - Added post-staple integrity checks before DMG creation and dist copy.
- Verification: Not run (requires local signing/notarization environment).
