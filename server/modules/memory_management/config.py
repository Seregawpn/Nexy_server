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
        
        # Промпты для анализа памяти
        self.memory_analysis_prompt = """
        Analyze this conversation between user and AI assistant to extract memory information.

        USER INPUT: {prompt}
        AI RESPONSE: {response}
        CURRENT_DATE_UTC: {current_date_utc}
        EXISTING_SHORT_MEMORY: {existing_short_memory}
        EXISTING_MEDIUM_MEMORY: {existing_medium_memory}
        EXISTING_LONG_MEMORY: {existing_long_memory}

        CRITICAL:
        - You MUST respond ONLY in English.
        - Return ONLY the canonical response block below and nothing else:
          SHORT_TERM: <text or EMPTY>
          MEDIUM_TERM: <text or EMPTY>
          LONG_TERM: <text or EMPTY>
        - Use each section label exactly once.
        - Section order is mandatory: SHORT_TERM, then MEDIUM_TERM, then LONG_TERM.
        - Each section value must be on a single line.
        - If you need multiple facts inside one section, separate them with "; " on the same line.
        - Do not add any extra labels, prefixes, suffixes, headings, explanations, markdown, quotes, or code fences.
        - Do not output any text before SHORT_TERM or after LONG_TERM.
        - Keep output concise and factual.
        - Record information in brief form, but include all necessary key points and keywords.
        - Use plain text only.
        - Do NOT duplicate information inside a section.
        - Each fact must appear only once per section.
        - Do not include explanations outside these three sections.
        - Treat EXISTING_SHORT_MEMORY, EXISTING_MEDIUM_MEMORY and EXISTING_LONG_MEMORY as read-only context.
        - EXISTING_SHORT_MEMORY is operational session context only. Do not copy it into LONG_TERM unless user explicitly states a durable fact now.
        - Do not repeat facts that already exist in existing memory.
        - Do not promote medium-term topic into LONG_TERM unless user explicitly stated a durable fact now.
        - If user explicitly asks to forget/remove specific information, you MUST remove that information from all relevant memory sections (SHORT_TERM, MEDIUM_TERM, LONG_TERM) in your output.
        - Forget requests are mandatory: do not keep requested-to-forget facts in any memory section.

        1) SHORT-TERM MEMORY (current operational context):
           Store only current communication continuity in one line.
           Use compact clauses separated by "; ".
           Example style: "current request ...; progress ...; previous result ...".
           Do not include timestamps or multiline formatting.
           If there is no useful short-term info, output EMPTY.

        2) MEDIUM-TERM MEMORY (cross-session digest):
           Store compact cross-session references in one line.
           Every medium-term fact MUST start with date in format [YYYY-MM-DD].
           Use compact dated facts separated by "; " (for example: "[2026-02-28] discussed X; result Y").
           Keep only important prior choices/topics and outcomes.
           Use ONLY CURRENT_DATE_UTC as the reference date for aging (never use local/system inferred date).
           CURRENT_DATE_UTC is always provided in input and is the only "today" value you may use.
           Daily accumulation policy (MEDIUM_TERM only):
           - Keep existing medium-term records from previous dates.
           - When CURRENT_DATE_UTC is a new date not present in MEDIUM_TERM, create a new dated record for that date.
           - When CURRENT_DATE_UTC date already exists in MEDIUM_TERM, update/append that same date record with new facts from this day.
           - Keep one consolidated record per date (no duplicate records for the same date).
           - Never delete previous-date records just because a new day started.
           Aging algorithm for MEDIUM_TERM:
           Step 1: Parse entry date from [YYYY-MM-DD] at the beginning of each medium-term fact.
           Step 2: Compute age_days = (CURRENT_DATE_UTC - entry_date) in full calendar days.
           Step 3: If age_days > 30, remove this medium-term fact.
           Step 4: If age_days <= 30, keep this medium-term fact.
           Step 5: If a medium-term fact has no valid [YYYY-MM-DD], remove it from MEDIUM_TERM output.
           This 30-day removal rule applies ONLY to MEDIUM_TERM.
           Do NOT remove LONG_TERM facts because of age.
           If there is no useful medium-term info, output EMPTY.

        3) LONG-TERM MEMORY (stable user profile, cross-session):
           Keep it concise, but preserve all necessary key points and keywords for personalization.
           STRICT FACTS ONLY:
           - Store ONLY explicit user-stated facts or explicit "remember this" facts.
           - Do NOT infer, guess, or generalize from one-time requests.
           - Never use wording like: implied, inferred, likely, maybe, seems, probably.
           - If user says a direct fact (example: "I love sneakers"), this MAY be stored in LONG_TERM.
           - If user asks a task/request (example: "find me sneakers"), this is NOT a stable preference and MUST NOT be stored in LONG_TERM.
             Put such request context into MEDIUM_TERM only.
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
           - If user explicitly asks to remember credentials/secrets, store only a safe reference,
             never raw secret values.
           - Allowed example: "user has credentials for gmail account".
           - Forbidden examples: raw password, raw token, raw api key.

           NEVER store in LONG_TERM:
           - one-time transient task details;
           - temporary failures/UI states;
           - internal technical execution details.

        If there is no useful info for a section, output EMPTY for that section.
        """
    
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
            'MEMORY_ANALYSIS_PROMPT': self.memory_analysis_prompt
        }
    
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
