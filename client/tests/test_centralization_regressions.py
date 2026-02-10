import asyncio
from types import MethodType, SimpleNamespace
from unittest.mock import Mock

import pytest

from integration.integrations.permission_restart_integration import (
    PermissionRestartIntegration,
)
from integration.integrations.whatsapp_integration import WhatsappIntegration


@pytest.mark.asyncio
async def test_permission_restart_does_not_write_restart_pending_state():
    """restart_pending is coordinator-owned; integration must not write it."""
    state_manager = Mock()
    state_manager.set_restart_pending = Mock()

    integration = PermissionRestartIntegration(
        event_bus=Mock(),
        state_manager=state_manager,
        error_handler=Mock(),
        config={"enabled": True},
    )
    integration._config = SimpleNamespace(enabled=True)
    integration._v2_enabled = False
    integration._was_restarted_this_session = False
    integration._restart_handler = None

    await integration._on_first_run_restart_pending(
        {
            "data": {
                "session_id": "test-session",
                "permissions": ["accessibility"],
                "is_last_batch": False,
                "batch_index": 0,
                "total_batches": 2,
            }
        }
    )

    state_manager.set_restart_pending.assert_not_called()


@pytest.mark.asyncio
async def test_whatsapp_reset_is_single_flight():
    """Multiple reset triggers must reuse one in-flight reset task."""
    integration = WhatsappIntegration(Mock(), Mock(), Mock())

    async def _fake_reset(self) -> None:
        await asyncio.sleep(0.05)

    integration._reset_session_and_restart = MethodType(_fake_reset, integration)

    integration._schedule_reset_session_and_restart("first_trigger")
    first_task = integration._reset_session_task
    integration._schedule_reset_session_and_restart("second_trigger")
    second_task = integration._reset_session_task

    assert first_task is not None
    assert first_task is second_task
    await first_task
