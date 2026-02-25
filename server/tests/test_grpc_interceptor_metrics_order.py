import asyncio
from pathlib import Path
import sys
from unittest.mock import patch

project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from modules.grpc_service.core import grpc_interceptor


def test_response_streaming_records_decision_before_metric() -> None:
    interceptor = grpc_interceptor.LoggingInterceptor()

    async def handler(request, context):
        yield "ok"

    wrapped = interceptor._wrap_response_streaming(
        handler, "/streaming.StreamingService/StreamAudio"
    )

    calls = []

    def fake_record_decision(method: str, decision: str) -> None:
        calls.append(("decision", method, decision))

    def fake_record_metric(method: str, duration_ms: float, is_error: bool = False) -> None:
        calls.append(("metric", method, is_error))

    class Ctx:
        def set_code(self, *args, **kwargs):
            return None

        def set_details(self, *args, **kwargs):
            return None

    async def _consume():
        out = []
        async for item in wrapped(object(), Ctx()):
            out.append(item)
        return out

    with patch.object(grpc_interceptor, "record_decision_metric", side_effect=fake_record_decision):
        with patch.object(grpc_interceptor, "record_metric", side_effect=fake_record_metric):
            output = asyncio.run(_consume())

    assert output == ["ok"]
    assert calls[0][0] == "decision"
    assert calls[1][0] == "metric"
