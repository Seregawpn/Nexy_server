import asyncio
import unittest

from integration.integrations.voiceover_ducking_integration import VoiceOverDuckingIntegration


class _DummyEventBus:
    async def subscribe(self, *_args, **_kwargs):
        return None


class _DummyStateManager:
    pass


class _DummyErrorHandler:
    def __init__(self):
        self.calls = []

    async def handle(self, exc, **kwargs):
        self.calls.append((exc, kwargs))


class _Mode:
    def __init__(self, value: str):
        self.value = value


class _FakeController:
    def __init__(self):
        self.applied_modes = []
        self.update_calls = 0
        self._in_apply = 0
        self.max_concurrency = 0

    async def update_voiceover_status(self):
        self.update_calls += 1
        await asyncio.sleep(0)

    async def apply_mode(self, mode: str):
        self._in_apply += 1
        self.max_concurrency = max(self.max_concurrency, self._in_apply)
        await asyncio.sleep(0.01)
        self.applied_modes.append(mode)
        self._in_apply -= 1


class VoiceOverDuckingModeGuardTests(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.error_handler = _DummyErrorHandler()
        self.integration = VoiceOverDuckingIntegration(
            event_bus=_DummyEventBus(),
            state_manager=_DummyStateManager(),
            error_handler=self.error_handler,
            config={},
        )
        self.integration.controller = _FakeController()
        self.integration._controller_ready = True

    async def test_duplicate_mode_events_are_coalesced(self):
        event = {"data": {"mode": _Mode("processing")}}
        await asyncio.gather(
            self.integration.handle_mode_change(event),
            self.integration.handle_mode_change(event),
            self.integration.handle_mode_change(event),
        )

        self.assertEqual(self.integration.controller.applied_modes, ["processing"])
        self.assertEqual(self.integration.controller.max_concurrency, 1)
        self.assertEqual(len(self.error_handler.calls), 0)

    async def test_different_modes_are_serialized_without_overlap(self):
        event_a = {"data": {"mode": _Mode("processing")}}
        event_b = {"data": {"mode": _Mode("sleeping")}}
        await asyncio.gather(
            self.integration.handle_mode_change(event_a),
            self.integration.handle_mode_change(event_b),
        )

        self.assertEqual(self.integration.controller.max_concurrency, 1)
        self.assertEqual(set(self.integration.controller.applied_modes), {"processing", "sleeping"})
        self.assertEqual(len(self.integration.controller.applied_modes), 2)
        self.assertEqual(len(self.error_handler.calls), 0)


if __name__ == "__main__":
    unittest.main()
