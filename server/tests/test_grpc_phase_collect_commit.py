#!/usr/bin/env python3
"""Tests for StreamAudio phase routing: COLLECT vs COMMIT."""

import sys
import uuid
from pathlib import Path
from unittest.mock import AsyncMock, Mock

import pytest

project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from modules.grpc_service import streaming_pb2
from modules.grpc_service.core.grpc_server import NewStreamingServicer


def _session_id() -> str:
    return str(uuid.uuid4())


async def _drain_stream(servicer: NewStreamingServicer, request: streaming_pb2.StreamRequest):
    context = Mock()
    responses = []
    async for resp in servicer.StreamAudio(request, context):
        responses.append(resp)
    return responses


@pytest.fixture
def servicer() -> NewStreamingServicer:
    manager = Mock()
    manager.initialize = AsyncMock(return_value=True)
    manager.cleanup = AsyncMock(return_value=None)
    manager.process = AsyncMock()
    manager.interrupt_workflow = Mock()
    manager.interrupt_workflow.check_interrupts = AsyncMock(return_value=False)

    s = NewStreamingServicer()
    s.grpc_service_manager = manager
    return s


@pytest.mark.asyncio
async def test_collect_phase_ack_without_workflow_processing(servicer: NewStreamingServicer) -> None:
    sid = _session_id()
    request = streaming_pb2.StreamRequest(
        prompt="",
        hardware_id="hw-collect-only",
        session_id=sid,
        phase=streaming_pb2.REQUEST_PHASE_COLLECT,
        chunk_seq=1,
        chunk_text="partial transcript",
    )

    responses = await _drain_stream(servicer, request)

    assert len(responses) == 1
    assert responses[0].WhichOneof("content") == "end_message"
    assert responses[0].end_message == "COLLECT_ACCEPTED"
    assert servicer.grpc_service_manager.process.call_count == 0


@pytest.mark.asyncio
async def test_commit_phase_consumes_buffered_collect_payload_when_prompt_empty(
    servicer: NewStreamingServicer,
) -> None:
    sid = _session_id()
    captured_request = {}

    async def _process(request_data):
        captured_request.update(request_data)
        yield {"success": True, "text_response": "ok"}

    servicer.grpc_service_manager.process = _process

    collect_request = streaming_pb2.StreamRequest(
        prompt="",
        screenshot="collect_screen_b64",
        screen_width=1920,
        screen_height=1080,
        hardware_id="hw-collect-commit",
        session_id=sid,
        phase=streaming_pb2.REQUEST_PHASE_COLLECT,
        chunk_seq=2,
        chunk_text="final buffered text",
    )
    collect_responses = await _drain_stream(servicer, collect_request)
    assert collect_responses[0].end_message == "COLLECT_ACCEPTED"

    commit_request = streaming_pb2.StreamRequest(
        prompt="",
        hardware_id="hw-collect-commit",
        session_id=sid,
        phase=streaming_pb2.REQUEST_PHASE_COMMIT,
    )
    commit_responses = await _drain_stream(servicer, commit_request)

    assert any(r.WhichOneof("content") == "text_chunk" for r in commit_responses)
    assert captured_request["text"] == "final buffered text"
    assert captured_request["screenshot"] == "collect_screen_b64"
    assert captured_request["screen_width"] == 1920
    assert captured_request["screen_height"] == 1080


@pytest.mark.asyncio
async def test_collect_chunk_seq_idempotency_ignores_older_chunks(
    servicer: NewStreamingServicer,
) -> None:
    sid = _session_id()
    captured_request = {}

    async def _process(request_data):
        captured_request.update(request_data)
        yield {"success": True, "text_response": "ok"}

    servicer.grpc_service_manager.process = _process

    req_seq2 = streaming_pb2.StreamRequest(
        prompt="",
        hardware_id="hw-idempotency",
        session_id=sid,
        phase=streaming_pb2.REQUEST_PHASE_COLLECT,
        chunk_seq=2,
        chunk_text="newer text",
    )
    req_seq1 = streaming_pb2.StreamRequest(
        prompt="",
        hardware_id="hw-idempotency",
        session_id=sid,
        phase=streaming_pb2.REQUEST_PHASE_COLLECT,
        chunk_seq=1,
        chunk_text="older text",
    )
    await _drain_stream(servicer, req_seq2)
    await _drain_stream(servicer, req_seq1)

    commit_request = streaming_pb2.StreamRequest(
        prompt="",
        hardware_id="hw-idempotency",
        session_id=sid,
        phase=streaming_pb2.REQUEST_PHASE_COMMIT,
    )
    await _drain_stream(servicer, commit_request)

    assert captured_request["text"] == "newer text"


@pytest.mark.asyncio
async def test_collect_commit_merges_delta_chunks_into_full_prompt(
    servicer: NewStreamingServicer,
) -> None:
    sid = _session_id()
    captured_request = {}

    async def _process(request_data):
        captured_request.update(request_data)
        yield {"success": True, "text_response": "ok"}

    servicer.grpc_service_manager.process = _process

    req_1 = streaming_pb2.StreamRequest(
        prompt="",
        hardware_id="hw-merge-delta",
        session_id=sid,
        phase=streaming_pb2.REQUEST_PHASE_COLLECT,
        chunk_seq=1,
        chunk_text="hello ",
    )
    req_2 = streaming_pb2.StreamRequest(
        prompt="",
        hardware_id="hw-merge-delta",
        session_id=sid,
        phase=streaming_pb2.REQUEST_PHASE_COLLECT,
        chunk_seq=2,
        chunk_text="world",
    )
    await _drain_stream(servicer, req_1)
    await _drain_stream(servicer, req_2)

    commit_request = streaming_pb2.StreamRequest(
        prompt="",
        hardware_id="hw-merge-delta",
        session_id=sid,
        phase=streaming_pb2.REQUEST_PHASE_COMMIT,
    )
    await _drain_stream(servicer, commit_request)

    assert captured_request["text"] == "hello world"


@pytest.mark.asyncio
async def test_collect_commit_merges_snapshot_and_commit_tail_without_losing_text(
    servicer: NewStreamingServicer,
) -> None:
    sid = _session_id()
    captured_request = {}

    async def _process(request_data):
        captured_request.update(request_data)
        yield {"success": True, "text_response": "ok"}

    servicer.grpc_service_manager.process = _process

    collect_request = streaming_pb2.StreamRequest(
        prompt="",
        hardware_id="hw-merge-snapshot",
        session_id=sid,
        phase=streaming_pb2.REQUEST_PHASE_COLLECT,
        chunk_seq=1,
        chunk_text="can you",
    )
    await _drain_stream(servicer, collect_request)

    # Commit carries only tail; final text must remain full merged request.
    commit_request = streaming_pb2.StreamRequest(
        prompt=" help me",
        hardware_id="hw-merge-snapshot",
        session_id=sid,
        phase=streaming_pb2.REQUEST_PHASE_COMMIT,
    )
    await _drain_stream(servicer, commit_request)

    assert captured_request["text"] == "can you help me"
