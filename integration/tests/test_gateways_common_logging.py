"""
Tests for _log_decision helper function in common gateways.

Tests that logging format is canonical:
decision=<decision> ctx={mic=...,screen=...,device=...,network=...,firstRun=...,appMode=...} source=<domain> duration_ms=<int>
"""

import logging
import re
import pytest

from integration.core.gateways.common import _log_decision
from integration.core.gateways.types import Decision
from integration.core.selectors import (
    Snapshot,
    PermissionStatus,
    DeviceStatus,
    NetworkStatus,
    AppMode,
)


class TestLogDecisionFormat:
    """Test that _log_decision produces canonical format logs."""

    def test_logs_all_required_context_keys(self, caplog):
        """Test that log includes all required context keys."""
        snapshot = Snapshot(
            perm_mic=PermissionStatus.GRANTED,
            perm_screen=PermissionStatus.GRANTED,
            perm_accessibility=PermissionStatus.GRANTED,
            device_input=DeviceStatus.DEFAULT_OK,
            network=NetworkStatus.ONLINE,
            first_run=False,
            app_mode=AppMode.SLEEPING,
        )

        with caplog.at_level(logging.DEBUG):
            _log_decision(
                level="debug",
                decision=Decision.START,
                s=snapshot,
                source="test_gateway",
            )

        log_text = caplog.text

        # Check canonical format pattern
        pattern = r"decision=start\s+ctx=\{mic=.*?,screen=.*?,device=.*?,network=.*?,firstRun=.*?,appMode=.*?\}\s+source=test_gateway"
        assert re.search(pattern, log_text), f"Log does not match canonical format: {log_text}"

        # Verify all required keys are present
        assert "mic=" in log_text
        assert "screen=" in log_text
        assert "device=" in log_text
        assert "network=" in log_text
        assert "firstRun=" in log_text
        assert "appMode=" in log_text

    def test_logs_with_reason(self, caplog):
        """Test that log includes reason when provided."""
        snapshot = Snapshot(
            perm_mic=PermissionStatus.DENIED,
            perm_screen=PermissionStatus.GRANTED,
            perm_accessibility=PermissionStatus.GRANTED,
            device_input=DeviceStatus.DEFAULT_OK,
            network=NetworkStatus.ONLINE,
            first_run=False,
            app_mode=AppMode.SLEEPING,
        )

        with caplog.at_level(logging.DEBUG):
            _log_decision(
                level="info",
                decision=Decision.ABORT,
                s=snapshot,
                source="test_gateway",
                reason="test_reason",
            )

        log_text = caplog.text

        # Check that reason is included
        assert "reason=test_reason" in log_text
        pattern = r"decision=abort\s+reason=test_reason\s+ctx=\{[^}]+\}\s+source=test_gateway"
        assert re.search(pattern, log_text), f"Log with reason does not match format: {log_text}"

    def test_logs_with_duration_ms(self, caplog):
        """Test that log includes duration_ms when provided."""
        snapshot = Snapshot(
            perm_mic=PermissionStatus.GRANTED,
            perm_screen=PermissionStatus.GRANTED,
            perm_accessibility=PermissionStatus.GRANTED,
            device_input=DeviceStatus.DEFAULT_OK,
            network=NetworkStatus.ONLINE,
            first_run=False,
            app_mode=AppMode.LISTENING,
        )

        with caplog.at_level(logging.DEBUG):
            _log_decision(
                level="debug",
                decision=Decision.START,
                s=snapshot,
                source="test_gateway",
                duration_ms=150,
            )

        log_text = caplog.text

        # Check that duration_ms is included
        assert "duration_ms=150" in log_text
        pattern = r"decision=start\s+ctx=\{[^}]+\}\s+source=test_gateway\s+duration_ms=150"
        assert re.search(pattern, log_text), f"Log with duration does not match format: {log_text}"

    def test_logs_with_reason_and_duration(self, caplog):
        """Test that log includes both reason and duration_ms."""
        snapshot = Snapshot(
            perm_mic=PermissionStatus.GRANTED,
            perm_screen=PermissionStatus.GRANTED,
            perm_accessibility=PermissionStatus.GRANTED,
            device_input=DeviceStatus.BUSY,
            network=NetworkStatus.OFFLINE,
            first_run=True,
            app_mode=AppMode.PROCESSING,
        )

        with caplog.at_level(logging.INFO):
            _log_decision(
                level="info",
                decision=Decision.RETRY,
                s=snapshot,
                source="test_gateway",
                reason="device_busy",
                duration_ms=250,
            )

        log_text = caplog.text

        # Check both reason and duration are included
        assert "reason=device_busy" in log_text
        assert "duration_ms=250" in log_text

        # Verify context values match snapshot
        assert f"mic={snapshot.perm_mic.value}" in log_text
        assert f"screen={snapshot.perm_screen.value}" in log_text
        assert f"device={snapshot.device_input.value}" in log_text
        assert f"network={snapshot.network.value}" in log_text
        assert f"firstRun={snapshot.first_run}" in log_text
        assert f"appMode={snapshot.app_mode.value}" in log_text

    def test_logs_string_decision(self, caplog):
        """Test that log accepts string decision value."""
        snapshot = Snapshot(
            perm_mic=PermissionStatus.GRANTED,
            perm_screen=PermissionStatus.GRANTED,
            perm_accessibility=PermissionStatus.GRANTED,
            device_input=DeviceStatus.DEFAULT_OK,
            network=NetworkStatus.ONLINE,
            first_run=False,
            app_mode=AppMode.SLEEPING,
        )

        with caplog.at_level(logging.DEBUG):
            _log_decision(
                level="debug",
                decision="start",  # String instead of Decision enum
                s=snapshot,
                source="test_gateway",
            )

        log_text = caplog.text

        # Check that string decision is logged correctly
        assert "decision=start" in log_text

    def test_logs_correct_level(self, caplog):
        """Test that log uses correct logging level."""
        snapshot = Snapshot(
            perm_mic=PermissionStatus.GRANTED,
            perm_screen=PermissionStatus.GRANTED,
            perm_accessibility=PermissionStatus.GRANTED,
            device_input=DeviceStatus.DEFAULT_OK,
            network=NetworkStatus.ONLINE,
            first_run=False,
            app_mode=AppMode.SLEEPING,
        )

        with caplog.at_level(logging.WARNING):
            _log_decision(
                level="warning",
                decision=Decision.ABORT,
                s=snapshot,
                source="test_gateway",
                reason="critical_error",
            )

        # Check that log was written at warning level
        assert len(caplog.records) > 0
        assert caplog.records[0].levelname == "WARNING"

