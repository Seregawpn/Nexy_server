from __future__ import annotations

import os
import sys
from unittest.mock import AsyncMock, Mock

import pytest

sys.path.insert(0, os.getcwd())

from integration.core.state_keys import StateKeys
from integration.core.state_manager import ApplicationStateManager
from modules.permissions.v2.integration import PermissionOrchestratorIntegration
from modules.permissions.v2.orchestrator import UIEvent, UIEventType


@pytest.mark.asyncio
async def test_v2_skips_ready_to_greet_when_first_run_restart_is_scheduled() -> None:
    state_manager = ApplicationStateManager()
    state_manager.set_state_data(StateKeys.FIRST_RUN_RESTART_SCHEDULED, True)

    event_bus = Mock()
    event_bus.publish = AsyncMock()

    integration = PermissionOrchestratorIntegration(
        event_bus=event_bus,
        config={},
        ledger_path="/tmp/permission_ledger_test.json",
        state_manager=state_manager,
    )

    await integration._publish_ready_to_greet(
        UIEvent(type=UIEventType.COMPLETED, timestamp=0.0, payload={"phase": "completed", "summary": {}})
    )

    event_bus.publish.assert_not_awaited()
    assert integration._ready_published is True


@pytest.mark.asyncio
async def test_v2_publishes_ready_to_greet_when_restart_not_scheduled() -> None:
    state_manager = ApplicationStateManager()
    state_manager.set_state_data(StateKeys.FIRST_RUN_RESTART_SCHEDULED, False)

    event_bus = Mock()
    event_bus.publish = AsyncMock()

    integration = PermissionOrchestratorIntegration(
        event_bus=event_bus,
        config={},
        ledger_path="/tmp/permission_ledger_test.json",
        state_manager=state_manager,
    )

    await integration._publish_ready_to_greet(
        UIEvent(type=UIEventType.COMPLETED, timestamp=0.0, payload={"phase": "completed", "summary": {}})
    )

    event_bus.publish.assert_awaited_once()
    assert event_bus.publish.await_args.args[0] == "system.ready_to_greet"
