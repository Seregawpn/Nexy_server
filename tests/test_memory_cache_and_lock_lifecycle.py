from datetime import datetime, timedelta, timezone

import pytest

from modules.memory_management.core.memory_manager import MemoryManager


@pytest.mark.asyncio
async def test_ephemeral_snapshot_cleanup_removes_expired_entries():
    manager = MemoryManager(db_manager=None)
    await manager._store_ephemeral_snapshot(
        "hw-cache",
        {
            "schema": "memory_v2",
            "updated_at": "",
            "short_current": {},
            "short_previous": [],
            "medium": "m1",
            "factual_long": "l1",
        },
    )

    async with manager._ephemeral_memory_lock:
        manager._ephemeral_memory["hw-cache"]["updated_at"] = (
            datetime.now(timezone.utc) - timedelta(hours=3)
        )

    removed = await manager.cleanup_inactive_short_term_cache(hours=1)
    snapshot_after = await manager._get_ephemeral_snapshot("hw-cache")

    assert removed == 1
    assert snapshot_after is None


@pytest.mark.asyncio
async def test_get_user_lock_reuses_same_lock_per_hardware_id():
    manager = MemoryManager(db_manager=None)

    first = await manager._get_user_lock("hw-1")
    second = await manager._get_user_lock("hw-1")
    third = await manager._get_user_lock("hw-2")

    assert first is second
    assert first is not third
    assert "hw-1" in manager._user_locks
    assert "hw-2" in manager._user_locks
