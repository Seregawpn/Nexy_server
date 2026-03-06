"""
Memory Manager - single owner for memory read/write/merge.

Responsibilities:
- build rolling short-term timeline for follow-up continuity;
- maintain medium-term digest with retention/rollup guards;
- merge factual long-term memory without creating duplicate owners;
- persist DB snapshot and keep ephemeral fallback in sync.
"""

import asyncio
import json
import logging
import re
from datetime import datetime, timedelta, timezone
from typing import Any, Dict, Optional, Tuple, Union

from ..config import MemoryConfig
from ..providers.memory_analyzer import MemoryAnalyzer

logger = logging.getLogger(__name__)

_CLEAR_LONG_TERM_MARKER = "__CLEAR_LONG_TERM__"


class MemoryManager:
    """Single owner for memory extraction, merge and storage."""

    _MEMORY_KEYWORD_PATTERN = re.compile(
        r"\b("
        r"remember|memory|memories|previous|earlier|before|discussed|discuss|recall|"
        r"what did we|what were we|what do you remember|my name|how am i called|"
        r"помни|помнишь|запомни|вспомни|раньше|ранее|обсуждали|говорили|"
        r"что ты помнишь|как меня зовут|как меня зовут\??"
        r")\b",
        flags=re.IGNORECASE,
    )
    _SECRET_PATTERN = re.compile(
        r"\b(password\w*|парол\w*|token\w*|токен\w*|api[_ -]?key|ключ\w*)\b",
        flags=re.IGNORECASE,
    )
    _NAME_PATTERNS = [
        re.compile(r"\bmy name is\s+([a-zа-яё][a-zа-яё\-']+)", flags=re.IGNORECASE),
        re.compile(r"\bi am\s+([a-zа-яё][a-zа-яё\-']+)", flags=re.IGNORECASE),
        re.compile(r"\bi'm\s+([a-zа-яё][a-zа-яё\-']+)", flags=re.IGNORECASE),
        re.compile(r"\bменя зовут\s+([a-zа-яё][a-zа-яё\-']+)", flags=re.IGNORECASE),
        re.compile(r"\bмое имя\s+([a-zа-яё][a-zа-яё\-']+)", flags=re.IGNORECASE),
        re.compile(r"\bмоё имя\s+([a-zа-яё][a-zа-яё\-']+)", flags=re.IGNORECASE),
    ]
    _PREFERENCE_PATTERNS = [
        re.compile(r"\bi love\s+([^.!?\n]+)", flags=re.IGNORECASE),
        re.compile(r"\bi like\s+([^.!?\n]+)", flags=re.IGNORECASE),
        re.compile(r"\bmy favorite\s+([^.!?\n]+)", flags=re.IGNORECASE),
        re.compile(r"\bя люблю\s+([^.!?\n]+)", flags=re.IGNORECASE),
        re.compile(r"\bмой любим(?:ый|ая|ое|ые)\s+([^.!?\n]+)", flags=re.IGNORECASE),
    ]

    def __init__(self, db_manager=None, token_usage_tracker=None):
        self.config = MemoryConfig()
        self.db_manager = db_manager
        self.token_usage_tracker = token_usage_tracker
        self.memory_analyzer = None
        self.is_initialized = False

        self._ephemeral_memory: Dict[str, Dict[str, Any]] = {}
        self._ephemeral_memory_lock = asyncio.Lock()
        self._ephemeral_memory_ttl = timedelta(hours=2)

        self._user_locks: Dict[str, asyncio.Lock] = {}
        self._user_locks_guard = asyncio.Lock()

        self._max_previous_turns = 4
        self._medium_rollup_interval = timedelta(hours=24)
        self._medium_term_retention = timedelta(days=30)

    async def initialize(self):
        """Initialize optional analyzer; manager itself stays available without it."""
        try:
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
            logger.error("❌ MemoryManager initialization failed: %s", e)
            raise

    def set_database_manager(self, db_manager):
        self.db_manager = db_manager
        logger.info("✅ DatabaseManager set in MemoryManager")

    def set_medium_term_retention(self, days: int = 30, seconds: Optional[int] = None) -> None:
        if seconds is not None and int(seconds) > 0:
            self._medium_term_retention = timedelta(seconds=int(seconds))
            return
        self._medium_term_retention = timedelta(days=max(int(days), 1))

    def set_medium_term_rollup_interval(self, seconds: int) -> None:
        self._medium_rollup_interval = timedelta(seconds=max(int(seconds), 1))

    def should_include_medium_term(self, user_input: Optional[str]) -> Tuple[bool, str]:
        text = str(user_input or "").strip()
        if not text:
            return False, "none"
        if self._MEMORY_KEYWORD_PATTERN.search(text):
            return True, "keyword"
        return False, "none"

    async def get_memory_context(
        self,
        hardware_id: str,
        user_input: Optional[str] = None,
        apply_medium_gate: bool = True,
    ) -> Union[Dict[str, Any], str]:
        if not hardware_id:
            return self._empty_memory_context(
                user_input=user_input,
                apply_medium_gate=apply_medium_gate,
            )

        try:
            snapshot = await self._load_snapshot(hardware_id)
            if not snapshot:
                return self._empty_memory_context(
                    user_input=user_input,
                    apply_medium_gate=apply_medium_gate,
                )

            return self._build_memory_context_response(
                snapshot,
                user_input=user_input,
                apply_medium_gate=apply_medium_gate,
            )
        except Exception as e:
            logger.error("❌ Error getting memory context for %s: %s", hardware_id, e)
            fallback = await self._get_ephemeral_snapshot(hardware_id)
            if not fallback:
                return self._empty_memory_context(
                    user_input=user_input,
                    apply_medium_gate=apply_medium_gate,
                )
            return self._build_memory_context_response(
                fallback,
                user_input=user_input,
                apply_medium_gate=apply_medium_gate,
            )

    async def analyze_conversation(
        self,
        prompt: str,
        response: str,
        hardware_id: Optional[str] = None,
    ) -> Tuple[str, str, str]:
        if not self.memory_analyzer:
            logger.debug("🧠 MemoryAnalyzer not available - using heuristic memory extraction")
            return self._extract_memory_heuristic(prompt, response)

        try:
            analyzed = await self.memory_analyzer.analyze_conversation(
                prompt,
                response,
                hardware_id=hardware_id,
            )
            return self._normalize_analysis_result(analyzed)
        except Exception as e:
            logger.error("❌ Error analyzing conversation: %s", e)
            return self._extract_memory_heuristic(prompt, response)

    def _normalize_analysis_result(self, analyzed: Any) -> Tuple[str, str, str]:
        if not isinstance(analyzed, tuple):
            return "", "", ""
        if len(analyzed) >= 3:
            return (
                str(analyzed[0] or ""),
                str(analyzed[1] or ""),
                str(analyzed[2] or ""),
            )
        if len(analyzed) == 2:
            return str(analyzed[0] or ""), "", str(analyzed[1] or "")
        if len(analyzed) == 1:
            return str(analyzed[0] or ""), "", ""
        return "", "", ""

    def _extract_memory_heuristic(self, prompt: str, response: str) -> Tuple[str, str, str]:
        text = (prompt or "").strip()
        if not text:
            return "", "", ""

        normalized = text.lower()
        remember_intent = bool(
            re.search(
                r"\b(запомни|запомни это|не забудь|remember this|remember that|keep (this|that) in mind)\b",
                normalized,
            )
        )

        short_memory = "User explicitly asked to remember this information" if remember_intent else ""
        medium_memory = self._build_medium_entry_text(prompt, response, "")

        long_parts: list[str] = []

        for pattern in self._NAME_PATTERNS:
            match = pattern.search(text)
            if match:
                long_parts.append(f"User name: {match.group(1).strip()}")
                break

        for pattern in self._PREFERENCE_PATTERNS:
            match = pattern.search(text)
            if match:
                candidate = match.group(1).strip(" ,;:.")
                if candidate and not self._SECRET_PATTERN.search(candidate):
                    long_parts.append(f"User prefers {candidate}")
                break

        if self._SECRET_PATTERN.search(text):
            # Sensitive data must never reach long-term storage.
            long_parts = [part for part in long_parts if "credentials" not in part.lower()]

        long_memory = self._join_unique_clauses(long_parts)
        return short_memory, medium_memory, long_memory

    async def update_memory_background(self, hardware_id: str, prompt: str, response: str) -> Optional[Dict[str, str]]:
        try:
            lock = await self._get_user_lock(hardware_id)
            async with lock:
                existing = await self._load_snapshot(hardware_id)
                short_note, medium_candidate, long_candidate = await self.analyze_conversation(
                    prompt,
                    response,
                    hardware_id=hardware_id,
                )
                now = datetime.now(timezone.utc)

                current_turn = self._build_turn_entry(prompt, response, short_note, now)
                previous_turns = self._build_previous_turns(existing, current_turn)
                medium_value = self._merge_medium(existing, prompt, response, medium_candidate, now)
                factual_long = self._merge_long_term(existing, long_candidate, prompt)

                snapshot = {
                    "schema": "memory_v2",
                    "updated_at": now.isoformat(),
                    "short_current": current_turn,
                    "short_previous": previous_turns,
                    "medium": medium_value,
                    "factual_long": factual_long,
                }
                short_blob = json.dumps(snapshot, ensure_ascii=True)

                if self.db_manager:
                    success = await self.db_manager.update_user_memory(
                        hardware_id,
                        short_blob,
                        factual_long,
                    )
                    if not success:
                        logger.warning("⚠️ Could not update memory for %s", hardware_id)
                        return None
                else:
                    logger.warning(
                        "⚠️ DatabaseManager is not set in MemoryManager; using ephemeral short-term memory fallback"
                    )

                await self._store_ephemeral_snapshot(hardware_id, snapshot)
                rendered_short = self._render_short_term_context(snapshot)
                return {
                    "short_live": rendered_short,
                    "short": rendered_short,
                    "medium": medium_value,
                    "factual_long": factual_long,
                    "long": factual_long,
                }
        except Exception as e:
            logger.error("❌ Error in background memory update for %s: %s", hardware_id, e)
            return None

    def _build_turn_entry(
        self,
        prompt: str,
        response: str,
        short_note: str,
        now: datetime,
    ) -> Dict[str, str]:
        return {
            "time_utc": now.isoformat(),
            "user": self._sanitize_memory_text(prompt, max_chars=220),
            "assistant": self._sanitize_memory_text(response, max_chars=220),
            "context": self._sanitize_memory_text(short_note, max_chars=120),
        }

    def _build_previous_turns(
        self,
        existing: Optional[Dict[str, Any]],
        current_turn: Dict[str, str],
    ) -> list[Dict[str, str]]:
        previous: list[Dict[str, str]] = []
        if existing:
            prev_current = existing.get("short_current")
            if isinstance(prev_current, dict) and prev_current != current_turn:
                previous.append(prev_current)
            for item in existing.get("short_previous", []):
                if isinstance(item, dict):
                    previous.append(item)
        return previous[: self._max_previous_turns]

    def _merge_medium(
        self,
        existing: Optional[Dict[str, Any]],
        prompt: str,
        response: str,
        medium_candidate: str,
        now: datetime,
    ) -> str:
        existing_medium = self._prune_medium_term(str((existing or {}).get("medium", "") or ""))
        last_rollup = self._extract_latest_medium_timestamp(existing_medium)
        should_rollup = (not existing_medium) or (not last_rollup) or ((now - last_rollup) >= self._medium_rollup_interval)
        if not should_rollup:
            return existing_medium

        new_entry = self._build_medium_entry_text(prompt, response, medium_candidate, now)
        if not new_entry:
            return existing_medium

        entries = [new_entry]
        if existing_medium:
            entries.extend(
                segment.strip()
                for segment in existing_medium.split(" || ")
                if segment.strip()
            )
        return " || ".join(self._dedupe_preserve_order(entries))

    def _merge_long_term(
        self,
        existing: Optional[Dict[str, Any]],
        long_candidate: str,
        prompt: str,
    ) -> str:
        current_long = str((existing or {}).get("factual_long", "") or "")
        candidate = str(long_candidate or "").strip()

        if candidate == _CLEAR_LONG_TERM_MARKER:
            return ""

        # Heuristic identity extraction still runs when analyzer returns nothing or fails.
        heuristic_name = ""
        if not candidate:
            _, _, heuristic_name = self._extract_memory_heuristic(prompt, "")
            candidate = heuristic_name

        return self._join_unique_clauses(
            [clause for clause in [current_long, candidate] if clause]
        )

    async def _load_snapshot(self, hardware_id: str) -> Optional[Dict[str, Any]]:
        if not hardware_id:
            return None

        db_short = ""
        db_long = ""
        if self.db_manager:
            memory_data = await asyncio.wait_for(
                self.db_manager.get_user_memory(hardware_id),
                timeout=self.config.memory_timeout,
            )
            db_short = str((memory_data or {}).get("short", "") or "")
            db_long = str((memory_data or {}).get("long", "") or "")

        if db_short or db_long:
            parsed = self._parse_snapshot_blob(db_short, db_long)
            await self._store_ephemeral_snapshot(hardware_id, parsed)
            return parsed

        return await self._get_ephemeral_snapshot(hardware_id)

    def _parse_snapshot_blob(self, short_blob: str, long_blob: str) -> Dict[str, Any]:
        if short_blob:
            try:
                payload = json.loads(short_blob)
                if isinstance(payload, dict) and payload.get("schema") == "memory_v2":
                    return {
                        "schema": "memory_v2",
                        "updated_at": payload.get("updated_at", ""),
                        "short_current": payload.get("short_current") or {},
                        "short_previous": payload.get("short_previous") or [],
                        "medium": payload.get("medium", "") or "",
                        "factual_long": str(long_blob or payload.get("factual_long", "") or ""),
                    }
            except Exception:
                pass

        legacy_text = str(short_blob or "")
        return {
            "schema": "memory_v2",
            "updated_at": "",
            "short_current": {
                "time_utc": "",
                "user": self._sanitize_memory_text(legacy_text, max_chars=220),
                "assistant": "",
                "context": "",
            } if legacy_text else {},
            "short_previous": [],
            # Legacy short blobs historically acted as a shared recent+digest source.
            # Keep medium compatibility until old DB rows are migrated.
            "medium": legacy_text,
            "factual_long": str(long_blob or ""),
        }

    def _build_memory_context_response(
        self,
        snapshot: Dict[str, Any],
        user_input: Optional[str],
        apply_medium_gate: bool,
    ) -> Dict[str, Any]:
        short_term_context = self._render_short_term_context(snapshot)
        medium_term_context = self._prune_medium_term(snapshot.get("medium", ""))
        include_medium, gate_reason = self._resolve_medium_gate(
            user_input=user_input,
            apply_medium_gate=apply_medium_gate,
        )
        if not include_medium:
            medium_term_context = ""

        factual_long_term_context = str(snapshot.get("factual_long", "") or "")
        return {
            "short_term_context": short_term_context,
            "medium_term_context": medium_term_context,
            "factual_long_term_context": factual_long_term_context,
            "memory_gate": gate_reason,
            "formatted_prompt": (
                "🧠 MEMORY CONTEXT\n\n"
                f"Short-term memory:\n{short_term_context or 'No data'}\n\n"
                f"Medium-term memory:\n{medium_term_context or 'No data'}\n\n"
                f"Long-term memory:\n{factual_long_term_context or 'No data'}"
            ),
        }

    def _empty_memory_context(
        self,
        user_input: Optional[str],
        apply_medium_gate: bool,
    ) -> Dict[str, Any]:
        _, gate_reason = self._resolve_medium_gate(
            user_input=user_input,
            apply_medium_gate=apply_medium_gate,
        )
        return {
            "short_term_context": "",
            "medium_term_context": "",
            "factual_long_term_context": "",
            "memory_gate": gate_reason,
            "formatted_prompt": (
                "🧠 MEMORY CONTEXT\n\n"
                "Short-term memory:\nNo data\n\n"
                "Medium-term memory:\nNo data\n\n"
                "Long-term memory:\nNo data"
            ),
        }

    def _resolve_medium_gate(
        self,
        user_input: Optional[str],
        apply_medium_gate: bool,
    ) -> Tuple[bool, str]:
        if not apply_medium_gate:
            return True, "disabled"
        return self.should_include_medium_term(user_input)

    def _render_short_term_context(self, snapshot: Dict[str, Any]) -> str:
        sections: list[str] = []

        current = snapshot.get("short_current") or {}
        if isinstance(current, dict) and any(current.values()):
            sections.append(self._format_turn_block("CURRENT_TURN", current))

        for idx, item in enumerate(snapshot.get("short_previous", []) or [], start=1):
            if idx > self._max_previous_turns:
                break
            if isinstance(item, dict) and any(item.values()):
                sections.append(self._format_turn_block(f"PREVIOUS_TURN_{idx}", item))

        return "\n".join(part for part in sections if part).strip()

    def _format_turn_block(self, label: str, turn: Dict[str, Any]) -> str:
        lines = [f"{label}:"]
        if turn.get("time_utc"):
            lines.append(f"TIME_UTC: {turn['time_utc']}")
        if turn.get("user"):
            lines.append(f"USER: {turn['user']}")
        if turn.get("assistant"):
            lines.append(f"ASSISTANT: {turn['assistant']}")
        if turn.get("context"):
            lines.append(f"CONTEXT: {turn['context']}")
        return "\n".join(lines)

    def _build_medium_entry_text(
        self,
        prompt: str,
        response: str,
        medium_candidate: str,
        now: Optional[datetime] = None,
    ) -> str:
        now = now or datetime.now(timezone.utc)
        user_text = self._sanitize_memory_text(prompt, max_chars=120)
        assistant_text = self._sanitize_memory_text(response, max_chars=120)
        summary = self._sanitize_memory_text(medium_candidate, max_chars=160)
        parts = [f"[{now.strftime('%Y-%m-%d')}]", f"time_utc={now.isoformat()}"]
        if user_text:
            parts.append(f"user_intent={user_text}")
        if assistant_text:
            parts.append(f"assistant_outcome={assistant_text}")
        if summary:
            parts.append(f"summary={summary}")
        parts.append("status=done")
        return "; ".join(parts)

    def _prune_medium_term(self, medium_blob: str) -> str:
        if not medium_blob:
            return ""
        cutoff = datetime.now(timezone.utc) - self._medium_term_retention
        kept: list[str] = []
        for segment in str(medium_blob).split(" || "):
            item = segment.strip()
            if not item:
                continue
            time_match = re.search(r"time_utc=([^;]+)", item)
            if not time_match:
                kept.append(item)
                continue
            try:
                ts = datetime.fromisoformat(time_match.group(1))
                if ts.tzinfo is None:
                    ts = ts.replace(tzinfo=timezone.utc)
            except Exception:
                kept.append(item)
                continue
            if ts >= cutoff:
                kept.append(item)
        return " || ".join(kept)

    def _extract_latest_medium_timestamp(self, medium_blob: str) -> Optional[datetime]:
        if not medium_blob:
            return None
        first = str(medium_blob).split(" || ", 1)[0].strip()
        if not first:
            return None
        match = re.search(r"time_utc=([^;]+)", first)
        if not match:
            return None
        try:
            ts = datetime.fromisoformat(match.group(1))
            if ts.tzinfo is None:
                ts = ts.replace(tzinfo=timezone.utc)
            return ts
        except Exception:
            return None

    async def _get_user_lock(self, hardware_id: str) -> asyncio.Lock:
        async with self._user_locks_guard:
            lock = self._user_locks.get(hardware_id)
            if lock is None:
                lock = asyncio.Lock()
                self._user_locks[hardware_id] = lock
            return lock

    async def _store_ephemeral_snapshot(self, hardware_id: str, snapshot: Dict[str, Any]) -> None:
        if not hardware_id:
            return
        async with self._ephemeral_memory_lock:
            self._cleanup_expired_ephemeral_locked()
            self._ephemeral_memory[hardware_id] = {
                "snapshot": snapshot,
                "updated_at": datetime.now(timezone.utc),
            }

    async def _get_ephemeral_snapshot(self, hardware_id: str) -> Optional[Dict[str, Any]]:
        if not hardware_id:
            return None
        async with self._ephemeral_memory_lock:
            self._cleanup_expired_ephemeral_locked()
            entry = self._ephemeral_memory.get(hardware_id)
            if not entry:
                return None
            snapshot = entry.get("snapshot")
            return dict(snapshot) if isinstance(snapshot, dict) else None

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

    async def cleanup_inactive_short_term_cache(self, hours: int = 1) -> int:
        threshold = timedelta(hours=max(int(hours), 1))
        removed = 0
        async with self._ephemeral_memory_lock:
            now = datetime.now(timezone.utc)
            to_remove = []
            for hardware_id, payload in self._ephemeral_memory.items():
                updated_at = payload.get("updated_at")
                if not isinstance(updated_at, datetime) or (now - updated_at) > threshold:
                    to_remove.append(hardware_id)
            for hardware_id in to_remove:
                self._ephemeral_memory.pop(hardware_id, None)
                removed += 1
        return removed

    @staticmethod
    def _sanitize_memory_text(text: str, max_chars: int) -> str:
        if not text:
            return ""
        compact = " ".join(str(text).strip().split())
        if not compact:
            return ""
        if MemoryManager._SECRET_PATTERN.search(compact):
            return "Sensitive credentials were mentioned"
        if len(compact) > max_chars:
            return compact[: max_chars - 3].rstrip() + "..."
        return compact

    @staticmethod
    def _join_unique_clauses(parts: list[str]) -> str:
        seen: set[str] = set()
        unique: list[str] = []
        for part in parts:
            for clause in str(part).split(";"):
                cleaned = clause.strip()
                if not cleaned:
                    continue
                key = cleaned.lower()
                if key in seen:
                    continue
                seen.add(key)
                unique.append(cleaned)
        return "; ".join(unique)

    @staticmethod
    def _dedupe_preserve_order(items: list[str]) -> list[str]:
        seen: set[str] = set()
        unique: list[str] = []
        for item in items:
            key = item.strip().lower()
            if not key or key in seen:
                continue
            seen.add(key)
            unique.append(item.strip())
        return unique

    def is_available(self) -> bool:
        return self.db_manager is not None or self.memory_analyzer is not None

    async def cleanup_expired_memory(self, hours: int = 24) -> int:
        if not self.db_manager:
            return 0
        try:
            return await self.db_manager.cleanup_expired_short_term_memory(hours)
        except Exception as e:
            logger.error("❌ Error cleaning up expired memory: %s", e)
            return 0
