import json

import pytest

from modules.memory_management.core.memory_manager import MemoryManager


class _StatefulFakeDB:
    def __init__(self):
        self.short = ""
        self.long = ""

    async def get_user_memory(self, hardware_id: str):
        return {"short": self.short, "long": self.long}

    async def update_user_memory(self, hardware_id: str, short_memory: str, long_memory: str):
        self.short = short_memory
        self.long = long_memory
        return True


class _CaseAnalyzer:
    def __init__(self, short_memory: str, long_memory: str, current_goal: str):
        self.short_memory = short_memory
        self.long_memory = long_memory
        self.current_goal = current_goal

    async def analyze_conversation(self, prompt, response, **kwargs):
        return self.short_memory, "", self.long_memory, self.current_goal


class _GoalStateCaseAnalyzer:
    def __init__(self, short_memory: str, long_memory: str, current_goal: str, goal_state: str):
        self.short_memory = short_memory
        self.long_memory = long_memory
        self.current_goal = current_goal
        self.goal_state = goal_state

    async def analyze_conversation(self, prompt, response, **kwargs):
        return self.short_memory, "", self.long_memory, self.current_goal, self.goal_state


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "case_name,prompt,response,analyzer_long,current_goal,expected_long,expected_goal",
    [
        (
            "messages_clarification",
            "Send a message to Sophia",
            "What message would you like to send to Sophia?",
            "",
            "User wants to send a message to Sophia. Missing detail: message text.",
            "",
            "User wants to send a message to Sophia. Missing detail: message text.",
        ),
        (
            "messages_completion",
            "Send hello to Sophia",
            "Sending your message to Sophia.",
            "",
            "",
            "",
            "",
        ),
        (
            "messages_missing_recipient",
            "Send a message",
            "Who do you want to send it to?",
            "",
            "User wants to send a message. Missing detail: recipient.",
            "",
            "User wants to send a message. Missing detail: recipient.",
        ),
        (
            "search_clarification",
            "Find news",
            "What kind of news do you want?",
            "",
            "User wants news. Missing detail: topic.",
            "",
            "User wants news. Missing detail: topic.",
        ),
        (
            "search_completion",
            "Find latest world news",
            "Here are the latest world news headlines.",
            "",
            "",
            "",
            "",
        ),
        (
            "system_control_clarification",
            "Open",
            "What app do you want to open?",
            "",
            "User wants to open an app. Missing detail: app name.",
            "",
            "User wants to open an app. Missing detail: app name.",
        ),
        (
            "system_control_completion",
            "Open Safari",
            "Opening Safari.",
            "",
            "",
            "",
            "",
        ),
        (
            "browser_clarification",
            "Open YouTube and find",
            "What should I find on YouTube?",
            "",
            "User wants to search YouTube. Missing detail: search query.",
            "",
            "User wants to search YouTube. Missing detail: search query.",
        ),
        (
            "browser_completion",
            "Open YouTube and play jazz",
            "Opening YouTube and playing jazz.",
            "",
            "",
            "",
            "",
        ),
        (
            "whatsapp_clarification",
            "Send a WhatsApp message to Mom",
            "What message do you want to send to Mom?",
            "",
            "User wants to send a WhatsApp message to Mom. Missing detail: message text.",
            "",
            "User wants to send a WhatsApp message to Mom. Missing detail: message text.",
        ),
        (
            "smalltalk_how_are_you",
            "How are you?",
            "I'm doing well, thank you.",
            "",
            "",
            "",
            "",
        ),
        (
            "smalltalk_thank_you",
            "Thank you",
            "You're welcome.",
            "",
            "",
            "",
            "",
        ),
        (
            "message_cancel_clears_goal",
            "No, I do not want to send a message",
            "Okay, I will not continue that task.",
            "",
            "",
            "",
            "",
        ),
        (
            "browser_cancel_clears_goal",
            "No, never mind",
            "Okay, I will not continue that task.",
            "",
            "",
            "",
            "",
        ),
        (
            "topic_switch_smalltalk_clears_goal",
            "No, I just want to know how are you doing",
            "I am doing well, thanks for asking.",
            "",
            "",
            "",
            "",
        ),
        (
            "pivot_to_new_task_replaces_goal",
            "No, open Safari instead",
            "Opening Safari.",
            "",
            "User wants to open Safari.",
            "",
            "User wants to open Safari.",
        ),
        (
            "capability_question",
            "What can you do?",
            "I can help with messages, apps, browsing, and search.",
            "",
            "",
            "",
            "",
        ),
        (
            "meta_recall_question",
            "What did I ask before?",
            "You asked me to send a message earlier.",
            "",
            "",
            "",
            "",
        ),
        (
            "gratitude_followup",
            "Okay, thanks",
            "Any time.",
            "",
            "",
            "",
            "",
        ),
        (
            "remember_name",
            "Remember this: my name is Sergiy",
            "I will remember that.",
            "User's first name is Sergiy.",
            "",
            "User's first name is Sergiy.",
            "",
        ),
        (
            "remember_preference",
            "Remember this: I like running",
            "I will remember that.",
            "User likes running.",
            "",
            "User likes running.",
            "",
        ),
        (
            "dont_store_transient_task",
            "Find me white sneakers",
            "I found several white sneaker options.",
            "",
            "",
            "",
            "",
        ),
        (
            "remember_timezone",
            "Remember this: I live in Toronto timezone",
            "I will remember that.",
            "User timezone is Toronto.",
            "",
            "User timezone is Toronto.",
            "",
        ),
        (
            "remember_language",
            "Remember this: I prefer English",
            "I will remember that.",
            "User prefers English.",
            "",
            "User prefers English.",
            "",
        ),
    ],
)
async def test_memory_basic_goal_matrix(
    case_name: str,
    prompt: str,
    response: str,
    analyzer_long: str,
    current_goal: str,
    expected_long: str,
    expected_goal: str,
):
    db = _StatefulFakeDB()
    manager = MemoryManager(db_manager=db)
    manager.memory_analyzer = _CaseAnalyzer(
        short_memory=f"[2026-03-07 00:00:00 UTC] USER: {prompt} | ASSISTANT: {response}",
        long_memory=analyzer_long,
        current_goal=current_goal,
    )

    updated = await manager.update_memory_background(
        hardware_id=f"hw-basic-goal-{case_name}",
        prompt=prompt,
        response=response,
    )

    assert updated is not None

    payload = json.loads(db.short)
    assert payload.get("current_goal", "") == expected_goal
    assert payload.get("factual_long", "") == expected_long

    context = await manager.get_memory_context(
        hardware_id=f"hw-basic-goal-{case_name}",
        user_input=prompt,
    )

    assert context.get("current_goal_context", "") == expected_goal
    assert context.get("factual_long_term_context", "") == expected_long


@pytest.mark.asyncio
async def test_memory_goal_state_clear_forces_empty_current_goal():
    db = _StatefulFakeDB()
    manager = MemoryManager(db_manager=db)
    manager.memory_analyzer = _GoalStateCaseAnalyzer(
        short_memory="[2026-03-07 00:00:00 UTC] USER: Tell her I'll be late | ASSISTANT: Sending your message to Sophia.",
        long_memory="",
        current_goal="User wants to send a message to Sophia.",
        goal_state="clear",
    )

    updated = await manager.update_memory_background(
        hardware_id="hw-goal-state-clear",
        prompt="Tell her I'll be late",
        response="Sending your message to Sophia.",
    )

    assert updated is not None
    payload = json.loads(db.short)
    assert payload.get("goal_state") == "clear"
    assert payload.get("current_goal") == ""


@pytest.mark.asyncio
async def test_memory_goal_state_replace_without_goal_fails_closed_to_empty():
    db = _StatefulFakeDB()
    manager = MemoryManager(db_manager=db)
    manager.memory_analyzer = _GoalStateCaseAnalyzer(
        short_memory="[2026-03-07 00:00:00 UTC] USER: No, open Safari instead | ASSISTANT: Opening Safari.",
        long_memory="",
        current_goal="",
        goal_state="replace",
    )

    updated = await manager.update_memory_background(
        hardware_id="hw-goal-state-replace-empty",
        prompt="No, open Safari instead",
        response="Opening Safari.",
    )

    assert updated is not None
    payload = json.loads(db.short)
    assert payload.get("goal_state") == "empty"
    assert payload.get("current_goal") == ""
