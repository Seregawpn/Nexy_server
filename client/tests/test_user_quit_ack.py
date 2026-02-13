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
    coordinator._tal_hold_active = True
    coordinator._release_tal_hold = Mock()

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
    coordinator._release_tal_hold.assert_called_once_with(reason="user_quit_intent")
    event_bus.publish.assert_not_awaited()


@pytest.mark.asyncio
async def test_user_quit_ack_is_idempotent() -> None:
    coordinator = SimpleModuleCoordinator()
    coordinator.state_manager = ApplicationStateManager()
    coordinator.state_manager.set_state_data(StateKeys.USER_QUIT_INTENT, False)
    coordinator._tal_hold_active = True
    coordinator._release_tal_hold = Mock()

    event_bus = Mock()
    event_bus.publish = AsyncMock()
    coordinator.event_bus = event_bus

    await coordinator._on_user_quit({"type": "tray.quit_clicked", "data": {}})
    await coordinator._on_user_quit({"type": "tray.quit_clicked", "data": {}})
    await asyncio.sleep(0)

    assert coordinator.state_manager.get_state_data(StateKeys.USER_QUIT_INTENT, False) is True
    coordinator._release_tal_hold.assert_called_once_with(reason="user_quit_intent")
    event_bus.publish.assert_not_awaited()


@pytest.mark.asyncio
async def test_stop_publishes_app_shutdown_once() -> None:
    coordinator = SimpleModuleCoordinator()
    coordinator.state_manager = ApplicationStateManager()
    coordinator.event_bus = Mock()
    coordinator.event_bus.publish = AsyncMock()
    coordinator.integrations = {}
    coordinator.workflows = {}
    coordinator.is_running = True

    assert await coordinator.stop() is True
    assert await coordinator.stop() is True

    coordinator.event_bus.publish.assert_awaited_once_with(
        "app.shutdown", {"source": "coordinator.stop"}
    )


@pytest.mark.asyncio
async def test_stop_clears_quit_in_flight_when_not_running() -> None:
    coordinator = SimpleModuleCoordinator()
    coordinator.state_manager = ApplicationStateManager()
    coordinator.event_bus = Mock()
    coordinator.event_bus.publish = AsyncMock()
    coordinator.is_running = False
    coordinator._quit_in_flight = True

    assert await coordinator.stop() is True
    assert coordinator._quit_in_flight is False
    coordinator.event_bus.publish.assert_not_awaited()


def test_hold_tal_skipped_when_tray_already_ready() -> None:
    coordinator = SimpleModuleCoordinator()
    coordinator._tray_ready = True
    coordinator._tal_hold_active = False
    coordinator._tal_hold_start = None

    coordinator._hold_tal_until_tray_ready()

    assert coordinator._tal_hold_active is False
    assert coordinator._tal_hold_start is None
