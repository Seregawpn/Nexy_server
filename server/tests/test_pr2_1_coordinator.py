"""Regression tests for the module coordinator integration (PR-2.1)."""

from __future__ import annotations

from pathlib import Path
from typing import Dict

import pytest
from unittest.mock import AsyncMock, patch

from integrations.core.module_status import ModuleState, ModuleStatus
from integrations.core.universal_module_interface import UniversalModuleInterface
from integrations.service_integrations.module_coordinator import ModuleCoordinator
from modules.grpc_service.core.grpc_service_manager import GrpcServiceManager


class StubModule(UniversalModuleInterface):
    """Small helper that mimics a UniversalModuleInterface module."""

    def __init__(self, name: str) -> None:
        super().__init__(name=name)
        self._status = ModuleStatus(state=ModuleState.INIT)
        self.config: Dict[str, str] = {}
        self.cleaned = False

    async def initialize(self, config: Dict[str, str]) -> None:
        self.config = config
        self._status = ModuleStatus(state=ModuleState.READY, health="ok")

    async def process(self, request):  # type: ignore[override]
        return {"request": request}

    async def cleanup(self) -> None:
        self.cleaned = True
        self._status = ModuleStatus(state=ModuleState.STOPPED, health="down")

    def status(self) -> ModuleStatus:
        return self._status


@pytest.fixture
def coordinator() -> ModuleCoordinator:
    return ModuleCoordinator({})


@pytest.mark.asyncio
async def test_coordinator_registers_modules(coordinator: ModuleCoordinator) -> None:
    module = StubModule("text")
    await coordinator.register("text_processing", module, {"foo": "bar"})

    assert coordinator.has("text_processing")
    assert coordinator.get("text_processing") is module


@pytest.mark.asyncio
async def test_coordinator_status_snapshot(coordinator: ModuleCoordinator) -> None:
    module = StubModule("text")
    await coordinator.register("text_processing", module, {})

    status = coordinator.get_status()
    assert status["modules_count"] == 1
    assert status["capabilities"]["text_processing"] == "text"


@pytest.mark.asyncio
async def test_coordinator_cleanup_marks_modules(coordinator: ModuleCoordinator) -> None:
    first = StubModule("first")
    second = StubModule("second")
    await coordinator.register("cap1", first, {})
    await coordinator.register("cap2", second, {})

    await coordinator.cleanup_all()

    assert coordinator.list_modules() == []
    assert first.cleaned and second.cleaned


@pytest.fixture
def grpc_manager() -> GrpcServiceManager:
    return GrpcServiceManager()


@pytest.mark.asyncio
async def test_grpc_manager_initialization_uses_coordinator(grpc_manager: GrpcServiceManager) -> None:
    with patch.object(grpc_manager.unified_config, "is_feature_enabled", return_value=True), patch.object(
        grpc_manager.unified_config, "is_kill_switch_active", return_value=False
    ), patch.object(grpc_manager, "_initialize_with_coordinator", new_callable=AsyncMock) as init_with_coord:
        await grpc_manager.initialize({})
        init_with_coord.assert_called_once()
        assert grpc_manager._use_coordinator is True


@pytest.mark.asyncio
async def test_grpc_manager_status_provides_state(grpc_manager: GrpcServiceManager) -> None:
    status = grpc_manager.status()
    assert isinstance(status, ModuleStatus)
    assert status.state is ModuleState.INIT


@pytest.mark.asyncio
async def test_grpc_manager_cleanup_invokes_coordinator(grpc_manager: GrpcServiceManager) -> None:
    grpc_manager.coordinator = AsyncMock()
    grpc_manager.grpc_service_integration = AsyncMock()
    grpc_manager.streaming_workflow = AsyncMock()
    grpc_manager.memory_workflow = AsyncMock()
    grpc_manager.interrupt_workflow = AsyncMock()

    await grpc_manager.cleanup()

    grpc_manager.coordinator.cleanup_all.assert_awaited()
    assert grpc_manager.status().state in {ModuleState.STOPPED, ModuleState.ERROR}


def test_grpc_manager_avoids_direct_module_imports() -> None:
    manager_file = Path(__file__).parent.parent / "modules" / "grpc_service" / "core" / "grpc_service_manager.py"
    content = manager_file.read_text(encoding="utf-8")

    forbidden_imports = [
        "from modules.text_processing",
        "from modules.audio_generation",
        "from modules.memory_management",
        "from modules.database",
        "from modules.session_management",
        "from modules.interrupt_handling",
        "from modules.text_filtering",
    ]

    for import_line in forbidden_imports:
        assert import_line not in content, f"Unexpected direct module import detected: {import_line}"

    assert "from integrations.core.module_factory import ModuleFactory" in content
    assert "ModuleFactory.create" in content
