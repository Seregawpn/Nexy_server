"""Unit tests for the PR-2 universal module interface helpers."""

from __future__ import annotations

import pytest

from integrations.core.module_status import ModuleState, ModuleStatus
from integrations.core.universal_module_interface import UniversalModuleInterface
from integrations.service_integrations.module_coordinator import ModuleCoordinator


class DummyModule(UniversalModuleInterface):
    """A minimal module implementation used to validate coordinator flows."""

    def __init__(self, name: str = "dummy") -> None:
        super().__init__(name=name)
        self._status = ModuleStatus(state=ModuleState.INIT)
        self._config = {}
        self._requests = []

    async def initialize(self, config: dict) -> None:
        self._config = config
        self._status = ModuleStatus(state=ModuleState.READY, health="ok")

    async def process(self, request):  # type: ignore[override]
        self._requests.append(request)
        self._status = ModuleStatus(state=ModuleState.PROCESSING, health="ok")
        self._status = ModuleStatus(state=ModuleState.READY, health="ok")
        return {"processed": True, "request": request}

    async def cleanup(self) -> None:
        self._status = ModuleStatus(state=ModuleState.STOPPED, health="down")

    def status(self) -> ModuleStatus:
        return self._status


@pytest.mark.asyncio
async def test_module_initialization_and_status() -> None:
    module = DummyModule("text")
    assert module.status().state is ModuleState.INIT

    await module.initialize({"foo": "bar"})

    status = module.status()
    assert status.state is ModuleState.READY
    assert status.health == "ok"


@pytest.mark.asyncio
async def test_module_process_roundtrip() -> None:
    module = DummyModule("processor")
    await module.initialize({})

    payload = {"data": "value"}
    response = await module.process(payload)

    assert response == {"processed": True, "request": payload}
    assert module.status().state is ModuleState.READY


@pytest.mark.asyncio
async def test_module_cleanup() -> None:
    module = DummyModule("cleanup")
    await module.initialize({})

    await module.cleanup()

    assert module.status().state is ModuleState.STOPPED


@pytest.mark.asyncio
async def test_coordinator_register_and_get() -> None:
    coordinator = ModuleCoordinator({})
    module = DummyModule("text")

    await coordinator.register("text_processing", module, {"foo": "bar"})

    assert coordinator.has("text_processing")
    assert coordinator.get("text_processing") is module


@pytest.mark.asyncio
async def test_coordinator_cleanup_all() -> None:
    coordinator = ModuleCoordinator({})
    first = DummyModule("first")
    second = DummyModule("second")

    await coordinator.register("cap1", first, {})
    await coordinator.register("cap2", second, {})

    await coordinator.cleanup_all()

    assert not coordinator.list_modules()
    assert not coordinator.list_capabilities()
    assert first.status().state is ModuleState.STOPPED
    assert second.status().state is ModuleState.STOPPED
