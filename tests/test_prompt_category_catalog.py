from pathlib import Path
import sys

project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from config.prompts import build_intent_classifier_prompt, build_route_system_prompt


def test_intent_classifier_prompt_contains_category_contracts():
    prompt = build_intent_classifier_prompt()

    assert "describe category rules:" in prompt
    assert "capability category rules:" in prompt
    assert "none category rules:" in prompt
    assert "- messages:" in prompt
    assert "- whatsapp:" in prompt
    assert "- browser:" in prompt
    assert "- payment:" in prompt


def test_none_route_uses_smalltalk_text_only_contract_without_action_sections():
    prompt = build_route_system_prompt("none")

    assert "[Generation Output Rules]" in prompt
    assert "Respond in English." in prompt
    assert "**MESSAGES ACTIONS" not in prompt
    assert "**WHATSAPP ACTIONS" not in prompt
    assert "Browser Automation Intent" not in prompt
    assert "Subscription & Payment Intent" not in prompt
    assert "Describe Intent" not in prompt


def test_messages_route_uses_only_messages_action_section():
    prompt = build_route_system_prompt("messages")

    assert "**MESSAGES ACTIONS" in prompt
    assert "**WHATSAPP ACTIONS" not in prompt
    assert "Browser Automation Intent" not in prompt
    assert "Subscription & Payment Intent" not in prompt


def test_whatsapp_route_uses_only_whatsapp_action_section():
    prompt = build_route_system_prompt("whatsapp", whatsapp_available=True)

    assert "**WHATSAPP ACTIONS" in prompt
    assert "**MESSAGES ACTIONS" not in prompt
    assert "Browser Automation Intent" not in prompt
    assert "Subscription & Payment Intent" not in prompt


def test_browser_route_uses_only_browser_section():
    prompt = build_route_system_prompt("browser", browser_available=True)

    assert "Browser Automation Intent" in prompt
    assert "**MESSAGES ACTIONS" not in prompt
    assert "**WHATSAPP ACTIONS" not in prompt
    assert "Subscription & Payment Intent" not in prompt


def test_payment_route_uses_only_payment_section():
    prompt = build_route_system_prompt("payment", payment_available=True)

    assert "Subscription & Payment Intent" in prompt
    assert "Browser Automation Intent" not in prompt
    assert "**MESSAGES ACTIONS" not in prompt
    assert "**WHATSAPP ACTIONS" not in prompt


def test_describe_route_uses_only_describe_section():
    prompt = build_route_system_prompt("describe")

    assert "Describe Intent" in prompt
    assert "WebSearch Intent" not in prompt
    assert "Browser Automation Intent" not in prompt
    assert "**MESSAGES ACTIONS" not in prompt


def test_google_search_route_uses_only_web_search_section():
    prompt = build_route_system_prompt("google_search")

    assert "WebSearch Intent" in prompt
    assert "Describe Intent" not in prompt
    assert "Browser Automation Intent" not in prompt
    assert "**MESSAGES ACTIONS" not in prompt


def test_capability_route_uses_only_capability_section():
    prompt = build_route_system_prompt("capability", capability_available=True)

    assert "Capability Intent" in prompt
    assert "WebSearch Intent" not in prompt
    assert "Describe Intent" not in prompt
    assert "**MESSAGES ACTIONS" not in prompt


def test_system_control_route_uses_only_system_control_section():
    prompt = build_route_system_prompt("system_control")

    assert "Action Intent (System Actions)" in prompt
    assert "**MESSAGES ACTIONS" not in prompt
    assert "Browser Automation Intent" not in prompt
    assert "Subscription & Payment Intent" not in prompt
