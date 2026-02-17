import asyncio
from typing import Any

import numpy as np
import pytest
import pytest_asyncio

from integration.core.error_handler import ErrorHandler
from integration.core.event_bus import EventBus
from integration.core.state_manager import ApplicationStateManager
from integration.integrations.speech_playback_integration import SpeechPlaybackIntegration


class FakeAVFPlayer:
    def __init__(self) -> None:
        self._initialized = True
        self._playing = False
        self._queue: list[np.ndarray] = []
        self.stop_calls = 0
        self.clear_calls = 0

    def initialize(self) -> bool:
        self._initialized = True
        return True

    def is_playing(self) -> bool:
        return self._playing

    def start_playback(self, *, reassert_session: bool = False) -> bool:
        self._playing = True
        return True

    def add_audio_data(self, audio_data: np.ndarray, metadata: dict[str, Any] | None = None):
        self._queue.append(audio_data)
        return f"chunk_{len(self._queue)}"

    def clear_queue(self) -> None:
        self.clear_calls += 1
        self._queue.clear()

    def stop_playback(self) -> bool:
        self.stop_calls += 1
        self._playing = False
        return True

    def is_queue_empty(self) -> bool:
        return True

    def get_buffered_audio_seconds(self) -> float:
        return 0.0

    def get_playback_runtime_status(self) -> dict[str, Any]:
        return {
            "playing_flag": self._playing,
            "thread_alive": False,
            "engine_running": True,
            "player_playing": self._playing,
            "route": "FakeRoute:UnitTest",
            "session_snapshot": {"route": "FakeRoute:UnitTest"},
        }


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
async def speech(event_bus, state_manager, error_handler):
    integration = SpeechPlaybackIntegration(
        event_bus=event_bus,
        state_manager=state_manager,
        error_handler=error_handler,
    )
    await integration.initialize()
    integration._avf_player = FakeAVFPlayer()
    integration._audio_diag_verbose = True
    yield integration
    await integration.stop()


@pytest.mark.asyncio
async def test_diagnostic_pipeline_grpc_start_complete_cancel_paths(speech, event_bus):
    sid = "04d52f95-ef3a-4387-a58f-cb78fb404877"
    published: list[tuple[str, dict[str, Any]]] = []

    async def capture(event):
        et = event.get("type")
        data = event.get("data", {})
        if et in {"playback.started", "playback.completed", "playback.cancelled"}:
            published.append((et, data))

    await event_bus.subscribe("playback.started", capture)
    await event_bus.subscribe("playback.completed", capture)
    await event_bus.subscribe("playback.cancelled", capture)

    # Step 1: grpc audio chunk (non-silent) should decode, start and confirm grpc start.
    pcm = np.array([12000, -12000, 8000, -8000], dtype=np.int16).tobytes()
    await speech._on_audio_chunk(
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

    assert speech._had_audio_for_session.get(sid) is True
    assert sid in speech._grpc_start_confirmed_sessions

    # Step 2: grpc completed with had-audio should finalize through silence task.
    await speech._on_grpc_completed({"data": {"session_id": sid}})
    deadline = asyncio.get_running_loop().time() + 1.0
    while asyncio.get_running_loop().time() < deadline:
        if any(e for e in published if e[0] == "playback.completed"):
            break
        await asyncio.sleep(0.05)

    completed_events = [e for e in published if e[0] == "playback.completed"]
    assert len(completed_events) == 1
    assert completed_events[0][1].get("session_id") == sid

    # Step 3: new session cancel race (grpc_cancel + unified_interrupt) should not create duplicate terminal paths.
    sid2 = "1acccfd3-fad8-4db2-a8f2-a95f23dcd951"
    speech._had_audio_for_session[sid2] = True
    # simulate both events arriving close
    await asyncio.gather(
        speech._on_grpc_cancel({"data": {"session_id": sid2}}),
        speech._on_unified_interrupt({"data": {"session_id": sid2}}),
    )

    cancelled_events = [e for e in published if e[0] == "playback.cancelled"]
    # grpc_cancel emits terminal cancel once; unified interrupt does cleanup only.
    assert len(cancelled_events) == 1
    assert cancelled_events[0][1].get("session_id") == sid2
    assert speech._terminal_event_by_session.get(sid2) == "playback.cancelled"
    assert sid2 in speech._finalized_sessions
