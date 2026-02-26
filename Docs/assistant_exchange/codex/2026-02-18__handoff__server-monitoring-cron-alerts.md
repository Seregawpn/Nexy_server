# Handoff: Server Monitoring Cron Alerts

Date: 2026-02-18
Assistant: codex
Type: handoff

## What was done
- Installed monitor script on VM: `/usr/local/bin/nexy-monitor.sh`
- Installed cron schedule file: `/etc/cron.d/nexy-monitor`
- Added hourly check: `5 * * * * root /usr/local/bin/nexy-monitor.sh hourly`
- Added daily heartbeat: `0 2 * * * root /usr/local/bin/nexy-monitor.sh daily`
- Added optional env variable to VM config if missing: `MONITOR_ALERT_WEBHOOK=` in `/home/azureuser/voice-assistant/config.env`

## Behavior
- Checks `voice-assistant` service state.
- If service is not `active`: tries restart automatically and logs alert.
- Checks local health endpoint `http://127.0.0.1:8080/health`.
- Scans recent `journalctl` errors (last ~70 minutes) for critical Gemini/runtime patterns.
- Writes events to:
  - `/var/log/nexy-monitor.log`
  - syslog via `logger -t nexy-monitor`
- Sends webhook alert if `MONITOR_ALERT_WEBHOOK` is set.

## Verification evidence
- Install output confirms both files created.
- Smoke run executed and produced monitor log line.

## Next optional step
- Set `MONITOR_ALERT_WEBHOOK` to Slack/Teams/Telegram bridge URL and restart service:
  - `sudo sed -i 's|^MONITOR_ALERT_WEBHOOK=.*|MONITOR_ALERT_WEBHOOK=https://...|' /home/azureuser/voice-assistant/config.env`
  - `sudo systemctl restart voice-assistant`
