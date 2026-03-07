from pathlib import Path
import sys
from types import SimpleNamespace

import pytest

project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from modules.text_processing.providers.langchain_gemini_provider import (
    GoogleGenerativeAITool,
    LangChainGeminiProvider,
    extract_text_from_chunk,
)


def _provider() -> LangChainGeminiProvider:
    return LangChainGeminiProvider(
        {
            "api_key": "test-key",
            "model": "gemini-2.5-flash",
            "temperature": 0.1,
            "max_tokens": 512,
            "tools": ["google_search"],
            "system_prompt": "system prompt",
            "search_model": "gemini-2.5-flash",
        }
    )


def test_provider_builds_native_google_search_tool():
    tool = LangChainGeminiProvider._build_google_search_tool()

    if GoogleGenerativeAITool is not None:
        assert isinstance(tool, GoogleGenerativeAITool)
        assert getattr(tool, "google_search_retrieval", None) is not None
    else:
        assert tool == {"google_search_retrieval": {}}


def test_select_llm_defaults_to_no_tools_when_use_search_is_none():
    provider = _provider()
    provider.llm_no_tools = object()
    provider.llm_with_tools = object()
    provider.llm = provider.llm_with_tools

    assert provider._select_llm(use_search=None) is provider.llm_no_tools


def test_provider_builds_runtime_prompt_from_route():
    provider = _provider()

    prompt = provider._resolve_runtime_system_prompt(
        route="messages",
        system_prompt_override=None,
    )

    assert "MESSAGES ACTIONS" in prompt
    assert "WHATSAPP ACTIONS" not in prompt


def test_extract_text_from_chunk_returns_json_text_as_is():
    nested = '{"session_id":"abc","text":"Grounded weather answer."}'
    assert extract_text_from_chunk({"text": nested}) == nested


@pytest.mark.asyncio
async def test_process_use_google_search_streams_from_tool_llm():
    provider = _provider()
    provider.is_initialized = True

    class _FakeToolLLM:
        def __init__(self):
            self.messages = None

        async def astream(self, messages):
            self.messages = messages
            yield SimpleNamespace(content="Bitcoin is 67123 USD.")

    tool_llm = _FakeToolLLM()
    provider.llm_with_tools = tool_llm
    provider.llm = tool_llm

    chunks = []
    async for chunk in provider.process(
        "What is the current Bitcoin price?",
        session_id="sid-123",
        use_google_search=True,
    ):
        chunks.append(chunk)

    assert "".join(chunks) == "Bitcoin is 67123 USD."
    assert tool_llm.messages is not None


@pytest.mark.asyncio
async def test_process_use_google_search_falls_back_to_no_tools_when_tools_unavailable():
    provider = _provider()
    provider.is_initialized = True

    class _FakeLLM:
        async def astream(self, _messages):
            yield SimpleNamespace(content="Unverified answer")

    provider.llm_no_tools = _FakeLLM()
    provider.llm_with_tools = None
    provider.llm = provider.llm_no_tools

    chunks = []
    async for chunk in provider.process(
        "Weather in Montreal today?",
        session_id="sid-456",
        use_google_search=True,
    ):
        chunks.append(chunk)

    assert "".join(chunks) == "Unverified answer"


@pytest.mark.asyncio
async def test_process_with_image_use_google_search_streams_from_tool_llm():
    provider = _provider()
    provider.is_initialized = True

    class _FakeToolLLM:
        async def astream(self, _messages):
            yield SimpleNamespace(content="Montreal is -9C and cloudy.")

    provider.llm_with_tools = _FakeToolLLM()
    provider.llm = provider.llm_with_tools

    chunks = []
    async for chunk in provider.process_with_image(
        "Weather in Montreal today?",
        image_data="ZmFrZS1pbWFnZS1iYXNlNjQ=",
        session_id="sid-789",
        use_google_search=True,
    ):
        chunks.append(chunk)

    assert "".join(chunks) == "Montreal is -9C and cloudy."


@pytest.mark.asyncio
async def test_process_use_google_search_propagates_tool_llm_error():
    provider = _provider()
    provider.is_initialized = True

    class _FailingToolLLM:
        async def astream(self, _messages):
            if False:
                yield None
            raise RuntimeError("tool llm failed")

    provider.llm_with_tools = _FailingToolLLM()
    provider.llm = provider.llm_with_tools

    with pytest.raises(RuntimeError, match="tool llm failed"):
        async for _ in provider.process(
            "Weather in Montreal today?",
            session_id="sid-connect",
            use_google_search=True,
        ):
            pass


@pytest.mark.asyncio
async def test_process_use_google_search_uses_tool_llm_when_available():
    provider = _provider()
    provider.is_initialized = True

    class _FakeToolLLM:
        async def astream(self, _messages):
            yield SimpleNamespace(content="Tool-based grounded weather answer.")

    provider.llm_with_tools = _FakeToolLLM()
    provider.llm = provider.llm_with_tools

    chunks = []
    async for chunk in provider.process(
        "Weather in Montreal today?",
        session_id="sid-tool-fallback",
        use_google_search=True,
    ):
        chunks.append(chunk)

    assert "".join(chunks) == "Tool-based grounded weather answer."


@pytest.mark.asyncio
async def test_process_use_google_search_without_tool_llm_uses_default_llm():
    provider = _provider()
    provider.is_initialized = True

    class _FakeLLM:
        async def astream(self, _messages):
            yield SimpleNamespace(content="Default llm answer.")

    provider.llm_no_tools = _FakeLLM()
    provider.llm = provider.llm_no_tools
    provider.llm_with_tools = None

    chunks = []
    async for chunk in provider.process(
        "Weather in Montreal today?",
        session_id="sid-tool-strict",
        use_google_search=True,
    ):
        chunks.append(chunk)

    assert "".join(chunks) == "Default llm answer."


@pytest.mark.asyncio
async def test_process_with_image_none_forwards_search_context():
    provider = _provider()
    provider.is_initialized = True
    provider.llm_no_tools = object()
    provider.llm = provider.llm_no_tools

    captured = {}

    async def _fake_process(
        user_input: str,
        session_id=None,
        use_search=None,
        use_google_search=None,
        route=None,
        system_prompt_override=None,
        hardware_id=None,
        runtime_memory_context=None,
        _retry_with_fallback_key=True,
    ):
        captured["user_input"] = user_input
        captured["session_id"] = session_id
        captured["use_search"] = use_search
        captured["use_google_search"] = use_google_search
        captured["route"] = route
        captured["system_prompt_override"] = system_prompt_override
        captured["hardware_id"] = hardware_id
        captured["runtime_memory_context"] = runtime_memory_context
        captured["_retry_with_fallback_key"] = _retry_with_fallback_key
        yield "ok"

    provider.process = _fake_process  # type: ignore[method-assign]

    chunks = []
    async for chunk in provider.process_with_image(
        user_input="Weather in Montreal today?",
        image_data=None,
        session_id="sid-none-image",
        use_google_search=True,
        route="google_search",
        system_prompt_override="prompt override",
        hardware_id="hw-123",
        _retry_with_fallback_key=False,
    ):
        chunks.append(chunk)

    assert "".join(chunks) == "ok"
    assert captured["user_input"] == "Weather in Montreal today?"
    assert captured["session_id"] == "sid-none-image"
    assert captured["use_google_search"] is True
    assert captured["route"] == "google_search"
    assert captured["system_prompt_override"] == "prompt override"
    assert captured["hardware_id"] == "hw-123"
    assert captured["_retry_with_fallback_key"] is False


@pytest.mark.asyncio
async def test_token_usage_skipped_without_hardware_id():
    provider = _provider()
    provider.is_initialized = True

    class _Tracker:
        def __init__(self):
            self.calls = []

        def record_usage(self, **kwargs):
            self.calls.append(kwargs)

    class _FakeLLM:
        async def astream(self, _messages):
            yield SimpleNamespace(content="Hello", usage_metadata={"input_tokens": 1, "output_tokens": 2})

    tracker = _Tracker()
    provider.token_usage_tracker = tracker
    provider.llm_no_tools = _FakeLLM()
    provider.llm = provider.llm_no_tools

    chunks = []
    async for chunk in provider.process(
        "Hello",
        session_id="sid-no-hw",
        use_google_search=False,
        hardware_id=None,
    ):
        chunks.append(chunk)

    assert "".join(chunks) == "Hello"
    assert len(tracker.calls) == 1
    assert tracker.calls[0]["hardware_id"] == "unknown"


@pytest.mark.asyncio
async def test_token_usage_recorded_with_hardware_id():
    provider = _provider()
    provider.is_initialized = True

    class _Tracker:
        def __init__(self):
            self.calls = []

        def record_usage(self, **kwargs):
            self.calls.append(kwargs)

    class _FakeLLM:
        async def astream(self, _messages):
            yield SimpleNamespace(content="Hello", usage_metadata={"input_tokens": 3, "output_tokens": 4})

    tracker = _Tracker()
    provider.token_usage_tracker = tracker
    provider.llm_no_tools = _FakeLLM()
    provider.llm = provider.llm_no_tools

    chunks = []
    async for chunk in provider.process(
        "Hello",
        session_id="sid-with-hw",
        use_google_search=False,
        hardware_id="hw-42",
    ):
        chunks.append(chunk)

    assert "".join(chunks) == "Hello"
    assert len(tracker.calls) == 1
    assert tracker.calls[0]["hardware_id"] == "hw-42"
    assert tracker.calls[0]["session_id"] == "sid-with-hw"
