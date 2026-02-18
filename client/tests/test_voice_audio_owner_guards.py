from types import SimpleNamespace
from unittest.mock import AsyncMock, Mock

import numpy as np
import pytest

from integration.core.error_handler import ErrorHandler
from integration.core.event_bus import EventBus
from integration.core.state_keys import StateKeys
from integration.core.state_manager import ApplicationStateManager
from integration.integrations.speech_playback_integration import SpeechPlaybackIntegration
from integration.integrations.voice_recognition_integration import VoiceRecognitionIntegration


@pytest.mark.asyncio
async def test_voice_mic_closed_dedup_by_session_across_sources():
    event_bus = EventBus()
    state_manager = ApplicationStateManager()
    state_manager.attach_event_bus(event_bus)
    error_handler = ErrorHandler()
    integration = VoiceRecognitionIntegration(event_bus, state_manager, error_handler)

    emitted: list[dict] = []

    async def capture(event):
        emitted.append(event.get("data", {}))

    await event_bus.subscribe("voice.mic_closed", capture)

    sid = "6e0a9e1a-3786-4c7d-b49a-1a2ca2549d0b"
    await integration._publish_mic_closed(sid, source="recording_stop")
    await integration._publish_mic_closed(sid, source="v2_completed")

    assert len(emitted) == 1
    assert emitted[0]["session_id"] == sid
    assert emitted[0]["source"] == "recording_stop"


@pytest.mark.asyncio
async def test_v2_failed_unknown_value_deferred_while_pending_stop_recognition():
    event_bus = EventBus()
    state_manager = ApplicationStateManager()
    error_handler = ErrorHandler()
    integration = VoiceRecognitionIntegration(event_bus, state_manager, error_handler)

    sid = "0f16ced8-4a88-4f3a-a156-b4a7e4048d35"
    integration._pending_stop_terminal_tasks[sid] = Mock()
    integration._has_pending_stop_recognition = Mock(return_value=True)
    integration._publish_recognition_failed = AsyncMock()
    integration._publish_mic_closed = AsyncMock()

    await integration._publish_v2_failed(
        sid,
        "unknown_value",
        was_listening_at_callback=False,
    )

    integration._publish_recognition_failed.assert_not_called()
    integration._publish_mic_closed.assert_not_called()


@pytest.mark.asyncio
async def test_v2_failed_unknown_value_publishes_when_no_pending_stop_recognition():
    event_bus = EventBus()
    state_manager = ApplicationStateManager()
    error_handler = ErrorHandler()
    integration = VoiceRecognitionIntegration(event_bus, state_manager, error_handler)

    sid = "8fbc84e1-2b8f-4304-887d-7f2f603f7cbc"
    integration._pending_stop_terminal_tasks[sid] = Mock()
    integration._has_pending_stop_recognition = Mock(return_value=False)
    integration._publish_recognition_failed = AsyncMock()
    integration._publish_mic_closed = AsyncMock()

    await integration._publish_v2_failed(
        sid,
        "unknown_value",
        was_listening_at_callback=False,
    )

    integration._publish_mic_closed.assert_called_once_with(sid, source="v2_failed")
    integration._publish_recognition_failed.assert_called_once()


@pytest.mark.asyncio
async def test_v2_completed_does_not_mark_terminal_while_listening():
    event_bus = EventBus()
    state_manager = ApplicationStateManager()
    state_manager.attach_event_bus(event_bus)
    error_handler = ErrorHandler()
    integration = VoiceRecognitionIntegration(event_bus, state_manager, error_handler)

    sid = "2b082bf6-26ad-4f14-bca3-b6124efd6d5a"
    state_manager.set_state_data(StateKeys.PTT_PRESSED, True)
    integration._recording_active = True

    published: list[dict] = []

    async def capture(event):
        published.append(event.get("data", {}))

    await event_bus.subscribe("voice.recognition_completed", capture)

    r1 = SimpleNamespace(text="hello", confidence=0.9, language="en", error=None)
    r2 = SimpleNamespace(text="hello world", confidence=0.9, language="en", error=None)
    await integration._publish_v2_completed(sid, r1)
    await integration._publish_v2_completed(sid, r2)

    assert len(published) == 2
    assert all(evt.get("interim") is True for evt in published)
    assert sid not in integration._terminal_recognition_ts

    # Final completion after release should become terminal and pass dedup once.
    state_manager.set_state_data(StateKeys.PTT_PRESSED, False)
    r3 = SimpleNamespace(text="hello world final", confidence=0.9, language="en", error=None)
    await integration._publish_v2_completed(sid, r3)

    assert len(published) == 3
    assert published[-1].get("interim") is False
    assert sid in integration._terminal_recognition_ts


def test_resolve_callback_session_id_rejects_stale_session():
    event_bus = EventBus()
    state_manager = ApplicationStateManager()
    error_handler = ErrorHandler()
    integration = VoiceRecognitionIntegration(event_bus, state_manager, error_handler)

    active_sid = "7f6c2e08-940f-4f5a-9f9b-a8f4239750c1"
    stale_sid = "e6025db8-c3b8-44f5-b7e6-2d1c6200f8c8"
    state_manager.update_session_id(active_sid)

    assert integration._resolve_callback_session_id(stale_sid) is None
    assert integration._resolve_callback_session_id(active_sid) == active_sid


@pytest.mark.asyncio
async def test_playback_mic_recovery_skips_stale_session():
    event_bus = EventBus()
    state_manager = ApplicationStateManager()
    error_handler = ErrorHandler()
    integration = SpeechPlaybackIntegration(event_bus, state_manager, error_handler)

    integration._running = True
    integration._avf_player = Mock()
    integration._avf_player.is_playing.return_value = False
    integration._avf_player.get_playback_runtime_status.return_value = {"mock": True}
    integration._avf_player.is_route_transition_in_flight = Mock(return_value=False)
    integration._ensure_player_ready = AsyncMock(return_value=True)

    integration._active_output_session_id = "active-session"
    integration._current_session_id = "active-session"

    await integration._on_voice_mic_closed(
        {"data": {"session_id": "stale-session", "source": "recording_stop"}}
    )

    integration._ensure_player_ready.assert_not_called()


@pytest.mark.asyncio
async def test_playback_mic_recovery_dedup_and_reassert_once():
    event_bus = EventBus()
    state_manager = ApplicationStateManager()
    error_handler = ErrorHandler()
    integration = SpeechPlaybackIntegration(event_bus, state_manager, error_handler)

    integration._running = True
    integration._avf_player = Mock()
    integration._avf_player.is_playing.return_value = True
    integration._avf_player.get_playback_runtime_status.return_value = {"mock": True}
    integration._avf_player.is_route_transition_in_flight = Mock(return_value=False)
    integration._ensure_player_ready = AsyncMock(return_value=True)
    integration._mic_recovery_post_stop_cooldown_sec = 0.0

    sid = "active-session"
    integration._active_output_session_id = sid
    integration._current_session_id = sid

    event = {"data": {"session_id": sid, "source": "recording_stop"}}
    await integration._on_voice_mic_closed(event)
    await integration._on_voice_mic_closed(event)

    integration._ensure_player_ready.assert_called_once_with(reassert_profile=True)


@pytest.mark.asyncio
async def test_playback_mic_recovery_skips_during_route_transition():
    event_bus = EventBus()
    state_manager = ApplicationStateManager()
    error_handler = ErrorHandler()
    integration = SpeechPlaybackIntegration(event_bus, state_manager, error_handler)

    integration._running = True
    integration._avf_player = Mock()
    integration._avf_player.is_playing.return_value = True
    integration._avf_player.get_playback_runtime_status.return_value = {"mock": True}
    integration._avf_player.is_route_transition_in_flight = Mock(return_value=True)
    integration._ensure_player_ready = AsyncMock(return_value=True)
    integration._mic_recovery_post_stop_cooldown_sec = 0.0
    integration._mic_recovery_route_wait_timeout_sec = 0.0

    sid = "active-session"
    integration._active_output_session_id = sid
    integration._current_session_id = sid

    await integration._on_voice_mic_closed(
        {"data": {"session_id": sid, "source": "recording_stop"}}
    )

    integration._ensure_player_ready.assert_not_called()


@pytest.mark.asyncio
async def test_playback_audio_chunk_does_not_write_non_uuid_session_to_state():
    event_bus = EventBus()
    state_manager = ApplicationStateManager()
    error_handler = ErrorHandler()
    integration = SpeechPlaybackIntegration(event_bus, state_manager, error_handler)
    integration._queue_session_audio = AsyncMock(return_value=False)

    await integration._on_audio_chunk(
        {
            "data": {
                "session_id": "system",
                "bytes": b"\x00\x00",
                "dtype": "int16",
                "sample_rate": 48000,
                "channels": 1,
                "shape": [1],
            }
        }
    )

    assert state_manager.get_current_session_id() is None


@pytest.mark.asyncio
async def test_playback_reopens_no_audio_terminal_when_first_audio_arrives():
    event_bus = EventBus()
    state_manager = ApplicationStateManager()
    error_handler = ErrorHandler()
    integration = SpeechPlaybackIntegration(event_bus, state_manager, error_handler)

    sid = "4f4f72c2-92e2-4fd2-a0a0-2a17cfac1bf1"
    integration._avf_player = Mock()
    integration._avf_player.add_audio_data = Mock()
    integration._ensure_player_ready = AsyncMock(return_value=True)
    integration._grpc_done_sessions[sid] = True
    integration._terminal_event_by_session[sid] = "playback.completed"
    integration._no_audio_terminal_sessions.add(sid)
    integration._finalized_sessions[sid] = True

    ok = await integration._queue_session_audio(
        session_id=sid,
        audio_data=np.zeros(32, dtype=np.float32),
        metadata={"kind": "grpc_audio"},
        trace_extra="test=true",
        source="grpc_audio",
    )

    assert ok is True
    assert sid not in integration._no_audio_terminal_sessions
    assert sid not in integration._terminal_event_by_session
    assert sid not in integration._finalized_sessions
    assert integration._had_audio_for_session[sid] is True
    assert sid in integration._silence_tasks
    integration._silence_tasks[sid].cancel()
