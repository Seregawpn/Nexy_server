from __future__ import annotations

import os
import sys
from unittest.mock import AsyncMock, Mock

import pytest

sys.path.insert(0, os.getcwd())

from integration.core.simple_module_coordinator import SimpleModuleCoordinator
from integration.core.state_keys import StateKeys
from integration.core.state_manager import ApplicationStateManager


@pytest.mark.asyncio
async def test_stop_publishes_user_initiated_shutdown_payload() -> None:
    coordinator = SimpleModuleCoordinator()
    coordinator.is_running = True
    coordinator.state_manager = ApplicationStateManager()
    coordinator.state_manager.set_state_data(StateKeys.USER_QUIT_INTENT, True)

    event_bus = Mock()
    event_bus.publish = AsyncMock()
    coordinator.event_bus = event_bus
    coordinator.integrations = {}
    coordinator.workflows = {}

    ok = await coordinator.stop()

    assert ok is True
    event_bus.publish.assert_awaited_once_with(
        "app.shutdown",
        {
            "coordinator": "simple_module_coordinator",
            "source": "coordinator.stop",
            "user_initiated": True,
        },
    )
