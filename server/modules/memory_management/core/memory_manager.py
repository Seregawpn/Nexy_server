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
        self._persistent_memory_cache: Dict[str, Dict[str, Any]] = {}
        self._persistent_memory_lock = asyncio.Lock()
        self._persistent_memory_ttl = timedelta(minutes=5)
        self._persistent_memory_max_entries = 2000
        self._user_update_locks: Dict[str, asyncio.Lock] = {}
        self._user_update_lock_last_used: Dict[str, datetime] = {}
        self._user_update_lock_ttl = timedelta(minutes=30)
        self._user_update_lock_max_entries = 2000
        self._user_update_locks_guard = asyncio.Lock()

    _MEDIUM_TERM_KEYWORDS = (
        "remember",
        "recall",
        "remind me",
        "what is my name",
        "what's my name",
        "как меня зовут",
        "мое имя",
        "моё имя",
        "what did i say",
        "what we discussed",
        "last time",
        "previously",
        "earlier",
        "as before",
        "that one",
        "the one i chose",
        "last week",
        "last month",
    )
    _LONG_TERM_CLEAR_MARKER = "__CLEAR_LONG_TERM__"
    _IDENTITY_FACT_PATTERNS = (
        re.compile(r"\bменя\s+зовут\s+([a-zA-Zа-яА-ЯёЁ][a-zA-Zа-яА-ЯёЁ' -]{0,48})\b", re.IGNORECASE),
        re.compile(r"\bmy\s+name\s+is\s+([a-zA-Z][a-zA-Z' -]{0,48})\b", re.IGNORECASE),
        re.compile(r"\bмо[её]\s+имя\s*[:\-]?\s*([a-zA-Zа-яА-ЯёЁ][a-zA-Zа-яА-ЯёЁ' -]{0,48})\b", re.IGNORECASE),
    )
        
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

    async def invalidate_persistent_memory_cache(self, hardware_id: Optional[str] = None) -> None:
        """
        Explicit cache invalidation hook.
        Useful for multi-instance deployments where another instance may update DB state.
        """
        async with self._persistent_memory_lock:
            if hardware_id:
                self._persistent_memory_cache.pop(hardware_id, None)
                logger.debug("🧠 MEMORY_CACHE invalidated hardware_id=%s", hardware_id)
                return
            self._persistent_memory_cache.clear()
            logger.debug("🧠 MEMORY_CACHE invalidated all entries")
    
    async def get_memory_context(
        self,
        hardware_id: str,
        user_input: Optional[str] = None,
    ) -> Union[Dict[str, Any], str]:
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
            snapshot = await self._get_persistent_memory_snapshot(hardware_id)
            db_short = snapshot.get("medium", "")
            db_long = snapshot.get("long", "")

            ephemeral = await self._get_ephemeral_memory(hardware_id)
            eph_short = (ephemeral or {}).get("short", "")
            eph_long = (ephemeral or {}).get("long", "")

            short_term_value = self._trim_memory_text(
                eph_short,
                self.config.max_short_term_memory_size,
            )
            medium_term_raw = self._trim_memory_text(
                db_short,
                self.config.max_short_term_memory_size,
            )
            factual_long_term_value = self._trim_memory_text(
                db_long or eph_long,
                self.config.max_long_term_memory_size,
            )
            include_medium_term, gate_reason = self._should_include_medium_term(user_input)
            medium_term_value = medium_term_raw if include_medium_term else ""

            # Backward-compatible alias: old consumers use recent_context.
            recent_value = short_term_value or medium_term_value

            if short_term_value or medium_term_value or factual_long_term_value:
                return {
                    "short_term_context": short_term_value,
                    "medium_term_context": medium_term_value,
                    "factual_long_term_context": factual_long_term_value,
                    "recent_context": recent_value,
                    "long_term_context": factual_long_term_value,
                    "memory_gate": gate_reason,
                    "formatted_prompt": f"""
🧠 MEMORY CONTEXT (for response context):

📋 SHORT-TERM MEMORY (current session, live):
{short_term_value or 'No short-term memory'}

🗂️ MEDIUM-TERM MEMORY (conversation history, intent-gated):
{medium_term_value or 'No medium-term memory for this request'}

📚 FACTUAL LONG-TERM MEMORY (user profile):
{factual_long_term_value or 'No factual long-term memory'}

💡 MEMORY USAGE INSTRUCTIONS:
- Use short-term memory for current conversational continuity
- Use medium-term memory only when user references prior conversations
- Use factual long-term memory for personalization
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
                    "short_term_context": fallback.get("short", ""),
                    "medium_term_context": "",
                    "factual_long_term_context": fallback.get("long", ""),
                    "recent_context": fallback.get("short", ""),
                    "long_term_context": fallback.get("long", ""),
                    "memory_gate": "timeout_fallback",
                }
            return ""
        except Exception as e:
            logger.error(f"❌ Error getting memory context for {hardware_id}: {e}")
            fallback = await self._get_ephemeral_memory(hardware_id)
            if fallback:
                return {
                    "short_term_context": fallback.get("short", ""),
                    "medium_term_context": "",
                    "factual_long_term_context": fallback.get("long", ""),
                    "recent_context": fallback.get("short", ""),
                    "long_term_context": fallback.get("long", ""),
                    "memory_gate": "error_fallback",
                }
            return ""
    
    async def analyze_conversation(
        self,
        prompt: str,
        response: str,
        hardware_id: Optional[str] = None,
        existing_short_memory: str = "",
        existing_medium_memory: str = "",
        existing_long_memory: str = "",
    ) -> Tuple[str, str, str]:
        """
        Анализирует диалог для извлечения памяти.
        
        Args:
            prompt: Запрос пользователя
            response: Ответ ассистента
            hardware_id: ID устройства для трекинга (опционально)
            
        Returns:
            Кортеж (short_memory, medium_memory, long_memory)
            
        Этот метод заменяет вызов memory_analyzer.analyze_conversation()
        """
        if not self.memory_analyzer:
            logger.debug("🧠 MemoryAnalyzer not available - using heuristic memory extraction")
            return self._extract_memory_heuristic(prompt, response)
        
        try:
            return await self.memory_analyzer.analyze_conversation(
                prompt,
                response,
                hardware_id=hardware_id,
                existing_short_memory=existing_short_memory,
                existing_medium_memory=existing_medium_memory,
                existing_long_memory=existing_long_memory,
            )
        except Exception as e:
            logger.error(f"❌ Error analyzing conversation: {e}")
            return "", "", ""

    def _extract_memory_heuristic(self, prompt: str, response: str) -> Tuple[str, str, str]:
        """
        Lightweight fallback extraction when Gemini analyzer is unavailable.

        Keeps one owner-path for memory updates and avoids "no-op memory" in runtime.
        """
        try:
            text = (prompt or "").strip()
            if not text:
                return "", "", ""

            normalized = text.lower()

            long_candidates: list[str] = []

            # Deterministic identity extraction to avoid name loss when analyzer misses.
            identity_facts = self._extract_identity_facts(prompt)
            long_candidates.extend(identity_facts)

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
                        long_candidates.append(f"User prefers {fact}")

            # Optional command-style fact extraction (non-blocking).
            if not long_candidates:
                remember_payload_patterns = [
                    r"(?:запомни(?: это)?[:\s-]*)([^.!?\n]+)",
                    r"(?:remember (?:this|that)[:\s-]*)([^.!?\n]+)",
                ]
                for pattern in remember_payload_patterns:
                    match = re.search(pattern, text, flags=re.IGNORECASE)
                    if match:
                        fact = match.group(1).strip(" ,;:.")
                        if fact:
                            long_candidates.append(f"Remembered fact: {fact}")
                            break

            if not long_candidates:
                short_live = self._sanitize_memory_text(prompt, max_chars=140)
                medium_memory = self._build_recent_chat_summary(prompt=prompt, response=response)
                return short_live, medium_memory, ""

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

            long_memory = "; ".join(unique)
            short_memory = self._sanitize_memory_text(prompt, max_chars=140)
            medium_memory = self._build_recent_chat_summary(
                prompt=prompt,
                response=response,
                analyzer_short_memory=short_memory,
            )
            return short_memory, medium_memory, long_memory
        except Exception as e:
            logger.warning(f"⚠️ Heuristic memory extraction failed: {e}")
            return "", "", ""

    def _extract_identity_facts(self, prompt: str) -> list[str]:
        """Extract stable identity facts (e.g. user name) from explicit user statements."""
        text = (prompt or "").strip()
        if not text:
            return []

        facts: list[str] = []
        for pattern in self._IDENTITY_FACT_PATTERNS:
            for match in pattern.finditer(text):
                raw_name = (match.group(1) or "").strip(" ,;:.!?\"'")
                if not raw_name:
                    continue
                # Keep only first two tokens to avoid capturing long clauses.
                tokens = [tok for tok in raw_name.split() if tok]
                if not tokens:
                    continue
                cleaned_name = " ".join(tokens[:2]).strip()
                if cleaned_name:
                    facts.append(f"User name: {cleaned_name}")

        # Deduplicate while preserving order.
        unique: list[str] = []
        seen: set[str] = set()
        for fact in facts:
            key = fact.lower()
            if key in seen:
                continue
            seen.add(key)
            unique.append(fact)
        return unique
    
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
            user_lock = await self._get_user_update_lock(hardware_id)
            async with user_lock:
                logger.debug("🔄 Starting background memory update for %s", hardware_id)
                ephemeral = await self._get_ephemeral_memory(hardware_id)
                existing_short = (ephemeral or {}).get("short", "") or ""
                snapshot = await self._get_persistent_memory_snapshot(hardware_id)
                existing_medium = snapshot.get("medium", "")
                existing_factual_long = snapshot.get("long", "")

                # Анализируем разговор для извлечения памяти
                short_memory, analyzer_medium_memory, long_memory = await self._analyze_for_update(
                    prompt=prompt,
                    response=response,
                    hardware_id=hardware_id,
                    existing_short_memory=existing_short,
                    existing_medium_memory=existing_medium,
                    existing_long_memory=existing_factual_long,
                )
                short_live_memory = self._trim_memory_text(
                    self._build_recent_chat_summary(
                        prompt=prompt,
                        response=response,
                        analyzer_short_memory=short_memory,
                    ),
                    self.config.max_short_term_memory_size,
                )

                # Medium-term from analyzer is primary; fallback to deterministic digest.
                medium_term_memory = analyzer_medium_memory or self._build_medium_term_digest(
                    prompt=prompt,
                    response=response,
                )
                medium_term_memory = self._trim_memory_text(
                    medium_term_memory,
                    self.config.max_short_term_memory_size,
                )
                new_factual_long_term = self._trim_memory_text(
                    long_memory,
                    self.config.max_long_term_memory_size,
                )
                # Full replace contract: each assistant response replaces the whole memory snapshot.
                replaced_medium = medium_term_memory
                replaced_factual_long = new_factual_long_term
                llm_requested_long_term_clear = (
                    replaced_factual_long.strip().upper() == self._LONG_TERM_CLEAR_MARKER
                )
                if llm_requested_long_term_clear:
                    replaced_factual_long = ""
                # Sticky-facts guard: do not drop previously established long-term facts
                # just because current turn has no new durable facts.
                if (
                    not replaced_factual_long
                    and existing_factual_long
                    and not llm_requested_long_term_clear
                ):
                    replaced_factual_long = self._trim_memory_text(
                        existing_factual_long,
                        self.config.max_long_term_memory_size,
                    )

                if self.db_manager:
                    success = await self.db_manager.update_user_memory(
                        hardware_id,
                        replaced_medium,
                        replaced_factual_long
                    )
                    if success:
                        await self._store_persistent_memory_snapshot(
                            hardware_id,
                            replaced_medium,
                            replaced_factual_long,
                        )
                        await self._store_ephemeral_memory(
                            hardware_id,
                            short_live_memory,
                            replaced_factual_long,
                        )
                        logger.info(
                            "✅ Memory for %s updated: mode=full_replace, medium-term (%s chars), factual long-term (%s chars), write_through_cache=true",
                            hardware_id,
                            len(replaced_medium),
                            len(replaced_factual_long),
                        )
                        return {
                            "medium": replaced_medium,
                            "factual_long": replaced_factual_long,
                            "short_live": short_live_memory,
                            # Backward-compatible aliases
                            "short": replaced_medium,
                            "long": replaced_factual_long,
                        }

                    logger.warning("⚠️ Could not update memory for %s", hardware_id)
                else:
                    logger.warning("⚠️ DatabaseManager is not set in MemoryManager; using ephemeral short-term memory fallback")
                    await self._store_persistent_memory_snapshot(
                        hardware_id,
                        replaced_medium,
                        replaced_factual_long,
                    )

                await self._store_ephemeral_memory(
                    hardware_id,
                    short_live_memory,
                    replaced_factual_long,
                )
                return {
                    "medium": replaced_medium,
                    "factual_long": replaced_factual_long,
                    "short_live": short_live_memory,
                    # Backward-compatible aliases
                    "short": replaced_medium,
                    "long": replaced_factual_long,
                }

        except Exception as e:
            logger.error(f"❌ Error in background memory update for {hardware_id}: {e}")
            # НЕ поднимаем исключение - это фоновая задача
            return None

    async def _analyze_for_update(
        self,
        prompt: str,
        response: str,
        hardware_id: str,
        existing_short_memory: str,
        existing_medium_memory: str,
        existing_long_memory: str,
    ) -> Tuple[str, str, str]:
        if not self.memory_analyzer:
            short_memory, medium_memory, long_memory = self._extract_memory_heuristic(prompt, response)
            return short_memory, medium_memory, long_memory
        try:
            short_memory, medium_memory, long_memory = await self.memory_analyzer.analyze_conversation(
                prompt,
                response,
                hardware_id=hardware_id,
                existing_short_memory=existing_short_memory,
                existing_medium_memory=existing_medium_memory,
                existing_long_memory=existing_long_memory,
            )
            return short_memory, medium_memory, long_memory
        except Exception as exc:
            logger.error("❌ Error analyzing conversation for memory update: %s", exc)
            return self._extract_memory_heuristic(prompt, response)

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

        lines = []
        if user_summary:
            lines.append(f"Current communication: {user_summary}")
        if assistant_summary or analyzer_note:
            progress_parts = []
            if assistant_summary:
                progress_parts.append(assistant_summary)
            if analyzer_note and analyzer_note.lower() not in (assistant_summary or "").lower():
                progress_parts.append(analyzer_note)
            lines.append(f"Progress: {'; '.join(progress_parts)}")
        lines.append("Previous communications:")
        previous_notes = self._extract_previous_communications(analyzer_short_memory)
        if previous_notes:
            for note in previous_notes:
                lines.append(f"- {note}")
        else:
            lines.append("- No relevant previous communication recorded.")
        return "\n".join(lines)

    def _build_medium_term_digest(self, prompt: str, response: str) -> str:
        """
        Builds compact cross-session digest format for medium-term memory.
        """
        topic = self._sanitize_memory_text(prompt, max_chars=120)
        outcome = self._sanitize_memory_text(response, max_chars=140)
        if not topic and not outcome:
            return ""
        if topic and outcome:
            line = f"Discussed {topic}; {outcome}."
        elif topic:
            line = f"Discussed {topic}; status noted."
        else:
            line = f"Discussed follow-up; {outcome}."
        current_date_utc = datetime.now(timezone.utc).strftime("%Y-%m-%d")
        return f"[{current_date_utc}] {line}"

    @staticmethod
    def _extract_previous_communications(analyzer_short_memory: str) -> list[str]:
        if not analyzer_short_memory:
            return []
        notes: list[str] = []
        for raw_line in str(analyzer_short_memory).splitlines():
            line = raw_line.strip()
            if not line:
                continue
            lowered = line.lower()
            if lowered.startswith("current communication:") or lowered.startswith("progress:"):
                continue
            if lowered.startswith("previous communications:"):
                continue
            if line.startswith("-"):
                line = line[1:].strip()
            if line:
                notes.append(line)
        deduped: list[str] = []
        seen: set[str] = set()
        for note in notes:
            key = note.lower()
            if key in seen:
                continue
            seen.add(key)
            deduped.append(note)
        return deduped[:5]

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
            logger.debug("🧠 SHORT_TERM replace hardware_id=%s chars=%s", hardware_id, len(short_memory or ""))

    async def _get_persistent_memory_snapshot(
        self,
        hardware_id: str,
        force_refresh: bool = False,
    ) -> Dict[str, str]:
        if not hardware_id:
            return {"medium": "", "long": ""}

        now = datetime.now(timezone.utc)
        cached_payload: Optional[Dict[str, Any]] = None

        async with self._persistent_memory_lock:
            self._cleanup_expired_persistent_locked(now)
            if not force_refresh:
                cached_payload = self._persistent_memory_cache.get(hardware_id)
                if cached_payload:
                    logger.debug("🧠 MEMORY_CACHE hit hardware_id=%s", hardware_id)
                    return {
                        "medium": cached_payload.get("medium", "") or "",
                        "long": cached_payload.get("long", "") or "",
                    }
                logger.debug("🧠 MEMORY_CACHE miss hardware_id=%s", hardware_id)

        if not self.db_manager:
            return {
                "medium": (cached_payload or {}).get("medium", "") or "",
                "long": (cached_payload or {}).get("long", "") or "",
            }

        try:
            memory_data = await asyncio.wait_for(
                self.db_manager.get_user_memory(hardware_id),
                timeout=self.config.memory_timeout,
            )
            medium = (memory_data or {}).get("short", "") or ""
            long_memory = (memory_data or {}).get("long", "") or ""
            await self._store_persistent_memory_snapshot(hardware_id, medium, long_memory, now=now)
            return {"medium": medium, "long": long_memory}
        except asyncio.TimeoutError:
            logger.warning("⚠️ Persistent memory retrieval timeout for %s", hardware_id)
        except Exception as exc:
            logger.error("❌ Error retrieving persistent memory snapshot for %s: %s", hardware_id, exc)

        async with self._persistent_memory_lock:
            fallback = self._persistent_memory_cache.get(hardware_id, {})
            return {
                "medium": fallback.get("medium", "") or "",
                "long": fallback.get("long", "") or "",
            }

    async def _store_persistent_memory_snapshot(
        self,
        hardware_id: str,
        medium_memory: str,
        long_memory: str,
        now: Optional[datetime] = None,
    ) -> None:
        if not hardware_id:
            return
        ts = now or datetime.now(timezone.utc)
        async with self._persistent_memory_lock:
            self._cleanup_expired_persistent_locked(ts)
            self._evict_if_needed_persistent_locked()
            self._persistent_memory_cache[hardware_id] = {
                "medium": medium_memory or "",
                "long": long_memory or "",
                "updated_at": ts,
            }

    def _cleanup_expired_persistent_locked(self, now: Optional[datetime] = None) -> None:
        check_time = now or datetime.now(timezone.utc)
        expired: list[str] = []
        for hardware_id, payload in self._persistent_memory_cache.items():
            updated_at = payload.get("updated_at")
            if not isinstance(updated_at, datetime):
                expired.append(hardware_id)
                continue
            if (check_time - updated_at) > self._persistent_memory_ttl:
                expired.append(hardware_id)
        for hardware_id in expired:
            self._persistent_memory_cache.pop(hardware_id, None)

    def _evict_if_needed_persistent_locked(self) -> None:
        if len(self._persistent_memory_cache) < self._persistent_memory_max_entries:
            return
        # Drop the oldest entry to keep bounded memory footprint.
        oldest_hardware_id: Optional[str] = None
        oldest_time: Optional[datetime] = None
        for hardware_id, payload in self._persistent_memory_cache.items():
            updated_at = payload.get("updated_at")
            if not isinstance(updated_at, datetime):
                oldest_hardware_id = hardware_id
                break
            if oldest_time is None or updated_at < oldest_time:
                oldest_hardware_id = hardware_id
                oldest_time = updated_at
        if oldest_hardware_id:
            self._persistent_memory_cache.pop(oldest_hardware_id, None)

    async def _get_user_update_lock(self, hardware_id: str) -> asyncio.Lock:
        async with self._user_update_locks_guard:
            self._cleanup_user_update_locks_locked()
            lock = self._user_update_locks.get(hardware_id)
            if lock is None:
                lock = asyncio.Lock()
                self._user_update_locks[hardware_id] = lock
            self._user_update_lock_last_used[hardware_id] = datetime.now(timezone.utc)
            return lock

    def _cleanup_user_update_locks_locked(self) -> None:
        now = datetime.now(timezone.utc)

        # Time-based cleanup for unused/unlocked locks.
        expired_keys: list[str] = []
        for hardware_id, lock in self._user_update_locks.items():
            last_used = self._user_update_lock_last_used.get(hardware_id)
            if lock.locked():
                continue
            if not isinstance(last_used, datetime):
                expired_keys.append(hardware_id)
                continue
            if (now - last_used) > self._user_update_lock_ttl:
                expired_keys.append(hardware_id)
        for hardware_id in expired_keys:
            self._user_update_locks.pop(hardware_id, None)
            self._user_update_lock_last_used.pop(hardware_id, None)

        # Size-based cleanup if many unique hardware ids were seen.
        if len(self._user_update_locks) <= self._user_update_lock_max_entries:
            return
        unlocked_candidates = [
            (hw_id, self._user_update_lock_last_used.get(hw_id))
            for hw_id, lock in self._user_update_locks.items()
            if not lock.locked()
        ]
        unlocked_candidates.sort(
            key=lambda item: item[1] if isinstance(item[1], datetime) else datetime.min.replace(tzinfo=timezone.utc)
        )
        idx = 0
        while len(self._user_update_locks) > self._user_update_lock_max_entries and idx < len(unlocked_candidates):
            hardware_id, _ = unlocked_candidates[idx]
            idx += 1
            self._user_update_locks.pop(hardware_id, None)
            self._user_update_lock_last_used.pop(hardware_id, None)

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

    def _should_include_medium_term(self, user_input: Optional[str]) -> Tuple[bool, str]:
        """
        Keyword-only intent gate for medium-term memory.
        If user_input is absent, default to compact mode (no medium-term).
        """
        if user_input is None:
            return False, "none"
        text = " ".join(str(user_input).lower().split())
        if not text:
            return False, "none"
        if any(keyword in text for keyword in self._MEDIUM_TERM_KEYWORDS):
            return True, "keyword"
        return False, "none"

    def should_include_medium_term(self, user_input: Optional[str]) -> Tuple[bool, str]:
        """
        Public wrapper for medium-term gate to keep a single owner for intent policy.
        """
        return self._should_include_medium_term(user_input)

    @staticmethod
    def _trim_memory_text(value: str, max_chars: int) -> str:
        if not value:
            return ""
        compact = " ".join(str(value).split())
        if len(compact) <= max_chars:
            return compact
        return compact[: max_chars - 3].rstrip() + "..."

    def is_available(self) -> bool:
        """
        Проверяет доступность модуля памяти.
        
        Returns:
            True если модуль готов к работе
        """
        return self.memory_analyzer is not None and self.db_manager is not None
    
    async def cleanup_expired_memory(self, hours: int = 24) -> int:
        """
        Очищает устаревшую persistent память в DB storage.
        
        Args:
            hours: Количество часов, после которых запись считается устаревшей
            
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
