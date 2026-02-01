# Analysis: missing permissions prompts root cause

## Findings
- First-run uses V2 orchestrator (`integration/integrations/first_run_permissions_integration.py`), which runs all permissions sequentially with no batching.
- `config/unified_config.yaml` contains a legacy batching fix under `permissions.first_run.*`, but V2 ignores it; `permissions_v2.batching` is present and disabled, yet there is no batching logic in V2.
- V2 defines `accessibility` and `full_disk_access` as `open_settings`, so no dialog prompt appears for those steps.
- Contacts permission relies on `pyobjc` Contacts framework; if missing in packaged app, the prompt will never fire.

## Conclusion
The most likely root cause is the V2 pipeline requesting many dialogs in one session (no batching), which macOS TCC can suppress after the first few prompts, combined with settings-only steps (accessibility/full disk) and potentially missing Contacts framework support.
