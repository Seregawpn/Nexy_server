import asyncio
from types import MethodType, SimpleNamespace
from unittest.mock import Mock

import pytest

from integration.integrations.permission_restart_integration import (
    PermissionRestartIntegration,
)
from integration.integrations.whatsapp_integration import WhatsappIntegration


@pytest.mark.asyncio
async def test_permission_restart_has_no_legacy_restart_pending_handler():
    """Legacy restart_pending flow must stay removed from PermissionRestartIntegration."""
    integration = PermissionRestartIntegration(
        event_bus=Mock(),
        state_manager=Mock(),
        error_handler=Mock(),
        config={"enabled": True},
    )
    assert not hasattr(integration, "_on_first_run_restart_pending")


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
