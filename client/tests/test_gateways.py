"""Gateway rules smoke tests and coverage anchors.

These tests intentionally reference gateway names and decision strings so
scripts/verify_rule_coverage.py can validate coverage.
"""

from __future__ import annotations

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from integration.core.gateways import (
    Decision,
    decide_continue_integration_startup,
    decide_permission_restart_safety,
    decide_permission_restart_schedule,
    decide_permission_restart_wait,
    decide_process_audio,
    decide_route_manager_reconcile,
    decide_start_listening,
    decide_update_launch,
    decide_whatsapp_action,
)
from integration.core.selectors import (
    DeviceStatus,
    NetworkStatus,
    PermissionStatus,
    Snapshot,
    WhatsappStatus,
)

try:
    from mode_management import AppMode  # type: ignore[reportMissingImports]
except Exception:  # pragma: no cover - fallback for repo layout
    from modules.mode_management import AppMode  # type: ignore[reportMissingImports]


GATEWAYS = [
    "decide_start_listening",
    "decide_process_audio",
    "decide_continue_integration_startup",
    "decide_permission_restart_safety",
    "decide_permission_restart_schedule",
    "decide_permission_restart_wait",
    "decide_route_manager_reconcile",
    "decide_update_launch",
    "decide_whatsapp_action",
]

DECISIONS = [
    "abort_listen",
    "abort_processing",
    "retry_backoff",
    "degrade_offline",
    "skip_restart",
    "delay_restart",
    "abort_permission_restart",
    "abort_update_launch",
    "abort_integration_startup",
    "notify_user",
]


def _make_snapshot(
    *,
    perm_mic: PermissionStatus = PermissionStatus.GRANTED,
    perm_screen: PermissionStatus = PermissionStatus.GRANTED,
    perm_accessibility: PermissionStatus = PermissionStatus.GRANTED,
    device_input: DeviceStatus = DeviceStatus.DEFAULT_OK,
    network: NetworkStatus = NetworkStatus.ONLINE,
    first_run: bool = False,
    app_mode: AppMode = AppMode.SLEEPING,
    restart_pending: bool = False,
    update_in_progress: bool = False,
    whatsapp_status: WhatsappStatus = WhatsappStatus.DISCONNECTED,
) -> Snapshot:
    return Snapshot(
        perm_mic=perm_mic,
        perm_screen=perm_screen,
        perm_accessibility=perm_accessibility,
        device_input=device_input,
        network=network,
        first_run=first_run,
        app_mode=app_mode,
        restart_pending=restart_pending,
        update_in_progress=update_in_progress,
        whatsapp_status=whatsapp_status,
    )


def test_decide_start_listening_abort_listen() -> None:
    snapshot = _make_snapshot(perm_mic=PermissionStatus.DENIED)
    assert decide_start_listening(snapshot) == Decision.ABORT


def test_decide_start_listening_retry_backoff() -> None:
    snapshot = _make_snapshot(device_input=DeviceStatus.BUSY, app_mode=AppMode.LISTENING)
    assert decide_start_listening(snapshot) == Decision.RETRY


def test_decide_start_listening_degrade_offline() -> None:
    snapshot = _make_snapshot(network=NetworkStatus.OFFLINE, app_mode=AppMode.LISTENING)
    assert decide_start_listening(snapshot) == Decision.DEGRADE


def test_decide_process_audio_abort_processing() -> None:
    snapshot = _make_snapshot(perm_screen=PermissionStatus.DENIED, app_mode=AppMode.PROCESSING)
    assert decide_process_audio(snapshot) == Decision.ABORT


def test_decide_process_audio_degrade_offline() -> None:
    snapshot = _make_snapshot(network=NetworkStatus.OFFLINE, app_mode=AppMode.PROCESSING)
    assert decide_process_audio(snapshot) == Decision.DEGRADE


def test_decide_continue_integration_startup_abort_integration_startup() -> None:
    snapshot = _make_snapshot(first_run=True, restart_pending=True)
    assert decide_continue_integration_startup(snapshot) == Decision.ABORT


def test_decide_permission_restart_safety_abort_permission_restart() -> None:
    snapshot = _make_snapshot(update_in_progress=True)
    assert decide_permission_restart_safety(snapshot) == Decision.ABORT


def test_decide_permission_restart_schedule_skip_restart() -> None:
    snapshot = _make_snapshot()
    extra = {
        "permission_restart": {
            "respect_updates": True,
            "update_available": True,
        }
    }
    assert decide_permission_restart_schedule(snapshot, extra=extra) == Decision.ABORT


def test_decide_permission_restart_wait_delay_restart() -> None:
    snapshot = _make_snapshot(app_mode=AppMode.LISTENING)
    extra = {
        "permission_restart": {
            "respect_active_sessions": True,
        }
    }
    assert decide_permission_restart_wait(snapshot, extra=extra) == Decision.RETRY


def test_decide_route_manager_reconcile_abort_integration_startup() -> None:
    snapshot = _make_snapshot(first_run=True)
    assert decide_route_manager_reconcile(snapshot) == Decision.ABORT


def test_decide_route_manager_reconcile_retry_backoff() -> None:
    snapshot = _make_snapshot(device_input=DeviceStatus.BUSY, app_mode=AppMode.LISTENING)
    assert decide_route_manager_reconcile(snapshot) == Decision.RETRY


def test_decide_update_launch_abort_update_launch() -> None:
    snapshot = _make_snapshot(app_mode=AppMode.LISTENING, update_in_progress=True)
    assert decide_update_launch(snapshot) == Decision.ABORT


def test_decide_whatsapp_action_notify_user() -> None:
    snapshot = _make_snapshot(whatsapp_status=WhatsappStatus.DISCONNECTED)
    assert decide_whatsapp_action(snapshot) == Decision.NOTIFY_USER
