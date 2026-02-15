import pytest

from integration.core.event_bus import EventBus


class _Handler:
    def __init__(self):
        self.calls = 0

    async def on_event(self, event):
        self.calls += 1


@pytest.mark.asyncio
async def test_event_bus_dedups_same_bound_method_subscription():
    bus = EventBus()
    handler = _Handler()

    await bus.subscribe("test.event", handler.on_event)
    await bus.subscribe("test.event", handler.on_event)

    assert len(bus.subscribers.get("test.event", [])) == 1

    await bus.publish("test.event", {"value": 1})
    assert handler.calls == 1


@pytest.mark.asyncio
async def test_event_bus_keeps_different_instances_subscribed():
    bus = EventBus()
    handler_a = _Handler()
    handler_b = _Handler()

    await bus.subscribe("test.event", handler_a.on_event)
    await bus.subscribe("test.event", handler_b.on_event)

    assert len(bus.subscribers.get("test.event", [])) == 2

    await bus.publish("test.event", {"value": 1})
    assert handler_a.calls == 1
    assert handler_b.calls == 1


@pytest.mark.asyncio
async def test_event_bus_unsubscribe_uses_same_bound_method_key():
    bus = EventBus()
    handler = _Handler()

    await bus.subscribe("test.event", handler.on_event)
    await bus.unsubscribe("test.event", handler.on_event)

    assert "test.event" not in bus.subscribers
