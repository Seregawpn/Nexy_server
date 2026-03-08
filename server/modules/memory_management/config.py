"""
Конфигурация для Memory Management Module
Использует централизованную конфигурацию
"""

from typing import Dict, Any, Optional

from config.unified_config import get_config


class MemoryConfig:
    """Конфигурация модуля управления памятью"""

    def __init__(self, config: Optional[Dict[str, Any]] = None):
        """
        Инициализация конфигурации из централизованной системы

        Args:
            config: Словарь с конфигурацией (опционально, переопределяет централизованную)
        """
        # Получаем централизованную конфигурацию
        unified_config = get_config()
        self.config = config or {}

        # Используем централизованные настройки с возможностью переопределения
        self.gemini_api_key = self.config.get('gemini_api_key', unified_config.memory.gemini_api_key)
        self.max_short_term_memory_size = self.config.get('max_short_term_memory_size', unified_config.memory.max_short_term_memory_size)
        self.max_long_term_memory_size = self.config.get('max_long_term_memory_size', unified_config.memory.max_long_term_memory_size)
        self.memory_timeout = self.config.get('memory_timeout', unified_config.memory.memory_timeout)
        self.analysis_timeout = self.config.get('analysis_timeout', unified_config.memory.analysis_timeout)

        # Настройки анализа памяти
        self.memory_analysis_model = self.config.get('memory_analysis_model', unified_config.memory.memory_analysis_model)
        self.memory_analysis_temperature = self.config.get('memory_analysis_temperature', unified_config.memory.memory_analysis_temperature)
        self.use_vertex_ai = self.config.get(
            'use_vertex_ai',
            getattr(unified_config.text_processing, 'use_vertex_ai', False),
        )
        self.vertex_project = self.config.get(
            'vertex_project',
            getattr(unified_config.text_processing, 'vertex_project', ''),
        )
        self.vertex_location = self.config.get(
            'vertex_location',
            getattr(unified_config.text_processing, 'vertex_location', 'global'),
        )
        self.vertex_api_key = self.config.get(
            'vertex_api_key',
            getattr(unified_config.text_processing, 'gemini_api_key', ''),
        )

        # Prompt preamble: shared context + global rules.
        self.memory_analysis_prompt_preamble = """
        Analyze this conversation between user and AI assistant to extract memory information.

        USER INPUT: {prompt}
        AI RESPONSE: {response}
        CURRENT_DATE_UTC: {current_date_utc}
        EXISTING_CURRENT_GOAL: {existing_current_goal}
        EXISTING_SHORT_MEMORY: {existing_short_memory}
        EXISTING_MEDIUM_MEMORY: {existing_medium_memory}
        EXISTING_LONG_MEMORY: {existing_long_memory}

        CRITICAL:
        - You MUST respond ONLY in English.
        - Populate each section strictly according to the mandatory detailed rules below.
        - If a section has no useful data, set it to EMPTY.
        - Do not add any extra labels, prefixes, suffixes, headings, explanations, markdown, quotes, or code fences.
        - Follow format only.
        - The final response MUST contain exactly these labels in this exact order:
          GOAL_STATE:
          CURRENT_GOAL:
          SHORT_TERM:
          MEDIUM_TERM:
          LONG_TERM:
        - Do NOT output numbered headings like "0) CURRENT GOAL" or descriptive headings like "CURRENT GOAL (active executable user goal)".
        - Do NOT output unlabeled bare lines.
        - Keep output concise and factual.
        - Do NOT duplicate information inside a section.
        - Treat EXISTING_SHORT_MEMORY, EXISTING_MEDIUM_MEMORY and EXISTING_LONG_MEMORY as read-only context.
        - Preserve useful existing memory entries and update them with current-turn changes.
        - Merge policy is mandatory: output must include valid existing entries from EXISTING_SHORT_MEMORY, EXISTING_MEDIUM_MEMORY, and EXISTING_LONG_MEMORY, plus new/updated entries from the current turn.
        - Do not replace the whole section with only new data if older valid data exists; keep prior valid items and append/update them in canonical format.
        - Store only logically complete, self-contained text units. Never store broken fragments.
        - If a phrase is incomplete (example: "delivery by Friday"), rewrite it into a complete memory sentence (example: "Shoes deliver by Friday.").
        - CURRENT_GOAL must be plain text only and must never use JSON or nested structure.
        - Canonical response example:
          GOAL_STATE: keep
          CURRENT_GOAL: User wants to send a message to Sophia. Missing detail: message text.
          SHORT_TERM: [2026-03-07 00:00:00 UTC] USER: Send a message to Sophia | ASSISTANT: What message would you like to send to Sophia?
          MEDIUM_TERM: EMPTY
          LONG_TERM: EMPTY
        """

        self.memory_analysis_current_goal_prompt_header = """
        0) CURRENT GOAL (active executable user goal):
           First output GOAL_STATE on its own single line.
           GOAL_STATE must be exactly one of:
           set
           keep
           clear
           replace
           empty
           Return exactly one plain-text line describing the current active executable goal.
           Keep plain text only. No JSON. No key-value syntax. No markdown.
           Keep it short and explicit.
        """
        self.memory_analysis_current_goal_universal_policy = """
           Universal task lifecycle policy:
           - Decide lifecycle by task continuity and task outcome, never by isolated keywords.
           - Use the same decision model for all executable categories: messages, WhatsApp, browser, web search, system control, payment, and future executable categories.
           - An executable task is active only if the assistant is still expected to clarify it, continue it, or execute it after this turn.
           - If the assistant already completed the task, already executed the task, or already delivered the final factual result in this turn, that task is not active after the turn.
           - If the current turn stops the old task and starts a new explicit executable task, only the new task may remain active after the turn.
           - If no executable task is active before or after the turn, CURRENT_GOAL must be EMPTY.
        """
        self.memory_analysis_current_goal_activation_rules = """
           Activation rules:
           - Use CURRENT_GOAL only when the user is performing or clarifying a concrete unfinished task.
           - If the turn is ordinary conversation, small talk, gratitude, capability/help, meta-conversation, or no executable goal exists, return EMPTY.
           - Do not store generic chat goals. Only executable user requests belong here.
        """
        self.memory_analysis_current_goal_decision_framework = """
           Decision framework:
           - Answer these questions in order:
             1. Was there an active executable task before this turn?
             2. Does the current user turn start a new executable task, continue the same task, cancel the old task, or replace it with a new one?
             3. After the assistant response in this turn, is any executable task still active?
             4. If an executable task is still active after the turn, is it the same task or a different one?
           - Choose set only when no active task existed before the turn and a new executable task exists after the turn.
           - Choose keep only when the same executable task existed before the turn and remains active after the turn.
           - Choose clear only when an active task existed before or during the turn and no executable task remains active after the turn.
           - Choose replace only when an old active task existed before the turn and a different executable task remains active after the turn.
           - Choose empty only when no executable task exists before or after the turn.
        """
        self.memory_analysis_current_goal_lifecycle_rules = """
           Lifecycle rules:
           - GOAL_STATE describes the lifecycle transition caused by THIS TURN, not just whether a goal exists after the turn.
           - Use GOAL_STATE=set when this turn starts a new executable task and leaves it active after the turn.
           - Use GOAL_STATE=keep when this turn clearly continues an already active task and that same task remains active after the turn.
           - Use GOAL_STATE=clear when this turn completes or cancels the task and no active executable goal remains after the turn.
           - Use GOAL_STATE=replace when this turn stops the old task and starts a different explicit executable task that becomes the new active goal.
           - Use GOAL_STATE=empty when there is no executable goal before or after the turn.
           - First-task clarification is set, not keep: when the user starts a new task and the assistant asks the first required clarification for it, choose set.
           - Referential continuation is keep, not set: when the user continues an already active task with pronouns or replacement wording such as her, him, it, that, instead, tomorrow, choose keep if the same task is still active.
           - If no active task existed before the turn and the task is fully completed in the same turn, use empty because no active executable goal remains after the turn.
           - If an active task existed before the turn and this turn completes it, use clear, not keep and not empty.
           - If the user provides the last missing required detail and the assistant executes the task in the same turn, use clear, not keep and not set.
           - If the user provides the app name after a prior clarification and the assistant only asks for confirmation, use keep.
           - If the user provides the app name after a prior clarification and the assistant opens the app in the same turn, use clear.
           - If the user continues an active browser task and the assistant immediately opens/searches/plays the requested browser content in the same turn, use clear.
           - If the user provides a search topic after an earlier clarification and the assistant returns the actual factual search answer in the same turn, use clear.
           - If an active search task existed before the turn and the assistant returns the final factual search answer in this turn, use clear, not empty, because an active task did exist and was completed by this turn.
           - If the user abandons the old task and switches to a different explicit action task such as opening an app, sending a different message, or starting a different browser action, use replace and keep only the new task in CURRENT_GOAL even if the assistant immediately begins executing it in the same turn.
           - If the user abandons the old task and starts a new explicit task that is still unfinished after the turn, use replace.
           - If the user abandons the old task and starts a different explicit task in the same turn, prefer replace over clear even if the assistant immediately starts executing the new task, because this turn replaced one active task with another explicit task domain.
           - If the user already gave a concrete browser target, site, or query in the current turn and the assistant asks an unnecessary follow-up clarification anyway, preserve the user's executable browser goal and use set, not empty.
           - If an active messaging or WhatsApp goal already knows the recipient and the assistant confirms that the message is being sent in this turn, use clear and return CURRENT_GOAL as EMPTY.
           - If assistant asks the first clarification for a new WhatsApp task with wording like "What would you like to say to Mom?", this is still set, not empty.
           - If an active WhatsApp goal already exists and the assistant says "Sending message to Mom." or similar without repeating the word WhatsApp, preserve the active WhatsApp channel and use clear, not keep.
           - If an active search goal is fully answered with factual search results in this turn, use clear and return CURRENT_GOAL as EMPTY.
           - If the assistant returns the actual factual search answer in this turn, prefer clear even when the answer starts directly with the facts instead of an explicit "Here are..." preface.
           - If the user pivots away from an active task to a new factual search request and the assistant fully answers that new search in the same turn, use clear and return CURRENT_GOAL as EMPTY because no active executable goal remains after the turn.
           - If the assistant now knows the specific app name, contact, site, or topic, CURRENT_GOAL must reflect that resolved entity and must not keep saying Missing detail for the same slot.
           - Immediate execution/completion responses are clear unless a new task replaces the old one in the same turn.
           - If assistant is asking a required clarification question for the same unfinished task, keep that task active.
           - If assistant already completed the task in this turn, CURRENT_GOAL must be EMPTY and GOAL_STATE must be clear.
           - If the user explicitly rejects, cancels, abandons, or declines the previous task, CURRENT_GOAL must be EMPTY unless the same turn clearly starts a new executable task.
           - If the user explicitly rejects, cancels, abandons, or declines the previous task and does not start a new one, clear the goal.
           - If the same turn both abandons the old goal and starts a new explicit task, use replace and set CURRENT_GOAL only for the new task.
        """
        self.memory_analysis_current_goal_task_identity_rules = """
           Task identity rules:
           - Treat the task as the same task when the user keeps the same execution domain and objective, even if wording changes or uses pronouns, shorthand, or replacement wording like her, him, it, that, instead, tomorrow, this one.
           - Treat the task as a different task only when the user clearly changes the executable objective, channel, destination, site, app, or domain.
           - Missing details do not create a new task. A task with unresolved details is still the same task.
           - Referential follow-up like "tell her ...", "send it", "world news", "Safari", or "sleep music instead" should usually continue the active task if the active task already establishes the missing entity.
           - If the current turn only fills a missing slot for the active task, choose keep or clear, never set.
           - If the current turn abandons one task and introduces another explicit task that remains active after the turn, choose replace.
           - If the current turn abandons one task and introduces another task that is also fully completed in the same turn, choose clear because no active executable goal remains after the turn.
           - If the current turn introduces a brand new factual information request and that request is fully answered in the same turn, choose empty because no active executable goal remains after the turn.
        """
        self.memory_analysis_current_goal_outcome_rules = """
           Outcome rules:
           - Clarification question for an unfinished task means the task remains active after the turn.
           - Confirmation request for an unfinished task means the task remains active after the turn.
           - Immediate execution means the task is not active after the turn unless the assistant explicitly leaves another required step unfinished.
           - Final factual answer means the task is not active after the turn.
           - Explicit cancellation, abandonment, or refusal with no new task means the old task is not active after the turn.
           - Explicit pivot to a different executable task means the old task is not active after the turn and the new task becomes the replacement task only if that new task still remains active after the turn.
           - If the pivoted-to task is already fully completed in the same turn, choose clear when an old task existed before the turn, not replace.
           - If the assistant asks for confirmation about a now-resolved slot like a specific app name, the task remains active and CURRENT_GOAL must include the resolved entity instead of an outdated Missing detail.
           - If the assistant immediately executes the same browser/search/app task in this turn, that task is completed after the turn and should not be treated as a newly set task.
        """
        self.memory_analysis_current_goal_missing_detail_rules = """
           Missing detail rules:
           - Add "Missing detail: ..." only when one required detail is truly blocking execution right now.
           - Add "Missing detail: ..." only when the assistant explicitly asks for that detail in this response.
           - Keep only one most critical missing detail.
           - Do not keep old missing details once they are provided, no longer relevant, or the task is completed.
           - If the task is executable now, do not include Missing detail.
        """
        self.memory_analysis_current_goal_examples = """
           Good examples:
           - GOAL_STATE: set / CURRENT_GOAL: User wants to send a message to Sophia. Missing detail: message text.
           - GOAL_STATE: keep / CURRENT_GOAL: User wants to send a message to Sophia. Missing detail: message text.
           - GOAL_STATE: clear / CURRENT_GOAL: EMPTY
           - GOAL_STATE: replace / CURRENT_GOAL: User wants to open an app. Missing detail: app name.
           - GOAL_STATE: empty / CURRENT_GOAL: EMPTY
           - USER: Send a message to Sophia / ASSISTANT: What message would you like to send to Sophia? -> GOAL_STATE: set
           - USER: Tell her I will be late / ASSISTANT: What exactly would you like me to tell Sophia? -> GOAL_STATE: keep
           - USER: Tell her I will be late / ASSISTANT: Sending your message to Sophia. -> GOAL_STATE: clear
           - EXISTING_CURRENT_GOAL: User wants to send a message to Sophia. Missing detail: message text. / USER: No, open an app instead / ASSISTANT: Which app do you want to open? -> GOAL_STATE: replace / CURRENT_GOAL: User wants to open an app. Missing detail: app name.
           - USER: How are you? / ASSISTANT: I am doing well, thank you. -> GOAL_STATE: empty
           - USER: Find news / ASSISTANT: What kind of news do you want? -> GOAL_STATE: set
           - USER: World news / ASSISTANT: Searching for the latest world news. -> GOAL_STATE: keep
           - EXISTING_CURRENT_GOAL: User wants news. Missing detail: topic. / USER: World news / ASSISTANT: Here are the latest world news headlines. -> GOAL_STATE: clear
           - EXISTING_CURRENT_GOAL: User wants news. Missing detail: topic. / USER: World news / ASSISTANT: Here are the latest world news headlines. -> GOAL_STATE: clear / CURRENT_GOAL: EMPTY
           - USER: Send a WhatsApp message to Mom / ASSISTANT: What message do you want to send to Mom? -> GOAL_STATE: set
           - USER: Send a WhatsApp message to Mom / ASSISTANT: What would you like to say to Mom? -> GOAL_STATE: set / CURRENT_GOAL: User wants to send a WhatsApp message to Mom. Missing detail: message text.
           - EXISTING_CURRENT_GOAL: User wants to send a WhatsApp message to Mom. Missing detail: message text. / USER: Tell Mom I arrived / ASSISTANT: Sending your WhatsApp message to Mom. -> GOAL_STATE: clear
           - EXISTING_CURRENT_GOAL: User wants to send a WhatsApp message to Mom. Missing detail: message text. / USER: Tell Mom I arrived / ASSISTANT: Sending message to Mom. -> GOAL_STATE: clear / CURRENT_GOAL: EMPTY
           - USER: Open Safari / ASSISTANT: Opening Safari. -> GOAL_STATE: empty
           - USER: Open Notes / ASSISTANT: Opening Notes. -> GOAL_STATE: empty
           - USER: Open YouTube and find sleep music / ASSISTANT: Opening YouTube to find sleep music. -> GOAL_STATE: empty
           - USER: Open YouTube and find sleep music / ASSISTANT: What should I find on YouTube? -> GOAL_STATE: set / CURRENT_GOAL: User wants to search YouTube for sleep music.
           - USER: Open YouTube and play jazz / ASSISTANT: Opening YouTube to play jazz. -> GOAL_STATE: empty
           - EXISTING_CURRENT_GOAL: User wants to open YouTube and play jazz. / USER: sleep music instead / ASSISTANT: Opening YouTube and searching for sleep music. -> GOAL_STATE: clear
           - USER: Open an app / ASSISTANT: Which app do you want to open? -> GOAL_STATE: set
           - USER: Safari / ASSISTANT: Do you want me to open Safari now? -> GOAL_STATE: keep / CURRENT_GOAL: User wants to open Safari.
           - USER: Safari / ASSISTANT: Opening Safari. -> GOAL_STATE: empty
           - EXISTING_CURRENT_GOAL: User wants to open an app. Missing detail: app name. / USER: Safari / ASSISTANT: Do you want me to open Safari now? -> GOAL_STATE: keep / CURRENT_GOAL: User wants to open Safari.
           - USER: To John: running late / ASSISTANT: Sending message to John. -> GOAL_STATE: empty
           - USER: Send a message / ASSISTANT: Who should I send the message to? -> GOAL_STATE: set / CURRENT_GOAL: User wants to send a message. Missing detail: recipient.
           - USER: Find latest world news / ASSISTANT: Here are the latest world news headlines. -> GOAL_STATE: empty / CURRENT_GOAL: EMPTY
           - USER: Find latest world news / ASSISTANT: The latest world news includes ongoing tensions in the Middle East ... -> GOAL_STATE: empty / CURRENT_GOAL: EMPTY
           - EXISTING_CURRENT_GOAL: User wants to send a message to Sophia. Missing detail: message text. / USER: Actually open Notes instead / ASSISTANT: Opening Notes. -> GOAL_STATE: clear / CURRENT_GOAL: EMPTY
           - EXISTING_CURRENT_GOAL: User wants to send a message to Sophia. Missing detail: message text. / USER: Actually find world news instead / ASSISTANT: Here are the latest world news headlines. -> GOAL_STATE: clear
           - EXISTING_CURRENT_GOAL: User wants to send a message to Sophia. Missing detail: message text. / USER: Tell her I will be late / ASSISTANT: Sending message to Sophia. -> GOAL_STATE: clear / CURRENT_GOAL: EMPTY
           - EXISTING_CURRENT_GOAL: User wants news. Missing detail: topic. / USER: world news / ASSISTANT: Here are the latest world news headlines. -> GOAL_STATE: clear / CURRENT_GOAL: EMPTY
           - EXISTING_CURRENT_GOAL: EMPTY / USER: world news / ASSISTANT: Here are the latest world news headlines. -> GOAL_STATE: empty / CURRENT_GOAL: EMPTY
           - EXISTING_CURRENT_GOAL: EMPTY / USER: Find latest world news / ASSISTANT: The latest world news includes ongoing tensions in the Middle East ... -> GOAL_STATE: empty / CURRENT_GOAL: EMPTY
           - EXISTING_CURRENT_GOAL: User wants to send a message to Sophia. Missing detail: message text. / USER: Actually find world news instead / ASSISTANT: Here are the latest world news headlines. -> GOAL_STATE: clear / CURRENT_GOAL: EMPTY
           - EXISTING_CURRENT_GOAL: EMPTY / USER: Open YouTube and find sleep music / ASSISTANT: What should I find on YouTube? -> GOAL_STATE: set / CURRENT_GOAL: User wants to search YouTube for sleep music.
           - EXISTING_CURRENT_GOAL: User wants news. Missing detail: topic. / USER: world news / ASSISTANT: Searching for the latest world news. -> GOAL_STATE: keep / CURRENT_GOAL: User wants latest world news.
           - EXISTING_CURRENT_GOAL: User wants to send a message to Sophia. Missing detail: message text. / USER: No, never mind / ASSISTANT: Okay, I will not continue that task. -> GOAL_STATE: clear / CURRENT_GOAL: EMPTY
           - EXISTING_CURRENT_GOAL: User wants to send a message to Sophia. Missing detail: message text. / USER: No, open Safari instead / ASSISTANT: Opening Safari. -> GOAL_STATE: clear / CURRENT_GOAL: EMPTY
           - EXISTING_CURRENT_GOAL: User wants to open YouTube and play jazz. / USER: sleep music instead / ASSISTANT: Opening YouTube and searching for sleep music. -> GOAL_STATE: clear / CURRENT_GOAL: EMPTY
           - CURRENT_GOAL examples:
             User wants to send a message to Sophia. Missing detail: message text.
             User wants latest world news.
             User wants to open Safari.
             User wants to search YouTube for creep by Eminem.
        """
        self.memory_analysis_current_goal_prompt_active = "\n".join(
            [
                self.memory_analysis_current_goal_prompt_header.strip(),
                self.memory_analysis_current_goal_universal_policy.strip(),
                self.memory_analysis_current_goal_activation_rules.strip(),
                self.memory_analysis_current_goal_decision_framework.strip(),
                self.memory_analysis_current_goal_lifecycle_rules.strip(),
                self.memory_analysis_current_goal_task_identity_rules.strip(),
                self.memory_analysis_current_goal_outcome_rules.strip(),
                self.memory_analysis_current_goal_missing_detail_rules.strip(),
                self.memory_analysis_current_goal_examples.strip(),
            ]
        )
        self.memory_analysis_current_goal_prompt_inactive = """
        0) CURRENT GOAL (active executable user goal):
           Return GOAL_STATE exactly as empty.
           GOAL_STATE: empty
           CURRENT_GOAL update is inactive for this call.
           Return CURRENT_GOAL exactly as EXISTING_CURRENT_GOAL (or EMPTY if no existing value).
           Do NOT derive new current goals in this call.
        """

        # 1) SHORT-TERM memory section (active/inactive variants).
        self.memory_analysis_short_term_prompt_active = """
        1) SHORT-TERM MEMORY (current operational context):
           Store ONLY one concise line for the latest user-assistant interaction.
           Do NOT store JSON payloads, tool call schemas, or technical execution dumps.
           Keep plain text, compact, factual.
           SHORT_TERM must be exactly one line and must describe only the current turn.
           SHORT_TERM line must be logically complete and self-contained (full meaning without missing context).
           Never store sentence fragments or clipped endings.
           REQUIRED exact shape:
           [YYYY-MM-DD HH:MM:SS UTC] USER: <plain summary> | ASSISTANT: <plain summary>
           Use exactly one timestamp prefix, one USER part, and one ASSISTANT part.
           Do NOT include labels like CURRENT, PREVIOUS, TURN, CONTEXT, CURRENT_REQUEST, PREVIOUS_REQUEST_n, DATE_UTC, TIME_UTC.
           For action/tool requests (open app, send message, browser actions), store only natural-language text:
           - What the user asked in plain words;
           - What assistant answered/did in plain words.
           - If assistant response contains JSON, command payload, args, tool schema, or runtime action metadata,
             rewrite it into one short plain-language action description before storing memory.
           - Example rewrites:
             {"command":"open_app","args":{"app_name":"Safari"}} -> opened Safari
             {"command":"browser_search","args":{"query":"weather in Toronto"}} -> started a browser search for weather in Toronto
             {"command":"send_message","args":{"contact":"Sophia"}} -> prepared or sent a message to Sophia
           Do NOT store JSON/tool payloads. Keep only human-readable user request and assistant reply.
           DO NOT STORE (examples):
           - {"tool":"send_message","to":"Sofia","payload":{"text":"I am late"}}
           - function=open_app args={"app":"Messages","bundle_id":"com.apple.MobileSMS"}
           - action_id=93; selector="#send-btn"; request_id="ab12-ff09"
        """
        self.memory_analysis_short_term_prompt_inactive = """
        1) SHORT-TERM MEMORY (current operational context):
           SHORT_TERM update is inactive for this call.
           Return SHORT_TERM exactly as EXISTING_SHORT_MEMORY (or EMPTY if no existing value).
           Do NOT derive new short-term summaries in this call.
        """

        # 2) MEDIUM-TERM memory section (active/inactive variants).
        self.memory_analysis_medium_term_prompt_active = """
        2) MEDIUM-TERM MEMORY (daily analytical summary):
           MEDIUM_TERM is a day-level summary built from short-term interactions.
           MEDIUM_TERM MUST be derived from current + existing SHORT_TERM context (not from raw tool payloads).
           This section is active only in the dedicated once-per-24-hours medium-rollup call controlled by runtime/orchestrator.
           Return EXACTLY one new MEDIUM_TERM line for the current day.
           Do NOT return the whole historical medium memory when this section is active.
           The line should briefly and logically summarize what happened during the day:
           - which goals were pursued;
           - what kinds of tasks were performed overall;
           - what meaningful outcomes were achieved;
           - what was special/important that day.
           - what assistant requested/clarified from the user that day.
           Keep medium-term concise and meaningful.
           Do NOT copy raw dialogue and do NOT include runtime/transcript labels.
           If the day included tool/action execution represented as JSON or payloads, rewrite that into short plain-language descriptions of what assistant did.
           REQUIRED exact shape:
           [YYYY-MM-DD] <complete daily summary sentence>
           One line = one day summary.
           The summary sentence may mention goals, key tasks, completed work, pending work, and assistant clarifications, but keep it as plain text.
           If there is no useful medium-term info, output EMPTY.
        """
        self.memory_analysis_medium_term_prompt_inactive = """
        2) MEDIUM-TERM MEMORY (daily analytical summary):
           MEDIUM_TERM rollup is inactive for this call.
           Return MEDIUM_TERM exactly as EXISTING_MEDIUM_MEMORY (or EMPTY if no existing value).
           Do NOT derive new medium-term summaries in this call.
        """

        # 3) LONG-TERM memory section (active/inactive variants).
        self.memory_analysis_long_term_prompt_active = """
        3) LONG-TERM MEMORY (stable user profile, cross-session):
           Keep it concise, but preserve all necessary key points and keywords for personalization.
           LONG_TERM must contain plain factual lines only.
           Each line must be one complete stable fact about the user.
           STRICT FACTS ONLY:
           - Store ONLY explicit user-stated facts or explicit "remember this" facts.
           - Do NOT infer, guess, or generalize from one-time requests.
           - Never use wording like: implied, inferred, likely, maybe, seems, probably.
           - If user says a direct fact (example: "I love sneakers"), this MAY be stored in LONG_TERM.
           - If user asks a task/request (example: "find me sneakers"), this is NOT a stable preference and MUST NOT be stored in LONG_TERM.
             Put such request context into MEDIUM_TERM only.
           REQUIRED durable profile facts (when explicitly provided) that MUST be remembered in LONG_TERM:
           - first name / last name / preferred name
           - email / contact identifier
           - timezone / preferred language / communication style
           - significant personal dates explicitly provided by user
           - information explicitly requested to remember ("remember this", "keep this")
           Useful stable facts include:
           - identity basics
           - communication preferences
           - work profile / recurring projects / project directories
           - recurring routines
           - stable interests / favorites / preferred apps or services
           - remembered facts user explicitly asked to keep
           Do not repeat the same factual statement more than once.
           - IMPORTANT: preserve valid facts from EXISTING_LONG_MEMORY unless explicitly contradicted by the user now.
           - If current turn has no new long-term facts, keep previously valid EXISTING_LONG_MEMORY facts (do not drop them).
           - Identity facts (for example user name) are persistent and should remain until user explicitly changes/corrects them.
           - If user asks to forget/remove only specific information (for example: name, preference, one fact),
             remove ONLY those requested facts from LONG_TERM and keep all other valid facts.
           - For partial forget requests, return LONG_TERM as updated fact list without deleted items (do not use clear marker).
           - If user explicitly asks to forget/clear stored profile memory, set:
             LONG_TERM: __CLEAR_LONG_TERM__
             (use exactly this marker and nothing else in LONG_TERM).

           For sensitive data:
           - If user explicitly asks to remember credentials/secrets (including password), store only a safe factual reference,
             never raw secret values.
           - Allowed example: User has Gmail account credentials saved elsewhere.
           - Forbidden examples: raw password, raw token, raw api key, full secret strings.

           NEVER store in LONG_TERM:
           - one-time transient task details;
           - temporary failures/UI states;
           - internal technical execution details.
           - raw JSON, command payloads, args objects, tool schemas, or runtime action metadata.

           If there is no useful info for a section, output EMPTY for that section.

           Canonical full response example:
           SHORT_TERM: [2026-03-04 14:22:11 UTC] USER: compare Nike Pegasus options and remember delivery priority Friday | ASSISTANT: options compared and delivery priority acknowledged
           MEDIUM_TERM: [2026-03-04] User compared running shoe options, updated delivery priority, and completed the shopping discussion for the day.
           LONG_TERM: User's name is Sergey Zasorin.
           User prefers concise communication.
           User is interested in running shoes.
        """
        self.memory_analysis_long_term_prompt_inactive = """
        3) LONG-TERM MEMORY (stable user profile, cross-session):
           LONG_TERM update is inactive for this call.
           Return LONG_TERM exactly as EXISTING_LONG_MEMORY (or EMPTY if no existing value).
           Do NOT derive new long-term facts in this call.
        """

        # Backward-compatible default prompt: all sections active.
        self.memory_analysis_prompt = self.build_memory_analysis_prompt(
            include_current_goal=True,
            include_short_term=True,
            include_medium_rollup=True,
            include_long_term=True,
        )
        self.memory_analysis_prompt_without_medium_rollup = self.build_memory_analysis_prompt(
            include_current_goal=True,
            include_short_term=True,
            include_medium_rollup=False,
            include_long_term=True,
        )

    def get_config_dict(self) -> Dict[str, Any]:
        """Возвращает конфигурацию в виде словаря"""
        return {
            'GEMINI_API_KEY': self.gemini_api_key,
            'MAX_SHORT_TERM_MEMORY_SIZE': self.max_short_term_memory_size,
            'MAX_LONG_TERM_MEMORY_SIZE': self.max_long_term_memory_size,
            'MEMORY_TIMEOUT': self.memory_timeout,
            'ANALYSIS_TIMEOUT': self.analysis_timeout,
            'MEMORY_ANALYSIS_MODEL': self.memory_analysis_model,
            'MEMORY_ANALYSIS_TEMPERATURE': self.memory_analysis_temperature,
            'USE_VERTEX_AI': self.use_vertex_ai,
            'VERTEX_PROJECT': self.vertex_project,
            'VERTEX_LOCATION': self.vertex_location,
            'MEMORY_ANALYSIS_PROMPT': self.memory_analysis_prompt,
        }

    def build_memory_analysis_prompt(
        self,
        include_current_goal: bool = True,
        include_short_term: bool = True,
        include_medium_rollup: bool = True,
        include_long_term: bool = True,
    ) -> str:
        current_goal_section = (
            self.memory_analysis_current_goal_prompt_active
            if include_current_goal
            else self.memory_analysis_current_goal_prompt_inactive.strip()
        )
        short_section = (
            self.memory_analysis_short_term_prompt_active
            if include_short_term
            else self.memory_analysis_short_term_prompt_inactive.strip()
        )
        medium_section = (
            self.memory_analysis_medium_term_prompt_active
            if include_medium_rollup
            else self.memory_analysis_medium_term_prompt_inactive.strip()
        )
        long_section = (
            self.memory_analysis_long_term_prompt_active
            if include_long_term
            else self.memory_analysis_long_term_prompt_inactive.strip()
        )
        return "\n\n".join(
            [
                self.memory_analysis_prompt_preamble.strip(),
                current_goal_section.strip(),
                short_section.strip(),
                medium_section.strip(),
                long_section.strip(),
            ]
        ).strip() + "\n"

    def build_current_goal_prompt(
        self,
        active: bool = True,
    ) -> str:
        """Return the dedicated CURRENT_GOAL prompt block for easier management/testing."""
        if active:
            return self.memory_analysis_current_goal_prompt_active.strip()
        return self.memory_analysis_current_goal_prompt_inactive.strip()

    def validate_config(self) -> bool:
        """Проверяет корректность конфигурации"""
        if self.use_vertex_ai:
            if not self.vertex_project:
                print("⚠️ GOOGLE_CLOUD_PROJECT не установлен для Vertex memory analysis")
                return False
            if not self.vertex_location:
                print("⚠️ GOOGLE_CLOUD_LOCATION не установлен для Vertex memory analysis")
                return False
        elif not self.gemini_api_key:
            print("⚠️ GEMINI_API_KEY не установлен")
            return False

        if self.memory_timeout <= 0 or self.analysis_timeout <= 0:
            print("❌ memory_timeout и analysis_timeout должны быть больше 0")
            return False

        if self.max_short_term_memory_size <= 0 or self.max_long_term_memory_size <= 0:
            print("❌ max_short_term_memory_size и max_long_term_memory_size должны быть больше 0")
            return False

        return True
