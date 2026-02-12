import asyncio
import os
import sys
from unittest.mock import AsyncMock

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from integration.integrations.welcome_message_integration import WelcomeMessageIntegration
from modules.welcome_message.core.types import WelcomeResult


class _DummyEventBus:
    async def subscribe(self, *_args, **_kwargs):
        return None

    async def unsubscribe(self, *_args, **_kwargs):
        return None

    async def publish(self, *_args, **_kwargs):
        return None


class _CaptureEventBus(_DummyEventBus):
    def __init__(self) -> None:
        self.published: list[str] = []

    async def publish(self, event_type, *_args, **_kwargs):
        self.published.append(str(event_type))
        return None


class _DummyStateManager:
    pass


class _DummyErrorHandler:
    pass


def _build_integration() -> WelcomeMessageIntegration:
    integration = WelcomeMessageIntegration(
        event_bus=_DummyEventBus(),  # type: ignore[arg-type]
        state_manager=_DummyStateManager(),  # type: ignore[arg-type]
        error_handler=_DummyErrorHandler(),  # type: ignore[arg-type]
        grpc_integration=None,
    )
    integration._running = True
    integration._playback_ready = True
    integration.config.enabled = True
    integration.config.delay_sec = 0.0
    integration._play_welcome_message = AsyncMock(return_value=None)  # type: ignore[method-assign]
    return integration


def test_welcome_plays_once_when_first_run_completed_then_ready_to_greet() -> None:
    async def _case() -> None:
        integration = _build_integration()
        await integration._on_first_run_completed({"data": {"source": "permissions.first_run_completed"}})
        await integration._on_ready_to_greet({"data": {"source": "permissions_v2"}})
        assert integration._play_welcome_message.await_count == 1

    asyncio.run(_case())


def test_welcome_plays_once_when_ready_to_greet_then_first_run_completed() -> None:
    async def _case() -> None:
        integration = _build_integration()
        await integration._on_ready_to_greet({"data": {"source": "permissions_v2"}})
        await integration._on_first_run_completed({"data": {"source": "permissions.first_run_completed"}})
        assert integration._play_welcome_message.await_count == 1

    asyncio.run(_case())


def test_first_run_completed_event_is_noop_for_welcome_trigger() -> None:
    async def _case() -> None:
        integration = _build_integration()
        await integration._on_first_run_completed({"data": {"source": "permissions.first_run_completed"}})
        assert integration._play_welcome_message.await_count == 0

    asyncio.run(_case())


def test_welcome_does_not_request_processing_mode_without_session_id() -> None:
    async def _case() -> None:
        event_bus = _CaptureEventBus()
        integration = WelcomeMessageIntegration(
            event_bus=event_bus,  # type: ignore[arg-type]
            state_manager=_DummyStateManager(),  # type: ignore[arg-type]
            error_handler=_DummyErrorHandler(),  # type: ignore[arg-type]
            grpc_integration=None,
        )
        integration._running = True
        integration._playback_ready = True
        integration.config.enabled = True
        integration.config.delay_sec = 0.0
        integration.welcome_player.play_welcome = AsyncMock(
            return_value=WelcomeResult(success=True, method="none", duration_sec=0.0)
        )
        integration.welcome_player.get_audio_data = lambda: None  # type: ignore[method-assign]
        integration._wait_for_playback_completion = AsyncMock(return_value=None)  # type: ignore[method-assign]

        await integration._on_ready_to_greet({"data": {"source": "permissions_v2"}})

        assert "mode.request" not in event_bus.published

    asyncio.run(_case())
