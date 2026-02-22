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

        CRITICAL:
        - You MUST respond ONLY in English.
        - Return exactly two lines in this format:
          SHORT_TERM: ...
          LONG_TERM: ...
        - Keep output concise and factual.

        Extraction policy:
        1) SHORT-TERM MEMORY (session context, quickly expiring, operational):
           Store ONLY what is needed to continue the current flow:
           - active user goal and current task state;
           - unresolved requests and pending next step;
           - temporary constraints (format, language, style, scope, deadline in this session);
           - current working context (site/app/page/entity user is interacting with now);
           - latest user correction/override ("not this, do that").
           Keep short-term compact: max 2-4 short actionable points.
           Remove obsolete points when task context changes.

           NEVER store in SHORT_TERM:
           - assistant internal artifacts, tool names, JSON/service internals, debug logs;
           - generic phrases without concrete value;
           - completed/obsolete details that no longer affect next step.

        2) LONG-TERM MEMORY (stable user profile, cross-session):
           Store durable facts/preferences that help in future sessions:
           - identity basics: name/surname/nickname/pronunciation preferences;
           - communication preferences: language, tone, brevity/detail level;
           - stable interests: favorite music, artists, movies, series, books, sports;
           - digital habits: favorite websites/services/apps used repeatedly;
           - work profile: projects, roles, recurring work context, long-term goals;
           - recurring routines: actions user repeatedly does over time;
           - important personal facts user explicitly asks to remember;
           - explicit memory commands: "remember this", "keep this in mind".

           For sensitive data:
           - If user explicitly asks to remember credentials/secrets, store only a safe reference
             (e.g., "user has credentials for service X"), NEVER store raw secret values.

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
