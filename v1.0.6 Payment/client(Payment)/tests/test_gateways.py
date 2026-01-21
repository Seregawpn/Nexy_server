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
from integration.core.gateways.permission_gateways import decide_permission_restart_safety
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
            # Processing: cannot start listening (must be in SLEEPING/LISTENING)
            (
                PermissionStatus.GRANTED,
                PermissionStatus.GRANTED,
                DeviceStatus.DEFAULT_OK,
                NetworkStatus.ONLINE,
                False,
                AppMode.PROCESSING,
                Decision.ABORT,  # PROCESSING mode blocks start_listening
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


class TestPermissionRestartGateway:
    """Tests for decide_permission_restart_safety gateway.
    
    Tests update_in_progress axis blocking permission restart (graceful).
    See STATE_CATALOG.md section 10 for update_in_progress rules.
    """

    def test_decide_permission_restart_safety_blocks_on_update_in_progress(self, caplog):
        """Test that decide_permission_restart_safety blocks restart when update_in_progress=true.
        
        This is a graceful block (not hard_stop) - restart is delayed until update completes.
        See STATE_CATALOG.md section 10 and interaction_matrix.yaml.
        """
        with caplog.at_level(logging.DEBUG):
            snapshot = Snapshot(
                perm_mic=PermissionStatus.GRANTED,
                perm_screen=PermissionStatus.GRANTED,
                perm_accessibility=PermissionStatus.GRANTED,
                device_input=DeviceStatus.DEFAULT_OK,
                network=NetworkStatus.ONLINE,
                first_run=False,
                app_mode=AppMode.SLEEPING,
                restart_pending=False,
                update_in_progress=True,  # Update in progress blocks restart
            )
            decision = decide_permission_restart_safety(snapshot)
            assert decision == Decision.ABORT

            # Verify decision log in canonical format with update_in_progress
            assert_decision_logged(
                caplog,
                decision="abort",
                source="permission_restart_gateway",
                ctx_keys=["mic", "screen", "device", "network", "firstRun", "appMode", "update_in_progress"],
                snapshot=snapshot,
            )
            
            # Verify reason is logged
            logs = caplog.text
            assert "reason=update_in_progress" in logs

    def test_decide_permission_restart_safety_allows_when_update_not_in_progress(self, caplog):
        """Test that decide_permission_restart_safety allows restart when update_in_progress=false.
        
        Happy path: no update in progress, restart is safe.
        """
        with caplog.at_level(logging.DEBUG):
            snapshot = Snapshot(
                perm_mic=PermissionStatus.GRANTED,
                perm_screen=PermissionStatus.GRANTED,
                perm_accessibility=PermissionStatus.GRANTED,
                device_input=DeviceStatus.DEFAULT_OK,
                network=NetworkStatus.ONLINE,
                first_run=False,
                app_mode=AppMode.SLEEPING,
                restart_pending=False,
                update_in_progress=False,  # No update - restart is safe
            )
            decision = decide_permission_restart_safety(snapshot)
            assert decision == Decision.START

            # Verify decision log in canonical format
            assert_decision_logged(
                caplog,
                decision="start",
                source="permission_restart_gateway",
                ctx_keys=["mic", "screen", "device", "network", "firstRun", "appMode", "update_in_progress"],
                snapshot=snapshot,
            )

    def test_decide_permission_restart_safety_blocks_on_first_run_restart_pending(self, caplog):
        """Test that decide_permission_restart_safety blocks restart when first_run_restart_pending=true.
        
        This is a hard_stop - first_run restart pending blocks all restarts.
        See STATE_CATALOG.md section 8 and interaction_matrix.yaml.
        """
        with caplog.at_level(logging.DEBUG):
            snapshot = Snapshot(
                perm_mic=PermissionStatus.GRANTED,
                perm_screen=PermissionStatus.GRANTED,
                perm_accessibility=PermissionStatus.GRANTED,
                device_input=DeviceStatus.DEFAULT_OK,
                network=NetworkStatus.ONLINE,
                first_run=True,  # First run
                app_mode=AppMode.SLEEPING,
                restart_pending=True,  # Restart pending blocks all restarts
                update_in_progress=False,
            )
            decision = decide_permission_restart_safety(snapshot)
            assert decision == Decision.ABORT

            # Verify decision log in canonical format
            assert_decision_logged(
                caplog,
                decision="abort",
                source="permission_restart_gateway",
                ctx_keys=["mic", "screen", "device", "network", "firstRun", "appMode", "restart_pending"],
                snapshot=snapshot,
            )
            
            # Verify reason is logged
            logs = caplog.text
            assert "reason=first_run_restart_pending" in logs


class TestPermissionRestartWithUpdates:
    """Tests for permission-restart rules with updates.
    
    Covers scenarios from interaction_matrix.yaml:
    - update_available=true + respect_updates=true → restart blocked (hard_stop)
    - update_in_progress=true → restart delayed (graceful, ≤10 minutes)
    - appMode!=SLEEPING + respect_active_sessions=true → delay until window
    """
    
    def test_restart_blocked_when_update_available(self, caplog):
        """Test that restart is blocked when update_available=true and respect_updates=true.
        
        Rule: respect_updates: true + update_available: true → skip_restart (hard_stop)
        See interaction_matrix.yaml and STATE_CATALOG.md.
        """
        from integration.core.gateways.permission_gateways import PermissionRestartGateway, PermissionRestartDecision
        from modules.permission_restart.core.config import PermissionRestartConfig
        from modules.permissions.core.types import PermissionType
        from unittest.mock import Mock
        
        # Mock updater with update_available=True
        updater_mock = Mock()
        updater_mock.is_update_available = lambda: True
        
        gateway = PermissionRestartGateway(
            state_manager=Mock(),
            updater_integration=updater_mock,
        )
        
        config = PermissionRestartConfig(
            enabled=True,
            respect_updates=True,  # Critical: respect_updates must be True
            respect_active_sessions=True,
            max_restart_attempts=3,
            restart_delay_sec=5.0,
        )
        
        decision = gateway.evaluate(
            pending_permissions=[PermissionType.MICROPHONE],
            config=config,
            attempts=1,
            is_first_run=False,
        )
        
        # Should be blocked by update_available
        assert not decision.allowed, \
            "Restart should be blocked when update_available=true and respect_updates=true"
        assert decision.blocked_by == "update_available", \
            f"Decision should be blocked_by='update_available', got '{decision.blocked_by}'"
    
    def test_restart_delayed_when_update_in_progress(self, caplog):
        """Test that restart is delayed when update_in_progress=true.
        
        Rule: update_in_progress: true → abort_permission_restart (graceful)
        See interaction_matrix.yaml and STATE_CATALOG.md section 10.
        """
        from integration.core.gateways.permission_gateways import decide_permission_restart_safety
        from integration.core.selectors import Snapshot, PermissionStatus, DeviceStatus, NetworkStatus, AppMode
        
        snapshot = Snapshot(
            perm_mic=PermissionStatus.GRANTED,
            perm_screen=PermissionStatus.GRANTED,
            perm_accessibility=PermissionStatus.GRANTED,
            device_input=DeviceStatus.DEFAULT_OK,
            network=NetworkStatus.ONLINE,
            first_run=False,
            app_mode=AppMode.SLEEPING,
            restart_pending=False,
            update_in_progress=True,  # Update in progress blocks restart
        )
        
        decision = decide_permission_restart_safety(snapshot)
        
        # Should be aborted (graceful block)
        assert decision == Decision.ABORT, \
            "Restart should be aborted when update_in_progress=true"
        
        # Verify decision log
        assert_decision_logged(
            caplog,
            decision="abort",
            source="permission_restart_gateway",
            ctx_keys=["update_in_progress"],
            snapshot=snapshot,
        )
        
        logs = caplog.text
        assert "reason=update_in_progress" in logs
    
    def test_restart_delayed_when_active_session(self, caplog):
        """Test that restart is delayed when appMode!=SLEEPING and respect_active_sessions=true.
        
        Rule: respect_active_sessions: true + appMode != SLEEPING → delay_restart (graceful)
        See interaction_matrix.yaml.
        """
        from integration.core.gateways.permission_gateways import PermissionRestartGateway, PermissionRestartDecision
        from modules.permission_restart.core.config import PermissionRestartConfig
        from modules.permissions.core.types import PermissionType
        from unittest.mock import Mock
        
        gateway = PermissionRestartGateway(
            state_manager=Mock(),
            updater_integration=Mock(),
        )
        
        # Mock is_idle_mode to return False (active session)
        gateway.is_idle_mode = lambda: False
        
        config = PermissionRestartConfig(
            enabled=True,
            respect_updates=True,
            respect_active_sessions=True,  # Critical: respect_active_sessions must be True
            max_restart_attempts=3,
            restart_delay_sec=5.0,
        )
        
        decision = gateway.evaluate(
            pending_permissions=[PermissionType.MICROPHONE],
            config=config,
            attempts=1,
            is_first_run=False,  # Not first run
        )
        
        # Should require idle (delay restart)
        assert decision.requires_idle, \
            "Restart should require idle mode when active session and respect_active_sessions=true"
        assert decision.allowed, \
            "Restart should be allowed but delayed (not blocked)"
    
    def test_restart_allowed_when_all_conditions_met(self, caplog):
        """Test that restart is allowed when all conditions are met.
        
        Happy path: no update, idle mode, no active sessions.
        """
        from integration.core.gateways.permission_gateways import decide_permission_restart_safety
        from integration.core.selectors import Snapshot, PermissionStatus, DeviceStatus, NetworkStatus, AppMode
        
        snapshot = Snapshot(
            perm_mic=PermissionStatus.GRANTED,
            perm_screen=PermissionStatus.GRANTED,
            perm_accessibility=PermissionStatus.GRANTED,
            device_input=DeviceStatus.DEFAULT_OK,
            network=NetworkStatus.ONLINE,
            first_run=False,
            app_mode=AppMode.SLEEPING,  # Idle mode
            restart_pending=False,
            update_in_progress=False,  # No update
        )
        
        decision = decide_permission_restart_safety(snapshot)
        
        # Should be allowed
        assert decision == Decision.START, \
            "Restart should be allowed when all conditions are met"
        
        # Verify decision log
        assert_decision_logged(
            caplog,
            decision="start",
            source="permission_restart_gateway",
            ctx_keys=["update_in_progress"],
            snapshot=snapshot,
        )


class TestDecisionLogFormatValidation:
    """Test that decision log format validation fails when format is violated.
    
    These tests ensure that assert_decision_logged() correctly fails when:
    - Decision log is missing
    - Format is incorrect
    - Context keys are missing
    - Snapshot values don't match
    """
    
    def test_assert_decision_logged_fails_when_log_missing(self, caplog):
        """Test that assert_decision_logged fails when decision log is missing."""
        from integration.tests.helpers.logging_asserts import assert_decision_logged
        from integration.core.selectors import Snapshot, PermissionStatus, DeviceStatus, NetworkStatus, AppMode
        
        snapshot = Snapshot(
            perm_mic=PermissionStatus.GRANTED,
            perm_screen=PermissionStatus.GRANTED,
            perm_accessibility=PermissionStatus.GRANTED,
            device_input=DeviceStatus.DEFAULT_OK,
            network=NetworkStatus.ONLINE,
            first_run=False,
            app_mode=AppMode.SLEEPING,
        )
        
        # No log written - should fail
        with pytest.raises(AssertionError, match="Decision log not found"):
            assert_decision_logged(
                caplog,
                decision="start",
                source="test_gateway",
                ctx_keys=["mic", "device"],
                snapshot=snapshot,
            )
    
    def test_assert_decision_logged_fails_when_format_wrong(self, caplog):
        """Test that assert_decision_logged fails when format is incorrect."""
        from integration.tests.helpers.logging_asserts import assert_decision_logged
        import logging
        
        logger = logging.getLogger("test")
        # Write log in wrong format (missing ctx=)
        logger.info("decision=start source=test_gateway")
        
        with pytest.raises(AssertionError, match="Decision log not found"):
            assert_decision_logged(
                caplog,
                decision="start",
                source="test_gateway",
            )
    
    def test_assert_decision_logged_fails_when_context_key_missing(self, caplog):
        """Test that assert_decision_logged fails when required context key is missing."""
        from integration.tests.helpers.logging_asserts import assert_decision_logged
        import logging
        
        logger = logging.getLogger("test")
        # Write log missing "mic" key
        logger.info("decision=start ctx={screen=granted,device=default_ok} source=test_gateway")
        
        with pytest.raises(AssertionError, match="Context key 'mic' not found"):
            assert_decision_logged(
                caplog,
                decision="start",
                source="test_gateway",
                ctx_keys=["mic", "screen", "device"],
            )
    
    def test_assert_decision_logged_fails_when_snapshot_value_mismatch(self, caplog):
        """Test that assert_decision_logged fails when snapshot value doesn't match log."""
        from integration.tests.helpers.logging_asserts import assert_decision_logged
        from integration.core.selectors import Snapshot, PermissionStatus, DeviceStatus, NetworkStatus, AppMode
        import logging
        
        logger = logging.getLogger("test")
        # Write log with wrong mic value
        logger.info("decision=start ctx={mic=denied,screen=granted} source=test_gateway")
        
        snapshot = Snapshot(
            perm_mic=PermissionStatus.GRANTED,  # Wrong - log says denied
            perm_screen=PermissionStatus.GRANTED,
            perm_accessibility=PermissionStatus.GRANTED,
            device_input=DeviceStatus.DEFAULT_OK,
            network=NetworkStatus.ONLINE,
            first_run=False,
            app_mode=AppMode.SLEEPING,
        )
        
        with pytest.raises(AssertionError, match="Snapshot mic value mismatch"):
            assert_decision_logged(
                caplog,
                decision="start",
                source="test_gateway",
                ctx_keys=["mic", "screen"],
                snapshot=snapshot,
            )

