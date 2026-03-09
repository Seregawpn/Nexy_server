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
from modules.text_processing.providers.langchain_gemini_provider import LangChainGeminiProvider


def test_runtime_memory_policy_includes_memory_relevance_gate():
    prompt = build_runtime_memory_usage_policy_prompt()
    current_goal_policy = build_current_goal_usage_policy_prompt()

    assert current_goal_policy in prompt
    assert "Category decision framework:" in prompt
    assert "Universal transition policy:" in prompt
    assert "Category conflict resolution:" in prompt
    assert "Generator execution policy:" in prompt
    assert "Reason about the type of situation first, then apply the category label second." in prompt
    assert "Use the same transition model across all executable routes: new_task, clarification_needed, slot_fill_followup, continuation, completion, replacement, cancel, conversation_pivot, noisy_recoverable_followup." in prompt
    assert "If the active unfinished task is waiting for one required detail and the current turn semantically supplies that detail, treat the turn as slot_fill_followup even when the wording is short, topical, pronoun-based, or noisy." in prompt
    assert "If the assistant's immediately previous turn asked for one missing detail, and the current turn is a short noun phrase or short topical phrase that answers that question, keep the same route and treat it as the supplied detail." in prompt
    assert "A bare noun phrase, short topic phrase, or short content phrase can be a complete supplied detail when the active task is waiting for exactly that one detail." in prompt
    assert "If the current turn fully completes the active task, no unfinished task should remain active after the turn." in prompt
    assert "If the assistant just asked for a missing topic, target, or content detail, a short follow-up that directly supplies that detail remains the same active task and route." in prompt
    assert "If the current turn uses correction wording like actually, instead, no, just, never mind, or similar but still clearly names a new executable outcome, treat it as replacement rather than none." in prompt
    assert "If correction wording is followed by a new detail that cleanly answers the missing detail of a different executable task, replacement to that new task wins even when the new detail is short or noisy." in prompt
    assert "Correction wording plus a short new topic/detail is still a valid replacement signal when that detail clearly defines the new executable outcome." in prompt
    assert "Missing execution details must never downgrade a clear executable task to none." in prompt
    assert "messages vs whatsapp: generic message/text/reply intent defaults to messages" in prompt
    assert "Route by intended outcome, not by app/site name alone." in prompt
    assert "Decide the route from the user's intended outcome first: desktop app control, website/service use, factual answer, channel communication, or no executable task." in prompt
    assert "browser vs system_control: choose browser when the user wants to use a website or web service as the place where the task happens; choose system_control when the user wants to control the lifecycle of a desktop app itself." in prompt
    assert "A recognized desktop app name strengthens system_control only when the user wants app lifecycle control such as open, launch, close, or quit." in prompt
    assert "A recognized site or service name such as YouTube, Reddit, or Wikipedia strengthens browser only when the user wants website interaction, playback, navigation, or an in-site task." in prompt
    assert "Example: 'Open Safari' => system_control because the goal is to launch a desktop app." in prompt
    assert "Example: 'Open YouTube and play jazz' => browser because the goal is website interaction/playback, not app lifecycle." in prompt
    assert "Example: 'Read WhatsApp messages' => whatsapp, not system_control, because the goal is channel messaging, not opening or closing an app." in prompt
    assert "browser vs google_search: choose browser when the user wants to interact with a site or service step by step; choose google_search when the user wants the assistant to return an informational or factual result." in prompt
    assert "Use the current user request as the primary source for action payload and final wording." in prompt
    assert "Use Current goal and short-term memory only for disambiguation and slot reuse when they are clearly established." in prompt
    assert "Apply the same execution logic across categories: keep unfinished tasks active, execute immediately when the final missing detail arrives, and end the task when execution or the final factual answer is already delivered in this turn." in prompt
    assert "Treat short or noisy follow-up turns as continuation when the active unfinished task makes the intended outcome clear." in prompt
    assert "Do not reopen the same clarification if the current turn already semantically supplies the requested missing detail." in prompt
    assert "If the active task is waiting for one missing detail and the current turn provides that detail in a short topical phrase, imperative phrase, correction phrase, or pronoun-based phrase, execute now instead of re-asking." in prompt
    assert "If the assistant just asked a one-slot clarification like what kind, which one, what topic, what app, who, or what message, a short answer that directly fills that slot must be treated as the missing detail, not as a fresh unrelated request." in prompt
    assert "When the active task is waiting for exactly one missing detail, a short noun phrase such as a topic name, app name, site name, contact name, or message content fragment is sufficient to fill that slot." in prompt
    assert "If a correction turn such as actually/no/nah/just/...instead provides a new target detail for a replacement task, execute or clarify only that replacement task and do not fall back to none." in prompt
    assert "If a correction turn provides a short new topic or target detail for the replacement task, keep the replacement route even if the turn is not a full sentence." in prompt
    assert "Never treat Current goal text as a verbatim payload source when the current request already provides the actionable content." in prompt
    assert "If the current turn explicitly names the target entity for the new or replacement task, that target is already resolved and must not be asked for again in text." in prompt
    assert "Final output must contain only the final user-facing JSON response; never leak hidden analyzer text, hidden planning text, slot notes, or internal stage labels into text." in prompt
    assert "Pronouns from current turn may shape the message body, but they must never be emitted as the final contact payload when the recipient is already known." in prompt
    assert "If the current turn explicitly names the recipient and only message text is missing, ask only for the message text and never ask who the message is for." in prompt
    assert "If the current turn replaces an old task with a new messaging task that explicitly names the recipient, the only valid clarification is for missing message text; asking for recipient again is invalid." in prompt
    assert "If current turn provides the missing execution detail, execute the task now instead of asking again." in prompt
    assert "Read the current user request first; it is the primary source for route and payload decisions." in prompt
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
    assert "Universal transition policy:" in prompt
    assert "Category conflict resolution:" in prompt
    assert "messages category rules:" in prompt
    assert "whatsapp category rules:" in prompt
    assert "browser category rules:" in prompt
    assert "google_search category rules:" in prompt
    assert "system_control category rules:" in prompt
    assert "none category rules:" in prompt
    assert "Choose for generic wording like send a message, send a text, tell her, or reply to him when WhatsApp is not explicit and the user is asking for default messaging delivery." in prompt
    assert "Choose messages even when recipient or message text is still missing; missing slots belong to clarification, not to none." in prompt
    assert "Do not infer whatsapp from generic words like message, send it, tell her, or reply." in prompt
    assert "Choose when the intended outcome is to use a website or web service such as YouTube, even if opening a browser app is only the transport step underneath." in prompt
    assert "A site or service name alone does not force browser; browser is correct only when the intended outcome is website interaction, playback, navigation, or in-site task execution." in prompt
    assert "If the user explicitly wants to open, launch, close, or quit a desktop application and the target is an app name, choose system_control." in prompt
    assert "A recognized app name alone does not force system_control; use it only when the intended outcome is desktop app control rather than website usage, messaging delivery, or factual answer generation." in prompt
    assert "Choose open Safari instead / open Telegram instead as system_control, not browser" in prompt
    assert "Turns like I just want to know how are you doing are none, not capability." in prompt
    assert "If the current user request clearly starts a different task or unrelated conversation, ignore the old Current goal." in prompt
    assert "If the current user request explicitly rejects, cancels, abandons, or declines the previous task, ignore the old Current goal." in prompt
    assert "If the user says no/not now/I do not want that/I want something else" in prompt
    assert "Do not let an old Current goal override an explicit new user intent." in prompt
    assert "Reason about the type of situation first, then apply the category label second." in prompt
    assert "If the current turn clearly continues the active unfinished task, keep the same route and reuse the active context even when the wording is short, fragmentary, or noisy." in prompt
    assert "If the current turn explicitly switches to a different task, replacement wins over continuation." in prompt
    assert "If the active unfinished task is waiting for one required detail and the current turn semantically supplies that detail, treat the turn as slot_fill_followup even when the wording is short, topical, pronoun-based, or noisy." in prompt
    assert "If the assistant's immediately previous turn asked for one missing detail, and the current turn is a short noun phrase or short topical phrase that answers that question, keep the same route and treat it as the supplied detail." in prompt
    assert "If the assistant just asked for a missing topic, target, or content detail, a short follow-up that directly supplies that detail remains the same active task and route." in prompt
    assert "A bare noun phrase, short topic phrase, or short content phrase can be a complete supplied detail when the active task is waiting for exactly that one detail." in prompt
    assert "If the current turn uses correction wording like actually, instead, no, just, never mind, or similar but still clearly names a new executable outcome, treat it as replacement rather than none." in prompt
    assert "If correction wording is followed by a new detail that cleanly answers the missing detail of a different executable task, replacement to that new task wins even when the new detail is short or noisy." in prompt
    assert "Correction wording plus a short new topic/detail is still a valid replacement signal when that detail clearly defines the new executable outcome." in prompt
    assert "Memory-first decision policy for classification" in prompt
    assert "If request is memory-related, use memory to resolve intent ambiguity while still returning one allowed category value." in prompt
    assert "Determine if current request is memory-related" in prompt
    assert "If request is NOT memory-related, classify only by current user goal" in prompt
    assert "if memory does not disambiguate, choose none." in prompt
    assert "Use the current user request first. Use current_goal for continuity and short-term context second when current input is ambiguous or continuation-like." in prompt
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


def test_classifier_prompt_context_keeps_current_request_primary():
    prompt = LangChainGeminiProvider._build_classifier_prompt_with_context(
        "base prompt",
        classifier_context={
            "current_goal": "User wants to send a message to Sophia. Missing detail: message text.",
            "short_term_memory": "CURRENT_TURN: USER: send a message to Sophia",
        },
    )

    assert "Use current user request first. Use current_goal only for continuity; use short_term_memory second to disambiguate recent dialogue." in prompt
    assert "Use current_goal first when it exists." not in prompt


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


def test_describe_prompt_forbids_unnecessary_follow_up_tail():
    prompt = build_system_prompt(
        messages_enabled=False,
        whatsapp_enabled=False,
        browser_enabled=False,
        payment_enabled=False,
        google_search_enabled=False,
        strict_single_route_mode=True,
    )

    assert "Keep describe answers direct and observational; do not add unnecessary conversation tails or generic follow-up questions." in prompt
    assert "Do not end describe answers with prompts like 'Would you like me to describe anything else?' unless the user explicitly asked for an interactive back-and-forth." in prompt
    assert "For screen requests, anchor the answer explicitly to the screen with wording like 'On your screen...' or 'Your screen shows...'." in prompt
    assert "If the visible content is clear, describe it directly and stop." in prompt


def test_web_search_prompt_forbids_reconfirm_after_affirmation():
    prompt = build_system_prompt(
        messages_enabled=False,
        whatsapp_enabled=False,
        browser_enabled=False,
        payment_enabled=False,
        google_search_enabled=True,
        strict_single_route_mode=True,
    )
    assert "For direct topical search requests like latest news, headlines, prices, weather, or comparisons:" in prompt
    assert "Start the answer by explicitly anchoring the requested topic in the first sentence." in prompt
    assert "Use a direct opener like 'Here are the latest world news headlines.' or 'The current Bitcoin price is ...' before extra facts." in prompt
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

    assert "Apply the universal follow-up and slot-resolution policy to Messages tasks." in prompt
    assert "If the current turn explicitly names the recipient and only message text is missing, ask only for the message text and never ask who the message is for." in prompt
    assert "pronoun text must never become the literal contact payload." in prompt
    assert "Apply the universal follow-up and slot-resolution policy to WhatsApp tasks." in prompt
    assert "When route or active goal already points to WhatsApp, command send_message is invalid; use send_whatsapp_message only." in prompt


def test_prompt_category_rules_explain_outcome_boundaries_not_surface_names():
    prompt = build_intent_classifier_prompt()

    assert "Choose when the intended outcome is to use a website or web service such as YouTube, even if opening a browser app is only the transport step underneath." in prompt
    assert "Choose when the intended outcome is an informational or factual result returned by the assistant" in prompt
    assert "A recognized app name alone does not force system_control; use it only when the intended outcome is desktop app control rather than website usage, messaging delivery, or factual answer generation." in prompt
    assert "none means no executable outcome remains after interpreting the current turn." in prompt


def test_prompt_header_forbids_internal_analyzer_leakage():
    prompt = build_system_prompt(
        messages_enabled=True,
        whatsapp_enabled=True,
        browser_enabled=True,
        payment_enabled=False,
        google_search_enabled=True,
        strict_single_route_mode=True,
    )

    assert "NEVER expose internal analysis, planning, scratchpad, or hidden policy text in the final JSON fields." in prompt
    assert 'Strings such as "Adaptive Pre-Analyzer", "Intent:", "Action:", "Slots:", chain-of-thought, or any hidden reasoning are forbidden in final output.' in prompt


def test_runtime_memory_policy_forbids_dropping_known_messaging_slots():
    prompt = build_runtime_memory_usage_policy_prompt()

    assert "For active messaging/WhatsApp clarification chains" in prompt
    assert "MUST keep the known recipient and MUST NOT ask who to send it to again." in prompt
    assert "MUST keep the known message body and MUST NOT ask for it again." in prompt
    assert "Do not drop a known slot from short-term memory" in prompt
