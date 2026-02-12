from __future__ import annotations

import asyncio
import os
import sys
from unittest.mock import AsyncMock, Mock

import pytest

sys.path.insert(0, os.getcwd())

from integration.integrations.first_run_permissions_integration import FirstRunPermissionsIntegration


def _build_integration() -> FirstRunPermissionsIntegration:
    integration = FirstRunPermissionsIntegration(
        event_bus=Mock(),
        state_manager=Mock(),
        error_handler=Mock(),
        config={},
    )
    integration._v2_enabled = True
    integration._advance_on_timeout = True
    integration._timeout_wait_s = 1.0
    return integration


@pytest.mark.asyncio
async def test_timeout_wait_task_cancelled_on_stop() -> None:
    integration = _build_integration()

    async def _wait_for_completion(*_args, **_kwargs):
        await asyncio.sleep(3600)
        return True

    v2_integration = Mock()
    v2_integration.start = AsyncMock()
    v2_integration.wait_for_completion = _wait_for_completion
    v2_integration.is_first_run_complete = Mock(return_value=False)
    integration._v2_integration = v2_integration

    await integration.start()
    assert integration._timeout_wait_task is not None
    assert not integration._timeout_wait_task.done()

    await integration.stop()
    assert integration._timeout_wait_task is None


@pytest.mark.asyncio
async def test_timeout_wait_task_single_flight_when_already_active() -> None:
    integration = _build_integration()

    gate = asyncio.Event()

    async def _wait_for_completion(*_args, **_kwargs):
        await gate.wait()
        return True

    v2_integration = Mock()
    v2_integration.start = AsyncMock()
    v2_integration.wait_for_completion = _wait_for_completion
    v2_integration.is_first_run_complete = Mock(return_value=False)
    integration._v2_integration = v2_integration

    await integration.start()
    first_task = integration._timeout_wait_task
    assert first_task is not None

    # Simulate repeated start call while timeout waiter is still in-flight.
    integration._running = False
    await integration.start()
    second_task = integration._timeout_wait_task

    assert first_task is second_task

    gate.set()
    await asyncio.sleep(0)
    await integration.stop()
