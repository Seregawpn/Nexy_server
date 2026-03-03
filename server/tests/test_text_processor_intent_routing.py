import sys
from pathlib import Path

project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from modules.text_processing.core.text_processor import TextProcessor
from config.prompts import resolve_prompt_sections


def test_extract_intent_text_from_enriched_prompt():
    enriched = (
        "SYSTEM_CONTEXT:\n"
        "Subscription Status: paid\n"
        "Memory Context: something\n\n"
        "USER_INPUT:\n"
        "how are you today"
    )
    assert TextProcessor._extract_intent_text(enriched) == "how are you today"


def test_intent_routing_ignores_subscription_context_for_smalltalk():
    enriched = (
        "SYSTEM_CONTEXT:\n"
        "Subscription Status: paid\n\n"
        "USER_INPUT:\n"
        "how are you today"
    )
    sections = resolve_prompt_sections(TextProcessor._extract_intent_text(enriched))
    assert sections["payment"] is False

