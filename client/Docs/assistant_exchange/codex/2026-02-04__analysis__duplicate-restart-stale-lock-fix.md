# Analysis: repeated app launches despite lock

## Observation
- log shows multiple CHECKIN with new PIDs (98378 → 98385 → 98410).
- `runningboardd` reports duplicate identities for `com.sergiyzasorin.nexy.voiceassistant`.

## Hypothesis
- lock validity check uses file mtime before PID validation; after timeout (or on access error), lock can be treated as stale even if process is alive.
- this allows a second instance to start.

## Fix applied
- In `modules/instance_manager/core/instance_manager.py::_is_lock_valid()`:
  - removed early mtime staleness check before PID validation.
  - only treat lock as stale when PID is missing or process is gone.

## Files changed
- `modules/instance_manager/core/instance_manager.py`

## Validation
- `python3 -m py_compile modules/instance_manager/core/instance_manager.py`

## Next checks
- Verify lock file created in `~/Library/Application Support/Nexy/nexy.lock` and is readable by the app process.
- If repeats persist, check whether LaunchAgent is auto-starting in parallel with manual app launch.
