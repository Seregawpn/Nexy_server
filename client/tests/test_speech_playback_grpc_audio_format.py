from unittest.mock import Mock

import numpy as np
import pytest
import pytest_asyncio

from integration.core.error_handler import ErrorHandler
from integration.core.event_bus import EventBus
from integration.core.state_manager import ApplicationStateManager
from integration.integrations.speech_playback_integration import SpeechPlaybackIntegration


@pytest.fixture
def event_bus():
    return EventBus()


@pytest.fixture
def state_manager(event_bus):
    manager = ApplicationStateManager()
    manager.attach_event_bus(event_bus)
    return manager


@pytest.fixture
def error_handler():
    return ErrorHandler()


@pytest_asyncio.fixture
async def speech_playback(event_bus, state_manager, error_handler):
    integration = SpeechPlaybackIntegration(
        event_bus=event_bus,
        state_manager=state_manager,
        error_handler=error_handler,
    )
    await integration.initialize()
    yield integration
    try:
        await integration.stop()
    except Exception:
        pass


@pytest.mark.asyncio
async def test_grpc_audio_chunk_decodes_int16_to_float_range(speech_playback):
    speech_playback._tts_auto_gain_enabled = False
    speech_playback._avf_player = Mock()
    speech_playback._avf_player.add_audio_data = Mock()

    async def _ready():
        return True

    speech_playback._ensure_player_ready = _ready

    sid = "e7d9f8dd-7ecf-4ef8-bf8d-20d0d2db17d1"
    pcm = np.array([3276, -3276, 1638, -1638], dtype=np.int16).tobytes()  # ~0.10 / ~0.05
    await speech_playback._on_audio_chunk(
        {
            "data": {
                "session_id": sid,
                "bytes": pcm,
                "dtype": "int16",
                "sample_rate": 48000,
                "channels": 1,
                "shape": [4],
            }
        }
    )

    speech_playback._avf_player.add_audio_data.assert_called_once()
    arr = speech_playback._avf_player.add_audio_data.call_args[0][0]
    assert arr.dtype == np.float32
    assert float(np.max(np.abs(arr))) == pytest.approx(0.09997, rel=1e-2)


@pytest.mark.asyncio
async def test_grpc_gain_is_not_pinned_by_near_silent_first_chunk(speech_playback):
    speech_playback._tts_auto_gain_enabled = True
    speech_playback._tts_target_peak = 0.35
    speech_playback._tts_max_gain = 6.0
    speech_playback._tts_min_peak_for_gain = 0.01

    speech_playback._avf_player = Mock()
    speech_playback._avf_player.add_audio_data = Mock()

    async def _ready():
        return True

    speech_playback._ensure_player_ready = _ready

    sid = "b194b7f1-6d88-4d95-bf37-5ebcf8f96fdb"

    # First chunk: near-silent lead-in, should NOT pin session gain to 1.0
    first = np.array([40, -40, 30, -30], dtype=np.int16).tobytes()
    await speech_playback._on_audio_chunk(
        {
            "data": {
                "session_id": sid,
                "bytes": first,
                "dtype": "int16",
                "sample_rate": 48000,
                "channels": 1,
                "shape": [4],
            }
        }
    )

    # Second chunk: meaningful speech amplitude; should be boosted
    second = np.array([3000, -3000, 2500, -2500], dtype=np.int16).tobytes()
    await speech_playback._on_audio_chunk(
        {
            "data": {
                "session_id": sid,
                "bytes": second,
                "dtype": "int16",
                "sample_rate": 48000,
                "channels": 1,
                "shape": [4],
            }
        }
    )

    assert speech_playback._avf_player.add_audio_data.call_count == 2
    second_arr = speech_playback._avf_player.add_audio_data.call_args_list[1][0][0]

    raw_peak = 3000.0 / 32768.0
    boosted_peak = float(np.max(np.abs(second_arr)))
    assert boosted_peak > raw_peak
    assert boosted_peak >= 0.20
    assert boosted_peak <= 0.98
