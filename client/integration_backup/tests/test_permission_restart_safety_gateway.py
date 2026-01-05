"""
Tests for decide_permission_restart_safety gateway.

Tests the three main decision paths:
- update_in_progress=True → ABORT (graceful)
- first_run & restart_pending=True → ABORT (hard_stop)
- otherwise → START
"""

import logging
import re
import pytest

from integration.core.gateways.permission_gateways import decide_permission_restart_safety
from integration.core.gateways.types import Decision
from integration.core.selectors import (
    Snapshot,
    PermissionStatus,
    DeviceStatus,
    NetworkStatus,
    AppMode,
)
from integration.tests.helpers.logging_asserts import assert_decision_logged


class TestDecidePermissionRestartSafety:
    """Test decide_permission_restart_safety gateway."""

    def test_update_in_progress_aborts(self, caplog):
        """Test that update_in_progress=True returns ABORT with graceful reason."""
        snapshot = Snapshot(
            perm_mic=PermissionStatus.GRANTED,
            perm_screen=PermissionStatus.GRANTED,
            perm_accessibility=PermissionStatus.GRANTED,
            device_input=DeviceStatus.DEFAULT_OK,
            network=NetworkStatus.ONLINE,
            first_run=False,
            app_mode=AppMode.SLEEPING,
            restart_pending=False,
            update_in_progress=True,  # update_in_progress blocks
        )

        with caplog.at_level(logging.INFO):
            decision = decide_permission_restart_safety(snapshot)

        assert decision == Decision.ABORT

        # Verify canonical log format with reason
        assert_decision_logged(
            caplog,
            decision="abort",
            source="permission_restart_gateway",
            ctx_keys=["mic", "screen", "device", "network", "firstRun", "appMode"],
            snapshot=snapshot,
        )

        # Verify reason is logged
        log_text = caplog.text
        assert "reason=update_in_progress" in log_text

    def test_first_run_restart_pending_aborts(self, caplog):
        """Test that first_run & restart_pending returns ABORT with hard_stop reason."""
        snapshot = Snapshot(
            perm_mic=PermissionStatus.GRANTED,
            perm_screen=PermissionStatus.GRANTED,
            perm_accessibility=PermissionStatus.GRANTED,
            device_input=DeviceStatus.DEFAULT_OK,
            network=NetworkStatus.ONLINE,
            first_run=True,  # first_run blocks
            app_mode=AppMode.SLEEPING,
            restart_pending=True,  # restart_pending blocks
            update_in_progress=False,
        )

        with caplog.at_level(logging.INFO):
            decision = decide_permission_restart_safety(snapshot)

        assert decision == Decision.ABORT

        # Verify canonical log format
        assert_decision_logged(
            caplog,
            decision="abort",
            source="permission_restart_gateway",
            ctx_keys=["mic", "screen", "device", "network", "firstRun", "appMode"],
            snapshot=snapshot,
        )

        # Verify reason is logged
        log_text = caplog.text
        assert "reason=first_run_restart_pending" in log_text

    def test_all_conditions_met_starts(self, caplog):
        """Test that when all conditions are met, returns START."""
        snapshot = Snapshot(
            perm_mic=PermissionStatus.GRANTED,
            perm_screen=PermissionStatus.GRANTED,
            perm_accessibility=PermissionStatus.GRANTED,
            device_input=DeviceStatus.DEFAULT_OK,
            network=NetworkStatus.ONLINE,
            first_run=False,
            app_mode=AppMode.SLEEPING,
            restart_pending=False,
            update_in_progress=False,
        )

        with caplog.at_level(logging.DEBUG):
            decision = decide_permission_restart_safety(snapshot)

        assert decision == Decision.START

        # Verify canonical log format (no reason for START)
        assert_decision_logged(
            caplog,
            decision="start",
            source="permission_restart_gateway",
            ctx_keys=["mic", "screen", "device", "network", "firstRun", "appMode"],
            snapshot=snapshot,
        )

    def test_update_in_progress_takes_precedence(self, caplog):
        """Test that update_in_progress takes precedence over other conditions."""
        snapshot = Snapshot(
            perm_mic=PermissionStatus.GRANTED,
            perm_screen=PermissionStatus.GRANTED,
            perm_accessibility=PermissionStatus.GRANTED,
            device_input=DeviceStatus.DEFAULT_OK,
            network=NetworkStatus.ONLINE,
            first_run=False,  # Would allow START if not for update_in_progress
            app_mode=AppMode.SLEEPING,
            restart_pending=False,
            update_in_progress=True,  # update_in_progress blocks
        )

        with caplog.at_level(logging.INFO):
            decision = decide_permission_restart_safety(snapshot)

        assert decision == Decision.ABORT
        assert "reason=update_in_progress" in caplog.text

    def test_first_run_restart_pending_takes_precedence_over_update(self, caplog):
        """Test that first_run_restart_pending takes precedence over update_in_progress."""
        snapshot = Snapshot(
            perm_mic=PermissionStatus.GRANTED,
            perm_screen=PermissionStatus.GRANTED,
            perm_accessibility=PermissionStatus.GRANTED,
            device_input=DeviceStatus.DEFAULT_OK,
            network=NetworkStatus.ONLINE,
            first_run=True,
            app_mode=AppMode.SLEEPING,
            restart_pending=True,
            update_in_progress=True,  # Both conditions are true, but first_run_restart_pending should be checked first
        )

        with caplog.at_level(logging.INFO):
            decision = decide_permission_restart_safety(snapshot)

        assert decision == Decision.ABORT
        assert "reason=first_run_restart_pending" in caplog.text

    def test_log_format_is_canonical(self, caplog):
        """Test that all logs follow canonical format exactly."""
        snapshot = Snapshot(
            perm_mic=PermissionStatus.GRANTED,
            perm_screen=PermissionStatus.DENIED,
            perm_accessibility=PermissionStatus.GRANTED,
            device_input=DeviceStatus.BUSY,
            network=NetworkStatus.OFFLINE,
            first_run=True,
            app_mode=AppMode.PROCESSING,
            restart_pending=True,
            update_in_progress=False,
        )

        with caplog.at_level(logging.INFO):
            decide_permission_restart_safety(snapshot)

        log_text = caplog.text

        # Verify canonical format with regex
        # Note: appMode values are lowercase (sleeping/listening/processing) from AppMode enum
        # New axes (restart_pending, update_in_progress) are optional and may be present in logs
        pattern = r"decision=(start|abort)\s+(reason=\w+\s+)?ctx=\{mic=(granted|denied|prompt_blocked),screen=(granted|denied|prompt_blocked),device=(default_ok|busy),network=(online|offline),firstRun=(True|False),appMode=(sleeping|listening|processing)(?:,restart_pending=(True|False))?(?:,update_in_progress=(True|False))?\}\s+source=permission_restart_gateway"
        assert re.search(pattern, log_text), f"Log does not match canonical format: {log_text}"

        # Verify all context values are present
        assert f"mic={snapshot.perm_mic.value}" in log_text
        assert f"screen={snapshot.perm_screen.value}" in log_text
        assert f"device={snapshot.device_input.value}" in log_text
        assert f"network={snapshot.network.value}" in log_text
        assert f"firstRun={snapshot.first_run}" in log_text
        assert f"appMode={snapshot.app_mode.value}" in log_text
        # New axes may be present in logs (restart_pending, update_in_progress)
        if hasattr(snapshot, 'restart_pending'):
            assert f"restart_pending={snapshot.restart_pending}" in log_text
        if hasattr(snapshot, 'update_in_progress'):
            assert f"update_in_progress={snapshot.update_in_progress}" in log_text
