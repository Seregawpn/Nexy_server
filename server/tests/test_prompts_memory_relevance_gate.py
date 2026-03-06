import sys
from pathlib import Path


project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from config.prompts import (
    build_intent_classifier_prompt,
    build_runtime_memory_usage_policy_prompt,
    build_system_prompt,
)


def test_runtime_memory_policy_includes_memory_relevance_gate():
    prompt = build_runtime_memory_usage_policy_prompt()

    assert "analyze the full available memory context (short + medium + long)" in prompt
    assert "Run Memory Relevance Gate for every request" in prompt
    assert "If memory relevance is YES, use only memory facts relevant to current request." in prompt
    assert "If memory relevance is NO, answer in normal format without memory-linked framing." in prompt
    assert "Never force memory references into non-memory requests." in prompt
    assert "If current USER turn is a short confirmation (yes/sure/ok/okay/yep/yup/yeah/go ahead/do it)" in prompt
    assert "continue the most recent unfinished assistant proposal/task" in prompt
    assert "If short-term history shows assistant already asked confirmation for the same task, do not ask again; execute immediately." in prompt
    assert "If confirmation target is unambiguous in recent context, execution is mandatory; do not ask permission again." in prompt


def test_intent_classifier_includes_memory_first_decision_policy():
    prompt = build_intent_classifier_prompt()

    assert "Memory-first decision policy for classification" in prompt
    assert "use full memory context (short + medium + long) only to validate relevance and consistency." in prompt
    assert "Determine if current request is memory-related" in prompt
    assert "If request is NOT memory-related, classify only by current user goal" in prompt
    assert "if memory does not disambiguate, choose none." in prompt
    assert "Short confirmation policy" in prompt
    assert "If current input is a short confirmation and short_term_memory indicates assistant asked a proceed/confirm question" in prompt
    assert "If current input contains explicit approval for the pending task, treat it as immediate execution signal." in prompt
    assert "For short confirmation of pending news/facts lookup, classify as google_search." in prompt
    assert "Conflict resolution priority (strict):" in prompt
    assert "prioritize the executable category over capability." in prompt
    assert "capability is allowed only for explicit capability/help intent without an executable task request." in prompt
    assert "For referential messaging turns after a messaging prompt" in prompt
    assert "Never select capability when an executable route can be resolved with high confidence" in prompt


def test_strict_prompt_includes_affirmation_execute_now_policy():
    prompt = build_system_prompt(
        messages_enabled=False,
        whatsapp_enabled=False,
        browser_enabled=False,
        payment_enabled=False,
        google_search_enabled=True,
        strict_single_route_mode=True,
    )

    assert "[Global Execution & Confirmation Policy]" in prompt
    assert "yes/sure/ok/okay/yep/yup/yeah/go ahead/do it/please do, including common STT variants like ves/es." in prompt
    assert "If recent dialogue shows assistant already asked confirmation for the same task, do not ask again; execute immediately." in prompt
    assert "Follow Global Execution & Confirmation Policy." in prompt
    assert "If affirmation confirms pending web-search/news/facts request, return factual results directly." in prompt


def test_web_search_prompt_forbids_reconfirm_after_affirmation():
    prompt = build_system_prompt(
        messages_enabled=False,
        whatsapp_enabled=False,
        browser_enabled=False,
        payment_enabled=False,
        google_search_enabled=True,
        strict_single_route_mode=True,
    )
    assert "When current turn is an affirmation/approval for a pending search task from recent history" in prompt
    assert "Do NOT output the phrase \"Would you like me to proceed?\"." in prompt


def test_messages_prompt_reuses_known_slot_within_active_clarification_chain():
    prompt = build_system_prompt(
        messages_enabled=True,
        whatsapp_enabled=True,
        browser_enabled=False,
        payment_enabled=False,
        google_search_enabled=False,
        strict_single_route_mode=True,
    )

    assert "Slot reuse policy for the active Messages clarification chain is strict." in prompt
    assert "MUST treat contact as already known and MUST NOT ask for contact again." in prompt
    assert "Do NOT reset the active messaging chain unless the current turn explicitly starts a different task." in prompt
    assert "Slot reuse policy for the active WhatsApp clarification chain is strict." in prompt


def test_runtime_memory_policy_forbids_dropping_known_messaging_slots():
    prompt = build_runtime_memory_usage_policy_prompt()

    assert "For active messaging/WhatsApp clarification chains" in prompt
    assert "MUST keep the known recipient and MUST NOT ask who to send it to again." in prompt
    assert "MUST keep the known message body and MUST NOT ask for it again." in prompt
    assert "Do not drop a known slot from short-term memory" in prompt
