import pytest
from pathlib import Path
import sys

# Добавляем путь к корню проекта
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from modules.memory_management.adapter import MemoryManagementAdapter


class _FakeMemoryManager:
    instances = []

    def __init__(self, db_manager=None, token_usage_tracker=None):
        self.db_manager = db_manager
        self.token_usage_tracker = token_usage_tracker
        self.cleanup_calls = []
        _FakeMemoryManager.instances.append(self)

    async def initialize(self):
        return True

    async def cleanup_expired_memory(self, hours=24):
        self.cleanup_calls.append(hours)
        return 1

    def set_database_manager(self, db_manager):
        self.db_manager = db_manager


@pytest.mark.asyncio
async def test_short_term_cleanup_loop_runs_with_idle_hours_2(monkeypatch):
    monkeypatch.setattr(
        "modules.memory_management.adapter.MemoryManager",
        _FakeMemoryManager,
    )
    _FakeMemoryManager.instances.clear()

    adapter = MemoryManagementAdapter()
    await adapter.initialize(
        {
            "short_term_cleanup_enabled": True,
            "short_term_cleanup_interval_seconds": 60,
            "short_term_cleanup_idle_hours": 2,
        }
    )

    fake_manager = _FakeMemoryManager.instances[0]
    await adapter._run_short_term_cleanup_once()
    assert fake_manager.cleanup_calls == [2]

    await adapter.cleanup()


@pytest.mark.asyncio
async def test_short_term_cleanup_task_stopped_on_cleanup(monkeypatch):
    monkeypatch.setattr(
        "modules.memory_management.adapter.MemoryManager",
        _FakeMemoryManager,
    )
    _FakeMemoryManager.instances.clear()

    adapter = MemoryManagementAdapter()
    await adapter.initialize(
        {
            "short_term_cleanup_enabled": True,
            "short_term_cleanup_interval_seconds": 60,
            "short_term_cleanup_idle_hours": 2,
        }
    )

    assert adapter._cleanup_task is not None
    assert not adapter._cleanup_task.done()

    await adapter.cleanup()

    assert adapter._cleanup_task is None
