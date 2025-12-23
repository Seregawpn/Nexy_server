"""
Pytest configuration and fixtures for integration tests.
"""
import pytest
import asyncio
from integration.core.event_bus import EventBus
from integration.core.state_manager import ApplicationStateManager


@pytest.fixture
async def event_bus():
    """Create EventBus with attached loop for async tests.
    
    This fixture is async to ensure we're in an async context when attaching loop.
    Works with both @pytest.mark.anyio and @pytest.mark.asyncio decorators.
    """
    bus = EventBus()
    # Always attach loop in async context (for anyio/asyncio)
    try:
        loop = asyncio.get_running_loop()
        bus.attach_loop(loop)
    except RuntimeError:
        # Not in async context - this should not happen with @pytest.mark.anyio
        # But we handle it gracefully for compatibility
        pass
    return bus


@pytest.fixture
def state_manager():
    """Create ApplicationStateManager."""
    return ApplicationStateManager()


@pytest.fixture
async def event_bus_with_loop():
    """Create EventBus with attached loop for async tests."""
    bus = EventBus()
    loop = asyncio.get_running_loop()
    bus.attach_loop(loop)
    return bus

