# Analysis: runtime smoke and legacy suite status

Date: 2026-02-09  
Type: analysis  
Assistant: codex

## Executed

1) Runtime smoke runner
- Command: `python3 client/scripts/run_release_suite.py --smoke`
- Result: FAILED
  - `pre_build_gate`: FAIL
  - `problem_scan_gate`: FAIL
  - `integration_tests`: PASS (`tests/test_gateways.py`, `tests/test_init_order.py`)

2) Detailed gate runs
- `client/scripts/pre_build_gate.sh --skip-tests` -> FAIL
- `client/scripts/problem_scan_gate.sh` -> FAIL

## Blocking reasons (from logs/reports)

1) Problem scan gate
- `TOTAL_ISSUES=762`
- `BLOCKING_ISSUES=609`
- Dominant blockers: `ruff` (line length/import/style), then `basedpyright`.
- Top offenders include archive docs snapshots under:
  - `client/Docs/_archive/input_arch/...`

2) Pre-build gate
- basedpyright: failed (1 error + many warnings)
- proto freshness check failed:
  - `server/server/modules/grpc_service/streaming_pb2.py` outdated
  - `client/modules/grpc_client/proto/streaming_pb2.py` outdated
- cancel centralization check failed:
  - direct `grpc.request_cancel` publisher found in
    `client/integration/integrations/input_processing_integration.py`

## Current runtime contour status
- Targeted regression suite for playback/interrupt/mode/actions: PASS (`17 passed`)
- New centralization changes remain stable in tests.

## What must be done to reach “100% confidence”

1) Regenerate protobuf artifacts (`streaming_pb2.py`) from updated `.proto`.
2) Remove/route direct `grpc.request_cancel` publish from `input_processing_integration.py` through centralized interrupt owner.
3) Reduce blocking lint debt in problem scan scope:
   - either exclude `Docs/_archive/**` from blocking lint gate,
   - or clean archive files to satisfy enforced rules.

## Artifacts
- `client/release_suite_report.json`
- `client/build_logs/problem_scan_latest.json`
- `client/build_logs/problem_scan_priority.json`
