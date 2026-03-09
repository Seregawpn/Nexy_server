from integrations.core.assistant_response_parser_bridge import (
    build_command_payload,
    extract_json_from_markdown,
    normalize_text_response,
    validate_action_payload,
)


def test_extract_json_from_markdown_handles_fenced_json() -> None:
    raw = "```json\n{\"text\":\"hello\",}\n```"
    cleaned = extract_json_from_markdown(raw)
    assert cleaned == '{"text": "hello"}'


def test_normalize_text_response_non_string_returns_empty() -> None:
    assert normalize_text_response(123) == ""


def test_validate_action_payload_requires_browser_task() -> None:
    errors = validate_action_payload(
        command="browser_use",
        args={},
        session_id="sid",
        allowed_commands=["browser_use"],
    )
    assert "args.task" in errors[0]


def test_build_command_payload_shape() -> None:
    payload = build_command_payload(session_id="sid", command="open_app", args={"app_name": "Telegram"})
    assert payload["event"] == "mcp.command_request"
    assert payload["payload"]["session_id"] == "sid"
