from modules.memory_management.providers.memory_analyzer import MemoryAnalyzer


def _analyzer() -> MemoryAnalyzer:
    return MemoryAnalyzer.__new__(MemoryAnalyzer)


def _payload(goal_state: str, current_goal: str, short_value: str, medium_value: str, long_value: str) -> str:
    return "\n".join(
        [
            f"GOAL_STATE: {goal_state}",
            f"CURRENT_GOAL: {current_goal}",
            f"SHORT_TERM: {short_value}",
            f"MEDIUM_TERM: {medium_value}",
            f"LONG_TERM: {long_value}",
        ]
    )


def test_parse_five_section_contract_with_goal_state():
    analyzer = _analyzer()
    text = _payload(
        "keep",
        "User wants to send a message to Sophia. Missing detail: message text.",
        "[2026-03-06 10:00:00 UTC] USER: send a message to Sophia | ASSISTANT: asked for message text",
        "[2026-03-06] User started a messaging task and assistant requested message content.",
        "User prefers concise communication.",
    )

    short_memory, medium_memory, long_memory, current_goal, goal_state = analyzer._parse_analysis_response(text)

    assert goal_state == "keep"
    assert current_goal == "User wants to send a message to Sophia. Missing detail: message text."
    assert "USER: send a message to Sophia" in short_memory
    assert "messaging task" in medium_memory
    assert "User prefers concise communication." in long_memory


def test_parse_contract_supports_clear_state():
    analyzer = _analyzer()
    text = _payload(
        "clear",
        "EMPTY",
        "[2026-03-06 10:00:00 UTC] USER: tell her i will be late | ASSISTANT: sent the message",
        "[2026-03-06] User completed a messaging task.",
        "EMPTY",
    )

    short_memory, medium_memory, long_memory, current_goal, goal_state = analyzer._parse_analysis_response(text)

    assert goal_state == "clear"
    assert current_goal == ""
    assert short_memory
    assert medium_memory
    assert long_memory == ""


def test_parse_rejects_missing_goal_state_label():
    analyzer = _analyzer()
    text = "\n".join(
        [
            "CURRENT_GOAL: User wants to send a message to Sophia. Missing detail: message text.",
            "SHORT_TERM: [2026-03-06 10:00:00 UTC] USER: compare sneakers | ASSISTANT: shared shortlist",
            "MEDIUM_TERM: [2026-03-06] User compared sneaker options and shortlist was created.",
            "LONG_TERM: User's first name is Sergiy.",
        ]
    )

    assert analyzer._parse_analysis_response(text) == ("", "", "", "", "empty")


def test_parse_repairs_code_fence_wrapping_with_goal_state():
    analyzer = _analyzer()
    text = (
        "```text\n"
        + _payload(
            "replace",
            "User wants to open Safari.",
            "[2026-03-06 10:00:00 UTC] USER: open Safari instead | ASSISTANT: opening Safari",
            "[2026-03-06] User replaced a previous task with opening Safari.",
            "User prefers Russian.",
        )
        + "\n```"
    )

    short_memory, medium_memory, long_memory, current_goal, goal_state = analyzer._parse_analysis_response(text)

    assert goal_state == "replace"
    assert current_goal == "User wants to open Safari."
    assert short_memory
    assert medium_memory
    assert long_memory
