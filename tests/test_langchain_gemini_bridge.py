from modules.text_processing.providers.langchain_gemini_bridge import (
    build_image_user_content,
    build_runtime_system_prompt,
    build_text_user_content,
    normalize_runtime_generation_inputs,
    record_usage_if_available,
)


def test_normalize_runtime_generation_inputs_extracts_legacy_context() -> None:
    clean_user_input, runtime_memory_context, legacy_used = normalize_runtime_generation_inputs(
        user_input=(
            "MEMORY_CONTEXT:\n"
            "Current goal: user asks about weather\n\n"
            "USER_INPUT:\n"
            "what is the weather today"
        ),
        runtime_memory_context=None,
    )

    assert legacy_used is True
    assert "Current goal" in runtime_memory_context
    assert clean_user_input == "what is the weather today"


def test_build_runtime_system_prompt_appends_runtime_memory_context() -> None:
    prompt = build_runtime_system_prompt(
        route="messages",
        system_prompt_override=None,
        runtime_memory_context="Current goal: send a message",
        resolve_system_prompt=lambda route, override: f"route={route} override={override}",
    )

    assert "route=messages" in prompt
    assert "[Runtime Memory Context]" in prompt
    assert "Current goal: send a message" in prompt


def test_build_image_user_content_keeps_session_context() -> None:
    content = build_image_user_content(
        clean_user_input="what is on the screen",
        session_id="sid-1",
        image_mime_type="image/webp",
        image_b64="ZmFrZQ==",
    )

    assert content[0]["type"] == "text"
    assert "session_id=sid-1" in content[0]["text"]
    assert content[1]["image_url"]["url"] == "data:image/webp;base64,ZmFrZQ=="


def test_record_usage_if_available_uses_unknown_hardware_id_fallback() -> None:
    calls = []

    class _Tracker:
        def record_usage(self, **kwargs):
            calls.append(kwargs)

    record_usage_if_available(
        token_usage_tracker=_Tracker(),
        accumulated_usage={"input_tokens": 2, "output_tokens": 3},
        hardware_id=None,
        session_id="sid-1",
        model_name="gemini-test",
    )

    assert calls == [
        {
            "hardware_id": "unknown",
            "source": "main_llm",
            "input_tokens": 2,
            "output_tokens": 3,
            "session_id": "sid-1",
            "model_name": "gemini-test",
        }
    ]


def test_build_text_user_content_without_session_id_is_plain_text() -> None:
    assert build_text_user_content(clean_user_input="hello", session_id=None) == "hello"
