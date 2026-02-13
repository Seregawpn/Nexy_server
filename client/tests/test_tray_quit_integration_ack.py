import asyncio
import os
import sys
import time
from types import SimpleNamespace
from unittest.mock import AsyncMock, Mock

import pytest

sys.path.insert(0, os.getcwd())

from integration.core.state_keys import StateKeys
from integration.integrations.tray_controller_integration import TrayControllerIntegration


@pytest.mark.asyncio
async def test_on_tray_quit_sets_intent_and_returns_without_waiting_publish():
    integration = TrayControllerIntegration.__new__(TrayControllerIntegration)
    integration.state_manager = Mock()

    async def slow_publish(*args, **kwargs):
        await asyncio.sleep(0.25)

    integration.event_bus = SimpleNamespace(
        publish=AsyncMock(side_effect=slow_publish),
        get_loop=asyncio.get_running_loop,
    )

    started = time.perf_counter()
    await integration._on_tray_quit("quit_clicked", {})
    elapsed = time.perf_counter() - started

    assert elapsed < 0.1
    integration.state_manager.set_state_data.assert_called_once_with(
        StateKeys.USER_QUIT_INTENT, True
    )

    await asyncio.sleep(0.3)
    integration.event_bus.publish.assert_awaited_once_with(
        "tray.quit_clicked", {"source": "tray.quit"}
    )
