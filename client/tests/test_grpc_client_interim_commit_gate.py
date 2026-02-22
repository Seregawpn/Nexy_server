import asyncio
from unittest.mock import AsyncMock

import pytest

from integration.core.error_handler import ErrorHandler
from integration.core.event_bus import EventBus
from integration.core.state_manager import ApplicationStateManager
from integration.integrations.grpc_client_integration import (
    GrpcClientIntegration,
    GrpcClientIntegrationConfig,
)


def _make_integration() -> GrpcClientIntegration:
    event_bus = EventBus()
    state_manager = ApplicationStateManager()
    error_handler = ErrorHandler()
    config = GrpcClientIntegrationConfig(aggregate_timeout_sec=0.0, use_network_gate=False)
    return GrpcClientIntegration(event_bus, state_manager, error_handler, config=config)


@pytest.mark.asyncio
async def test_voice_completed_interim_updates_buffer_without_send():
    integration = _make_integration()
    integration._maybe_send = AsyncMock()

    sid = "3fcf19f8-fb2b-47ad-bf57-bf551e0ecfb2"
    await integration._on_voice_completed(
        {"data": {"session_id": sid, "text": "partial text", "interim": True}}
    )

    assert integration._sessions[sid]["text"] == "partial text"
    assert integration._sessions[sid]["ready_to_send"] is False
    integration._maybe_send.assert_not_called()

    await integration._on_voice_completed(
        {"data": {"session_id": sid, "text": "final text", "interim": False}}
    )

    assert integration._sessions[sid]["text"] == "final text"
    assert integration._sessions[sid]["ready_to_send"] is False
    integration._maybe_send.assert_not_called()

    await integration._on_recording_stop({"data": {"session_id": sid}})
    assert integration._sessions[sid]["ready_to_send"] is True
    integration._maybe_send.assert_called_once_with(sid)


@pytest.mark.asyncio
async def test_terminal_before_release_does_not_send_until_recording_stop():
    integration = _make_integration()
    integration._maybe_send = AsyncMock()

    sid = "1f4dd920-57fd-49f4-80ba-e901b85aa1ca"
    await integration._on_voice_completed(
        {"data": {"session_id": sid, "text": "final while holding", "interim": False}}
    )

    assert integration._sessions[sid]["terminal_recognition_received"] is True
    assert integration._sessions[sid]["ready_to_send"] is False
    assert integration.get_status()["terminal_before_release_deferred"] == 1
    integration._maybe_send.assert_not_called()

    await integration._on_recording_stop({"data": {"session_id": sid}})
    assert integration._sessions[sid]["ready_to_send"] is True
    integration._maybe_send.assert_called_once_with(sid)


@pytest.mark.asyncio
async def test_maybe_send_requires_terminal_gate_and_dispatches_once():
    integration = _make_integration()
    integration._send = AsyncMock()

    sid = "f6b4f4d7-374f-4d66-ad27-a4b81dc7f1fb"
    integration._sessions[sid] = {"text": "hello", "ready_to_send": False}

    await integration._maybe_send(sid)
    integration._send.assert_not_called()

    integration._sessions[sid]["ready_to_send"] = True
    await integration._maybe_send(sid)
    await asyncio.sleep(0.01)
    integration._send.assert_called_once_with(sid)

    await integration._maybe_send(sid)
    integration._send.assert_called_once_with(sid)


@pytest.mark.asyncio
async def test_collect_text_is_debounced_and_sends_latest_chunk():
    integration = _make_integration()
    integration._collect_debounce_sec = 0.02
    integration._send_collect = AsyncMock()

    sid = "8bd1722f-d361-4aa1-b51d-cf8d77db3f9e"
    integration._schedule_collect_send(sid, chunk_text="one", chunk_seq=1)
    integration._schedule_collect_send(sid, chunk_text="two", chunk_seq=2)
    await asyncio.sleep(0.06)

    integration._send_collect.assert_called_once_with(
        session_id=sid,
        chunk_text="two",
        chunk_seq=2,
        include_screenshot=False,
    )


@pytest.mark.asyncio
async def test_collect_screenshot_is_sent_immediately():
    integration = _make_integration()
    integration._collect_debounce_sec = 0.1
    integration._send_collect = AsyncMock()

    sid = "7643e6b8-6668-4938-b7c2-c3f36a50077f"
    integration._schedule_collect_send(sid, chunk_seq=3, include_screenshot=True)
    await asyncio.sleep(0.02)

    integration._send_collect.assert_called_once_with(
        session_id=sid,
        chunk_text=None,
        chunk_seq=3,
        include_screenshot=True,
    )
