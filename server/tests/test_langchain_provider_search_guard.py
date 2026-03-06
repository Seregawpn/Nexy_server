from pathlib import Path
import sys
from types import SimpleNamespace

import pytest

project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from modules.text_processing.providers.langchain_gemini_provider import LangChainGeminiProvider


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


def test_select_llm_defaults_to_no_tools_when_use_search_is_none():
    provider = _provider()
    provider.llm_no_tools = object()
    provider.llm_with_tools = object()
    provider.llm = provider.llm_with_tools

    assert provider._select_llm(use_search=None) is provider.llm_no_tools


def test_normalize_model_text_response_extracts_inner_text():
    provider = _provider()
    nested = '{"session_id":"abc","text":"Grounded weather answer."}'
    assert provider._normalize_model_text_response(nested) == "Grounded weather answer."


@pytest.mark.asyncio
async def test_process_use_google_search_returns_grounded_plain_text(monkeypatch):
    provider = _provider()

    def _fake_sync_search(input_data: str, system_prompt: str):
        assert "Bitcoin" in input_data
        assert system_prompt == "system prompt"
        return "Bitcoin is 67123 USD.", True

    monkeypatch.setattr(provider, "_generate_grounded_search_text_sync", _fake_sync_search)

    chunks = []
    async for chunk in provider.process(
        "What is the current Bitcoin price?",
        session_id="sid-123",
        use_google_search=True,
    ):
        chunks.append(chunk)

    assert "".join(chunks) == "Bitcoin is 67123 USD."


@pytest.mark.asyncio
async def test_process_use_google_search_without_grounding_returns_model_text(monkeypatch):
    provider = _provider()

    def _fake_sync_search(_input_data: str, _system_prompt: str):
        return "Unverified answer", False

    monkeypatch.setattr(provider, "_generate_grounded_search_text_sync", _fake_sync_search)

    chunks = []
    async for chunk in provider.process(
        "Weather in Montreal today?",
        session_id="sid-456",
        use_google_search=True,
    ):
        chunks.append(chunk)

    assert "".join(chunks) == "Unverified answer"


@pytest.mark.asyncio
async def test_process_with_image_use_google_search_uses_same_guard(monkeypatch):
    provider = _provider()

    def _fake_sync_search(_input_data: str, _system_prompt: str):
        return "Montreal is -9C and cloudy.", True

    monkeypatch.setattr(provider, "_generate_grounded_search_text_sync", _fake_sync_search)

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
async def test_process_use_google_search_connect_error_falls_back_to_normal_assistant(monkeypatch):
    provider = _provider()
    provider.is_initialized = True

    class _FakeLLM:
        async def astream(self, _messages):
            yield SimpleNamespace(content="Fallback assistant answer.")

    provider.llm_no_tools = _FakeLLM()
    provider.llm = provider.llm_no_tools

    def _raise_connect_error(_input_data: str, _system_prompt: str):
        raise RuntimeError("ConnectError: nodename nor servname provided")

    monkeypatch.setattr(provider, "_generate_grounded_search_text_sync", _raise_connect_error)

    chunks = []
    async for chunk in provider.process(
        "Weather in Montreal today?",
        session_id="sid-connect",
        use_google_search=True,
    ):
        chunks.append(chunk)

    assert "".join(chunks) == "Fallback assistant answer."


@pytest.mark.asyncio
async def test_process_use_google_search_uses_langchain_tool_strategy_when_deterministic_empty(monkeypatch):
    provider = _provider()
    provider.is_initialized = True

    class _FakeToolLLM:
        async def astream(self, _messages):
            yield SimpleNamespace(content="Tool-based grounded weather answer.")

    provider.llm_with_tools = _FakeToolLLM()

    def _empty_search(_input_data: str, _system_prompt: str):
        return "", False

    monkeypatch.setattr(provider, "_generate_grounded_search_text_sync", _empty_search)

    chunks = []
    async for chunk in provider.process(
        "Weather in Montreal today?",
        session_id="sid-tool-fallback",
        use_google_search=True,
    ):
        chunks.append(chunk)

    assert "".join(chunks) == "Tool-based grounded weather answer."


@pytest.mark.asyncio
async def test_process_use_google_search_strict_policy_raises_on_empty_search(monkeypatch):
    provider = LangChainGeminiProvider(
        {
            "api_key": "test-key",
            "model": "gemini-2.5-flash",
            "temperature": 0.1,
            "max_tokens": 512,
            "tools": ["google_search"],
            "system_prompt": "system prompt",
            "search_model": "gemini-2.5-flash",
            "search_policy": "strict_search",
        }
    )
    provider.is_initialized = True

    class _FakeToolLLM:
        async def astream(self, _messages):
            if False:
                yield None

    provider.llm_with_tools = _FakeToolLLM()

    def _empty_search(_input_data: str, _system_prompt: str):
        return "", False

    monkeypatch.setattr(provider, "_generate_grounded_search_text_sync", _empty_search)

    with pytest.raises(RuntimeError, match="Google Search returned empty response across strategies"):
        async for _ in provider.process(
            "Weather in Montreal today?",
            session_id="sid-tool-strict",
            use_google_search=True,
        ):
            pass


@pytest.mark.asyncio
async def test_process_with_image_none_forwards_search_context():
    provider = _provider()
    provider.is_initialized = True

    captured = {}

    async def _fake_process(
        input_data: str,
        session_id=None,
        use_google_search=None,
        system_prompt_override=None,
        hardware_id=None,
        _retry_with_fallback_key=True,
    ):
        captured["input_data"] = input_data
        captured["session_id"] = session_id
        captured["use_google_search"] = use_google_search
        captured["system_prompt_override"] = system_prompt_override
        captured["hardware_id"] = hardware_id
        captured["_retry_with_fallback_key"] = _retry_with_fallback_key
        yield "ok"

    provider.process = _fake_process  # type: ignore[method-assign]

    chunks = []
    async for chunk in provider.process_with_image(
        input_data="Weather in Montreal today?",
        image_data=None,
        session_id="sid-none-image",
        use_google_search=True,
        system_prompt_override="prompt override",
        hardware_id="hw-123",
        _retry_with_fallback_key=False,
    ):
        chunks.append(chunk)

    assert "".join(chunks) == "ok"
    assert captured["input_data"] == "Weather in Montreal today?"
    assert captured["session_id"] == "sid-none-image"
    assert captured["use_google_search"] is True
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
    assert tracker.calls == []


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
