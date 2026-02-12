# Analysis: build_final blocked by strict basedpyright gate

## What was fixed in this pass
- `config/unified_config.yaml`: set `integrations.permissions_v2.advance_on_timeout: false` (permissions preflight now passes).
- Replaced direct state reads with selector access:
  - `integration/integrations/speech_playback_integration.py`
  - `integration/integrations/first_run_permissions_integration.py`
- Fixed failing tests:
  - `tests/test_microphone_activation.py` (`_handle_key_release` -> `_handle_release`)
  - `tests/test_token_reporting.py` (`pytest.mark.asyncio` + `import pytest`)
- Installed tools in `.venv`:
  - `basedpyright`
  - `ruff`

## Current blocker
- `scripts/problem_scan_gate.sh` is called with `REQUIRE_BASEDPYRIGHT_IN_SCAN=true` from `packaging/build_final.sh`.
- Now that basedpyright is installed, scan runs and reports large legacy debt:
  - `TOTAL_ISSUES=406`
  - `BLOCKING_ISSUES=261`
  - `basedpyright_status=failed`
- Result: preflight fails on quality gate, even though packaging artifacts and permissions checks are healthy.

## Conclusion
- Root cause shifted from missing packaging artifacts to quality-gate policy mismatch:
  strict “basedpyright must be ok” conflicts with current repository baseline.
- To unblock sustainably, gate must enforce “no new violations” (delta/baseline policy), not “zero total historical violations”.
