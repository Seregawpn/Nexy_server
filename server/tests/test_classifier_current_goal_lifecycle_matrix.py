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
    "case_name,user_text,classifier_category,runtime_memory_context,expected_route",
    [
        (
            "messages_continue_payload",
            "tell her I will be late",
            "messages",
            _runtime_memory(
                current_goal="User wants to send a message to Sophia. Missing detail: message text.",
                short_term="CURRENT_TURN:\nTIME_UTC: 2026-03-07 02:00:00 UTC\nUSER: send a message to Sophia\nASSISTANT: What message would you like to send to Sophia?",
            ),
            "messages",
        ),
        (
            "messages_continue_short_affirmation",
            "yes",
            "messages",
            _runtime_memory(
                current_goal="User wants to send a message to Sophia. Missing detail: message text.",
                short_term="CURRENT_TURN:\nTIME_UTC: 2026-03-07 02:01:00 UTC\nUSER: send a message to Sophia saying I am on my way\nASSISTANT: Do you want me to send it now?",
            ),
            "messages",
        ),
        (
            "whatsapp_continue_payload",
            "tell Mom I arrived safely",
            "whatsapp",
            _runtime_memory(
                current_goal="User wants to send a WhatsApp message to Mom. Missing detail: message text.",
                short_term="CURRENT_TURN:\nTIME_UTC: 2026-03-07 02:02:00 UTC\nUSER: send a WhatsApp message to Mom\nASSISTANT: What message do you want to send to Mom?",
            ),
            "whatsapp",
        ),
        (
            "whatsapp_continue_short_affirmation",
            "yes",
            "whatsapp",
            _runtime_memory(
                current_goal="User wants to send a WhatsApp message to Mom.",
                short_term="CURRENT_TURN:\nTIME_UTC: 2026-03-07 02:03:00 UTC\nUSER: send a WhatsApp message to Mom saying I arrived safely\nASSISTANT: Do you want me to send it now?",
            ),
            "whatsapp",
        ),
        (
            "browser_continue_query",
            "sleep music",
            "browser",
            _runtime_memory(
                current_goal="User wants to search YouTube. Missing detail: search query.",
                short_term="CURRENT_TURN:\nTIME_UTC: 2026-03-07 02:04:00 UTC\nUSER: open YouTube and find\nASSISTANT: What should I find on YouTube?",
            ),
            "browser",
        ),
        (
            "browser_continue_short_affirmation",
            "yes",
            "browser",
            _runtime_memory(
                current_goal="User wants to open YouTube and play jazz.",
                short_term="CURRENT_TURN:\nTIME_UTC: 2026-03-07 02:05:00 UTC\nUSER: open YouTube and play jazz\nASSISTANT: Do you want me to open YouTube now?",
            ),
            "browser",
        ),
        (
            "search_continue_topic",
            "world news",
            "google_search",
            _runtime_memory(
                current_goal="User wants news. Missing detail: topic.",
                short_term="CURRENT_TURN:\nTIME_UTC: 2026-03-07 02:06:00 UTC\nUSER: find news\nASSISTANT: What kind of news do you want?",
            ),
            "google_search",
        ),
        (
            "search_continue_short_affirmation",
            "yes",
            "google_search",
            _runtime_memory(
                current_goal="User wants latest bitcoin price.",
                short_term="CURRENT_TURN:\nTIME_UTC: 2026-03-07 02:07:00 UTC\nUSER: find latest bitcoin price\nASSISTANT: Do you want me to search for the latest bitcoin price now?",
            ),
            "google_search",
        ),
        (
            "system_control_continue_target",
            "Safari",
            "system_control",
            _runtime_memory(
                current_goal="User wants to open an app. Missing detail: app name.",
                short_term="CURRENT_TURN:\nTIME_UTC: 2026-03-07 02:08:00 UTC\nUSER: open\nASSISTANT: What app do you want to open?",
            ),
            "system_control",
        ),
        (
            "system_control_continue_short_affirmation",
            "yes",
            "system_control",
            _runtime_memory(
                current_goal="User wants to open Safari.",
                short_term="CURRENT_TURN:\nTIME_UTC: 2026-03-07 02:09:00 UTC\nUSER: open Safari\nASSISTANT: Do you want me to open Safari now?",
            ),
            "system_control",
        ),
        (
            "messages_cancel_none",
            "no, I do not want to send a message",
            "none",
            _runtime_memory(
                current_goal="User wants to send a message to Sophia. Missing detail: message text.",
                short_term="CURRENT_TURN:\nTIME_UTC: 2026-03-07 02:10:00 UTC\nUSER: send a message to Sophia\nASSISTANT: What message would you like to send to Sophia?",
            ),
            "none",
        ),
        (
            "messages_topic_switch_to_smalltalk",
            "no, I just want to know how are you doing",
            "none",
            _runtime_memory(
                current_goal="User wants to send a message to Sophia. Missing detail: message text.",
                short_term="CURRENT_TURN:\nTIME_UTC: 2026-03-07 02:11:00 UTC\nUSER: send a message to Sophia\nASSISTANT: What message would you like to send to Sophia?",
            ),
            "none",
        ),
        (
            "messages_pivot_to_new_task",
            "no, open Safari instead",
            "system_control",
            _runtime_memory(
                current_goal="User wants to send a message to Sophia. Missing detail: message text.",
                short_term="CURRENT_TURN:\nTIME_UTC: 2026-03-07 02:12:00 UTC\nUSER: send a message to Sophia\nASSISTANT: What message would you like to send to Sophia?",
            ),
            "system_control",
        ),
        (
            "whatsapp_cancel_none",
            "not now",
            "none",
            _runtime_memory(
                current_goal="User wants to send a WhatsApp message to Mom. Missing detail: message text.",
                short_term="CURRENT_TURN:\nTIME_UTC: 2026-03-07 02:13:00 UTC\nUSER: send a WhatsApp message to Mom\nASSISTANT: What message do you want to send to Mom?",
            ),
            "none",
        ),
        (
            "whatsapp_pivot_to_search",
            "I want something else, find world news",
            "google_search",
            _runtime_memory(
                current_goal="User wants to send a WhatsApp message to Mom. Missing detail: message text.",
                short_term="CURRENT_TURN:\nTIME_UTC: 2026-03-07 02:14:00 UTC\nUSER: send a WhatsApp message to Mom\nASSISTANT: What message do you want to send to Mom?",
            ),
            "google_search",
        ),
        (
            "browser_cancel_none",
            "no, never mind",
            "none",
            _runtime_memory(
                current_goal="User wants to search YouTube. Missing detail: search query.",
                short_term="CURRENT_TURN:\nTIME_UTC: 2026-03-07 02:15:00 UTC\nUSER: open YouTube and find\nASSISTANT: What should I find on YouTube?",
            ),
            "none",
        ),
        (
            "browser_pivot_to_messages",
            "no, send a message to Sophia instead",
            "messages",
            _runtime_memory(
                current_goal="User wants to search YouTube. Missing detail: search query.",
                short_term="CURRENT_TURN:\nTIME_UTC: 2026-03-07 02:16:00 UTC\nUSER: open YouTube and find\nASSISTANT: What should I find on YouTube?",
            ),
            "messages",
        ),
        (
            "search_cancel_none",
            "no, I am not interested now",
            "none",
            _runtime_memory(
                current_goal="User wants news. Missing detail: topic.",
                short_term="CURRENT_TURN:\nTIME_UTC: 2026-03-07 02:17:00 UTC\nUSER: find news\nASSISTANT: What kind of news do you want?",
            ),
            "none",
        ),
        (
            "search_pivot_to_browser",
            "actually open YouTube instead",
            "browser",
            _runtime_memory(
                current_goal="User wants news. Missing detail: topic.",
                short_term="CURRENT_TURN:\nTIME_UTC: 2026-03-07 02:18:00 UTC\nUSER: find news\nASSISTANT: What kind of news do you want?",
            ),
            "browser",
        ),
        (
            "system_control_cancel_to_none",
            "no, leave it",
            "none",
            _runtime_memory(
                current_goal="User wants to open an app. Missing detail: app name.",
                short_term="CURRENT_TURN:\nTIME_UTC: 2026-03-07 02:19:00 UTC\nUSER: open\nASSISTANT: What app do you want to open?",
            ),
            "none",
        ),
    ],
)
async def test_classifier_current_goal_lifecycle_matrix(
    case_name: str,
    user_text: str,
    classifier_category: str,
    runtime_memory_context: str,
    expected_route: str,
):
    tp = TextProcessor(config={})
    tp.live_provider.classify_intent_decision = AsyncMock(
        return_value={"category": classifier_category}
    )

    route_flags, _ = await tp._build_prompt_for_text(
        user_text,
        session_id=f"classifier-lifecycle-{case_name}",
        runtime_memory_context=runtime_memory_context,
        has_image=False,
    )

    assert route_flags["route"] == expected_route

    tp.live_provider.classify_intent_decision.assert_awaited_once()
    call = tp.live_provider.classify_intent_decision.await_args_list[0]
    classifier_context = call.kwargs["classifier_context"]

    assert "current_goal" in classifier_context
    assert classifier_context["current_goal"]
    assert "short_term_memory" in classifier_context
    assert classifier_context["short_term_memory"]
