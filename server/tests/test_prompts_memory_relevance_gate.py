import sys
from pathlib import Path


project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from config.prompts import (
    build_current_goal_usage_policy_prompt,
    build_intent_classifier_prompt,
    build_runtime_memory_usage_policy_prompt,
    build_system_prompt,
)


def test_runtime_memory_policy_includes_memory_relevance_gate():
    prompt = build_runtime_memory_usage_policy_prompt()
    current_goal_policy = build_current_goal_usage_policy_prompt()

    assert current_goal_policy in prompt
    assert "Category decision framework:" in prompt
    assert "Category conflict resolution:" in prompt
    assert "Generator execution policy:" in prompt
    assert "Missing execution details must never downgrade a clear executable task to none." in prompt
    assert "messages vs whatsapp: generic message/text/reply intent defaults to messages" in prompt
    assert "browser vs system_control: websites/browser tabs/player tasks => browser; opening or closing desktop apps => system_control." in prompt
    assert "Reuse known slots from Current goal and short-term memory when they are clearly established." in prompt
    assert "If current turn provides the missing execution detail, execute the task now instead of asking again." in prompt
    assert "Read Current goal first as the active task anchor." in prompt
    assert "If the current user request explicitly rejects, cancels, abandons, or declines the previous task, ignore the old Current goal." in prompt
    assert "If the user says no/not now/I do not want that/I want something else" in prompt
    assert "If Current goal is empty, do not invent a new goal from memory." in prompt
    assert "Before any final answer, inspect all three memory tiers: short-term, medium-term, and long-term." in prompt
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
    current_goal_policy = build_current_goal_usage_policy_prompt()

    assert current_goal_policy in prompt
    assert "Category decision framework:" in prompt
    assert "Category conflict resolution:" in prompt
    assert "messages category rules:" in prompt
    assert "whatsapp category rules:" in prompt
    assert "browser category rules:" in prompt
    assert "google_search category rules:" in prompt
    assert "system_control category rules:" in prompt
    assert "none category rules:" in prompt
    assert "Choose for generic wording like send a message, send a text, tell her, reply to him when WhatsApp is not explicit." in prompt
    assert "Do not infer whatsapp from generic words like message, send it, tell her, or reply." in prompt
    assert "Choose open Safari instead / open Telegram instead as system_control, not browser" in prompt
    assert "Turns like I just want to know how are you doing are none, not capability." in prompt
    assert "If the current user request clearly starts a different task or unrelated conversation, ignore the old Current goal." in prompt
    assert "If the current user request explicitly rejects, cancels, abandons, or declines the previous task, ignore the old Current goal." in prompt
    assert "If the user says no/not now/I do not want that/I want something else" in prompt
    assert "Do not let an old Current goal override an explicit new user intent." in prompt
    assert "Memory-first decision policy for classification" in prompt
    assert "If request is memory-related, use memory to resolve intent ambiguity while still returning one allowed category value." in prompt
    assert "Determine if current request is memory-related" in prompt
    assert "If request is NOT memory-related, classify only by current user goal" in prompt
    assert "if memory does not disambiguate, choose none." in prompt
    assert "Short confirmation follow-up policy" in prompt
    assert "If current input is a short confirmation and short_term_memory indicates assistant asked a proceed/confirm question" in prompt
    assert "If current input contains explicit approval for the pending task, treat it as immediate execution signal." in prompt
    assert "For short confirmation of pending news/facts lookup, classify as google_search." in prompt
    assert "Conflict resolution priority (strict):" in prompt
    assert "prioritize the executable category over capability." in prompt
    assert "capability is allowed only for explicit capability/help intent without an executable task request." in prompt
    assert "If a messaging action is present and there is no explicit WhatsApp signal in current_goal, short_term_memory, or current input, default to messages." in prompt
    assert "Never switch an active Messages/iMessage thread to whatsapp unless the current user request explicitly says WhatsApp." in prompt
    assert "Never infer whatsapp from generic words like 'message', 'send it', 'tell her', or 'reply' alone." in prompt
    assert "For follow-up pronoun turns after messaging prompt" in prompt
    assert "Never select capability when an executable route can be resolved with high confidence" in prompt
    assert "Noisy input policy for classification:" in prompt
    assert "Infer likely intent from semantics and context, not literal token matching only." in prompt
    assert "If two categories remain equally plausible after context checks, choose none." in prompt
    assert "'send a message to Sophia' => messages" in prompt
    assert "'tell her how are you doing today' after 'What message would you like to send to Sophia?' => messages." in prompt


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
    assert "[Noisy Input Interpretation Policy]" in prompt
    assert "This can create noisy words, noisy keywords, and broken command phrases." in prompt
    assert "Determine action/category by intended meaning, not by exact malformed keyword matches." in prompt
    assert "First determine what the user is logically trying to get in the end result" in prompt
    assert "General phrase corruption patterns to handle:" in prompt
    assert "clipped ending: the word or phrase cuts off before completion" in prompt
    assert "letter-fragment phrase: only a few letters of the intended word remain" in prompt
    assert "isolated-token phrase: one or two meaningful tokens remain without full grammar" in prompt
    assert "split word: one word becomes two broken parts" in prompt
    assert "glued words: multiple words are merged together" in prompt
    assert "Interpretation guidance:" in prompt
    assert "A request may arrive as a clipped phrase, broken phrase, isolated letters, or a semantically damaged fragment." in prompt
    assert "The text may be too short, too broken, or too noisy to look valid literally" in prompt
    assert "Reconstruct meaning from logical user need, recent context, active task state, and memory" in prompt
    assert "Treat broken wording as transport noise, not as the user's real intention" in prompt
    assert "If the fragment is too weak and multiple materially different outcomes remain plausible, ask one short clarification." in prompt
    assert "If the meaning is genuinely not recoverable, do not guess; ask one short clarification." in prompt
    assert "General examples of the kind of noisy input to expect:" in prompt
    assert '"helo" instead of a normal greeting like "hello"' in prompt
    assert '"how ar yu" instead of "how are you"' in prompt
    assert '"giv me las new" instead of a complete natural request' in prompt
    assert '"lost news" when the phrase likely means "last news"' in prompt
    assert '"w e a t h e r" where the intended word survives only as spaced letters' in prompt


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
