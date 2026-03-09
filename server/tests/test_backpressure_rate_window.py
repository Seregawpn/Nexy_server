import sys
from pathlib import Path

import pytest

project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from modules.grpc_service.core.backpressure import BackpressureManager, StreamLimits  # noqa: E402


@pytest.mark.asyncio
async def test_check_message_rate_uses_sliding_window_without_rebuilding_state() -> None:
    manager = BackpressureManager(
        StreamLimits(
            max_concurrent_streams=10,
            idle_timeout_seconds=0,
            max_message_rate_per_second=2,
            grace_period_seconds=0,
        )
    )

    acquired, error = await manager.acquire_stream("sid-rate", "hw-rate")
    assert acquired is True
    assert error is None

    allowed_1, error_1 = await manager.check_message_rate("sid-rate")
    allowed_2, error_2 = await manager.check_message_rate("sid-rate")
    blocked, blocked_error = await manager.check_message_rate("sid-rate")

    assert allowed_1 is True and error_1 is None
    assert allowed_2 is True and error_2 is None
    assert blocked is False
    assert blocked_error is not None

    stream_info = manager.active_streams["sid-rate"]
    assert hasattr(stream_info.message_timestamps, "popleft")
    assert len(stream_info.message_timestamps) == 2
