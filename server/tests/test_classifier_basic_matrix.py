from unittest.mock import AsyncMock

import pytest

from modules.text_processing.core.text_processor import TextProcessor


def _runtime_memory(current_goal: str = "", short_term: str = "") -> str:
    parts = []
    if current_goal:
        parts.append(f"Current goal:\n{current_goal}")
    if short_term:
        parts.append(
            "Short-term memory:\n"
            "Current/recent dialogue turns (USER/ASSISTANT order).\n"
            f"{short_term}"
        )
    parts.append("Medium-term memory:\nNo data")
    return "\n\n".join(parts)


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "case_name,user_text,classifier_category,runtime_memory_context,expected_route,expect_goal_ctx,expect_short_ctx",
    [
        (
            "messages_direct",
            "send a message to Sophia",
            "messages",
            None,
            "messages",
            False,
            False,
        ),
        (
            "messages_followup_goal",
            "tell her how are you doing today",
            "messages",
            _runtime_memory(
                current_goal="User wants to send a message to Sophia. Missing detail: message text.",
                short_term="CURRENT_TURN:\nTIME_UTC: 2026-03-07 01:32:39 UTC\nUSER: send a message to Sophia\nASSISTANT: What message would you like to send to Sophia?",
            ),
            "messages",
            True,
            True,
        ),
        (
            "messages_cancel_none",
            "no, I do not want to send a message",
            "none",
            _runtime_memory(
                current_goal="User wants to send a message to Sophia. Missing detail: message text.",
                short_term="CURRENT_TURN:\nTIME_UTC: 2026-03-07 01:32:39 UTC\nUSER: send a message to Sophia\nASSISTANT: What message would you like to send to Sophia?",
            ),
            "none",
            True,
            True,
        ),
        (
            "messages_topic_switch_none",
            "no, I just want to know how are you doing",
            "none",
            _runtime_memory(
                current_goal="User wants to send a message to Sophia. Missing detail: message text.",
                short_term="CURRENT_TURN:\nTIME_UTC: 2026-03-07 01:32:39 UTC\nUSER: send a message to Sophia\nASSISTANT: What message would you like to send to Sophia?",
            ),
            "none",
            True,
            True,
        ),
        (
            "messages_pivot_to_new_task",
            "no, open Safari instead",
            "system_control",
            _runtime_memory(
                current_goal="User wants to send a message to Sophia. Missing detail: message text.",
                short_term="CURRENT_TURN:\nTIME_UTC: 2026-03-07 01:32:39 UTC\nUSER: send a message to Sophia\nASSISTANT: What message would you like to send to Sophia?",
            ),
            "system_control",
            True,
            True,
        ),
        (
            "whatsapp_direct",
            "send a WhatsApp message to Mom",
            "whatsapp",
            None,
            "whatsapp",
            False,
            False,
        ),
        (
            "browser_direct",
            "open YouTube and play jazz",
            "browser",
            None,
            "browser",
            False,
            False,
        ),
        (
            "browser_followup_goal",
            "rain sounds",
            "browser",
            _runtime_memory(
                current_goal="User wants to search YouTube. Missing detail: search query.",
                short_term="CURRENT_TURN:\nTIME_UTC: 2026-03-07 01:35:00 UTC\nUSER: open YouTube and find\nASSISTANT: What should I find on YouTube?",
            ),
            "browser",
            True,
            True,
        ),
        (
            "google_search_direct",
            "find latest world news",
            "google_search",
            None,
            "google_search",
            False,
            False,
        ),
        (
            "google_search_followup_goal",
            "world news",
            "google_search",
            _runtime_memory(
                current_goal="User wants news. Missing detail: topic.",
                short_term="CURRENT_TURN:\nTIME_UTC: 2026-03-07 01:36:00 UTC\nUSER: find news\nASSISTANT: What kind of news do you want?",
            ),
            "google_search",
            True,
            True,
        ),
        (
            "describe_direct",
            "what is on my screen",
            "describe",
            None,
            "describe",
            False,
            False,
        ),
        (
            "system_control_direct",
            "open Safari",
            "system_control",
            None,
            "system_control",
            False,
            False,
        ),
        (
            "system_control_followup_goal",
            "Safari",
            "system_control",
            _runtime_memory(
                current_goal="User wants to open an app. Missing detail: app name.",
                short_term="CURRENT_TURN:\nTIME_UTC: 2026-03-07 01:37:00 UTC\nUSER: open\nASSISTANT: What app do you want to open?",
            ),
            "system_control",
            True,
            True,
        ),
        (
            "payment_direct",
            "upgrade my subscription",
            "payment",
            None,
            "payment",
            False,
            False,
        ),
        (
            "capability_direct",
            "what can you do",
            "capability",
            None,
            "capability",
            False,
            False,
        ),
        (
            "meta_none",
            "what did I ask before",
            "none",
            None,
            "none",
            False,
            False,
        ),
        (
            "search_confirm_yes",
            "yes",
            "google_search",
            _runtime_memory(
                short_term="CURRENT_TURN:\nTIME_UTC: 2026-03-07 01:38:00 UTC\nUSER: find latest bitcoin price\nASSISTANT: Do you want me to search for the latest bitcoin price now?",
            ),
            "google_search",
            False,
            True,
        ),
        (
            "browser_confirm_yes",
            "yes",
            "browser",
            _runtime_memory(
                short_term="CURRENT_TURN:\nTIME_UTC: 2026-03-07 01:39:00 UTC\nUSER: open YouTube and play jazz\nASSISTANT: Do you want me to open YouTube now?",
            ),
            "browser",
            False,
            True,
        ),
        (
            "whatsapp_continue",
            "continue",
            "whatsapp",
            _runtime_memory(
                current_goal="User wants to send a WhatsApp message to Mom. Missing detail: message text.",
                short_term="CURRENT_TURN:\nTIME_UTC: 2026-03-07 01:40:00 UTC\nUSER: send a WhatsApp message to Mom\nASSISTANT: What message do you want to send to Mom?",
            ),
            "whatsapp",
            True,
            True,
        ),
        (
            "describe_image_forced",
            "",
            "messages",
            None,
            "describe",
            False,
            False,
        ),
    ],
)
async def test_classifier_basic_matrix(
    case_name: str,
    user_text: str,
    classifier_category: str,
    runtime_memory_context: str | None,
    expected_route: str,
    expect_goal_ctx: bool,
    expect_short_ctx: bool,
):
    tp = TextProcessor(config={})
    tp.live_provider.classify_intent_decision = AsyncMock(return_value={"category": classifier_category})

    route_flags, _ = await tp._build_prompt_for_text(
        user_text,
        session_id=f"classifier-matrix-{case_name}",
        runtime_memory_context=runtime_memory_context,
        has_image=(case_name == "describe_image_forced"),
    )

    assert route_flags["route"] == expected_route

    if case_name == "describe_image_forced":
        tp.live_provider.classify_intent_decision.assert_not_awaited()
        return

    tp.live_provider.classify_intent_decision.assert_awaited_once()
    call = tp.live_provider.classify_intent_decision.await_args_list[0]
    classifier_context = call.kwargs["classifier_context"]

    if expect_goal_ctx:
        assert "current_goal" in classifier_context
        assert classifier_context["current_goal"]
    else:
        assert "current_goal" not in classifier_context

    if expect_short_ctx:
        assert "short_term_memory" in classifier_context
        assert classifier_context["short_term_memory"]
    else:
        assert "short_term_memory" not in classifier_context
