import asyncio
import sys
import importlib.util
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(PROJECT_ROOT))
sys.path.insert(0, str(PROJECT_ROOT / "server"))

from typing import Any, Awaitable, Callable, Optional

import pytest

from server.utils import metrics_collector


MODULE_PATH = PROJECT_ROOT / "server" / "modules" / "grpc_service" / "core" / "grpc_interceptor.py"
spec = importlib.util.spec_from_file_location("grpc_logging_interceptor", MODULE_PATH)
_grpc_logging_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(_grpc_logging_module)
LoggingInterceptor = _grpc_logging_module.LoggingInterceptor

class _DummyContext:
    def __init__(self) -> None:
        self.code = None
        self.details = None

    def set_code(self, code: Any) -> None:
        self.code = code

    def set_details(self, details: str) -> None:
        self.details = details


class _DummyHandler:
    def __init__(
        self,
        *,
        request_streaming: bool,
        response_streaming: bool,
        unary_unary: Optional[Callable[..., Awaitable[Any]]] = None,
        unary_stream: Optional[Callable[..., Awaitable[Any]]] = None,
        stream_unary: Optional[Callable[..., Awaitable[Any]]] = None,
        stream_stream: Optional[Callable[..., Awaitable[Any]]] = None,
    ) -> None:
        self.request_streaming = request_streaming
        self.response_streaming = response_streaming
        self.unary_unary = unary_unary
        self.unary_stream = unary_stream
        self.stream_unary = stream_unary
        self.stream_stream = stream_stream

    def _replace(self, **updates: Any) -> "_DummyHandler":
        cloned = _DummyHandler(
            request_streaming=self.request_streaming,
            response_streaming=self.response_streaming,
            unary_unary=self.unary_unary,
            unary_stream=self.unary_stream,
            stream_unary=self.stream_unary,
            stream_stream=self.stream_stream,
        )
        for key, value in updates.items():
            setattr(cloned, key, value)
        return cloned


class _DummyCallDetails:
    def __init__(self, method: str) -> None:
        self.method = method


@pytest.fixture
def anyio_backend():
    return "asyncio"


@pytest.fixture(autouse=True)
def _reset_metrics() -> None:
    collector = metrics_collector.get_metrics_collector()
    collector.reset()
    yield
    collector.reset()


@pytest.mark.anyio("asyncio")
async def test_unary_handler_is_wrapped() -> None:
    interceptor = LoggingInterceptor()

    async def unary_handler(request: Any, context: _DummyContext) -> str:
        return "ok"

    handler = _DummyHandler(request_streaming=False, response_streaming=False, unary_unary=unary_handler)

    async def continuation(call_details: _DummyCallDetails) -> _DummyHandler:
        return handler

    wrapped = await interceptor.intercept_service(continuation, _DummyCallDetails("/svc/Test"))
    assert wrapped is not handler
    assert wrapped is not None
    assert wrapped.request_streaming is False
    assert wrapped.response_streaming is False

    context = _DummyContext()
    response = await wrapped.unary_unary(object(), context)
    assert response == "ok"


class _AsyncIterator:
    def __init__(self, values: list[Any]):
        self._values = values

    def __aiter__(self) -> "_AsyncIterator":
        return self

    async def __anext__(self) -> Any:
        if not self._values:
            raise StopAsyncIteration
        await asyncio.sleep(0)
        return self._values.pop(0)


@pytest.mark.anyio("asyncio")
async def test_stream_stream_handler_preserves_flags_and_yields() -> None:
    interceptor = LoggingInterceptor()

    async def bidi_handler(iterator: _AsyncIterator, context: _DummyContext):
        async for value in iterator:
            yield value * 2

    handler = _DummyHandler(
        request_streaming=True,
        response_streaming=True,
        stream_stream=bidi_handler,
    )

    async def continuation(call_details: _DummyCallDetails) -> _DummyHandler:
        return handler

    wrapped = await interceptor.intercept_service(continuation, _DummyCallDetails("/svc/Bidi"))
    assert wrapped is not handler
    assert wrapped.request_streaming is True
    assert wrapped.response_streaming is True

    context = _DummyContext()
    iterator = _AsyncIterator([1, 2, 3])
    responses = []
    async for item in wrapped.stream_stream(iterator, context):
        responses.append(item)

    assert responses == [2, 4, 6]
