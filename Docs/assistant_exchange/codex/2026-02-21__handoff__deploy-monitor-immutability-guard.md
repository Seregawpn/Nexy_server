# Handoff: Deploy monitor immutability guard

## Goal
Prevent accidental monitoring changes during regular server deploy/update.

## Change
- Updated `server/scripts/deploy_server_one_click.sh`:
  - Added strict monitor guard enabled by default: `MONITOR_GUARD_STRICT=1`.
  - Before deploy, captures SHA256 hashes of:
    - `/usr/local/bin/nexy-monitor-snapshot.sh`
    - `/etc/cron.d/nexy-monitor-snapshot`
  - After deploy+restart+health checks, compares hashes.
  - If changed, deploy exits with error `41` (`ERROR: monitor artifacts changed during deploy`).
  - Added opt-out flag only for intentional monitor edits: `--allow-monitor-changes`.

## Verification
- `bash -n server/scripts/deploy_server_one_click.sh` passed.
- grep confirms guard paths/flag/error logic present.

## Operational usage
- Default deploy keeps monitoring immutable.
- Use `--allow-monitor-changes` only when intentionally changing monitor setup.
