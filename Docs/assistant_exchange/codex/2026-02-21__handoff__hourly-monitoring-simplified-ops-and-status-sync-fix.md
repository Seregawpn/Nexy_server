# Handoff: Hourly monitoring + simplified ops + remote status sync fix

## Scope
- Simplified server operations into one entrypoint.
- Enforced hourly remote monitoring cadence.
- Fixed local pull of remote monitoring status that incorrectly wrote `{}`.

## Changes
- Updated: `server/scripts/pull_remote_server_monitor_status.sh`
  - Split fetch flow into two phases:
    - phase 1: status + incident metadata only
    - phase 2: incident body fetch by file path only when incident mtime changed
  - Hardened `[stdout]/[stderr]` parsing with optional leading spaces.
  - Switched marker extraction to `sed` range parsing for stability.
  - Added JSON validation before writing `monitor_inbox/remote_server_status.json`.
  - Added state file: `monitor_inbox/.state/remote_last_incident_mtime_epoch`.
  - Added metadata-only remote incident fallback file when full body is truncated by `az vm run-command` output limit.

## Verification
- Ran `bash server/scripts/pull_remote_server_monitor_status.sh`.
- Confirmed `monitor_inbox/remote_server_status.json` contains valid JSON with real fields (not `{}`).
- Confirmed `monitor_inbox/2026-02-21__01-54-11__incident__server-monitor.remote.md` created and state file updated.
- Ran `bash server/scripts/quick_server_ops.sh monitor-once`.
- Confirmed no duplicate remote incident file creation for same incident mtime.

## Current operational status
- Monitoring pipeline is functional end-to-end (hourly cadence + local file artifacts).
- Remote status currently indicates broken state due elevated error count:
  - `error_count_70m: 20`
  - contains `API key expired` / `API_KEY_INVALID` class errors in logs.

## Required follow-up
- Rotate/replace server API key in VM `config.env` and restart service.
- Re-run:
  - `bash server/scripts/quick_server_ops.sh check`
  - `bash server/scripts/quick_server_ops.sh monitor-once`
- Expected after key fix: `state: "ok"` and `error_count_70m: 0` trend.
