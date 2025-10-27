# Permission Restart Module

Automatically schedules a Nexy client relaunch when the user grants critical
macOS permissions (microphone, accessibility, input monitoring, screen
recording). The module is designed to work exclusively through the EventBus and
does not have direct dependencies on other integrations besides the optional
updater coordination hook.

## Components

- **`core.permission_change_detector`** — normalises `permissions.changed` and
  `permissions.status_checked` events and emits `PermissionTransition` objects
  when a critical permission moves into the `GRANTED` state.
- **`core.restart_scheduler`** — debounces restart requests, waits for safe
  application state (no active sessions, no ongoing updates) and publishes
  diagnostic events before triggering the actual relaunch.
- **`macos.restart_handler`** — macOS specific helper that reuses the updater
  relaunch strategy (`open -a Nexy.app` + `os._exit(0)`). Supports
  `NEXY_DISABLE_AUTO_RESTART=true` for dry‑run testing.

## Event Contract

The integration publishes diagnostics via the EventBus:

```text
permission_restart.scheduled {
  session_id: str | null,
  reason: str,
  delay_sec: float,
  critical_permissions: [str]
}

permission_restart.executing {
  session_id: str | null,
  reason: str
}
```

Consumers can subscribe to these events to surface UI notifications or log
entries.

## Configuration

`config/unified_config.yaml` section:

```yaml
integrations:
  permission_restart:
    enabled: true
    critical_permissions:
      - microphone
      - accessibility
      - input_monitoring
      - screen_capture
    restart_delay_sec: 5.0
    max_restart_attempts: 3
    respect_active_sessions: true
    respect_updates: true
```

The `critical_permissions` field accepts enum values from
`modules.permissions.core.types.PermissionType`.

## Behaviour Summary

1. Watch permission events via EventBus.
2. Detect transitions where a critical permission becomes `GRANTED`.
3. Debounce multiple permissions and wait until:
   - the application mode returns to `SLEEPING` (optional), and
   - the updater is not currently installing an update (optional).
4. Delay for `restart_delay_sec`, publish `permission_restart.executing` and
   relaunch Nexy using the existing updater relaunch logic.
