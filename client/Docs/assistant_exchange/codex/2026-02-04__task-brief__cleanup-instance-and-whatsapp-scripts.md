# Task Brief: cleanup for residual duplicates/warnings

## Changes made
1. `integration/integrations/instance_manager_integration.py`
- Removed duplicate assignment in initialize:
  - deleted extra `self._initialized = True`

2. `scripts/force_login_whatsapp.py`
- Switched import from `client.modules.whatsapp` to `modules.whatsapp`
- Updated logger namespace to `modules.whatsapp.service_manager`
- Fixed import ordering for Ruff

3. `scripts/verify_whatsapp.py`
- Switched import from `client.modules.whatsapp` to `modules.whatsapp`

## Validation
- `python3 -m py_compile integration/integrations/instance_manager_integration.py scripts/force_login_whatsapp.py scripts/verify_whatsapp.py`
- `scripts/pre_build_gate.sh`
  - Result: all checks passed
  - Ruff: passed
  - basedpyright: 0 errors, 0 warnings, 0 notes

## Outcome
- Removed minor duplicate code noise in instance integration.
- Removed remaining basedpyright warnings in WhatsApp scripts.
- Quality gate remains green after cleanup.
