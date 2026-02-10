import asyncio
import os
import sys
import time
from unittest.mock import AsyncMock, Mock

import pytest

sys.path.insert(0, os.getcwd())

from integration.core.simple_module_coordinator import SimpleModuleCoordinator
from integration.core.state_keys import StateKeys
from integration.core.state_manager import ApplicationStateManager


@pytest.mark.asyncio
async def test_user_quit_ack_is_non_blocking() -> None:
    coordinator = SimpleModuleCoordinator()
    coordinator.state_manager = ApplicationStateManager()
    coordinator.state_manager.set_state_data(StateKeys.USER_QUIT_INTENT, False)

    async def slow_publish(*args, **kwargs):
        await asyncio.sleep(0.3)

    event_bus = Mock()
    event_bus.publish = AsyncMock(side_effect=slow_publish)
    coordinator.event_bus = event_bus

    started = time.perf_counter()
    await coordinator._on_user_quit({"type": "tray.quit_clicked", "data": {}})
    elapsed = time.perf_counter() - started

    assert elapsed < 0.1
    assert coordinator.state_manager.get_state_data(StateKeys.USER_QUIT_INTENT, False) is True

    await asyncio.sleep(0.35)
    event_bus.publish.assert_awaited_once_with(
        "app.shutdown",
        {"source": "user.quit", "user_initiated": True},
    )


@pytest.mark.asyncio
async def test_user_quit_ack_is_idempotent() -> None:
    coordinator = SimpleModuleCoordinator()
    coordinator.state_manager = ApplicationStateManager()
    coordinator.state_manager.set_state_data(StateKeys.USER_QUIT_INTENT, False)

    event_bus = Mock()
    event_bus.publish = AsyncMock()
    coordinator.event_bus = event_bus

    await coordinator._on_user_quit({"type": "tray.quit_clicked", "data": {}})
    await coordinator._on_user_quit({"type": "tray.quit_clicked", "data": {}})
    await asyncio.sleep(0)

    assert coordinator.state_manager.get_state_data(StateKeys.USER_QUIT_INTENT, False) is True
    event_bus.publish.assert_awaited_once_with(
        "app.shutdown",
        {"source": "user.quit", "user_initiated": True},
    )
