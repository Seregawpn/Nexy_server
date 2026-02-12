from types import SimpleNamespace
from unittest.mock import AsyncMock, Mock

import pytest

from modules.permissions.v2.integration import PermissionOrchestratorIntegration
from modules.permissions.v2.orchestrator import UIEvent, UIEventType
from modules.permissions.v2.types import Phase


@pytest.mark.asyncio
async def test_restart_scheduled_does_not_signal_completion() -> None:
    event_bus = Mock()
    event_bus.publish = AsyncMock()
    integration = PermissionOrchestratorIntegration(
        event_bus=event_bus,
        config={},
        ledger_path="/tmp/test-ledger.json",
    )

    await integration._emit_event(
        UIEvent(
            type=UIEventType.RESTART_SCHEDULED,
            timestamp=0.0,
            payload={"reason": "test"},
        )
    )

    assert integration._completed is False
    assert integration._completion_event.is_set() is False


@pytest.mark.asyncio
async def test_non_terminal_phase_defers_completion_signal() -> None:
    integration = PermissionOrchestratorIntegration(
        event_bus=Mock(),
        config={},
        ledger_path="/tmp/test-ledger.json",
    )
    integration._orchestrator = SimpleNamespace(
        start=AsyncMock(),
        ledger=SimpleNamespace(phase=Phase.RESTART_PENDING, steps={}),
        hard_permissions=[],
    )

    await integration._run_orchestrator()

    assert integration._completed is False
    assert integration._completion_event.is_set() is False


@pytest.mark.asyncio
async def test_terminal_phase_signals_completion() -> None:
    integration = PermissionOrchestratorIntegration(
        event_bus=Mock(),
        config={},
        ledger_path="/tmp/test-ledger.json",
    )
    integration._orchestrator = SimpleNamespace(
        start=AsyncMock(),
        ledger=SimpleNamespace(phase=Phase.COMPLETED, steps={}),
        hard_permissions=[],
    )

    await integration._run_orchestrator()

    assert integration._completed is True
    assert integration._completion_event.is_set() is True
