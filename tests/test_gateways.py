"""
Tests for integration/core/gateways.py

Tests decision-making logic with pairwise combinations of state axes.
Ensures decision logs follow canonical format (see .cursorrules section 8.x).

Decision log format:
decision=<start|abort|retry|degrade> ctx={mic=...,screen=...,device=...,network=...,firstRun=...,appMode=...} source=<domain> duration_ms=<int>
"""

import logging
from unittest.mock import Mock, patch

import pytest

from integration.core.gateways import (
    Decision,
    decide_process_audio,
    decide_start_listening,
    decide_with_backoff,
)
from integration.core.selectors import (
    AppMode,
    DeviceStatus,
    NetworkStatus,
    PermissionStatus,
    Snapshot,
)
from integration.tests.helpers.logging_asserts import assert_decision_logged


class TestGatewayDecisionLogs:
    """Test that all gateways log decisions in canonical format."""

    def test_decide_start_listening_logs_on_abort(self, caplog):
        """Test that decide_start_listening logs ABORT decision with canonical format."""
        with caplog.at_level(logging.DEBUG):
            snapshot = Snapshot(
                perm_mic=PermissionStatus.DENIED,
                perm_screen=PermissionStatus.GRANTED,
                perm_accessibility=PermissionStatus.GRANTED,
                device_input=DeviceStatus.DEFAULT_OK,
                network=NetworkStatus.ONLINE,
                first_run=False,
                app_mode=AppMode.SLEEPING,
            )
            decision = decide_start_listening(snapshot)
            assert decision == Decision.ABORT

            # Use helper to check canonical format
            assert_decision_logged(
                caplog,
                decision="abort",
                source="listening_gateway",
                ctx_keys=["mic", "device", "network"],
                snapshot=snapshot,
            )

    def test_decide_start_listening_logs_on_start(self, caplog):
        """Test that decide_start_listening logs START decision with canonical format."""
        with caplog.at_level(logging.DEBUG):
            snapshot = Snapshot(
                perm_mic=PermissionStatus.GRANTED,
                perm_screen=PermissionStatus.GRANTED,
                perm_accessibility=PermissionStatus.GRANTED,
                device_input=DeviceStatus.DEFAULT_OK,
                network=NetworkStatus.ONLINE,
                first_run=False,
                app_mode=AppMode.SLEEPING,
            )
            decision = decide_start_listening(snapshot)
            assert decision == Decision.START

            # Use helper to check canonical format
            assert_decision_logged(
                caplog,
                decision="start",
                source="listening_gateway",
                ctx_keys=["mic", "device", "network", "appMode"],
                snapshot=snapshot,
            )

    def test_decide_process_audio_logs_on_abort(self, caplog):
        """Test that decide_process_audio logs ABORT decision with canonical format."""
        with caplog.at_level(logging.DEBUG):
            snapshot = Snapshot(
                perm_mic=PermissionStatus.DENIED,
                perm_screen=PermissionStatus.GRANTED,
                perm_accessibility=PermissionStatus.GRANTED,
                device_input=DeviceStatus.DEFAULT_OK,
                network=NetworkStatus.ONLINE,
                first_run=False,
                app_mode=AppMode.PROCESSING,
            )
            decision = decide_process_audio(snapshot)
            assert decision == Decision.ABORT

            # Check canonical format
            logs = caplog.text
            assert "decision=abort" in logs
            assert "ctx={" in logs
            assert "source=processing_gateway" in logs

    def test_decide_with_backoff_logs_on_retry(self, caplog):
        """Test that decide_with_backoff logs RETRY decision with canonical format."""
        with caplog.at_level(logging.DEBUG):
            snapshot = Snapshot(
                perm_mic=PermissionStatus.GRANTED,
                perm_screen=PermissionStatus.GRANTED,
                perm_accessibility=PermissionStatus.GRANTED,
                device_input=DeviceStatus.BUSY,
                network=NetworkStatus.ONLINE,
                first_run=False,
                app_mode=AppMode.LISTENING,
            )
            decision = decide_with_backoff(snapshot, retry_count=1, max_retries=3)
            assert decision == Decision.RETRY

            # Check canonical format
            logs = caplog.text
            assert "decision=retry" in logs
            assert "ctx={" in logs
            assert "source=backoff_gateway" in logs


class TestGatewayPairwiseCombinations:
    """Pairwise tests for gateway decision logic.

    Covers combinations from interaction_matrix.yaml:
    - ≥8–14 pairwise combinations
    - 2+ negative cases
    """

    @pytest.mark.parametrize(
        "perm_mic,perm_screen,device,network,first_run,app_mode,expected_decision",
        [
            # Hard stop: mic denied
            (
                PermissionStatus.DENIED,
                PermissionStatus.GRANTED,
                DeviceStatus.DEFAULT_OK,
                NetworkStatus.ONLINE,
                False,
                AppMode.SLEEPING,
                Decision.ABORT,
            ),
            # Hard stop: first_run blocks activation
            (
                PermissionStatus.GRANTED,
                PermissionStatus.GRANTED,
                DeviceStatus.DEFAULT_OK,
                NetworkStatus.ONLINE,
                True,  # first_run blocks
                AppMode.SLEEPING,
                Decision.ABORT,
            ),
            # Graceful: device busy
            (
                PermissionStatus.GRANTED,
                PermissionStatus.GRANTED,
                DeviceStatus.BUSY,
                NetworkStatus.ONLINE,
                False,
                AppMode.LISTENING,
                Decision.RETRY,
            ),
            # Graceful: network offline (can still listen)
            (
                PermissionStatus.GRANTED,
                PermissionStatus.GRANTED,
                DeviceStatus.DEFAULT_OK,
                NetworkStatus.OFFLINE,
                False,
                AppMode.LISTENING,
                Decision.DEGRADE,
            ),
            # Start: all conditions met
            (
                PermissionStatus.GRANTED,
                PermissionStatus.GRANTED,
                DeviceStatus.DEFAULT_OK,
                NetworkStatus.ONLINE,
                False,
                AppMode.SLEEPING,
                Decision.START,
            ),
            # Processing: screen denied
            (
                PermissionStatus.GRANTED,
                PermissionStatus.DENIED,
                DeviceStatus.DEFAULT_OK,
                NetworkStatus.ONLINE,
                False,
                AppMode.PROCESSING,
                Decision.ABORT,
            ),
            # Processing: network offline
            (
                PermissionStatus.GRANTED,
                PermissionStatus.GRANTED,
                DeviceStatus.DEFAULT_OK,
                NetworkStatus.OFFLINE,
                False,
                AppMode.PROCESSING,
                Decision.DEGRADE,
            ),
            # Processing: all conditions met
            (
                PermissionStatus.GRANTED,
                PermissionStatus.GRANTED,
                DeviceStatus.DEFAULT_OK,
                NetworkStatus.ONLINE,
                False,
                AppMode.PROCESSING,
                Decision.START,
            ),
        ],
    )
    def test_decide_start_listening_pairwise(
        self, perm_mic, perm_screen, device, network, first_run, app_mode, expected_decision, caplog
    ):
        """Pairwise test for decide_start_listening with various state combinations."""
        snapshot = Snapshot(
            perm_mic=perm_mic,
            perm_screen=perm_screen,
            perm_accessibility=PermissionStatus.GRANTED,
            device_input=device,
            network=network,
            first_run=first_run,
            app_mode=app_mode,
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
        "perm_mic,network,app_mode,expected_decision",
        [
            # Negative: mic denied
            (PermissionStatus.DENIED, NetworkStatus.ONLINE, AppMode.PROCESSING, Decision.ABORT),
            # Negative: network offline
            (PermissionStatus.GRANTED, NetworkStatus.OFFLINE, AppMode.PROCESSING, Decision.DEGRADE),
            # Positive: all conditions met
            (PermissionStatus.GRANTED, NetworkStatus.ONLINE, AppMode.PROCESSING, Decision.START),
        ],
    )
    def test_decide_process_audio_negative_cases(
        self, perm_mic, network, app_mode, expected_decision, caplog
    ):
        """Negative cases for decide_process_audio."""
        snapshot = Snapshot(
            perm_mic=perm_mic,
            perm_screen=PermissionStatus.GRANTED,
            perm_accessibility=PermissionStatus.GRANTED,
            device_input=DeviceStatus.DEFAULT_OK,
            network=network,
            first_run=False,
            app_mode=app_mode,
        )
        with caplog.at_level(logging.DEBUG):
            decision = decide_process_audio(snapshot)
            assert decision == expected_decision

            # Verify decision log in canonical format
            logs = caplog.text
            assert "decision=" in logs
            assert "ctx={" in logs
            assert "source=processing_gateway" in logs

    def test_decide_with_backoff_max_retries(self, caplog):
        """Test that max retries leads to ABORT."""
        snapshot = Snapshot(
            perm_mic=PermissionStatus.GRANTED,
            perm_screen=PermissionStatus.GRANTED,
            perm_accessibility=PermissionStatus.GRANTED,
            device_input=DeviceStatus.BUSY,
            network=NetworkStatus.ONLINE,
            first_run=False,
            app_mode=AppMode.LISTENING,
        )
        with caplog.at_level(logging.DEBUG):
            decision = decide_with_backoff(snapshot, retry_count=3, max_retries=3)
            assert decision == Decision.ABORT

            # Verify decision log in canonical format
            logs = caplog.text
            assert "decision=abort" in logs
            assert "ctx={" in logs
            assert "source=backoff_gateway" in logs

