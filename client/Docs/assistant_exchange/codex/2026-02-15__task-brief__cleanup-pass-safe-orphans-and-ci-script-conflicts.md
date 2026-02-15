# Task Brief: Cleanup Pass (Safe Orphans + CI Script Conflicts)

## What was done
1. Removed safe orphan files (no runtime/CI refs):
- `check_frozen.py`
- `main_output.txt`
- `test_messages_real.py`
- `verify_first_run_centralization.sh`

2. Closed CI/script conflicts with missing files in client tree:
- Added `scripts/generate_requirements_coverage.py`
- Added `scripts/monitor_metrics.py`
- Added `scripts/verify_docs_root_server_links.py`

3. Verified lint/gates:
- `ruff` for new scripts: OK
- `scripts/verify_doc_links.py`: OK
- `scripts/verify_docs_root_server_links.py`: OK
- `REQUIRE_BASEDPYRIGHT_IN_SCAN=true ./scripts/problem_scan_gate.sh`: blocking=0

## Notes
- `scripts/verify_docs_root_server_links.py` supports client-only checkout and skips false positives from “missing docs” section in `Docs/README.md` and placeholder refs.
- Cleanup intentionally avoided touching runtime modules and SoT docs.

## Next cleanup candidates (not executed in this pass)
- `modules/_module_template/` (template-only, no runtime refs)
- `REFACTORING_STATUS.md`, `voiceover.md` (historical/manual artifacts)
- Hotkey docs not linked in canonical map:
  - `Docs/HOTKEY_COMBINATION_REQUIREMENTS.md`
  - `Docs/HOTKEY_CONFLICT_GUARD_IMPLEMENTATION_PLAN.md`

