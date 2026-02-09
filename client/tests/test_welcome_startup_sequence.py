import asyncio
import os
import sys
from unittest.mock import AsyncMock

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from integration.integrations.welcome_message_integration import WelcomeMessageIntegration


class _DummyEventBus:
    async def subscribe(self, *_args, **_kwargs):
        return None

    async def unsubscribe(self, *_args, **_kwargs):
        return None

    async def publish(self, *_args, **_kwargs):
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
