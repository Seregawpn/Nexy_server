"""
Integration tests for coordinator restart_pending gateway.

Tests that:
- decide_continue_integration_startup returns ABORT when firstRun=True & restart_pending=True
- Logs follow canonical format
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


class TestCoordinatorRestartPendingGate:
    """Test that coordinator blocks integration startup when restart is pending."""

    def test_decide_continue_integration_startup_aborts_when_restart_pending(self, caplog):
        """Test that gateway returns ABORT when firstRun=True & restart_pending=True."""
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

        assert decision == Decision.ABORT

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

    def test_decide_continue_integration_startup_starts_when_no_restart_pending(self, caplog):
        """Test that gateway returns START when restart_pending=False."""
        snapshot = Snapshot(
            perm_mic=PermissionStatus.GRANTED,
            perm_screen=PermissionStatus.GRANTED,
            perm_accessibility=PermissionStatus.GRANTED,
            device_input=DeviceStatus.DEFAULT_OK,
            network=NetworkStatus.ONLINE,
            first_run=False,
            app_mode=AppMode.SLEEPING,
            restart_pending=False,  # No restart pending
        )

        with caplog.at_level(logging.DEBUG):
            decision = decide_continue_integration_startup(snapshot)

        assert decision == Decision.START

        # Verify canonical log format
        assert_decision_logged(
            caplog,
            decision="start",
            source="coordinator_gateway",
            ctx_keys=["mic", "screen", "device", "network", "firstRun", "appMode"],
            snapshot=snapshot,
        )

    def test_log_format_is_canonical(self, caplog):
        """Test that logs follow canonical format exactly."""
        snapshot = Snapshot(
            perm_mic=PermissionStatus.GRANTED,
            perm_screen=PermissionStatus.DENIED,
            perm_accessibility=PermissionStatus.GRANTED,
            device_input=DeviceStatus.BUSY,
            network=NetworkStatus.OFFLINE,
            first_run=True,
            app_mode=AppMode.PROCESSING,
            restart_pending=True,
        )

        with caplog.at_level(logging.INFO):
            decide_continue_integration_startup(snapshot)

        log_text = caplog.text

        # Verify canonical format with regex
        import re
        # Note: appMode values are lowercase (sleeping/listening/processing) from AppMode enum
        pattern = r"decision=abort\s+reason=first_run_restart_pending\s+ctx=\{mic=(granted|denied|prompt_blocked),screen=(granted|denied|prompt_blocked),device=(default_ok|busy),network=(online|offline),firstRun=(True|False),appMode=(sleeping|listening|processing)\}\s+source=coordinator_gateway(\s+duration_ms=\d+)?"
        assert re.search(pattern, log_text), f"Log does not match canonical format: {log_text}"

        # Verify all context values are present
        assert f"mic={snapshot.perm_mic.value}" in log_text
        assert f"screen={snapshot.perm_screen.value}" in log_text
        assert f"device={snapshot.device_input.value}" in log_text
        assert f"network={snapshot.network.value}" in log_text
        assert f"firstRun={snapshot.first_run}" in log_text
        assert f"appMode={snapshot.app_mode.value}" in log_text

