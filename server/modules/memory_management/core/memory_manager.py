"""
Memory Manager - координатор всех операций с памятью

Обеспечивает:
- Получение контекста памяти для LLM
- Координацию анализа и обновления памяти
- Интеграцию с Database Module
- Совместимость с существующим TextProcessor
"""

import asyncio
import logging
import re
from typing import Any, Dict, Optional, Tuple, Union

from ..config import MemoryConfig
from ..providers.memory_analyzer import MemoryAnalyzer

logger = logging.getLogger(__name__)

class MemoryManager:
    """
    Координатор всех операций с памятью пользователей.
    
    Интегрируется с существующим TextProcessor без изменения его логики.
    Предоставляет те же методы, которые ожидает TextProcessor.
    """
    
    def __init__(self, db_manager=None, token_usage_tracker=None):
        """
        Инициализация MemoryManager.
        
        Args:
            db_manager: Экземпляр DatabaseManager для работы с БД
            token_usage_tracker: Сервис трекинга токенов (опционально)
        """
        self.config = MemoryConfig()
        self.db_manager = db_manager
        self.token_usage_tracker = token_usage_tracker
        self.memory_analyzer = None
        self.is_initialized = False
        
    async def initialize(self):
        """Инициализация MemoryManager"""
        try:
            # Инициализируем MemoryAnalyzer если доступен API ключ
            if self.config.gemini_api_key and self.config.validate_config():
                try:
                    self.memory_analyzer = MemoryAnalyzer(
                        self.config.gemini_api_key,
                        token_tracker=self.token_usage_tracker,
                        model_name=self.config.memory_analysis_model,
                        temperature=self.config.memory_analysis_temperature,
                        analysis_prompt_template=self.config.memory_analysis_prompt,
                    )
                    logger.info("✅ MemoryAnalyzer initialized successfully")
                except Exception as e:
                    logger.warning(f"⚠️ MemoryAnalyzer initialization failed: {e}")
                    self.memory_analyzer = None
            else:
                logger.warning("⚠️ MemoryAnalyzer not initialized - missing API key or invalid config")
            
            self.is_initialized = True
            logger.info("✅ MemoryManager initialized successfully")
            return True
        except Exception as e:
            logger.error(f"❌ MemoryManager initialization failed: {e}")
            raise
    
    def set_database_manager(self, db_manager):
        """
        Устанавливает DatabaseManager для работы с памятью.
        
        Args:
            db_manager: Экземпляр DatabaseManager
        
        Этот метод нужен для совместимости с существующим TextProcessor.
        """
        self.db_manager = db_manager
        logger.info("✅ DatabaseManager set in MemoryManager")
    
    async def get_memory_context(self, hardware_id: str) -> Union[Dict[str, Any], str]:
        """
        Получает контекст памяти для LLM.
        
        Args:
            hardware_id: Аппаратный ID пользователя
            
        Returns:
            Словарь с контекстом памяти или пустая строка
            
        Этот метод заменяет логику из text_processor.py (строки 254-282)
        """
        if not hardware_id or not self.db_manager:
            return {}
        
        try:
            # Таймаут 2 секунды на получение памяти (как в оригинале)
            # Таймаут 2 секунды на получение памяти (как в оригинале)
            memory_data = await asyncio.wait_for(
                self.db_manager.get_user_memory(hardware_id),
                timeout=self.config.memory_timeout
            )
            
            if memory_data.get('short') or memory_data.get('long'):
                # Возвращаем словарь, как ожидает StreamingWorkflowIntegration
                return {
                    "recent_context": memory_data.get('short', ''),
                    "long_term_context": memory_data.get('long', ''),
                    "formatted_prompt": f"""
🧠 MEMORY CONTEXT (for response context):

📋 SHORT-TERM MEMORY (current session):
{memory_data.get('short', 'No short-term memory')}

📚 LONG-TERM MEMORY (user information):
{memory_data.get('long', 'No long-term memory')}

💡 MEMORY USAGE INSTRUCTIONS:
- Use short-term memory to understand current conversation context
- Use long-term memory for response personalization
- Memory should complement the answer, not replace it
"""
                }
            else:
                logger.info(f"🧠 No memory found for {hardware_id}")
                return ""
                    
        except asyncio.TimeoutError:
            logger.warning(f"⚠️ Memory retrieval timeout for {hardware_id}")
            return ""
        except Exception as e:
            logger.error(f"❌ Error getting memory context for {hardware_id}: {e}")
            return ""
    
    async def analyze_conversation(self, prompt: str, response: str, hardware_id: Optional[str] = None) -> Tuple[str, str]:
        """
        Анализирует диалог для извлечения памяти.
        
        Args:
            prompt: Запрос пользователя
            response: Ответ ассистента
            hardware_id: ID устройства для трекинга (опционально)
            
        Returns:
            Кортеж (short_memory, long_memory)
            
        Этот метод заменяет вызов memory_analyzer.analyze_conversation()
        """
        if not self.memory_analyzer:
            logger.debug("🧠 MemoryAnalyzer not available - using heuristic memory extraction")
            return self._extract_memory_heuristic(prompt, response)
        
        try:
            return await self.memory_analyzer.analyze_conversation(prompt, response, hardware_id=hardware_id)
        except Exception as e:
            logger.error(f"❌ Error analyzing conversation: {e}")
            return "", ""

    def _extract_memory_heuristic(self, prompt: str, response: str) -> Tuple[str, str]:
        """
        Lightweight fallback extraction when Gemini analyzer is unavailable.

        Keeps one owner-path for memory updates and avoids "no-op memory" in runtime.
        """
        try:
            text = (prompt or "").strip()
            if not text:
                return "", ""

            normalized = text.lower()

            # Explicit remember intents (RU/EN)
            remember_intent = bool(
                re.search(
                    r"\b(запомни|запомни это|не забудь|remember this|remember that|keep (this|that) in mind)\b",
                    normalized,
                )
            )

            long_candidates: list[str] = []

            # Preference patterns: "я люблю X", "I like X", "мой любимый X"
            pref_patterns = [
                r"\bя люблю\s+([^.!?\n]+)",
                r"\bi like\s+([^.!?\n]+)",
                r"\bмой любим(?:ый|ая|ое|ые)\s+([^.!?\n]+)",
                r"\bmy favorite\s+([^.!?\n]+)",
            ]
            for pattern in pref_patterns:
                match = re.search(pattern, normalized, flags=re.IGNORECASE)
                if match:
                    fact = match.group(1).strip(" ,;:.")
                    if fact:
                        long_candidates.append(fact)

            # Extract fact after remember command if explicit preference wasn't found.
            if remember_intent and not long_candidates:
                remember_payload_patterns = [
                    r"(?:запомни(?: это)?[:\s-]*)([^.!?\n]+)",
                    r"(?:remember (?:this|that)[:\s-]*)([^.!?\n]+)",
                ]
                for pattern in remember_payload_patterns:
                    match = re.search(pattern, text, flags=re.IGNORECASE)
                    if match:
                        fact = match.group(1).strip(" ,;:.")
                        if fact:
                            long_candidates.append(fact)
                            break

            if not long_candidates:
                return "", ""

            # Security guard: never store raw secrets as memory values.
            secret_pattern = re.compile(
                r"\b(password\w*|парол\w*|token\w*|токен\w*|api[_ -]?key|ключ\w*)\b",
                flags=re.IGNORECASE,
            )
            sanitized_candidates = []
            for candidate in long_candidates:
                if secret_pattern.search(candidate):
                    sanitized_candidates.append("User asked to remember credentials for a service")
                else:
                    sanitized_candidates.append(candidate)

            # Deduplicate while preserving order
            unique: list[str] = []
            seen: set[str] = set()
            for item in sanitized_candidates:
                key = item.lower()
                if key in seen:
                    continue
                seen.add(key)
                unique.append(item)

            long_memory = "; ".join(f"User prefers {item}" for item in unique)
            short_memory = (
                "User explicitly asked to remember this information"
                if remember_intent
                else ""
            )
            return short_memory, long_memory
        except Exception as e:
            logger.warning(f"⚠️ Heuristic memory extraction failed: {e}")
            return "", ""
    
    async def update_memory_background(self, hardware_id: str, prompt: str, response: str) -> Optional[Dict[str, str]]:
        """
        Фоновое обновление памяти пользователя.
        
        Args:
            hardware_id: Аппаратный ID пользователя
            prompt: Запрос пользователя
            response: Ответ ассистента
            
        Этот метод заменяет _update_memory_background() из text_processor.py
        """
        try:
            logger.debug(f"🔄 Starting background memory update for {hardware_id}")
            
            # Анализируем разговор для извлечения памяти
            short_memory, long_memory = await self.analyze_conversation(prompt, response, hardware_id=hardware_id)
            
            # Если есть что сохранять
            if short_memory or long_memory:
                # Проверяем наличие менеджера базы данных
                if not self.db_manager:
                    logger.warning("⚠️ DatabaseManager is not set in MemoryManager; skipping memory update")
                    return None
                # Обновляем память в базе данных
                success = await self.db_manager.update_user_memory(
                    hardware_id,
                    short_memory,
                    long_memory
                )
                
                if success:
                    logger.info(f"✅ Memory for {hardware_id} updated: short-term ({len(short_memory)} chars), long-term ({len(long_memory)} chars)")
                    return {"short": short_memory, "long": long_memory}
                else:
                    logger.warning(f"⚠️ Could not update memory for {hardware_id}")
                    return None
            else:
                logger.debug(f"🧠 No information found for {hardware_id} to remember")
                return None
                
        except Exception as e:
            logger.error(f"❌ Error in background memory update for {hardware_id}: {e}")
            # НЕ поднимаем исключение - это фоновая задача
            return None
    
    def is_available(self) -> bool:
        """
        Проверяет доступность модуля памяти.
        
        Returns:
            True если модуль готов к работе
        """
        return self.memory_analyzer is not None and self.db_manager is not None
    
    async def cleanup_expired_memory(self, hours: int = 24) -> int:
        """
        Очищает устаревшую краткосрочную память.
        
        Args:
            hours: Количество часов, после которых память считается устаревшей
            
        Returns:
            Количество очищенных записей
        """
        if not self.db_manager:
            return 0
        
        try:
            return await self.db_manager.cleanup_expired_short_term_memory(hours)
        except Exception as e:
            logger.error(f"❌ Error cleaning up expired memory: {e}")
            return 0
