"""
Integration tests for UpdaterIntegration mode guard.

Tests that:
- _can_update() returns False when AppMode=LISTENING|PROCESSING (both Enum and string)
- Update does not start when in LISTENING|PROCESSING mode
"""

import pytest
import asyncio
from unittest.mock import Mock, AsyncMock

from integration.core.event_bus import EventBus
from integration.core.state_manager import ApplicationStateManager, AppMode
from integration.integrations.updater_integration import UpdaterIntegration


class TestUpdaterModeGuard:
    """Test that updater respects active session modes."""

    @pytest.fixture
    async def event_bus(self):
        """Create EventBus with attached loop."""
        bus = EventBus()
        try:
            loop = asyncio.get_running_loop()
            bus.attach_loop(loop)
        except RuntimeError:
            pass
        return bus

    @pytest.fixture
    def state_manager(self):
        """Create ApplicationStateManager."""
        return ApplicationStateManager()

    @pytest.mark.anyio
    async def test_can_update_returns_false_for_listening_enum(self, event_bus, state_manager):
        """Test that _can_update() returns False when AppMode=LISTENING (Enum)."""
        config = {"updater": {"enabled": True, "check_on_startup": False, "check_interval_sec": 3600}}

        integration = UpdaterIntegration(event_bus, state_manager, config)
        await integration.initialize()

        # Set mode to LISTENING (Enum)
        state_manager.set_mode(AppMode.LISTENING)

        # Check if update is allowed
        can_update = await integration._can_update()

        assert can_update is False
        
        # Cleanup: stop the integration to cancel check_task
        await integration.stop()

    @pytest.mark.anyio
    async def test_can_update_returns_false_for_processing_enum(self, event_bus, state_manager):
        """Test that _can_update() returns False when AppMode=PROCESSING (Enum)."""
        config = {"updater": {"enabled": True, "check_on_startup": False, "check_interval_sec": 3600}}

        integration = UpdaterIntegration(event_bus, state_manager, config)
        await integration.initialize()

        # Set mode to PROCESSING (Enum)
        state_manager.set_mode(AppMode.PROCESSING)

        # Check if update is allowed
        can_update = await integration._can_update()

        assert can_update is False
        
        # Cleanup: stop the integration to cancel check_task
        await integration.stop()

    @pytest.mark.anyio
    async def test_can_update_returns_true_for_sleeping_enum(self, event_bus, state_manager):
        """Test that _can_update() returns True when AppMode=SLEEPING (Enum)."""
        config = {"updater": {"enabled": True, "check_on_startup": False, "check_interval_sec": 3600}}

        integration = UpdaterIntegration(event_bus, state_manager, config)
        
        # Mock updater to return None (no updates available)
        integration.updater = Mock()
        integration.updater.check_for_updates = Mock(return_value=None)
        integration.updater.get_current_build = Mock(return_value="1.0.0")
        
        await integration.initialize()

        # Set mode to SLEEPING (Enum)
        state_manager.set_mode(AppMode.SLEEPING)

        # Check if update is allowed
        can_update = await integration._can_update()

        assert can_update is True
        
        # Cleanup: stop the integration to cancel check_task
        await integration.stop()

    @pytest.mark.anyio
    async def test_update_does_not_start_in_listening_mode(self, event_bus, state_manager):
        """Test that update does not start when in LISTENING mode."""
        config = {"updater": {"enabled": True, "check_on_startup": False, "check_interval_sec": 3600}}

        integration = UpdaterIntegration(event_bus, state_manager, config)
        await integration.initialize()

        # Set mode to LISTENING
        state_manager.set_mode(AppMode.LISTENING)

        # Check _can_update instead of _execute_update (avoids network calls)
        can_update = await integration._can_update()

        # Update should be blocked
        assert can_update is False
        
        # Cleanup: stop the integration to cancel check_task
        await integration.stop()

    @pytest.mark.anyio
    async def test_update_does_not_start_in_processing_mode(self, event_bus, state_manager):
        """Test that update does not start when in PROCESSING mode."""
        config = {"updater": {"enabled": True, "check_on_startup": False, "check_interval_sec": 3600}}

        integration = UpdaterIntegration(event_bus, state_manager, config)
        await integration.initialize()

        # Set mode to PROCESSING
        state_manager.set_mode(AppMode.PROCESSING)

        # Check _can_update instead of _execute_update (avoids network calls)
        can_update = await integration._can_update()

        # Update should be blocked
        assert can_update is False
        
        # Cleanup: stop the integration to cancel check_task
        await integration.stop()

    @pytest.mark.anyio
    async def test_update_starts_in_sleeping_mode(self, event_bus, state_manager):
        """Test that update can start when in SLEEPING mode (if updates available)."""
        config = {"updater": {"enabled": True, "check_on_startup": False, "check_interval_sec": 3600}}

        integration = UpdaterIntegration(event_bus, state_manager, config)
        
        # Mock updater to return None (no updates available)
        integration.updater = Mock()
        integration.updater.check_for_updates = Mock(return_value=None)
        integration.updater.get_current_build = Mock(return_value="1.0.0")

        await integration.initialize()

        # Set mode to SLEEPING
        state_manager.set_mode(AppMode.SLEEPING)

        # Try to execute update (should check, but no updates available)
        update_executed = await integration._execute_update(trigger="test")

        # Update should be checked (but no updates available, so returns False)
        assert update_executed is False
        integration.updater.check_for_updates.assert_called_once()
        
        # Cleanup: stop the integration to cancel check_task
        await integration.stop()

