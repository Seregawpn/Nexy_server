import pytest

from integration.core.error_handler import ErrorHandler
from integration.core.event_bus import EventBus
from integration.core.gateways import Decision
from integration.core.state_manager import AppMode, ApplicationStateManager
from integration.integrations.voice_recognition_integration import (
    VoiceRecognitionConfig,
    VoiceRecognitionIntegration,
)
import integration.integrations.voice_recognition_integration as vr_module


@pytest.mark.asyncio
async def test_route_reconcile_abort_blocks_recording_start(monkeypatch):
    event_bus = EventBus()
    state_manager = ApplicationStateManager()
    state_manager.attach_event_bus(event_bus)
    state_manager.set_mode(AppMode.SLEEPING)
    integration = VoiceRecognitionIntegration(
        event_bus=event_bus,
        state_manager=state_manager,
        error_handler=ErrorHandler(),
        config=VoiceRecognitionConfig(simulate=True),
    )

    published: list[tuple[str | None, dict]] = []

    async def capture(event):
        published.append((event.get("type"), event.get("data", {})))

    await event_bus.subscribe("voice.mic_closed", capture)
    await event_bus.subscribe("voice.recognition_failed", capture)

    monkeypatch.setattr(vr_module, "decide_route_manager_reconcile", lambda _snapshot: Decision.ABORT)

    sid = "11111111-1111-4111-8111-111111111111"
    await integration._on_recording_start({"data": {"session_id": sid}})

    assert integration._recording_active is False
    assert state_manager.get_current_session_id() is None

    mic_closed = [d for t, d in published if t == "voice.mic_closed"]
    failed = [d for t, d in published if t == "voice.recognition_failed"]
    assert len(mic_closed) == 1
    assert len(failed) == 1
    assert mic_closed[0]["session_id"] == sid
    assert failed[0]["session_id"] == sid
    assert failed[0]["reason"] == "route_reconcile_abort"


@pytest.mark.asyncio
async def test_route_reconcile_retry_abort_blocks_recording_start(monkeypatch):
    event_bus = EventBus()
    state_manager = ApplicationStateManager()
    state_manager.attach_event_bus(event_bus)
    state_manager.set_mode(AppMode.LISTENING)
    integration = VoiceRecognitionIntegration(
        event_bus=event_bus,
        state_manager=state_manager,
        error_handler=ErrorHandler(),
        config=VoiceRecognitionConfig(simulate=True),
    )

    decisions = iter([Decision.RETRY, Decision.ABORT])
    monkeypatch.setattr(vr_module, "decide_route_manager_reconcile", lambda _snapshot: next(decisions))

    published: list[tuple[str | None, dict]] = []

    async def capture(event):
        published.append((event.get("type"), event.get("data", {})))

    await event_bus.subscribe("voice.recognition_failed", capture)

    sid = "22222222-2222-4222-8222-222222222222"
    await integration._on_recording_start({"data": {"session_id": sid}})

    failed = [d for t, d in published if t == "voice.recognition_failed"]
    assert len(failed) == 1
    assert failed[0]["session_id"] == sid
    assert failed[0]["reason"] == "route_reconcile_retry_abort"


@pytest.mark.asyncio
async def test_route_reconcile_retry_retry_blocks_recording_start(monkeypatch):
    event_bus = EventBus()
    state_manager = ApplicationStateManager()
    state_manager.attach_event_bus(event_bus)
    state_manager.set_mode(AppMode.LISTENING)
    integration = VoiceRecognitionIntegration(
        event_bus=event_bus,
        state_manager=state_manager,
        error_handler=ErrorHandler(),
        config=VoiceRecognitionConfig(simulate=True),
    )

    decisions = iter([Decision.RETRY, Decision.RETRY])
    monkeypatch.setattr(vr_module, "decide_route_manager_reconcile", lambda _snapshot: next(decisions))

    published: list[tuple[str | None, dict]] = []

    async def capture(event):
        published.append((event.get("type"), event.get("data", {})))

    await event_bus.subscribe("voice.recognition_failed", capture)

    sid = "33333333-3333-4333-8333-333333333333"
    await integration._on_recording_start({"data": {"session_id": sid}})

    failed = [d for t, d in published if t == "voice.recognition_failed"]
    assert len(failed) == 1
    assert failed[0]["session_id"] == sid
    assert failed[0]["reason"] == "route_reconcile_retry_exhausted"
