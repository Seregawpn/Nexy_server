# VoiceOS installed state analysis

Date: 2026-02-10
Scope: local inspection of installed `/Applications/VoiceOS.app` without runtime debugging.

## Findings
- App exists: `/Applications/VoiceOS.app`
- Bundle id: `com.voiceos.app`
- Version: `0.0.23` (`CFBundleShortVersionString` and `CFBundleVersion`)
- Stack: Electron app (`AtomApplication`, `Resources/app.asar`)
- Min macOS: `11.0`
- URL scheme: `voiceos://`
- ATS: arbitrary loads enabled + localhost/127.0.0.1 insecure HTTP exceptions
- Permissions requested: microphone, camera, bluetooth
- Auto-update channel: S3 bucket `voiceos-staging-releases` (`us-east-1`)
- Binary: universal (`x86_64`, `arm64`)

## Runtime profile found
- App support directory exists: `~/Library/Application Support/VoiceOS`
- Log directory exists: `~/Library/Logs/VoiceOS`
- Local DB exists: `voiceos.db`
- DB tables: `app_icons`, `custom_instructions`, `db_migrations`, `dictations`, `dictionary`, `sync_metadata`, `voice_sessions`
- Main log indicates helper start:
  - `Starting app monitor: .../Resources/binaries/app-observer`

## Security/integrity observations
- `codesign -d --entitlements` reports invalid entitlements blob (ignored by OS).
- `codesign --verify --deep --strict` failed with invalid signature for arm64.
- `spctl -a -vv` returned code signing subsystem internal error.

## Notes
- Local config contains active auth/session material in plaintext JSON.
- Do not copy/share the file contents externally.
