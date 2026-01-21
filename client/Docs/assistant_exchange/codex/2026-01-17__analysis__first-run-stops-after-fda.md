# First-Run Stops After FDA

## Summary
User reports the permission flow hangs after granting Full Disk Access; Contacts and Input Monitoring prompts do not appear.

## Hypotheses
1) System Settings opens for FDA and the app loses foreground; subsequent Contacts/Input prompts may be suppressed or hidden while Settings is frontmost.
2) FDA activation blocks the async flow longer than expected (hold duration or synchronous `open` call), creating a perceived hang.

## Suggested Checks
- Inspect `logs/nexy.log` for `[FIRST_RUN]` and `[ACTIVATOR]` to confirm whether `activate_contacts` and `activate_input_monitoring` are invoked.
- If not invoked, trace where the loop stops after FDA.

## Proposed Direction
Keep the sequential flow in `FirstRunPermissionsIntegration`, but avoid blocking on FDA and re-activate the app after opening Settings (or defer FDA Settings to the end) so subsequent permission prompts are visible.
