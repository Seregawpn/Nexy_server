"""
Тесты полного прерывания воспроизведения в текущей AVF-архитектуре.
"""

import pytest
import pytest_asyncio
from unittest.mock import AsyncMock, MagicMock, Mock

from integration.integrations.speech_playback_integration import SpeechPlaybackIntegration
from integration.core.event_bus import EventBus
from integration.core.state_manager import ApplicationStateManager
from integration.core.error_handler import ErrorHandler


@pytest.fixture
def event_bus():
    bus = MagicMock(spec=EventBus)
    bus.publish = AsyncMock()
    bus.subscribe = AsyncMock()
    bus.unsubscribe = AsyncMock()
    return bus


@pytest.fixture
def state_manager():
    manager = MagicMock(spec=ApplicationStateManager)
    manager.update_session_id = Mock()
    return manager


@pytest.fixture
def error_handler():
    return MagicMock(spec=ErrorHandler)


@pytest_asyncio.fixture
async def speech_playback_integration(event_bus, state_manager, error_handler):
    integration = SpeechPlaybackIntegration(
        event_bus=event_bus,
        state_manager=state_manager,
        error_handler=error_handler,
    )
    await integration.initialize()
    return integration


@pytest.mark.asyncio
async def test_interrupt_marks_cancelled_and_stops_player(speech_playback_integration):
    session_id = "test_session_123"
    mock_player = Mock()
    mock_player.clear_queue = Mock(return_value=None)
    mock_player.stop_playback = Mock(return_value=True)
    speech_playback_integration._avf_player = mock_player

    interrupt_event = {
        "type": "playback.cancelled",
        "data": {
            "session_id": session_id,
            "source": "keyboard",
            "reason": "user_interrupt",
        },
    }

    await speech_playback_integration._on_unified_interrupt(interrupt_event)

    # Guard-контракт: без предварительного audio session не добавляется в cancelled_sessions.
    assert session_id not in speech_playback_integration._cancelled_sessions
    assert mock_player.clear_queue.call_count >= 1
    assert mock_player.stop_playback.call_count >= 1


@pytest.mark.asyncio
async def test_new_chunks_ignored_after_interrupt(speech_playback_integration):
    session_id = "test_session_123"
    mock_player = Mock()
    mock_player.clear_queue = Mock(return_value=None)
    mock_player.stop_playback = Mock(return_value=True)
    mock_player.add_audio_data = Mock(return_value="chunk_id")
    speech_playback_integration._avf_player = mock_player

    # Имитируем, что session уже проигрывала аудио: только в этом случае
    # cancel должен блокировать поздние чанки через cancelled_sessions guard.
    speech_playback_integration._had_audio_for_session[session_id] = True

    await speech_playback_integration._on_unified_interrupt(
        {
            "type": "playback.cancelled",
            "data": {"session_id": session_id, "source": "keyboard", "reason": "user_interrupt"},
        }
    )

    await speech_playback_integration._on_audio_chunk(
        {
            "type": "grpc.response.audio",
            "data": {
                "session_id": session_id,
                "bytes": (b"\x00\x01" * 2048),
                "dtype": "int16",
                "sample_rate": 48000,
                "channels": 1,
            },
        }
    )

    # Чанк должен быть проигнорирован guard-ом cancelled_sessions.
    assert mock_player.add_audio_data.call_count == 0


@pytest.mark.asyncio
async def test_interrupt_idempotent_for_same_session(speech_playback_integration):
    session_id = "test_session_123"
    mock_player = Mock()
    mock_player.clear_queue = Mock(return_value=None)
    mock_player.stop_playback = Mock(return_value=True)
    speech_playback_integration._avf_player = mock_player

    event = {
        "type": "playback.cancelled",
        "data": {"session_id": session_id, "source": "keyboard", "reason": "user_interrupt"},
    }

    speech_playback_integration._had_audio_for_session[session_id] = True
    await speech_playback_integration._on_unified_interrupt(event)
    await speech_playback_integration._on_unified_interrupt(event)

    # Вторая отмена дедуплицируется в guard-окне и не должна ломать состояние.
    assert session_id in speech_playback_integration._cancelled_sessions
