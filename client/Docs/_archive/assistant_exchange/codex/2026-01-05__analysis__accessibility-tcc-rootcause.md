# Accessibility TCC Root Cause Analysis

## Summary
- Current source code uses AXIsProcessTrustedWithOptions in status_checker.py as the only Accessibility check.
- No direct TCCAccessRequest usage found in code; old subprocess path removed.

## Key Observations
- modules/permissions/first_run/status_checker.py: centralized AXIsProcessTrustedWithOptions check.
- modules/permissions/macos/accessibility_handler.py delegates checks to status_checker.
- modules/permissions/macos/permission_queue_old.py still references request_accessibility_permission, but file appears unused.

## Hypotheses
1) App binary still outdated or invalidly packaged, so logs come from old build.
2) Early AXIsProcessTrustedWithOptions call may still trigger TCC log on this macOS version (even if public API).

## Next Steps
- Ensure packaging completes successfully and produces valid signed app.
- Verify runtime logs contain AXIsProcessTrustedWithOptions line.
