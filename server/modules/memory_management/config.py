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
        self.memory_analysis_current_goal_activation_rules = """
           Activation rules:
           - Use CURRENT_GOAL only when the user is performing or clarifying a concrete unfinished task.
           - If the turn is ordinary conversation, small talk, gratitude, capability/help, meta-conversation, or no executable goal exists, return EMPTY.
           - Do not store generic chat goals. Only executable user requests belong here.
        """
        self.memory_analysis_current_goal_lifecycle_rules = """
           Lifecycle rules:
           - Ask: "Would the assistant still be expected to execute this same task after this turn?"
           - If YES, CURRENT_GOAL may be set.
           - If NO, return EMPTY.
           - If assistant is asking a required clarification question for the same unfinished task, keep that task as CURRENT_GOAL.
           - If assistant already completed the task in this turn, CURRENT_GOAL must be EMPTY.
           - If the current turn does not clearly continue the previous task, CURRENT_GOAL must be EMPTY.
           - If the user switched to a new task or a new topic, replace the old goal or return EMPTY.
           - If the user explicitly rejects, cancels, abandons, or declines the previous task, CURRENT_GOAL must be EMPTY unless the same turn clearly starts a new executable task.
           - If the user says no, not now, never mind, leave it, I do not want that, or I want something else, treat the previous goal as inactive.
           - If the same turn both abandons the old goal and starts a new explicit task, set CURRENT_GOAL only for the new task.
           - Use GOAL_STATE=set when a new executable goal appears and there was no active previous goal.
           - Use GOAL_STATE=keep when the same goal stays active after this turn.
           - Use GOAL_STATE=clear when the previous goal is completed or abandoned and no new goal replaces it.
           - Use GOAL_STATE=replace when the previous goal is replaced by a new explicit executable goal.
           - Use GOAL_STATE=empty when no active executable goal exists.
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
           - GOAL_STATE: keep / CURRENT_GOAL: User wants to send a message to Sophia. Missing detail: message text.
           - GOAL_STATE: clear / CURRENT_GOAL: EMPTY
           - GOAL_STATE: replace / CURRENT_GOAL: User wants to open Safari.
           - GOAL_STATE: empty / CURRENT_GOAL: EMPTY
           - User wants to send a message to Sophia. Missing detail: message text.
           - User wants latest world news.
           - User wants to open Safari.
           - User wants to search YouTube for creep by Eminem.
        """
        self.memory_analysis_current_goal_prompt_active = "\n".join(
            [
                self.memory_analysis_current_goal_prompt_header.strip(),
                self.memory_analysis_current_goal_activation_rules.strip(),
                self.memory_analysis_current_goal_lifecycle_rules.strip(),
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
        if not self.gemini_api_key:
            print("⚠️ GEMINI_API_KEY не установлен")
            return False

        if self.memory_timeout <= 0 or self.analysis_timeout <= 0:
            print("❌ memory_timeout и analysis_timeout должны быть больше 0")
            return False

        if self.max_short_term_memory_size <= 0 or self.max_long_term_memory_size <= 0:
            print("❌ max_short_term_memory_size и max_long_term_memory_size должны быть больше 0")
            return False

        return True
