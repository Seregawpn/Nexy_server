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
        EXISTING_SHORT_MEMORY: {existing_short_memory}
        EXISTING_MEDIUM_MEMORY: {existing_medium_memory}
        EXISTING_LONG_MEMORY: {existing_long_memory}

        CRITICAL:
        - You MUST respond ONLY in English.
        - Populate each section strictly according to the mandatory detailed rules below.
        - If a section has no useful data, set it to EMPTY.
        - Do not add any extra labels, prefixes, suffixes, headings, explanations, markdown, quotes, or code fences.
        - Follow format only.
        - Keep output concise and factual.
        - Do NOT duplicate information inside a section.
        - Treat EXISTING_SHORT_MEMORY, EXISTING_MEDIUM_MEMORY and EXISTING_LONG_MEMORY as read-only context.
        - Preserve useful existing memory entries and update them with current-turn changes.
        - Merge policy is mandatory: output must include valid existing entries from EXISTING_SHORT_MEMORY, EXISTING_MEDIUM_MEMORY, and EXISTING_LONG_MEMORY, plus new/updated entries from the current turn.
        - Do not replace the whole section with only new data if older valid data exists; keep prior valid items and append/update them in canonical format.
        - Processing order is mandatory: first analyze/update SHORT_TERM, then derive/update MEDIUM_TERM from SHORT_TERM, and only after that SHORT_TERM may be reduced/cleaned by runtime policies.
        - Never lose day context: if SHORT_TERM contains useful daily activity, reflect it in MEDIUM_TERM before any short-term cleanup.
        - MEDIUM_TERM activation is trigger-based. Use activation phrase exactly: MEDIUM_TERM_ROLLUP_24H=ON.
        - If activation phrase is missing, keep MEDIUM_TERM unchanged from EXISTING_MEDIUM_MEMORY (or EMPTY if no existing value).
        - 24h cadence owner is runtime/orchestrator: trigger phrase should be injected no more than once per 24 hours.
        - Store only logically complete, self-contained text units. Never store broken fragments.
        - If a phrase is incomplete (example: "delivery by Friday"), rewrite it into a complete memory sentence (example: "Shoes deliver by Friday.").
        """

        # 1) SHORT-TERM memory section (active/inactive variants).
        self.memory_analysis_short_term_prompt_active = """
        1) SHORT-TERM MEMORY (current operational context):
           Store ONLY one concise line for the latest user-assistant interaction.
           Do NOT store JSON payloads, tool call schemas, or technical execution dumps.
           Keep plain text, compact, factual.
           SHORT_TERM must be exactly one line and must describe only the current turn.
           Do NOT include labels like CURRENT, PREVIOUS, TURN, TIME_UTC, CURRENT_REQUEST, PREVIOUS_REQUEST_n.
           SHORT_TERM line must be logically complete and self-contained (full meaning without missing context).
           Never store sentence fragments or clipped endings.
           Recommended shape:
           [YYYY-MM-DD] user_request=<plain summary>; assistant_reply=<plain summary>; outcome=<plain summary>
           For action/tool requests (open app, send message, browser actions), store only natural-language text:
           - What the user asked in plain words;
           - What assistant answered/did in plain words.
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
           MEDIUM_TERM must be recalculated/updated only when activation phrase MEDIUM_TERM_ROLLUP_24H=ON is present.
           Return EXACTLY one MEDIUM_TERM line (single-line output, no extra lines).
           Parser expects one line only: do not output multi-line bullets/tables/numbered blocks.
           It should briefly and logically summarize what happened during each day:
           - which goals were pursued;
           - what kinds of tasks were performed overall;
           - what meaningful outcomes were achieved;
           - what was special/important that day.
           Keep medium-term concise and meaningful.
           Do NOT copy raw dialogue and do NOT include runtime/transcript labels.
           Every entry MUST start with [YYYY-MM-DD].
           MEDIUM_TERM must be returned as a single output line.
           If there are multiple daily records, keep them in that same line separated by " || ".
           Ordering rule: newest record first, oldest record last.
           One record = one day summary (do NOT create separate records for each individual task).
           Within each day record, aggregate repeated requests into one consolidated summary.
           If same topic/request appeared multiple times that day, reflect frequency in repeat_signals (for example: messaging_intent x3).
           Do not duplicate topic/action/outcome values inside the same day record.
           Each day record must be a complete, logically finished text.
           MEDIUM_TERM must contain logically complete day summaries, not partial fragments.
           Preferred record shape:
           [YYYY-MM-DD] topic=<...>; daily_summary=<complete sentence>; key_actions=<category1|category2>; outcomes=<result1|result2>; repeat_signals=<signal1 xN|signal2 xM>; status=<done|in_progress|mixed>
           If there is no useful medium-term info, output EMPTY.
           Example:
           MEDIUM_TERM: [2026-03-03] topic=communication and search tasks; daily_summary=User focused on messaging, browser search, and news lookup, and the planned actions were completed successfully.; key_actions=messaging|browser_search|news_check; outcomes=message_sent|search_results_collected; repeat_signals=messaging_intent x3|browser_query x2; status=done || [2026-03-02] topic=communication tasks; daily_summary=User repeatedly worked on message drafting and recipient clarification, then completed the messaging flow.; key_actions=messaging|recipient_resolution; outcomes=recipient_confirmed|message_sent; repeat_signals=messaging_intent x4|recipient_clarification x2; status=done || [2026-03-01] topic=planning tasks; daily_summary=User focused on planning-related requests and part of actions remained open.; key_actions=planning; outcomes=plan_draft_created; repeat_signals=planning_intent x2; status=in_progress
           Visual ordering reference (newest on top, oldest below; for understanding only):
           [2026-03-03] ...
           [2026-03-02] ...
           [2026-03-01] ...
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
           Use compact clauses separated by "; ".
           LONG_TERM facts must be logically complete standalone facts (no broken fragments).
           STRICT FACTS ONLY:
           - Store ONLY explicit user-stated facts or explicit "remember this" facts.
           - Do NOT infer, guess, or generalize from one-time requests.
           - Never use wording like: implied, inferred, likely, maybe, seems, probably.
           - If user says a direct fact (example: "I love sneakers"), this MAY be stored in LONG_TERM.
           - If user asks a task/request (example: "find me sneakers"), this is NOT a stable preference and MUST NOT be stored in LONG_TERM.
             Put such request context into MEDIUM_TERM only.
           REQUIRED durable profile facts (when explicitly provided) that MUST be remembered in LONG_TERM:
           - first name / given name;
           - surname / family name;
           - stable email or contact identifier;
           - significant personal dates/events explicitly provided by user (birthday, anniversary, major life event);
           - information explicitly requested to remember ("remember this", "keep this").
           Store durable facts/preferences that help in future sessions:
           - identity basics: name/surname/nickname/pronunciation preferences;
           - profile facts: date of birth, marital status, family status if user explicitly provided;
           - communication preferences: language, tone, brevity/detail level;
           - stable interests: favorite music, artists, movies, series, books, sports;
           - digital habits: favorite websites/services/apps used repeatedly;
           - work profile: projects, roles, recurring work context, long-term goals;
           - critical recurring entities: important file names, folder paths, project directories;
           - stable contact facts: important emails/usernames/contact identifiers;
           - recurring routines: actions user repeatedly does over time;
           - important personal facts user explicitly asks to remember;
           - explicit memory commands: "remember this", "keep this in mind".
           - do not repeat the same factual statement more than once.
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
           - If user explicitly asks to remember credentials/secrets (including password), store only a safe reference,
             never raw secret values.
           - Allowed example: "user has credentials for gmail account".
           - Forbidden examples: raw password, raw token, raw api key, full secret strings.

           NEVER store in LONG_TERM:
           - one-time transient task details;
           - temporary failures/UI states;
           - internal technical execution details.

           If there is no useful info for a section, output EMPTY for that section.

           Canonical full response example:
           SHORT_TERM: [2026-03-04] user_request=compare Nike Pegasus options and remember delivery priority Friday; assistant_reply=profile details saved and options compared; outcome=priority recorded and comparison completed
           MEDIUM_TERM: [2026-03-04] topic=shopping and profile update tasks; daily_summary=User compared Nike Pegasus options and updated delivery priority for future actions.; key_actions=product_comparison|profile_update; outcomes=comparison_completed|delivery_priority_recorded; status=done || [2026-03-03] topic=communication tasks; daily_summary=User focused on messaging-related actions and completed planned communication tasks.; key_actions=messaging; outcomes=messages_prepared_or_sent; status=done
           LONG_TERM: name=Sergey; surname=Zasorin; email=sergey@example.com; stable_preference=running shoes (Nike Pegasus)
        """
        self.memory_analysis_long_term_prompt_inactive = """
        3) LONG-TERM MEMORY (stable user profile, cross-session):
           LONG_TERM update is inactive for this call.
           Return LONG_TERM exactly as EXISTING_LONG_MEMORY (or EMPTY if no existing value).
           Do NOT derive new long-term facts in this call.
        """

        # Backward-compatible default prompt: all sections active.
        self.memory_analysis_prompt = self.build_memory_analysis_prompt(
            include_short_term=True,
            include_medium_rollup=True,
            include_long_term=True,
        )
        self.memory_analysis_prompt_without_medium_rollup = self.build_memory_analysis_prompt(
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
        include_short_term: bool = True,
        include_medium_rollup: bool = True,
        include_long_term: bool = True,
    ) -> str:
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
                short_section.strip(),
                medium_section.strip(),
                long_section.strip(),
            ]
        ).strip() + "\n"

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
