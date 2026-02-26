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
from datetime import datetime, timedelta, timezone
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
        self._ephemeral_memory: Dict[str, Dict[str, Any]] = {}
        self._ephemeral_memory_lock = asyncio.Lock()
        self._ephemeral_memory_ttl = timedelta(hours=2)
        
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
                    logger.warning(
                        "⚠️ MemoryAnalyzer disabled (optional): reason=%s; fallback=heuristic",
                        e,
                    )
                    self.memory_analyzer = None
            else:
                logger.info(
                    "MemoryAnalyzer disabled (optional): missing API key or invalid config; fallback=heuristic"
                )
            
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
        if not hardware_id:
            return {}
        
        try:
            db_short = ""
            db_long = ""
            if self.db_manager:
                memory_data = await asyncio.wait_for(
                    self.db_manager.get_user_memory(hardware_id),
                    timeout=self.config.memory_timeout
                )
                db_short = (memory_data or {}).get('short', '') or ""
                db_long = (memory_data or {}).get('long', '') or ""

            ephemeral = await self._get_ephemeral_memory(hardware_id)
            eph_short = (ephemeral or {}).get("short", "")
            eph_long = (ephemeral or {}).get("long", "")

            short_value = db_short or eph_short
            long_value = db_long or eph_long

            if short_value or long_value:
                return {
                    "recent_context": short_value,
                    "long_term_context": long_value,
                    "formatted_prompt": f"""
🧠 MEMORY CONTEXT (for response context):

📋 SHORT-TERM MEMORY (current session):
{short_value or 'No short-term memory'}

📚 LONG-TERM MEMORY (user information):
{long_value or 'No long-term memory'}

💡 MEMORY USAGE INSTRUCTIONS:
- Use short-term memory to understand current conversation context
- Use long-term memory for response personalization
- Memory should complement the answer, not replace it
"""
                }
            logger.info(f"🧠 No memory found for {hardware_id}")
            return ""
                    
        except asyncio.TimeoutError:
            logger.warning(f"⚠️ Memory retrieval timeout for {hardware_id}")
            fallback = await self._get_ephemeral_memory(hardware_id)
            if fallback:
                return {
                    "recent_context": fallback.get("short", ""),
                    "long_term_context": fallback.get("long", ""),
                }
            return ""
        except Exception as e:
            logger.error(f"❌ Error getting memory context for {hardware_id}: {e}")
            fallback = await self._get_ephemeral_memory(hardware_id)
            if fallback:
                return {
                    "recent_context": fallback.get("short", ""),
                    "long_term_context": fallback.get("long", ""),
                }
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

            # Стандартизуем short-term память как компактный chat-summary.
            short_memory = self._build_recent_chat_summary(
                prompt=prompt,
                response=response,
                analyzer_short_memory=short_memory,
            )

            if not short_memory and not long_memory:
                logger.debug(f"🧠 No information found for {hardware_id} to remember")
                return None

            if self.db_manager:
                success = await self.db_manager.update_user_memory(
                    hardware_id,
                    short_memory,
                    long_memory
                )
                if success:
                    await self._store_ephemeral_memory(hardware_id, short_memory, long_memory)
                    logger.info(
                        f"✅ Memory for {hardware_id} updated: short-term ({len(short_memory)} chars), long-term ({len(long_memory)} chars)"
                    )
                    return {"short": short_memory, "long": long_memory}

                logger.warning(f"⚠️ Could not update memory for {hardware_id}")
            else:
                logger.warning("⚠️ DatabaseManager is not set in MemoryManager; using ephemeral short-term memory fallback")

            await self._store_ephemeral_memory(hardware_id, short_memory, long_memory)
            return {"short": short_memory, "long": long_memory}
                
        except Exception as e:
            logger.error(f"❌ Error in background memory update for {hardware_id}: {e}")
            # НЕ поднимаем исключение - это фоновая задача
            return None

    def _build_recent_chat_summary(
        self,
        prompt: str,
        response: str,
        analyzer_short_memory: str = "",
    ) -> str:
        """
        Builds a compact chat-style memory snippet.
        Stores only essential dialogue summary, not raw full text.
        """
        user_summary = self._sanitize_memory_text(prompt, max_chars=140)
        assistant_summary = self._sanitize_memory_text(response, max_chars=140)
        analyzer_note = self._sanitize_memory_text(analyzer_short_memory, max_chars=120)

        if not user_summary and not assistant_summary and not analyzer_note:
            return ""

        lines = ["Recent chat summary:"]
        if user_summary:
            lines.append(f"- User: {user_summary}")
        if assistant_summary:
            lines.append(f"- Assistant: {assistant_summary}")
        if analyzer_note and analyzer_note.lower() not in (user_summary or "").lower():
            lines.append(f"- Context: {analyzer_note}")
        return "\n".join(lines)

    @staticmethod
    def _sanitize_memory_text(text: str, max_chars: int) -> str:
        if not text:
            return ""
        compact = " ".join(str(text).strip().split())
        if not compact:
            return ""

        # Never keep raw secrets in memory snippet.
        secret_pattern = re.compile(
            r"\b(password\w*|парол\w*|token\w*|токен\w*|api[_ -]?key|ключ\w*)\b",
            flags=re.IGNORECASE,
        )
        if secret_pattern.search(compact):
            return "Sensitive credentials were mentioned"

        if len(compact) > max_chars:
            return compact[: max_chars - 3].rstrip() + "..."
        return compact

    async def _store_ephemeral_memory(self, hardware_id: str, short_memory: str, long_memory: str) -> None:
        if not hardware_id:
            return
        async with self._ephemeral_memory_lock:
            self._cleanup_expired_ephemeral_locked()
            self._ephemeral_memory[hardware_id] = {
                "short": short_memory or "",
                "long": long_memory or "",
                "updated_at": datetime.now(timezone.utc),
            }

    async def _get_ephemeral_memory(self, hardware_id: str) -> Optional[Dict[str, str]]:
        if not hardware_id:
            return None
        async with self._ephemeral_memory_lock:
            self._cleanup_expired_ephemeral_locked()
            entry = self._ephemeral_memory.get(hardware_id)
            if not entry:
                return None
            return {
                "short": entry.get("short", "") or "",
                "long": entry.get("long", "") or "",
            }

    def _cleanup_expired_ephemeral_locked(self) -> None:
        now = datetime.now(timezone.utc)
        expired = []
        for hardware_id, payload in self._ephemeral_memory.items():
            updated_at = payload.get("updated_at")
            if not isinstance(updated_at, datetime):
                expired.append(hardware_id)
                continue
            if (now - updated_at) > self._ephemeral_memory_ttl:
                expired.append(hardware_id)
        for hardware_id in expired:
            self._ephemeral_memory.pop(hardware_id, None)
    
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
