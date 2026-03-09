import sys
from pathlib import Path
from unittest.mock import AsyncMock, Mock

import pytest

project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from integrations.workflow_integrations.streaming_workflow_integration import (  # noqa: E402
    RequestContext,
    StreamingWorkflowIntegration,
)


@pytest.mark.asyncio
async def test_emit_stream_segment_dedups_repeated_final_emit() -> None:
    text_module = Mock()
    text_module.is_initialized = True
    text_module.name = "text_processing"

    audio_module = Mock()
    audio_module.is_initialized = True
    audio_module.name = "audio_generation"
    audio_module.process = AsyncMock()

    workflow = StreamingWorkflowIntegration(
        text_processor=text_module,
        audio_processor=audio_module,
    )
    await workflow.initialize()

    async def _audio_stream():
        yield b"audio"

    async def _stream_audio_for_sentence(*_args, **_kwargs):
        async for chunk in _audio_stream():
            yield chunk

    workflow._stream_audio_for_sentence = _stream_audio_for_sentence

    ctx = RequestContext(session_id="sid-emit-dedup")

    first = []
    async for item in workflow._emit_stream_segment("Повтори меня.", ctx):
        first.append(item)

    second = []
    async for item in workflow._emit_stream_segment("Повтори меня.", ctx, log_label="final segment"):
        second.append(item)

    assert len(first) == 2
    assert first[0]["text_response"] == "Повтори меня."
    assert first[1]["audio_chunk"] == b"audio"
    assert second == []
    assert ctx.emitted_segment_counter == 1
    assert ctx.total_audio_chunks == 1
    assert ctx.captured_segments == ["Повтори меня."]


@pytest.mark.asyncio
async def test_early_text_preview_then_final_emit_yields_only_suffix() -> None:
    text_module = Mock()
    text_module.is_initialized = True
    text_module.name = "text_processing"

    audio_module = Mock()
    audio_module.is_initialized = True
    audio_module.name = "audio_generation"
    audio_module.process = AsyncMock()

    workflow = StreamingWorkflowIntegration(
        text_processor=text_module,
        audio_processor=audio_module,
    )
    await workflow.initialize()

    async def _stream_audio_for_sentence(*_args, **_kwargs):
        yield b"audio"

    workflow._stream_audio_for_sentence = _stream_audio_for_sentence
    workflow._split_complete_sentences = AsyncMock(return_value=([], ""))
    workflow._count_meaningful_words = AsyncMock(return_value=3)

    ctx = RequestContext(session_id="sid-early-preview", stream_buffer="Hello there")

    preview_events = []
    async for item in workflow._maybe_emit_early_text_preview(ctx, []):
        preview_events.append(item)

    final_events = []
    async for item in workflow._emit_stream_segment("Hello there, friend.", ctx):
        final_events.append(item)

    assert preview_events == [
        {
            "success": True,
            "text_response": "Hello there",
            "sentence_index": 0,
            "text_preview": True,
        }
    ]
    assert final_events[0]["text_response"] == ", friend."
    assert final_events[1]["audio_chunk"] == b"audio"
    assert ctx.captured_segments == ["Hello there, friend."]
