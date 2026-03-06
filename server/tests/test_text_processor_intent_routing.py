import sys
from pathlib import Path
from unittest.mock import AsyncMock

import pytest
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from modules.text_processing.core.text_processor import TextProcessor


def test_extract_intent_text_from_enriched_prompt():
    enriched = (
        "MEMORY_CONTEXT:\n"
        "Subscription Status: paid\n"
        "Memory Context: something\n\n"
        "USER_INPUT:\n"
        "how are you today"
    )
    assert TextProcessor._extract_intent_text(enriched) == "how are you today"

@pytest.mark.asyncio
async def test_text_processor_classifier_route_whatsapp():
    tp = TextProcessor(config={})
    tp.live_provider.classify_intent_decision = AsyncMock(return_value={"category": "whatsapp"})
    prompt, sections, normalized_text, routing_context = await tp._build_prompt_for_text("send hello in WhatsApp")

    assert sections["primary_route"] == "whatsapp"
    assert sections["whatsapp"] is True
    assert sections["messages"] is False
    assert sections["browser"] is False
    assert sections["payment"] is False
    assert normalized_text == "send hello in WhatsApp"
    assert "primary_route: whatsapp" in routing_context
    assert "has_image: false" in routing_context
    assert isinstance(prompt, str) and len(prompt) > 0
    tp.live_provider.classify_intent_decision.assert_awaited_once()


@pytest.mark.asyncio
async def test_text_processor_classifier_route_open_youtube_to_browser():
    tp = TextProcessor(config={})
    tp.live_provider.classify_intent_decision = AsyncMock(return_value={"category": "browser"})
    _, sections, normalized_text, _ = await tp._build_prompt_for_text("open YouTube")

    assert sections["primary_route"] == "browser"
    assert sections["browser"] is True
    assert sections["google_search"] is False
    assert normalized_text == "open YouTube"
    tp.live_provider.classify_intent_decision.assert_awaited_once()


@pytest.mark.asyncio
async def test_text_processor_continuation_forces_tier_c_classifier():
    tp = TextProcessor(config={})
    tp.live_provider.classify_intent_decision = AsyncMock(return_value={"category": "messages"})

    enriched = "USER_INPUT:\ntell me more"
    _, _, normalized_text, _ = await tp._build_prompt_for_text(enriched)
    assert normalized_text.endswith("tell me more")
    tp.live_provider.classify_intent_decision.assert_awaited_once()


@pytest.mark.asyncio
async def test_text_processor_conflict_whatsapp_imessage_falls_back_to_tier_c():
    tp = TextProcessor(config={})
    tp.live_provider.classify_intent_decision = AsyncMock(return_value={"category": "none"})

    _, sections, _, _ = await tp._build_prompt_for_text("open whatsapp and imessage now")
    assert sections["primary_route"] == "none"
    tp.live_provider.classify_intent_decision.assert_awaited_once()


@pytest.mark.asyncio
async def test_text_processor_conflict_capability_and_action_falls_back_to_tier_c():
    tp = TextProcessor(config={})
    tp.live_provider.classify_intent_decision = AsyncMock(return_value={"category": "messages"})

    _, sections, _, routing_context = await tp._build_prompt_for_text("can you send her how are you doing today")
    assert sections["primary_route"] == "messages"
    assert "primary_route: messages" in routing_context
    tp.live_provider.classify_intent_decision.assert_awaited_once()


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "user_text,classifier_category,expected_route,expected_reason,classifier_called",
    [
        (
            "snd mesage to sofiya how r u",
            "messages",
            "messages",
            "classifier_only",
            True,
        ),
        (
            "wht on scren nw",
            "describe",
            "describe",
            "classifier_only",
            True,
        ),
        (
            "opn yotube n ply lofi",
            "browser",
            "browser",
            "classifier_only",
            True,
        ),
        (
            "lates news in world tday",
            "google_search",
            "google_search",
            "classifier_only",
            True,
        ),
        (
            "can send msg to sofiya",
            "messages",
            "messages",
            "classifier_only",
            True,
        ),
        (
            "snd msg to sofiya how r u",
            "messages",
            "messages",
            "classifier_only",
            True,
        ),
        (
            "smd mesage to sofiya",
            "messages",
            "messages",
            "classifier_only",
            True,
        ),
    ],
)
async def test_text_processor_ragged_queries_routing(
    user_text: str,
    classifier_category: str,
    expected_route: str,
    expected_reason: str,
    classifier_called: bool,
):
    tp = TextProcessor(config={})
    tp.live_provider.classify_intent_decision = AsyncMock(return_value={"category": classifier_category})

    _, sections, _, routing_context = await tp._build_prompt_for_text(user_text, session_id="ragged-1")

    assert sections["primary_route"] == expected_route
    assert f"primary_route: {expected_route}" in routing_context
    if classifier_called:
        tp.live_provider.classify_intent_decision.assert_awaited_once()
    else:
        tp.live_provider.classify_intent_decision.assert_not_awaited()


@pytest.mark.asyncio
async def test_text_processor_no_can_capability_shortcut_for_message_like_input():
    tp = TextProcessor(config={})
    tp.live_provider.classify_intent_decision = AsyncMock(return_value={"category": "messages"})

    _, sections, _, routing_context = await tp._build_prompt_for_text("can snd msg to sofiya")

    assert sections["primary_route"] == "messages"
    assert "primary_route: messages" in routing_context
    tp.live_provider.classify_intent_decision.assert_awaited_once()


@pytest.mark.asyncio
async def test_text_processor_contextual_followup_browser_find_keeps_browser_route():
    tp = TextProcessor(config={})
    tp.live_provider.classify_intent_decision = AsyncMock(return_value={"category": "google_search"})

    _, sections, _, routing_context = await tp._build_prompt_for_text(
        "find lofi focus mix",
        session_id="browser-followup-1",
        runtime_memory_context=(
            "Short-term memory:\n"
            "Current/recent dialogue turns (USER/ASSISTANT order).\n"
            "USER: open youtube and find\n"
            "ASSISTANT: What should I find on YouTube?\n\n"
            "Medium-term memory:\n"
            "No data"
        ),
    )

    assert sections["primary_route"] == "google_search"
    assert "primary_route: google_search" in routing_context
    tp.live_provider.classify_intent_decision.assert_awaited_once()


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "user_text,short_term_memory,classifier_category,expected_route",
    [
        (
            "send",
            None,
            "messages",
            "messages",
        ),
        (
            "to Sophia",
            (
                "Short-term memory:\n"
                "Current/recent dialogue turns (USER/ASSISTANT order).\n"
                "USER: send message\n"
                "ASSISTANT: Who do you want to send it to?\n\n"
                "Medium-term memory:\n"
                "No data"
            ),
            "messages",
            "messages",
        ),
        (
            "how are you doing",
            (
                "Short-term memory:\n"
                "Current/recent dialogue turns (USER/ASSISTANT order).\n"
                "USER: send message to Sophia\n"
                "ASSISTANT: What message do you want to send?\n\n"
                "Medium-term memory:\n"
                "No data"
            ),
            "messages",
            "messages",
        ),
        (
            "open",
            None,
            "system_control",
            "system_control",
        ),
        (
            "what now on screen",
            None,
            "describe",
            "describe",
        ),
        (
            "youtube",
            (
                "Short-term memory:\n"
                "Current/recent dialogue turns (USER/ASSISTANT order).\n"
                "USER: open\n"
                "ASSISTANT: What do you want to open?\n\n"
                "Medium-term memory:\n"
                "No data"
            ),
            "browser",
            "browser",
        ),
        (
            "open youtube and find",
            None,
            "browser",
            "browser",
        ),
        (
            "find meditation live stream",
            (
                "Short-term memory:\n"
                "Current/recent dialogue turns (USER/ASSISTANT order).\n"
                "USER: open youtube and find\n"
                "ASSISTANT: What should I find on YouTube?\n\n"
                "Medium-term memory:\n"
                "No data"
            ),
            "browser",
            "browser",
        ),
    ],
)
async def test_text_processor_user_discussed_sequential_fragments_matrix(
    user_text: str,
    short_term_memory: str,
    classifier_category: str,
    expected_route: str,
):
    tp = TextProcessor(config={})
    tp.live_provider.classify_intent_decision = AsyncMock(return_value={"category": classifier_category})

    _, sections, _, _ = await tp._build_prompt_for_text(
        user_text,
        session_id="seq-matrix-1",
        runtime_memory_context=short_term_memory,
    )

    assert sections["primary_route"] == expected_route


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "user_text,short_term_memory,classifier_category,expected_route",
    [
        (
            "to Sophia",
            (
                "Short-term memory:\n"
                "Current/recent dialogue turns (USER/ASSISTANT order).\n"
                "USER: send message\n"
                "ASSISTANT: Who do you want to send it to?\n\n"
                "Medium-term memory:\n"
                "No data"
            ),
            "messages",
            "messages",
        ),
        (
            "how are you doing today",
            (
                "Short-term memory:\n"
                "Current/recent dialogue turns (USER/ASSISTANT order).\n"
                "USER: send message to Sophia\n"
                "ASSISTANT: What message do you want to send?\n\n"
                "Medium-term memory:\n"
                "No data"
            ),
            "messages",
            "messages",
        ),
        (
            "youtube",
            (
                "Short-term memory:\n"
                "Current/recent dialogue turns (USER/ASSISTANT order).\n"
                "USER: open\n"
                "ASSISTANT: What do you want to open?\n\n"
                "Medium-term memory:\n"
                "No data"
            ),
            "browser",
            "browser",
        ),
        (
            "safari",
            (
                "Short-term memory:\n"
                "Current/recent dialogue turns (USER/ASSISTANT order).\n"
                "USER: open\n"
                "ASSISTANT: What do you want to open?\n\n"
                "Medium-term memory:\n"
                "No data"
            ),
            "system_control",
            "system_control",
        ),
        (
            "hr u tday",
            (
                "Short-term memory:\n"
                "Current/recent dialogue turns (USER/ASSISTANT order).\n"
                "USER: send message to Sophia\n"
                "ASSISTANT: What message do you want to send?\n\n"
                "Medium-term memory:\n"
                "No data"
            ),
            "messages",
            "messages",
        ),
    ],
)
async def test_text_processor_clarification_followups_with_ragged_fragments(
    user_text: str,
    short_term_memory: str,
    classifier_category: str,
    expected_route: str,
):
    tp = TextProcessor(config={})
    tp.live_provider.classify_intent_decision = AsyncMock(return_value={"category": classifier_category})

    _, sections, _, _ = await tp._build_prompt_for_text(
        user_text,
        session_id="clarify-followup-1",
        runtime_memory_context=short_term_memory,
    )

    assert sections["primary_route"] == expected_route
    tp.live_provider.classify_intent_decision.assert_awaited_once()
    call = tp.live_provider.classify_intent_decision.await_args_list[0]
    classifier_context = call.kwargs["classifier_context"]
    assert "short_term_memory" in classifier_context
    assert "ASSISTANT:" in classifier_context["short_term_memory"]


@pytest.mark.asyncio
async def test_text_processor_messaging_pronoun_followup_uses_classifier_with_short_term_context():
    tp = TextProcessor(config={})
    tp.live_provider.classify_intent_decision = AsyncMock(return_value={"category": "messages"})

    _, sections, _, routing_context = await tp._build_prompt_for_text(
        "can you send to her how are you doing today",
        session_id="msg-pronoun-1",
        runtime_memory_context=(
            "Short-term memory:\n"
            "Current/recent dialogue turns (USER/ASSISTANT order).\n"
            "CURRENT_TURN:\n"
            "TIME_UTC: 2026-03-05T23:49:15+00:00\n"
            "USER: can you send message to Sophia\n"
            "ASSISTANT: What message would you like to send to Sophia?\n\n"
            "Medium-term memory:\n"
            "No data"
        ),
    )

    assert sections["primary_route"] == "messages"
    assert "primary_route: messages" in routing_context
    tp.live_provider.classify_intent_decision.assert_awaited_once()
    call = tp.live_provider.classify_intent_decision.await_args_list[0]
    classifier_context = call.kwargs["classifier_context"]
    assert "short_term_memory" in classifier_context
    assert "Sophia" in classifier_context["short_term_memory"]


@pytest.mark.asyncio
async def test_text_processor_uses_only_short_term_memory_in_classifier_context():
    tp = TextProcessor(config={})
    tp.live_provider.classify_intent_decision = AsyncMock(
        return_value={"category": "whatsapp"}
    )

    await tp._build_prompt_for_text(
        "continue",
        session_id="s-1",
        runtime_memory_context=(
            "Short-term memory:\n"
            "Current/recent dialogue turns (USER/ASSISTANT order).\n"
            "USER: send message to Sophia\n"
            "ASSISTANT: preparing message\n\n"
            "Medium-term memory:\n"
            "No data"
        ),
    )

    second_call = tp.live_provider.classify_intent_decision.await_args_list[0]
    classifier_context = second_call.kwargs["classifier_context"]
    assert "short_term_memory" in classifier_context
    assert "last_primary_route" not in classifier_context
    assert "last_user_query" not in classifier_context
    assert "send message to Sophia" in classifier_context["short_term_memory"]


@pytest.mark.asyncio
async def test_text_processor_does_not_rewrite_classifier_whatsapp_decision():
    tp = TextProcessor(config={})
    tp.live_provider.classify_intent_decision = AsyncMock(return_value={"category": "whatsapp"})

    _, sections, _, routing_context = await tp._build_prompt_for_text(
        "send message to Sophia how are you doing today",
        session_id="s-2",
    )

    assert sections["primary_route"] == "whatsapp"
    assert sections["whatsapp"] is True
    assert sections["messages"] is False
    assert "primary_route: whatsapp" in routing_context


@pytest.mark.asyncio
@pytest.mark.asyncio
async def test_text_processor_passes_short_term_memory_to_classifier_context():
    tp = TextProcessor(config={})
    tp.live_provider.classify_intent_decision = AsyncMock(return_value={"category": "none"})

    runtime_memory_context = (
        "Short-term memory:\n"
        "Current/recent dialogue turns (USER/ASSISTANT order).\n"
        "USER: open youtube\n"
        "ASSISTANT: opening browser\n\n"
        "Medium-term memory:\n"
        "No data"
    )
    await tp._build_prompt_for_text(
        "tell me more",
        session_id="mem-s1",
        runtime_memory_context=runtime_memory_context,
    )

    call = tp.live_provider.classify_intent_decision.await_args_list[0]
    ctx = call.kwargs["classifier_context"]
    assert "short_term_memory" in ctx
    assert "open youtube" in ctx["short_term_memory"].lower()


@pytest.mark.asyncio
async def test_text_processor_image_input_without_text_forces_describe_route():
    tp = TextProcessor(config={})
    tp.live_provider.classify_intent_decision = AsyncMock(return_value={"category": "messages"})

    _, sections, _, _ = await tp._build_prompt_for_text(
        "",
        has_image=True,
    )

    assert sections["primary_route"] == "describe"
    assert sections["describe"] is True
    assert sections["messages"] is False
    tp.live_provider.classify_intent_decision.assert_not_awaited()


@pytest.mark.asyncio
async def test_text_processor_image_input_with_text_uses_intent_route():
    tp = TextProcessor(config={})
    tp.live_provider.classify_intent_decision = AsyncMock(return_value={"category": "browser"})

    _, sections, _, _ = await tp._build_prompt_for_text(
        "open youtube",
        has_image=True,
    )

    assert sections["primary_route"] == "browser"
    assert sections["browser"] is True
    tp.live_provider.classify_intent_decision.assert_awaited_once()


@pytest.mark.asyncio
async def test_text_processor_enables_single_category_prompt_only():
    tp = TextProcessor(config={})
    tp.live_provider.classify_intent_decision = AsyncMock(return_value={"category": "browser"})

    prompt, sections, _, _ = await tp._build_prompt_for_text("open YouTube")
    assert sections["primary_route"] == "browser"
    assert "Browser Automation Intent" in prompt
    assert "**MESSAGES ACTIONS" not in prompt
    assert "**WHATSAPP ACTIONS" not in prompt
    assert "WebSearch Intent" not in prompt
    tp.live_provider.classify_intent_decision.assert_awaited_once()


@pytest.mark.asyncio
async def test_text_processor_does_not_pass_image_for_non_describe_route():
    tp = TextProcessor(config={})
    tp.is_initialized = True

    process_calls = {"text": 0, "image": 0}

    async def _process(*args, **kwargs):
        process_calls["text"] += 1
        yield "ok"

    async def _process_with_image(*args, **kwargs):
        process_calls["image"] += 1
        yield "ok-image"

    tp.live_provider.process = _process
    tp.live_provider.process_with_image = _process_with_image

    chunks = []
    async for chunk in tp.process_text_streaming(
        text="open youtube",
        image_data=b"fake-image",
        session_id="sid-1",
    ):
        chunks.append(chunk)

    assert chunks == ["ok"]
    assert process_calls["text"] == 1
    assert process_calls["image"] == 0
