from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Optional


CATEGORY_ORDER: tuple[str, ...] = (
    "none",
    "capability",
    "describe",
    "messages",
    "whatsapp",
    "system_control",
    "browser",
    "google_search",
    "payment",
)

LEVEL_ORDER: tuple[int, ...] = (1, 2, 3, 4, 5)

PROMPT_OWNER_BY_CATEGORY: dict[str, str] = {
    "none": "PROMPT_FOOTER+PROMPT_UNIFIED_POLICY",
    "capability": "PROMPT_CAPABILITY",
    "describe": "PROMPT_DESCRIBE",
    "messages": "PROMPT_MESSAGES",
    "whatsapp": "PROMPT_WHATSAPP",
    "system_control": "PROMPT_SYSTEM_CONTROL",
    "browser": "PROMPT_BROWSER",
    "google_search": "PROMPT_WEB_SEARCH",
    "payment": "PROMPT_PAYMENT",
}

LEVEL_1_CASE_INPUTS: dict[str, tuple[tuple[str, str], ...]] = {
    "none": (
        ("Greeting", "Hi, how are you?"),
        ("Thanks", "Thanks a lot."),
        ("Short smalltalk", "Tell me a quick joke."),
        ("Casual check-in", "I am feeling tired today."),
    ),
    "capability": (
        ("Capability overview", "What can you help me with?"),
        ("Apps capability", "What app-related tasks can you do for me?"),
        ("Messaging capability", "What messaging tasks can you handle for me?"),
        ("Browser capability", "What browser tasks can you do?"),
    ),
    "describe": (
        ("Describe screen", "What is on my screen right now?"),
        ("Describe interface", "Describe what you see on screen."),
        ("Visible content", "What do you see here?"),
        ("Screen summary", "Give me a quick description of the screen."),
    ),
    "messages": (
        ("Direct message Sophia", "Text Sophia: I am outside."),
        ("Direct message Mom", "Send Mom a message: I will call later."),
        ("Direct message Alex", "Message Alex: I arrived safely."),
        ("Direct message Sarah", "Tell Sarah: Meeting starts at three."),
    ),
    "whatsapp": (
        ("Direct WhatsApp Mom", "Send WhatsApp to Mom: I got home."),
        ("Direct WhatsApp Daniel", "WhatsApp Daniel: I am on my way."),
        ("Direct WhatsApp Sophia", "Message Sophia on WhatsApp: Running five minutes late."),
        ("Direct WhatsApp Emma", "Send Emma a WhatsApp: Please check your email."),
    ),
    "system_control": (
        ("Open Safari", "Open Safari."),
        ("Open Calendar", "Launch Calendar."),
        ("Open Notes", "Open Notes for me."),
        ("Open Music", "Start the Music app."),
    ),
    "browser": (
        ("YouTube jazz", "Open YouTube and play jazz."),
        ("Wikipedia page", "Open Wikipedia and search for Helen Keller."),
        ("Amazon search", "Open Amazon and search for AirPods Pro."),
        ("Reddit task", "Open Reddit and find the latest Mac apps discussion."),
    ),
    "google_search": (
        ("World news", "What are the latest world news headlines?"),
        ("Weather", "What is the weather in Toronto today?"),
        ("Bitcoin price", "What is the current Bitcoin price?"),
        ("Stock price", "What is Apple stock price right now?"),
    ),
    "payment": (
        ("Buy premium", "Buy premium subscription now."),
        ("Upgrade now", "Upgrade my plan now."),
        ("Purchase subscription", "Purchase the subscription for me."),
        ("Subscribe now", "Subscribe me to premium now."),
    ),
}

LEVEL_2_CASE_INPUTS: dict[str, tuple[tuple[str, str], ...]] = {
    "none": (
        ("Unclear help request", "Can you help me with that?"),
        ("Vague follow-up", "What should I do next?"),
        ("Unspecified issue", "Something is wrong here."),
        ("Unclear request", "I need help with this."),
    ),
    "capability": (
        ("Broad capability ask", "Can you help with communication stuff?"),
        ("Unclear app capability", "What app tasks can you do exactly for this?"),
        ("Mixed capability ask", "Can you handle messages or browser things here?"),
        ("Need capability narrowing", "What kind of tasks can you do in this case?"),
    ),
    "describe": (
        ("Describe missing target", "Can you describe the part I need?"),
        ("Screen area unclear", "What is happening in that section?"),
        ("Unclear screen focus", "Can you tell me what is there?"),
        ("Need visual focus", "Describe the important part on the screen."),
    ),
    "messages": (
        ("Message missing recipient and text", "Send a message."),
        ("Recipient only", "Text Sophia."),
        ("Body only", "Send this message for me: I am outside."),
        ("Read messages missing contact", "Check my messages."),
    ),
    "whatsapp": (
        ("WhatsApp missing recipient and text", "Send a WhatsApp message."),
        ("WhatsApp recipient only", "WhatsApp Daniel."),
        ("WhatsApp body only", "Send this on WhatsApp: I am on my way."),
        ("Read WhatsApp missing contact", "Check WhatsApp messages."),
    ),
    "system_control": (
        ("Open missing app", "Open the app for me."),
        ("Launch unclear target", "Launch something for me."),
        ("Close missing app", "Close that application."),
        ("System action unclear", "Open what I need for this task."),
    ),
    "browser": (
        ("Open missing site", "Open that website for me."),
        ("Search missing query", "Search for this in the browser."),
        ("Browser action vague", "Open the page I need."),
        ("Website unclear", "Go to the site about that topic."),
    ),
    "google_search": (
        ("Latest update unclear topic", "What is the latest update?"),
        ("News unclear topic", "What are the latest headlines about that?"),
        ("Price unclear asset", "What is the current price right now?"),
        ("Weather unclear location", "What is the weather today there?"),
    ),
    "payment": (
        ("Subscription help vague", "Help me with my subscription."),
        ("Payment action unclear", "I want to upgrade."),
        ("Billing intent broad", "I need to manage my plan."),
        ("Purchase intent unclear", "Can you help me buy it?"),
    ),
}


@dataclass(frozen=True)
class CategoryLevelCase:
    case_id: str
    category: str
    level: int
    summary: str
    user_input: str
    expected_route: str
    expected_goal_state: str
    expected_behavior: str
    expected_command: Optional[str]
    memory_expected: bool
    prompt_owner: str
    owner_focus: tuple[str, ...]
    expected_text_contains: tuple[str, ...] = ()
    notes: str = ""

    @property
    def interaction_shape(self) -> str:
        if self.expected_behavior in {"replace", "cancel"}:
            return self.expected_behavior
        if self.level == 1:
            return "direct"
        if self.level in {2, 3}:
            return "follow_up"
        if self.level == 4:
            return "recovery"
        return "ambiguous"

    @property
    def outcome_shape(self) -> str:
        if self.expected_behavior in {"answer", "continue_answer"}:
            return "answer"
        if self.expected_behavior in {"clarify", "disambiguate"}:
            return "clarify"
        if self.expected_behavior in {"execute", "continue_execute"}:
            return "execute"
        return self.expected_behavior


def _case(
    category: str,
    level: int,
    index: int,
    summary: str,
    user_input: str,
    expected_goal_state: str,
    expected_behavior: str,
    expected_command: Optional[str],
    memory_expected: bool,
    expected_text_contains: tuple[str, ...] = (),
    notes: str = "",
) -> CategoryLevelCase:
    return CategoryLevelCase(
        case_id=f"{category}_l{level}_{index:02d}",
        category=category,
        level=level,
        summary=summary,
        user_input=user_input,
        expected_route=category,
        expected_goal_state=expected_goal_state,
        expected_behavior=expected_behavior,
        expected_command=expected_command,
        memory_expected=memory_expected,
        prompt_owner=PROMPT_OWNER_BY_CATEGORY[category],
        owner_focus=("classifier", "generator", "memory", "live"),
        expected_text_contains=expected_text_contains,
        notes=notes,
    )


def _make_cases(category: str, command: Optional[str]) -> tuple[CategoryLevelCase, ...]:
    route = category
    l1_behavior = "execute" if command else "answer"
    l3_behavior = "continue_execute" if command else "continue_answer"
    l4_behavior = "execute" if command and category not in {"system_control", "payment"} else ("answer" if not command else "clarify")
    l5_primary_behavior = "replace" if command else "answer"
    l5_primary_goal_state = "replace" if command else "empty"
    l5_primary_command = command if command else None
    l1_inputs = LEVEL_1_CASE_INPUTS[category]
    l2_inputs = LEVEL_2_CASE_INPUTS[category]
    return (
        _case(category, 1, 1, l1_inputs[0][0], l1_inputs[0][1], "clear" if command and category in {"messages", "whatsapp"} else "empty", l1_behavior, command, category in {"messages", "whatsapp"}),
        _case(category, 1, 2, l1_inputs[1][0], l1_inputs[1][1], "clear" if command and category in {"messages", "whatsapp"} else "empty", l1_behavior, command, category in {"messages", "whatsapp"}),
        _case(category, 1, 3, l1_inputs[2][0], l1_inputs[2][1], "clear" if command and category in {"messages", "whatsapp"} else "empty", l1_behavior, command, category in {"messages", "whatsapp"}),
        _case(category, 1, 4, l1_inputs[3][0], l1_inputs[3][1], "clear" if command and category in {"messages", "whatsapp"} else "empty", l1_behavior, command, category in {"messages", "whatsapp"}),
        _case(category, 2, 1, l2_inputs[0][0], l2_inputs[0][1], "set", "clarify", None, True),
        _case(category, 2, 2, l2_inputs[1][0], l2_inputs[1][1], "set", "clarify", None, True),
        _case(category, 2, 3, l2_inputs[2][0], l2_inputs[2][1], "set", "clarify", None, True),
        _case(category, 2, 4, l2_inputs[3][0], l2_inputs[3][1], "set", "clarify", None, True),
        _case(category, 3, 1, "Level 3 continuation case A", f"{route} level 3 continue a", "clear", l3_behavior, command, True),
        _case(category, 3, 2, "Level 3 continuation case B", f"{route} level 3 continue b", "clear", l3_behavior, command, True),
        _case(category, 3, 3, "Level 3 continuation case C", f"{route} level 3 continue c", "clear", l3_behavior, command, True),
        _case(category, 3, 4, "Level 3 continuation case D", f"{route} level 3 continue d", "clear", l3_behavior, command, True),
        _case(category, 4, 1, "Level 4 noisy case A", f"{route} level 4 noisy a", "clear" if l4_behavior.endswith("execute") else "set" if l4_behavior == "clarify" else "empty", l4_behavior, command if l4_behavior.endswith("execute") else None, True),
        _case(category, 4, 2, "Level 4 noisy case B", f"{route} level 4 noisy b", "clear" if l4_behavior.endswith("execute") else "set" if l4_behavior == "clarify" else "empty", l4_behavior, command if l4_behavior.endswith("execute") else None, True),
        _case(category, 4, 3, "Level 4 noisy case C", f"{route} level 4 noisy c", "clear" if l4_behavior.endswith("execute") else "set" if l4_behavior == "clarify" else "empty", l4_behavior, command if l4_behavior.endswith("execute") else None, True),
        _case(category, 4, 4, "Level 4 noisy case D", f"{route} level 4 noisy d", "clear" if l4_behavior.endswith("execute") else "set" if l4_behavior == "clarify" else "empty", l4_behavior, command if l4_behavior.endswith("execute") else None, True),
        _case(category, 5, 1, "Level 5 ambiguous case A", f"{route} level 5 ambiguous a", l5_primary_goal_state, l5_primary_behavior, l5_primary_command, True),
        _case(category, 5, 2, "Level 5 ambiguous case B", f"{route} level 5 ambiguous b", "set", "disambiguate", None, True),
        _case(category, 5, 3, "Level 5 ambiguous case C", f"{route} level 5 ambiguous c", "clear", "cancel", None, True),
        _case(category, 5, 4, "Level 5 ambiguous case D", f"{route} level 5 ambiguous d", "set" if category != "none" else "empty", "answer" if category in {"none", "capability"} else "disambiguate", None, True),
    )


_CATEGORY_COMMANDS: dict[str, Optional[str]] = {
    "none": None,
    "capability": None,
    "describe": None,
    "messages": "send_message",
    "whatsapp": "send_whatsapp_message",
    "system_control": "open_app",
    "browser": "browser_use",
    "google_search": None,
    "payment": "buy_subscription",
}

CATEGORY_LEVEL_180_CASE_GATE: tuple[CategoryLevelCase, ...] = tuple(
    case
    for category in CATEGORY_ORDER
    for case in _make_cases(category, _CATEGORY_COMMANDS[category])
)

FULL_CATEGORY_LEVEL_CAMPAIGN: tuple[CategoryLevelCase, ...] = CATEGORY_LEVEL_180_CASE_GATE

LEVEL_CAMPAIGNS: dict[int, tuple[CategoryLevelCase, ...]] = {
    level: tuple(case for case in CATEGORY_LEVEL_180_CASE_GATE if case.level == level)
    for level in LEVEL_ORDER
}

CATEGORY_CAMPAIGNS: dict[str, tuple[CategoryLevelCase, ...]] = {
    category: tuple(case for case in CATEGORY_LEVEL_180_CASE_GATE if case.category == category)
    for category in CATEGORY_ORDER
}

LEVEL_1_30_CASE_CAMPAIGN: tuple[CategoryLevelCase, ...] = tuple(
    case
    for case in CATEGORY_LEVEL_180_CASE_GATE
    if case.case_id in {
        "none_l1_01", "none_l1_02", "none_l1_03",
        "capability_l1_01", "capability_l1_02", "capability_l1_03",
        "describe_l1_01", "describe_l1_02", "describe_l1_03",
        "messages_l1_01", "messages_l1_02", "messages_l1_03", "messages_l1_04",
        "whatsapp_l1_01", "whatsapp_l1_02", "whatsapp_l1_03", "whatsapp_l1_04",
        "system_control_l1_01", "system_control_l1_02", "system_control_l1_03",
        "browser_l1_01", "browser_l1_02", "browser_l1_03", "browser_l1_04",
        "google_search_l1_01", "google_search_l1_02", "google_search_l1_03",
        "payment_l1_01", "payment_l1_02", "payment_l1_03",
    }
)

LEVEL_2_36_CASE_CAMPAIGN: tuple[CategoryLevelCase, ...] = LEVEL_CAMPAIGNS[2]


def build_category_level_matrix_rows(
    cases: Optional[tuple[CategoryLevelCase, ...]] = None,
) -> tuple[dict[str, Any], ...]:
    selected_cases = cases or CATEGORY_LEVEL_180_CASE_GATE
    return tuple(
        {
            "case_id": case.case_id,
            "category": case.category,
            "level": case.level,
            "interaction_shape": case.interaction_shape,
            "outcome_shape": case.outcome_shape,
            "expected_route": case.expected_route,
            "expected_goal_state": case.expected_goal_state,
            "expected_behavior": case.expected_behavior,
            "expected_command": case.expected_command or "none",
            "memory_expected": case.memory_expected,
            "prompt_owner": case.prompt_owner,
            "summary": case.summary,
        }
        for case in selected_cases
    )


def build_category_level_heatmap_rows(
    cases: Optional[tuple[CategoryLevelCase, ...]] = None,
) -> tuple[dict[str, Any], ...]:
    selected_cases = cases or CATEGORY_LEVEL_180_CASE_GATE
    rows: list[dict[str, Any]] = []
    for category in CATEGORY_ORDER:
        for level in LEVEL_ORDER:
            cell_cases = tuple(case for case in selected_cases if case.category == category and case.level == level)
            rows.append(
                {
                    "category": category,
                    "level": level,
                    "cases": len(cell_cases),
                    "memory_cases": sum(1 for case in cell_cases if case.memory_expected),
                    "execute_cases": sum(1 for case in cell_cases if case.outcome_shape == "execute"),
                    "clarify_cases": sum(1 for case in cell_cases if case.outcome_shape == "clarify"),
                    "answer_cases": sum(1 for case in cell_cases if case.outcome_shape == "answer"),
                    "replace_cases": sum(1 for case in cell_cases if case.outcome_shape == "replace"),
                    "cancel_cases": sum(1 for case in cell_cases if case.outcome_shape == "cancel"),
                }
            )
    return tuple(rows)
