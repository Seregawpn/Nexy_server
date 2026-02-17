import asyncio
from types import SimpleNamespace
from unittest.mock import AsyncMock, Mock

import pytest

from modules.permissions.v2.integration import PermissionOrchestratorIntegration
from modules.permissions.v2.orchestrator import UIEvent, UIEventType
from modules.permissions.v2.types import PermissionId, Phase, StepMode, StepState


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


@pytest.mark.asyncio
async def test_completed_event_includes_final_snapshot_payload() -> None:
    event_bus = Mock()
    event_bus.publish = AsyncMock()
    integration = PermissionOrchestratorIntegration(
        event_bus=event_bus,
        config={},
        ledger_path="/tmp/test-ledger.json",
    )
    step_entry = SimpleNamespace(
        state=StepState.PASS_,
        mode=StepMode.AUTO_DIALOG,
        needs_restart_marked=False,
    )
    integration._hard_permissions = [PermissionId.MICROPHONE]
    integration._orchestrator = SimpleNamespace(
        ledger=SimpleNamespace(
            phase=Phase.COMPLETED,
            restart_count=0,
            steps={PermissionId.MICROPHONE: step_entry},
        ),
        hard_permissions=[PermissionId.MICROPHONE],
    )

    await integration._emit_event(
        UIEvent(
            type=UIEventType.COMPLETED,
            timestamp=0.0,
            payload={"phase": "completed"},
        )
    )

    completion_calls = [
        call
        for call in event_bus.publish.call_args_list
        if call.args and call.args[0] == "permissions.first_run_completed"
    ]
    assert len(completion_calls) == 1
    completion_payload = completion_calls[0].args[1]
    assert completion_payload["all_hard_granted"] is True
    assert completion_payload["missing_hard"] == []
    assert completion_payload["final_snapshot"]["phase"] == "completed"
    assert completion_payload["final_snapshot"]["hard_permissions"]["microphone"]["granted"] is True


@pytest.mark.asyncio
async def test_concurrent_completed_events_publish_legacy_once() -> None:
    event_bus = Mock()
    event_bus.publish = AsyncMock()
    integration = PermissionOrchestratorIntegration(
        event_bus=event_bus,
        config={},
        ledger_path="/tmp/test-ledger.json",
    )
    step_entry = SimpleNamespace(
        state=StepState.PASS_,
        mode=StepMode.AUTO_DIALOG,
        needs_restart_marked=False,
    )
    integration._hard_permissions = [PermissionId.MICROPHONE]
    integration._orchestrator = SimpleNamespace(
        ledger=SimpleNamespace(
            phase=Phase.COMPLETED,
            restart_count=0,
            steps={PermissionId.MICROPHONE: step_entry},
        ),
        hard_permissions=[PermissionId.MICROPHONE],
    )

    event = UIEvent(
        type=UIEventType.COMPLETED,
        timestamp=0.0,
        payload={"phase": "completed"},
    )
    await asyncio.gather(integration._emit_event(event), integration._emit_event(event))

    completion_calls = [
        call
        for call in event_bus.publish.call_args_list
        if call.args and call.args[0] == "permissions.first_run_completed"
    ]
    assert len(completion_calls) == 1
