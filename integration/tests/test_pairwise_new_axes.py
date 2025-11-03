"""
Pairwise tests with new axes: restart_pending and update_in_progress.

Tests:
- decide_start_listening with new axes
- decide_process_audio with new axes
- decide_permission_restart_safety with full axis combinations

Axes:
- perm_mic (granted/denied)
- device_input (ok/busy)
- network (online/offline)
- firstRun (true/false)
- appMode (sleep/listen/process)
- restart_pending (true/false)
- update_in_progress (true/false)
"""

import logging
import pytest

from integration.core.gateways.common import (
    Decision,
    decide_start_listening,
    decide_process_audio,
)
from integration.core.gateways.permission_gateways import decide_permission_restart_safety
from integration.core.selectors import (
    Snapshot,
    PermissionStatus,
    DeviceStatus,
    NetworkStatus,
    AppMode,
)


class TestPairwiseWithNewAxes:
    """Pairwise tests including new axes restart_pending and update_in_progress."""

    @pytest.mark.parametrize(
        "perm_mic,device,network,first_run,app_mode,restart_pending,expected_decision",
        [
            # Base cases (without new axes)
            (
                PermissionStatus.GRANTED,
                DeviceStatus.DEFAULT_OK,
                NetworkStatus.ONLINE,
                False,
                AppMode.SLEEPING,
                False,
                Decision.START,
            ),
            (
                PermissionStatus.DENIED,
                DeviceStatus.DEFAULT_OK,
                NetworkStatus.ONLINE,
                False,
                AppMode.SLEEPING,
                False,
                Decision.ABORT,
            ),
            # First_run blocks (regardless of restart_pending)
            (
                PermissionStatus.GRANTED,
                DeviceStatus.DEFAULT_OK,
                NetworkStatus.ONLINE,
                True,  # first_run blocks
                AppMode.SLEEPING,
                False,
                Decision.ABORT,
            ),
            (
                PermissionStatus.GRANTED,
                DeviceStatus.DEFAULT_OK,
                NetworkStatus.ONLINE,
                True,  # first_run blocks
                AppMode.SLEEPING,
                True,  # restart_pending doesn't affect this gateway
                Decision.ABORT,
            ),
            # Restart_pending alone doesn't affect listening (only affects coordinator)
            (
                PermissionStatus.GRANTED,
                DeviceStatus.DEFAULT_OK,
                NetworkStatus.ONLINE,
                False,
                AppMode.SLEEPING,
                True,  # restart_pending doesn't affect listening gateway
                Decision.START,
            ),
            # Device busy
            (
                PermissionStatus.GRANTED,
                DeviceStatus.BUSY,
                NetworkStatus.ONLINE,
                False,
                AppMode.LISTENING,
                False,
                Decision.RETRY,
            ),
            # Network offline
            (
                PermissionStatus.GRANTED,
                DeviceStatus.DEFAULT_OK,
                NetworkStatus.OFFLINE,
                False,
                AppMode.LISTENING,
                False,
                Decision.DEGRADE,
            ),
            # All combinations with restart_pending
            (
                PermissionStatus.GRANTED,
                DeviceStatus.DEFAULT_OK,
                NetworkStatus.ONLINE,
                False,
                AppMode.SLEEPING,
                True,  # restart_pending
                Decision.START,  # restart_pending doesn't affect listening
            ),
            (
                PermissionStatus.GRANTED,
                DeviceStatus.DEFAULT_OK,
                NetworkStatus.ONLINE,
                False,
                AppMode.LISTENING,
                True,  # restart_pending
                Decision.START,  # restart_pending doesn't affect listening
            ),
            (
                PermissionStatus.GRANTED,
                DeviceStatus.DEFAULT_OK,
                NetworkStatus.ONLINE,
                False,
                AppMode.PROCESSING,
                True,  # restart_pending
                Decision.ABORT,  # PROCESSING mode blocks listening start
            ),
        ],
    )
    def test_decide_start_listening_with_restart_pending(
        self, perm_mic, device, network, first_run, app_mode, restart_pending, expected_decision, caplog
    ):
        """Pairwise test for decide_start_listening with restart_pending axis."""
        snapshot = Snapshot(
            perm_mic=perm_mic,
            perm_screen=PermissionStatus.GRANTED,
            perm_accessibility=PermissionStatus.GRANTED,
            device_input=device,
            network=network,
            first_run=first_run,
            app_mode=app_mode,
            restart_pending=restart_pending,
        )

        with caplog.at_level(logging.DEBUG):
            decision = decide_start_listening(snapshot)
            assert decision == expected_decision

            # Verify decision log in canonical format
            logs = caplog.text
            assert "decision=" in logs
            assert "ctx={" in logs
            assert "source=listening_gateway" in logs

    @pytest.mark.parametrize(
        "perm_mic,network,app_mode,restart_pending,expected_decision",
        [
            # Base cases
            (
                PermissionStatus.GRANTED,
                NetworkStatus.ONLINE,
                AppMode.PROCESSING,
                False,
                Decision.START,
            ),
            (
                PermissionStatus.DENIED,
                NetworkStatus.ONLINE,
                AppMode.PROCESSING,
                False,
                Decision.ABORT,
            ),
            # Restart_pending doesn't affect processing gateway
            (
                PermissionStatus.GRANTED,
                NetworkStatus.ONLINE,
                AppMode.PROCESSING,
                True,  # restart_pending doesn't affect processing
                Decision.START,
            ),
            # Network offline
            (
                PermissionStatus.GRANTED,
                NetworkStatus.OFFLINE,
                AppMode.PROCESSING,
                False,
                Decision.DEGRADE,
            ),
            (
                PermissionStatus.GRANTED,
                NetworkStatus.OFFLINE,
                AppMode.PROCESSING,
                True,  # restart_pending doesn't affect processing
                Decision.DEGRADE,
            ),
        ],
    )
    def test_decide_process_audio_with_restart_pending(
        self, perm_mic, network, app_mode, restart_pending, expected_decision, caplog
    ):
        """Pairwise test for decide_process_audio with restart_pending axis."""
        snapshot = Snapshot(
            perm_mic=perm_mic,
            perm_screen=PermissionStatus.GRANTED,
            perm_accessibility=PermissionStatus.GRANTED,
            device_input=DeviceStatus.DEFAULT_OK,
            network=network,
            first_run=False,
            app_mode=app_mode,
            restart_pending=restart_pending,
        )

        with caplog.at_level(logging.DEBUG):
            decision = decide_process_audio(snapshot)
            assert decision == expected_decision

            # Verify decision log in canonical format
            logs = caplog.text
            assert "decision=" in logs
            assert "ctx={" in logs
            assert "source=processing_gateway" in logs

    @pytest.mark.parametrize(
        "perm_mic,device,network,first_run,app_mode,restart_pending,update_in_progress,expected_decision",
        [
            # All conditions met → START
            (
                PermissionStatus.GRANTED,
                DeviceStatus.DEFAULT_OK,
                NetworkStatus.ONLINE,
                False,
                AppMode.SLEEPING,
                False,
                False,
                Decision.START,
            ),
            # update_in_progress=True → ABORT (graceful)
            (
                PermissionStatus.GRANTED,
                DeviceStatus.DEFAULT_OK,
                NetworkStatus.ONLINE,
                False,
                AppMode.SLEEPING,
                False,
                True,  # update_in_progress blocks
                Decision.ABORT,
            ),
            # first_run=True & restart_pending=True → ABORT (hard_stop)
            (
                PermissionStatus.GRANTED,
                DeviceStatus.DEFAULT_OK,
                NetworkStatus.ONLINE,
                True,  # first_run
                AppMode.SLEEPING,
                True,  # restart_pending
                False,
                Decision.ABORT,
            ),
            # first_run_restart_pending takes precedence over update_in_progress
            (
                PermissionStatus.GRANTED,
                DeviceStatus.DEFAULT_OK,
                NetworkStatus.ONLINE,
                True,  # first_run
                AppMode.SLEEPING,
                True,  # restart_pending
                True,  # update_in_progress (ignored)
                Decision.ABORT,  # first_run_restart_pending checked first
            ),
            # restart_pending alone (without first_run) doesn't block
            (
                PermissionStatus.GRANTED,
                DeviceStatus.DEFAULT_OK,
                NetworkStatus.ONLINE,
                False,
                AppMode.SLEEPING,
                True,  # restart_pending alone
                False,
                Decision.START,  # Only blocks if first_run=True
            ),
            # update_in_progress blocks regardless of other conditions
            (
                PermissionStatus.GRANTED,
                DeviceStatus.BUSY,
                NetworkStatus.OFFLINE,
                False,
                AppMode.LISTENING,
                False,
                True,  # update_in_progress blocks
                Decision.ABORT,
            ),
            # All conditions met in LISTENING mode
            (
                PermissionStatus.GRANTED,
                DeviceStatus.DEFAULT_OK,
                NetworkStatus.ONLINE,
                False,
                AppMode.LISTENING,
                False,
                False,
                Decision.START,
            ),
            # All conditions met in PROCESSING mode
            (
                PermissionStatus.GRANTED,
                DeviceStatus.DEFAULT_OK,
                NetworkStatus.ONLINE,
                False,
                AppMode.PROCESSING,
                False,
                False,
                Decision.START,
            ),
            # update_in_progress blocks in LISTENING mode
            (
                PermissionStatus.GRANTED,
                DeviceStatus.DEFAULT_OK,
                NetworkStatus.ONLINE,
                False,
                AppMode.LISTENING,
                False,
                True,  # update_in_progress blocks
                Decision.ABORT,
            ),
            # update_in_progress blocks in PROCESSING mode
            (
                PermissionStatus.GRANTED,
                DeviceStatus.DEFAULT_OK,
                NetworkStatus.ONLINE,
                False,
                AppMode.PROCESSING,
                False,
                True,  # update_in_progress blocks
                Decision.ABORT,
            ),
            # Restart_pending doesn't block without first_run
            (
                PermissionStatus.GRANTED,
                DeviceStatus.DEFAULT_OK,
                NetworkStatus.ONLINE,
                False,
                AppMode.SLEEPING,
                True,  # restart_pending alone
                False,
                Decision.START,  # Doesn't block without first_run
            ),
            # First_run alone doesn't block (needs restart_pending)
            (
                PermissionStatus.GRANTED,
                DeviceStatus.DEFAULT_OK,
                NetworkStatus.ONLINE,
                True,  # first_run alone
                AppMode.SLEEPING,
                False,  # No restart_pending
                False,
                Decision.START,  # Doesn't block without restart_pending
            ),
            # Combination: first_run & restart_pending in LISTENING mode
            (
                PermissionStatus.GRANTED,
                DeviceStatus.DEFAULT_OK,
                NetworkStatus.ONLINE,
                True,
                AppMode.LISTENING,
                True,
                False,
                Decision.ABORT,
            ),
            # Combination: first_run & restart_pending in PROCESSING mode
            (
                PermissionStatus.GRANTED,
                DeviceStatus.DEFAULT_OK,
                NetworkStatus.ONLINE,
                True,
                AppMode.PROCESSING,
                True,
                False,
                Decision.ABORT,
            ),
        ],
    )
    def test_decide_permission_restart_safety_pairwise(
        self,
        perm_mic,
        device,
        network,
        first_run,
        app_mode,
        restart_pending,
        update_in_progress,
        expected_decision,
        caplog,
    ):
        """Pairwise test for decide_permission_restart_safety with all axes."""
        snapshot = Snapshot(
            perm_mic=perm_mic,
            perm_screen=PermissionStatus.GRANTED,
            perm_accessibility=PermissionStatus.GRANTED,
            device_input=device,
            network=network,
            first_run=first_run,
            app_mode=app_mode,
            restart_pending=restart_pending,
        )

        with caplog.at_level(logging.INFO if expected_decision == Decision.ABORT else logging.DEBUG):
            decision = decide_permission_restart_safety(snapshot, update_in_progress)
            assert decision == expected_decision, (
                f"Expected {expected_decision}, got {decision}\n"
                f"Context: first_run={first_run}, restart_pending={restart_pending}, "
                f"update_in_progress={update_in_progress}, app_mode={app_mode}"
            )

            # Verify decision log in canonical format
            logs = caplog.text
            assert "decision=" in logs
            assert "ctx={" in logs
            assert "source=permission_restart_gateway" in logs

            # Verify context contains all required keys
            assert "mic=" in logs
            assert "screen=" in logs
            assert "device=" in logs
            assert "network=" in logs
            assert "firstRun=" in logs
            assert "appMode=" in logs

            # Verify reason is logged for ABORT decisions
            if expected_decision == Decision.ABORT:
                if first_run and restart_pending:
                    assert "reason=first_run_restart_pending" in logs
                elif update_in_progress:
                    assert "reason=update_in_progress" in logs

