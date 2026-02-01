# Analysis: packaged app shows no permission prompts

## Observations
- V2 pipeline completes immediately in logs; no prompt sequence shown.
- `permission_ledger.json` shows all permissions in PASS state with recent probes.
- Packaged app Info.plist contains all required usage descriptions; bundle id is `com.nexy.assistant`.
- Packaged app entitlements include mic/screen-capture/contacts, sandbox disabled.

## Conclusion
- The packaged app is not the root cause; the system already considers permissions granted, so no prompts appear.
- Immediate completion can happen when ledger is already in PASS or post-restart verify state, leading to fast completion without UI.

## Likely Cause
- Shared app data dir + prior runs already granted permissions for the same bundle id; V2 probes return PASS and pipeline completes.

## Evidence
- `~/Library/Application Support/Nexy/permission_ledger.json` shows PASS for all steps.
- `/tmp/NexyMount/Nexy.app/Contents/Info.plist` includes all NS*UsageDescription keys.
- `codesign -d --entitlements :- /tmp/NexyMount/Nexy.app` shows expected entitlements.

