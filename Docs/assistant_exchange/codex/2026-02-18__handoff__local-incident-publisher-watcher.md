# Handoff: Local Incident Publisher Watcher

Date: 2026-02-18
Assistant: codex
Type: handoff

## Goal
Публиковать локальный markdown-документ в текущем проекте при сбоях удалённого сервера.

## Implemented
- Added one-shot incident publisher:
  - `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/server/server/scripts/publish_server_incident_local.sh`
- Added local watcher start script:
  - `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/server/server/scripts/start_local_server_monitor.sh`
- Added local watcher stop script:
  - `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/server/server/scripts/stop_local_server_monitor.sh`
- Output directory (local, in current project):
  - `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/server/monitor_inbox`

## Behavior
- Every 5 minutes watcher runs publisher.
- Publisher checks VM via `az vm run-command`:
  - `systemctl is-active voice-assistant`
  - `curl http://127.0.0.1:8080/health`
  - recent `journalctl` errors (70m window)
- If broken state detected, creates markdown incident in `monitor_inbox`.
- Duplicate incident states are deduplicated via hash (`monitor_inbox/.state/last_issue_hash`).

## Runbook
- Start watcher:
  - `server/scripts/start_local_server_monitor.sh`
- Stop watcher:
  - `server/scripts/stop_local_server_monitor.sh`
- Manual check + publish once:
  - `server/scripts/publish_server_incident_local.sh`

## Current status
- Watcher started successfully and running.
- Incident file published in local `monitor_inbox`.
