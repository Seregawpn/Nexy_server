# Analysis: packaged permissions metadata

## Checks
- Mounted `dist/Nexy.dmg` and inspected `Nexy.app`.
- Verified Info.plist usage description keys.
- Verified entitlements via codesign.

## Results
- Info.plist contains: NSMicrophoneUsageDescription, NSScreenCaptureUsageDescription, NSContactsUsageDescription, NSInputMonitoringUsageDescription, NSAccessibilityUsageDescription, NSFullDiskAccessUsageDescription.
- Bundle ID: `com.nexy.assistant`.
- Entitlements include mic, screen capture, contacts (addressbook), network client, automation apple-events.

## Conclusion
Packaging includes required keys/entitlements for permission prompts; missing prompts would be due to TCC state or non-app launch, not packaging metadata.
