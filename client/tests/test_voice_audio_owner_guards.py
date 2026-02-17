from unittest.mock import AsyncMock, Mock

import pytest

from integration.core.error_handler import ErrorHandler
from integration.core.event_bus import EventBus
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
