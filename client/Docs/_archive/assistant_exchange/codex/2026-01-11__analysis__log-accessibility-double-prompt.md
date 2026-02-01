# Log analysis: Accessibility + double prompt

## Evidence
- log.md:467, 479, 1203, 1209 show `TCCAccessRequest for kTCCServiceAccessibility` from com.nexy.assistant without entitlement.
- log.md:520+ shows repeated `System Events TCCAccessRequestIndirect` (osascript/System Events activity).
- No ListenEvent/Input Monitoring entries in log excerpt.

## Interpretation
- Accessibility prompt is triggered from a non-recommended path (AXIsProcessTrustedWithOptions / private request).
- Additional prompts likely come from osascript/System Events calls (Apple Events), not strictly Input Monitoring.

## Next steps
- Ensure no early pynput/AX calls in main process.
- Gate any osascript/System Events usage until after first-run permissions.
