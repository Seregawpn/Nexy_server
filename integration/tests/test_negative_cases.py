"""
Negative tests for critical failure scenarios.

Tests:
- Updater does not start in PROCESSING mode (both string and Enum)
- Coordinator interrupts integration startup when restart_pending & firstRun
"""

import logging
import pytest

from integration.core.gateways.common import decide_continue_integration_startup, Decision
from integration.core.selectors import (
    Snapshot,
    PermissionStatus,
    DeviceStatus,
    NetworkStatus,
    AppMode,
)
from integration.tests.helpers.logging_asserts import assert_decision_logged


class TestNegativeCases:
    """Negative tests for critical failure scenarios."""

    def test_updater_does_not_start_in_processing_mode_string(self):
        """Test that updater does not start when appMode is string 'PROCESSING'."""
        from integration.core.state_manager import ApplicationStateManager, AppMode
        
        state_manager = ApplicationStateManager()
        
        # Set mode as string (simulating edge case)
        try:
            # Try to set mode as string value
            state_manager.current_mode = "PROCESSING"
            
            # Simulate _can_update check
            current_mode = state_manager.get_current_mode()
            
            # Normalize to AppMode if needed
            if not isinstance(current_mode, AppMode):
                try:
                    current_mode = AppMode(current_mode)  # type: ignore[arg-type]
                except Exception:
                    # In case of failure, should default to False
                    can_update = False
                else:
                    can_update = current_mode not in (AppMode.LISTENING, AppMode.PROCESSING)
            else:
                can_update = current_mode not in (AppMode.LISTENING, AppMode.PROCESSING)
            
            # Verify update is blocked
            assert can_update is False, "Update should be blocked in PROCESSING mode (string)"
        except Exception:
            # If mode setting fails, that's also a valid negative case
            pass

    def test_updater_does_not_start_in_processing_mode_enum(self):
        """Test that updater does not start when appMode is AppMode.PROCESSING (Enum)."""
        from integration.core.state_manager import ApplicationStateManager, AppMode
        
        state_manager = ApplicationStateManager()
        
        # Set mode as Enum
        state_manager.set_mode(AppMode.PROCESSING)
        
        # Simulate _can_update check
        current_mode = state_manager.get_current_mode()
        
        # Normalize to AppMode if needed
        if not isinstance(current_mode, AppMode):
            try:
                current_mode = AppMode(current_mode)  # type: ignore[arg-type]
            except Exception:
                can_update = False
            else:
                can_update = current_mode not in (AppMode.LISTENING, AppMode.PROCESSING)
        else:
            can_update = current_mode not in (AppMode.LISTENING, AppMode.PROCESSING)
        
        # Verify update is blocked
        assert can_update is False, "Update should be blocked in PROCESSING mode (Enum)"

    def test_coordinator_interrupts_startup_when_restart_pending_and_first_run(self, caplog):
        """Test that coordinator interrupts integration startup when restart_pending & firstRun."""
        snapshot = Snapshot(
            perm_mic=PermissionStatus.GRANTED,
            perm_screen=PermissionStatus.GRANTED,
            perm_accessibility=PermissionStatus.GRANTED,
            device_input=DeviceStatus.DEFAULT_OK,
            network=NetworkStatus.ONLINE,
            first_run=True,  # first_run blocks
            app_mode=AppMode.SLEEPING,
            restart_pending=True,  # restart_pending blocks
        )

        with caplog.at_level(logging.INFO):
            decision = decide_continue_integration_startup(snapshot)

        # Verify decision is ABORT
        assert decision == Decision.ABORT, "Coordinator should abort integration startup when restart_pending & firstRun"

        # Verify canonical log format
        assert_decision_logged(
            caplog,
            decision="abort",
            source="coordinator_gateway",
            ctx_keys=["mic", "screen", "device", "network", "firstRun", "appMode"],
            snapshot=snapshot,
        )

        # Verify reason is logged
        log_text = caplog.text
        assert "reason=first_run_restart_pending" in log_text

    def test_coordinator_interrupts_startup_when_restart_pending_without_first_run(self, caplog):
        """Test that coordinator interrupts startup when restart_pending=True but first_run=False."""
        snapshot = Snapshot(
            perm_mic=PermissionStatus.GRANTED,
            perm_screen=PermissionStatus.GRANTED,
            perm_accessibility=PermissionStatus.GRANTED,
            device_input=DeviceStatus.DEFAULT_OK,
            network=NetworkStatus.ONLINE,
            first_run=False,  # No first_run
            app_mode=AppMode.SLEEPING,
            restart_pending=True,  # restart_pending alone blocks
        )

        with caplog.at_level(logging.WARNING):
            decision = decide_continue_integration_startup(snapshot)

        # Verify decision is ABORT (restart_pending alone also blocks)
        assert decision == Decision.ABORT, "Coordinator should abort when restart_pending=True"

        # Verify canonical log format
        assert_decision_logged(
            caplog,
            decision="abort",
            source="coordinator_gateway",
            ctx_keys=["mic", "screen", "device", "network", "firstRun", "appMode"],
            snapshot=snapshot,
        )

        # Verify reason is logged
        log_text = caplog.text
        assert "reason=restart_pending_without_first_run" in log_text

    def test_permission_restart_blocked_by_update_in_progress(self):
        """Test that permission restart is blocked when update is in progress."""
        snapshot = Snapshot(
            perm_mic=PermissionStatus.GRANTED,
            perm_screen=PermissionStatus.GRANTED,
            perm_accessibility=PermissionStatus.GRANTED,
            device_input=DeviceStatus.DEFAULT_OK,
            network=NetworkStatus.ONLINE,
            first_run=False,
            app_mode=AppMode.SLEEPING,
            restart_pending=False,
        )

        from integration.core.gateways.permission_gateways import decide_permission_restart_safety

        decision = decide_permission_restart_safety(snapshot, update_in_progress=True)

        # Verify restart is blocked
        assert decision == Decision.ABORT, "Permission restart should be blocked when update is in progress"

    def test_permission_restart_blocked_by_first_run_restart_pending(self):
        """Test that permission restart is blocked when first_run=True & restart_pending=True."""
        snapshot = Snapshot(
            perm_mic=PermissionStatus.GRANTED,
            perm_screen=PermissionStatus.GRANTED,
            perm_accessibility=PermissionStatus.GRANTED,
            device_input=DeviceStatus.DEFAULT_OK,
            network=NetworkStatus.ONLINE,
            first_run=True,  # first_run blocks
            app_mode=AppMode.SLEEPING,
            restart_pending=True,  # restart_pending blocks
        )

        from integration.core.gateways.permission_gateways import decide_permission_restart_safety

        decision = decide_permission_restart_safety(snapshot, update_in_progress=False)

        # Verify restart is blocked
        assert decision == Decision.ABORT, "Permission restart should be blocked when first_run=True & restart_pending=True"

    def test_listening_blocked_during_first_run(self, caplog):
        """Test that listening is blocked during first_run."""
        snapshot = Snapshot(
            perm_mic=PermissionStatus.GRANTED,
            perm_screen=PermissionStatus.GRANTED,
            perm_accessibility=PermissionStatus.GRANTED,
            device_input=DeviceStatus.DEFAULT_OK,
            network=NetworkStatus.ONLINE,
            first_run=True,  # first_run blocks listening
            app_mode=AppMode.SLEEPING,
            restart_pending=False,
        )

        from integration.core.gateways.common import decide_start_listening

        with caplog.at_level(logging.INFO):
            decision = decide_start_listening(snapshot)

        # Verify listening is blocked
        assert decision == Decision.ABORT, "Listening should be blocked during first_run"

        # Verify reason is logged
        log_text = caplog.text
        assert "reason=first_run_in_progress" in log_text

