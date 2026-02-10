
import pytest
import asyncio
import json
from unittest.mock import MagicMock, AsyncMock
from integration.integrations.grpc_client_integration import GrpcClientIntegration, GrpcClientIntegrationConfig
from integration.core.event_bus import EventBus
from integration.core.state_manager import ApplicationStateManager
from integration.core.error_handler import ErrorHandler

# Mock response object that matches what grpc_client yields
class MockResponse:
    def __init__(self, text_chunk=None, action_chunk=None):
        self.text_chunk = text_chunk
        self.action_chunk = action_chunk
        self.audio_chunk = None
        self.browser_progress = None
        self.end_message = None
        self.error_message = None
        self.format = None
        self.sample_rate = None
        self.channels = None
    
    def WhichOneof(self, oneof_group):
        if oneof_group == 'content':
            if self.text_chunk: return 'text_chunk'
            if self.action_chunk: return 'action_message'
            if self.audio_chunk: return 'audio_chunk'
            if self.browser_progress: return 'browser_progress'
            if self.end_message: return 'end_message'
            if self.error_message: return 'error_message'
        return None

@pytest.fixture
def event_bus():
    return EventBus()

@pytest.fixture
def state_manager():
    return ApplicationStateManager()

@pytest.fixture
def integration(event_bus, state_manager):
    error_handler = ErrorHandler(event_bus)
    config = GrpcClientIntegrationConfig(server="test", aggregate_timeout_sec=0)
    # We need to mock the internal _client
    integration = GrpcClientIntegration(event_bus, state_manager, error_handler, config)
    integration._client = MagicMock()
    return integration

@pytest.mark.asyncio
async def test_legacy_text_action_dispatch(integration, event_bus):
    # Setup
    session_id = "test_session_legacy"
    integration._sessions[session_id] = {"text": "foo"} 
    
    # Mock stream_audio to yield a legacy action in text
    action_payload = {"command": "open_app", "args": {"name": "Calculator"}}
    legacy_text = "__MCP__" + json.dumps(action_payload)
    
    async def mock_stream(*args, **kwargs):
        yield MockResponse(text_chunk=legacy_text)
    
    integration._client.stream_audio = mock_stream
    integration._hardware_id = "hwid-123"
    integration._ensure_connected = AsyncMock(return_value=True)

    # Capture events
    events = []
    async def capture(event):
        events.append(event)
    await event_bus.subscribe("grpc.response.action", capture)
    await event_bus.subscribe("grpc.response.text", capture)
    
    # Execute
    await integration._send_in_grpc_loop(session_id)
    
    # Verify
    action_events = [e for e in events if e["type"] == "grpc.response.action"]
    text_events = [e for e in events if e["type"] == "grpc.response.text"]
    
    assert len(action_events) == 1
    # Check that payload is correctly normalized/passed
    # Note: depends on implementation details, but expectation is valid JSON string in 'action_json'
    data = json.loads(action_events[0]["data"]["action_json"])
    assert data["command"] == action_payload["command"]
    assert data["args"] == action_payload["args"]
    assert action_events[0]["data"]["source"] == "text_chunk_legacy"
    
    # Should NOT emit text event for the legacy action text
    assert len(text_events) == 0

@pytest.mark.asyncio
async def test_deduplication_legacy_and_new(integration, event_bus):
     # Setup
    session_id = "test_session_dedup"
    integration._sessions[session_id] = {"text": "foo"}
    
    action_payload = {"command": "open_app", "args": {"name": "Calculator"}}
    legacy_text = "__MCP__" + json.dumps(action_payload)
    
    # Yield both legacy text AND formal action message
    # Mock ActionMessage structure (needs .command and .args attributes possibly, or just dict depending on protobuf map)
    # The actual grpc client returns a protobuf object.
    # GrpcClientIntegration usually accesses resp.action_message.action_json
    
    mock_action_msg = MagicMock()
    mock_action_msg.action_json = json.dumps({"command": "open_app", "args": {"name": "Calculator"}})
    mock_action_msg.session_id = session_id
    mock_action_msg.feature_id = "test-feature"

    async def mock_stream(*args, **kwargs):
        # 1. Legacy text comes first
        yield MockResponse(text_chunk=legacy_text)
        # 2. Action chunk comes second
        yield MockResponse(action_chunk=mock_action_msg)
    
    integration._client.stream_audio = mock_stream
    integration._hardware_id = "hwid-123"
    integration._ensure_connected = AsyncMock(return_value=True)
    
    events = []
    async def capture(event):
        events.append(event)
    await event_bus.subscribe("grpc.response.action", capture)
    
    await integration._send_in_grpc_loop(session_id)
    
    # Should only process the first one (legacy text in this order)
    # If the logic is correct, it sets action_dispatched=True after first, and ignores second
    assert len(events) == 1

@pytest.mark.asyncio
async def test_legacy_json_text_dispatch(integration, event_bus):
    # Setup - test robust JSON detection without __MCP__ prefix but valid action signature
    session_id = "test_session_json"
    integration._sessions[session_id] = {"text": "foo"}
    
    action_payload = {"event": "mcp.command_request", "payload": {"command": "open_app", "args": {}}}
    # Sometimes it's wrapped in event/payload, sometimes direct. Reference legacy check.
    # Plan says: "event": "mcp.command_request" ... payload"
    
    legacy_text = json.dumps(action_payload)
    
    async def mock_stream(*args, **kwargs):
        yield MockResponse(text_chunk=legacy_text)
        
    integration._client.stream_audio = mock_stream
    integration._hardware_id = "hwid-123"
    integration._ensure_connected = AsyncMock(return_value=True)
    
    events = []
    async def capture(event):
        events.append(event)
    await event_bus.subscribe("grpc.response.action", capture)
    
    await integration._send_in_grpc_loop(session_id)
    
    assert len(events) == 1
    data = json.loads(events[0]["data"]["action_json"])
    assert data["command"] == "open_app"

@pytest.mark.asyncio
async def test_full_cycle_mixed_conversation(integration, event_bus):
    # Setup - simulate a full turn: "Opening..." (text) -> Action -> "Done" (text)
    session_id = "test_session_full_cycle"
    integration._sessions[session_id] = {"text": "user request"}
    
    # 1. First text chunk
    text_1 = "Okay, opening calculator."
    # 2. Legacy action chunk
    action_payload = {"command": "open_app", "args": {"name": "Calculator"}}
    legacy_action_text = "__MCP__" + json.dumps(action_payload)
    # 3. Second text chunk (after action)
    text_2 = " I have opened it."
    
    async def mock_stream(*args, **kwargs):
        yield MockResponse(text_chunk=text_1)
        # Yield action as legacy text
        yield MockResponse(text_chunk=legacy_action_text)
        yield MockResponse(text_chunk=text_2)
        
    integration._client.stream_audio = mock_stream
    integration._hardware_id = "hwid-123"
    integration._ensure_connected = AsyncMock(return_value=True)
    
    events = []
    async def capture(event):
        events.append(event)
    
    await event_bus.subscribe("grpc.response.text", capture)
    await event_bus.subscribe("grpc.response.action", capture)
    
    # Execute
    await integration._send_in_grpc_loop(session_id)
    
    # Verify sequence
    # Expected: 
    # 1. text event (text_1)
    # 2. action event (legacy_action_text payload)
    # 3. text event (text_2)
    # Crucially: legacy_action_text should NOT be emitted as text event
    
    text_events = [e for e in events if e["type"] == "grpc.response.text"]
    action_events = [e for e in events if e["type"] == "grpc.response.action"]
    
    assert len(action_events) == 1
    assert len(text_events) == 2
    
    # Check content
    assert text_events[0]["data"]["text"] == text_1
    assert text_events[1]["data"]["text"] == text_2
    
    action_data = json.loads(action_events[0]["data"]["action_json"])
    assert action_data["command"] == "open_app"
    
    # Verify strict ordering in the event list
    assert events[0]["type"] == "grpc.response.text"
    assert events[1]["type"] == "grpc.response.action"
    assert events[2]["type"] == "grpc.response.text"

@pytest.mark.asyncio
async def test_all_legacy_action_types(integration, event_bus):
    # Verify that specific known commands are correctly parsed from legacy text
    # We must use separate sessions because of the single-action-per-stream guard
    
    events = []
    async def capture(event):
        events.append(event)
    await event_bus.subscribe("grpc.response.action", capture)

    # 1. open_app
    payload_open = {"command": "open_app", "args": {"name": "Safari"}}
    text_open = "__MCP__" + json.dumps(payload_open)
    
    # 2. close_app
    payload_close = {"command": "close_app", "args": {"name": "Notes"}}
    text_close = "__MCP__" + json.dumps(payload_close)
    
    # 3. browser_use
    payload_browser = {"command": "browser_use", "args": {"text": "search google", "url": "https://google.com"}}
    text_browser = "__MCP__" + json.dumps(payload_browser)

    # Queue of response lists
    scenarios = [
        [MockResponse(text_chunk=text_open)],
        [MockResponse(text_chunk=text_close)],
        [MockResponse(text_chunk=text_browser)],
    ]
    
    async def mock_router(*args, **kwargs):
        if not scenarios:
            return 
        current_responses = scenarios.pop(0)
        for resp in current_responses:
            yield resp

    # Setup mocks
    integration._client.stream_audio = mock_router
    integration._hardware_id = "hwid-123"
    integration._ensure_connected = AsyncMock(return_value=True)
    
    # Pre-configure sessions so _send_in_grpc_loop proceeds
    integration._sessions["session_open"] = {"text": "dummy"}
    integration._sessions["session_close"] = {"text": "dummy"}
    integration._sessions["session_browser"] = {"text": "dummy"}
    
    await integration._send_in_grpc_loop("session_open")
    await integration._send_in_grpc_loop("session_close")
    await integration._send_in_grpc_loop("session_browser")
    
    assert len(events) == 3
    
    data_open = json.loads(events[0]["data"]["action_json"])
    assert data_open["command"] == "open_app"
    assert data_open["args"]["name"] == "Safari"
    
    data_close = json.loads(events[1]["data"]["action_json"])
    assert data_close["command"] == "close_app"
    assert data_close["args"]["name"] == "Notes"
    
    data_browser = json.loads(events[2]["data"]["action_json"])
    assert data_browser["command"] == "browser_use"
    assert data_browser["args"]["url"] == "https://google.com"


@pytest.mark.asyncio
async def test_message_actions_legacy(integration, event_bus):
    # Verify legacy format support for message-related commands
    
    events = []
    async def capture(event):
        events.append(event)
    await event_bus.subscribe("grpc.response.action", capture)

    # 1. send_message
    payload_send = {
        "command": "send_message", 
        "args": {"contact": "John Doe", "message": "Hello world"}
    }
    text_send = "__MCP__" + json.dumps(payload_send)
    
    # 2. read_messages
    payload_read = {
        "command": "read_messages", 
        "args": {"contact": "Alice", "limit": 5}
    }
    text_read = "__MCP__" + json.dumps(payload_read)
    
    # 3. find_contact
    payload_find = {
        "command": "find_contact", 
        "args": {"query": "Bob"}
    }
    text_find = "__MCP__" + json.dumps(payload_find)

    # Queue of response lists
    scenarios = [
        [MockResponse(text_chunk=text_send)],
        [MockResponse(text_chunk=text_read)],
        [MockResponse(text_chunk=text_find)],
    ]
    
    async def mock_router(*args, **kwargs):
        if not scenarios:
            return 
        current_responses = scenarios.pop(0)
        for resp in current_responses:
            yield resp

    # Setup mocks
    integration._client.stream_audio = mock_router
    integration._hardware_id = "hwid-123"
    integration._ensure_connected = AsyncMock(return_value=True)
    
    # Pre-configure sessions
    integration._sessions["session_send"] = {"text": "dummy"}
    integration._sessions["session_read"] = {"text": "dummy"}
    integration._sessions["session_find"] = {"text": "dummy"}
    
    await integration._send_in_grpc_loop("session_send")
    await integration._send_in_grpc_loop("session_read")
    await integration._send_in_grpc_loop("session_find")
    
    assert len(events) == 3
    
    data_send = json.loads(events[0]["data"]["action_json"])
    assert data_send["command"] == "send_message"
    assert data_send["args"]["contact"] == "John Doe"
    
    data_read = json.loads(events[1]["data"]["action_json"])
    assert data_read["command"] == "read_messages"
    assert data_read["args"]["limit"] == 5
    
    data_find = json.loads(events[2]["data"]["action_json"])
    assert data_find["command"] == "find_contact"
    assert data_find["args"]["query"] == "Bob"


@pytest.mark.asyncio
async def test_mixed_wrapper_action(integration, event_bus):
    # Verify support for nested wrappers: __MCP__ + markdown + json
    
    events = []
    async def capture(event):
        events.append(event)
    await event_bus.subscribe("grpc.response.action", capture)

    # Payload: __MCP__ then ```json ... ```
    payload = {
        "command": "send_message", 
        "args": {"message": "nested wrapper test"}
    }
    json_str = json.dumps(payload)
    mixed_text = f"__MCP__```json\n{json_str}\n```"

    # Queue response
    scenarios = [[MockResponse(text_chunk=mixed_text)]]
    
    async def mock_router(*args, **kwargs):
        if not scenarios: return 
        for resp in scenarios.pop(0): yield resp

    # Setup
    integration._client.stream_audio = mock_router
    integration._hardware_id = "hwid-123"
    integration._ensure_connected = AsyncMock(return_value=True)
    integration._sessions["session_mixed"] = {"text": "dummy"}
    
    await integration._send_in_grpc_loop("session_mixed")
    
    # Assert
    assert len(events) == 1
    data = json.loads(events[0]["data"]["action_json"])
    assert data["command"] == "send_message"
    assert data["args"]["message"] == "nested wrapper test"


@pytest.mark.asyncio
async def test_e2e_comprehensive_verification(integration, event_bus):
    """
    Simulates the full pipeline for ALL action types with various formatting quirks.
    Verifies that the client correctly:
    1. Receives mixed text/legacy/markdown.
    2. Parses the action payload.
    3. Dispatches grpc.response.action.
    4. DOES NOT dispatch the action text as speech.
    """
    
    events = []
    async def capture(event):
        events.append(event)
    await event_bus.subscribe("grpc.response.action", capture)
    await event_bus.subscribe("grpc.response.text", capture)

    # Define scenarios with different formats
    scenarios = [
        # 1. Clean Open App (Standard legacy)
        {
            "id": "scenario_open_app",
            "format": "standard",
            "payload": {"command": "open_app", "args": {"name": "Calculator"}},
            "text_wrapper": lambda p: f"__MCP__{json.dumps(p)}"
        },
        # 2. Browser Use (Markdown fenced)
        {
            "id": "scenario_browser",
            "format": "markdown",
            "payload": {"command": "browser_use", "args": {"url": "https://example.com"}},
            "text_wrapper": lambda p: f"```json\n{json.dumps(p)}\n```"
        },
        # 3. Send Message (Mixed: __MCP__ + Markdown) - THE FIX VERIFICATION
        {
            "id": "scenario_message",
            "format": "mixed",
            "payload": {"command": "send_message", "args": {"message": "Hello!"}},
            "text_wrapper": lambda p: f"__MCP__```json\n{json.dumps(p)}\n```"
        }
    ]

    # Create mock router
    response_queue = []
    for sc in scenarios:
        # Each scenario gets its own session and response list
        integration._sessions[sc["id"]] = {"text": "dummy"}
        
        text_payload = sc["text_wrapper"](sc["payload"])
        # Sequence: Text -> Action -> Text
        response_queue.append([
            MockResponse(text_chunk=f"Starting {sc['id']}..."),
            MockResponse(text_chunk=text_payload),
            MockResponse(text_chunk="Done.")
        ])

    async def mock_router(*args, **kwargs):
        if not response_queue: return 
        for resp in response_queue.pop(0): yield resp

    # Setup mocks
    integration._client.stream_audio = mock_router
    integration._hardware_id = "hwid-123"
    integration._ensure_connected = AsyncMock(return_value=True)

    # Execute all scenarios
    for sc in scenarios:
        await integration._send_in_grpc_loop(sc["id"])

    # --- VERIFICATION ---
    
    action_events = [e for e in events if e["type"] == "grpc.response.action"]
    text_events = [e for e in events if e["type"] == "grpc.response.text"]
    
    # 1. Check Action Count
    assert len(action_events) == 3, f"Expected 3 actions, got {len(action_events)}"
    
    # 2. Check Action Payloads
    for i, event in enumerate(action_events):
        data = json.loads(event["data"]["action_json"])
        expected = scenarios[i]["payload"]
        assert data["command"] == expected["command"]
        assert data["args"] == expected["args"]
        print(f"✅ Verified {expected['command']} ({scenarios[i]['format']})")

    # 3. Check Text Events (Should NOT contain action JSON)
    # We expect 2 text events per scenario (Start + Done) = 6 total
    assert len(text_events) == 6
    for evt in text_events:
        txt = evt["data"]["text"]
        assert "command" not in txt, f"Leaked action JSON in text: {txt}"
        assert "__MCP__" not in txt
        print(f"✅ Verified text clean: '{txt}'")






