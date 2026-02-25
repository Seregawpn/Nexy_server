# Cutover Endpoint Sync to New Azure IP

## Context
User confirmed to proceed with post-migration cutover work.
New production server endpoint: `20.104.80.82`.

## What was done
- Replaced legacy endpoint references in active (non-archive) server scripts/docs:
  - old IP `20.63.24.187` -> `20.104.80.82`
  - old host `nexy-server.canadacentral.cloudapp.azure.com` -> `20.104.80.82`
- Scope excluded:
  - `**/_archive/**`
  - `**/assistant_exchange/**`

## Source of Truth
- Runtime public endpoint: `https://20.104.80.82`
- VM: `NexyNew` (`NexyNewRG`)

## Notes
- Existing workspace has many unrelated modified files; this sync touched only files matched by endpoint pattern replacement in active paths.
- DNS cutover still required if clients use a domain.

## Next step
- Update domain A-record to `20.104.80.82` (if domain is used) and monitor 30-60 minutes.
