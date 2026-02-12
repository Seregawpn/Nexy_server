from __future__ import annotations

import os
import sys
from unittest.mock import AsyncMock, Mock

import pytest

sys.path.insert(0, os.getcwd())

from integration.integrations.first_run_permissions_integration import FirstRunPermissionsIntegration


def _build_strict_integration() -> FirstRunPermissionsIntegration:
    integration = FirstRunPermissionsIntegration(
        event_bus=Mock(),
        state_manager=Mock(),
        error_handler=Mock(),
        config={},
    )
    integration._v2_enabled = True
    integration._advance_on_timeout = False
    return integration


@pytest.mark.asyncio
async def test_strict_start_resets_running_when_completion_is_false() -> None:
    integration = _build_strict_integration()

    v2_integration = Mock()
    v2_integration.start = AsyncMock()
    v2_integration.wait_for_completion = AsyncMock(return_value=False)
    v2_integration.is_first_run_complete = Mock(return_value=False)
    integration._v2_integration = v2_integration

    ok = await integration.start()

    assert ok is False
    assert integration._running is False

    # No sticky running state: second call should execute start again.
    ok2 = await integration.start()
    assert ok2 is False
    assert v2_integration.start.await_count == 2


@pytest.mark.asyncio
async def test_strict_start_resets_running_when_v2_start_raises() -> None:
    integration = _build_strict_integration()

    v2_integration = Mock()
    v2_integration.start = AsyncMock(side_effect=RuntimeError("boom"))
    v2_integration.wait_for_completion = AsyncMock(return_value=True)
    v2_integration.is_first_run_complete = Mock(return_value=False)
    integration._v2_integration = v2_integration

    ok = await integration.start()

    assert ok is False
    assert integration._running is False
