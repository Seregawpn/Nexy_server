# Analysis — First-run permissions order + welcome after restart

## Context
User reports:
- permission prompts appear in wrong order and too quickly (mic → accessibility → screen, no input prompt)
- welcome message does not play after app restart

## Sources
- `Docs/first_run_flow_spec.md`
- `config/unified_config.yaml`
- `integration/integrations/first_run_permissions_integration.py`
- `modules/permissions/first_run/status_checker.py`
- `modules/permissions/first_run/activator.py`
- `integration/integrations/permission_restart_integration.py`
- `integration/integrations/welcome_message_integration.py`

## Key Observations
- Canonical order in spec: microphone → accessibility → input monitoring → screen capture.
- Runtime order is config-driven (`integrations.permissions.required_permissions`), currently matches canonical.
- `check_input_monitoring_status()` can return GRANTED based on IOHIDCheckAccess; if it returns GRANTED early, input prompt is skipped.
- `system.ready_to_greet` is published only when accessibility + input monitoring + screen capture are GRANTED; missing input blocks welcome.

## Working Hypotheses
1) Input monitoring status check yields false-positive GRANTED → skips prompt → screen capture triggers next → welcome blocked after restart.
2) Packaged app config differs (order or required list), causing input monitoring to be skipped entirely.

## Low-cost Verification
- Inspect app logs for `📋 [PERMISSIONS] INITIAL statuses` and `Requesting <perm>` sequence.
- Confirm `check_input_monitoring_status()` values right before/after prompt.
- Verify runtime config in packaged bundle for `required_permissions` order.

## Proposed Fix Direction
- Ensure first-run flow strictly follows canonical order and does not skip input monitoring unless confirmed GRANTED.
- Add explicit guard/log when input monitoring is skipped due to status check.
- Ensure readiness gating logs include input status to unblock welcome diagnostics.

