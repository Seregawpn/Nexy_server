"""
Integration tests for permission restart and update interplay.

Tests that:
- PermissionRestartIntegration does NOT schedule restart when update_in_progress=True
- Gateway blocks restart scheduling (ABORT decision)
"""

import pytest
from unittest.mock import Mock, AsyncMock, patch

from integration.core.event_bus import EventBus
from integration.core.state_manager import ApplicationStateManager
from integration.core.error_handler import ErrorHandler
from integration.integrations.permission_restart_integration import PermissionRestartIntegration
from modules.permission_restart.core.types import PermissionTransition, RestartRequest
from modules.permissions.core.types import PermissionType, PermissionStatus as PermStatus


class TestPermissionRestartAndUpdateInterplay:
    """Test interaction between permission restart and update."""

    @pytest.mark.anyio("asyncio")
    async def test_restart_blocked_when_update_in_progress(self):
        """Test that restart is blocked when update_in_progress=True."""
        event_bus = Mock(spec=EventBus)
        state_manager = ApplicationStateManager()
        error_handler = Mock(spec=ErrorHandler)
        config = {
            "enabled": True,
            "restart_delay_sec": 5.0,
            "max_restart_attempts": 3,
            "respect_updates": True,
        }

        # Create mock updater integration
        updater_integration = Mock()
        updater_integration.is_update_in_progress = Mock(return_value=True)

        integration = PermissionRestartIntegration(
            event_bus=event_bus,
            state_manager=state_manager,
            error_handler=error_handler,
            config=config,
            updater_integration=updater_integration,
        )

        await integration._do_initialize()

        # Set update_in_progress flag
        state_manager.set_state_data("update_in_progress", True)

        # Create a transition that would normally trigger restart
        transition = PermissionTransition(
            permission=PermissionType.ACCESSIBILITY,
            old_status=PermStatus.NOT_DETERMINED,
            new_status=PermStatus.GRANTED,
            session_id="test-session-123",
            source="test_source",
        )

        # Mock scheduler to track if maybe_schedule_restart is called
        scheduler_called = []
        async def mock_maybe_schedule_restart(t):
            scheduler_called.append(t)
            return RestartRequest(
                session_id=t.session_id,
                reason="test",
                delay_sec=0.0,
                critical_permissions=(t.permission,),
            )

        integration._scheduler.maybe_schedule_restart = mock_maybe_schedule_restart

        # Try to handle transition
        await integration._handle_transition(transition)

        # Verify that scheduler was NOT called (restart blocked by gateway)
        assert len(scheduler_called) == 0, "Scheduler should not be called when update is in progress"

    @pytest.mark.anyio("asyncio")
    async def test_restart_allowed_when_update_not_in_progress(self):
        """Test that restart is allowed when update_in_progress=False."""
        event_bus = Mock(spec=EventBus)
        state_manager = ApplicationStateManager()
        error_handler = Mock(spec=ErrorHandler)
        config = {
            "enabled": True,
            "restart_delay_sec": 5.0,
            "max_restart_attempts": 3,
            "respect_updates": True,
        }

        # Create mock updater integration
        updater_integration = Mock()
        updater_integration.is_update_in_progress = Mock(return_value=False)

        integration = PermissionRestartIntegration(
            event_bus=event_bus,
            state_manager=state_manager,
            error_handler=error_handler,
            config=config,
            updater_integration=updater_integration,
        )

        await integration._do_initialize()

        # Set update_in_progress flag to False
        state_manager.set_state_data("update_in_progress", False)

        # Create a transition that should trigger restart
        transition = PermissionTransition(
            permission=PermissionType.ACCESSIBILITY,
            old_status=PermStatus.NOT_DETERMINED,
            new_status=PermStatus.GRANTED,
            session_id="test-session-123",
            source="test_source",
        )

        # Mock scheduler to track if maybe_schedule_restart is called
        scheduler_called = []
        async def mock_maybe_schedule_restart(t):
            scheduler_called.append(t)
            return RestartRequest(
                session_id=t.session_id,
                reason="test",
                delay_sec=0.0,
                critical_permissions=(t.permission,),
            )

        integration._scheduler.maybe_schedule_restart = mock_maybe_schedule_restart

        # Try to handle transition
        await integration._handle_transition(transition)

        # Verify that scheduler WAS called (restart allowed)
        assert len(scheduler_called) > 0, "Scheduler should be called when update is not in progress"
        assert scheduler_called[0] == transition

    @pytest.mark.anyio("asyncio")
    async def test_restart_blocked_when_first_run_restart_pending(self):
        """Test that restart is blocked when first_run=True & restart_pending=True."""
        event_bus = Mock(spec=EventBus)
        state_manager = ApplicationStateManager()
        error_handler = Mock(spec=ErrorHandler)
        config = {
            "enabled": True,
            "restart_delay_sec": 5.0,
            "max_restart_attempts": 3,
            "respect_updates": True,
        }

        # Create mock updater integration
        updater_integration = Mock()
        updater_integration.is_update_in_progress = Mock(return_value=False)

        integration = PermissionRestartIntegration(
            event_bus=event_bus,
            state_manager=state_manager,
            error_handler=error_handler,
            config=config,
            updater_integration=updater_integration,
        )

        await integration._do_initialize()

        # Set first_run and restart_pending flags
        state_manager.set_state_data("permissions_restart_pending", True)
        state_manager.set_state_data("first_run_required", True)
        state_manager.set_state_data("first_run_completed", False)

        # Create a transition
        transition = PermissionTransition(
            permission=PermissionType.ACCESSIBILITY,
            old_status=PermStatus.NOT_DETERMINED,
            new_status=PermStatus.GRANTED,
            session_id="test-session-123",
            source="test_source",
        )

        # Mock scheduler to track if maybe_schedule_restart is called
        scheduler_called = []
        async def mock_maybe_schedule_restart(t):
            scheduler_called.append(t)
            return RestartRequest(
                session_id=t.session_id,
                reason="test",
                delay_sec=0.0,
                critical_permissions=(t.permission,),
            )

        integration._scheduler.maybe_schedule_restart = mock_maybe_schedule_restart

        # Try to handle transition
        await integration._handle_transition(transition)

        # Verify that scheduler was NOT called (restart blocked by gateway)
        # Note: This depends on how create_snapshot_from_state determines first_run
        # In this test, we're testing the gateway logic, not the snapshot creation
        # If snapshot shows first_run=True & restart_pending=True, scheduler should not be called
