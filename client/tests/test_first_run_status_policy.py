from types import SimpleNamespace
from unittest.mock import AsyncMock, Mock

import pytest

from integration.integrations.first_run_permissions_integration import (
    FirstRunPermissionsIntegration,
)
from modules.permissions.v2.integration import PermissionOrchestratorIntegration
from modules.permissions.v2.types import PermissionId, StepState


def test_hard_permissions_summary_requires_pass_only() -> None:
    integration = PermissionOrchestratorIntegration(
        event_bus=Mock(),
        config={},
        ledger_path="/tmp/test-ledger.json",
    )
    integration._hard_permissions = [PermissionId.MICROPHONE]
    integration._ledger_store = object()

    ledger = SimpleNamespace(
        steps={
            PermissionId.MICROPHONE: SimpleNamespace(state=StepState.NEEDS_RESTART),
        }
    )
    integration._load_ledger = lambda: ledger  # type: ignore[method-assign]

    all_granted, missing = integration.hard_permissions_summary()
    assert all_granted is False
    assert missing == [PermissionId.MICROPHONE.value]


@pytest.mark.asyncio
async def test_timeout_mode_terminal_completion_uses_v2_owner_path() -> None:
    event_bus = Mock()
    event_bus.publish = AsyncMock()
    state_manager = Mock()
    state_manager.get_state_data = Mock(return_value=False)

    integration = FirstRunPermissionsIntegration(
        event_bus=event_bus,
        state_manager=state_manager,
        error_handler=Mock(),
    )
    integration._v2_enabled = True
    integration._advance_on_timeout = True
    integration._v2_integration = SimpleNamespace(
        is_first_run_complete=lambda: False,
        start=AsyncMock(),
        wait_for_completion=AsyncMock(return_value=True),
    )
    success = await integration.start()

    assert success is True
    integration._v2_integration.start.assert_awaited_once()
    integration._v2_integration.wait_for_completion.assert_awaited_once()
    event_bus.publish.assert_not_awaited()


@pytest.mark.asyncio
async def test_timeout_mode_does_not_publish_completion_when_not_terminal() -> None:
    integration = FirstRunPermissionsIntegration(
        event_bus=Mock(),
        state_manager=Mock(),
        error_handler=Mock(),
    )
    integration._v2_enabled = True
    integration._advance_on_timeout = True
    integration._v2_integration = SimpleNamespace(
        is_first_run_complete=lambda: False,
        start=AsyncMock(),
        wait_for_completion=AsyncMock(return_value=False),
    )

    success = await integration.start()

    assert success is True


@pytest.mark.asyncio
async def test_completed_ledger_uses_reemit_without_pipeline_start() -> None:
    integration = FirstRunPermissionsIntegration(
        event_bus=Mock(),
        state_manager=Mock(),
        error_handler=Mock(),
    )
    integration._v2_enabled = True
    integration._v2_integration = SimpleNamespace(
        is_first_run_complete=lambda: True,
        reemit_completion_from_ledger=AsyncMock(return_value=True),
        start=AsyncMock(),
        wait_for_completion=AsyncMock(return_value=True),
    )

    success = await integration.start()

    assert success is True
    integration._v2_integration.reemit_completion_from_ledger.assert_awaited_once()
    integration._v2_integration.start.assert_not_awaited()
    integration._v2_integration.wait_for_completion.assert_not_awaited()


@pytest.mark.asyncio
async def test_completed_ledger_reemit_fallback_starts_pipeline() -> None:
    integration = FirstRunPermissionsIntegration(
        event_bus=Mock(),
        state_manager=Mock(),
        error_handler=Mock(),
    )
    integration._v2_enabled = True
    integration._v2_integration = SimpleNamespace(
        is_first_run_complete=lambda: True,
        reemit_completion_from_ledger=AsyncMock(return_value=False),
        start=AsyncMock(),
        wait_for_completion=AsyncMock(return_value=True),
    )

    success = await integration.start()

    assert success is True
    integration._v2_integration.reemit_completion_from_ledger.assert_awaited_once()
    integration._v2_integration.start.assert_awaited_once()
    integration._v2_integration.wait_for_completion.assert_awaited_once()
