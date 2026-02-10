# VoiceOS ASAR unpack and code-culture snapshot

Date: 2026-02-10
Scope: unpack `app.asar` and assess code structure/engineering signals from shipped artifact.

## Unpack result
- Source archive: `/Applications/VoiceOS.app/Contents/Resources/app.asar`
- Unpacked to: `/Users/sergiyzasorin/Fix_new/tmp/voiceos_asar_unpacked`
- Extracted files: `4030`

## Product structure from artifact
- Platform type: Electron desktop app (not mobile bundle)
- Runtime code layout:
  - `out/main/main.js` (main process bundle, obfuscated/minified)
  - `out/preload/preload.js` (preload bundle, obfuscated/minified)
  - `out/renderer/index.html` + hashed assets bundle (`index-DCfnb0CP.js`, css/media)
- Dependencies include: `electron-updater`, `electron-store`, `sqlite3`, `@supabase/supabase-js`, `@connectrpc/*`, `posthog-node`.

## Mobile code presence check
- No iOS/Android artifacts found in unpacked app:
  - no `ios/`, `android/`, `.swift`, `.kt`, `gradle`, `.xcodeproj`, `react-native`, `flutter`.
- Conclusion: this package contains desktop code only.

## Code-culture signals from shipped build
- Positive:
  - clear process split (`main`/`preload`/`renderer`);
  - strict window prefs observed in bundle snippets (`contextIsolation: true`, `sandbox: true`, `nodeIntegration: false`) for at least part of windows;
  - structured local persistence with SQLite migrations and sync metadata.
- Risks:
  - production bundle is heavily obfuscated/minified, limiting maintainability and external auditability;
  - broad preload IPC surface exposed to renderer (large API object);
  - auth/session handling traces and token propagation pathways visible in built code strings;
  - previous signing/integrity issues remain separate release risk.

## Notes
- This is artifact-level analysis; repo-level code standards (tests/lint/CI) are not inferable from packaged app alone.
